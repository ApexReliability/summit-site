const { chromium } = require('playwright'); const path = require('path');
const dep = process.argv[2]; const fs = require('fs'); const fu = f => 'data:font/woff2;base64,' + fs.readFileSync(path.join(dep, 'fonts', f)).toString('base64');
const T = {
  fr: { eyebrow: 'Logiciel de fiabilité industrielle', a: "L'AMDEC qui pilote ", em: 'réellement', b: ' votre plan de maintenance.', sub: 'Ordres de travail reliés aux modes de défaillance · MTBF et MTTR · Priorisation par le risque' },
  en: { eyebrow: 'Industrial reliability software', a: 'The FMECA that ', em: 'actually', b: ' drives your maintenance plan.', sub: 'Work orders linked to failure modes · MTBF and MTTR · Risk-based prioritization' } };
const mark = '<svg viewBox="0 0 64 64" width="64" height="64" fill="none"><rect x="1" y="1" width="62" height="62" rx="10" stroke="#1F6E7E" stroke-width="2"/><path d="M8 50 L19 39 L26 44 L38 18 L46 31 L56 50" stroke="#FCC200" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/><circle cx="38" cy="18" r="4" fill="#F3F7F8"/></svg>';
const html = t => `<!doctype html><html><head><style>
@font-face{font-family:P;font-weight:400;src:url(${fu('ibm-plex-sans-latin-400-normal.woff2')})}
@font-face{font-family:P;font-weight:700;src:url(${fu('ibm-plex-sans-latin-700-normal.woff2')})}
@font-face{font-family:M;font-weight:500;src:url(${fu('ibm-plex-mono-latin-500-normal.woff2')})}
html,body{margin:0;width:1200px;height:630px;overflow:hidden}
body{background:#004F60;color:#F3F7F8;font-family:P;position:relative;
 background-image:linear-gradient(rgba(156,195,202,.07) 1px,transparent 1px),linear-gradient(90deg,rgba(156,195,202,.07) 1px,transparent 1px);background-size:48px 48px}
.in{position:absolute;inset:64px 72px}
.brand{display:flex;align-items:center;gap:16px;font-weight:700;font-size:34px}.brand span{font-family:M;font-size:18px;letter-spacing:.35em;color:#B9D6DB;font-weight:500}
.eb{margin-top:70px;font-family:M;font-weight:500;font-size:20px;letter-spacing:.18em;text-transform:uppercase;color:#FCC200}
h1{margin:18px 0 0;font-size:58px;line-height:1.12;font-weight:700;max-width:900px;letter-spacing:-.01em}h1 em{font-style:normal;color:#FCC200}
.sub{position:absolute;bottom:0;left:0;font-size:22px;color:#B9D6DB}
svg.tr{position:absolute;right:0;bottom:120px}
.url{position:absolute;top:8px;right:0;font-family:M;font-weight:500;font-size:18px;color:#B9D6DB;letter-spacing:.04em}
</style></head><body>
<svg class="tr" width="520" height="200" viewBox="0 0 520 200" fill="none"><path d="M0 170 L80 150 L130 160 L200 120 L250 135 L320 40 L360 95 L420 80 L520 110" stroke="rgba(79,179,193,.55)" stroke-width="3" stroke-linejoin="round"/><circle cx="320" cy="40" r="7" fill="#FCC200"/></svg>
<div class="in"><div class="brand">${mark}Summit<span>RMS</span></div><div class="url">summit-reliability.fr</div>
<div class="eb">${t.eyebrow}</div><h1>${t.a}<em>${t.em}</em>${t.b}</h1><div class="sub">${t.sub}</div></div></body></html>`;
(async () => { const b = await chromium.launch();
  for (const l of ['fr', 'en']) { const pg = await b.newPage({ viewport: { width: 1200, height: 630 } });
    await pg.setContent(html(T[l]), { waitUntil: 'load' }); await pg.evaluate(() => document.fonts.ready); await pg.waitForTimeout(300);
    await pg.screenshot({ path: path.join(dep, `og-${l}.png`) }); await pg.close(); }
  await b.close(); })();
