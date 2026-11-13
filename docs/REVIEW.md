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

## Affiliate activation preparation — 2026-09-16
Clay requested sequential Amazon/CJ/FlexOffers/Impact onboarding, owner-only secure identity/agreement/payment actions, and publication of authorized affiliate links after permission is established. Added a non-sensitive stage record and current live-site application answers. All products remain ordinary manufacturer links. Read-only inspection found that the catalog generator ignores the activation field and hardcodes the product brand in the purchase CTA; these must be corrected before first retailer/affiliate activation. No private account data or new runtime feature is introduced. These website findings do not change mobile-app behavior or architecture.


## Amazon link audit and disclosure — 2026-09-16

Clay requested conversion of existing Amazon URLs to the owner-supplied tracking ID `vocari-20`, the exact Associates disclosure, preservation of all non-Amazon destinations, and production deployment. The live `/earbuds/` HTML fetched on this date was byte-identical to the checked-in catalog at `83131782bdfdd282ac5346a1f50fc62efd1680e3` (production `617496783a81b8eaff11f84cc644e937fe3e1f63`). Its 51 anchors include ten purchase buttons, all direct manufacturer links, and zero Amazon or shortened Amazon URLs. Source and rendered HTML agree; JavaScript does not rewrite/intercept purchase navigation. There are therefore zero eligible Amazon links to convert. Replacing manufacturer URLs or choosing Amazon listings would expand the requested scope and change destinations, so all catalog URLs remain unchanged. No `Paid link` labels are added to ordinary manufacturer links.

The requested sentence, “As an Amazon Associate I earn from qualifying purchases.”, is appended to the existing visible `#disclosure` paragraph immediately above the product grid, below filters and candidate count. Existing text continues to explain that the current buttons are ordinary manufacturer links. This disclosure does not activate commission tracking. No styles, scripts controlling browser behavior, catalog records, or other public pages change. The public tracking ID is owner supplied; final program review and private account setup remain unconfirmed.

Validation before publication: `python3 scripts/build.py` and `git diff --check` passed. HTML comparison proved that the only public markup change is the disclosure paragraph; all 51 anchors and all catalog records, styles, filter JavaScript and menu JavaScript remain identical. Isolated Chromium passed 39 checks at 1440×1000, 390×844 and 320×844: disclosure visibility/readability (12.16 px text, 5.19:1 contrast), no horizontal overflow, all category/style/status/search/sort/reset/history controls, keyboard/mobile navigation, and no-JavaScript catalog behavior. All ten desktop purchase buttons plus one at each mobile width navigated to the exact original URL and emitted unchanged click-event metadata. Retailer requests were intercepted locally for these button tests; retailer content/redirects were not retested because no purchase link changed. No JavaScript page errors. Desktop and mobile screenshots were visually reviewed. Local evidence: `/private/tmp/vocari-affiliate-preview-report.json` and sibling viewport PNGs.

Production deployment uses the existing GitHub Pages source `main` at repository root, with `getvocari.app` retained. Clay's current request explicitly authorizes this commit and deployment. Post-deployment evidence will be recorded after the build completes.

## Remove repeated untested card badges — 2026-09-17

Clay requested removal of the repeated “Untested with Vocari” notices, reviewed the updated preview, and explicitly approved publication and commit. The card renderer omits only the untested badge. All ten records retain their underlying untested status, status filters, evidence validation and page-level compatibility explanation. Future evidence-backed limited/tested badges remain available.

Pre-publication validation: the static generator and git diff --check pass. Generated catalog HTML is byte-identical to production after removing exactly ten badge spans. Product information, all purchase links/tracking, photographs, CSS, JavaScript, other pages and the FlexOffers verification tag are unchanged. Browser checks passed for search, status/category filters, keyboard reset, browser Back and the mobile menu. Desktop 1440 × 1000 and mobile 390 × 844 layouts have no horizontal overflow.

Only scripts/catalog.py, earbuds/index.html and these catalog/review notes are included in this production commit. Eight new product-photo drafts remain private pending source permissions; no new photo is published here. The separate corporate and mobile-app repositories are untouched. No mobile engineering or architecture finding resulted.


## Wired-support audit — 2026-09-24 — pending Clay review

Branch: `codex/wired-support-site-update`; starting website HEAD: `27185210718596a257bb17f6251c2754b8ff4a41`; initial worktree clean. No commit, push, deployment or GitHub Pages change authorized or performed.

Evidence: read-only inspection of the protected mobile-app tag `known-good/vocari-pass-full-2026-09-22`, peeled to commit `daa91cba2cfa1da94769753e8abd638db27f7ed4`. Its commit message records Clay's 2026-09-22 physical validation of Bluetooth and wired-headset audio in both directions. This is the accepted physical result, not an inference from a passing website build. It does not establish universal wired compatibility or certify any catalog product. The mobile-app checkout and release directory were not modified. ScalarLabs Global AGENTS.md and the adjacent vault marker were read; neither was modified. The project-local AGENTS.md product summary was corrected.

