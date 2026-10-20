#!/usr/bin/env python3
"""Собирает статический сайт parimatch-betting-india.com из src/ в public/.

Страница = src/pages/<slug>.html (вложенные: src/pages/esports/cs2.html → /esports/cs2/):
сверху JSON с метаданными в <!--{ ... }-->, ниже HTML контента. Запуск: python3 build.py
"""
import hashlib
import html
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "src"
OUT = ROOT / "public"

SITE = "https://parimatch-betting-india.com"
SITE_NAME = "Parimatch Betting India"
UPDATED_ISO = "2026-10-20"
UPDATED_TXT = "20 October 2026"
# Партнёрские ссылки: регистрация и приложение.
AFF = {
    "reg": "https://pbic.parimatch-betting-india.com/vZdjWYy",
    "app": "https://pbic.parimatch-betting-india.com/vZdjWYy?type=app",
}

ICONS = {
    "home": '<path d="M3 11l9-7 9 7v9a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/>',
    "user": '<circle cx="10" cy="8" r="4"/><path d="M2 21c0-4 4-6 8-6s8 2 8 6"/><path d="M19 8v6M16 11h6"/>',
    "key": '<circle cx="8" cy="15" r="4"/><path d="M11 12l9-9M17 6l3 3M15 8l2 2"/>',
    "phone": '<rect x="6" y="2" width="12" height="20" rx="2"/><path d="M11 18h2"/>',
    "gift": '<rect x="3" y="8" width="18" height="5" rx="1"/><path d="M5 13v8h14v-8M12 8v13M12 8c-2-4-6-4-6-1s6 1 6 1zm0 0c2-4 6-4 6-1s-6 1-6 1z"/>',
    "card": '<rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20M6 15h4"/>',
    "down": '<path d="M12 4v12M6 11l6 6 6-6"/><path d="M4 20h16"/>',
    "up": '<path d="M12 20V8M6 13l6-6 6 6"/><path d="M4 4h16"/>',
    "dice": '<rect x="3" y="3" width="18" height="18" rx="4"/><circle cx="8.5" cy="8.5" r="1.3" fill="currentColor"/><circle cx="15.5" cy="15.5" r="1.3" fill="currentColor"/><circle cx="12" cy="12" r="1.3" fill="currentColor"/>',
    "ball": '<circle cx="12" cy="12" r="9"/><path d="M12 7l4 3-1.5 5h-5L8 10z"/><path d="M12 3v4M21 10l-5 0M3 10h5M7 20l2.5-5M17 20l-2.5-5"/>',
    "bat": '<path d="M14 4l6 6-9.5 9.5a2 2 0 0 1-2.8 0l-3.2-3.2a2 2 0 0 1 0-2.8z"/><path d="M4.5 19.5L3 21"/><circle cx="19" cy="19" r="2"/>',
    "shield": '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
    "info": '<circle cx="12" cy="12" r="9"/><path d="M12 11v6M12 7.5v.5"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
    "close": '<path d="M6 6l12 12M18 6L6 18"/>',
    "chev": '<path d="M6 9l6 6 6-6"/>',
    "trophy": '<path d="M8 21h8M12 17v4M7 4h10v5a5 5 0 0 1-10 0z"/><path d="M17 5h3v2a3 3 0 0 1-3 3M7 5H4v2a3 3 0 0 0 3 3"/>',
    "crown": '<path d="M3 8l4.5 4L12 5l4.5 7L21 8l-2 11H5z"/>',
    "tv": '<rect x="3" y="6" width="18" height="13" rx="2"/><path d="M8 3l4 3 4-3"/><circle cx="12" cy="12.5" r="2.5" fill="currentColor" stroke="none"/>',
    "lock": '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>',
    "chat": '<path d="M4 5h16v11H9l-5 4z"/><path d="M8 10h8M8 13h5"/>',
    "star": '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z"/>',
    "alert": '<path d="M12 3l9.5 17h-19z"/><path d="M12 10v4M12 17v.5"/>',
    "heart": '<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/>',
    "plane": '<path d="M2 16l20-8-6 12-3-5z"/><path d="M13 15l9-7"/>',
    "game": '<rect x="2" y="7" width="20" height="11" rx="4"/><path d="M7 11v3M5.5 12.5h3"/><circle cx="15.5" cy="11.5" r="1" fill="currentColor"/><circle cx="18" cy="14" r="1" fill="currentColor"/>',
    "rocket": '<path d="M5 15c-1.5 1.5-2 5-2 5s3.5-.5 5-2"/><path d="M9 15l-3-3c1-4 5-9 13-9 0 8-5 12-9 13z"/><circle cx="15" cy="9" r="1.5"/>',
    "handshake": '<path d="M2 12l4-4 4 2 4-3 4 3 4 2"/><path d="M6 8v6l4 4 2-1 2 1 4-4"/>',
}


