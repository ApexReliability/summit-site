# summit-reliability.fr

Website of Summit RMS, published with GitHub Pages from the root of the `main` branch.

- `index.html` is the French home page, `en/` the English page, `404.html` the page for unknown addresses.
- `fonts/` holds IBM Plex, served from the site itself (SIL Open Font License, see `fonts/OFL.txt`).
- `og-fr.png` and `og-en.png` are the link-preview images; `robots.txt` and `sitemap.xml` are for search engines.
- `source/` builds everything. All page text lives in `source/content.py`.

## Rebuild

```
cd source
python3 build.py out          # pages, preview and out/deploy/
node og.js out/deploy         # link-preview images (needs Playwright)
cp -r out/deploy/. ..         # copy the published files to the repo root
```

© 2026 Apex Reliability SRL
