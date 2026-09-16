# Catalog maintenance

## Commercial/editorial policy
Drive downloads and expected net affiliate income through suitable choices, trusted merchants and clear explanations. Do not optimize only for percentage or ticket price. Preserve all four market categories; up to five well-supported products/category, without padding. Products may span categories. Default order is alphabetical, not a performance or earnings ranking.

## Research and test evidence
The original catalog contained six records in earbuds/app.js (EarFun Air Pro 4+, Samsung Galaxy Buds4 Pro, JLab Work Buds, Shokz OpenComm2 UC, ISOtunes PRO 3.0, 3M PELTOR WS ProTac XPI). No actual product image or active affiliate configuration existed. Its HTML initially displayed zero and JavaScript supplied the cards. The preview recovers JLab Work Buds and the relevant Shokz/ISOtunes product families; old leads remain in baseline history, not mandatory recommendations. No broad platform badge is proof of app compatibility.

Current ten candidates are sourced from official manufacturer purchase/spec pages (URLs in each record and docs/PRODUCT_RESEARCH.md). No live prices are copied. Ordinary direct purchase links remain useful before affiliate activation. Check region, model, microphone, return policy and availability periodically and before publishing.

All public statuses are `untested`: no complete publishable compatibility evaluation established. Canonical app TEST_LOG has limited 2026-08-28 observations naming “Bose QC Ultra 2 Earbuds” and JBL Endurance Peak4, but subjective bidirectional audio completeness and exact Bose retail mapping are not fully established. Do not erase that evidence or turn it into certification. Clay can authorize a carefully scoped limited-evidence label after mapping the exact model and confirming what can be published. A fully tested label needs exact models/phones/OS/app commit, dates, both audio directions, routing, stability, recovery, conditions and limitations.

Keep microphone noise suppression separate from listening ANC. ISOtunes ratings are US NRR: FREE 2.0 foam 25 dB / supplied double-flange silicone 22 dB; PRO 2.0 27 dB; LINK 2.0 headband 25 dB. No SNR conversion. Do not transfer ratings to Helmet Mount or Listen Only variants. Open-ear and ordinary ANC are not protective certification. JBL's official sources disagree on HFP version; display profile support without a version.

## Edit products and links
`content/products.json` is the sole catalog/destination source. Keep stable IDs. Fields: exact brand/name, categories, type, short intended use, sourced features, consideration, testStatus/evidence, purchase, image/permission and research date. Source copy should be concise paraphrase rather than pasted marketing text.

`purchase.url` is the default full destination. `affiliate:false`, `network:null`, `activation:pending` means an ordinary link. When a program approves the property, save its complete issued URL in `purchase.placements.catalogcard` (or purchase.url), set affiliate true/network name/activation active, and retain any merchant-required disclosure. Do not invent IDs or change signed/encoded parameters. No `/go` redirects are implemented: GitHub Pages has no server-side click recorder and networks may restrict redirects. Use link builders to set permitted placement labels; no user identifiers.

The generator checks HTTPS destinations, network names on affiliate links, evidence for tests, and grants for product images. Validate clicks after edits. The disclosure automatically reflects the actual mix of affiliate and normal links, and adds the required Associate statement when an approved active Amazon destination is present. Never set affiliate true before actual enrollment. Test labels use untested/limited/tested; anything beyond untested needs testEvidence with date, summary and public report URL describing the setup, conditions and limitations.

## Images
Bose/JBL owner-supplied photo edits were reviewed and approved for publication on 2026-09-16; see PRODUCT_PHOTO_GRANTS.md. The other eight product photo slots await permission. Uncleared cards retain real manufacturer-gallery links. To activate: obtain owner photo or approved program creative, record provenance/rights in docs/ASSETS.md, populate image src/alt/width/height and imagePermission approved + grant. Follow contract restrictions on caching, hosting, modification, region, expiry and linking. Amazon content requires its approved mechanism and refresh rules; do not copy static Amazon photos into this repository.

## Placements and measurements
Each card has stable product ID and `catalogcard` placement. Approved per-placement URLs can use network-issued tracking IDs/subIDs as allowed. `vocari:product-click` emits {productId, placement, affiliate} in browser memory only. It does not send/store anything; no click/visit dataset exists. No clicks or sales are claimed.

Target metric: `100 × finalized net affiliate commission / actual product-page visits`, with consistent date window, attribution maturity, currency and scope. Currently /earbuds/ is the product-page visit unit. Get aggregate visits only through an explicitly approved privacy-reviewed analytics or host reporting solution; do not substitute outbound clicks as the denominator. Network reports establish approved sales and commission, including returns/reversals. Do not collect PII, visitor IDs or conversation data. Compare conversion and net commissions, not just public program rates. No analytics or account setup was silently added.
