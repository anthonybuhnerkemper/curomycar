# Curo My Car: Off-Site SEO Next Steps

The website is done. These steps happen outside the site and matter as much as the site for showing up in local Google results and the map pack. Do them roughly in this order.

## 1. Google Business Profile (most important)
1. Go to https://business.google.com and create a profile for **Curo My Car**.
2. Category: **Mobile mechanic** (primary). Possible secondary: **Auto repair shop**, **Auto air conditioning service**, **Brake shop**. Only pick ones that are accurate.
3. Set it up as a **service-area business**: when asked if customers visit your location, choose **No**. Enter the real Stafford address for verification only. It stays **hidden**.
4. Service areas: Stafford, Sugar Land, Missouri City, Richmond, Rosenberg, Katy, Fulshear, Meadows Place, Houston (or specific ZIPs). Google allows up to 20.
5. Phone **(281) 789-8609**, website **https://curomycar.com/**, hours **Mon–Sat 8am–6pm**.
6. Turn on the **Veteran-led** attribute.
7. Add the services, matching the website pages. Write the description in plain language with no keyword lists. Don't name past employers or insurers.
8. Add real photos: Walter, the work vehicle, tools, and jobs in progress (no customer plates or faces without permission). Add new ones now and then.
9. Complete verification (video or postcard, whichever Google offers).
10. Post an update every few weeks (seasonal tips: AC before summer, batteries in heat).

## 2. Google Search Console
1. https://search.google.com/search-console → **Add property** → choose **Domain** → `curomycar.com`.
2. Google shows a TXT record like `google-site-verification=XXXX`.
3. At **Porkbun**: Domain Management → curomycar.com → **DNS** → add record: Type **TXT**, Host **blank** (root), Answer = the full `google-site-verification=...` value, TTL default. Don't touch the existing GitHub Pages A/CNAME records.
4. Wait a few minutes, then click **Verify** (DNS can take up to a few hours).
5. **Sitemaps** → submit `https://curomycar.com/sitemap.xml`.
6. Use **URL Inspection** → "Request indexing" on the home page and a few key pages.
7. Check back weekly for coverage errors and which searches show the site.

## 3. Bing Webmaster Tools
1. https://www.bing.com/webmasters → sign in → **Import from Google Search Console** (fastest), or add the site and verify with a DNS record at Porkbun.
2. Submit `https://curomycar.com/sitemap.xml`. This also feeds DuckDuckGo and Yahoo.

## 4. Consistent citations (NAP)
Use **exactly** the same details everywhere:
- Name: **Curo My Car**
- Phone: **(281) 789-8609**
- Website: **https://curomycar.com/**
- Address: Stafford, TX (hidden/service-area wherever the platform allows)
- Hours: Mon–Sat 8am–6pm

Claim or create listings on:
- **Apple Business Connect** (https://businessconnect.apple.com) for Apple Maps and Siri
- **Yelp for Business** (https://biz.yelp.com). Pick "Mobile mechanic," hide the address, set service areas.
- **Facebook Page**. Category Automotive Repair Shop / Mobile mechanic, service area, link to the site.
- **Nextdoor Business Page**. Strong for local word of mouth.
- Optional later: Bing Places (via Bing Webmaster Tools), BBB, Angi/Thumbtack if you want leads from them.

Once these profiles exist, they can be added to the `sameAs` list in the home page JSON-LD (`index.html`). It's intentionally empty now.

## 5. Real customer reviews
- After every completed job, text the customer your Google review link (GBP → "Ask for reviews" gives a short link). Something like: *"Thanks for having me out today. If you were happy with the work, a quick Google review would really help my small business: [link]. – Walter"*
- Ask everyone the same way. Don't offer discounts or gifts for reviews, don't write your own, and don't ask only happy customers. Google and the FTC prohibit fake or incentivized reviews.
- Reply to every review, good or bad, briefly and professionally.
- Once you have real reviews, they can be added to the hidden "What Customers Say" section on the home page (with the customer's permission). Never make up reviews or ratings.

## 6. Ongoing
- Add a real photo of Walter to the "Why Walter" section (there's a slot in `index.html`), with width/height set and descriptive alt text.
- When Microsoft Bookings is live, paste its URL into `js/config.js` (`BOOKINGS_URL`).
- Editing service or city page copy: change `_tools/content.py`, run `python3 _tools/build.py`, commit, push. That also refreshes `sitemap.xml`.