def icon(name):
    return (f'<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


# Меню. Betting и Casino — хабы без страниц (href="#"), раскрывают подменю.
NAV = [
    ("/app/", "App", "phone"),
    ("/registration/", "Registration", "user"),
    ("/login/", "Login", "key"),
    ("/bonus/", "Bonus", "gift"),
    ("#betting", "Betting", "ball", [
        ("/cricket/", "Cricket", "bat"),
        ("/football/", "Football", "ball"),
        ("/kabaddi/", "Kabaddi", "ball"),
        ("/tennis/", "Tennis", "ball"),
        ("/esports/", "Esports", "game"),
        ("/esports/cs2/", "CS2", "game"),
        ("/esports/dota2/", "Dota 2", "game"),
    ]),
    ("#casino", "Casino", "dice", [
        ("/slots/", "Slots", "dice"),
        ("/live-casino/", "Live Casino", "tv"),
        ("/aviator/", "Aviator", "plane"),
        ("/crash-games/", "Crash Games", "rocket"),
    ]),
    ("/support/", "Support", "chat"),
]
NAV_MORE = [
    ("/mobile-version/", "Mobile Version", "phone"),
    ("/verification/", "Verification", "shield"),
    ("/deposit/", "Deposit", "down"),
    ("/withdrawal/", "Withdrawal", "up"),
    ("/affiliate-program/", "Affiliate Program", "handshake"),
]

FOOTER_GUIDES = [
    ("/app/", "Parimatch App"), ("/mobile-version/", "Mobile Version"), ("/registration/", "Registration"),
    ("/login/", "Login"), ("/verification/", "Verification"), ("/bonus/", "Bonuses"),
    ("/deposit/", "Deposit"), ("/withdrawal/", "Withdrawal"),
]
FOOTER_PLAY = [
    ("/cricket/", "Cricket Betting"), ("/football/", "Football Betting"), ("/kabaddi/", "Kabaddi Betting"),
    ("/tennis/", "Tennis Betting"), ("/esports/", "Esports Betting"), ("/slots/", "Slots"),
    ("/live-casino/", "Live Casino"), ("/aviator/", "Aviator"), ("/crash-games/", "Crash Games"),
]
FOOTER_INFO = [
    ("/about/", "About Us"), ("/contacts/", "Contacts"), ("/support/", "Support"), ("/affiliate-program/", "Affiliate Program"),
]
FOOTER_LEGAL = [
    ("/privacy-policy/", "Privacy Policy"), ("/terms-and-conditions/", "Terms and Conditions"),
    ("/cookie-policy/", "Cookie Policy"), ("/responsible-gambling/", "Responsible Gambling"),
]
PAYMENT_LOGOS = ["UPI", "Paytm", "PhonePe", "Google Pay", "IMPS", "Net Banking", "Visa", "Mastercard", "USDT", "BTC"]

GAME_COLORS = [
    ("#e8f400", "#3a3d00"), ("#ff5a1f", "#3d1205"), ("#7b2ff7", "#22093f"), ("#00b84a", "#05301a"),
    ("#1aa3ff", "#062a40"), ("#ff2d6f", "#3f0619"), ("#ffb800", "#3d2b00"), ("#00d1b2", "#00332b"),
]


def asset_ver(name):
    """Короткий хэш файла для ?v= — после правки CSS/JS браузеры и Cloudflare берут новую версию."""
    return hashlib.md5((SRC / "assets" / name).read_bytes()).hexdigest()[:8]


# Title Case: каждое слово с большой буквы, кроме предлогов. Первое слово и слово после «:», «?», «!», «.»,
# «—», «|» — всегда с большой. Частицы фразовых глаголов (Log In, Sign In, Cash Out) — с большой.
PREPOSITIONS = {
    "about", "above", "across", "after", "against", "along", "among", "around", "at", "before", "behind",
    "below", "beneath", "beside", "besides", "between", "beyond", "by", "despite", "during", "except",
    "for", "from", "in", "inside", "into", "like", "near", "of", "off", "on", "onto", "outside", "over",
    "past", "per", "since", "than", "through", "throughout", "till", "to", "toward", "towards", "under",
    "underneath", "until", "upon", "via", "vs", "with", "within", "without",
}
PHRASAL = {"log", "logs", "logging", "logged", "sign", "signs", "signing", "signed", "opt", "check",
           "cash", "top", "set", "set-up", "plug", "turn", "switch", "back", "pay"}
_LEAD = "\"'“‘([«"
_TRAIL = "?!.,;:”’\"')]»…"


def _tc_word(word, force, prev):
    i = 0
    while i < len(word) and word[i] in _LEAD:
        i += 1
    j = len(word)
    while j > i and word[j - 1] in _TRAIL:
        j -= 1
    core = word[i:j]
    if not core or not core[0].isalpha():
        return word
    if any(c.isupper() for c in core[1:]):
        return word  # iOS, eSports, UPI, PhonePe — как есть
    low = core.lower()
    if not force and low in PREPOSITIONS and prev not in PHRASAL:
        core = low
    else:
        core = "-".join(p[:1].upper() + p[1:] if p else p for p in core.split("-"))
    return word[:i] + core + word[j:]


def title_case(text, start=True, prev=""):
    out = []
    for part in re.split(r"(\s+)", text):
        if not part or part.isspace():
            out.append(part)
            continue
        out.append(_tc_word(part, start, prev))
        stripped = part.rstrip("”’\"')»")
        start = (bool(stripped) and stripped[-1] in ":?!.") or part in ("—", "–", "|", "-")
        prev = re.sub(r"[^a-z\-]", "", part.lower())
    return "".join(out), start, prev


def tc(text):
    return title_case(text)[0]


def tc_html(fragment):
    """Title case только для текста между тегами (иконки и разметка не трогаются)."""
    out, start, prev = [], True, ""
    for part in re.split(r"(<[^>]+>)", fragment):
        if part.startswith("<"):
            out.append(part)
        else:
            t, start, prev = title_case(part, start, prev)
            out.append(t)
    return "".join(out)


def headings_tc(doc):
    doc = re.sub(r"(<(h[1-3])\b[^>]*>)(.*?)(</\2>)", lambda m: m.group(1) + tc_html(m.group(3)) + m.group(4), doc, flags=re.S)
    doc = re.sub(r'(<div class="big">)(.*?)(</div>)', lambda m: m.group(1) + tc_html(m.group(2)) + m.group(3), doc)
    doc = re.sub(r'(<div class="cta-box"><p>)(.*?)(<small>)', lambda m: m.group(1) + tc_html(m.group(2)) + m.group(3), doc)
    doc = re.sub(r'(<nav class="tabs".*?</nav>)', lambda m: re.sub(r'(<a href="#[^"]+">)(.*?)(</a>)', lambda a: a.group(1) + tc_html(a.group(2)) + a.group(3), m.group(1)), doc, flags=re.S)
    return doc


def esc(s):
    return html.escape(s, quote=True)


def cta(text, style="", link="reg"):
    cls = "btn" + (" btn-" + style if style else "")
    return (f'<a class="{cls}" href="{esc(AFF[link])}" target="_blank" '
            f'rel="nofollow sponsored noopener">{esc(text)}</a>')


def slugify(text):
    import unicodedata
    t = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")


def strip_tags(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s)).strip()


