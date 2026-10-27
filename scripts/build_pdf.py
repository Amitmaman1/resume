"""Render cv.html to a one-page A4 PDF with headless Chromium (Playwright)."""
import pathlib
import sys

from playwright.sync_api import sync_playwright

src = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "cv.html").resolve()
out = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else "dist/Amit Maman CV.pdf")
out.parent.mkdir(parents=True, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(src.as_uri(), wait_until="load")
    page.wait_for_timeout(1500)  # let web fonts settle
    page.pdf(path=str(out), format="A4", print_background=True, prefer_css_page_size=True)
    browser.close()

print(f"wrote {out}")