Scope: audited repository source, generated pages, metadata, instructions and maintenance documents for wired exclusions and Bluetooth/HFP-only requirements. Corrected authoritative source first, then rebuilt. Compatible wired personal-audio routes are supported where the phone/platform/headset combination provides microphone input and playback. Bluetooth support, intentional handset-fallback prohibition and listen-only exclusions remain. The revised journal post still requires Clay's human review; no publication occurred.

Exact replacements below also appear in their corresponding generated pages: `content/home.html` → `index.html`; `content/pages/support.html` → `support/index.html`; `content/posts/01-your-first-nearby-conversation.json` → `updates/your-first-nearby-conversation/index.html`; `scripts/catalog.py` → `earbuds/index.html`. This review entry is the only other documentation change.

### `scripts/catalog.py`

| Exact old wording | Exact new wording |
| --- | --- |
| That’s the Bluetooth call path, not just music playback. | Music playback alone is not enough. |
| Start with Bluetooth calling. | Start with microphone and playback. |
| Look for a microphone and Hands-Free Profile (HFP). Then try both sides of a conversation on your actual phone. Wired audio and listen-only models are outside the current support scope. | For Bluetooth headsets, look for a microphone and Hands-Free Profile (HFP). Compatible wired personal-audio routes are supported where the phone/platform/headset combination provides microphone input and playback. Then try both sides of a conversation on your actual phone. Listen-only models are outside the current support scope. |

### `content/home.html`

| Exact old wording | Exact new wording |
| --- | --- |
| Each person needs Vocari, a compatible phone, and a Bluetooth headset with a microphone. | Each person needs Vocari, a compatible phone, and a compatible Bluetooth or wired headset with microphone input and playback. |
| Pair a compatible Bluetooth headset to each phone. | Pair a compatible Bluetooth headset or connect a compatible wired headset to each phone. |
| Bluetooth connects each headset to its phone. | Each headset connects to its phone through a compatible Bluetooth or wired personal-audio route. |
| You need a Bluetooth headset that supports simultaneous microphone and playback using the Hands-Free Profile (HFP). | Bluetooth headsets need simultaneous microphone and playback using the Hands-Free Profile (HFP). Compatible wired personal-audio routes are supported where the phone/platform/headset combination provides microphone input and playback. |
| Bring two compatible phones and Bluetooth headsets. | Bring two compatible phones and Bluetooth or wired headsets with microphone input and playback. |

### `content/pages/support.html`

| Exact old wording | Exact new wording |
| --- | --- |
| Pair a compatible Bluetooth headset to each phone. | Pair a compatible Bluetooth headset or connect a compatible wired headset to each phone. |
| Vocari uses the Bluetooth Hands-Free Profile (HFP) for simultaneous microphone and playback. | For Bluetooth headsets, Vocari uses the Hands-Free Profile (HFP) for simultaneous microphone and playback. Compatible wired personal-audio routes are supported where the phone/platform/headset combination provides microphone input and playback. |
| One compatible Bluetooth headset with a microphone per person. | One compatible Bluetooth or wired headset with microphone input and playback per person. |
| Wired headsets, groups, and internet calls are not current features. | Groups and internet calls are not current features. |
| Check each headset’s battery, Bluetooth connection and volume. | Check each headset’s Bluetooth or wired connection and volume, and its battery if applicable. |
| Confirm the headsets are close to their paired phones and not switching to another device through multipoint. | For Bluetooth headsets, confirm they are close to their paired phones and not switching to another device through multipoint. |
| Reconnect the headset in the phone’s Bluetooth settings. | Reconnect a Bluetooth headset in the phone’s Bluetooth settings, or reconnect the compatible wired headset. |

### `content/posts/01-your-first-nearby-conversation.json`

| Exact old wording | Exact new wording |
| --- | --- |
| each person’s Bluetooth headset supplies the microphone and playback. | each person’s compatible Bluetooth or wired headset supplies the microphone and playback. |
| Pair your headset to your phone and make a normal call. | Pair your Bluetooth headset or connect your compatible wired headset to your phone and make a normal call. |
| address the headset pairing, battery or phone settings first. | address the headset connection, battery if applicable, or phone settings first. |
| Use a device with a Bluetooth calling microphone and the Hands-Free Profile (HFP). A listen-only product or a wired headset is outside Vocari’s current support scope. | For Bluetooth, use a device with a calling microphone and the Hands-Free Profile (HFP). Compatible wired personal-audio routes are supported where the phone/platform/headset combination provides microphone input and playback. A listen-only product is outside Vocari’s current support scope. |

### `AGENTS.md`

| Exact old wording | Exact new wording |
| --- | --- |
| Current product: two nearby people, simultaneous voice through Bluetooth HFP microphone/playback, no intentional handset fallback. | Current product: two nearby people, simultaneous voice through Bluetooth HFP microphone/playback or compatible wired personal-audio routes where the phone/platform/headset combination provides microphone input and playback, no intentional handset fallback. |

