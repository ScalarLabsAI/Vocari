:root {
  --navy-950: #061526;
  --navy-900: #08233d;
  --navy-800: #0a355a;
  --blue-700: #075fbd;
  --blue-600: #0877e3;
  --blue-100: #e7f2ff;
  --cyan-500: #00a6c7;
  --green-700: #168049;
  --green-100: #e9f8ef;
  --amber-700: #9a5b00;
  --amber-100: #fff3d6;
  --ink: #15283a;
  --muted: #607286;
  --line: #d9e3ec;
  --surface: #ffffff;
  --surface-soft: #f5f8fb;
  --page: #eef4f8;
  --shadow: 0 16px 45px rgba(6, 31, 56, .10);
  --radius: 18px;
  --max: 1240px;
}

* { box-sizing: border-box; }

html { scroll-behavior: smooth; }

body {
  margin: 0;
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  color: var(--ink);
  background: var(--page);
  line-height: 1.55;
}

button, select, a { font: inherit; }

a { color: inherit; }

img { max-width: 100%; }

.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0,0,0,0);
  white-space: nowrap;
  border: 0;
}

.skip-link {
  position: fixed;
  left: 14px;
  top: -60px;
  background: #fff;
  color: var(--navy-900);
  padding: 10px 14px;
  border-radius: 8px;
  z-index: 100;
  transition: top .2s ease;
}

.skip-link:focus { top: 14px; }

.site-header {
  position: sticky;
  top: 0;
  z-index: 50;
  background: rgba(255,255,255,.96);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid rgba(10,53,90,.10);
}

.header-inner {
  width: min(calc(100% - 34px), var(--max));
  margin: 0 auto;
  min-height: 76px;
  display: grid;
  grid-template-columns: auto 1fr auto;
  align-items: center;
  gap: 28px;
}

.brand {
  display: flex;
  flex-direction: column;
  text-decoration: none;
  line-height: 1;
}

.wordmark,
.footer-wordmark {
  font-weight: 950;
  letter-spacing: .11em;
  color: var(--navy-950);
  font-size: 1.55rem;
}

.brand-section {
  margin-top: 7px;
  color: var(--blue-700);
  font-size: .70rem;
  font-weight: 800;
  letter-spacing: .08em;
  text-transform: uppercase;
}

.primary-nav {
  display: flex;
  justify-content: center;
  gap: 30px;
}

.primary-nav a {
  position: relative;
  text-decoration: none;
  font-weight: 700;
  color: #314a60;
  font-size: .95rem;
}

.primary-nav a:hover,
.primary-nav a[aria-current="page"] {
  color: var(--blue-700);
}

.primary-nav a[aria-current="page"]::after {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  bottom: -11px;
  height: 3px;
  border-radius: 3px;
  background: var(--blue-600);
}

.header-cta,
.button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  border-radius: 10px;
  min-height: 44px;
  padding: 0 18px;
  text-decoration: none;
  font-weight: 850;
  border: 1px solid transparent;
  cursor: pointer;
}

.header-cta,
.button.primary {
  background: linear-gradient(135deg, var(--blue-700), var(--blue-600));
  color: #fff;
  box-shadow: 0 8px 20px rgba(8,119,227,.24);
}

.button.secondary {
  background: #fff;
  color: var(--navy-900);
  border-color: #c6d6e4;
}

.button:hover,
.header-cta:hover {
  transform: translateY(-1px);
}

.menu-button {
  display: none;
  background: transparent;
  border: 0;
  font-size: 1.55rem;
  color: var(--navy-900);
}

