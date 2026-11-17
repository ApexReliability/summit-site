# -*- coding: utf-8 -*-
import os, re, html, sys
sys.path.insert(0, os.path.dirname(__file__))
from content import FR, EN
OUT = sys.argv[1]
E = html.escape

def fr_typo(s):
    # espaces insécables avant : ; ? ! » et après «
    s = re.sub(r' ([:;?!»])', '&nbsp;\\1', s)
    return s.replace('« ', '«&nbsp;')

def T(L, s):
    s = E(s, quote=False)
    return fr_typo(s) if L['lang'] == 'fr' else s

CSS = r"""
/* Layout: teal hero band with product mock, then light sections on a 1160px column; identity Ridgeline (Apex teal + Golden Poppy, IBM Plex) */
:root{
  --bg:#F3F7F8; --surface:#FFFFFF; --raised:#E1ECEE; --line:#CFDEE1;
  --fg:#004F60; --fg2:#1F6E7E; --muted:#3D5F66;
  --action:#004F60; --on-action:#F3F7F8;
  --gold:#FCC200; --on-gold:#00303A; --mist:#9CC3CA;
  --hero:#004F60; --on-hero:#F3F7F8; --on-hero-2:#B9D6DB; --hero-line:#1F6E7E;
  --grid:rgba(156,195,202,.09); --trace:rgba(156,195,202,.55); --trace-2:rgba(156,195,202,.22); --gold-halo:rgba(252,194,0,.25);
  --sans:'IBM Plex Sans', 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
  --mono:'IBM Plex Mono', ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace;
}
@media (prefers-color-scheme: dark){ :root:not([data-theme="light"]){
  --bg:#071C22; --surface:#0D2A32; --raised:#143843; --line:#24525C;
  --fg:#E8F1F3; --fg2:#9CC3CA; --muted:#8FB3B9;
  --action:#4FB3C1; --on-action:#071C22; --mist:#6E949B;
  --hero:#0B2730; --on-hero:#E8F1F3; --on-hero-2:#9CC3CA; --hero-line:#24525C; --grid:rgba(156,195,202,.06); --trace:rgba(79,179,193,.5); --trace-2:rgba(79,179,193,.2); --gold-halo:rgba(252,194,0,.2); color-scheme:dark } }
:root[data-theme="dark"]{
  --bg:#071C22; --surface:#0D2A32; --raised:#143843; --line:#24525C;
  --fg:#E8F1F3; --fg2:#9CC3CA; --muted:#8FB3B9;
  --action:#4FB3C1; --on-action:#071C22; --mist:#6E949B;
  --hero:#0B2730; --on-hero:#E8F1F3; --on-hero-2:#9CC3CA; --hero-line:#24525C; --grid:rgba(156,195,202,.06); --trace:rgba(79,179,193,.5); --trace-2:rgba(79,179,193,.2); --gold-halo:rgba(252,194,0,.2); color-scheme:dark }
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font-family:var(--sans);font-size:17px;line-height:1.6;-webkit-font-smoothing:antialiased}
a{color:inherit}
:focus-visible{outline:3px solid var(--gold);outline-offset:3px;border-radius:4px}
.wrap{max-width:1160px;margin-inline:auto;padding-left:max(16px, env(safe-area-inset-left, 0px));padding-right:max(16px, env(safe-area-inset-right, 0px))}
h1,h2,h3{margin:0;text-wrap:balance;letter-spacing:-0.02em;line-height:1.15}
p{margin:0}
.eyebrow{font-family:var(--mono);font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:var(--fg2)}
.btn{display:inline-flex;align-items:center;justify-content:center;min-height:48px;padding:12px 22px;border-radius:8px;font-weight:600;font-size:16px;text-decoration:none;border:1px solid transparent;cursor:pointer;font-family:inherit;transition:transform .15s ease, background-color .15s ease}
.btn:hover{transform:translateY(-1px)}
.btn-gold{background:var(--gold);color:var(--on-gold)}
.btn-ghost{border-color:var(--on-hero-2);color:var(--on-hero)}
.btn-ghost:hover{background:rgba(255,255,255,.06)}
.btn-action{background:var(--action);color:var(--on-action)}

/* header + hero */
.hero{background:var(--hero);color:var(--on-hero)}
.bar{position:sticky;top:env(safe-area-inset-top, 0px);z-index:20;background:var(--hero);color:var(--on-hero);border-bottom:1px solid var(--hero-line)}
body::before{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top, 0px);z-index:21;background:var(--hero)}
.top{display:flex;align-items:center;justify-content:space-between;gap:16px;padding-block:14px}
.nav .btn .s{display:none}
section,.hero-grid{scroll-margin-top:76px}
.brand{display:flex;align-items:center;gap:12px;text-decoration:none;color:var(--on-hero)}
.brand svg{width:38px;height:38px;flex:none}
.brand b{font-size:21px;letter-spacing:-.02em}
.brand span{font-family:var(--mono);font-size:12px;letter-spacing:.35em;color:var(--on-hero-2);margin-left:2px}
.nav{display:flex;align-items:center;gap:26px;font-size:15px}
.nav a{text-decoration:none;color:var(--on-hero-2)}
.nav a:hover{color:var(--on-hero)}
.nav .btn{min-height:40px;padding:8px 16px;font-size:15px}
.lang{font-family:var(--mono);font-size:13px;letter-spacing:.1em;border:1px solid var(--hero-line);border-radius:6px;padding:5px 9px;background:transparent;color:var(--on-hero);cursor:pointer;text-decoration:none}
.nav .links{display:contents}
.nav a.btn-gold{color:var(--on-gold)}
@media (max-width:860px){.nav .links{display:none}}
@media (max-width:520px){.nav .btn .l{display:none}.nav .btn .s{display:inline}.nav{gap:10px}.brand b{font-size:19px}.brand svg{width:34px;height:34px}}
.hero-grid{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr);gap:56px;align-items:center;padding-block:64px 92px}
.hero h1{font-size:clamp(2.05rem,4.1vw,3.35rem);font-weight:700;margin-top:18px}
.hero h1 em{font-style:normal;color:var(--gold)}
.hero .eyebrow{color:var(--on-hero-2)}
.lead{font-size:clamp(1.05rem,1.6vw,1.22rem);color:var(--on-hero-2);margin-top:22px;max-width:56ch}
.ctas{display:flex;flex-wrap:wrap;gap:12px;margin-top:32px}
.sectors{margin-top:30px;font-family:var(--mono);font-size:13px;letter-spacing:.06em;color:var(--on-hero-2)}
@media (max-width:900px){.hero-grid{grid-template-columns:minmax(0,1fr);gap:40px;padding-block:28px 64px}}

/* product mock */
.mock{background:var(--surface);color:var(--fg);border-radius:14px;padding:22px;box-shadow:0 24px 60px -24px rgba(0,0,0,.45);border:1px solid var(--line)}
.mock-h{display:flex;justify-content:space-between;align-items:baseline;gap:12px;margin-bottom:16px}
.mock-h b{font-size:16px}
.mock-h span{font-family:var(--mono);font-size:12px;color:var(--muted)}
.bars{display:grid;grid-template-columns:minmax(0,9.5em) minmax(0,1fr) 2.2em;gap:12px 12px;align-items:center;font-size:14px}
.bars .n{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.track{height:10px;border-radius:5px;background:var(--raised);overflow:hidden}
.track i{display:block;height:100%;border-radius:5px;background:var(--action)}
.bars .s{font-family:var(--mono);text-align:right;font-variant-numeric:tabular-nums}
.queue{margin-top:18px;padding-top:16px;border-top:1px solid var(--line);display:flex;flex-direction:column;gap:10px}
.queue .q{display:flex;justify-content:space-between;font-size:13px;color:var(--muted)}
.queue .q b{font-family:var(--mono);font-weight:500;color:var(--fg2)}
.ot{display:flex;align-items:center;gap:10px;flex-wrap:wrap;background:var(--raised);border-radius:8px;padding:10px 12px;font-size:14px}
.ot code{font-family:var(--mono);font-size:13px;color:var(--muted)}
.ot .t{flex:1 1 12em;min-width:0}
.chip{display:inline-flex;align-items:center;gap:6px;background:var(--gold);color:var(--on-gold);border-radius:999px;padding:3px 10px;font-size:13px;font-weight:600}

/* sections */
section{padding-block:88px}
.sec-head{display:flex;flex-direction:column;gap:14px;max-width:46rem}
.sec-head h2{font-size:clamp(1.7rem,3vw,2.4rem)}
.sec-head p{color:var(--muted);font-size:1.08rem}
.constats{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:28px;margin-top:44px}
.constat{border-top:2px solid var(--line);padding-top:18px;display:flex;flex-direction:column;gap:8px}
.constat h3{font-size:1.15rem}
.constat p{color:var(--muted);font-size:16px}
.loop-h{margin-top:72px;display:flex;flex-direction:column;gap:8px}
.loop-h h3{font-size:1.45rem}
.loop-h p{color:var(--muted)}
.loop{display:flex;gap:10px;align-items:stretch;margin-top:26px}
.step{flex:1 1 0;min-width:0;background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:18px;display:flex;flex-direction:column;gap:8px}
.step .where{align-self:flex-start;font-family:var(--mono);font-size:12px;letter-spacing:.08em;color:var(--fg2);background:var(--raised);border-radius:5px;padding:2px 8px}
.step.cmms .where{color:var(--muted);background:transparent;border:1px dashed var(--line)}
.step h4{margin:0;font-size:1.02rem;line-height:1.3}
.step p{font-size:14.5px;color:var(--muted);line-height:1.5}
.arr{flex:none;align-self:center;color:var(--fg2);width:22px;height:22px}
.return{margin-top:10px;display:flex;align-items:center;gap:12px;border:1px dashed var(--line);border-radius:12px;padding:14px 18px;color:var(--muted);font-size:15px}
.return svg{flex:none;width:22px;height:22px;color:var(--fg2)}
@media (max-width:860px){.constats{grid-template-columns:minmax(0,1fr)}.loop{flex-direction:column}.arr{transform:rotate(90deg)}}

.alt{background:var(--surface);border-block:1px solid var(--line)}
.features{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px;margin-top:44px}
.feat{background:var(--bg);border:1px solid var(--line);border-radius:12px;padding:26px;display:flex;flex-direction:column;gap:12px}
.feat .tag{align-self:flex-start;font-family:var(--mono);font-size:12.5px;color:var(--fg2);background:var(--raised);border-radius:6px;padding:3px 9px}
.feat h3{font-size:1.18rem}
.feat p{color:var(--muted);font-size:16px}
.feat.wide{grid-column:span 2;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:28px;align-items:center}
.feat.wide .txt{display:flex;flex-direction:column;gap:12px}
.mini{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px}
.mini > div{background:var(--surface);border:1px solid var(--line);border-radius:8px;padding:10px;display:flex;flex-direction:column;gap:6px}
.mini span{font-family:var(--mono);font-size:11.5px;color:var(--muted);letter-spacing:.04em}
.mini .track{height:8px}
@media (max-width:980px){.features{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:640px){.features{grid-template-columns:minmax(0,1fr)}.feat.wide{grid-column:auto;grid-template-columns:minmax(0,1fr)}}

.offers{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px;margin-top:44px}
.offer{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:26px;display:flex;flex-direction:column;gap:14px}
.offer h3{font-size:1.2rem}
.offer ul{margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:9px}
.offer li{position:relative;padding-left:22px;color:var(--muted);font-size:16px}
.offer li::before{content:"";position:absolute;left:0;top:.62em;width:9px;height:9px;border-radius:2px;background:var(--gold)}
@media (max-width:760px){.offers{grid-template-columns:minmax(0,1fr)}}
.pilot{margin-top:20px;background:var(--hero);color:var(--on-hero);border-radius:16px;padding:36px;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.2fr);gap:36px;align-items:center}
.pilot h3{font-size:1.55rem}
.pilot p{color:var(--on-hero-2);margin-top:10px}
.pilot .btn{margin-top:22px}
.pilot ol{margin:0;padding:0;list-style:none;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;counter-reset:s}
.pilot li{counter-increment:s;border-top:2px solid var(--hero-line);padding-top:12px;font-size:15px;line-height:1.45}
.pilot li::before{content:counter(s, decimal-leading-zero);display:block;font-family:var(--mono);color:var(--gold);font-size:14px;margin-bottom:6px}
@media (max-width:860px){.pilot{grid-template-columns:minmax(0,1fr);padding:26px}.pilot ol{grid-template-columns:minmax(0,1fr)}}

.trust{background:var(--raised)}
.trust .wrap{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:18px;padding-block:26px}
.trust div{display:flex;align-items:center;gap:10px;font-weight:500;font-size:15px}
.trust svg{flex:none;width:20px;height:20px;color:var(--fg2)}
@media (max-width:860px){.trust .wrap{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:480px){.trust .wrap{grid-template-columns:minmax(0,1fr)}}

.about{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:48px;align-items:start}
.about .body{display:flex;flex-direction:column;gap:14px;color:var(--muted);max-width:62ch}
.about .sign{font-family:var(--mono);font-size:13px;color:var(--fg2);letter-spacing:.04em}
@media (max-width:860px){.about{grid-template-columns:minmax(0,1fr);gap:20px}}

.contact{background:var(--hero);color:var(--on-hero)}
.contact .wrap{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:40px;align-items:center;padding-block:80px}
.contact .eyebrow{color:var(--on-hero-2)}
.contact h2{font-size:clamp(1.7rem,3vw,2.4rem);margin-top:14px}
.contact p{color:var(--on-hero-2);margin-top:14px;max-width:52ch}
.mail{background:rgba(255,255,255,.05);border:1px solid var(--hero-line);border-radius:14px;padding:24px;display:flex;flex-direction:column;gap:14px}
.mail span{font-family:var(--mono);font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--on-hero-2)}
.mail a.addr{font-family:var(--mono);font-size:clamp(1rem,2.2vw,1.25rem);color:var(--on-hero);word-break:break-all;user-select:all}
.mail .row{display:flex;flex-wrap:wrap;gap:10px}
@media (max-width:860px){.contact .wrap{grid-template-columns:minmax(0,1fr);padding-block:60px}}
footer{padding-block:28px;font-size:13.5px;color:var(--muted)}
footer .wrap{display:flex;flex-wrap:wrap;justify-content:space-between;gap:12px}

/* ---------- motion: one staged load sequence in the hero, read like an instrument powering up ---------- */
@property --v{syntax:'<integer>';initial-value:0;inherits:false}
.hero{position:relative;overflow:hidden;isolation:isolate}
.hero::before{content:"";position:absolute;inset:0;z-index:-2;pointer-events:none;
  background-image:linear-gradient(var(--grid) 1px,transparent 1px),linear-gradient(90deg,var(--grid) 1px,transparent 1px);
  background-size:56px 56px;background-position:-1px -1px;
  -webkit-mask-image:linear-gradient(to bottom,transparent 0,#000 30%,#000 75%,transparent 100%);mask-image:linear-gradient(to bottom,transparent 0,#000 30%,#000 75%,transparent 100%)}
.trace{position:absolute;left:0;right:0;bottom:0;width:100%;height:30%;z-index:-1;pointer-events:none;overflow:visible}
.trace path{fill:none;stroke:var(--trace);stroke-width:2;vector-effect:non-scaling-stroke;stroke-linejoin:round;stroke-dasharray:1;stroke-dashoffset:0}
.trace path.ghost{stroke:var(--trace-2);stroke-width:1.5}
.peak{position:absolute;width:12px;height:12px;margin:-6px 0 0 -6px;border-radius:50%;background:var(--gold);z-index:-1;pointer-events:none}
.peak::after{content:"";position:absolute;inset:-6px;border-radius:50%;border:2px solid var(--gold);opacity:0}
.hero .brand svg path{stroke-dasharray:1;stroke-dashoffset:0}

.mock .s{counter-reset:v var(--v);--v:var(--to)}
.mock .s::after{content:counter(v)}
.hero h1 em{position:relative;white-space:nowrap}
.hero h1 em::after{content:"";position:absolute;left:0;right:0;bottom:-.02em;height:3px;border-radius:2px;background:var(--gold);opacity:.55;transform-origin:left center}
.chip{position:relative}
.chip::after{content:"";position:absolute;inset:-4px;border-radius:999px;border:2px solid var(--gold);opacity:0}

@media (prefers-reduced-motion: no-preference){
  .rv{animation:rise .7s cubic-bezier(.2,.7,.2,1) both;animation-delay:var(--d,0ms)}
  .top{animation:fade .5s ease-out both}
  .hero .brand svg path{animation:draw .9s .1s cubic-bezier(.6,0,.2,1) both}
  .hero h1{animation:rise .8s cubic-bezier(.2,.7,.2,1) both,wipe .9s cubic-bezier(.2,.7,.2,1) both;animation-delay:var(--d,0ms)}
  .hero h1 em{animation:signal .5s 1.35s ease-out both}
  .hero h1 em::after{animation:sweep .6s 1.45s cubic-bezier(.6,0,.2,1) both}
  .trace path{animation:draw 2s .2s cubic-bezier(.45,0,.2,1) both}
  .trace path.ghost{animation-duration:2.4s;animation-delay:.35s}
  .peak{animation:pop .4s 1.9s cubic-bezier(.3,1.6,.5,1) both}
  .peak::after{animation:ring 1.4s 2.1s ease-out 2}
  .mock{animation:lift .9s .35s cubic-bezier(.2,.7,.2,1) both}
  .track i{animation:fill 1s cubic-bezier(.25,.8,.25,1) both;animation-delay:var(--d,0ms)}
  .mock .s{animation:count 1s cubic-bezier(.25,.8,.25,1) both;animation-delay:var(--d,0ms)}
  .queue{animation:rise .6s 1.55s cubic-bezier(.2,.7,.2,1) both}
  .chip{animation:snap .45s 2.05s cubic-bezier(.3,1.6,.5,1) both}
  .chip::after{animation:ring 1s 2.4s ease-out 1}
  /* micro-interactions, kept quiet */
  html{scroll-behavior:smooth}
}
@media (max-width:900px){.peak{display:none}.trace{opacity:.6}}

@media (hover:hover) and (prefers-reduced-motion: no-preference){
  .feat,.offer,.step{transition:border-color .2s ease,transform .2s ease}
  .feat:hover,.offer:hover,.step:hover{border-color:var(--fg2);transform:translateY(-2px)}
  .btn-gold:hover{box-shadow:0 0 0 4px var(--gold-halo)}
}
@media (hover:none){.btn:hover{transform:none}}
/* section focus: the section you are reading is lit, the ones before and after recede (driven by FOCUS_JS) */
@media (prefers-reduced-motion: no-preference){
  .io-focus .focus{transition:opacity .7s ease,filter .7s ease;opacity:.28;filter:saturate(.3)}
  .io-focus .focus.in{opacity:1;filter:none}
}
/* mobile */
@media (max-width:640px){
  body{font-size:16px}
  section{padding-block:60px}
  .hero-grid{padding-block:28px 60px}
  .ctas .btn{flex:1 1 100%}
  .lead{margin-top:18px}
  .mock{padding:18px}
  .bars{grid-template-columns:minmax(0,8.2em) minmax(0,1fr) 2em;gap:10px}
  .constats{gap:22px;margin-top:32px}
  .loop-h{margin-top:52px}
  .features,.offers{margin-top:32px}
  .feat,.offer{padding:22px}
  .pilot{padding:22px}
  .contact .wrap{padding-block:52px}
  .mail .row .btn{flex:1 1 100%}
  footer .wrap{flex-direction:column}
}

@keyframes fade{from{opacity:0}}
@keyframes rise{from{opacity:0;transform:translateY(16px)}}
@keyframes wipe{from{clip-path:inset(0 0 100% 0)}to{clip-path:inset(0 0 -20% 0)}}
@keyframes draw{from{stroke-dashoffset:1}}
@keyframes signal{from{color:var(--on-hero)}}
@keyframes sweep{from{transform:scaleX(0)}}
@keyframes lift{from{opacity:0;transform:translateY(28px) scale(.98)}}
@keyframes fill{from{width:0}}
@keyframes count{from{--v:0}}
@keyframes pop{from{transform:scale(0);opacity:0}}
@keyframes snap{from{transform:scale(.55);opacity:0}}
@keyframes ring{0%{opacity:.8;transform:scale(1)}100%{opacity:0;transform:scale(1.9)}}

@media (prefers-reduced-motion: reduce){*{transition:none!important}}
"""

