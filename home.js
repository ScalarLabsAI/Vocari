document.documentElement.classList.add('js');
const menu = document.querySelector('.menu-button');
const nav = document.querySelector('#primary-nav');
function closeMenu(returnFocus = false) {
  nav.classList.remove('open');
  menu.setAttribute('aria-expanded', 'false');
  menu.textContent = 'Menu';
  if (returnFocus) menu.focus();
}
menu?.addEventListener('click', () => {
  const open = nav.classList.toggle('open');
  menu.setAttribute('aria-expanded', String(open));
  menu.textContent = open ? 'Close' : 'Menu';
});
nav?.querySelectorAll('a').forEach(link => link.addEventListener('click', () => closeMenu()));
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && nav?.classList.contains('open')) closeMenu(true);
});
matchMedia('(min-width:761px)').addEventListener('change', event => { if (event.matches) closeMenu(); });
