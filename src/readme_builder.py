import datetime
import json
from src.config import STATS_FILE, README_FILE
from src.utils import logger

REPO = "ewecrow78-gif/Free_VPN_Aggregator"
RAW_GH = "https://raw.githubusercontent.com/" + REPO + "/main/configs"
JSDELIVR = "https://cdn.jsdelivr.net/gh/" + REPO + "@output"
GITHACK = "https://raw.githack.com/" + REPO + "/main/configs"
FASTLY = "https://fastly.jsdelivr.net/gh/" + REPO + "@output"


def _b64(name: str) -> str:
    return f"{RAW_GH}/base64/{name}.txt"


def _qr(name: str) -> str:
    return f"{RAW_GH}/qr/{name}.png"


def _clash(name: str) -> str:
    return f"{RAW_GH}/clash/{name}.yaml"


def _sing(name: str) -> str:
    return f"{RAW_GH}/sing-box/{name}.json"


def _mirrors(rel_path: str) -> str:
    return "\n".join(
        [
            f"- **GitHub RAW:** `{RAW_GH}/{rel_path}`",
            f"- **jsDelivr:** `{JSDELIVR}/{rel_path}`",
            f"- **GitHack:** `{GITHACK}/{rel_path}`",
            f"- **Fastly:** `{FASTLY}/{rel_path}`",
        ]
    )


def sub_card(
    title: str,
    b64_name: str,
    desc: str,
    *,
    raw_rel: str | None = None,
    badge: str = "",
    count_hint: str = "",
) -> str:
    """Card block inspired by igareck: title + link + QR + description."""
    link = _b64(b64_name)
    label = f"base64/{b64_name}.txt"
    count = f" ({count_hint})" if count_hint else ""
    badge_s = f" {badge}" if badge else ""
    raw_rel = raw_rel or f"{b64_name}.txt"
    return f"""### {title}{badge_s}{count}

### [{label}]({link})

<details>
<summary>QR-код</summary>

![qr-{b64_name}]({_qr(b64_name)})

</details>

`{desc}`

<details>
<summary>🪞 Зеркала и другие форматы</summary>

**Base64 (рекомендуется):**
{_mirrors(f"base64/{b64_name}.txt")}

**Raw TXT:**
{_mirrors(raw_rel)}

| Формат | Ссылка |
| :--- | :--- |
| Base64 | [open]({link}) |
| Raw | [open]({RAW_GH}/{raw_rel}) |
| Clash | [yaml]({_clash(b64_name)}) |
| Sing-Box | [json]({_sing(b64_name)}) |
| QR | [png]({_qr(b64_name)}) |

</details>

---
"""