MARK_H = '<svg viewBox="0 0 64 64" fill="none" aria-hidden="true"><rect x="1" y="1" width="62" height="62" rx="10" stroke="#1F6E7E" stroke-width="2"/><path pathLength="1" d="M8 50 L19 39 L26 44 L38 18 L46 31 L56 50" stroke="#FCC200" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/><circle cx="38" cy="18" r="4" fill="#F3F7F8"/></svg>'
TRACE = '<svg class="trace" viewBox="0 0 1440 400" preserveAspectRatio="none" aria-hidden="true"><path class="ghost" pathLength="1" d="M0 392 L130 380 L220 388 L340 360 L430 372 L560 340 L650 352 L770 300 L860 322 L980 286 L1080 310 L1200 276 L1310 300 L1440 284"/><path pathLength="1" d="M0 380 L140 366 L230 374 L360 344 L450 356 L590 318 L680 330 L792 133 L880 300 L1010 262 L1110 300 L1220 270 L1330 296 L1440 280"/></svg><span class="peak" style="left:55%;top:80%"></span>'
MARK = '<svg viewBox="0 0 64 64" fill="none" aria-hidden="true"><rect x="1" y="1" width="62" height="62" rx="10" stroke="#1F6E7E" stroke-width="2"/><path d="M8 50 L19 39 L26 44 L38 18 L46 31 L56 50" stroke="#FCC200" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/><circle cx="38" cy="18" r="4" fill="#F3F7F8"/></svg>'
ARR = '<svg class="arr" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M4 12h15m-5-5 5 5-5 5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
RET = '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M20 7v4a4 4 0 0 1-4 4H5m4-4-4 4 4 4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
CHECK = '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12 3 4.5 6v5.5c0 4.6 3.1 8.1 7.5 9.5 4.4-1.4 7.5-4.9 7.5-9.5V6L12 3Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path d="m8.8 12 2.2 2.2 4.4-4.4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
BARCOL = ['var(--gold)','var(--action)','var(--action)','var(--mist)']
IDS = ['concept','fonctionnalites','offre','contact']

