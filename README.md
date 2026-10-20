# parimatch-betting-india.com

Партнёрский сайт о Parimatch для игроков из Индии, на английском (lang="en").

Статический сайт на чистом HTML/CSS без React: 28 страниц + 404.

## Что внутри

| Путь | Что внутри |
|---|---|
| `src/pages/*.html` | контент страниц (вложенные: `src/pages/esports/cs2.html` → `/esports/cs2/`); сверху JSON с метаданными (`title`, `description`, `lead`, `h1`, `crumb`, `offer`, `type`) |
| `src/assets/` | `style.css` (чёрный + жёлтый в стиле Parimatch), `site.js` (меню, подменю Betting/Casino, табы), `favicon.svg`, `fonts/` (Manrope, OFL) |
| `build.py` | собирает `public/`: шапка с меню, футер, хлебные крошки, оглавление, schema.org, `sitemap.xml`, `robots.txt`; проверяет title ≤ 60, description ≤ 160, дубли, FAQ, упоминания официального сайта, местоимения we/our и it/they рядом с брендом, pros/cons |
| `public/` | готовый сайт (не в git, собирается командой) |
| `facts.md` | база фактов: официальные данные + самое частое и правдоподобное у 22 сателлитов, с уровнем уверенности |
| `research/` | анализ выдачи, структура, официальные факты, скриншоты |
| `serve.mjs` | локальный сервер |

## Команды

```bash
npm run build
```

```bash
npm run dev
```

Локально: http://localhost:8090. Проверка одной страницы без сборки: `python3 build.py --check <slug>`.

## Партнёрские ссылки

| Кнопка | URL |
|---|---|
| Register / Sign Up | `https://pbic.parimatch-betting-india.com/vZdjWYy` |
| Download App | `https://pbic.parimatch-betting-india.com/vZdjWYy?type=app` |

Ссылки ставятся напрямую (`rel="nofollow sponsored"`), без промежуточной страницы `/go/`. Поддомен `pbic.` — сервис редиректов, его не трогаем.

## Правила текста

- Официальный сайт Parimatch не упоминаем.
- Пишем в третьем лице: «Parimatch», «the platform», без местоимений.
- Без блоков pros/cons.
- Все заголовки и meta title в Title Case.
- Цифры (бонусы, лимиты, платежи) берём с официального сайта. Если официальных данных нет, берём самое частое и правдоподобное значение у сателлитов (см. `facts.md`).
