// Progressive enhancement: the complete catalog is already in the HTML.
(() => {
  const grid = document.querySelector('#product-grid');
  if (!grid) return;
  const cards = [...grid.querySelectorAll('.product-card')];
  const controls = document.querySelector('.catalog-controls');
  const search = document.querySelector('#product-search');
  const type = document.querySelector('#type-filter');
  const status = document.querySelector('#status-filter');
  const sort = document.querySelector('#sort-filter');
  const buttons = [...document.querySelectorAll('[data-category]')];
  const allowedCategories = buttons.map(button => button.dataset.category);
  let category = 'all';
  function optionValue(select, value) { return [...select.options].some(o => o.value === value) ? value : 'all'; }
  function restore() {
    const params = new URLSearchParams(location.search);
    category = allowedCategories.includes(params.get('category')) ? params.get('category') : 'all';
    search.value = (params.get('q') || '').slice(0,100);
    type.value = optionValue(type, params.get('type'));
    status.value = optionValue(status, params.get('status'));
    sort.value = params.get('sort') === 'reverse' ? 'reverse' : 'name';
    render(false);
  }
  function render(updateUrl = true, push = false) {
    const query = search.value.trim().toLocaleLowerCase();
    buttons.forEach(button => {
      const selected = button.dataset.category === category;
      button.classList.toggle('active', selected);
      button.setAttribute('aria-pressed', String(selected));
    });
    let visible = 0;
    const ordered = [...cards].sort((a,b) => a.dataset.name.localeCompare(b.dataset.name) * (sort.value === 'reverse' ? -1 : 1));
    ordered.forEach(card => {
      const matches = (category === 'all' || card.dataset.categories.split(' ').includes(category)) &&
        (type.value === 'all' || card.dataset.type === type.value) &&
        (status.value === 'all' || card.dataset.status === status.value) &&
        (!query || card.dataset.name.toLocaleLowerCase().includes(query));
      card.hidden = !matches;
      if (matches) visible++;
      grid.append(card);
    });
    document.querySelector('#result-count').textContent = `${visible} candidate${visible === 1 ? '' : 's'}`;
    document.querySelector('#empty-state').hidden = visible !== 0;
    if (updateUrl) {
      const url = new URL(location.href);
      for (const [key,value,empty] of [['category',category,'all'],['q',search.value.trim(),''],['type',type.value,'all'],['status',status.value,'all'],['sort',sort.value,'name']]) {
        if (value === empty) url.searchParams.delete(key); else url.searchParams.set(key,value);
      }
      if (url.href !== location.href) history[push ? 'pushState' : 'replaceState'](null,'',url);
    }
  }
  buttons.forEach(button => button.addEventListener('click', () => { category = button.dataset.category; render(true,true); }));
  search.addEventListener('input', () => render());
  [type,status,sort].forEach(select => select.addEventListener('change', () => render(true,true)));
  function reset(event) {
    const wasEmpty = event?.currentTarget?.hasAttribute('data-reset');
    category='all'; search.value=''; type.value='all'; status.value='all'; sort.value='name'; render(true,true);
    if (wasEmpty) search.focus();
  }
  document.querySelector('#clear-filters').addEventListener('click', reset);
  document.querySelector('[data-reset]').addEventListener('click', reset);
  window.addEventListener('popstate', restore);
  // Optional integration hook only: no tracker, storage, visitor ID or network request.
  grid.addEventListener('click', event => {
    const link = event.target.closest('.purchase-link');
    if (!link) return;
    window.dispatchEvent(new CustomEvent('vocari:product-click', {detail:{productId:link.dataset.productId,placement:link.dataset.placement,affiliate:link.dataset.affiliate === 'true'}}));
  });
  restore();
  controls.hidden=false;
})();
