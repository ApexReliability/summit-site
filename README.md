# summit-reliability.fr

Website of Summit RMS, published with GitHub Pages from the `docs/` folder.

- `docs/` is the published site: French home page, English page in `docs/en/`, 404 page, self-hosted IBM Plex fonts (SIL Open Font License, see `docs/fonts/OFL.txt`), sitemap and link-preview images.
- `source/` builds it. All page text lives in `source/content.py`.

## Rebuild

```
cd source
python3 build.py out          # pages, preview and out/deploy/
node og.js out/deploy         # link-preview images (needs Playwright)
rm -rf ../docs && cp -r out/deploy ../docs
```

© 2026 Apex Reliability SRL
