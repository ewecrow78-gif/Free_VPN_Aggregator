<div align="center">

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
| 🥇 **Не знаю, что выбрать** | [recommended](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/recommended.txt) | Стабильность + score + DPI |
| 📱 **Телефон** | [top_150_mobile](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/top_150_mobile.txt) | Лёгкий список |
| 🚀 **Минимальный пинг** | [top_fast](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/top_fast.txt) | Топ по latency |
| ⚪ **Белые списки у оператора** | [ru_mobile_whitelist](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/ru_mobile_whitelist.txt) | Whitelist bypass |
| 🔒 **SNI/CIDR** | [sni_cidr_bypass](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/sni_cidr_bypass.txt) | TLS + SNI |
| 💎 **Максимум качества** | [whitelist_premium](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/whitelist_premium.txt) | Жёсткий отбор |

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

> Автообновление пайплайном. Время: **2026-08-01 08:33 UTC**.

| Показатель | Значение | Описание |
| :--- | :---: | :--- |
| **Собрано ссылок** | `0` | Сырые строки из источников |
| **Уникальных конфигов** | `0` | После парсинга / дедупа |
| **Отсеяно (синтаксис / IP)** | `0` | Битый URI, private IP |
| **Отсеяно (DNS / TCP)** | `0` | Мёртвые домены / порты |
| **Рабочих (Xray test)** | `0` | Реальный HTTP через VPN |
| **В выдаче (top)** | `69` | Лимит клиентских подписок |
| **Whitelist** | `0` | White-list сценарий |
| **Premium** | `0` | Жёсткий отбор |
| **Recommended** | `0` | Для новичков |
| **Mobile** | `0` | Лёгкие протоколы |

---

## 📋 Подписки

