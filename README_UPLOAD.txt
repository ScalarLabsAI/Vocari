VOCARI RECOMMENDED EARBUDS PAGE
===============================

Purpose
-------
Responsive static page for:
    https://getvocari.app/earbuds/

Files
-----
earbuds/index.html
earbuds/styles.css
earbuds/app.js

Current behavior
----------------
- Supports desktop, Android-sized mobile screens, and iPhone-sized mobile screens.
- Provides four requested market categories.
- Provides Android and iPhone/iOS filters.
- Clearly labels every current product as "Under Evaluation."
- Does not publish fabricated Vocari scores or active affiliate links.
- Explains why Vocari measures the full bidirectional Bluetooth communication path.
- Includes the affiliate disclosure and ScalarLabs parent-brand attribution.

Deployment
----------
Upload the entire "earbuds" folder into the web root for getvocari.app.

Expected route:
    /earbuds/index.html
Public URL:
    https://getvocari.app/earbuds/

Before public deployment, verify that these existing routes are correct:
    /
    /support/
    /privacy/
    /terms/

The "Get Vocari" button currently points to:
    https://play.google.com/store/apps/details?id=com.vocari.vocari2

Official logo
-------------
The page deliberately uses a clean text wordmark rather than inventing a new Vocari logo.
When the official logo asset is available on getvocari.app, replace the .wordmark span in
index.html with the official image. Do not use a generated substitute.

Updating products
-----------------
All product records are at the top of earbuds/app.js in the PRODUCTS array.

After a product has completed Vocari testing:
1. Change its public status from "Under Evaluation."
2. Replace the pending evaluation block with actual repeatable test results.
3. Add the approved affiliate destination URL or preferably a ScalarLabs tracking redirect:
       /go/product-slug
4. Add the approved VOCARI code only after the merchant confirms:
   - code ownership/assignment to ScalarLabs;
   - code-only attribution;
   - commission rate;
   - return/cancellation rules;
   - reporting cadence;
   - permission to publish the code.

Do not display affiliate commission percentages to customers. Public ranking should be based
on tested customer value and use-case fit.

Suggested future product data fields
------------------------------------
tested: true/false
latencyMs: measured full-path value
latencyScore: normalized public score
clarityScore
stabilityScore
noiseScore
comfortScore
batteryScore
overallScore
discountCode
dealUrl
affiliateDisclosure
testedAndroidDevices
testedIOSDevices
testDate
testMethodVersion

Recommended tracking structure
------------------------------
Public button:
    https://getvocari.app/go/earfun-air-pro-4-plus?src=earbuds-personal

Server records click, source, category, platform, and product, then sends a 302 redirect to
the merchant's approved affiliate URL.

The merchant's exclusive VOCARI code remains the primary code-only attribution mechanism.
