# Vocari affiliate research — 2026-09-16

Initial public-source research only: no account was created, application submitted, agreement accepted, credential accessed, or third party contacted during that research. See [the activation status record](AFFILIATE_STATUS.md) for current owner-confirmed stages. Read ScalarLabs Global AGENTS.md and confirmed SCALARLABS_VAULT.md. This is an operator handoff, not website copy; public rate references are recorded here for maintenance and excluded from Pages; private negotiated terms and performance data must remain outside this public repository.

## Current program facts and application routes

| Program | Primary-source finding | Owner application action |
| --- | --- | --- |
| Amazon US Associates | Headphones are currently 3% of qualifying revenue. Standard session generally ends at the earliest of 24 hours, an order, or a competing affiliate click; additional cart rules apply. | Open [Amazon Associates signup](https://affiliate-program.amazon.com/signup), sign in with the owner-controlled Amazon account, register `https://getvocari.app` as the actual website, describe the editorial guide accurately, supply requested business/payee/tax details in Amazon only, review the agreement, and submit personally. Generate product links and assigned tracking IDs in Associates Central. |
| Soundcore US / CJ | Official page lists CID **7382109**, 3–15% on approved sales excluding returns/cancellations, and 30-day cookies. A separate 2% graphic is explicitly a conversion-rate claim, not the commission. The publisher's actual offer remains to be obtained. | Follow [Soundcore’s official affiliate page](https://www.soundcore.com/become-an-affiliate) or its [CJ signup link](https://public.cj.com/signup/publisher?pageId=dc6d7aca-a971-4b78-8e59-483bd74821b4). Create/reuse the owner's CJ publisher account; add getvocari.app as the promotional property; locate Soundcore CID 7382109, review the US terms and submit. |
| Shokz US / Impact | Official page advertises average/minimum 5%, up to 10%, 30-day cookie. Terms say the commission depends on referral-site type and new/existing customers; cancellations/refunds or competing attribution can reverse commission. Treat the actual Impact contract as decisive. | Use [Shokz’s official page](https://shokz.com/pages/become-an-affiliate), whose Apply Now points to [Shokz US on Impact](https://app.impact.com/campaign-promo-signup/SHOKZ-US.brand). Owner signs up/signs in, registers the website media property, reviews contract, applies. The link destination was observed; the web fetch encountered a redirect loop, so the application form was not inspected. |
| ISOtunes US / FlexOffers | [FlexOffers’ current listing](https://www.flexoffers.com/affiliate-programs/isotunes-us-affiliate-program/) says 4% of sales excluding blacklisted codes, 30-day cookies; updated August 27, 2026. | Register/reuse the [FlexOffers publisher account](https://publisherprobeta.flexoffers.com/signup/accountInfo), add getvocari.app as the traffic source, search **ISOtunes US** in Advertisers, verify it is active for that source, review restrictions and apply. The public template exposes both Active and Deactivated labels, so do not infer account-level availability from its HTML. |
| Sony US / direct CJ | [Sony’s own affiliate page](https://electronics.sony.com/affiliate) explicitly offers free CJ enrollment and supplied promotional materials; public rate unspecified. Its signup redirects to [CJ advertiser 6068899](https://public.cj.com/signup/publisher?advertiserId=6068899). | Prefer checking the direct CJ offer first. Add the same website property and apply to Sony after reviewing its US contract. Compare its real net terms against the FlexOffers route before activating a destination. |
| Sony US / FlexOffers | [FlexOffers listing](https://www.flexoffers.com/affiliate-programs/sony-affiliate-program/) says 2.4% online sales, 14-day cookie, last updated July 14, 2025. | In FlexOffers, search Sony Electronics, inspect current offer and exclusions, apply for the approved traffic source. This is a separately published route, not proof of Sony direct CJ terms. |
| Bose US | Direct CJ rate and current merchant-specific application route were **not confirmed from an accessible Bose/CJ primary page**. A verified [FlexOffers listing](https://www.flexoffers.com/affiliate-programs/bose-com-us-affiliate-program/) advertises 2.4% online sales and 30-day cookies, dated February 3, 2025. | Owner can inspect **Bose US / Bose.com** within the [CJ publisher account](https://www.cj.com/publisher) and compare with FlexOffers before applying. Confirm region, acceptance, and actual rates in the dashboard. Do not present a direct 3%/5% rate as verified. |
| JBL US | Prior claim of a direct 6% program remains **unconfirmed**. Search results for other regions and unrelated resellers do not establish a US JBL offer. | Keep normal verified retail/manufacturer links until owner obtains an approved US network offer. Do not invent a JBL affiliate tag or advertise an affiliation. |

Amazon sources: [headphone rate table](https://affiliate-program.amazon.com/help/node/topic/GRXPHT8U84RAYDXZ), [program policies](https://affiliate-program.amazon.com/help/operating/policies). Its [application review guidance](https://affiliate-program.amazon.com/help/node/topic/G8TW5AE9XL2VX9VM) requires at least three qualifying sales within 180 days; personal purchases do not qualify. Amazon reviews every declared site and expects substantive original public content (its suggested benchmark is ten posts). Do not manufacture purchases or posts simply to meet a threshold. Do not start the clock against an unfinished preview.

## Earnings strategy — inference, not a revenue forecast

There is not enough evidence to name the highest-earning merchant for Vocari. No actual site traffic, merchant conversion, order values, accepted rates, reversal rates, or payout costs were supplied.

Use `expected net earnings = qualified outbound clicks × approved conversion rate × average net commission per approved order − attributable fees/costs`. If starting from gross orders, account for exclusions, cancellations, returns, attribution loss, and network deductions once; do not double-subtract reversals from an already net figure. Compare paid/locked earnings per qualified click by product, placement and merchant after the applicable attribution/locking periods.

Practical sequence: establish Amazon as a broad retail baseline; obtain direct Soundcore and Shokz offers; apply to ISOtunes for relevant industrial products; compare Sony CJ with FlexOffers; verify Bose/JBL rather than assuming rates. This sequence is an operating hypothesis based on breadth, product relevance, and public offers, not a sales ranking. A higher rate can lose to a lower rate with better conversion or availability. Keep compatibility evidence and editorial ordering independent of commission. Never use a commission advantage to imply a product is tested or more compatible.

## Tracking rules and static-site implementation

- **Amazon:** use assigned `tag` / approved tracking IDs, never a made-up suffix. Its policies expressly prohibit tying sub-tags or reports to an individual visitor. Use placement-level labels only. Do not add an invented generic `subid`. [Policy source](https://affiliate-program.amazon.com/help/operating/policies).
- **CJ (Soundcore, direct Sony, Bose if accepted):** preserve the complete network-generated URL, including the correct promotional property PID and creative AID. CJ publicly documents optional SID for placement attribution, but the current character limit and generic mutation rules were not located in accessible primary docs. Use the account’s link/deep-link builder and SID field; do not make up PID/AID values. [CJ ID guide](https://junction.cj.com/article/identification-its-everywhere), [CJ SID reference](https://junction.cj.com/article/cj-account-manager-top-notch-tactical-tips), [publisher link tools](https://www.cj.com/publisher).
- **Impact / Shokz:** `subId1`, `subId2`, `subId3` for partner-only reporting; `sharedId` visible to merchant too. All support 255 characters; current docs say alphanumeric and explicitly letters/numbers only for sharedId. For example, page/product/placement values `earbuds`, `opencomm2`, `cardprimary`. No PII. Use an issued tracking URL; custom label parameters are not affiliate credentials. [Impact rules](https://help.impact.com/partner/what-would-you-like-to-learn-about/platform-features/tracking/tracking-links/link-parameters/sub-id-and-shared-id-parameters-explained-for-partners).
- **FlexOffers:** five documented sub-ID parameters are `fobs`, `fobs2`, `fobs3`, `fobs4`, `fobs5`; campaign groups use network-generated `fot`. Links → Link Search → View Link → Add SubIds generates the URL. For products, Links → Product Search requires the traffic source and advertiser catalog. [Sub-ID instructions](https://supportbeta.flexoffers.com/knowledge/how-do-i-modify-my-link-adding-campaign-ids-or-subids), [product links](https://supportbeta.flexoffers.com/knowledge/how-to-create-a-product-widget-and-get-product-links).

Store approved full public tracking URLs per product/merchant and a short placement ID, keeping a normal verified destination when no approved link exists. Mark actual affiliate links `rel="sponsored noopener"` (if new window). Use clear disclosure near purchase links. Never put API secrets, account passwords, tax records, negotiated contracts, or private performance data in static assets or the public repo. Manual URL activation avoids introducing a tracking SDK or dependency just to earn commission. UTM values alone do not establish affiliate attribution.

## Image/content permissions

- Manufacturer photos are not licensed for commercial reuse merely because their product page is public.
- **Soundcore:** supplied affiliate feed content may be posted; other website copy/images need case-by-case program-manager permission. Use approved feed/creative assets after enrollment. [Official FAQ](https://www.soundcore.com/become-an-affiliate).
- **Shokz:** offers promotional assets after approval, but the public page does not grant blanket rights to download arbitrary catalog photos. Its terms require prior written consent for materials referring to its program; confirm scope before publishing affiliate copy. Only program-provided coupons may be advertised. [Official terms](https://shokz.com/pages/become-an-affiliate).
- **Sony:** direct program supplies banners/materials; the exact grant, permitted transformations and hosting/caching rights remain contract-dependent. [Official program](https://electronics.sony.com/affiliate).
- **Bose:** commercial copying/posting of website content requires express prior consent. Use approved affiliate creatives or separately licensed imagery. [Bose terms, §2](https://www.bose.com/legal/terms-of-use).
- **JBL:** no usable affiliate image grant verified. Site terms reserve content/marks rights. [JBL terms](https://www.jbl.com/terms/terms-of-use.html).
- **ISOtunes / FlexOffers:** approved product feeds can include images, but this does not confirm per-brand rights for arbitrary downloads, modifications or caching. Inspect the accepted merchant/feed agreement. [FlexOffers feed guidance](https://supportbeta.flexoffers.com/knowledge/data-feeds-subscriptions).
- **Amazon:** Product Advertising Content has restrictive approved access/use terms: no caching image files; image links at most 24 hours; relevant content links only to Amazon. A manually copied catalog image is not covered by simply joining Associates. Avoid an API/image integration until eligible and approved. [IP license in policies](https://affiliate-program.amazon.com/help/operating/policies).

For the current preview, use existing assets with known rights, owner photographs, or original category illustrations clearly identified as illustrations; do not invent product photos. Retain source/license/permission provenance when approved product images arrive.

Once actually enrolled, Amazon requires the prominent statement: “As an Amazon Associate I earn from qualifying purchases.” Do not claim current participation before it exists. [Operating agreement §5](https://affiliate-program.amazon.com/help/operating/agreement).

## Application text for owner review

**Website description:**

“getvocari.app is the website for Vocari, a nearby voice communication app. Our earbud and headset guide helps visitors understand the Bluetooth microphone and audio capabilities to look for, compare product categories, and find manufacturer or retailer product information. We distinguish documented hands-on Vocari testing from untested candidates and support the guide with practical setup and educational articles. We are applying to monetize relevant product links through a clearly disclosed affiliate relationship.”

**Promotional methods:**

“We plan to use contextual product links and approved product creatives on getvocari.app, primarily within our earbud/headset guide and relevant educational articles. Visitors will arrive through the website, direct referrals and organic search. We will link to the appropriate product page and keep compatibility claims tied to evidence. Our application does not include paid search, coupon distribution, browser extensions, incentivized clicks, email campaigns or social-media promotion.”

The description must match what is publicly live when applying. Until the redesigned guide/articles are approved and published, call them planned, not already live. Answer quantitative fields only with owner-provided measurements; use “not yet measured” or the actual allowed new-site option where truthful. Do not invent monthly traffic, audience size, an operating history, affiliation, conversions, test results or sales promises. Owner must supply accurate legal/business identity, country, contact, payment/tax details, current traffic if required, and personally accept terms. No forms were inspected behind authentication, so exact field labels beyond documented network navigation may vary.


## Live-site application answers and next steps — 2026-09-16

The redesign is now public at https://getvocari.app, deployed from commit `617496783a81b8eaff11f84cc644e937fe3e1f63`. Earlier preview-only wording in this research is historical. The live site has ten researched candidate products, three original guides, setup/support, and policy links. All product destinations remain ordinary manufacturer links. There is no installed analytics service and no measured traffic claim. Application form labels below are suggested mappings; the current authenticated form has not been inspected.

Clay requested guided activation in this order: Amazon Associates, CJ, FlexOffers, Impact. Clay completes sign-in, agreements, identity verification, tax and payment information in provider websites. Approved link integration and publishing are authorized once the program/property/merchant permits those specific links. Do not label provisional enrollment as final approval. Track stages and live evidence in [AFFILIATE_STATUS.md](AFFILIATE_STATUS.md); record no private account information.

### Start with Amazon US Associates

Exact application route: [Amazon US Associates signup](https://affiliate-program.amazon.com/signup). If already enrolled, use [Associates Central](https://affiliate-program.amazon.com/) with the existing account rather than creating a duplicate. This is the US program for Amazon.com links; owner confirms the appropriate marketplace before applying elsewhere.

| Application topic, if asked | Prepared answer |
| --- | --- |
| Public business/publisher name | ScalarLabs |
| Legal entity, payee, address, telephone, tax status | Owner supplies the exact legal details directly to Amazon. Do not assume ScalarLabs is the legal payee or invent a corporate suffix. |
| Website name | Vocari |
| Website URL / Website and Mobile App List | https://getvocari.app/ — the property hosting the links. Do not add the Vocari mobile app or scalarlabs.ai unless links will actually be placed there and those properties are separately eligible. |
| Preferred Associates Store ID | Request `getvocari` if available. This is a proposed label, not an issued ID; use only Amazon's actual assigned ID in generated links. |
| Site type | Content / niche website with original educational articles and an equipment guide; choose the closest option actually offered. |
| Topics | Bluetooth earbuds and headsets; nearby voice communication; setup and compatibility guidance. |
| Product categories | Electronics / headphones / headsets, where offered. |
| Intended audience | Adults researching earbuds or headsets for everyday, professional, sports and suitable industrial contexts. The website is not directed primarily at children under 13. |
| Reason for joining | Earn affiliate commissions from relevant equipment links while helping readers choose suitable earbuds and headsets. |
| Promotion | Planned organic search and direct visits to educational and product-guide pages. Only select other channels if the owner actually uses them. |
| Current monetization | No active affiliate links or paid advertising on getvocari.app. Ordinary manufacturer purchase links are already present. |
| Link creation, if asked | Links inserted manually into a custom static website. |
| Traffic, sales, existing audience | Not yet measured in the current website setup. Use real owner measurements if available; do not equate unknown with zero or fabricate a number to fit a required field. |
| How you heard about the program | Owner answers truthfully; do not select a referral or relationship that did not occur. |

**Copy-ready site/content description:**

> ScalarLabs publishes getvocari.app, the website for Vocari, a nearby voice communication app. We publish original setup guides, practical use cases, and a researched guide to Bluetooth earbuds and headsets for personal, professional, sports, and industrial settings. The guide explains microphone and audio requirements and distinguishes manufacturer specifications from documented Vocari testing. Products without completed compatibility evidence are clearly labeled untested. We plan to use relevant, clearly disclosed Amazon product links to help readers find equipment. Our current site includes ten product candidates and three original guides.

**Short version for a smaller field:**

> Vocari by ScalarLabs publishes practical guides to nearby voice communication and Bluetooth earbuds and headsets. We help readers compare documented features, understand compatibility limits, and find suitable equipment through clearly disclosed product links.

**Enrollment versus final approval:** [Amazon's application-review guidance](https://affiliate-program.amazon.com/help/node/topic/G8TW5AE9XL2VX9VM) says review follows at least three qualifying sales within 180 days; personal purchases do not count. Amazon recommends substantial original content, with ten posts as a rule of thumb. This site currently has three guides, so approval is not assured. Do not claim ten posts or manufacture purchases. Record initial enrollment, permission to use issued links, and final review as distinct stages. If the owner wants to wait for final review before any links go live, explain that this prevents this site from producing the qualifying referrals needed for that review.

### Generate the first Amazon product link when permitted

1. Owner confirms that Amazon has enrolled the account, lists getvocari.app, and permits Special Links. Record final review separately if it is still pending.
2. In Associates Central, use Account Settings → Manage your Tracking IDs to create a site/placement label if desired. Request a label such as `vocaricatalog`, subject to Amazon availability and format. Record only the actual issued public tracking ID embedded in a link; never invent the suffix or reuse an ID from an example.
3. Sign in to Amazon.com with the enrolled account. Find the exact model and variant from our catalog. Begin with JLab Work Buds if an exact listing is available; otherwise choose another exact catalog match. Manufacturer gallery links are not Amazon listings and cannot simply be given a tag.
4. On that product page, use SiteStripe → Get Link → Text. Select the correct issued tracking ID and copy the full generated link when offered. Amazon's generated short link is also acceptable; its destination and attribution need verification. [Official SiteStripe instructions](https://affiliate-program.amazon.com/help/node/topic/GJMMT7G4C8K4Y3AY).
5. Supply only the product name and public generated affiliate link. No login URL, session cookie, password, API key, private dashboard/report or bank/tax record is needed.
6. The implementation must preserve the issued URL, use an accurate retailer CTA (for example View at Amazon), label the affiliate link, and render `rel="sponsored noopener"`. Add the required disclosure before product cards: “As an Amazon Associate I earn from qualifying purchases.” Also retain clear commission language. [Amazon disclosure requirement](https://affiliate-program.amazon.com/help/operating/agreement).
7. Check the exact model/variant, selected tracking ID and generated markup in preview. Commit the real output, publish through the existing main/Pages workflow, wait for deployment, and verify the live card's href, destination, retailer text and disclosures on desktop/mobile. Only then mark that product's live-link status monetized. This does not mean a sale occurred.
8. Use the issued tag and Associates reporting for attribution. Amazon says its Link Checker is for manually created/modified links and is not the validator for links generated by Associates Central. [Official link-tagging guidance](https://affiliate-program.amazon.com/help/node/topic/G6253GFSARDQENZR). A working destination and correct tag do not prove an eventual commission; finalized network reports do.

### Activation implementation notes

Read-only inspection found two changes required before the first affiliate activation: `scripts/catalog.py` currently ignores `purchase.activation` when choosing a placement override, and its CTA names the product brand even if the destination is another retailer. Add a small validation gate for active/approved link configuration and an explicit retailer label. Preserve current manufacturer URLs for fallback. Use the same validated affiliate state for card labels and disclosure. Update the privacy landing page's future-tense affiliate wording at first activation. Keep testing status and image rights independent of commercial activation.

The existing browser product-click event is memory-only; it provides no stored click, visit, sale or revenue measurement. Issued network links can provide provider-side attribution without installing a tracker on the site. Do not call the existing event analytics or invent a sales result. Do not copy Amazon product photos, prices or reviews as part of text-link activation.

### Continue in the requested order

After the Amazon application/link stage is resolved, continue through CJ, FlexOffers and Impact with the same truthful business/site description. Network acceptance and each merchant's permission are separate checkpoints. Use the official entry routes above, and record network/property review and merchant review separately. Select a single approved primary destination per card; do not overwrite an existing approved link merely because another program accepts the site. Keep all unapproved products on ordinary manufacturer links.


Official next-program routes rechecked 2026-09-16:

| Step | Entry route | After sign-in / onboarding |
| --- | --- | --- |
| CJ | [Publisher signup](https://public.cj.com/signup/publisher) | Register getvocari.app as the content property. Then apply separately to Soundcore CID 7382109 and Sony advertiser 6068899 using their branded routes above. An account or branded signup does not itself prove merchant acceptance. |
| FlexOffers | [Publisher signup](https://publisherprobeta.flexoffers.com/signup/accountInfo) | Owner verifies email/mobile and site ownership. After network/traffic-source review, use Advertisers to apply to ISOtunes US and evaluate Sony/Bose offers for getvocari.app. [Official advertiser steps](https://supportbeta.flexoffers.com/knowledge/how-do-i-apply-for-advertiser-programs). |
| Impact / Shokz | [Shokz US direct application](https://app.impact.com/campaign-promo-signup/SHOKZ-US.brand) from [Shokz's official program](https://shokz.com/pages/become-an-affiliate) | Reuse the owner's Impact partner account if present, register/verify the website property and apply to Shokz. If starting through the general network, use [Impact sign-in / Partner signup](https://app.impact.com/login.user). Direct brand acceptance and full marketplace access are distinct. |

Use the actual current form options and owner-confirmed traffic. No universal traffic minimum or merchant approval is inferred. Copy-ready descriptions above can be reused with the selected merchant/network name replacing Amazon; do not claim existing enrollment, negotiated terms or accepted image permissions.