def body(L, p, switch_html):
    t = lambda s: T(L, s)
    i = lambda n: p + n
    nav = ''.join(f'<a href="#{i(IDS[k])}">{t(L["nav"][k])}</a>' for k in range(3))
    bars = ''.join(f'<div class="n">{t(n)}</div><div class="track"><i style="width:{v}%;background:{BARCOL[k]};--d:{750+k*130}ms"></i></div><div class="s" style="--to:{v};--d:{750+k*130}ms"></div>' for k,(n,v) in enumerate(L['mock_rows']))
    constats = ''.join(f'<div class="constat"><h3>{t(a)}</h3><p>{t(b)}</p></div>' for a,b in L['constats'])
    steps=[]
    for k,(w,h,d) in enumerate(L['loop']):
        steps.append(f'<div class="step{" cmms" if k==0 else ""}"><span class="where">{t(w)}</span><h4>{t(h)}</h4><p>{t(d)}</p></div>')
    loop = ARR.join(steps)
    f = L['features']
    feats = ''.join(f'<div class="feat"><span class="tag">{t(b)}</span><h3>{t(a)}</h3><p>{t(c)}</p></div>' for a,b,c in f[:4])
    mini = ''.join(f'<div><span>{t(n)}</span><div class="track"><i style="width:{v}%;background:{BARCOL[k]}"></i></div></div>' for k,(n,v) in enumerate(L['mock_rows'][:3]))
    feats += f'<div class="feat wide"><div class="txt"><span class="tag">{t(f[4][1])}</span><h3>{t(f[4][0])}</h3><p>{t(f[4][2])}</p></div><div class="mini" aria-hidden="true">{mini}</div></div>'
    offers = ''.join('<div class="offer"><h3>%s</h3><ul>%s</ul></div>' % (t(h), ''.join(f'<li>{t(x)}</li>' for x in items)) for h,items in L['offers'])
    psteps = ''.join(f'<li>{t(s)}</li>' for s in L['pilot_steps'])
    trust = ''.join(f'<div>{CHECK}<span>{t(s)}</span></div>' for s in L['trust'])
    about = ''.join(f'<p>{t(s)}</p>' for s in L['a_txt'])
    return f'''<header class="bar"><div class="wrap top"><a class="brand" href="#{i("top")}" aria-label="Summit RMS">{MARK_H}<b>Summit</b><span>RMS</span></a>
<nav class="nav"><span class="links">{nav}</span><a class="btn btn-gold" href="#{i("contact")}"><span class="l">{t(L["nav_cta"])}</span><span class="s">{t(L["nav_cta_short"])}</span></a>{switch_html}</nav></div></header>
<div class="hero">{TRACE}<div class="wrap">
<div class="hero-grid focus" id="{i("top")}"><div>
<div class="eyebrow rv" style="--d:150ms">{t(L["hero_eyebrow"])}</div>
<h1 style="--d:250ms">{t(L["h1_a"])}<em>{t(L["h1_em"])}</em>{t(L["h1_b"])}</h1>
<p class="lead rv" style="--d:520ms">{t(L["hero_lead"])}</p>
<div class="ctas rv" style="--d:660ms"><a class="btn btn-gold" href="#{i("contact")}">{t(L["cta1"])}</a><a class="btn btn-ghost" href="#{i("concept")}">{t(L["cta2"])}</a></div>
<p class="sectors rv" style="--d:800ms">{t(L["sectors"])}</p></div>
<div class="mock" role="img" aria-label="{E(L["mock_title"])}, {E(L["mock_tag"])}"><div class="mock-h"><b>{t(L["mock_title"])}</b><span>{t(L["mock_tag"])}</span></div>
<div class="bars">{bars}</div>
<div class="queue"><div class="q"><span>{t(L["mock_queue"])}</span><b>{t(L["mock_queue_n"])}</b></div>
<div class="ot"><code>{t(L["mock_ot"])}</code><span class="t">{t(L["mock_ot_txt"])}</span><span class="chip">{t(L["mock_chip"])}</span></div></div></div>
</div></div></div>
<main>
<section id="{i("concept")}"><div class="wrap focus">
<div class="sec-head"><div class="eyebrow">{t(L["c_eyebrow"])}</div><h2>{t(L["c_h2"])}</h2></div>
<div class="constats">{constats}</div>
<div class="loop-h"><h3>{t(L["loop_h3"])}</h3><p>{t(L["loop_intro"])}</p></div>
<div class="loop">{loop}</div>
<div class="return">{RET}<span>{t(L["loop_return"])}</span></div>
</div></section>
<section class="alt" id="{i("fonctionnalites")}"><div class="wrap focus">
<div class="sec-head"><div class="eyebrow">{t(L["f_eyebrow"])}</div><h2>{t(L["f_h2"])}</h2></div>
<div class="features">{feats}</div></div></section>
<section id="{i("offre")}"><div class="wrap focus">
<div class="sec-head"><div class="eyebrow">{t(L["o_eyebrow"])}</div><h2>{t(L["o_h2"])}</h2><p>{t(L["o_intro"])}</p></div>
<div class="offers">{offers}</div>
<div class="pilot"><div><h3>{t(L["pilot_h3"])}</h3><p>{t(L["pilot_txt"])}</p><a class="btn btn-gold" href="#{i("contact")}">{t(L["pilot_cta"])}</a></div><ol>{psteps}</ol></div>
</div></section>
<div class="trust"><div class="wrap focus" data-fg="about">{trust}</div></div>
<section><div class="wrap about focus" data-fg="about">
<div class="sec-head"><div class="eyebrow">{t(L["a_eyebrow"])}</div><h2>{t(L["a_h2"])}</h2></div>
<div class="body">{about}<p class="sign">{t(L["a_sign"])}</p></div></div></section>
<section class="contact" id="{i("contact")}" style="padding-block:0"><div class="wrap focus">
<div><div class="eyebrow">{t(L["k_eyebrow"])}</div><h2>{t(L["k_h2"])}</h2><p>{t(L["k_txt"])}</p></div>
<div class="mail"><span>{t(L["k_label"])}</span><a class="addr" href="mailto:{L["email"]}">{L["email"]}</a>
<div class="row"><button class="btn btn-gold copy" type="button" id="{i("copy")}" data-email="{L["email"]}" data-done="{E(L["copied"])}">{t(L["copy"])}</button></div></div>
</div></section>
</main>
<footer><div class="wrap"><span>{t(L["foot"])}</span><span>© 2026 Apex Reliability · {t(L["nocookie"])}</span></div></footer>'''

