(function () {
  var body = document.body;
  var drawer = document.getElementById('drawer');
  var scrim = document.querySelector('.scrim');
  var burger = document.querySelector('.burger');

  // Фон под открытым меню недоступен (inert), фокус уходит в меню и возвращается на кнопку при закрытии
  var background = document.querySelectorAll('.topbar, main, .site-footer, .sticky-cta, .skip');
  function setOpen(open) {
    if (body.classList.contains('menu-open') === open) return;
    body.classList.toggle('menu-open', open);
    if (scrim) scrim.hidden = !open;
    if (burger) burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    background.forEach(function (el) { el.inert = open; });
    if (open && drawer) {
      var first = drawer.querySelector('a, button');
      if (first) first.focus({ preventScroll: true });
    } else if (burger) {
      burger.focus({ preventScroll: true });
    }
  }

  if (burger) burger.addEventListener('click', function () { setOpen(!body.classList.contains('menu-open')); });
  document.querySelectorAll('[data-close-menu]').forEach(function (b) {
    b.addEventListener('click', function () { setOpen(false); });
  });

  // Betting и Casino: пункты-хабы с href="#", открывают подменю
  document.querySelectorAll('.sub-toggle').forEach(function (t) {
    t.addEventListener('click', function () {
      var li = t.parentElement;
      var open = !li.classList.contains('open');
      li.parentElement.querySelectorAll('.has-sub.open').forEach(function (o) {
        if (o !== li) { o.classList.remove('open'); o.firstElementChild.setAttribute('aria-expanded', 'false'); }
      });
      li.classList.toggle('open', open);
      t.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });
  document.addEventListener('click', function (e) {
    if (!e.target.closest('.main-nav .has-sub')) {
      document.querySelectorAll('.main-nav .has-sub.open').forEach(function (o) {
        o.classList.remove('open');
        o.firstElementChild.setAttribute('aria-expanded', 'false');
      });
    }
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      if (body.classList.contains('menu-open')) setOpen(false);
      document.querySelectorAll('.has-sub.open').forEach(function (o) { o.classList.remove('open'); });
    }
  });
  if (drawer) drawer.addEventListener('click', function (e) {
    var a = e.target.closest('a');
    if (a) setOpen(false);
  });

  // Подсветка активного таба при прокрутке
  var tabs = document.querySelectorAll('.tabs a');
  if (tabs.length && 'IntersectionObserver' in window) {
    var map = {};
    tabs.forEach(function (a) { map[a.getAttribute('href').slice(1)] = a; });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        tabs.forEach(function (a) { a.classList.remove('active'); });
        var a = map[en.target.id];
        if (a) {
          a.classList.add('active');
          var bar = a.closest('ul');
          bar.scrollTo({ left: a.offsetLeft - bar.clientWidth / 2 + a.offsetWidth / 2, behavior: 'smooth' });
        }
      });
    }, { rootMargin: '-120px 0px -70% 0px' });
    Object.keys(map).forEach(function (id) {
      var el = document.getElementById(id);
      if (el) io.observe(el);
    });
  }
})();
