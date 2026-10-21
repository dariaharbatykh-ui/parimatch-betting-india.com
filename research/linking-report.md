# Перелинковка: отчёт

Дата: 21.10.2026. Ядро и правила — от заказчика. Ссылки ставились в два круга: агент на страницу + отдельная проверка каждой страницы; затем сквозная проверка скриптом.

Допущение: правила применены к ссылкам в тексте страниц. Меню, хлебные крошки, логотип, футер и кнопки Sign Up / Download App (партнёрские) — навигация и интерфейс, правила 7, 8 и 15 к ним не применялись.

## Итог

- Ссылка на главную в первом экране: 27 из 27 страниц (на главной первый экран без ссылок).
- Новых ссылок в тексте: 27.
- Существующие ссылки не менялись (правило 12).

## Входящие ссылки из текста страниц

| Страница | Входящих |
|---|---|
| `/` | 27 |
| `/responsible-gambling/` | 27 |
| `/app/` | 22 |
| `/bonus/` | 20 |
| `/registration/` | 19 |
| `/deposit/` | 18 |
| `/withdrawal/` | 15 |
| `/support/` | 14 |
| `/login/` | 13 |
| `/verification/` | 12 |
| `/mobile-version/` | 10 |
| `/cricket/` | 9 |
| `/slots/` | 8 |
| `/live-casino/` | 7 |
| `/aviator/` | 5 |
| `/contacts/` | 4 |
| `/about/` | 4 |
| `/crash-games/` | 3 |
| `/football/` | 3 |
| `/esports/` | 3 |
| `/terms-and-conditions/` | 2 |
| `/privacy-policy/` | 2 |
| `/cookie-policy/` | 2 |
| `/kabaddi/` | 1 |
| `/affiliate-program/` | 1 |
| `/esports/dota2/` | 1 |
| `/esports/cs2/` | 1 |

На Kabaddi, Tennis, Esports, CS2, Dota 2, Crash Games и Affiliate Program мало входящих: на других страницах эти темы почти не упоминаются в обычном тексте (только в заголовках, таблицах и списках-метках, где ссылки запрещены), а дописывать текст правила не разрешают.

## Ссылка на главную в первом экране

| Страница | Анкор |
|---|---|
| `/about/` | Parimatch |
| `/affiliate-program/` | Parimatch |
| `/app/` | Parimatch |
| `/aviator/` | Parimatch |
| `/bonus/` | Parimatch |
| `/contacts/` | Parimatch |
| `/cookie-policy/` | Parimatch |
| `/crash-games/` | Parimatch |
| `/cricket/` | Parimatch |
| `/deposit/` | Parimatch |
| `/esports/` | Parimatch |
| `/esports/cs2/` | Parimatch bet |
| `/esports/dota2/` | Parimatch |
| `/football/` | Parimatch |
| `/` | — (главная, без ссылок) |
| `/kabaddi/` | Parimatch |
| `/live-casino/` | Parimatch |
| `/login/` | Parimatch |
| `/mobile-version/` | Parimatch site |
| `/privacy-policy/` | Parimatch |
| `/registration/` | Parimatch |
| `/responsible-gambling/` | Parimatch |
| `/slots/` | Parimatch |
| `/support/` | Parimatch |
| `/tennis/` | Parimatch |
| `/terms-and-conditions/` | Parimatch |
| `/verification/` | Parimatch |
| `/withdrawal/` | Parimatch |

## Новые ссылки в тексте

