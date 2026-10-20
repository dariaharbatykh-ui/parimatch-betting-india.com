# Структура сайта (утверждено 20.10.2026)

28 страниц + 404.

## Основные (9)

| # | URL | Страница |
|---|---|---|
| 1 | `/` | Главная |
| 2 | `/app/` | Приложение: Android APK, iOS и ПК разделами на одной странице |
| 3 | `/mobile-version/` | Мобильная версия |
| 4 | `/registration/` | Регистрация |
| 5 | `/login/` | Вход |
| 6 | `/verification/` | Верификация (KYC) |
| 7 | `/bonus/` | Бонусы: welcome-бонусы и все акции |
| 8 | `/deposit/` | Пополнение |
| 9 | `/withdrawal/` | Вывод |

## Betting (7)

В меню пункт Betting — хаб со ссылкой `#`, отдельной страницы нет.

| # | URL | Страница |
|---|---|---|
| 10 | `/cricket/` | Cricket |
| 11 | `/football/` | Football |
| 12 | `/kabaddi/` | Kabaddi |
| 13 | `/tennis/` | Tennis |
| 14 | `/esports/` | Esports |
| 15 | `/esports/cs2/` | CS2 |
| 16 | `/esports/dota2/` | Dota 2 |

## Casino (4)

В меню пункт Casino — хаб со ссылкой `#`, отдельной страницы нет.

| # | URL | Страница |
|---|---|---|
| 17 | `/slots/` | Slots |
| 18 | `/live-casino/` | Live Casino |
| 19 | `/aviator/` | Aviator |
| 20 | `/crash-games/` | Crash Games |

## Информационные (2)

| # | URL | Страница |
|---|---|---|
| 21 | `/support/` | Support: страница о поддержке |
| 22 | `/affiliate-program/` | Affiliate Program |

## Служебные (6)

На первом экране кнопки Register и Download App.

| # | URL | Страница |
|---|---|---|
| 23 | `/about/` | About Us |
| 24 | `/contacts/` | Contacts |
| 25 | `/privacy-policy/` | Privacy Policy |
| 26 | `/terms-and-conditions/` | Terms and Conditions |
| 27 | `/cookie-policy/` | Cookie Policy |
| 28 | `/responsible-gambling/` | Responsible Gambling |

## Технические

- `404`
- `sitemap.xml`
- `robots.txt`

## Убрано по решению заказчика

`/app/android-apk/`, `/app/ios/`, `/app/pc/`, `/promo-code/`, `/promotions/` (акции перенесены в `/bonus/`), `/payments/`, `/betting/`, `/casino/` (только пункты меню), `/ipl/`, `/horse-racing/`, `/live-betting/`, `/virtual-sports/`, `/how-to-bet/`, `/teen-patti/`, `/andar-bahar/`, `/crazy-time/`, `/review/`, `/is-parimatch-legal-in-india/`, `/ambassadors/`, `/faq/` (FAQ-блок на каждой странице), HTML-карта сайта, страницы авторов, `/go/`.

## Меню

- Header: App · Registration · Login · Bonus · Betting ▾ (`#`) · Casino ▾ (`#`) · Support, кнопки Sign Up и Download App.
- Betting ▾: Cricket, Football, Kabaddi, Tennis, Esports (CS2, Dota 2).
- Casino ▾: Slots, Live Casino, Aviator, Crash Games.
- Footer: Information (About Us, Contacts, Support, Affiliate Program) · Rules & Policies (Privacy Policy, Terms and Conditions, Cookie Policy, Responsible Gambling) · логотипы платёжек · 18+ · короткая пометка о партнёрском характере сайта.

## Правила для всех страниц

- FAQ-блок на каждой контентной странице, на служебных его нет.
- Официальный сайт не упоминаем. Третье лицо («Parimatch», «the platform»), без местоимений.
- Без блоков pros/cons. Заголовки и meta title в Title Case.
- Кнопки Register и Download App ведут на партнёрские ссылки из `README.md`.
- Сквозные элементы: хлебные крошки, оглавление, дата обновления, липкий CTA-бар на мобильных, плашка 18+, cookie-баннер.
- Разметка: Organization, FAQPage, HowTo, BreadcrumbList, SoftwareApplication на `/app/`.