def game_img(name, prov):
    """<img> превью игры, если файл есть в src/assets/img/games/<slug>.webp."""
    slug = slugify(name)
    if not (SRC / "assets" / "img" / "games" / f"{slug}.webp").exists():
        return ""
    return (f'<img src="/assets/img/games/{slug}.webp" width="180" height="236" loading="lazy" decoding="async" '
            f'alt="{esc(name)} by {esc(prov)} at Parimatch">')


# Иконки у заголовков H2 по смыслу (порядок важен: сначала частные случаи)
ICON_RULES = [
    ("chat", ("faq", "frequently asked", "questions")),
    ("alert", ("problem", "issue", "error", "not working", "declined", "pending", "troubleshoot", "mistake", "avoid")),
    ("crown", ("vip", "loyalty")),
    ("gift", ("bonus", "promo", "free bet", "freebet", "free spin", "cashback", "reward", "offer")),
    ("plane", ("aviator",)),
    ("rocket", ("crash",)),
    ("phone", ("app", "apk", "android", "ios", "iphone", "mobile", "pwa", "install", "download")),
    ("key", ("log in", "login", "password", "sign in")),
    ("down", ("deposit",)),
    ("up", ("withdraw", "cash out", "payout")),
    ("card", ("payment", "upi", "limit", "method", "fee")),
    ("shield", ("verif", "kyc", "document", "security", "safe", "licen")),
    ("user", ("regist", "sign up", "account", "requirement")),
    ("chat", ("support", "chat", "contact", "help")),
    ("handshake", ("affiliate", "partner", "commission")),
    ("heart", ("responsible", "limits and tools", "self-exclusion", "tips")),
    ("tv", ("live casino", "live dealer", "game show", "streaming", "live betting", "in-play")),
    ("game", ("esports", "cs2", "dota", "counter-strike", "valorant")),
    ("bat", ("cricket", "ipl", "t20", "odi")),
    ("trophy", ("tournament", "league", "championship", "grand slam", "pro kabaddi", "major")),
    ("dice", ("slot", "casino", "game", "provider", "jackpot", "rtp", "andar", "teen patti")),
    ("ball", ("bet", "market", "odds", "football", "kabaddi", "tennis", "sport", "match")),
    ("star", ("overview", "key facts", "features", "how", "what", "why", "start")),
]