README_TEMPLATE = """<div align="center">

<a href="https://github.com/ewecrow78-gif/Free_VPN_Aggregator">
  <img src="https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/assets/banner.svg" alt="Free VPN Aggregator">
</a>

<br><br>

# <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNTljeGk4d3lzZnU3Mm1peDBienFpbmEyb3JmaDB5N21tMW9oczIwdyZlcD12MV9zdGlja2Vyc19zZWFyY2gmY3Q9cw/8p1WPEOeDWFCksfe18/giphy.gif" width="45"> Бесплатные VPN-конфигурации, работающие в РФ

[![Stars](https://img.shields.io/github/stars/ewecrow78-gif/Free_VPN_Aggregator?style=flat)](https://github.com/ewecrow78-gif/Free_VPN_Aggregator/stargazers)
<a href="https://github.com/ewecrow78-gif/Free_VPN_Aggregator"><img src="https://komarev.com/ghpvc/?username=ewecrow78-gif&label=Visitors&color=0e75b6&style=flat" alt="Visitor Count" /></a>
[![Issues](https://img.shields.io/github/issues/ewecrow78-gif/Free_VPN_Aggregator?style=flat&color=0e75b6)](https://github.com/ewecrow78-gif/Free_VPN_Aggregator/issues)
[![Last commit](https://custom-icon-badges.demolab.com/github/last-commit/ewecrow78-gif/Free_VPN_Aggregator?logo=history&logoColor=white&color=0e75b6&style=flat)](https://github.com/ewecrow78-gif/Free_VPN_Aggregator/commits/main)
<a href="https://github.com/ewecrow78-gif/Free_VPN_Aggregator"><img src="https://badges.frapsoft.com/os/v2/open-source.png?v=103" alt="Open Source Love"></a>
[![Auto-update](https://github.com/ewecrow78-gif/Free_VPN_Aggregator/actions/workflows/update.yml/badge.svg)](https://github.com/ewecrow78-gif/Free_VPN_Aggregator/actions)

**Автообновляемая коллекция VLESS, VMess, Trojan, Shadowsocks и Reality для пользователей из России**

`VLESS` · `Trojan` · `Shadowsocks` · `VMess` · `Reality` · Xray-core

[🌐 Репозиторий](https://github.com/ewecrow78-gif/Free_VPN_Aggregator) · [💬 Telegram](https://t.me) · [📦 Ветка output](https://github.com/ewecrow78-gif/Free_VPN_Aggregator/tree/main/configs)

</div>

---

## 📑 Содержание

- [📖 Описание](#-описание)
- [🚀 Быстрый старт](#-быстрый-старт-что-выбрать)
- [📊 Статус сети](#-статус-сети)
- [📋 Подписки](#-подписки)
  - [⚫ Обычный режим](#️-обычный-режим-чёрные-списки)
  - [⚪ Обход белых списков](#️-обход-белых-списков)
  - [📱 Мобильные](#-мобильные--лёгкие)
  - [📦 Полный список ссылок](#-полный-список-ссылок-для-клиента)
- [🪞 Зеркала](#-зеркала)
- [🗂️ Гайды по клиентам](#️-гайды-по-клиентам)
- [⚙️ Как это работает](#️-как-это-работает)
- [🗂 Структура репозитория](#-структура-репозитория)
- [🔧 Локальный запуск](#-локальный-запуск)
- [⚠️ Безопасность](#️-безопасность)
- [📊 Статистика](#-статистика)
- [📜 Лицензия](#-лицензия)

---

## 📖 Описание

Автоматически обновляемая коллекция **публичных** VPN-конфигов, которые проходят **реальную проверку через Xray-core** (не просто парсинг и дедуп).

Каждая подписка — TXT / Base64 / Clash / Sing-Box для клиентов:
`v2rayNG`, `v2rayN`, `Hiddify`, `Happ`, `V2Box`, `Throne`, `Karing`, `NekoBox`, `Clash Meta` и др.

Раз в **2 часа** GitHub Actions:

1. собирает конфиги из публичных источников и Telegram;
2. отсеивает мёртвые DNS/TCP;
3. гоняет **HTTP-тест через Xray** (latency, jitter, success rate, DPI/YouTube);
4. обновляет **Stable Pool** (история успехов/провалов);
5. публикует подписки в ветку [`output`](https://github.com/ewecrow78-gif/Free_VPN_Aggregator/tree/main/configs).

> [!IMPORTANT]
> **Добавляйте ссылку подписки в клиент, а не скачивайте файл вручную.**  
> Тогда список серверов будет обновляться сам.

---

## 🚀 Быстрый старт: что выбрать?

<details open>
<summary><b>👇 Если вы здесь впервые — читайте сюда</b></summary>

### Дорогие друзья!

| Ваша ситуация | Берите подписку | Зачем |
| :--- | :--- | :--- |
| 🥇 **Не знаю, что выбрать** | [recommended]({base_url}base64/recommended.txt) | Стабильность + score + DPI |
| 📱 **Телефон** | [top_150_mobile]({base_url}base64/top_150_mobile.txt) | Лёгкий список |
| 🚀 **Минимальный пинг** | [top_fast]({base_url}base64/top_fast.txt) | Топ по latency |
| ⚪ **Белые списки у оператора** | [ru_mobile_whitelist]({base_url}base64/ru_mobile_whitelist.txt) | Whitelist bypass |
| 🔒 **SNI/CIDR** | [sni_cidr_bypass]({base_url}base64/sni_cidr_bypass.txt) | TLS + SNI |
| 💎 **Максимум качества** | [whitelist_premium]({base_url}base64/whitelist_premium.txt) | Жёсткий отбор |

**Клиенты на старт**

| Платформа | Клиент |
| :--- | :--- |
| Android | **v2rayNG** / **Happ** / **Karing** |
| iOS | **Happ** / **V2Box** / **Streisand** |
| Windows / Linux | **Throne** / **v2rayN** / **Hiddify** |
| macOS | **Hiddify** / **V2Box** |

1. Скопируйте **Base64**-ссылку.  
2. Импортируйте URL в клиент (см. [гайды](#️-гайды-по-клиентам)).  
3. Обновите подписку → **проверьте пинг** → сортировка → Connect.

</details>

---

## 📊 Статус сети

> Автообновление пайплайном. Время: **{update_time} UTC**.

| Показатель | Значение | Описание |
| :--- | :---: | :--- |
| **Собрано ссылок** | `{downloaded_lines}` | Сырые строки из источников |
| **Уникальных конфигов** | `{parsed_configs}` | После парсинга / дедупа |
| **Отсеяно (синтаксис / IP)** | `{rejected_syntax}` | Битый URI, private IP |
| **Отсеяно (DNS / TCP)** | `{rejected_dns}` | Мёртвые домены / порты |
| **Рабочих (Xray test)** | `{xray_alive}` | Реальный HTTP через VPN |
| **В выдаче (top)** | `{total}` | Лимит клиентских подписок |
| **Whitelist** | `{whitelists}` | White-list сценарий |
| **Premium** | `{premium}` | Жёсткий отбор |
| **Recommended** | `{recommended}` | Для новичков |
| **Mobile** | `{mobile}` | Лёгкие протоколы |

---

## 📋 Подписки

> [!TIP]
> Для клиентов почти всегда берите **Base64**.  
> Если `raw.githubusercontent.com` не открывается — [🪞 Зеркала](#-зеркала).

### ⚫ Обычный режим (чёрные списки)

*Обычный интернет без жёсткого whitelist у провайдера.*

{card_recommended}
{card_top_fast}
{card_alive}

### ⚪ Обход белых списков

*Когда «режут» всё, кроме белых IP/SNI.*

{card_ru_mobile_wl}
{card_wl_all}
{card_wl_small}
{card_wl_premium}
{card_sni}

### 📱 Мобильные / лёгкие

*Меньше узлов = быстрее импорт и пинг-тест на телефоне.*

{card_top150}
{card_mobile}
{card_happ}

### ⚠️ Risky

{card_insecure}

---

### 📦 Полный список ссылок для клиента

<details>
<summary><b>📋 Раскрыть все Base64 URL (копировать в клиент)</b></summary>

> Рекомендуемые: **[recommended]({base_url}base64/recommended.txt)**, **[top_fast]({base_url}base64/top_fast.txt)**, **[top_150_mobile]({base_url}base64/top_150_mobile.txt)**, **[ru_mobile_whitelist]({base_url}base64/ru_mobile_whitelist.txt)**, **[sni_cidr_bypass]({base_url}base64/sni_cidr_bypass.txt)**.

- [x] **Вечно актуальные (ветка output)**

1) `{base_url}base64/recommended.txt`
2) `{base_url}base64/top_fast.txt`
3) `{base_url}base64/alive.txt`
4) `{base_url}base64/mobile.txt`
5) `{base_url}base64/top_150_mobile.txt`
6) `{base_url}base64/ru_mobile_whitelist.txt`
7) `{base_url}base64/whitelist_all.txt`
8) `{base_url}base64/whitelist_small.txt`
9) `{base_url}base64/whitelist_premium.txt`
10) `{base_url}base64/sni_cidr_bypass.txt`
11) `{base_url}base64/happ.txt`
12) `{base_url}base64/incy.txt`
13) `{base_url}base64/allow_insecure.txt`

🔗 QR: `{base_url}qr/` (например `recommended.png`)

</details>

---

## 🪞 Зеркала

> **Сохраните зеркала** на случай сбоев GitHub RAW.

| Зеркало | Правило | Пример (recommended) |
| :--- | :--- | :--- |
| **GitHub RAW** | основное | `{base_url}base64/recommended.txt` |
| **jsDelivr** | CDN | `{jsdelivr}/base64/recommended.txt` |
| **Fastly jsDelivr** | CDN | `{fastly}/base64/recommended.txt` |
| **GitHack** | live proxy | `{githack}/base64/recommended.txt` |

<details>
<summary><b>Готовые зеркала recommended / top_fast / whitelist / sni</b></summary>

#### recommended
```
{base_url}base64/recommended.txt
{jsdelivr}/base64/recommended.txt
{githack}/base64/recommended.txt
{fastly}/base64/recommended.txt
```

#### top_fast
```
{base_url}base64/top_fast.txt
{jsdelivr}/base64/top_fast.txt
{githack}/base64/top_fast.txt
```

#### ru_mobile_whitelist
```
{base_url}base64/ru_mobile_whitelist.txt
{jsdelivr}/base64/ru_mobile_whitelist.txt
{githack}/base64/ru_mobile_whitelist.txt
```

#### sni_cidr_bypass
```
{base_url}base64/sni_cidr_bypass.txt
{jsdelivr}/base64/sni_cidr_bypass.txt
{githack}/base64/sni_cidr_bypass.txt
```

</details>

✦ **jsDelivr** иногда кэширует дольше — если список «старый», берите **GitHack** или прямой GitHub RAW.

---

## 🗂️ Гайды по клиентам

<details>
<summary><b>📱 Android — v2rayNG</b></summary>

1. Скачайте **v2rayNG**: [Releases](https://github.com/2dust/v2rayNG/releases)
2. Скопируйте Base64-ссылку (например recommended).
3. **☰ → Группы (подписки) → ＋ → URL подписки**.
4. Имя: `FreeVPN`, URL: вставить → сохранить.
5. **⋮ → Обновить подписку**.
6. **⋮ → Проверить задержку** → сортировка по пингу.
7. Выберите сервер → ▶️.

<details>
<summary>⚠ Нет интернета / handshake timeout</summary>

- Остановите приложение полностью и запустите снова.
- Обновите подписку и заново проверьте пинг.
- DNS: 1.1.1.1 / 8.8.8.8.
- Другая подписка: `top_fast` или `sni_cidr_bypass`.

</details>

<details>
<summary>🔄 Обновление подписки</summary>

☰ → Группы → иконка круговой стрелки.

</details>

</details>

<details>
<summary><b>📱 Android / Multi — Happ, Hiddify, Karing</b></summary>

### Happ
1. **＋ → Import from URL/Clipboard**.
2. URL: `{base_url}base64/happ.txt` или `recommended.txt`.
3. Обновите → лучший пинг → Connect.

### Hiddify
1. **Новый профиль → из буфера**.
2. Вставьте Base64 URL → обновить → Connect.

### Karing
1. Добавьте subscription URL + автообновление.
2. Задайте **логин/пароль inbound (Mixed)** — защита localhost SOCKS.

</details>

<details>
<summary><b>🍎 iOS / iPadOS — Happ / V2Box</b></summary>

1. **Happ** или **V2Box** из App Store.
2. **Configs → ＋ → Add Subscription**.
3. Вставьте Base64 URL → дождитесь загрузки.
4. Выберите сервер → Connect.
5. Обновление: refresh у группы подписки.

</details>

<details>
<summary><b>🖥 Windows / Linux — Throne / v2rayN</b></summary>

### Throne
1. [Throne Releases](https://github.com/throneproj/Throne/releases)
2. **Профили → Добавить из буфера** (Base64 URL).
3. Тест задержки → **TUN** при необходимости → запуск.

### v2rayN
1. Подписка → URL → обновить.
2. Real ping / tcping → сортировка → Enter.

</details>

<details>
<summary><b>💻 macOS — Hiddify / V2Box</b></summary>

1. [Hiddify macOS](https://github.com/hiddify/hiddify-app/releases) или V2Box.
2. Новый профиль из URL/буфера.
3. Обновить → Connect.

</details>

<details>
<summary><b>📺 Android TV — v2rayNG + QR</b></summary>

1. v2rayNG (TV/APK).
2. Импорт QR из `{base_url}qr/`.
3. Проверка задержки → Connect.

</details>

---

## ⚙️ Как это работает

Не «голое» зеркало чужих списков, а **quality pipeline**:

1. **Сбор** — URL + Telegram.  
2. **Fingerprint дедуп** — SHA-256.  
3. **Pre-filter** — синтаксис, private IP, DNS, TCP.  
4. **Xray Phase 1** — HTTP `generate_204` (alive).  
5. **Xray Phase 2** — median RTT, jitter, success rate, DPI (YouTube).  
6. **Phase 3** — speedtest топа.  
7. **Stable Pool** — `data/history.json`, 3 fail подряд → drop.  
8. **Score 100** — Success + Stability + Latency − Jitter − insecure.  
9. **Генерация** — raw / base64 / clash / sing-box / QR + README.

```text
Источники → Parse → TCP → Xray HTTP → Score/History → output/
```

---

## 🗂 Структура репозитория

```text
.github/workflows/     — CI (каждые 2 часа)
configs/               — артефакты → branch output
  base64/              — подписки Base64
  clash/ · sing-box/   — клиентские форматы
  countries/ · protocols/
  whitelists/ · qr/
  stats.json
data/history.json      — Stable Pool
src/services/          — scraper, validator, generator
src/readme_builder.py  — этот README
main.py
urls.txt · tg_channels.txt
```

---

## 🔧 Локальный запуск

```bash
git clone https://github.com/ewecrow78-gif/Free_VPN_Aggregator.git
cd Free_VPN_Aggregator
python -m pip install -r requirements.txt
python main.py
```

Требования: **Python 3.11+**, Windows/Linux.  
Опционально: `TG_API_ID`, `TG_API_HASH`, `TG_SESSION`.

---

<details>
<summary><b>❓ FAQ: Зачем я тестирую конфигурации и какой транспорт лучше? (Нажмите, чтобы узнать)</b></summary>

⚡ **Зачем я вообще тестирую конфигурации?** В самом начале из 40.000+ взятых на пробу бесплатных публичных конфигураций - проверку на работоспособность прошли примерно 700 штук, а это менее 2%, а в итоге тут выложил около 200 самых качественных с высоким откликом и приличной скоростью, а это уже пол процента. Не у каждого есть время разбираться со сборками из десятков тысяч конфигураций, где реально работающих только пару сотен.

⚡ **Протоколы:** Протоколов в сети целый вагон, но самый эффективный, защищающий от DPI Роскомнадзора и его блокировок - это VLESS+Reality из-за способности маскировать трафик под обращение к безобидному HTTPS сайту, делая использование VPN абсолютно невидимым для вашего интернет-провайдера. Остальные протоколы - идут по убывающей в рейтинге, так как легче демаскируются.

⚡ **Транспорт:** Самый стабильный транспорт: XHTTP, GRPC и WS.

⚡ Часть конфигураций со временем могут перестать работать из-за независящих от меня причин, поэтому списки будут периодически обновляться.
</details>

<details>
<summary><b>🛡️ Обход блокировок и DNS-over-HTTPS (DoH) (Нажмите, чтобы узнать)</b></summary>

⚡ Если провайдер блокирует подключение к VPN - попробуйте поменять обычный DNS на своем роутере, ПК или телефоне на шифрованный DNS-over-HTTPS (DoH) или DNS-over-TLS (DoT). Даже если не поможет - просто поставьте себе DoH для вашей же конфиденциальности в сети!

⚡ Во время работы белых списков некоторые иностранные DNS-DoH (Google, например) иногда могут быть недоступны. Сначала я бы проверил работу Cloudflare, OpenDNS, Google, Quad9, AdGuard, Dnsforge, и если ни один не работает, то выбрал бы Яндекс DoH. Если вообще никакой DoH не заводится - отключите и используйте автоматический провайдерский.

🧾 **Что такое и как подключить DNS-over-HTTPS (DoH)?**
- **НА РОУТЕРЕ**: удалите и отключите дефолтный провайдерский DNS и поставьте DNS-over-HTTPS (DoH), сначала потребуется скачать DoH-клиент в настройках обновления роутера. Можно поставить и DNS-over-TLS (DoT), но его не советуют в России из-за частых блокировок. DNS-over-HTTPS (DoH) должен работать 100% стабильно.
- **НА ТЕЛЕФОНЕ**: скачайте приложение "Cloudflare 1.1.1.1 + WARP" (Android/iOS). Для iOS можно скачать профиль конфигурации с официальных сайтов Quad9, AdGuard. Для Android: Настройки ➡️ Сеть и интернет ➡️ Расширенные настройки ➡️ Персональный DNS-сервер и введите хост из списка ниже.
- **НА ПК**: пропишите DoH-сервер в настройках DNS сетевого адаптера или в самом браузере.
- **В ПРИЛОЖЕНИИ VPN**: пропишите DoH-сервер в настройках DNS приложения.

**DNS-over-HTTPS (DoH)** - шифрует DNS‑запросы от локальных наблюдателей (провайдера), повышая приватность. Провайдер видит только соединение с IP‑адресом резолвера DoH + конечный IP целевого сервера.
</details>

<details>
<summary><b>🧾 Список публичных DoH-серверов (Нажмите, чтобы посмотреть список)</b></summary>

- `https://common.dot.dns.yandex.net/dns-query` - Яндекс DNS Базовый (только если другие не работают)
- `https://safe.dot.dns.yandex.net/dns-query` - Яндекс DNS Безопасный
- `https://dns.adguard-dns.com/dns-query` - AdGuard DNS (блокировщик рекламы)
- `https://dns.quad9.net/dns-query` - Quad9 DNS (Malware Blocking)
- `https://dnsforge.de/dns-query` - DNSFORGE (без логов, сервера в Германии)
- `https://dns.cloudflare.com/dns-query` - Cloudflare DNS Базовый
- `https://security.cloudflare-dns.com/dns-query` - Cloudflare DNS Malware Protection
- `https://dns.google/dns-query` - Google Public DNS
- `https://doh.opendns.com/dns-query` - Cisco Umbrella (OpenDNS)
</details>

---

## ⚠️ Безопасность

> [!CAUTION]
> **Бесплатные публичные VPN могут быть опасны.**
> - Не используйте для банков, Госуслуг, крипты, почты без HTTPS.
> - Админ узла теоретически видит незашифрованный трафик.
> - `allowInsecure=1` → отдельный risky-список + штраф в score.
> - На Android с RU-приложениями задайте **логин/пароль локального inbound** (Karing / v2rayNG / Happ).
> - Проект educational / anti-censorship, AS IS, без гарантий.

---

## 📊 Статистика

<details>
<summary><b>🌍 По странам</b></summary>

| Страна | Кол-во | Флаг | Подписки |
| :--- | :---: | :---: | :--- |
{countries_table}

</details>

<details>
<summary><b>🔌 По протоколам</b></summary>

| Протокол | Кол-во | Доля |
| :--- | :---: | :---: |
{protocols_table}

</details>

---

## 📜 Лицензия

MIT — см. [LICENSE](LICENSE).

---

<div align="center">

**⭐ Если проект полезен — поставьте Star**

<sub>Generated automatically by Free VPN Aggregator Pro · {update_time} UTC</sub>

</div>
"""