FOCUS_JS = """
(function(){
  if(!('IntersectionObserver' in window)||matchMedia('(prefers-reduced-motion: reduce)').matches)return;
  var root=document.documentElement,units={},order=[],vis=new Map(),cur=null,raf=0,th=[];
  [].slice.call(document.querySelectorAll('.focus')).forEach(function(el,i){
    var k=el.getAttribute('data-fg')||'s'+i,b=el.closest('section,.trust,.hero')||el;
    if(!units[k]){units[k]={els:[],blocks:[]};order.push(k)}
    units[k].els.push(el);units[k].blocks.push(b);
  });
  function update(){
    raf=0;
    var se=document.scrollingElement||root,top=0,bot,c,best=null,bd=Infinity;
    if(se.scrollHeight>innerHeight*1.2){
      /* the page scrolls in its own window: the reading line is the middle of the window, under the sticky bar */
      [].slice.call(document.querySelectorAll('.bar')).forEach(function(b){var r=b.getBoundingClientRect();if(r.height&&r.bottom>top)top=r.bottom});
      bot=innerHeight;
    }else{
      /* the page is shown at full height inside a host that scrolls it: use the part reported on screen */
      top=Infinity;bot=-Infinity;
      vis.forEach(function(r){if(r){if(r.top<top)top=r.top;if(r.bottom>bot)bot=r.bottom}});
      if(top===Infinity)return;
    }
    /* near the end of the page the reading line slides down, so the last section gets its turn */
    var half=(bot-top)/2,left=Math.max(0,se.scrollHeight-(se.scrollHeight>innerHeight*1.2?scrollY+innerHeight:bot)),f=left<half?.5+.45*(1-left/half):.5;
    c=top+(bot-top)*f;
    order.forEach(function(k){units[k].blocks.forEach(function(b){
      var r=b.getBoundingClientRect();if(!r.height)return;
      var d=c<r.top?r.top-c:(c>r.bottom?c-r.bottom:0);if(d<bd){bd=d;best=k}
    })});
    if(best===null)return;
    if(best!==cur){order.forEach(function(k){units[k].els.forEach(function(el){el.classList.toggle('in',k===best)})});cur=best}
    if(!root.classList.contains('io-focus'))root.classList.add('io-focus');
  }
  function schedule(){if(!raf)raf=requestAnimationFrame(update)}
  for(var i=0;i<=100;i++)th.push(i/100);
  var io=new IntersectionObserver(function(es){es.forEach(function(e){vis.set(e.target,e.isIntersecting?e.intersectionRect:null)});schedule()},{threshold:th});
  [].slice.call(document.querySelectorAll('.bar,.hero,main>section,main>.trust,footer')).forEach(function(b){io.observe(b)});
  addEventListener('scroll',schedule,{passive:true});addEventListener('resize',schedule);
  update();
})();
"""
COPY_JS = """
document.querySelectorAll('.copy').forEach(function(b){b.addEventListener('click',function(){
  var e=b.getAttribute('data-email'),label=b.textContent;
  function done(){b.textContent=b.getAttribute('data-done');setTimeout(function(){b.textContent=label},2000)}
  function sel(){var a=b.closest('.mail').querySelector('.addr');var r=document.createRange();r.selectNodeContents(a);var s=window.getSelection();s.removeAllRanges();s.addRange(r)}
  try{navigator.clipboard.writeText(e).then(done,sel)}catch(x){sel()}
})});
"""
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap">'
FAV = "data:image/svg+xml," + "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%23FCC200'/%3E%3Cpath d='M10 48 L20 38 L27 43 L38 19 L46 31 L54 48' stroke='%23004F60' stroke-width='5' fill='none' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E"

