# Vocari website link check — 2026-09-16

Checked the 10 purchase destinations in `content/products.json` using read-only HTTP requests and manufacturer page content. All 10 point to the intended product; no redirect to a different model was observed. Eight returned HTTP 200 directly. JBL and Sony returned 403 to curl, while the web reader retrieved the correct current product pages and buying controls; these are access restrictions, not evidence of broken links.

| Catalog product | Destination and exact identity | Result |
|---|---|---|
| Bose QuietComfort Ultra Earbuds (2nd Gen) | [Bose QCUE2 retail page](https://www.bose.com/p/earbuds/bose-quietcomfort-ultra-earbuds-2nd-gen/QCUE2-HEADPHONEIN.html) | HTTP 200, no redirect; exact second-generation earbuds; Add to Cart present. |
| ISOtunes FREE 2.0 | [FREE 2.0](https://isotunes.com/products/isotunes-free-2) | HTTP 200, no redirect; microphone-equipped FREE 2.0, not Listen Only. |
| ISOtunes LINK 2.0 — Headband | [LINK 2.0](https://isotunes.com/products/isotunes-link-2) | HTTP 200, no redirect; headband model IT-48, not Helmet Mount. |
| ISOtunes PRO 2.0 | [PRO 2.0](https://isotunes.com/products/isotunes-pro-2) | HTTP 200, no redirect; exact model, with color variants and Add to Cart. |
| JBL Endurance Peak 4 | [Endurance Peak 4](https://www.jbl.com/ENDURANCE-PEAK-4.html) | Curl 403; web reader retrieves exact Peak 4 retail page with Add to Cart. No wrong-model redirect. |
| JLab Work Buds | [Work Buds In-Ear Headset](https://www.jlab.com/products/work-buds-in-ear-headset) | HTTP 200, no redirect; exact in-ear model with detachable boom, not JBuds Work over-ear. |
| Shokz OpenComm2 2025 Upgrade | [OpenComm2 2025 Upgrade](https://shokz.com/products/opencomm2-2025-upgrade) | HTTP 200, no redirect; exact mobile headset, not UC bundle. Stock unspecified: extracted page contains both Sold out and Add to Cart. |
| Shokz OpenRun Pro 2 | [OpenRun Pro 2](https://shokz.com/products/openrunpro2) | HTTP 200, no redirect; exact model with size/color choices and Add to Cart. |
| Sony LinkBuds Open (WF-L910) | [WF-L910/B](https://electronics.sony.com/audio/headphones/all-headphones/p/wfl910-b) | Curl 403; web reader retrieves exact LinkBuds Open black retail page with Add to Cart. Not LinkBuds Fit or Clip. |
| soundcore AeroFit 2 | [A3874 AeroFit 2](https://www.soundcore.com/products/a3874-aerofit-2-open-earbuds) | HTTP 200, no redirect; exact AeroFit 2, not AeroFit 2 Pro; buying controls present. |

## App and policy destinations

- [Google Play](https://play.google.com/store/apps/details?id=com.vocari.vocari2): HTTP 200, no redirect, title “Vocari - Apps on Google Play”. The public listing identifies package `com.vocari.vocari2` and developer ScalarLabs, LLC.
- [ScalarLabs Privacy Policy](https://scalarlabs.ai/privacy/): HTTP 200, no redirect, matching “Privacy Policy | ScalarLabs” title.
- [ScalarLabs Terms of Use](https://scalarlabs.ai/terms/): HTTP 200, no redirect, matching “Terms of Use | ScalarLabs” title.

No catalog link replacements are needed based on this check. Availability, prices and regional delivery can change; the website correctly avoids fixed stock/price promises. These checks establish link destination identity only, not Vocari compatibility. No purchases, cart actions or website edits were made.