| Страница | Куда | Анкор |
|---|---|---|
| `/app/` | `/cricket/` | Parimatch cricket |
| `/app/` | `/slots/` | Parimatch casino |
| `/aviator/` | `/slots/` | Parimatch casino |
| `/aviator/` | `/login/` | Parimatch login |
| `/bonus/` | `/login/` | Parimatch login |
| `/bonus/` | `/live-casino/` | Parimatch live casino |
| `/bonus/` | `/aviator/` | Aviator Parimatch |
| `/bonus/` | `/crash-games/` | Parimatch JetX |
| `/bonus/` | `/kabaddi/` | kabaddi bettors |
| `/crash-games/` | `/mobile-version/` | mobile site |
| `/cricket/` | `/football/` | Parimatch football betting |
| `/deposit/` | `/login/` | Parimatch login |
| `/deposit/` | `/slots/` | Parimatch casino |
| `/esports/` | `/football/` | football leagues |
| `/live-casino/` | `/aviator/` | Aviator Parimatch |
| `/login/` | `/registration/` | Parimatch sign-up |
| `/mobile-version/` | `/withdrawal/` | Parimatch withdrawal |
| `/mobile-version/` | `/live-casino/` | Parimatch live casino |
| `/registration/` | `/withdrawal/` | Parimatch withdrawal |
| `/registration/` | `/live-casino/` | Parimatch live casino |
| `/registration/` | `/mobile-version/` | mobile browser |
| `/responsible-gambling/` | `/cricket/` | Parimatch cricket |
| `/responsible-gambling/` | `/login/` | Parimatch login |
| `/slots/` | `/aviator/` | Aviator Parimatch |
| `/support/` | `/bonus/` | Parimatch bonus |
| `/verification/` | `/slots/` | Parimatch casino |
| `/withdrawal/` | `/login/` | Parimatch sign in |

## Не поставлены (по правилам 3, 9, 10, 11)