.hero {
  position: relative;
  overflow: hidden;
  background:
    radial-gradient(circle at 80% 15%, rgba(0,166,199,.18), transparent 29%),
    radial-gradient(circle at 20% 0%, rgba(8,119,227,.16), transparent 34%),
    linear-gradient(180deg, #fff, #edf6fc);
  border-bottom: 1px solid #d8e6ef;
}

.hero::after {
  content: "";
  position: absolute;
  inset: auto -20% -80% 35%;
  height: 580px;
  background: repeating-radial-gradient(ellipse at center, rgba(8,119,227,.10) 0 1px, transparent 1px 14px);
  transform: rotate(-9deg);
  pointer-events: none;
}

.hero-inner {
  position: relative;
  z-index: 1;
  width: min(calc(100% - 34px), var(--max));
  margin: 0 auto;
  padding: 82px 0 70px;
  display: grid;
  grid-template-columns: 1.25fr .75fr;
  gap: 64px;
  align-items: center;
}

.eyebrow {
  margin: 0 0 12px;
  color: var(--blue-700);
  font-size: .78rem;
  font-weight: 950;
  letter-spacing: .14em;
}

.hero h1 {
  max-width: 760px;
  margin: 0;
  font-size: clamp(2.6rem, 5.4vw, 5rem);
  line-height: .99;
  letter-spacing: -.055em;
  color: var(--navy-950);
}

.hero-text {
  max-width: 730px;
  margin: 26px 0 0;
  color: #445f75;
  font-size: 1.12rem;
}

.platform-status,
.hero-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.platform-status { margin-top: 26px; }
.hero-actions { margin-top: 30px; }

.platform-chip {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 12px;
  border: 1px solid;
  border-radius: 999px;
  font-size: .88rem;
  font-weight: 800;
}

.platform-chip.available {
  color: var(--green-700);
  border-color: #a9d9bd;
  background: var(--green-100);
}

.platform-chip.planned {
  color: #51667a;
  border-color: #cbd8e2;
  background: rgba(255,255,255,.75);
}

.hero-panel {
  position: relative;
  background: rgba(255,255,255,.86);
  border: 1px solid rgba(255,255,255,.92);
  box-shadow: var(--shadow);
  border-radius: 24px;
  padding: 26px;
  backdrop-filter: blur(10px);
}

.signal-graphic {
  position: relative;
  height: 190px;
  border-radius: 18px;
  overflow: hidden;
  background:
    radial-gradient(circle at center, rgba(0,166,199,.27), transparent 34%),
    linear-gradient(140deg, #061a2c, #0b406a);
  margin-bottom: 24px;
}

.phone {
  position: absolute;
  top: 48px;
  width: 42px;
  height: 86px;
  border: 4px solid #eaf6ff;
  border-radius: 10px;
  box-shadow: inset 0 0 0 2px rgba(255,255,255,.12);
}

.left-phone { left: 66px; transform: rotate(-6deg); }
.right-phone { right: 66px; transform: rotate(6deg); }

.phone::after {
  content: "";
  position: absolute;
  left: 50%;
  bottom: 5px;
  width: 12px;
  height: 2px;
  border-radius: 2px;
  background: #a9d9ff;
  transform: translateX(-50%);
}

.signal {
  position: absolute;
  top: 69px;
  left: 50%;
  width: 52px;
  height: 52px;
  border: 3px solid rgba(66,199,255,.9);
  border-left-color: transparent;
  border-right-color: transparent;
  border-radius: 50%;
  transform: translateX(-50%);
}

.signal-two {
  width: 88px;
  height: 88px;
  top: 51px;
  opacity: .48;
}

.headset {
  position: absolute;
  bottom: 22px;
  width: 32px;
  height: 32px;
  border: 5px solid #63d8ef;
  border-bottom-color: transparent;
  border-radius: 50%;
}

.headset::after {
  content: "";
  position: absolute;
  width: 18px;
  height: 5px;
  background: #63d8ef;
  border-radius: 8px;
  top: 22px;
}

.headset-left { left: 23px; }
.headset-left::after { left: 19px; transform: rotate(12deg); }
.headset-right { right: 23px; }
.headset-right::after { right: 19px; transform: rotate(-12deg); }

.panel-kicker {
  margin: 0;
  color: var(--cyan-500);
  font-size: .78rem;
  font-weight: 950;
  text-transform: uppercase;
  letter-spacing: .13em;
}

.hero-panel h2 {
  margin: 7px 0 8px;
  color: var(--navy-950);
  line-height: 1.12;
}

.hero-panel p:last-child {
  margin-bottom: 0;
  color: #526a7e;
}

.proof-strip {
  width: min(calc(100% - 34px), var(--max));
  margin: -22px auto 0;
  position: relative;
  z-index: 3;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  background: #fff;
  border: 1px solid #d7e4ed;
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  overflow: hidden;
}

.proof-strip > div {
  min-height: 94px;
  padding: 19px 22px;
  display: grid;
  grid-template-columns: auto 1fr;
  column-gap: 12px;
  align-content: center;
}

.proof-strip > div + div { border-left: 1px solid #e2eaf0; }

.proof-icon {
  grid-row: 1 / 3;
  display: grid;
  place-items: center;
  width: 36px;
  height: 36px;
  border-radius: 10px;
  color: var(--blue-700);
  background: var(--blue-100);
  font-weight: 950;
}

.proof-strip strong {
  color: var(--navy-900);
  font-size: .92rem;
}

.proof-strip small { color: var(--muted); }

.catalog-section,
.method-section,
.disclosure-section {
  width: min(calc(100% - 34px), var(--max));
  margin-left: auto;
  margin-right: auto;
}

.catalog-section { padding: 78px 0 86px; }

.section-heading {
  display: flex;
  justify-content: space-between;
  gap: 50px;
  align-items: end;
}

.section-heading h2,
.method-section h2,
.disclosure-section h2 {
  color: var(--navy-950);
  margin: 0;
  font-size: clamp(2rem, 4vw, 3.35rem);
  line-height: 1.05;
  letter-spacing: -.035em;
}

.section-intro {
  max-width: 520px;
  margin: 0;
  color: var(--muted);
}

.category-tabs {
  display: grid;
  grid-template-columns: 1fr 1.35fr 1.4fr .8fr 1.6fr;
  gap: 10px;
  margin-top: 34px;
}

.category-tab {
  min-height: 64px;
  padding: 11px 14px;
  border: 1px solid #cfdde8;
  border-radius: 12px;
  background: #fff;
  color: #324d64;
  font-weight: 850;
  cursor: pointer;
}

.category-tab:hover,
.category-tab.active {
  color: #fff;
  border-color: var(--blue-700);
  background: linear-gradient(135deg, var(--blue-700), var(--blue-600));
  box-shadow: 0 9px 22px rgba(8,119,227,.18);
}

.category-tab span { margin-right: 6px; }

.filter-bar {
  margin-top: 16px;
  display: grid;
  grid-template-columns: repeat(3, minmax(180px, 1fr)) auto;
  gap: 12px;
  padding: 16px;
  background: #e7eff5;
  border: 1px solid #d3e0e9;
  border-radius: 14px;
}

.filter-bar label {
  display: grid;
  gap: 5px;
}

.filter-bar label > span {
  color: #516a7f;
  font-size: .72rem;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: .08em;
}

select,
.clear-button {
  min-height: 44px;
  border: 1px solid #bdcedb;
  border-radius: 9px;
  background: #fff;
  color: var(--navy-900);
  padding: 0 12px;
}

.clear-button {
  align-self: end;
  cursor: pointer;
  font-weight: 850;
}

.results-meta {
  display: flex;
  justify-content: space-between;
  gap: 18px;
  margin: 20px 2px 14px;
  color: var(--muted);
  font-size: .9rem;
}

.results-meta strong { color: var(--navy-900); }

.product-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0,1fr));
  gap: 18px;
}