def icon_for(text):
    t = strip_tags(text).lower()
    for name, keys in ICON_RULES:
        if any(k in t for k in keys):
            return name
    return None


def add_icons(body, headings=True):
    def _h2(m):
        name = icon_for(m.group(2))
        if not name:
            return m.group(0)
        return f'{m.group(1)}<span class="h-ico" aria-hidden="true">{icon(name)}</span>{m.group(2)}</h2>'
    if headings:
        body = re.sub(r'(<h2 id="[^"]+"(?: data-tab="[^"]+")?>)(.*?)</h2>', _h2, body)

    def _card(m):
        inner = m.group(2)
        h3 = re.search(r"<h3>(.*?)</h3>", inner)
        kicker = re.search(r'<span class="kicker">(.*?)</span>', inner)
        name = icon_for((h3.group(1) if h3 else "") + " " + (kicker.group(1) if kicker else "")) or "star"
        return f'{m.group(1)}<span class="card-ico" aria-hidden="true">{icon(name)}</span>{inner}{m.group(3)}'
    body = re.sub(r'(<(?:div|a) class="card"[^>]*>)(.*?)(</(?:div|a)>)', _card, body, flags=re.S)
    return body


def expand(body):
    """Шорткоды:
    {{cta:Текст|style|link}} — кнопка (style: ''/ghost/dark, link: reg/app);
    {{ctabox:Заголовок|Подпись|Кнопка|link}} — блок с кнопкой;
    {{games:Название/Провайдер;...}} — плитки игр;
    {{icon:name}}, {{updated}}."""
    def _cta(m):
        parts = m.group(1).split("|")
        return cta(parts[0], parts[1] if len(parts) > 1 else "", parts[2] if len(parts) > 2 else "reg")

    def _box(m):
        head, sub, btn, link = (m.group(1).split("|") + ["", "", "", ""])[:4]
        return (f'<div class="cta-box"><p>{esc(head)}<small>{esc(sub)}</small></p>'
                f'{cta(btn, "", link or "reg")}</div>')

    def _games(m):
        items = [g.strip() for g in m.group(1).split(";") if g.strip()]
        out = []
        for i, g in enumerate(items):
            name, prov = (g.split("/") + [""])[:2]
            c1, c2 = GAME_COLORS[i % len(GAME_COLORS)]
            img = game_img(name, prov)
            out.append(f'<div class="game"><div class="art{" has-img" if img else ""}" style="--g1:{c1};--g2:{c2}">'
                       f'{img}<b>{esc(name)}</b></div><span>{esc(prov)}</span></div>')
        return '<div class="games">' + "".join(out) + "</div>"

    body = re.sub(r"\{\{cta:([^}]+)\}\}", _cta, body)
    body = re.sub(r"\{\{ctabox:([^}]+)\}\}", _box, body)
    body = re.sub(r"\{\{games:([^}]+)\}\}", _games, body)
    body = re.sub(r"\{\{icon:([a-z]+)\}\}", lambda m: icon(m.group(1)), body)
    body = body.replace("{{updated}}", UPDATED_TXT)
    return body


def short_label(text):
    t = strip_tags(text)
    if t.lower().startswith(("faq", "frequently asked")):
        return "FAQ"
    for cut in (" at Parimatch India", " on Parimatch India", " at Parimatch", " on Parimatch", " in Parimatch"):
        t = t.replace(cut, "")
    t = re.sub(r":.*$", "", t).strip()
    return t[:1].upper() + t[1:]