| Страница | Куда | Причина |
|---|---|---|
| `/affiliate-program/` | `/withdrawal/` | The page never mentions player withdrawals. Every payout or payment mention (steps, cards, FAQ 'Payouts are usually monthly', 'questions about deal terms and payments') is about affiliate commission, so linking it to the |
| `/affiliate-program/` | `/mobile-version/` | No sentence mentions the mobile site or mobile version. The only mobile references are 'app reviews' in a step list and the PWA app bonus inside an <a class="card"> (already linked to /app/; rule 9). 'Parimatch mobile ve |
| `/affiliate-program/` | `/esports/` | 'Esports' appears only as a chip label in the 'Verticals to Promote' ul.chips tag list. That is a UI label list, and no chip list anywhere on the site contains links. 'Esports' on its own is not a core anchor, and turnin |
| `/app/` | `/live-casino/` | The page mentions live casino in only a few places. The "live dealer tables" sentence is in the paragraph that now holds the /cricket/ link, and turning it into "Parimatch live casino" would take 3 word changes. "Live Ca |
| `/app/` | `/aviator/` | Aviator appears only in a card (div.card) and in the chips list. No paragraph, list item or FAQ answer mentions Aviator, and adding it would add a fact. |
| `/app/` | `/football/` | Football appears only in a card (Live Betting) and in the chips list. No body sentence mentions football, so "Parimatch football betting" cannot be made with an edit of 2 words or fewer. |
| `/app/` | `/live-casino/` | No allowed spot. The hint sentence (line 26, 'live dealer tables') is in a paragraph that already holds the /cricket/ link (rule 11). It also does not contain a core key: turning 'live dealer tables' into 'Parimatch live |
| `/aviator/` | `/live-casino/` | The page never mentions live casino, Crazy Time or live dealer games. Getting "Parimatch live casino" or "Parimatch Crazy Time" would mean adding a new fact (for example, changing "the rest of the casino" to "live casino |
| `/aviator/` | `/cricket/` | The only sentence on topic, "Real money deposited for a cricket bet can be used in Aviator...", is in the In the App paragraph (line 96). That paragraph already links to /slots/ ("Parimatch casino"), so rule 11 rules it  |
| `/bonus/` | `/football/` | No natural spot. Football appears in the body only in "the natural pick for cricket, football and kabaddi bettors" (Sports bonus paragraph). Getting "Parimatch football betting" or "football betting at Parimatch" from th |
| `/bonus/` | `/football/` | The only body mention of football outside a card is in the same sentence and paragraph (line 35) that now holds the /kabaddi/ link, and rule 11 allows one new link per paragraph. The other mention is in a promotion card  |
| `/crash-games/` | `/withdrawal/` | No sentence can hold a core anchor. The only withdrawal wording is "withdrawing before the wagering is finished cancels the bonus" (getting "a Parimatch withdrawal" takes 3 word edits) and "KYC is required before bonus w |
| `/crash-games/` | `/tennis/` | The page never mentions tennis or tennis betting. Adding "tennis betting" would add a fact and take more than 2 words. |
| `/cricket/` | `/login/` | No sentence contains a login anchor or can take one with an edit of 2 words or fewer. The only login wording is "to logged-in users" in the streaming paragraph and the streaming FAQ answer, and turning that into "after P |
| `/cricket/` | `/aviator/` | Aviator is mentioned only inside the CricketX <div class="card"> ("Aviator and JetX sit in the same section."), and rule 9 bans links in cards. It is not mentioned anywhere else. |
| `/cricket/` | `/esports/` | The page never mentions esports, so no anchor for "Parimatch esports" can be made with a light edit. |
| `/cricket/` | `/kabaddi/` | The page never mentions kabaddi, so no anchor for "kabaddi betting" can be made with a light edit. |
| `/cricket/` | `/login/` | No core login key fits within a 2-word light edit. The hinted step 1 already links to /registration/ (rule 11: one link per list item). Its 'log in' sits in the <strong> step title, which acts as a heading, and turning i |
| `/deposit/` | `/live-casino/` | The body only mentions Live Casino in the welcome-bonus table (rule 9 forbids table links). No paragraph, list item or FAQ answer can get "Parimatch live casino" or "Parimatch Crazy Time" with an edit of 2 words or fewer |
| `/deposit/` | `/esports/dota2/` | The page never mentions Dota 2 or esports, so no core or by-analogy anchor fits without adding facts. |
| `/esports/` | `/login/` | No core login anchor fits. The only login wording is 'Logged-in users can watch selected events' (Live Betting list) and 'for logged-in users' (FAQ streaming answer). Getting 'Parimatch login' or 'Parimatch sign in' woul |
| `/esports/` | `/cricket/` | The body never uses the word 'cricket' in a usable spot. 'cricket' appears only in the lead, where only the home link is allowed, and in 'Virtual Cricket' (note), which is a UI section name and means simulated events, so |
| `/esports/` | `/kabaddi/` | Kabaddi is not mentioned anywhere on the page, and 'kabaddi betting' cannot be added without adding a fact. |
| `/esports/` | `/tennis/` | Tennis is not mentioned anywhere on the page, and 'tennis betting' cannot be added without adding a fact. |
| `/esports/` | `/cricket/` | The core anchors are 'Parimatch cricket' and 'Parimatch cricket betting', and neither appears in the body. The hint sentence in the note only says 'Virtual Cricket', and adding 'Parimatch' there would still not give a co |
| `/esports/cs2/` | `/login/` | No sentence about logging in can take a login anchor. The only mention is "Selected events can be streamed for logged-in users" (Live list item), and turning that into "Parimatch login" or "Parimatch sign in" needs more  |
| `/esports/cs2/` | `/cricket/` | The page never mentions cricket. The closest spot is the FAQ "₹10, the same as on other sports", and adding cricket there would add a fact and need more than 2 words. |
| `/esports/cs2/` | `/football/` | The page never mentions football, so a football anchor would need new content and new facts. |
| `/esports/cs2/` | `/kabaddi/` | The page never mentions kabaddi, so a kabaddi anchor would need new content and new facts. |
| `/esports/cs2/` | `/tennis/` | The page never mentions tennis, so a tennis anchor would need new content and new facts. |
| `/esports/dota2/` | `/slots/` | The page never says casino or slot. Every 'game' refers to a Dota 2 map ('game length', 'a fast game', 'a thrown game', 'late-game drafts'), so linking it to slots goes against the context (rule 10). Getting 'Parimatch c |
| `/esports/dota2/` | `/cricket/` | Cricket is never mentioned on the page. Adding 'Parimatch cricket' anywhere would add a new fact and take more than a 2-word edit (rules 3 and 5). |
| `/esports/dota2/` | `/football/` | Football is never mentioned on the page. No sentence can carry 'Parimatch football betting' with a 2-word edit or less without adding facts. |
| `/esports/dota2/` | `/kabaddi/` | Kabaddi is never mentioned on the page. No sentence can carry 'kabaddi betting' with a 2-word edit or less without adding facts. |
| `/esports/dota2/` | `/tennis/` | Tennis is never mentioned on the page. No sentence can carry 'tennis betting' with a 2-word edit or less without adding facts. |
| `/football/` | `/slots/` | The page never mentions casino, slots or games in a Parimatch-game sense. No core anchor (Parimatch casino, Parimatch online casino, Parimatch game, best game in Parimatch) can be made with an edit of 2 words or fewer wi |
| `/football/` | `/live-casino/` | There is no mention of live casino or Crazy Time. "Live" on this page always means in-play football betting (the Live section, All Live, Hot Matches), so a live casino link would contradict the context (rule 10). |
| `/football/` | `/kabaddi/` | Kabaddi is not mentioned anywhere on the page. Adding "kabaddi betting" would add a new fact and take more than 2 words. |
| `/football/` | `/tennis/` | Tennis is not mentioned anywhere on the page. Adding "tennis betting" would add a new fact and take more than 2 words. |
| `/football/` | `/esports/cs2/` | CS2 is not mentioned. The only esports sentence (line 48, EA SPORTS FC / E-Football) already holds the /esports/ link, and naming CS2 there would add a fact and break the one-link-per-paragraph rule. |
| `/` | `/esports/cs2/` | CS2 is mentioned only in the esports card heading (<a class="card" href="/esports/">…<h3>CS2, Dota 2 and More</h3>), where links are forbidden by rule 9, and in a table cell. No paragraph, list item or FAQ answer mention |
| `/` | `/esports/dota2/` | Same as CS2: Dota 2 appears only in the card heading (rule 9 forbids links there). No sentence in the body text mentions Dota 2 or esports, so "Dota 2 betting" or "Parimatch Dota 2 betting" cannot be added with an edit o |
| `/` | `/affiliate-program/` | The page never mentions an affiliate program. The nearest wording does not fit. Line 37 "brand partners" is about sponsorships (Sunil Narine, Manchester United, Leeds United), so a link there would contradict the target  |
| `/kabaddi/` | `/slots/` | The only place the casino comes up in the body is line 19: "One account and balance cover kabaddi, <a href="/cricket/">cricket betting</a> and the casino." Changing it to "the Parimatch casino" would be a 1-word edit, bu |
| `/kabaddi/` | `/live-casino/` | "Parimatch live casino" and "Parimatch Crazy Time" do not appear in the text, and no edit of 2 words or fewer creates them. The page's "Live" mentions ("Parimatch Live section", "All Live / Live Events") are about in-pla |
| `/kabaddi/` | `/esports/` | Esports is never mentioned on the page. Adding "Parimatch esports" (for example to "listed alongside cricket and football" or "other sports") would add a fact, which rule 5 forbids. |
| `/kabaddi/` | `/tennis/` | Tennis is never mentioned on the page. Adding "tennis betting" would add a fact (rule 5), and no edit of 2 words or fewer works. |
| `/kabaddi/` | `/esports/cs2/` | CS2 is never mentioned on the page. Adding "CS2 betting" would add a fact (rule 5), and no edit of 2 words or fewer works. |
| `/kabaddi/` | `/login/` | The hint list item (step 1, line 76) already holds the /registration/ link (rule 11). Its only login wording, 'log in', sits in the bold step label <strong>Create an account or log in</strong>, which works like a heading |
| `/live-casino/` | `/crash-games/` | The page never mentions JetX or crash games. The only nearby wording is "Aviator" and the section name "Instant Games". Getting "Parimatch JetX" or "Parimatch crash games" would mean changing or adding facts, so no natur |
| `/live-casino/` | `/esports/dota2/` | The page is about live casino and never mentions Dota 2 or esports. "Dota 2 betting" could not be added with an edit of 2 words or fewer without adding facts. |
| `/login/` | `/live-casino/` | The page never mentions live casino, Crazy Time or casino games. The only possible spots ("the main sections are one tap away", the bonus card) would need new words and a new fact (more than 2 words), and one of them is  |
| `/mobile-version/` | `/slots/` | No allowed body text mentions the casino, slots or a Parimatch game in a way that fits a core anchor (Parimatch casino / online casino / Parimatch game) with at most 2 words of edit. Casino mentions are only in the lead, |
| `/mobile-version/` | `/aviator/` | Aviator appears only inside the "Slots and Live Tables" card (div.card), where links are forbidden. No other sentence mentions Aviator, so "Aviator Parimatch" cannot be formed in at most 2 words. |
| `/mobile-version/` | `/crash-games/` | The page never mentions JetX or crash games. The only nearby term is "Instant Games" (a bonus/section name in a card and an FAQ answer). Swapping it for "Parimatch crash games" would change the fact and take more than 2  |
| `/mobile-version/` | `/slots/` | No core anchor for /slots/ can be formed within the rules. The only body sentence that mentions slots or casino and may take a link is the FAQ answer on line 145: "Slots, Live Casino or Instant Games offers can be picked |
| `/registration/` | `/aviator/` | The page never mentions Aviator. It only names "Instant Games" offers, and those sit in step-list items and the bonus table. Building "Aviator Parimatch" would mean adding Aviator as a new fact (rule 5), so it can't be d |
| `/registration/` | `/slots/` | No core anchor can be made with an edit of 2 words or fewer. The page only has the offer name "Slots" (step 3 list item, the bonus table and the note). Turning that into "Parimatch casino", "Parimatch online casino" or " |
| `/responsible-gambling/` | `/aviator/` | The page never mentions Aviator, crash games or any specific casino game, only "casino games" in general. Adding "Aviator Parimatch" would mean adding a new fact, which breaks rules 3 and 5. |
| `/responsible-gambling/` | `/football/` | Football appears in only one sentence on the page: the 'Principles' paragraph, which now holds the /cricket/ link. Rule 11 allows one new link per paragraph. The only other sports mention is 'IPL season' inside a div.car |
| `/slots/` | `/cricket/` | No sentence talks about cricket betting. The page only mentions cricket through the "Cricket Slots" shelf (cricket-themed slot games, lines 18 and 57), so a cricket-betting link there would go against the context (rule 1 |
| `/slots/` | `/cricket/` | No sentence in the body speaks about cricket betting. The word 'cricket' only shows up in the name of the 'Cricket Slots' casino shelf (lines 18 and 57: 'Cricket Slots and Parimatch Exclusive shelves sit next to the usua |
| `/support/` | `/aviator/` | The page never mentions Aviator, casino or games. The only anchor, "Aviator Parimatch", cannot be made with an edit of 2 words or fewer without adding a fact. |
| `/support/` | `/affiliate-program/` | The page never mentions affiliates, partners or the affiliate program. "Parimatch affiliate program" cannot be made with an edit of 2 words or fewer without adding a fact. |
| `/tennis/` | `/aviator/` | Aviator is not mentioned anywhere on the page, so no anchor fits within 2 words without adding a fact. |
| `/tennis/` | `/football/` | "football" appears only once, in the overview paragraph that now holds the new /slots/ link (and the existing /cricket/ link), so a second new link there would break rule 11. Both anchors would also need 2 or more insert |
| `/tennis/` | `/esports/` | Esports are not mentioned on the tennis page, so no anchor is possible within 2 words without adding a fact. |
| `/tennis/` | `/kabaddi/` | Kabaddi is not mentioned on the tennis page, so no anchor is possible within 2 words without adding a fact. |
| `/tennis/` | `/football/` | The only mention of football on the page is in the overview paragraph (line 18), which already holds the round-1 link to /cricket/ ('cricket betting'). Linking 'football' there would put two adjacent links in one paragra |
| `/terms-and-conditions/` | `/ (alternative anchors)` | Plain "Parimatch" was used because "Parimatch Betting India" is the site's proper name, so lowercasing it to "Parimatch betting" would distort the name. "Is not operated by Parimatch" was rejected because a link to the g |
| `/verification/` | `/crash-games/` | The page never mentions crash games, JetX, Aviator or instant games. Its only casino mention is "casino games" in the When-needed paragraph, which now holds the /slots/ link (one new link per paragraph). Changing it to " |
| `/withdrawal/` | `/crash-games/` | The page never mentions crash games, JetX or Aviator. The nearest wording is the bonus-cap category "Instant Games" in the bonus note. Changing it would alter a category name (a factual change), and that paragraph alread |
| `/withdrawal/` | `/slots/` | "Slots" appears only in the active-bonus warning note ("about 5x the bonus for Sports and Slots..."). That paragraph already links to /bonus/. No core anchor fits without changing facts: turning "Slots" into "Parimatch c |
| `/withdrawal/` | `/live-casino/` | "Live Casino" appears only in the same active-bonus warning paragraph, which already holds the /bonus/ link. Rule 11 allows one new link per paragraph and says to avoid paragraphs that already have one, and no other sent |

## Ключи ядра, которые не использованы как анкоры

- **parimatch official site, parimatch official website, parimatch official app** — на сайте нет упоминаний официального сайта (правило заказчика).
- **parimatch promo code no deposit** — бездепозитного промокода в фактах нет (правило 3).
- **parimatch withdrawal limit per day** — лимита в день в фактах нет, только за одну заявку (правило 3).
- **parimatch login bonus** — такого бонуса в фактах нет.
- **parimatch exchange, parimatch horse racing** — нет страницы и фактов.
- **parimatch bd, parimatch bangladesh** — другой рынок.
- **parimatch customer care number, parimatch contact number, parimatch helpline number india, parimatch number** — сайт не публикует телефоны поддержки, контекст противоречит (правило 10).
- **parimatch promo code today, parimatch link** — в текстах нет подходящих фраз без переписывания.

## Дубли ссылок (правило 8) — исправлено 21.10.2026

На каждой странице оставлена одна ссылка на один URL. Где на тот же URL вела карточка, осталась карточка, а ссылка в тексте или таблице снята (текст анкора не менялся). Где обе ссылки были в тексте, осталась первая.

| Страница | URL | Снятая ссылка |
|---|---|---|
| `/registration/` | `/login/` | «Parimatch login page» (Common Registration Problems) |
| `/registration/` | `/app/` | «Parimatch app page» (осталась карточка Step 3) |
| `/support/` | `/withdrawal/` | «Withdrawal guide» ×2 в таблице Help Centre Articles (осталась карточка) |
| `/support/` | `/registration/` | «Registration guide» в таблице (осталась карточка) |
| `/support/` | `/app/` | «App guide» в таблице (осталась карточка) |
| `/support/` | `/login/` | «Parimatch login page» (осталась карточка) |
| `/support/` | `/deposit/` | «Parimatch deposit guide» (осталась карточка) |
| `/support/` | `/verification/` | «verification page» (осталась карточка) |
| `/login/` | `/verification/` | «account verification» в таблице (осталась карточка) |
| `/verification/` | `/withdrawal/` | «Parimatch withdrawal guide» (осталась карточка) |
| `/crash-games/` | `/aviator/` | «Parimatch Aviator guide» (осталась карточка) |
| 404 | `/` | карточка Home (осталась кнопка Go to the Home Page) |

## Старые ссылки в таблицах (правило 9) — не менялись

- `/contacts/`: `/deposit/` («Parimatch deposit guide»)
- `/contacts/`: `/withdrawal/` («Parimatch withdrawal guide»)
- `/contacts/`: `/verification/` («Parimatch verification guide»)
- `/contacts/`: `/login/` («Parimatch login help»)
- `/support/`: `/mobile-version/` («mobile version guide»)

`/responsible-gambling/` получает ссылки почти со всех страниц (27) — это старые ссылки из напоминаний об ответственной игре; оставлены по правилу 12.