FONT_FILES = [('IBM Plex Sans',w,f'ibm-plex-sans-latin-{w}-normal.woff2') for w in (400,500,600,700)] + [('IBM Plex Mono',w,f'ibm-plex-mono-latin-{w}-normal.woff2') for w in (400,500)]
LATIN = 'U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD'
def self_fonts(prefix):
    pre = ''.join(f'<link rel="preload" href="{prefix}{f}" as="font" type="font/woff2" crossorigin>' for fam,w,f in FONT_FILES if w in (400,700) and 'Sans' in fam)
    faces = ''.join(f"@font-face{{font-family:'{fam}';font-style:normal;font-weight:{w};font-display:swap;src:url({prefix}{f}) format('woff2');unicode-range:{LATIN}}}" for fam,w,f in FONT_FILES)
    return pre + f'<style>{faces}</style>'

def site_page(L, other_href, self_url, other_url, other_lang, with_switch=True, fonts=None, og_image=None):
    sw = '' if not with_switch else f'<a class="lang" href="{other_href}" hreflang="{other_lang}" lang="{other_lang}" title="{E(L["switch_title"])}">{L["switch_label"]}</a>'
    return f'''<!doctype html>
<html lang="{L["lang"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{E(L["meta_title"])}</title>
<meta name="description" content="{E(L["meta_desc"])}">
<link rel="canonical" href="{self_url}">
<link rel="alternate" hreflang="{L["lang"]}" href="{self_url}">
<link rel="alternate" hreflang="{other_lang}" href="{other_url}">
<link rel="alternate" hreflang="x-default" href="https://summit-reliability.fr/">
<meta property="og:title" content="{E(L["meta_title"])}">
<meta property="og:description" content="{E(L["meta_desc"])}">
<meta property="og:url" content="{self_url}">
<meta property="og:type" content="website">
<link rel="icon" href="{FAV}">
{f'<meta property="og:image" content="{og_image}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">' if og_image else ''}
{fonts if fonts is not None else FONTS}
<style>{CSS}</style>
</head>
<body>
{body(L, "", sw)}
<script>{COPY_JS}{FOCUS_JS}</script>
</body>
</html>
'''

