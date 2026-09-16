#!/usr/bin/env python3
# Generate dependency-free HTML. Run before preview/commit; never deploys.
from pathlib import Path
import html, json
ROOT=Path(__file__).resolve().parents[1]
BASE='https://getvocari.app'
PLAY='https://play.google.com/store/apps/details?id=com.vocari.vocari2'
def esc(value): return html.escape(str(value),quote=True)
def read(path): return (ROOT/path).read_text()
def write(path,value):
 p=ROOT/path; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(value+'\n')
def header(active=''):
 links=[('/#how-it-works','How it works'),('/earbuds/','Earbuds & headsets'),('/updates/','Journal'),('/support/','Support')]
 nav=''.join(f'<a href="{url}"'+(' aria-current="page"' if active==url else '')+f'>{label}</a>' for url,label in links)
 return f'''<a class="skip-link" href="#main">Skip to content</a><header class="site-header"><div class="wrap header-inner"><a class="brand" href="/" aria-label="Vocari home"><img src="/assets/images/vocari_wordmark.webp" width="700" height="185" alt="Vocari"></a><button class="menu-button" aria-expanded="false" aria-controls="primary-nav" type="button">Menu</button><nav class="primary-nav" id="primary-nav" aria-label="Main navigation">{nav}<a class="button header-cta" href="/#download">Get Vocari <span aria-hidden="true">↗</span></a></nav></div></header>'''
def footer():
 return '''<footer class="site-footer"><div class="wrap"><div class="footer-top"><div class="footer-brand"><a href="/" aria-label="Vocari home"><img src="/assets/images/vocari_wordmark.webp" width="700" height="185" alt="Vocari" loading="lazy"></a><p>Private, nearby conversations.<br>Through the earbuds you make your own.</p><a class="text-link small" href="https://scalarlabs.ai/">A ScalarLabs product ↗</a></div><div><h2>Explore</h2><nav aria-label="Explore"><a href="/#how-it-works">How it works</a><a href="/earbuds/">Earbuds & headsets</a><a href="/updates/">Journal & updates</a><a href="/#download">Download Vocari</a></nav></div><div><h2>Here to help</h2><nav aria-label="Help and legal"><a href="/support/">Setup & support</a><a href="mailto:feedback@scalarlabs.ai">Contact us</a><a href="/privacy/">Privacy</a><a href="/terms/">Terms of use</a><a href="/earbuds/#disclosure">Affiliate disclosure</a></nav></div></div><div class="footer-bottom"><p>© 2026 ScalarLabs. All rights reserved.</p><p>Android on Google Play · iPhone: Awaiting Apple review</p></div></div></footer>'''
def page(path,title,desc,body,active='',kind='WebPage',extra='',image=True):
 canonical=BASE+path
 schema={'@context':'https://schema.org','@type':kind,'name':title,'description':desc,'url':canonical,'publisher':{'@type':'Organization','name':'ScalarLabs','url':'https://scalarlabs.ai/'}}
 if kind=='Article': schema.update({'headline':title,'author':{'@type':'Organization','name':'Vocari','url':BASE},'mainEntityOfPage':canonical})
 if path=='/404.html': extra+='<meta name="robots" content="noindex">'
 if path=='/': schema['about']={'@type':'MobileApplication','name':'Vocari','applicationCategory':'CommunicationApplication','operatingSystem':'Android, iOS','downloadUrl':PLAY,'description':'Nearby two-person voice communication using compatible Bluetooth headsets. No Wi-Fi router or internet connection required.'}
 schema_json=json.dumps(schema).replace('<', chr(92)+'u003c')
 social=(' <meta property="og:image" content="https://getvocari.app/assets/images/social-preview.png"><meta name="twitter:image" content="https://getvocari.app/assets/images/social-preview.png">' if image and (ROOT/'assets/images/social-preview.png').exists() else '')
 result=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(title)} | Vocari</title><meta name="description" content="{esc(desc)}"><link rel="canonical" href="{canonical}"><meta property="og:title" content="{esc(title)} | Vocari"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{canonical}"><meta property="og:type" content="{'article' if kind=='Article' else 'website'}"><meta property="og:site_name" content="Vocari"><meta name="twitter:card" content="{'summary_large_image' if social else 'summary'}"><meta name="twitter:title" content="{esc(title)} | Vocari"><meta name="twitter:description" content="{esc(desc)}">{social}<meta name="theme-color" content="#081a34"><link rel="icon" href="/assets/images/favicon.png" type="image/png"><link rel="stylesheet" href="/home.css"><script src="/home.js" defer></script>{extra}<script type="application/ld+json">{schema_json}</script></head><body>{header(active)}<main id="main">{body}</main>{footer()}</body></html>'''
 write(('index.html' if path=='/' else '404.html' if path=='/404.html' else path.strip('/')+'/index.html'),result)
