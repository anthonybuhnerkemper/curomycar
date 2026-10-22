#!/usr/bin/env python3
"""Generates service pages, city pages, hubs, privacy/404 chrome and sitemap.xml.
Run from repo root: python3 _tools/build.py"""
import json, os, html, datetime
from content import SERVICES, CITIES
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://curomycar.com"
TODAY = datetime.date.today().isoformat()
PHONE_T, PHONE_D, EMAIL = "+12817898609", "(281) 789-8609", "walter@curomycar.com"
SVC = {s["slug"]: s for s in SERVICES}
BIZ = {"@type": "AutoRepair", "@id": SITE + "/#business", "name": "Curo My Car", "url": SITE + "/", "telephone": "+1-281-789-8609"}
I_PHONE = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 17v3a2 2 0 0 1-2 2A19 19 0 0 1 2 4a2 2 0 0 1 2-2h3l2 5-2 1a12 12 0 0 0 7 7l1-2 5 2z"/></svg>'
I_SMS = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>'
I_CAL = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg>'
I_STAR = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2l3 7h7l-6 5 2 7-6-4-6 4 2-7-6-5h7z"/></svg>'

def esc(t): return html.escape(t, quote=True)
def strip(t):
    import re; return html.unescape(re.sub(r"<[^>]+>", "", t))

def head(title, desc, path, ld, ogtype="website"):
    url = SITE + path
    assert len(title) <= 60, title; assert len(desc) <= 155, desc
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
<link rel="preload" href="/assets/fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/css/styles.css">
<meta name="theme-color" content="#0b1424">
<meta property="og:type" content="{ogtype}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="Curo My Car">
<meta property="og:image" content="{SITE}/assets/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Curo My Car: veteran-owned mobile mechanic in Fort Bend County, TX">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{SITE}/assets/og-image.png">
<meta name="twitter:image:alt" content="Curo My Car: veteran-owned mobile mechanic in Fort Bend County, TX">
<meta name="robots" content="index,follow">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/assets/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
''' + "".join(f'<script type="application/ld+json">\n{json.dumps(x, indent=1, ensure_ascii=False)}\n</script>\n' for x in ld) + "</head>\n"

def header(home=False):
    p = "" if home else "/"
    return f'''<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
 <div class="wrap bar">
  <a href="{'#top' if home else '/'}" class="logo" aria-label="Curo My Car home"><img src="/assets/favicon.svg" alt="" width="36" height="36"><span>CURO <b>MY CAR</b></span></a>
  <button class="nav-toggle" aria-expanded="false" aria-controls="nav" aria-label="Menu"><span></span><span></span><span></span></button>
  <nav id="nav" aria-label="Main"><a href="/services/">Services</a><a href="/service-area/">Service Area</a><a href="{p}#why">Why Walter</a><a href="{p}#faq">FAQ</a><a href="{p}#quote">Quote</a><a class="btn btn-sm" href="{p}#quote">Get a Quote</a></nav>
 </div>
</header>
'''

def footer(home=False):
    p = "" if home else "/"
    svc = "".join(f'<li><a href="/{s["slug"]}/">{esc(s["name"])}</a></li>' for s in SERVICES)
    cty = "".join(f'<li><a href="/{c["slug"]}/">{esc(c["name"])}</a></li>' for c in CITIES)
    priv = ('<p class="priv" id="privacy"><b>Privacy:</b>&nbsp;This site uses no cookies, analytics, or trackers. Quote requests are delivered to Walter\'s email by the FormSubmit service (formsubmit.co); this site does not store them. If online booking is ever enabled, scheduling is handled by Microsoft Bookings under Microsoft\'s privacy policy. Your info is used only to contact you about your vehicle and is never sold. <a href="/privacy.html">Full privacy note</a>.</p>\n' if home else "")
    return f'''<footer class="foot"><div class="wrap">
 <div class="foot-grid">
  <div><h2 class="foot-h"><a href="/services/">Services</a></h2><ul class="foot-links">{svc}</ul></div>
  <div><h2 class="foot-h"><a href="/service-area/">Service Area</a></h2><ul class="foot-links">{cty}</ul></div>
  <div><h2 class="foot-h">Contact</h2><ul class="foot-links"><li><a href="tel:{PHONE_T}" data-phone="tel"><span data-phone-text>{PHONE_D}</span></a></li><li><a href="sms:{PHONE_T}" data-phone="sms">Text Walter</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li><a href="{p}#quote">Request a quote</a></li><li><a href="/privacy.html">Privacy</a></li></ul><p>Mon&ndash;Sat 8am&ndash;6pm<br>Mobile service based in Stafford, TX</p></div>
 </div>
 <p>&copy; <span id="year">2026</span> Curo My Car &middot; <b>{I_STAR} Veteran Owned</b> &middot; Mobile mechanic serving Fort Bend County, TX</p>
 {priv}</div></footer>