def toc_from(body):
    items = re.findall(r'<h2 id="([^"]+)"(?: data-tab="([^"]+)")?>(.*?)</h2>', body, re.S)
    if len(items) < 3:
        return ""
    lis = "".join(f'<li><a href="#{i}">{esc(tab or short_label(t))}</a></li>' for i, tab, t in items)
    return f'<nav class="tabs" aria-label="On this page"><ul>{lis}</ul></nav>'


def faq_schema(body):
    pairs = re.findall(r"<summary>(.*?)</summary>\s*<div>(.*?)</div>\s*</details>", body, re.S)
    if not pairs:
        return None
    return {
        "@type": "FAQPage",
        "mainEntity": [{
            "@type": "Question",
            "name": strip_tags(q),
            "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)},
        } for q, a in pairs],
    }


def url_of(slug):
    return "/" if slug == "index" else f"/{slug}/"


LOGO = (f'<a class="logo" href="/" aria-label="{SITE_NAME} home">'
        f'<span class="logo-mark" aria-hidden="true">PM</span>'
        f'<span class="logo-txt">Parimatch<small>Betting India</small></span></a>')


def nav_html(current, mobile=False):
    items = []
    for entry in NAV:
        href, label, ico = entry[:3]
        if len(entry) == 4:
            sub = entry[3]
            active = any(h == current for h, _, _ in sub)
            cur_attr = ' aria-current="page"'
            subs = "".join(
                f'<li><a href="{h}"{cur_attr if h == current else ""}>{icon(i)}<span>{t}</span></a></li>'
                for h, t, i in sub)
            items.append(
                f'<li class="has-sub{" active" if active else ""}">'
                f'<a href="#" class="sub-toggle" aria-haspopup="true" aria-expanded="false">{icon(ico)}<span>{label}</span>{icon("chev")}</a>'
                f'<ul class="sub">{subs}</ul></li>')
        else:
            cur = ' aria-current="page"' if href == current else ""
            items.append(f'<li><a href="{href}"{cur}>{icon(ico)}<span>{label}</span></a></li>')
    if mobile:
        for href, label, ico in NAV_MORE:
            cur = ' aria-current="page"' if href == current else ""
            items.append(f'<li><a href="{href}"{cur}>{icon(ico)}<span>{label}</span></a></li>')
    return "<ul>" + "".join(items) + "</ul>"


def header(current):
    return f'''<header class="topbar">
  <div class="topbar-in">
    <button class="burger" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="drawer">{icon("menu")}</button>
    {LOGO}
    <nav class="main-nav" aria-label="Main menu">{nav_html(current)}</nav>
    <div class="top-actions">
      {cta("Download App", "ghost", "app").replace('class="btn btn-ghost"', 'class="btn btn-ghost btn-sm hide-sm"')}
      {cta("Sign Up").replace('class="btn"', 'class="btn btn-sm"')}
    </div>
  </div>
</header>
<aside class="drawer" id="drawer" aria-label="Menu">
  <div class="drawer-head">{LOGO}<button class="drawer-close" type="button" aria-label="Close menu" data-close-menu>{icon("close")}</button></div>
  <nav class="drawer-nav" aria-label="Mobile menu">{nav_html(current, mobile=True)}</nav>
  <div class="drawer-cta">{cta("Sign Up")}{cta("Download App", "ghost", "app")}</div>
  <p class="drawer-note"><span class="badge-18">18+</span> Play responsibly</p>
</aside>
<div class="scrim" data-close-menu hidden></div>'''


def links(items):
    return "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in items)


def footer():
    pays = "".join(f"<li>{p}</li>" for p in PAYMENT_LOGOS)
    return f'''<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-about">
        {LOGO}
        <p>An independent English guide to Parimatch for players in India: app, registration, bonuses, payments in rupees, cricket betting and casino games.</p>
        <div class="badges"><span class="badge badge-y">18+</span><span class="badge">Play Responsibly</span></div>
      </div>
      <div><h2>Guides</h2><ul>{links(FOOTER_GUIDES)}</ul></div>
      <div><h2>Betting &amp; Casino</h2><ul>{links(FOOTER_PLAY)}</ul></div>
      <div><h2>Information</h2><ul>{links(FOOTER_INFO)}</ul></div>
      <div><h2>Rules &amp; Policies</h2><ul>{links(FOOTER_LEGAL)}</ul></div>
    </div>
    <ul class="pay-strip" aria-label="Payment methods">{pays}</ul>
    <div class="disclaimer">
      <p>{SITE_NAME} is an independent information site about Parimatch. The site does not accept bets, run games or process payments. Some links are affiliate links: if you register through them, the site may earn a commission at no extra cost to you.</p>
      <p>For users aged 18 and over only. Online betting rules differ between Indian states: check the rules where you live before you play. Gambling can be addictive. Set limits and stop if the game stops being fun.</p>
      <p>© 2026 {SITE_NAME}</p>
    </div>
  </div>
</footer>'''


