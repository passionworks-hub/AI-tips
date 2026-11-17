# Back up your own Loom recordings as MP4 🎥

Loom's download button is not always available (it depends on your plan and on who owns the workspace). This small Python script saves a Loom video you have access to as a local `.mp4`, so you can archive it, edit it, or hand it to an AI tool for transcription and summarising.

- ✅ Zero tokens: plain Python, no model involved
- ✅ One file, standard library only ([`yt-dlp`](https://github.com/yt-dlp/yt-dlp) is optional but recommended)
- ✅ Works on macOS, Linux and Windows (Python 3.10+)

> **Use it responsibly.** Only download videos you recorded yourself or have the owner's permission to save. The script does not bypass any access control: it can only fetch a video your own Loom login (or a public share link) can already play. Check Loom's terms of service for your use case.

## Setup

```bash
# 1. Get the script
curl -O https://raw.githubusercontent.com/passionworks-hub/AI-tips/main/tips/loom-download/loom_download.py

# 2. Recommended: install yt-dlp for best quality
pip install -U yt-dlp
```

## Usage

```bash
# Public share link
python3 loom_download.py https://www.loom.com/share/<video-id>

# Private or workspace video you can view while logged in to Loom in Chrome
python3 loom_download.py https://www.loom.com/share/<video-id> --browser chrome

# Choose the output filename
python3 loom_download.py https://www.loom.com/share/<video-id> -o standup.mp4
```

| Flag | What it does |
|---|---|
| `--browser chrome` | Reads your Loom login cookies from that browser, so videos only you can view also work. Accepts `chrome`, `safari`, `firefox`, `edge`, `brave`. Needs `yt-dlp`. |
| `-o name.mp4` | Output filename. Defaults to `loom_<video-id>.mp4` in the current folder. |

## How it works

```
Loom share URL
      │
      ▼
Extract the 32-character video ID
      │
      ▼
Try yt-dlp (best quality, merges video + audio, can use browser cookies)
      │  not installed, or failed
      ▼
Fall back to the URL Loom's own share page uses to play the video
(public shares only)
      │
      ▼
Saved as loom_<video-id>.mp4
```

## Troubleshooting

| Problem | Fix |
|---|---|
| `Download failed` on a private video | Re-run with `--browser chrome` while logged in to Loom in that browser. |
| `yt-dlp not found` | `pip install -U yt-dlp`. Public videos still work without it through the fallback. |
| Safari cookies cannot be read (macOS) | Give your terminal Full Disk Access in System Settings, or use `--browser chrome`. |

Script: [`loom-download/loom_download.py`](loom-download/loom_download.py)