os.makedirs(os.path.join(OUT,'site','en'), exist_ok=True)
open(os.path.join(OUT,'site','index.html'),'w').write(site_page(FR,'en/index.html','https://summit-reliability.fr/','https://summit-reliability.fr/en/','en'))
open(os.path.join(OUT,'site','en','index.html'),'w').write(site_page(EN,'../index.html','https://summit-reliability.fr/en/','https://summit-reliability.fr/','fr'))

# preview: desktop view (both languages, toggle) + phone view (iframes of the real pages)
def sw_btn(L, target):
    return f'<button class="lang" type="button" data-set-lang="{target}" title="{E(L["switch_title"])}">{L["switch_label"]}</button>'
frame_fr = E(site_page(FR,'#','https://summit-reliability.fr/','https://summit-reliability.fr/en/','en', False), quote=True)
frame_en = E(site_page(EN,'#','https://summit-reliability.fr/en/','https://summit-reliability.fr/','fr', False), quote=True)
PV_CSS = """
.pv{position:fixed;z-index:50;left:50%;transform:translateX(-50%);bottom:calc(16px + env(safe-area-inset-bottom, 0px));display:flex;gap:4px;padding:5px;border-radius:999px;background:var(--surface);border:1px solid var(--line);box-shadow:0 10px 30px -10px rgba(0,0,0,.35);font-family:var(--sans)}
.pv button{border:0;background:transparent;color:var(--fg);font:600 14px/1 var(--sans);padding:10px 16px;border-radius:999px;cursor:pointer}
.pv button[aria-pressed="true"]{background:var(--action);color:var(--on-action)}
.pv .sep{width:1px;background:var(--line);margin:6px 4px}
@media (max-width:700px){.pv .dev{display:none}.pv .sep{display:none}}
.phone-view{min-height:100vh;background:var(--raised);display:flex;flex-direction:column;align-items:center;gap:16px;padding-block:32px 110px;padding-left:max(16px, env(safe-area-inset-left, 0px));padding-right:max(16px, env(safe-area-inset-right, 0px))}
.phone-view p{margin:0;font-family:var(--mono);font-size:13px;color:var(--muted);text-align:center}
.phone{width:412px;max-width:100%;height:min(844px, calc(100vh - 170px));min-height:560px;border-radius:46px;border:11px solid #0B1A1F;background:#0B1A1F;box-shadow:0 30px 70px -30px rgba(0,0,0,.5);overflow:hidden}
.phone iframe{width:100%;height:100%;border:0;border-radius:35px;display:block;background:#F3F7F8}
"""
prev = f'''<title>Summit RMS site</title>
<meta name="claude:viewport-fit-sides" content="cover">
{FONTS}
<style>{CSS}{PV_CSS}</style>
<div id="pv-desktop">
<div data-lang="fr" lang="fr">{body(FR, "fr-", sw_btn(FR,"en"))}</div>
<div data-lang="en" lang="en" hidden>{body(EN, "en-", sw_btn(EN,"fr"))}</div>
</div>
<div id="pv-mobile" class="phone-view" hidden>
<div class="phone"><iframe data-lang-frame="fr" title="Aperçu mobile, français" srcdoc="{frame_fr}"></iframe><iframe data-lang-frame="en" title="Mobile preview, English" srcdoc="{frame_en}" hidden></iframe></div>
<p>390 px · {E("vue mobile / mobile view")}</p>
</div>
<div class="pv" role="toolbar" aria-label="Preview">
<button type="button" data-pv-lang="fr" aria-pressed="true">FR</button><button type="button" data-pv-lang="en" aria-pressed="false">EN</button>
<span class="sep"></span>
<button type="button" class="dev" data-pv-dev="desktop" aria-pressed="true">Desktop</button><button type="button" class="dev" data-pv-dev="mobile" aria-pressed="false">Mobile</button>
</div>
<script>
var pvLang='fr',pvDev='desktop';
function press(attr,val){{document.querySelectorAll('['+attr+']').forEach(function(b){{b.setAttribute('aria-pressed',String(b.getAttribute(attr)===val))}})}}
function setLang(l){{pvLang=l;document.querySelectorAll('[data-lang]').forEach(function(d){{d.hidden=d.getAttribute('data-lang')!==l}});
  document.querySelectorAll('[data-lang-frame]').forEach(function(f){{f.hidden=f.getAttribute('data-lang-frame')!==l}});
  document.documentElement.lang=l;press('data-pv-lang',l);try{{localStorage.setItem('lang',l)}}catch(e){{}}}}
function setDev(d){{pvDev=d;document.getElementById('pv-desktop').hidden=d!=='desktop';document.getElementById('pv-mobile').hidden=d!=='mobile';press('data-pv-dev',d);window.scrollTo(0,0)}}
document.querySelectorAll('[data-set-lang]').forEach(function(b){{b.addEventListener('click',function(){{setLang(b.getAttribute('data-set-lang'));window.scrollTo(0,0)}})}});
document.querySelectorAll('[data-pv-lang]').forEach(function(b){{b.addEventListener('click',function(){{setLang(b.getAttribute('data-pv-lang'))}})}});
document.querySelectorAll('[data-pv-dev]').forEach(function(b){{b.addEventListener('click',function(){{setDev(b.getAttribute('data-pv-dev'))}})}});
try{{var s=localStorage.getItem('lang');if(s==='en')setLang('en')}}catch(e){{}}
{COPY_JS}{FOCUS_JS}
</script>
'''
open(os.path.join(OUT,'preview.html'),'w').write(prev)
print('built')