> [!TIP]
> Для клиентов почти всегда берите **Base64**.  
> Если `raw.githubusercontent.com` не открывается — [🪞 Зеркала](#-зеркала).

### ⚫ Обычный режим (чёрные списки)

*Обычный интернет без жёсткого whitelist у провайдера.*

### 🥇 RECOMMENDED — лучший старт ⚫ (0)

### [base64/recommended.txt](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/recommended.txt)

<details>
<summary>QR-код</summary>

![qr-recommended](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/qr/recommended.png)

</details>

`Сбалансированный список: success rate, stable pool, DPI-bypass. Идеально новичкам.`

<details>
<summary>🪞 Зеркала и другие форматы</summary>

**Base64 (рекомендуется):**
- **GitHub RAW:** `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/recommended.txt`
- **jsDelivr:** `https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/recommended.txt`
- **GitHack:** `https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/recommended.txt`
- **Fastly:** `https://fastly.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/recommended.txt`

**Raw TXT:**
- **GitHub RAW:** `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/recommended.txt`
- **jsDelivr:** `https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/recommended.txt`
- **GitHack:** `https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/recommended.txt`
- **Fastly:** `https://fastly.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/recommended.txt`

| Формат | Ссылка |
| :--- | :--- |
| Base64 | [open](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/recommended.txt) |
| Raw | [open](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/recommended.txt) |
| Clash | [yaml](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/recommended.yaml) |
| Sing-Box | [json](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/recommended.json) |
| QR | [png](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/qr/recommended.png) |

</details>

---

### 🚀 TOP FAST — минимальный пинг ⚫

### [base64/top_fast.txt](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/top_fast.txt)

<details>
<summary>QR-код</summary>

![qr-top_fast](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/qr/top_fast.png)

</details>

`Топ узлов с наименьшей latency после Xray HTTP-теста.`

<details>
<summary>🪞 Зеркала и другие форматы</summary>

**Base64 (рекомендуется):**
- **GitHub RAW:** `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/top_fast.txt`
- **jsDelivr:** `https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/top_fast.txt`
- **GitHack:** `https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/top_fast.txt`
- **Fastly:** `https://fastly.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/top_fast.txt`

**Raw TXT:**
- **GitHub RAW:** `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/top_fast.txt`
- **jsDelivr:** `https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/top_fast.txt`
- **GitHack:** `https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/top_fast.txt`
- **Fastly:** `https://fastly.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/top_fast.txt`

| Формат | Ссылка |
| :--- | :--- |
| Base64 | [open](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/top_fast.txt) |
| Raw | [open](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/top_fast.txt) |
| Clash | [yaml](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/top_fast.yaml) |
| Sing-Box | [json](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/top_fast.json) |
| QR | [png](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/qr/top_fast.png) |

</details>

---

### ✅ ALIVE — все прошедшие Xray ⚫ (69)

### [base64/alive.txt](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/alive.txt)

<details>
<summary>QR-код</summary>

![qr-alive](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/qr/alive.png)

</details>

`Полный рабочий пул (с лимитом выдачи). Больше выбор — дольше пинг-тест на слабых телефонах.`

<details>
<summary>🪞 Зеркала и другие форматы</summary>

**Base64 (рекомендуется):**
- **GitHub RAW:** `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/alive.txt`
- **jsDelivr:** `https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/alive.txt`
- **GitHack:** `https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/alive.txt`
- **Fastly:** `https://fastly.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/alive.txt`

**Raw TXT:**
- **GitHub RAW:** `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/alive.txt`
- **jsDelivr:** `https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/alive.txt`
- **GitHack:** `https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/alive.txt`
- **Fastly:** `https://fastly.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/alive.txt`

| Формат | Ссылка |
| :--- | :--- |
| Base64 | [open](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/alive.txt) |
| Raw | [open](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/alive.txt) |
| Clash | [yaml](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/alive.yaml) |
| Sing-Box | [json](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/alive.json) |
| QR | [png](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/qr/alive.png) |

</details>

---


### ⚪ Обход белых списков

*Когда «режут» всё, кроме белых IP/SNI.*

### 📱 RU MOBILE WHITELIST ⚪

### [base64/ru_mobile_whitelist.txt](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/ru_mobile_whitelist.txt)

<details>
<summary>QR-код</summary>

![qr-ru_mobile_whitelist](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/qr/ru_mobile_whitelist.png)

</details>

`Обход ограничений мобильных операторов / whitelist. Лёгкий набор для телефона.`

<details>
<summary>🪞 Зеркала и другие форматы</summary>

**Base64 (рекомендуется):**
- **GitHub RAW:** `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/ru_mobile_whitelist.txt`
- **jsDelivr:** `https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/ru_mobile_whitelist.txt`
- **GitHack:** `https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/ru_mobile_whitelist.txt`
- **Fastly:** `https://fastly.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/ru_mobile_whitelist.txt`

**Raw TXT:**
- **GitHub RAW:** `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/ru_mobile_whitelist.txt`
- **jsDelivr:** `https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/ru_mobile_whitelist.txt`
- **GitHack:** `https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/ru_mobile_whitelist.txt`
- **Fastly:** `https://fastly.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/ru_mobile_whitelist.txt`

| Формат | Ссылка |
| :--- | :--- |
| Base64 | [open](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/ru_mobile_whitelist.txt) |
| Raw | [open](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/ru_mobile_whitelist.txt) |
| Clash | [yaml](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/ru_mobile_whitelist.yaml) |
| Sing-Box | [json](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/ru_mobile_whitelist.json) |
| QR | [png](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/qr/ru_mobile_whitelist.png) |

</details>

---

### WHITE LIST ALL ⚪ (~)

### [base64/whitelist_all.txt](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/whitelist_all.txt)

<details>
<summary>QR-код</summary>

![qr-whitelist_all](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/qr/whitelist_all.png)

</details>

`Расширенный whitelist-пул (clean IP / RU-reachable).`

<details>
<summary>🪞 Зеркала и другие форматы</summary>

**Base64 (рекомендуется):**
- **GitHub RAW:** `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/whitelist_all.txt`
- **jsDelivr:** `https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/whitelist_all.txt`
- **GitHack:** `https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/whitelist_all.txt`
- **Fastly:** `https://fastly.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/whitelist_all.txt`

**Raw TXT:**
- **GitHub RAW:** `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/whitelists/all.txt`
- **jsDelivr:** `https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/whitelists/all.txt`
- **GitHack:** `https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/whitelists/all.txt`
- **Fastly:** `https://fastly.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/whitelists/all.txt`

| Формат | Ссылка |
| :--- | :--- |
| Base64 | [open](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/whitelist_all.txt) |
| Raw | [open](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/whitelists/all.txt) |
| Clash | [yaml](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/whitelist_all.yaml) |
| Sing-Box | [json](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/whitelist_all.json) |
| QR | [png](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/qr/whitelist_all.png) |

</details>

---

### WHITE LIST SMALL — жёстче фильтр ⚪ (~)

### [base64/whitelist_small.txt](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/whitelist_small.txt)

<details>
<summary>QR-код</summary>

![qr-whitelist_small](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/qr/whitelist_small.png)

</details>

`Меньше узлов, выше требования к пингу / success / jitter.`

<details>
<summary>🪞 Зеркала и другие форматы</summary>

**Base64 (рекомендуется):**
- **GitHub RAW:** `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/whitelist_small.txt`
- **jsDelivr:** `https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/whitelist_small.txt`
- **GitHack:** `https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/whitelist_small.txt`
- **Fastly:** `https://fastly.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/whitelist_small.txt`

**Raw TXT:**
- **GitHub RAW:** `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/whitelists/small.txt`
- **jsDelivr:** `https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/whitelists/small.txt`
- **GitHack:** `https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/whitelists/small.txt`
- **Fastly:** `https://fastly.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/whitelists/small.txt`

| Формат | Ссылка |
| :--- | :--- |
| Base64 | [open](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/whitelist_small.txt) |
| Raw | [open](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/whitelists/small.txt) |
| Clash | [yaml](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/whitelist_small.yaml) |
| Sing-Box | [json](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/whitelist_small.json) |
| QR | [png](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/qr/whitelist_small.png) |

</details>

---

### 💎 WHITE LIST PREMIUM ⚪ (~)

### [base64/whitelist_premium.txt](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/whitelist_premium.txt)

<details>
<summary>QR-код</summary>

![qr-whitelist_premium](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/qr/whitelist_premium.png)

</details>

`Самый жёсткий отбор: низкий пинг, высокий success, speed-test. Узлов мало — зато качество.`

<details>
<summary>🪞 Зеркала и другие форматы</summary>

**Base64 (рекомендуется):**
- **GitHub RAW:** `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/whitelist_premium.txt`
- **jsDelivr:** `https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/whitelist_premium.txt`
- **GitHack:** `https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/whitelist_premium.txt`
- **Fastly:** `https://fastly.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/whitelist_premium.txt`

**Raw TXT:**
- **GitHub RAW:** `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/whitelists/premium.txt`
- **jsDelivr:** `https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/whitelists/premium.txt`
- **GitHack:** `https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/whitelists/premium.txt`
- **Fastly:** `https://fastly.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/whitelists/premium.txt`

| Формат | Ссылка |
| :--- | :--- |
| Base64 | [open](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/whitelist_premium.txt) |
| Raw | [open](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/whitelists/premium.txt) |
| Clash | [yaml](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/whitelist_premium.yaml) |
| Sing-Box | [json](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/whitelist_premium.json) |
| QR | [png](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/qr/whitelist_premium.png) |

</details>

---

### 🔒 SNI / CIDR BYPASS ⚪

### [base64/sni_cidr_bypass.txt](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/sni_cidr_bypass.txt)

<details>
<summary>QR-код</summary>

![qr-sni_cidr_bypass](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/qr/sni_cidr_bypass.png)

</details>

`Конфиги с TLS/Reality и SNI — обход SNI/CIDR ограничений.`

<details>
<summary>🪞 Зеркала и другие форматы</summary>

**Base64 (рекомендуется):**
- **GitHub RAW:** `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/sni_cidr_bypass.txt`
- **jsDelivr:** `https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/sni_cidr_bypass.txt`
- **GitHack:** `https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/sni_cidr_bypass.txt`
- **Fastly:** `https://fastly.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/sni_cidr_bypass.txt`

**Raw TXT:**
- **GitHub RAW:** `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sni_cidr_bypass.txt`
- **jsDelivr:** `https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/sni_cidr_bypass.txt`
- **GitHack:** `https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sni_cidr_bypass.txt`
- **Fastly:** `https://fastly.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/sni_cidr_bypass.txt`

| Формат | Ссылка |
| :--- | :--- |
| Base64 | [open](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/sni_cidr_bypass.txt) |
| Raw | [open](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sni_cidr_bypass.txt) |
| Clash | [yaml](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/sni_cidr_bypass.yaml) |
| Sing-Box | [json](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/sni_cidr_bypass.json) |
| QR | [png](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/qr/sni_cidr_bypass.png) |

</details>

---


### 📱 Мобильные / лёгкие

*Меньше узлов = быстрее импорт и пинг-тест на телефоне.*

### TOP-150 MOBILE 📱

### [base64/top_150_mobile.txt](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/top_150_mobile.txt)

<details>
<summary>QR-код</summary>

![qr-top_150_mobile](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/qr/top_150_mobile.png)

</details>

`До 150 лёгких узлов (VLESS/Trojan/SS). Не перегружает смартфон.`

<details>
<summary>🪞 Зеркала и другие форматы</summary>

**Base64 (рекомендуется):**
- **GitHub RAW:** `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/top_150_mobile.txt`
- **jsDelivr:** `https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/top_150_mobile.txt`
- **GitHack:** `https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/top_150_mobile.txt`
- **Fastly:** `https://fastly.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/top_150_mobile.txt`

**Raw TXT:**
- **GitHub RAW:** `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/top_150_mobile.txt`
- **jsDelivr:** `https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/top_150_mobile.txt`
- **GitHack:** `https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/top_150_mobile.txt`
- **Fastly:** `https://fastly.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/top_150_mobile.txt`

| Формат | Ссылка |
| :--- | :--- |
| Base64 | [open](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/top_150_mobile.txt) |
| Raw | [open](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/top_150_mobile.txt) |
| Clash | [yaml](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/top_150_mobile.yaml) |
| Sing-Box | [json](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/top_150_mobile.json) |
| QR | [png](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/qr/top_150_mobile.png) |

</details>

---

### MOBILE 📱 (~)

### [base64/mobile.txt](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/mobile.txt)

<details>
<summary>QR-код</summary>

![qr-mobile](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/qr/mobile.png)

</details>

`Мобильный профиль: лёгкие протоколы, лимит по странам.`

<details>
<summary>🪞 Зеркала и другие форматы</summary>

**Base64 (рекомендуется):**
- **GitHub RAW:** `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/mobile.txt`
- **jsDelivr:** `https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/mobile.txt`
- **GitHack:** `https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/mobile.txt`
- **Fastly:** `https://fastly.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/mobile.txt`

**Raw TXT:**
- **GitHub RAW:** `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/mobile.txt`
- **jsDelivr:** `https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/mobile.txt`
- **GitHack:** `https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/mobile.txt`
- **Fastly:** `https://fastly.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/mobile.txt`

| Формат | Ссылка |
| :--- | :--- |
| Base64 | [open](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/mobile.txt) |
| Raw | [open](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/mobile.txt) |
| Clash | [yaml](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/mobile.yaml) |
| Sing-Box | [json](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/mobile.json) |
| QR | [png](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/qr/mobile.png) |

</details>

---

### Happ / Incy profile 📱

### [base64/happ.txt](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/happ.txt)

<details>
<summary>QR-код</summary>

![qr-happ](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/qr/happ.png)

</details>

`Укороченный набор под Happ/Incy и похожие клиенты.`

<details>
<summary>🪞 Зеркала и другие форматы</summary>

**Base64 (рекомендуется):**
- **GitHub RAW:** `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/happ.txt`
- **jsDelivr:** `https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/happ.txt`
- **GitHack:** `https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/happ.txt`
- **Fastly:** `https://fastly.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/happ.txt`

**Raw TXT:**
- **GitHub RAW:** `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/apps/happ.txt`
- **jsDelivr:** `https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/apps/happ.txt`
- **GitHack:** `https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/apps/happ.txt`
- **Fastly:** `https://fastly.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/apps/happ.txt`

| Формат | Ссылка |
| :--- | :--- |
| Base64 | [open](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/happ.txt) |
| Raw | [open](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/apps/happ.txt) |
| Clash | [yaml](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/happ.yaml) |
| Sing-Box | [json](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/happ.json) |
| QR | [png](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/qr/happ.png) |

</details>

---


### ⚠️ Risky

### ALLOW INSECURE (risky) ⚠️

### [base64/allow_insecure.txt](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/allow_insecure.txt)

<details>
<summary>QR-код</summary>

![qr-allow_insecure](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/qr/allow_insecure.png)

</details>

`Конфиги с allowInsecure. Только если понимаете риск. Не для банков и личных кабинетов.`

<details>
<summary>🪞 Зеркала и другие форматы</summary>

**Base64 (рекомендуется):**
- **GitHub RAW:** `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/allow_insecure.txt`
- **jsDelivr:** `https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/allow_insecure.txt`
- **GitHack:** `https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/allow_insecure.txt`
- **Fastly:** `https://fastly.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/allow_insecure.txt`

**Raw TXT:**
- **GitHub RAW:** `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/risky/allow_insecure.txt`
- **jsDelivr:** `https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/risky/allow_insecure.txt`
- **GitHack:** `https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/risky/allow_insecure.txt`
- **Fastly:** `https://fastly.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/risky/allow_insecure.txt`

| Формат | Ссылка |
| :--- | :--- |
| Base64 | [open](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/allow_insecure.txt) |
| Raw | [open](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/risky/allow_insecure.txt) |
| Clash | [yaml](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/allow_insecure.yaml) |
| Sing-Box | [json](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/allow_insecure.json) |
| QR | [png](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/qr/allow_insecure.png) |

</details>

---


---

### 📦 Полный список ссылок для клиента

<details>
<summary><b>📋 Раскрыть все Base64 URL (копировать в клиент)</b></summary>

> Рекомендуемые: **[recommended](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/recommended.txt)**, **[top_fast](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/top_fast.txt)**, **[top_150_mobile](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/top_150_mobile.txt)**, **[ru_mobile_whitelist](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/ru_mobile_whitelist.txt)**, **[sni_cidr_bypass](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/sni_cidr_bypass.txt)**.

- [x] **Вечно актуальные (ветка output)**

1) `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/recommended.txt`
2) `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/top_fast.txt`
3) `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/alive.txt`
4) `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/mobile.txt`
5) `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/top_150_mobile.txt`
6) `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/ru_mobile_whitelist.txt`
7) `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/whitelist_all.txt`
8) `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/whitelist_small.txt`
9) `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/whitelist_premium.txt`
10) `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/sni_cidr_bypass.txt`
11) `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/happ.txt`
12) `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/incy.txt`
13) `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/allow_insecure.txt`

