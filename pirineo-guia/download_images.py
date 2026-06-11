#!/usr/bin/env python3
"""Descarga imágenes de Wikimedia a pirineo-guia/images/ para servir en la PWA."""
import time
import urllib.request
from pathlib import Path

from images_data import SITES  # noqa

OUT = Path(__file__).parent / "images"
UA = "PirineoGuia/1.0 (https://github.com/520520u/VIAJEPIRINEOS; educational)"


def download(url: str, dest: Path) -> bool:
    if dest.exists() and dest.stat().st_size > 1024:
        return True
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            dest.write_bytes(r.read())
        return True
    except Exception as e:
        print(f"  ERROR {dest.name}: {e}")
        return False


def main():
    OUT.mkdir(exist_ok=True)
    ok = 0
    for key, meta in SITES.items():
        url = meta["full"]
        ext = ".jpg"
        if url.lower().endswith(".jpeg"):
            ext = ".jpeg"
        elif url.lower().endswith(".png"):
            ext = ".png"
        dest = OUT / f"{key}{ext}"
        print(f"↓ {key}")
        if download(url, dest):
            ok += 1
        time.sleep(0.8)
    print(f"\nDescargadas: {ok}/{len(SITES)} → {OUT}")


if __name__ == "__main__":
    main()
