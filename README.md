# Resume

`cv.html` is the single source of truth. A GitHub Actions workflow renders it to a one-page A4 PDF.

## Workflow
- **Push to `main`** that touches `cv.html`: builds the PDF (downloadable from the run's artifacts) and uploads it to Nextcloud if configured.
- **Push a tag** like `v1.1`: also creates a GitHub Release with the PDF attached. This is the version history.

```bash
git tag v1.1 && git push origin v1.1
```

## Build locally
```bash
pip install playwright && playwright install chromium
python scripts/build_pdf.py cv.html "dist/Amit Maman CV.pdf"
```

## Nextcloud upload (optional)
Add these repository secrets. Without `NEXTCLOUD_URL` the upload step is skipped.

| Secret | Purpose |
|---|---|
| `NEXTCLOUD_URL` | Base URL of the instance |
| `NEXTCLOUD_USER` | Nextcloud username |
| `NEXTCLOUD_APP_PASSWORD` | An app password, not the login password |
| `NEXTCLOUD_FOLDER` | Target folder (must already exist) |
| `NEXTCLOUD_CA_CERT` | Optional: internal CA certificate (PEM) |
| `TS_OAUTH_CLIENT_ID`, `TS_OAUTH_SECRET` | Tailscale OAuth client so the runner can reach a tailnet-only Nextcloud |

## LinkedIn
LinkedIn has no API for replacing a resume, so upload the PDF from the latest release by hand.