<nav class="mbar" aria-label="Quick contact">
 <a href="tel:{PHONE_T}" data-phone="tel">{I_PHONE}Call</a>
 <a href="sms:{PHONE_T}" data-phone="sms">{I_SMS}Text</a>
 <a href="{p}#quote" class="hot">{I_CAL}Get a Quote</a>
</nav>
<script src="/js/config.js" defer></script>
<script src="/js/main.js" defer></script>
</body>
</html>
'''

def crumbs_ld(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u} for i, (n, u) in enumerate(items)]}
def crumbs_html(items):
    li = []
    for i, (n, u) in enumerate(items):
        li.append(f'<li><a href="{u}"' + (' aria-current="page"' if i == len(items) - 1 else "") + f'>{esc(n)}</a></li>')
    return '<nav class="crumbs" aria-label="Breadcrumb"><ol>' + "".join(li) + "</ol></nav>"
def faq_ld(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}
def faq_html(faqs, h="Frequently Asked Questions"):
    return f'<section class="sec"><div class="wrap narrow"><h2 class="stencil">{h}</h2>' + "".join(
        f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in faqs) + "</div></section>\n"

def hero(crumbs, eyebrow, h1, lead):
    return f'''<main id="main">
<section class="hero pg-hero" id="top">
 <div class="hero-fx" aria-hidden="true"><i class="orb o1"></i><i class="orb o2"></i><i class="grid-lines"></i></div>
 <div class="wrap hero-in">
  {crumbs_html(crumbs)}
  <p class="eyebrow">{I_STAR} {eyebrow}</p>
  <h1>{h1}</h1>
  <p class="lead">{lead}</p>
  {cta()}
 </div>
</section>
'''
def cta(quote="/#quote"):
    return f'''<div class="cta"><a class="btn" href="tel:{PHONE_T}" data-phone="tel">{I_PHONE} Call <span data-phone-text>{PHONE_D}</span></a><a class="btn btn-ghost" href="sms:{PHONE_T}" data-phone="sms">{I_SMS} Text</a><a class="btn btn-ghost" href="{quote}">{I_CAL} Get a Quote</a></div>'''
def cta_band(text):
    return f'''<section class="sec book"><div class="wrap"><div class="book-fallback"><h2 class="stencil cta-h">Get it fixed where you are</h2><p>{text}</p>{cta()}<p class="small">Mon&ndash;Sat 8am&ndash;6pm &middot; Price given before any work starts &middot; <a href="/#quote">Request a quote by email</a></p></div></div></section>