def sticky_cta(slug):
    if slug == "404":
        return ""
    first = cta("Download App", "", "app") if slug == "app" else cta("Sign Up")
    second = cta("Sign Up", "ghost") if slug == "app" else cta("Download App", "ghost", "app")
    return f'<div class="sticky-cta" role="region" aria-label="Quick actions">{first}{second}</div>'


def crumbs_for(slug, label):
    trail = [("Home", "/")]
    parts = slug.split("/")
    if len(parts) > 1:
        parent = "/".join(parts[:-1])
        ppath = SRC / "pages" / f"{parent}.html"
        if ppath.exists():
            pmeta, _ = parse(ppath)
            trail.append((pmeta.get("crumb", pmeta["h1"]), url_of(parent)))
    trail.append((label, url_of(slug)))
    return trail


def page_html(slug, meta, body):
    return headings_tc(_page_html(slug, meta, body))


def _page_html(slug, meta, body):
    url = url_of(slug)
    canonical = SITE + url
    kind = meta.get("type", "commercial")
    body = expand(body)
    body = add_icons(body, headings=kind != "legal")

    crumbs = ""
    graph = []
    if slug not in ("index", "404"):
        label = meta.get("crumb", meta["h1"])
        trail = crumbs_for(slug, label)
        parts = []
        for i, (name, href) in enumerate(trail):
            if i == len(trail) - 1:
                parts.append(f"<span>{esc(name)}</span>")
            else:
                parts.append(f'<a href="{href}">{esc(name)}</a>')
        crumbs = '<nav class="crumbs" aria-label="Breadcrumbs">' + '<span aria-hidden="true">›</span>'.join(parts) + "</nav>"
        graph.append({
            "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + h}
                                for i, (n, h) in enumerate(trail)],
        })
    elif slug == "index":
        graph.append({"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/",
                      "name": SITE_NAME, "inLanguage": "en-IN"})
        graph.append({"@type": "Organization", "@id": SITE + "/#org", "name": SITE_NAME,
                      "url": SITE + "/", "email": "contact@parimatch-betting-india.com"})

    graph.append({
        "@type": "WebPage" if kind == "legal" else "Article",
        "headline": meta["h1"],
        "description": meta["description"],
        "url": canonical,
        "inLanguage": "en-IN",
        "dateModified": UPDATED_ISO,
        "datePublished": UPDATED_ISO,
        "author": {"@type": "Organization", "name": SITE_NAME, "url": SITE + "/"},
        "publisher": {"@type": "Organization", "name": SITE_NAME, "url": SITE + "/"},
    })
    fs = faq_schema(body)
    if fs:
        graph.append(fs)
    for extra in meta.get("schema", []):
        graph.append(extra)
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)

    hero_side = ""
    if meta.get("offer"):
        o = meta["offer"]
        points = "".join(f"<li>{esc(p)}</li>" for p in o.get("points", []))
        hero_side = (f'<aside class="offer-card"><span class="tag">{esc(o["tag"])}</span>'
                     f'<div class="offer-art" aria-hidden="true"><span></span><span></span><span></span></div>'
                     f'<div class="big">{esc(o["title"])}</div>'
                     f'{"<ul>" + points + "</ul>" if points else ""}'
                     f'{cta(o["button"], "", o.get("link", "reg"))}'
                     f'<p class="fine">18+ · T&amp;Cs apply · Play responsibly</p></aside>')

    # Первый экран каждой страницы (и служебных тоже): регистрация + скачать приложение
    actions = ""
    if slug != "404":
        reg_btn = cta("Sign Up at Parimatch", "", "reg")
        app_btn = cta("Download the App", "ghost", "app")
        btns = [cta("Download the App", "", "app"), cta("Sign Up at Parimatch", "ghost", "reg")] if slug == "app" else [reg_btn, app_btn]
        actions = '<div class="hero-actions">' + "".join(btns) + "</div>"

    lead = f'<p class="lead">{esc(meta["lead"])}</p>' if meta.get("lead") else ""
    hero = f'''<section class="hero{' hero-legal' if kind == 'legal' else ''}">
  <div class="wrap">
    {crumbs}
    <div class="hero-grid"{' style="grid-template-columns:1fr"' if not hero_side else ''}>
      <div>
        <h1>{esc(meta["h1"])}</h1>
        {lead}
        {actions}
      </div>
      {hero_side}
    </div>
  </div>
</section>'''

    toc = toc_from(body) if kind != "legal" else ""
    updated_label = "Last updated" if kind == "legal" else "Updated"
    meta_line = (f'<div class="meta-line updated"><span>{updated_label}: <time datetime="{UPDATED_ISO}">{UPDATED_TXT}</time></span></div>'
                 if slug != "404" else "")

    robots = meta.get("robots", "index, follow, max-image-preview:large")
    og_type = "website" if slug == "index" else "article"

    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(meta["title"])}</title>
