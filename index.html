const PRODUCTS = [
  {
    priority: 1,
    brand: "EarFun",
    name: "Air Pro 4+",
    categories: ["sports", "personal"],
    categoryLabel: "Sports / Personal",
    platforms: ["android", "ios"],
    type: "earbuds",
    typeLabel: "True wireless earbuds",
    summary: "High-priority consumer candidate for testing low-latency communication behavior, microphone quality, and broad device compatibility."
  },
  {
    priority: 2,
    brand: "Samsung",
    name: "Galaxy Buds4 Pro",
    categories: ["personal"],
    categoryLabel: "Personal / Professional / Executive",
    platforms: ["android"],
    type: "earbuds",
    typeLabel: "True wireless earbuds",
    summary: "Priority Android benchmark for Samsung-device routing, call-path stability, and future LE Audio evaluation."
  },
  {
    priority: 3,
    brand: "JLab",
    name: "Work Buds",
    categories: ["personal", "enterprise"],
    categoryLabel: "Professional / Enterprise",
    platforms: ["android", "ios"],
    type: "boom",
    typeLabel: "Earbuds with detachable boom microphone",
    summary: "Accessible communication-focused candidate whose detachable boom microphone may improve practical voice pickup."
  },
  {
    priority: 4,
    brand: "Shokz",
    name: "OpenComm2 UC",
    categories: ["sports", "enterprise"],
    categoryLabel: "Activity / Enterprise",
    platforms: ["android", "ios"],
    type: "open-ear",
    typeLabel: "Open-ear communication headset",
    summary: "Communication benchmark candidate emphasizing voice pickup, environmental awareness, comfort, and long-session use."
  },
  {
    priority: 5,
    brand: "ISOtunes",
    name: "PRO 3.0",
    categories: ["industrial"],
    categoryLabel: "Industrial / Manufacturing / Construction",
    platforms: ["android", "ios"],
    type: "hearing-protection",
    typeLabel: "Bluetooth hearing protection",
    summary: "Industrial candidate for rugged use, hearing-protection requirements, background-noise performance, and extended shifts."
  },
  {
    priority: 6,
    brand: "3M PELTOR",
    name: "WS ProTac XPI",
    categories: ["enterprise", "industrial"],
    categoryLabel: "Enterprise / Industrial",
    platforms: ["android", "ios"],
    type: "hearing-protection",
    typeLabel: "Protective communication headset",
    summary: "High-noise benchmark candidate for industrial communication, protective equipment integration, and boom-microphone performance."
  }
];

let activeCategory = "all";

const grid = document.querySelector("#product-grid");
const count = document.querySelector("#result-count");
const empty = document.querySelector("#empty-state");
const platformFilter = document.querySelector("#platform-filter");
const typeFilter = document.querySelector("#type-filter");
const sortFilter = document.querySelector("#sort-filter");

function categoryName(category) {
  const labels = {
    sports: "Sports / Activity / Exercise",
    personal: "Personal / Professional / Executive",
    enterprise: "Enterprise",
    industrial: "Industrial / Manufacturing / Construction"
  };
  return labels[category] || category;
}

function productCard(product) {
  const platformBadges = product.platforms.map(platform => {
    const text = platform === "android" ? "Android candidate" : "iPhone / iOS candidate";
    return `<span class="badge ${platform}">${text}</span>`;
  }).join("");

  return `
    <article class="product-card">
      <div class="product-visual">
        <span class="status-ribbon">Under Evaluation</span>
        <span class="priority-badge" title="Evaluation priority">${product.priority}</span>
        <div class="device-illustration ${product.type}" aria-hidden="true">
          ${product.type === "boom" ? "<span></span>" : ""}
        </div>
      </div>
      <div class="product-body">
        <p class="product-brand">${product.brand}</p>
        <h3 class="product-title">${product.name}</h3>
        <p class="product-category">${product.categoryLabel} · ${product.typeLabel}</p>

        <div class="badge-row">${platformBadges}</div>

        <div class="evaluation-block">
          <div class="evaluation-title">
            <span>Vocari evaluation</span>
            <span>Pending</span>
          </div>
          <div class="pending-bars" aria-label="Testing pending">
            <div class="pending-row"><span>Latency</span><span class="pending-line"></span></div>
            <div class="pending-row"><span>Voice clarity</span><span class="pending-line"></span></div>
            <div class="pending-row"><span>Stability</span><span class="pending-line"></span></div>
            <div class="pending-row"><span>Use-case fit</span><span class="pending-line"></span></div>
          </div>
        </div>

        <p class="product-summary">${product.summary}</p>

        <div class="product-footer">
          <button class="pending-button" type="button" disabled>Deal link activates after testing</button>
          <p class="product-note">No affiliate recommendation has been issued.</p>
        </div>
      </div>
    </article>
  `;
}

function renderProducts() {
  const platform = platformFilter.value;
  const type = typeFilter.value;
  const sort = sortFilter.value;

  let products = PRODUCTS.filter(product => {
    const categoryMatch = activeCategory === "all" || product.categories.includes(activeCategory);
    const platformMatch = platform === "all" || product.platforms.includes(platform);
    const typeMatch = type === "all" || product.type === type;
    return categoryMatch && platformMatch && typeMatch;
  });

  products.sort((a, b) => {
    if (sort === "name") return `${a.brand} ${a.name}`.localeCompare(`${b.brand} ${b.name}`);
    if (sort === "category") return a.categoryLabel.localeCompare(b.categoryLabel);
    return a.priority - b.priority;
  });

  grid.innerHTML = products.map(productCard).join("");
  count.textContent = `${products.length} candidate${products.length === 1 ? "" : "s"}`;
  empty.hidden = products.length !== 0;
}

document.querySelectorAll(".category-tab").forEach(tab => {
  tab.addEventListener("click", () => {
    activeCategory = tab.dataset.category;
    document.querySelectorAll(".category-tab").forEach(item => {
      const selected = item === tab;
      item.classList.toggle("active", selected);
      item.setAttribute("aria-selected", String(selected));
    });
    renderProducts();
  });
});

[platformFilter, typeFilter, sortFilter].forEach(control => {
  control.addEventListener("change", renderProducts);
});

document.querySelector("#clear-filters").addEventListener("click", () => {
  activeCategory = "all";
  platformFilter.value = "all";
  typeFilter.value = "all";
  sortFilter.value = "priority";

  document.querySelectorAll(".category-tab").forEach(tab => {
    const selected = tab.dataset.category === "all";
    tab.classList.toggle("active", selected);
    tab.setAttribute("aria-selected", String(selected));
  });

  renderProducts();
});

const menuButton = document.querySelector(".menu-button");
const primaryNav = document.querySelector("#primary-nav");

menuButton.addEventListener("click", () => {
  const open = primaryNav.classList.toggle("open");
  menuButton.setAttribute("aria-expanded", String(open));
});

const dialog = document.querySelector("#method-dialog");

document.querySelectorAll("[data-open-method]").forEach(button => {
  button.addEventListener("click", () => dialog.showModal());
});

document.querySelectorAll("[data-close-method]").forEach(button => {
  button.addEventListener("click", () => dialog.close());
});

dialog.addEventListener("click", event => {
  const bounds = dialog.getBoundingClientRect();
  const outside =
    event.clientX < bounds.left ||
    event.clientX > bounds.right ||
    event.clientY < bounds.top ||
    event.clientY > bounds.bottom;

  if (outside) dialog.close();
});

renderProducts();
