# Vocari website instructions

This separate repository is the getvocari.app website, not the mobile application. Read and obey ScalarLabs Global AGENTS.md before work. Never change its file or protections. Do not modify the mobile-app repository or its release directory from website tasks.

Preserve the static HTML/CSS/JavaScript stack and GitHub Pages. Work on a codex/ branch. Inspect path, branch, HEAD and status before edits; preserve user work. main is the publishing branch: never merge, push main, or publish without Clay's explicit approval. The deployed starting baseline is 0bd97021afb41eb514dc9ac721a48f1e9d1c3851 (2026-08-05), retained by safety/live-2026-09-16. Git credentials are not stored here.

## Product and commercial direction
- Drive Vocari downloads and sustainable affiliate income from suitable earbuds/headsets. Optimize expected net commission through purchase volume, customer trust, suitability, price and returns, not rate alone.
- Product truth comes from canonical mobile-app docs, not marketing guesses. Current product: two nearby people, simultaneous voice through Bluetooth HFP microphone/playback, no intentional handset fallback. Android is on Google Play; iPhone built and submitted to Apple, with full cross-platform capability. Clay’s deployment instruction is to retain “Awaiting Apple review” until public availability is confirmed; do not add an App Store CTA without the public listing URL. Do not infer public availability solely from an upload or search results. Do not promise E2E encryption, universal compatibility, group/mesh, Internet calling or safety-critical use.
- Preserve actual Vocari branding. Use owner-provided screenshots; never invent UI, test evidence, ratings, prices, certifications, affiliate IDs, or announcements.
- Catalog categories: Sports / Activity / Exercise; Personal / Professional / Executive; Enterprise; Industrial / Manufacturing / Construction. Aim for up to five useful candidates/category; no padding. Manufacturer calling support is candidate evidence, not proof of Vocari compatibility.
- Separate listening ANC, outgoing-microphone suppression, and rated hearing protection. Record exact model/variant and NRR/SNR conditions. Do not imply open-ear or ANC products protect hearing.
- Product photos require recorded commercial-use permission or approved network creatives. Publicly visible photos are not automatically reusable. Follow Amazon's content rules. Keep placeholders until rights are documented.
- Every purchase destination lives in content/products.json; preserve approved affiliate parameters verbatim. Use ordinary links when activation is pending. No redirect or added parameter unless the program permits it. Never expose internal rates/setup details on customer pages.
- Keep disclosure near recommendations. Clicks are not sales. Eventual metric: net commission per 100 product-page visits, from real aggregate visit counts and finalized affiliate reports. No unnecessary personal data collection.
- Clay handles verification, payment/tax details and agreements. Never request or store secrets. Application drafts are preparation, not submission authorization.

## Maintenance
Read README.md, docs/CATALOG.md, docs/AFFILIATES.md and docs/REVIEW.md for catalog, image, attribution and review limits. Edit content/ and styles/scripts, then run python3 scripts/build.py. This only generates checked-in HTML and never publishes. Every journal post requires human review; no scheduled publishing. Keep docs/source excluded from Pages via _config.yml (repository itself is public, so still no private account info).

Validate affected routes, keyboard/mobile navigation, catalog search/filters/reset/back navigation, links and responsive layout. Record material findings and tests in docs/REVIEW.md. A passing site check is not evidence that an app/headset combination is physically tested.

2026-09-16 clarification: no Wi-Fi router is required, regardless of internet service. Wi-Fi must remain enabled for the direct phone connection; no shared router/network is needed. This is explicit in home, support and guides.