🔗 QR: `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/qr/` (например `recommended.png`)

</details>

---

## 🪞 Зеркала

> **Сохраните зеркала** на случай сбоев GitHub RAW.

| Зеркало | Правило | Пример (recommended) |
| :--- | :--- | :--- |
| **GitHub RAW** | основное | `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/recommended.txt` |
| **jsDelivr** | CDN | `https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/recommended.txt` |
| **Fastly jsDelivr** | CDN | `https://fastly.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/recommended.txt` |
| **GitHack** | live proxy | `https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/recommended.txt` |

<details>
<summary><b>Готовые зеркала recommended / top_fast / whitelist / sni</b></summary>

#### recommended
```
https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/recommended.txt
https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/recommended.txt
https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/recommended.txt
https://fastly.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/recommended.txt
```

#### top_fast
```
https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/top_fast.txt
https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/top_fast.txt
https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/top_fast.txt
```

#### ru_mobile_whitelist
```
https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/ru_mobile_whitelist.txt
https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/ru_mobile_whitelist.txt
https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/ru_mobile_whitelist.txt
```

#### sni_cidr_bypass
```
https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/sni_cidr_bypass.txt
https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/sni_cidr_bypass.txt
https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/sni_cidr_bypass.txt
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
2. URL: `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/happ.txt` или `recommended.txt`.
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
2. Импорт QR из `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/qr/`.
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
| The Netherlands | 11 | 🇳🇱 | [Base64](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/country_the_netherlands.txt) \| [Raw](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/countries/the_netherlands.txt) \| [Clash](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/country_the_netherlands.yaml) \| [Sing-Box](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/country_the_netherlands.json) |
| Russia | 10 | 🇷🇺 | [Base64](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/country_russia.txt) \| [Raw](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/countries/russia.txt) \| [Clash](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/country_russia.yaml) \| [Sing-Box](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/country_russia.json) |
| Italy | 9 | 🇮🇹 | [Base64](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/country_italy.txt) \| [Raw](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/countries/italy.txt) \| [Clash](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/country_italy.yaml) \| [Sing-Box](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/country_italy.json) |
| Germany | 8 | 🇩🇪 | [Base64](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/country_germany.txt) \| [Raw](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/countries/germany.txt) \| [Clash](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/country_germany.yaml) \| [Sing-Box](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/country_germany.json) |
| France | 3 | 🇫🇷 | [Base64](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/country_france.txt) \| [Raw](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/countries/france.txt) \| [Clash](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/country_france.yaml) \| [Sing-Box](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/country_france.json) |
| Bulgaria | 3 | 🏳️ | [Base64](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/country_bulgaria.txt) \| [Raw](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/countries/bulgaria.txt) \| [Clash](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/country_bulgaria.yaml) \| [Sing-Box](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/country_bulgaria.json) |
| Sweden | 2 | 🇸🇪 | [Base64](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/country_sweden.txt) \| [Raw](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/countries/sweden.txt) \| [Clash](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/country_sweden.yaml) \| [Sing-Box](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/country_sweden.json) |
| Lithuania | 2 | 🏳️ | [Base64](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/country_lithuania.txt) \| [Raw](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/countries/lithuania.txt) \| [Clash](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/country_lithuania.yaml) \| [Sing-Box](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/country_lithuania.json) |
| United States | 2 | 🇺🇸 | [Base64](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/country_united_states.txt) \| [Raw](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/countries/united_states.txt) \| [Clash](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/country_united_states.yaml) \| [Sing-Box](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/country_united_states.json) |
| Seychelles | 2 | 🏳️ | [Base64](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/country_seychelles.txt) \| [Raw](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/countries/seychelles.txt) \| [Clash](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/country_seychelles.yaml) \| [Sing-Box](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/country_seychelles.json) |
| Austria | 2 | 🏳️ | [Base64](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/country_austria.txt) \| [Raw](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/countries/austria.txt) \| [Clash](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/country_austria.yaml) \| [Sing-Box](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/country_austria.json) |
| Colombia | 2 | 🏳️ | [Base64](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/country_colombia.txt) \| [Raw](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/countries/colombia.txt) \| [Clash](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/country_colombia.yaml) \| [Sing-Box](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/country_colombia.json) |
| United Arab Emirates | 1 | 🇦🇪 | [Base64](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/country_united_arab_emirates.txt) \| [Raw](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/countries/united_arab_emirates.txt) \| [Clash](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/country_united_arab_emirates.yaml) \| [Sing-Box](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/country_united_arab_emirates.json) |
| Poland | 1 | 🇵🇱 | [Base64](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/country_poland.txt) \| [Raw](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/countries/poland.txt) \| [Clash](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/country_poland.yaml) \| [Sing-Box](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/country_poland.json) |
| Spain | 1 | 🇪🇸 | [Base64](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/country_spain.txt) \| [Raw](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/countries/spain.txt) \| [Clash](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/country_spain.yaml) \| [Sing-Box](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/country_spain.json) |
| India | 1 | 🇮🇳 | [Base64](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/country_india.txt) \| [Raw](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/countries/india.txt) \| [Clash](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/country_india.yaml) \| [Sing-Box](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/country_india.json) |
| Malaysia | 1 | 🏳️ | [Base64](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/country_malaysia.txt) \| [Raw](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/countries/malaysia.txt) \| [Clash](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/country_malaysia.yaml) \| [Sing-Box](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/country_malaysia.json) |
| Thailand | 1 | 🏳️ | [Base64](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/country_thailand.txt) \| [Raw](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/countries/thailand.txt) \| [Clash](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/country_thailand.yaml) \| [Sing-Box](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/country_thailand.json) |
| United Kingdom | 1 | 🇬🇧 | [Base64](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/country_united_kingdom.txt) \| [Raw](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/countries/united_kingdom.txt) \| [Clash](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/country_united_kingdom.yaml) \| [Sing-Box](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/country_united_kingdom.json) |
| Taiwan | 1 | 🇹🇼 | [Base64](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/country_taiwan.txt) \| [Raw](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/countries/taiwan.txt) \| [Clash](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/country_taiwan.yaml) \| [Sing-Box](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/country_taiwan.json) |
| Hong Kong | 1 | 🇭🇰 | [Base64](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/country_hong_kong.txt) \| [Raw](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/countries/hong_kong.txt) \| [Clash](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/country_hong_kong.yaml) \| [Sing-Box](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/country_hong_kong.json) |
| Singapore | 1 | 🇸🇬 | [Base64](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/country_singapore.txt) \| [Raw](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/countries/singapore.txt) \| [Clash](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/country_singapore.yaml) \| [Sing-Box](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/country_singapore.json) |
| Japan | 1 | 🇯🇵 | [Base64](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/country_japan.txt) \| [Raw](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/countries/japan.txt) \| [Clash](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/country_japan.yaml) \| [Sing-Box](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/country_japan.json) |

</details>

<details>
<summary><b>🔌 По протоколам</b></summary>

| Протокол | Кол-во | Доля |
| :--- | :---: | :---: |
| VLESS | 53 | 79.1% |
| SS | 9 | 13.4% |
| TROJAN | 3 | 4.5% |
| VMESS | 2 | 3.0% |

</details>

---

## 📜 Лицензия

MIT — см. [LICENSE](LICENSE).

---

<div align="center">

**⭐ Если проект полезен — поставьте Star**

<sub>Generated automatically by Free VPN Aggregator Pro · 2026-08-01 08:33 UTC</sub>

</div>
