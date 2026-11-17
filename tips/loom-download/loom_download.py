#!/usr/bin/env python3
"""
Download a Loom video you recorded or have permission to save.

Only fetches videos your own Loom login (or a public share link) can already
play. It does not bypass any access control.

Usage:
    python3 loom_download.py <loom-share-url> [--browser chrome|safari|firefox|edge|brave] [-o output.mp4]

Strategy:
  1. Try yt-dlp (best quality, handles HLS/DASH). Uses your browser's cookies
     if --browser is given, so private/workspace videos you can view also work.
  2. Fall back to Loom's public "transcoded-url" endpoint (works for public shares).
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
import urllib.request


def video_id(url: str) -> str:
    m = re.search(r"loom\.com/(?:share|embed)/([0-9a-f]{32})", url)
    if not m:
        sys.exit(f"Could not find a Loom video ID in: {url}")
    return m.group(1)


def try_ytdlp(url: str, out: str, browser: str | None) -> bool:
    cmd = shutil.which("yt-dlp")
    if not cmd:
        print("yt-dlp not found (install with: pip install -U yt-dlp). Trying fallback...")
        return False
    args = [cmd, "-f", "bv*+ba/b", "--merge-output-format", "mp4", "-o", out, url]
    if browser:
        args[1:1] = ["--cookies-from-browser", browser]
    print("Running:", " ".join(args))
    return subprocess.run(args).returncode == 0


def try_loom_api(vid: str, out: str) -> bool:
    for endpoint in ("transcoded-url", "raw-url"):
        api = f"https://www.loom.com/api/campaigns/sessions/{vid}/{endpoint}"
        req = urllib.request.Request(
            api,
            data=b"{}",
            method="POST",
            headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"},
        )
        try:
            with urllib.request.urlopen(req) as r:
                link = json.load(r).get("url")
        except Exception as e:
            print(f"{endpoint}: {e}")
            continue
        if not link:
            continue
        print(f"Downloading via {endpoint} -> {out}")
        dl = urllib.request.Request(link, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(dl) as r, open(out, "wb") as f:
            total = int(r.headers.get("Content-Length") or 0)
            done = 0
            while chunk := r.read(1 << 20):
                f.write(chunk)
                done += len(chunk)
                if total:
                    print(f"\r  {done * 100 // total}%", end="", flush=True)
        print("\nDone.")
        return True
    return False


def main():
    p = argparse.ArgumentParser(description="Download a Loom video")
    p.add_argument("url")
    p.add_argument("-o", "--output", help="Output filename (default: loom_<id>.mp4)")
    p.add_argument("--browser", help="Browser to read login cookies from (chrome, safari, firefox, edge, brave)")
    a = p.parse_args()

    vid = video_id(a.url)
    out = a.output or f"loom_{vid}.mp4"

    if try_ytdlp(a.url, out, a.browser) or try_loom_api(vid, out):
        print(f"Saved: {out}")
    else:
        sys.exit("Download failed. If the video is private, re-run with --browser chrome "
                 "(while logged in to Loom in that browser).")


if __name__ == "__main__":
    main()