<meta name="description" content="{esc(meta["description"])}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="en-IN" href="{canonical}">
<link rel="alternate" hreflang="x-default" href="{canonical}">
<meta property="og:locale" content="en_IN">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:title" content="{esc(meta["title"])}">
<meta property="og:description" content="{esc(meta["description"])}">
<meta property="og:url" content="{canonical}">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#0b0b0b">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/assets/fonts/manrope-latin-800-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/style.css?v={asset_ver("style.css")}">
<script type="application/ld+json">{ld}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{header(url)}
<main id="main">
{hero}
{toc}
<div class="page">
  <article class="content{' legal' if kind == 'legal' else ''}">
{body}
  </article>
  {meta_line}
</div>
</main>
{footer()}
{sticky_cta(slug)}
<script src="/assets/site.js?v={asset_ver("site.js")}" defer></script>
</body>
</html>
'''


def parse(path):
    raw = path.read_text(encoding="utf-8").replace("{{updated}}", UPDATED_TXT)
    m = re.match(r"\s*<!--(\{.*?\})-->\s*(.*)", raw, re.S)
    if not m:
        sys.exit(f"{path}: нет JSON-шапки")
    return json.loads(m.group(1)), m.group(2)


# Проверки текста: официальный сайт не упоминаем, бренд — в третьем лице без местоимений.
BANNED = [
    (r"\bofficial (?:site|website|page|web ?site|platform|app)\b", "упоминание официального сайта", re.I),
    (r"parimatch\.(?:com|in)\b|pari123|pariwin", "домен оператора", re.I),
    (r"\b(?:[Ww]e|[Oo]ur|[Oo]urs|us|Us)\b", "местоимение we/our/us", 0),  # «US Open» не ловим
    (r"\b(?:editorial team|our team|our experts)\b", "упоминание редакции", re.I),
    (r"\bpros\b.*\bcons\b|\badvantages and disadvantages\b", "блок pros/cons", re.I),
]


def text_checks(slug, body):
    text = strip_tags(re.sub(r"<!--.*?-->", "", body))
    errs = []
    for pat, what, flags in BANNED:
        m = re.search(pat, text, flags)
        if m:
            errs.append(f"{slug}: {what} — «{text[max(0, m.start() - 30):m.end() + 30]}»")
    # Бренд — только по имени: «Parimatch … it/its/they» в одном предложении считаем ошибкой
    for sent in re.split(r"(?<=[.!?])\s+", text):
        if re.search(r"\bParimatch\b", sent) and re.search(r"\b(?:it|its|It|Its|they|their|They|Their)\b", sent):
            errs.append(f"{slug}: местоимение рядом с брендом — «{sent[:140]}»")
    return errs


def check_page(slug):
    """python3 build.py --check <slug>: проверка одной страницы без записи public/ (можно запускать параллельно)."""
    p = SRC / "pages" / f"{slug}.html"
    if not p.exists():
        sys.exit(f"нет файла {p}")
    meta, body = parse(p)
    errors = []
    for key in ("title", "description", "h1"):
        if not meta.get(key):
            errors.append(f"{slug}: нет {key}")
    t, d = tc(meta.get("title", "")), meta.get("description", "")
    if len(t) > 60:
        errors.append(f"{slug}: title {len(t)} > 60")
    if len(d) > 160:
        errors.append(f"{slug}: description {len(d)} > 160")
    kind = meta.get("type", "commercial")
    if kind == "commercial" and "<details>" not in body:
        errors.append(f"{slug}: нет FAQ")
    if kind != "legal" and not meta.get("lead"):
        errors.append(f"{slug}: нет lead")
    errors += text_checks(slug, expand(body) + " " + meta.get("lead", ""))
    known = {url_of(x.relative_to(SRC / "pages").with_suffix("").as_posix()) for x in (SRC / "pages").rglob("*.html")}
    planned = {"/", "/app/", "/mobile-version/", "/registration/", "/login/", "/verification/", "/bonus/", "/deposit/",
               "/withdrawal/", "/cricket/", "/football/", "/kabaddi/", "/tennis/", "/esports/", "/esports/cs2/",
               "/esports/dota2/", "/slots/", "/live-casino/", "/aviator/", "/crash-games/", "/support/",
               "/affiliate-program/", "/about/", "/contacts/", "/privacy-policy/", "/terms-and-conditions/",
               "/cookie-policy/", "/responsible-gambling/"}
    for href in re.findall(r'href="(/[^"#]*)', body):
        if href not in known | planned and not href.startswith("/assets/"):
            errors.append(f"{slug}: ссылка на несуществующую страницу {href}")
    out = page_html(slug, meta, body)
    if "{{" in out:
        errors.append(f"{slug}: остался шорткод")
    words = len(strip_tags(expand(body)).split())
    print(f"{url_of(slug)} T({len(t)}) D({len(d)}) words={words}")
    if errors:
        print("ОШИБКИ:\n" + "\n".join(errors))
        sys.exit(1)
    print("OK")


def main():
    if len(sys.argv) == 3 and sys.argv[1] == "--check":
        return check_page(sys.argv[2])
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copytree(SRC / "assets", OUT / "assets")

    errors = []
    titles, descs = {}, {}
    pages = sorted((SRC / "pages").rglob("*.html"))
    sitemap = []
    for p in pages:
        slug = p.relative_to(SRC / "pages").with_suffix("").as_posix()
        meta, body = parse(p)
        meta["title"] = tc(meta["title"])
        meta.setdefault("crumb", meta["h1"])
        meta["h1"] = tc(meta["h1"])
        if meta.get("offer"):
            meta["offer"]["title"] = tc(meta["offer"]["title"])
        t, d = meta["title"], meta["description"]
        if len(t) > 60:
            errors.append(f"{slug}: title {len(t)} > 60")
        if len(d) > 160:
            errors.append(f"{slug}: description {len(d)} > 160")
        if t in titles:
            errors.append(f"{slug}: title дублирует {titles[t]}")
        if d in descs:
            errors.append(f"{slug}: description дублирует {descs[d]}")
        titles[t], descs[d] = slug, slug
        errors += text_checks(slug, expand(body) + " " + meta.get("lead", ""))
        if meta.get("type", "commercial") == "commercial" and "<details>" not in body:
            errors.append(f"{slug}: нет FAQ")

        out = page_html(slug, meta, body)
        if "{{" in out:
            errors.append(f"{slug}: остался шорткод")
        if slug == "404":
            (OUT / "404.html").write_text(out, encoding="utf-8")
            continue
        dest = OUT / "index.html" if slug == "index" else OUT / slug / "index.html"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(out, encoding="utf-8")
        if "noindex" not in meta.get("robots", ""):
            prio = meta.get("priority", "0.5")
            sitemap.append(f"  <url><loc>{SITE}{url_of(slug)}</loc><lastmod>{UPDATED_ISO}</lastmod><priority>{prio}</priority></url>")
        print(f"{url_of(slug):30} T({len(t)}) D({len(d)})")

    (OUT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(sitemap) + "\n</urlset>\n", encoding="utf-8")
    (OUT / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")

    # Cloudflare (Workers static assets): кэш и заголовки безопасности
    (OUT / "_headers").write_text(
        "/*\n"
        "  X-Content-Type-Options: nosniff\n"
        "  Referrer-Policy: strict-origin-when-cross-origin\n"
        "  X-Frame-Options: SAMEORIGIN\n"
        "  Permissions-Policy: camera=(), microphone=(), geolocation=()\n"
        "/assets/*\n"
        "  Cache-Control: public, max-age=31536000, immutable\n"
        "/sitemap.xml\n"
        "  Cache-Control: public, max-age=3600\n"
        "/robots.txt\n"
        "  Cache-Control: public, max-age=3600\n",
        encoding="utf-8")

    if errors:
        print("\nОШИБКИ:\n" + "\n".join(errors))
        sys.exit(1)
    print(f"\nГотово: {len(pages)} страниц → {OUT}")


if __name__ == "__main__":
    main()
