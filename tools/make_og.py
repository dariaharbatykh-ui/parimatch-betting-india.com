#!/usr/bin/env python3
"""Картинки для соцсетей 1200×630: заголовок страницы + её композиция первого экрана.
Запуск: python3 tools/make_og.py (нужен Google Chrome и запущенный node serve.mjs 8090)."""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import build  # noqa: E402

OUT_HTML = build.OUT / "_og"
OUT_IMG = build.SRC / "assets" / "img" / "og"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def main():
    OUT_HTML.mkdir(parents=True, exist_ok=True)
    OUT_IMG.mkdir(parents=True, exist_ok=True)
    css = f'/assets/style.css?v={build.asset_ver("style.css")}'
    pages = sorted((build.SRC / "pages").rglob("*.html"))
    for p in pages:
        slug = p.relative_to(build.SRC / "pages").with_suffix("").as_posix()
        if slug == "404":
            continue
        meta, _ = build.parse(p)
        h1 = build.tc(meta["h1"])
        art = build.hero_shot_html(slug, build.tc(meta["offer"]["title"]) if meta.get("offer") else "")
        name = slug.replace("/", "-")
        (OUT_HTML / f"{name}.html").write_text(f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<link rel="stylesheet" href="{css}"><style>
html,body{{margin:0;width:1200px;height:630px;overflow:hidden;background:#0b0b0b}}
.og{{position:relative;width:1200px;height:630px;display:grid;grid-template-columns:560px 580px;gap:20px;align-items:center;padding:0 40px;box-sizing:border-box;
background:radial-gradient(700px 380px at 90% -10%,rgba(238,245,26,.18),transparent 62%),#0b0b0b}}
.og h1{{font-size:50px;line-height:1.12;margin:18px 0 0}}
.og .logo{{font-size:1.4rem}}
.og .hero-art2{{width:580px}}
.og .bar{{position:absolute;left:0;right:0;bottom:0;height:8px;background:var(--y)}}
</style></head><body><div class="og"><div>{build.LOGO}<h1>{build.esc(h1)}</h1></div>{art}<span class="bar"></span></div></body></html>''', encoding="utf-8")
        png = OUT_HTML / f"{name}.png"
        subprocess.run(["perl", "-e", "alarm shift; exec @ARGV", "60", CHROME, "--headless=new", "--disable-gpu",
                        "--hide-scrollbars", "--no-first-run", f"--user-data-dir={OUT_HTML / 'prof'}",
                        "--window-size=1200,630", "--virtual-time-budget=6000", f"--screenshot={png}",
                        f"http://localhost:8090/_og/{name}.html"], capture_output=True)
        subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "82", str(png),
                        "--out", str(OUT_IMG / f"{name}.jpg")], capture_output=True)
        print(name, "ok" if (OUT_IMG / f"{name}.jpg").exists() else "FAIL")
    idx = OUT_IMG / "index.jpg"
    if idx.exists():
        (OUT_IMG / "default.jpg").write_bytes(idx.read_bytes())


if __name__ == "__main__":
    main()