def build_readme():
    try:
        with open(STATS_FILE, "r", encoding="utf-8") as f:
            stats = json.load(f)
    except Exception as e:
        logger.error(f"[Readme] Stats file not found or corrupted: {e}")
        return

    update_time = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M")
    base_url = RAW_GH + "/"
    funnel = stats.get("funnel", {})
    total = stats.get("total", 0)

    cards = {
        "card_recommended": sub_card(
            "🥇 RECOMMENDED — лучший старт",
            "recommended",
            "Сбалансированный список: success rate, stable pool, DPI-bypass. Идеально новичкам.",
            badge="⚫",
            count_hint=str(stats.get("recommended", "~")),
            raw_rel="recommended.txt",
        ),
        "card_top_fast": sub_card(
            "🚀 TOP FAST — минимальный пинг",
            "top_fast",
            "Топ узлов с наименьшей latency после Xray HTTP-теста.",
            badge="⚫",
            raw_rel="top_fast.txt",
        ),
        "card_alive": sub_card(
            "✅ ALIVE — все прошедшие Xray",
            "alive",
            "Полный рабочий пул (с лимитом выдачи). Больше выбор — дольше пинг-тест на слабых телефонах.",
            badge="⚫",
            count_hint=str(total),
            raw_rel="alive.txt",
        ),
        "card_ru_mobile_wl": sub_card(
            "📱 RU MOBILE WHITELIST",
            "ru_mobile_whitelist",
            "Обход ограничений мобильных операторов / whitelist. Лёгкий набор для телефона.",
            badge="⚪",
            raw_rel="ru_mobile_whitelist.txt",
        ),
        "card_wl_all": sub_card(
            "WHITE LIST ALL",
            "whitelist_all",
            "Расширенный whitelist-пул (clean IP / RU-reachable).",
            badge="⚪",
            count_hint=str(stats.get("whitelists", "~")),
            raw_rel="whitelists/all.txt",
        ),
        "card_wl_small": sub_card(
            "WHITE LIST SMALL — жёстче фильтр",
            "whitelist_small",
            "Меньше узлов, выше требования к пингу / success / jitter.",
            badge="⚪",
            count_hint=str(stats.get("whitelist_small", "~")),
            raw_rel="whitelists/small.txt",
        ),
        "card_wl_premium": sub_card(
            "💎 WHITE LIST PREMIUM",
            "whitelist_premium",
            "Самый жёсткий отбор: низкий пинг, высокий success, speed-test. Узлов мало — зато качество.",
            badge="⚪",
            count_hint=str(stats.get("whitelist_premium", funnel.get("premium", "~"))),
            raw_rel="whitelists/premium.txt",
        ),
        "card_sni": sub_card(
            "🔒 SNI / CIDR BYPASS",
            "sni_cidr_bypass",
            "Конфиги с TLS/Reality и SNI — обход SNI/CIDR ограничений.",
            badge="⚪",
            raw_rel="sni_cidr_bypass.txt",
        ),
        "card_top150": sub_card(
            "TOP-150 MOBILE",
            "top_150_mobile",
            "До 150 лёгких узлов (VLESS/Trojan/SS). Не перегружает смартфон.",
            badge="📱",
            raw_rel="top_150_mobile.txt",
        ),
        "card_mobile": sub_card(
            "MOBILE",
            "mobile",
            "Мобильный профиль: лёгкие протоколы, лимит по странам.",
            badge="📱",
            count_hint=str(stats.get("mobile", "~")),
            raw_rel="mobile.txt",
        ),
        "card_happ": sub_card(
            "Happ / Incy profile",
            "happ",
            "Укороченный набор под Happ/Incy и похожие клиенты.",
            badge="📱",
            raw_rel="apps/happ.txt",
        ),
        "card_insecure": sub_card(
            "ALLOW INSECURE (risky)",
            "allow_insecure",
            "Конфиги с allowInsecure. Только если понимаете риск. Не для банков и личных кабинетов.",
            badge="⚠️",
            raw_rel="risky/allow_insecure.txt",
        ),
    }

    country_rows = []
    sorted_countries = sorted(
        stats.get("by_country", {}).items(), key=lambda x: x[1], reverse=True
    )
    country_flags = stats.get("country_flags", {})
    for c_name, count in sorted_countries:
        flag = country_flags.get(c_name, "🏳️")
        safe = c_name.lower().replace(" ", "_")
        links = (
            f"[Base64]({base_url}base64/country_{safe}.txt) \\| "
            f"[Raw]({base_url}countries/{safe}.txt) \\| "
            f"[Clash]({base_url}clash/country_{safe}.yaml) \\| "
            f"[Sing-Box]({base_url}sing-box/country_{safe}.json)"
        )
        country_rows.append(f"| {c_name.title()} | {count} | {flag} | {links} |")
    countries_table = "\n".join(country_rows) if country_rows else "| - | 0 | 🏳️ | - |"

    proto_rows = []
    sorted_protos = sorted(
        stats.get("by_protocol", {}).items(), key=lambda x: x[1], reverse=True
    )
    total_protos = sum(stats.get("by_protocol", {}).values()) or 1
    for proto, count in sorted_protos:
        pct = round((count / total_protos) * 100, 1)
        proto_rows.append(f"| {proto.upper()} | {count} | {pct}% |")
    protocols_table = "\n".join(proto_rows) if proto_rows else "| - | 0 | 0% |"

    readme_content = README_TEMPLATE.format(
        base_url=base_url,
        jsdelivr=JSDELIVR,
        githack=GITHACK,
        fastly=FASTLY,
        update_time=update_time,
        downloaded_lines=funnel.get("downloaded_lines", 0),
        parsed_configs=funnel.get("parsed_configs", 0),
        rejected_syntax=funnel.get("rejected_syntax", 0) + funnel.get("private_ip", 0),
        rejected_dns=funnel.get("rejected_dns", 0) + funnel.get("rejected_tcp", 0),
        xray_alive=funnel.get("xray_alive", 0),
        premium=funnel.get("premium", stats.get("whitelist_premium", 0)),
        total=total,
        whitelists=stats.get("whitelists", 0),
        recommended=stats.get("recommended", 0),
        mobile=stats.get("mobile", 0),
        countries_table=countries_table,
        protocols_table=protocols_table,
        **cards,
    )

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(readme_content.strip() + "\n")
    logger.info("[Readme] Goida/igareck-style README.md compiled successfully.")