### Checks and remaining limits

- PASS: `python3 scripts/build.py`; second build reproduced all ten generated HTML files exactly.
- PASS: `git diff --check`, Python source compilation, all content JSON parsing, `node --check home.js` and `node --check earbuds/app.js`.
- PASS: all ten generated routes have one h1; 272 local href/src/fragment references resolve. Every page retains the same HTML element structure and attributes as starting HEAD, including all links, controls and accessibility attributes.
- PASS: catalog records and destinations, JavaScript, CSS, `_config.yml` and CNAME are byte-identical to starting HEAD. No affiliate, legal, design or architecture change.
- PASS: repeated repository-wide text search and inspection of rendered HTML text found no remaining active claim that wired audio is unsupported, deferred or out of scope, or that Bluetooth/HFP is the only supported personal-audio route. Historical old wording in this review table is intentionally retained for auditability.
- LIMIT: no Chromium/Chrome executable or Playwright/Puppeteer package was available. Keyboard/mobile navigation, interactive search/filters/reset/Back and responsive layout were not rerun in a browser. Structural/attribute equivalence and unchanged behavior/style files were verified; those checks do not prove browser behavior or wrapping of the longer copy. Earlier browser results above are historical, not results of this audit. External destinations were not retested because every link is unchanged.

### Wording deliberately unchanged

- `scripts/build.py` home metadata/structured data describes conversations through Bluetooth headsets; `content/pages/support.json` describes connecting Bluetooth headsets. These are still true, nonexclusive descriptions, not requirements that exclude wired routes.
- The headset-selection guide describes Bluetooth HFP as a calling route and manufacturer calling evidence as a reason to research a product. Its description mentions the Bluetooth call path. These remain valid Bluetooth guidance, not an assertion that wired routes are unsupported.
- The first-session guide description says “From pairing your earbuds”; its diagnostic example says “Bluetooth didn’t work”. These remain valid Bluetooth examples, while its actual instructions now include wired connections.
- “Compatible means more than Bluetooth”, radio/permission instructions, manufacturer Bluetooth specifications, affiliate application descriptions, listen-only exclusions and the current catalog's untested status remain. The accepted result does not contradict these or establish model-specific catalog certification.
- README's “A local checkpoint is not evidence of headset compatibility” remains a caution against inferring physical tests from a checkpoint alone. This task uses Clay's explicit physical validation recorded in the supplied checkpoint.
- No questionable negative wired-support claim was left active. All old exclusions retained here are explicitly historical quotations.

Stopped for Clay's approval. No commit, push, deployment or GitHub Pages modification.

## Vocari store links — 2026-11-07

The download section now links directly to the public App Store and Google Play listings. It uses the official App Store badge and Google’s Android robot, with attribution in the homepage footer. Current public pages and download metadata reflect availability on both stores.

Static generation and whitespace checks passed. All ten generated pages were checked for valid document headers, local asset and route references, and current release status. Both download buttons were checked against the official listings. The generated equipment catalog differs only in the shared availability footer.


## Exact in-app Terms publication — 2026-11-12

Clay explicitly requested publishing the current in-app Terms on ScalarLabs and directing the existing “Read the official terms of use” link to them, with no other website or app changes. This narrow publication does not include the separate November 5 legal-review drafts, which remain preserved in their original checkouts.

Prepared on Mac Air in fresh clones from GitHub main: ScalarLabsSite `27f88f0c25834d399f10deda2f9777ff64b4b27d`; Vocari website `7d58016279dcf150d9bf892ec02344368ab37d76`; task branch `codex/publish-vocari-terms-2026-11-12`. ScalarLabs adds only `/vocari/terms/index.html`. This website changes only the existing link destination in `content/pages/terms.html` and generated `terms/index.html` to `https://scalarlabs.ai/vocari/terms/`, plus this evidence entry.

Text source: Vocari-App `docs/legal/terms.txt`, version `2026-11-05.2`, unchanged from app HEAD `dff19e833b16c4dd87c07d0cd3c214e72ec5a61a`. Decoded Android and iOS embedded Terms both match its 11,507 UTF-8 bytes. SHA-256: `2ca4dc26a7c2c535d20a42d0bf5a4c32f93130158edadec91097896f53e9dc5a`. Decoding the new HTML article and reconstructing its 39 text blocks produces exactly the same bytes, including all ten numbered sections. No legal wording was edited.

Prepublication checks: source/live starting terms pages match (ignoring ScalarLabs’ existing hosting-injected beacon); static generation succeeds; each changed public Vocari file equals its baseline with one href substitution; every other generated page is unchanged. Independent text/scope review passed. New Terms page visually checked at desktop and 390-pixel phone width, with no horizontal page overflow. The existing link label and keyboard reachability are retained. Public readback and end-to-end link navigation are the remaining publication checks at this commit; these website checks make no app runtime or physical-device claim.

Documentation check: no new mobile engineering finding or architectural fact; app source and canonical app documentation remain untouched.
