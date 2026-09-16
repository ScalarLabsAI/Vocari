# Website review — 2026-09-16

## Scope and state
Separate checkout `/Users/xcodetest/Documents/Projects/Vocari-Website`; branch `codex/website-refresh`; baseline `0bd97021afb41eb514dc9ac721a48f1e9d1c3851`. Mobile checkout remains `integration/active-session-ui-consolidation` at `7e98992f1011da4d2c49be5b8bac5976e37ca4df` with pre-existing untracked `release/`; website work does not modify it.

GitHub Pages deployment 5754701261 succeeded 2026-08-05 from main/baseline to getvocari.app. Safety branch retains that commit. The initial review was local. Clay subsequently approved replacing the live site and explicitly authorized merging and pushing main on 2026-09-16 (see deployment authorization below). Push credentials were unavailable at the read-only access check; local work does not require them.

## Material findings
- The original /earbuds page contains six products in JavaScript and an initial 0-candidate HTML shell. The observed zero was not evidence of no records. The new page ships all cards in HTML; filtering is progressive enhancement.
- Original /support/, /privacy/ and /terms/ destinations had no files in the website repository. Added actual support and policy landing routes; official published policies remain at ScalarLabs rather than inventing replacement legal agreements.
- GitHub Pages is static; the old README's suggested server-side 302 click recorder is not an existing capability. Approved network destinations are preserved directly; no analytics, redirects or account infrastructure added.
- No approved affiliate IDs, configured tracking or licensed product photos existed in the source. Current photos remain a documented permission gap; ordinary manufacturer links are functional.
- Canonical app documents record partial device/headset evidence and unverified full-matrix behavior. Website avoids global certification, measured latency/range, application E2E encryption, group/mesh, remote calling, and current iPhone availability claims.
- Canonical app semantics are separate from historical Google Play labels. User-facing setup uses Host/Join and QR/Join Code. Captions identify screenshots as the submitted iPhone preview.

## Owner review needed before publication
- Confirm proposed design, copy and prepared app screenshots.
- Obtain approved commercial product images (all ten slots) or provide owner photographs. Gallery links are present in the meantime.
- Complete affiliate account/merchant applications, verification, agreements and tax/payment details; activate only real issued links.
- Confirm exact store/public iPhone release status at publishing time. Latest Clay update: built, uploaded, fully cross-platform and “available.” Clarification requested for whether public App Store availability is live and its exact URL. Current neutral website copy says submitted to Apple and does not invent a store link.
- No analytics denominator exists yet; the net commission per 100 product-page visits metric remains a defined future measurement, not an implemented dashboard.

Automated and browser evidence will be appended after implementation checks.

2026-09-16 clarification: no Wi-Fi router is required, regardless of internet service. Wi-Fi must remain enabled for the direct phone connection; no shared router/network is needed. This is explicit in home, support and guides.

Clay support-copy correction, 2026-09-16: QR/Join Code troubleshooting may require completely closing/reopening both apps and starting a fresh Host session, although seldom required. This is website guidance requested by Clay, not a change to app lifecycle semantics.

## Validation result
- PASS: ten routes (home, catalog, support, privacy, terms, journal, three guides and 404) at 1440×1000, 390×844 and 320×844 in isolated Chromium 151.
- PASS: one h1 per route, title/description/canonical/JSON-LD presence, no horizontal overflow, no broken rendered images, no missing image alt, no JavaScript page errors.
- PASS: category counts 4 sports / 5 personal / 4 enterprise / 3 industrial; search; type/status combinations; honest zero results; reset focus; alphabetical/reverse order; query restoration; browser Back; invalid filter state.
- PASS: ten configured purchase destinations match rendered hrefs exactly; optional click event fires without storage; no analytics service added.
- PASS: mobile navigation opens/closes, aria-expanded, Escape/focus return, navigation link closure, keyboard FAQ disclosure, mobile download navigation.
- PASS: without JavaScript, all ten cards, purchase links and navigation remain usable.
- PASS: all local href/src references and fragments resolve across ten output pages; article-specific metadata does not inherit an unrelated image; CNAME retained.
- PASS: Git diff whitespace check; Python generation completes; no new JavaScript or Python dependency.
- Visual review: desktop home/catalog/journal and mobile home/catalog screenshots inspected. Main app screenshot is approximately 34 KB WebP; system fonts and local assets avoid remote font/analytics requests. Social card is only metadata, not page-rendered.
- External links: ten correct product identities; eight return HTTP200 directly, JBL/Sony reject curl but official web reader shows correct retail pages. Shokz OpenComm2 stock is unspecified because extracted availability is ambiguous. Google Play and ScalarLabs policy pages return HTTP200. See LINK_CHECK.md.
- Support correction confirmed in generated HTML: complete app close/reopen may seldom be necessary.
- These are website checks, not physical headset/app testing. GitHub Pages remote deployment is deliberately untested because nothing is published.

Documentation check: meaningful website findings and restrictions are recorded above; commercial policy, catalog/image/link maintenance and public application-source research are persisted in this repository. No mobile architectural facts were changed, and no mobile docs were edited.

Clay final wording, 2026-09-16: replaced “Although seldom required…” with “As a last resort, close the app completely on both phones, reopen it, and start a fresh Host session.” This supersedes the earlier frequency wording above.

## Deployment authorization — 2026-09-16
Clay approved publishing the current redesign through ScalarLabsAI/Vocari’s existing GitHub Pages deployment from main, with the previous live commit retained as a rollback reference. The mobile-app repository must remain untouched. Ordinary manufacturer links and no unlicensed product photos are approved for launch; affiliate activation and product-photo permissions are follow-up items, not deployment blockers. The three prepared guides and supplied app screenshots are included in the approved current version.

The latest explicit store instruction supersedes the earlier ambiguous availability clarification: retain “Awaiting Apple review” for iPhone until public availability is confirmed. Cross-platform support and direct phone connection without a Wi-Fi router remain current capability descriptions. Generated HTML, CSS, JavaScript, all site assets, source content and the standalone Python generator are tracked in this repository; no temporary assembly script is needed to rebuild.

Pre-deployment check: regenerated all output from tracked source; build and git diff --check passed. Home, earbuds, support and updates passed isolated Chromium checks at 1440, 390 and 320 px, including pending Apple status, canonical URLs, images, layout, catalog/search/reset/manufacturer destinations, mobile navigation, support FAQ and Google Play link; no JavaScript page errors. Mobile checkout remains unchanged at the recorded branch/HEAD with only its pre-existing untracked release directory.