'''
def ul(items, cls="checks one"): return f'<ul class="{cls}">' + "".join(f"<li>{x}</li>" for x in items) + "</ul>"
def links(items, cls="linkgrid"): return f'<ul class="{cls}">' + "".join(f'<li><a href="{u}">{esc(n)}</a></li>' for n, u in items) + "</ul>"

def write(path, s):
    full = os.path.join(ROOT, path.strip("/"), "index.html") if path.endswith("/") else os.path.join(ROOT, path.strip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w").write(s)

AREA_LD = [{"@type": "City", "name": f"{c['name']}, TX"} for c in CITIES] + [{"@type": "AdministrativeArea", "name": "Fort Bend County, TX"}]

def service_page(s):
    path = f'/{s["slug"]}/'
    cr = [("Home", "/"), ("Services", "/services/"), (s["name"], path)]
    ld = [crumbs_ld(cr), {"@context": "https://schema.org", "@type": "Service", "@id": SITE + path + "#service", "name": s["name"],
          "serviceType": s["name"], "description": s["desc"], "url": SITE + path, "provider": BIZ, "areaServed": AREA_LD}, faq_ld(s["faqs"])]
    rel = [(SVC[r]["name"], f"/{r}/") for r in s["related"]]
    body = hero(cr, "Mobile service &middot; Fort Bend County, TX", esc(s["h1"]), strip(s["intro"][0]) and s["intro"][0])
    body += f'''<section class="sec"><div class="wrap narrow prose">
 <p>{s["intro"][1]}</p>
 <h2>What's included</h2>{ul(s["included"])}
 <h2>Signs you need it</h2>{ul(s["signs"], "bullets")}
 <h2>How mobile service works</h2>
 <ol class="steps steps-sm"><li><b>1</b><h3>Call, text, or request a quote</h3><p>Tell Walter the year, make and model and what's going on.</p></li><li><b>2</b><h3>Get an upfront price</h3><p>You know the cost before any work starts.</p></li><li><b>3</b><h3>Walter comes to you</h3><p>Home, office, or parking lot in Fort Bend County.</p></li></ol>
 <p>{s["mobile"]}</p>
 <h2>Why Walter</h2>
 <p>Walter Curo grew up around cars and got his formal training as a U.S. Army mechanic. Since then he has worked on diesel trucks, heavy equipment and forklifts, worked as a dealership technician, and spent years as an auto insurance adjuster and in the body-shop world. He works on all makes and models. He explains what's wrong in plain English and gives you the price first. <a href="/#why">More about Walter</a>.</p>
</div></section>
'''
    body += faq_html(s["faqs"])
    body += f'''<section class="sec alt"><div class="wrap"><h2 class="stencil">Related services</h2>{links(rel)}
<h2 class="stencil sm-top">Where we offer {esc(s["short"].lower() if s["slug"]!="pre-purchase-inspection" else "pre-purchase inspections")}</h2><p class="sub">{esc(s["name"])} is available across Fort Bend County and nearby:</p>{links([(c["name"], "/"+c["slug"]+"/") for c in CITIES], "areas arealinks")}</div></section>
'''
    body += cta_band(f'Call or text Walter about {esc(s["name"].lower())}. Tell him your vehicle and where it\'s parked.') + "</main>\n"
    write(path, head(s["title"], s["desc"], path, ld) + header() + body + footer())

WILD_CARD = ('<li class="card"><h3><a href="/#quote">And Much More</a></h3>'
             '<p>Don&#x27;t see what you need? If it&#x27;s on your car, just ask. Walter handles plenty of jobs not listed here. '
             '<a href="/#quote">Ask About It &rarr;</a></p></li>')

def city_page(c):
    path = f'/{c["slug"]}/'
    cr = [("Home", "/"), ("Service Area", "/service-area/"), (c["name"], path)]
    ld = [crumbs_ld(cr), {"@context": "https://schema.org", "@type": "Service", "@id": SITE + path + "#service", "name": f"Mobile mechanic in {c['name']}",
          "serviceType": "Mobile auto repair", "description": c["desc"], "url": SITE + path, "provider": BIZ,
          "areaServed": {"@type": "City", "name": f"{c['name']}, TX"}}, faq_ld(c["faqs"])]
    others = [(o["name"], "/"+o["slug"]+"/") for o in CITIES if o is not c]
    svc = "".join(f'<li class="card"><h3><a href="/{s["slug"]}/">{esc(s["name"])}</a></h3><p>{esc(strip(s["desc"]).split(". ")[0].rstrip("."))}.</p></li>' for s in SERVICES) + WILD_CARD
    body = hero(cr, f"Serving {esc(c['name'])} &middot; Mon&ndash;Sat 8am&ndash;6pm", esc(c["h1"]), c["paras"][0])
    body += f'''<section class="sec"><div class="wrap narrow prose">
 <h2>Car repair that comes to you in {esc(c["name"])}</h2>
 {"".join(f"<p>{p}</p>" for p in c["paras"][1:])}
 <h2>Areas we cover in and around {esc(c["name"])}</h2>
 <p>{esc(c["areas"])}. Not sure if you're in range? Call or text and ask.</p>
 <h2>Your mechanic</h2>
 <p>Walter Curo is an Army-trained mechanic who has worked on diesel trucks, heavy equipment and forklifts, worked as a dealership technician, and spent years as an auto insurance adjuster and in the body-shop world. He works on all makes and models. You get a straight answer and a price before any work starts.</p>
