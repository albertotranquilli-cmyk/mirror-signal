#!/usr/bin/env python3
"""Step 1: fetch public mirror download stats.

Targets: npmmirror, tuna (Tsinghua), pypistats.
No keys. Cache under data/raw/.

Usage: python src/fetch_mirrors.py
"""
import json, os, time, urllib.request, urllib.error

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
RAW = os.path.join(ROOT, "data", "raw")

ENDPOINTS = {
    "tuna_status": "https://mirrors.tuna.tsinghua.edu.cn/static/json/status.json",
    "pypistats_requests": "https://pypistats.org/api/packages/requests/recent",
    # npmmirror binary listing (may be HTML; parser TBD after inspection)
    "npmmirror_binary": "https://registry.npmmirror.com/-/binary/",
}


def get(url, timeout=60):
    req = urllib.request.Request(url, headers={"User-Agent": "mirror-signal/0.1 (research)"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def main():
    os.makedirs(RAW, exist_ok=True)
    for name, url in ENDPOINTS.items():
        path = os.path.join(RAW, f"{name}.bin")
        print(f"get {name} ...", flush=True)
        try:
            b = get(url)
            open(path, "wb").write(b)
            print(f"  -> {len(b)} bytes")
            # try JSON
            try:
                data = json.loads(b)
                print(f"  -> JSON OK, top keys: {list(data)[:8] if isinstance(data, dict) else type(data).__name__}")
            except Exception:
                print(f"  -> not JSON (HTML or other), head: {b[:120]!r}")
        except Exception as e:
            print(f"  ERR {type(e).__name__}: {e}")
        time.sleep(2)
    print("done — inspect data/raw/ and write parse step")


if __name__ == "__main__":
    main()
