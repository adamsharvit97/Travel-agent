#!/usr/bin/env python3
"""
Latitude 43 — city-alerts signup server.

Stdlib HTTP server (plus openpyxl via subscribers.py). Serves the signup
page with the city list rendered from catalog/_hubs.json, and handles
POST /subscribe by upserting into deals/data/subscribers.xlsx.

    python3 server.py            # http://localhost:8043
    python3 server.py --port 80
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))

import subscribers  # noqa: E402
from latitude43_deals import load_hubs  # noqa: E402

INDEX_PATH = os.path.join(HERE, "index.html")


def city_label(hub: dict) -> str:
    """Mono sub-label: lead airport code, e.g. 'ORD'."""
    aps = hub.get("airports") or []
    return aps[0]["code"] if aps else ""


def render_index() -> bytes:
    hubs = load_hubs()
    options = []
    for slug, hub in hubs.items():
        options.append(
            f'<label class="city"><input type="checkbox" name="city" value="{slug}">'
            f'<span class="box"></span><span class="nm">{hub["city"]}</span>'
            f'<span class="ll">{city_label(hub)}</span></label>'
        )
    with open(INDEX_PATH, "r", encoding="utf-8") as fh:
        html = fh.read()
    return html.replace("{{CITY_OPTIONS}}", "\n      ".join(options)).encode("utf-8")


class Handler(BaseHTTPRequestHandler):
    server_version = "Latitude43/1.0"

    def _send(self, code: int, body: bytes, ctype: str) -> None:
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _json(self, code: int, payload: dict) -> None:
        self._send(code, json.dumps(payload).encode("utf-8"),
                   "application/json; charset=utf-8")

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            self._send(200, render_index(), "text/html; charset=utf-8")
        else:
            self._json(404, {"error": "not found"})

    def do_POST(self):
        if self.path != "/subscribe":
            self._json(404, {"error": "not found"})
            return
        try:
            length = int(self.headers.get("Content-Length", 0))
            data = json.loads(self.rfile.read(length) or b"{}")
            hubs = load_hubs()
            cities = [c for c in data.get("cities", []) if c in hubs]
            if not cities:
                self._json(400, {"error": "Pick at least one city."})
                return
            rec = subscribers.upsert(data.get("email", ""),
                                     data.get("name", ""), cities)
            rec["cities_pretty"] = [hubs[c]["city"] for c in rec["cities"]]
            self._json(200, rec)
        except ValueError as e:
            self._json(400, {"error": str(e)})
        except Exception:
            self._json(500, {"error": "Something went wrong at the desk."})

    def log_message(self, fmt, *args):
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))


def main(argv=None):
    p = argparse.ArgumentParser(description="Latitude 43 alerts signup server")
    p.add_argument("--port", type=int, default=8043)
    p.add_argument("--host", default="0.0.0.0")
    args = p.parse_args(argv)
    httpd = ThreadingHTTPServer((args.host, args.port), Handler)
    print(f"Latitude 43 alerts — http://localhost:{args.port}")
    httpd.serve_forever()


if __name__ == "__main__":
    raise SystemExit(main())