</div></section>
<section class="sec alt"><div class="wrap"><h2 class="stencil">Mobile services in {esc(c["name"])}</h2><p class="sub">Common jobs Walter handles on site. Don't see yours? Just ask.</p><ul class="grid">{svc}</ul></div></section>
'''
    body += faq_html(c["faqs"], f"{esc(c['name'])} FAQ")
    body += f'<section class="sec alt"><div class="wrap"><h2 class="stencil">Nearby areas we serve</h2>{links(others, "areas arealinks")}</div></section>\n'
    body += cta_band(f'Need a mechanic in {esc(c["name"])}? Call or text Walter with your vehicle and what\'s going on.') + "</main>\n"
    write(path, head(c["title"], c["desc"], path, ld) + header() + body + footer())

def hubs():
    cr = [("Home", "/"), ("Services", "/services/")]
    ld = [crumbs_ld(cr), {"@context": "https://schema.org", "@type": "ItemList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "url": SITE + "/" + s["slug"] + "/", "name": s["name"]} for i, s in enumerate(SERVICES)]}]
    svc = "".join(f'<li class="card"><h3><a href="/{s["slug"]}/">{esc(s["name"])}</a></h3><p>{esc(strip(s["intro"][0]).split(". ")[0].rstrip("."))}.</p></li>' for s in SERVICES) + WILD_CARD
    body = hero(cr, "Mobile auto repair &middot; Fort Bend County, TX", "Mobile Auto Repair Services",
                "Everything below can usually be done at your home or work. If a job truly needs a lift or a shop, Walter will tell you up front.")
    body += f'<section class="sec"><div class="wrap"><ul class="grid">{svc}</ul><p class="sub sm-top">Not sure what you need? Start with <a href="/check-engine-light-diagnostics/">diagnostics</a>, or just call or text and describe the problem.</p></div></section>\n'
    body += cta_band("Tell Walter your vehicle and what's going on, and get a price before any work starts.") + "</main>\n"
    write("/services/", head("Mobile Auto Repair Services | Curo My Car", "Brakes, oil changes, diagnostics, batteries, AC checks, tune-ups, inspections and fleet service, done at your home or work in Fort Bend County, TX.", "/services/", ld) + header() + body + footer())

    cr = [("Home", "/"), ("Service Area", "/service-area/")]
    ld = [crumbs_ld(cr)]
    cty = "".join(f'<li class="card"><h3><a href="/{c["slug"]}/">{esc(c["name"])}</a></h3><p>{esc(c["areas"].split(", ")[0])} and nearby.</p></li>' for c in CITIES)
    body = hero(cr, "Based in Stafford, TX", "Mobile Mechanic Service Area",
                "Curo My Car is based in Stafford and serves Fort Bend County and nearby Houston. Walter comes to your home, office, or parking lot.")
    body += f'<section class="sec"><div class="wrap"><ul class="grid">{cty}</ul><p class="sub sm-top">Just outside these areas? Call or text and ask. If it is workable, Walter will say so.</p></div></section>\n'
    body += cta_band("Call or text with your location and vehicle.") + "</main>\n"
    write("/service-area/", head("Service Area: Fort Bend County, TX | Curo My Car", "Mobile mechanic serving Stafford, Sugar Land, Missouri City, Richmond, Rosenberg, Katy, Fulshear, Meadows Place and Houston.", "/service-area/", ld) + header() + body + footer())

def sitemap():
    urls = [("/", "1.0"), ("/services/", "0.8"), ("/service-area/", "0.8")] + [("/"+s["slug"]+"/", "0.8") for s in SERVICES] + [("/"+c["slug"]+"/", "0.7") for c in CITIES] + [("/privacy.html", "0.2")]
    x = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
        f" <url><loc>{SITE}{u}</loc><lastmod>{TODAY}</lastmod><priority>{p}</priority></url>\n" for u, p in urls) + "</urlset>\n"
    open(os.path.join(ROOT, "sitemap.xml"), "w").write(x)

if __name__ == "__main__":
    for s in SERVICES: service_page(s)
    for c in CITIES: city_page(c)
    hubs(); sitemap()
    print("built", len(SERVICES), "services,", len(CITIES), "cities")