.product-card {
  display: flex;
  flex-direction: column;
  min-height: 100%;
  background: #fff;
  border: 1px solid #d7e3ec;
  border-radius: 17px;
  overflow: hidden;
  box-shadow: 0 9px 26px rgba(12,48,78,.07);
}

.product-visual {
  position: relative;
  height: 180px;
  display: grid;
  place-items: center;
  overflow: hidden;
  background:
    radial-gradient(circle at 75% 20%, rgba(0,166,199,.18), transparent 29%),
    linear-gradient(145deg, #eff8fe, #e6eef5);
}

.product-visual::after {
  content: "";
  position: absolute;
  inset: auto -10% -70px 25%;
  height: 160px;
  border-radius: 50%;
  border: 1px solid rgba(8,119,227,.15);
  box-shadow: 0 0 0 18px rgba(8,119,227,.04), 0 0 0 36px rgba(8,119,227,.03);
}

.device-illustration {
  position: relative;
  z-index: 1;
  width: 136px;
  height: 92px;
}

.device-illustration.earbuds::before,
.device-illustration.earbuds::after {
  content: "";
  position: absolute;
  top: 7px;
  width: 36px;
  height: 58px;
  border-radius: 24px 24px 18px 18px;
  background: linear-gradient(145deg, #142a3d, #385872);
  box-shadow: 0 12px 18px rgba(7,31,54,.20);
}

.device-illustration.earbuds::before { left: 26px; transform: rotate(-12deg); }
.device-illustration.earbuds::after { right: 26px; transform: rotate(12deg); }

.device-illustration.open-ear {
  border: 12px solid #17364e;
  border-bottom-color: transparent;
  border-radius: 54% 54% 35% 35%;
  height: 72px;
  margin-top: 15px;
}

.device-illustration.open-ear::before,
.device-illustration.open-ear::after {
  content: "";
  position: absolute;
  top: 36px;
  width: 30px;
  height: 40px;
  border-radius: 18px;
  background: #294e67;
}

.device-illustration.open-ear::before { left: -15px; }
.device-illustration.open-ear::after { right: -15px; }

.device-illustration.boom {
  border: 11px solid #17364e;
  border-bottom-color: transparent;
  border-radius: 60px 60px 0 0;
  height: 76px;
  margin-top: 10px;
}

.device-illustration.boom::before,
.device-illustration.boom::after {
  content: "";
  position: absolute;
  top: 39px;
  width: 34px;
  height: 44px;
  border-radius: 10px;
  background: #2d526c;
}

.device-illustration.boom::before { left: -15px; }
.device-illustration.boom::after { right: -15px; }

.device-illustration.boom span {
  position: absolute;
  right: -46px;
  top: 60px;
  width: 65px;
  height: 7px;
  border-radius: 7px;
  background: #142b3d;
  transform: rotate(12deg);
}

.device-illustration.boom span::after {
  content: "";
  position: absolute;
  right: -2px;
  top: -4px;
  width: 15px;
  height: 15px;
  border-radius: 50%;
  background: #0877e3;
}

.device-illustration.hearing-protection {
  border: 15px solid #17364e;
  border-bottom-color: transparent;
  border-radius: 62px 62px 0 0;
  height: 80px;
}

.device-illustration.hearing-protection::before,
.device-illustration.hearing-protection::after {
  content: "";
  position: absolute;
  top: 34px;
  width: 42px;
  height: 58px;
  border-radius: 15px;
  background: linear-gradient(145deg, #17364e, #406984);
}

.device-illustration.hearing-protection::before { left: -23px; }
.device-illustration.hearing-protection::after { right: -23px; }

.status-ribbon {
  position: absolute;
  z-index: 2;
  top: 14px;
  left: 14px;
  display: inline-flex;
  padding: 6px 9px;
  border-radius: 7px;
  color: var(--amber-700);
  background: var(--amber-100);
  border: 1px solid #f0d596;
  font-size: .72rem;
  font-weight: 950;
  text-transform: uppercase;
  letter-spacing: .05em;
}

.priority-badge {
  position: absolute;
  z-index: 2;
  top: 14px;
  right: 14px;
  display: inline-grid;
  place-items: center;
  width: 34px;
  height: 34px;
  border-radius: 50%;
  background: rgba(255,255,255,.92);
  color: var(--blue-700);
  border: 1px solid #c9dce9;
  font-weight: 950;
}

.product-body {
  display: flex;
  flex-direction: column;
  flex: 1;
  padding: 20px;
}

.product-brand {
  margin: 0 0 2px;
  color: var(--blue-700);
  font-size: .72rem;
  font-weight: 950;
  text-transform: uppercase;
  letter-spacing: .11em;
}

.product-title {
  margin: 0;
  color: var(--navy-950);
  font-size: 1.24rem;
  line-height: 1.16;
}

.product-category {
  margin: 7px 0 0;
  color: #60768a;
  font-size: .84rem;
}

.badge-row {
  display: flex;
  flex-wrap: wrap;
  gap: 7px;
  margin-top: 14px;
}

.badge {
  padding: 5px 8px;
  border-radius: 999px;
  border: 1px solid #cad9e5;
  color: #466178;
  background: #f5f8fa;
  font-size: .72rem;
  font-weight: 850;
}

.badge.android {
  color: var(--green-700);
  border-color: #b8ddc6;
  background: var(--green-100);
}

.badge.ios {
  color: #46566a;
  background: #f3f5f7;
}

.evaluation-block {
  margin-top: 17px;
  padding: 13px;
  border: 1px solid #dce6ed;
  background: #f7fafc;
  border-radius: 11px;
}

.evaluation-title {
  display: flex;
  justify-content: space-between;
  gap: 8px;
  color: var(--navy-900);
  font-size: .82rem;
  font-weight: 900;
}

.pending-bars {
  display: grid;
  gap: 7px;
  margin-top: 11px;
}

.pending-row {
  display: grid;
  grid-template-columns: 110px 1fr;
  gap: 10px;
  align-items: center;
  font-size: .75rem;
  color: #64798c;
}

.pending-line {
  height: 7px;
  border-radius: 8px;
  background: repeating-linear-gradient(90deg, #d7e3eb 0 16px, #edf2f6 16px 24px);
}

.product-summary {
  margin: 16px 0 0;
  color: #516a7e;
  font-size: .9rem;
}

.product-footer {
  margin-top: auto;
  padding-top: 18px;
}

.pending-button {
  width: 100%;
  min-height: 43px;
  border: 1px solid #c9d8e3;
  border-radius: 9px;
  background: #edf3f7;
  color: #65798b;
  font-weight: 850;
  cursor: not-allowed;
}

.product-note {
  margin: 9px 0 0;
  color: #798b9a;
  font-size: .72rem;
  text-align: center;
}

.empty-state {
  margin-top: 20px;
  padding: 54px 20px;
  text-align: center;
  background: #fff;
  border: 1px dashed #b9cad7;
  border-radius: var(--radius);
}

.method-section {
  margin-bottom: 76px;
  padding: 44px;
  display: grid;
  grid-template-columns: .86fr 1.14fr;
  gap: 58px;
  border-radius: 24px;
  color: #fff;
  background:
    radial-gradient(circle at 85% 0%, rgba(0,166,199,.25), transparent 26%),
    linear-gradient(135deg, #06192c, #0a3e68);
  box-shadow: var(--shadow);
}

.method-section .eyebrow { color: #66d5ea; }
.method-section h2 { color: #fff; }
.method-copy > p:last-child { color: #bdd0df; }

.method-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: grid;
  gap: 15px;
}

.method-list li {
  display: grid;
  grid-template-columns: 42px 1fr;
  gap: 15px;
  align-items: start;
  padding: 17px;
  border: 1px solid rgba(255,255,255,.12);
  border-radius: 13px;
  background: rgba(255,255,255,.055);
}

.method-list li > span {
  display: grid;
  place-items: center;
  width: 38px;
  height: 38px;
  border-radius: 10px;
  background: #0a75c9;
  font-weight: 950;
}

.method-list strong { display: block; }
.method-list p { margin: 3px 0 0; color: #bdd0df; font-size: .9rem; }

.disclosure-section {
  margin-bottom: 82px;
  padding: 32px 36px;
  display: grid;
  grid-template-columns: 1.5fr .5fr;
  gap: 40px;
  background: #fff;
  border: 1px solid #d5e2eb;
  border-radius: 20px;
  box-shadow: 0 10px 28px rgba(11,48,78,.07);
}

.disclosure-section h2 { font-size: 1.65rem; }
.disclosure-section p { color: var(--muted); }

.disclosure-note {
  padding-left: 30px;
  border-left: 1px solid #dae4eb;
}

.disclosure-note strong {
  color: var(--blue-700);
  text-transform: uppercase;
  letter-spacing: .08em;
  font-size: .8rem;
}

.site-footer {
  background: var(--navy-950);
  color: #fff;
}

.footer-inner {
  width: min(calc(100% - 34px), var(--max));
  margin: 0 auto;
  min-height: 170px;
  display: grid;
  grid-template-columns: 1fr 1.3fr .8fr;
  gap: 45px;
  align-items: center;
}

.footer-wordmark { color: #fff; }

.footer-inner p { color: #aebfcd; }

.footer-inner nav {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
}

.footer-inner nav a {
  color: #d8e5ee;
  text-decoration: none;
  font-weight: 750;
  font-size: .9rem;
}

.parent-brand { text-align: right; }

.method-dialog {
  width: min(calc(100% - 28px), 650px);
  border: 0;
  border-radius: 20px;
  padding: 34px;
  color: var(--ink);
  box-shadow: 0 24px 80px rgba(0,0,0,.34);
}

.method-dialog::backdrop {
  background: rgba(1,16,28,.72);
  backdrop-filter: blur(4px);
}

.method-dialog h2 {
  margin: 0;
  color: var(--navy-950);
}

.method-dialog ul {
  padding-left: 20px;
  color: #4d6579;
}

.dialog-close {
  position: absolute;
  top: 12px;
  right: 14px;
  width: 38px;
  height: 38px;
  border: 0;
  border-radius: 50%;
  background: #eaf0f4;
  color: var(--navy-900);
  font-size: 1.4rem;
  cursor: pointer;
}

@media (max-width: 1040px) {
  .primary-nav { gap: 18px; }
  .hero-inner { grid-template-columns: 1fr; gap: 35px; }
  .hero-panel { max-width: 720px; }
  .category-tabs { grid-template-columns: repeat(2, 1fr); }
  .product-grid { grid-template-columns: repeat(2, minmax(0,1fr)); }
  .method-section { grid-template-columns: 1fr; }
  .proof-strip { grid-template-columns: repeat(2, 1fr); }
  .proof-strip > div:nth-child(3) { border-left: 0; border-top: 1px solid #e2eaf0; }
  .proof-strip > div:nth-child(4) { border-top: 1px solid #e2eaf0; }
}

@media (max-width: 820px) {
  .header-inner {
    grid-template-columns: auto auto 1fr;
    gap: 14px;
  }

  .menu-button {
    display: block;
    grid-column: 3;
    justify-self: end;
  }

  .header-cta { display: none; }

  .primary-nav {
    display: none;
    grid-column: 1 / -1;
    flex-direction: column;
    align-items: stretch;
    gap: 0;
    padding: 5px 0 16px;
  }

  .primary-nav.open { display: flex; }

  .primary-nav a {
    padding: 12px 2px;
    border-top: 1px solid #e6edf2;
  }

  .primary-nav a[aria-current="page"]::after { display: none; }

  .hero-inner { padding-top: 56px; }

  .section-heading {
    display: grid;
    gap: 18px;
  }

  .filter-bar {
    grid-template-columns: 1fr 1fr;
  }

  .clear-button { min-height: 44px; }

  .disclosure-section {
    grid-template-columns: 1fr;
  }

  .disclosure-note {
    padding-left: 0;
    padding-top: 22px;
    border-left: 0;
    border-top: 1px solid #dae4eb;
  }

  .footer-inner {
    grid-template-columns: 1fr;
    gap: 22px;
    padding: 36px 0;
    text-align: center;
  }

  .parent-brand { text-align: center; }
}

@media (max-width: 620px) {
  .header-inner { min-height: 68px; }
  .wordmark { font-size: 1.32rem; }
  .brand-section { display: none; }

  .hero-inner {
    width: min(calc(100% - 26px), var(--max));
    padding: 44px 0 52px;
  }

  .hero h1 { font-size: clamp(2.35rem, 13vw, 3.8rem); }

  .hero-panel { padding: 17px; }

  .signal-graphic { height: 155px; }
  .left-phone { left: 48px; }
  .right-phone { right: 48px; }
  .headset-left { left: 13px; }
  .headset-right { right: 13px; }

  .proof-strip {
    width: min(calc(100% - 26px), var(--max));
    grid-template-columns: 1fr;
    margin-top: -15px;
  }

  .proof-strip > div + div {
    border-left: 0;
    border-top: 1px solid #e2eaf0;
  }

  .catalog-section,
  .method-section,
  .disclosure-section {
    width: min(calc(100% - 26px), var(--max));
  }

  .catalog-section { padding: 60px 0; }

  .category-tabs { grid-template-columns: 1fr; }

  .filter-bar { grid-template-columns: 1fr; }

  .results-meta {
    flex-direction: column;
    gap: 3px;
  }

  .product-grid { grid-template-columns: 1fr; }

  .method-section {
    padding: 28px 20px;
    gap: 30px;
    margin-bottom: 55px;
  }

  .disclosure-section {
    padding: 26px 21px;
    margin-bottom: 55px;
  }
}