# ---- deploy folder (what goes online): self-hosted fonts, clean URLs, sitemap, robots, 404, share images
import shutil
DEP = os.path.join(OUT, 'deploy')
FONT_SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fonts')
SITE = 'https://summit-reliability.fr/'
if os.path.isdir(DEP): shutil.rmtree(DEP)
os.makedirs(os.path.join(DEP, 'en'))
shutil.copytree(FONT_SRC, os.path.join(DEP, 'fonts'))
open(os.path.join(DEP,'index.html'),'w').write(site_page(FR,'en/',SITE,SITE+'en/','en', fonts=self_fonts('fonts/'), og_image=SITE+'og-fr.png'))
open(os.path.join(DEP,'en','index.html'),'w').write(site_page(EN,'../',SITE+'en/',SITE,'fr', fonts=self_fonts('../fonts/'), og_image=SITE+'og-en.png'))
open(os.path.join(DEP,'robots.txt'),'w').write(f'User-agent: *\nAllow: /\nDisallow: /source/\n\nSitemap: {SITE}sitemap.xml\n')
open(os.path.join(DEP,'sitemap.xml'),'w').write(f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
<url><loc>{SITE}</loc><xhtml:link rel="alternate" hreflang="fr" href="{SITE}"/><xhtml:link rel="alternate" hreflang="en" href="{SITE}en/"/><xhtml:link rel="alternate" hreflang="x-default" href="{SITE}"/></url>
<url><loc>{SITE}en/</loc><xhtml:link rel="alternate" hreflang="fr" href="{SITE}"/><xhtml:link rel="alternate" hreflang="en" href="{SITE}en/"/><xhtml:link rel="alternate" hreflang="x-default" href="{SITE}"/></url>
</urlset>
''')
open(os.path.join(DEP,'404.html'),'w').write(f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Page introuvable · Page not found · Summit RMS</title>
<meta name="robots" content="noindex">
<link rel="icon" href="{FAV}">
{self_fonts('/fonts/')}
<style>{CSS}
.nf{{min-height:calc(100vh - 140px);display:flex;align-items:center}}
.nf>.wrap{{width:100%}}
.nf h1{{font-size:clamp(30px,4vw,44px);line-height:1.15;color:var(--fg);margin:14px 0 10px}}
.nf p{{color:var(--fg2);margin:0 0 6px}}
.nf .row{{display:flex;gap:16px;flex-wrap:wrap;align-items:center;margin-top:26px}}
.nf .row a:not(.btn){{color:var(--fg)}}</style>
</head>
<body>
<header class="bar"><div class="wrap top"><a class="brand" href="/" aria-label="Summit RMS">{MARK_H}<b>Summit</b><span>RMS</span></a></div></header>
<main class="nf"><div class="wrap">
<div class="eyebrow">Erreur 404 · Error 404</div>
<h1>Cette page n'existe pas.</h1>
<p lang="en">This page does not exist.</p>
<div class="row"><a class="btn btn-gold" href="/">Retour à l'accueil</a><a href="/en/" lang="en">Go to the English home page</a></div>
</div></main>
</body>
</html>
''')
open(os.path.join(DEP,'CNAME'),'w').write('summit-reliability.fr\n')
open(os.path.join(DEP,'.nojekyll'),'w').write('')