def hero(title,desc,kicker='Vocari',crumb=''):
 return f'<section class="page-hero"><div class="wrap">'+(f'<p class="breadcrumbs"><a href="/">Home</a> / {crumb}</p>' if crumb else '')+f'<span class="eyebrow">{kicker}</span><h1>{title}</h1><p class="lead">{desc}</p></div></section>'
def post_cards(posts):
 return '<div class="cards-three">'+''.join(f'<article class="article-card"><span class="article-category">{esc(p["category"])} · {esc(p["readTime"])} min read</span><h3><a href="/updates/{p["slug"]}/">{esc(p["title"])}</a></h3><p>{esc(p["description"])}</p><a class="text-link" href="/updates/{p["slug"]}/">Read the guide <span aria-hidden="true">↗</span></a></article>' for p in posts)+'</div>'
posts=[json.loads(p.read_text()) for p in sorted((ROOT/'content/posts').glob('*.json'))]
posts=[p for p in posts if p.get('status')=='ready-for-review']
page('/','Keep the conversation going','Private, nearby, continuous two-way conversation through Bluetooth earbuds or headsets. Supports Android–iPhone conversations. No Wi-Fi router or internet required.',read('content/home.html').replace('{{POST_CARDS}}',post_cards(posts)),extra='<meta name="fo-verify" content="56690dc9-c94a-45d2-a057-f271be1a59a1" />')
for source in sorted((ROOT/'content/pages').glob('*.json')):
 p=json.loads(source.read_text()); page(p['path'],p['title'],p['description'],read(p['body']),p.get('active',''),p.get('kind','WebPage'))
if posts:
 page('/updates/','Journal & updates','Practical Vocari guides for nearby conversations, headset choices, and everyday use.',hero('A little know-how.<br>A better conversation.','Practical guides for getting connected, choosing your headset, and making the most of a nearby conversation.','The Vocari journal','Journal')+'<section class="section"><div class="wrap">'+post_cards(posts)+'<p class="comparison-note">Product news will appear here when there’s something confirmed to share. The completed iPhone app supports cross-platform communication and is awaiting Apple review before public App Store availability.</p></div></section>','/updates/')
 for p in posts:
  body=hero(esc(p['title']),esc(p['description']),esc(p['category']),'<a href="/updates/">Journal</a> / Guide')+f'<section class="section"><div class="wrap article-layout"><article class="prose"><p class="article-meta">By Vocari · {esc(p["readTime"])} min read</p>'+p['body']+'</article><aside class="article-aside"><span class="eyebrow">Keep exploring</span><h2>Find your setup</h2><p>Start with compatible personal audio and two nearby phones.</p><a class="button" href="/earbuds/">Explore headsets ↗</a><p style="margin:20px 0 0"><a href="/support/">Setup & support</a></p></aside></div></section>'
  page('/updates/'+p['slug']+'/',p['title'],p['description'],body,'/updates/','Article',image=False)
page('/404.html','Page not found','Find your way back to Vocari.',hero('Let’s get you back<br>to the conversation.','That page could not be found. Explore Vocari, find a headset, or get help setting up.','404 — Page not found')+'<section class="section"><div class="wrap actions"><a class="button" href="/">Back to Vocari</a><a class="button secondary" href="/earbuds/">Equipment guide</a><a class="text-link" href="/support/">Support ↗</a></div></section>')
# Optional catalog extension stays small and uses only the standard library.
catalog_script=ROOT/'scripts/catalog.py'
if catalog_script.exists(): exec(compile(catalog_script.read_text(),str(catalog_script),'exec'))
paths=['/']+[p['path'] for p in [json.loads(f.read_text()) for f in (ROOT/'content/pages').glob('*.json')]]
if posts: paths+=['/updates/']+['/updates/'+p['slug']+'/' for p in posts]
if (ROOT/'earbuds/index.html').exists(): paths+=['/earbuds/']
write('sitemap.xml','<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+BASE+p+'</loc></url>' for p in paths)+'</urlset>')
write('robots.txt','User-agent: *\nAllow: /\nSitemap: '+BASE+'/sitemap.xml')
print('Generated static HTML. No deployment performed.')
