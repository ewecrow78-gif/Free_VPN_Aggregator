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

[🌐 Репозиторий](https://github.com/ewecrow78-gif/Free_VPN_Aggregator) · [📦 Ветка output](https://github.com/ewecrow78-gif/Free_VPN_Aggregator/tree/main/configs)

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
- [➕ Как добавить свой источник](#-как-добавить-свой-источник-конфигов)
- [🛠 Troubleshooting (для разработчиков)](#-troubleshooting-для-разработчиков)
- [⚠️ Безопасность и Disclaimer](#️-безопасность-и-disclaimer)
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

> Автообновление пайплайном. Время: **2026-08-11 18:14 UTC**.

| Показатель | Значение | Описание |
| :--- | :---: | :--- |
| **Собрано ссылок** | `0` | Сырые строки из источников |
| **Уникальных конфигов** | `0` | После парсинга / дедупа |
| **Отсеяно (синтаксис / IP)** | `0` | Битый URI, private IP |
| **Отсеяно (DNS / TCP)** | `0` | Мёртвые домены / порты |
| **Рабочих (Xray test)** | `0` | Реальный HTTP через VPN |
| **Топ 50 быстрых** | `39` | |
| **Топ 30 быстрых** | `30` | |
| **Все конфиги** | `39` | Без лимитов |
| **Белые списки 100** | `0` | |
| **Топ 50 белых списков** | `0` | |
| **Топ 30 белых списков** | `0` | |
| **Все вместе** | `39` | 50 обычных + 50 белых |
| **Все белые списки** | `0` | Без лимитов |
| **Топ быстрых 100** | `39` | Обычные и белые |

---

## 📋 Подписки

> [!TIP]
> Для клиентов почти всегда берите **Base64**.  
> Если `raw.githubusercontent.com` не открывается — [🪞 Зеркала](#-зеркала).

### 1. 🌍 По странам
*(Подписки для каждой страны находятся ниже в разделе «Страны»)*

### 2. Топ 50 быстрых
### 🚀 ТОП 50 БЫСТРЫХ ⚫ (39)

### [base64/top_50_fast.txt](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/top_50_fast.txt)

<details>
<summary>QR-код</summary>

![qr-top_50_fast](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/qr/top_50_fast.png)

</details>

`50 лучших обычных конфигов (не белые списки) с самым низким пингом.`

<details>
<summary>🪞 Зеркала и другие форматы</summary>

**Base64 (рекомендуется):**
- **GitHub RAW:** `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/top_50_fast.txt`
- **jsDelivr:** `https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/top_50_fast.txt`
- **GitHack:** `https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/top_50_fast.txt`
- **Fastly:** `https://fastly.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/top_50_fast.txt`

**Raw TXT:**
- **GitHub RAW:** `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/top_50_fast.txt`
- **jsDelivr:** `https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/top_50_fast.txt`
- **GitHack:** `https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/top_50_fast.txt`
- **Fastly:** `https://fastly.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/top_50_fast.txt`

| Формат | Ссылка |
| :--- | :--- |
| Base64 | [open](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/top_50_fast.txt) |
| Raw | [open](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/top_50_fast.txt) |
| Clash | [yaml](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/top_50_fast.yaml) |
| Sing-Box | [json](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/top_50_fast.json) |
| QR | [png](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/qr/top_50_fast.png) |

</details>

---


### 3. Топ 30 быстрых
### 🚀 ТОП 30 БЫСТРЫХ ⚫ (30)

### [base64/top_30_fast.txt](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/top_30_fast.txt)

<details>
<summary>QR-код</summary>

![qr-top_30_fast](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/qr/top_30_fast.png)

</details>

`30 лучших обычных конфигов (не белые списки) с самым низким пингом.`

<details>
<summary>🪞 Зеркала и другие форматы</summary>

**Base64 (рекомендуется):**
- **GitHub RAW:** `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/top_30_fast.txt`
- **jsDelivr:** `https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/top_30_fast.txt`
- **GitHack:** `https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/top_30_fast.txt`
- **Fastly:** `https://fastly.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/top_30_fast.txt`

**Raw TXT:**
- **GitHub RAW:** `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/top_30_fast.txt`
- **jsDelivr:** `https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/top_30_fast.txt`
- **GitHack:** `https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/top_30_fast.txt`
- **Fastly:** `https://fastly.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/top_30_fast.txt`

| Формат | Ссылка |
| :--- | :--- |
| Base64 | [open](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/top_30_fast.txt) |
| Raw | [open](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/top_30_fast.txt) |
| Clash | [yaml](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/top_30_fast.yaml) |
| Sing-Box | [json](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/top_30_fast.json) |
| QR | [png](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/qr/top_30_fast.png) |

</details>

---


### 4. Все конфиги (без лимитов на количество)
### 📚 ВСЕ КОНФИГИ (Без лимитов) ⚫ (39)

### [base64/all_configs.txt](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/all_configs.txt)

<details>
<summary>QR-код</summary>

![qr-all_configs](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/qr/all_configs.png)

</details>

`Абсолютно все живые конфигурации в одном месте.`

<details>
<summary>🪞 Зеркала и другие форматы</summary>

**Base64 (рекомендуется):**
- **GitHub RAW:** `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/all_configs.txt`
- **jsDelivr:** `https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/all_configs.txt`
- **GitHack:** `https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/all_configs.txt`
- **Fastly:** `https://fastly.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/all_configs.txt`

**Raw TXT:**
- **GitHub RAW:** `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/all_configs.txt`
- **jsDelivr:** `https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/all_configs.txt`
- **GitHack:** `https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/all_configs.txt`
- **Fastly:** `https://fastly.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/all_configs.txt`

| Формат | Ссылка |
| :--- | :--- |
| Base64 | [open](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/all_configs.txt) |
| Raw | [open](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/all_configs.txt) |
| Clash | [yaml](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/all_configs.yaml) |
| Sing-Box | [json](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/all_configs.json) |
| QR | [png](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/qr/all_configs.png) |

</details>

---


### 5. Белые списки (не должно превышать 100)
### ⚪ БЕЛЫЕ СПИСКИ (До 100) ⚪ (0)

### [base64/wl_100.txt](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/wl_100.txt)

<details>
<summary>QR-код</summary>

![qr-wl_100](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/qr/wl_100.png)

</details>

`Обход блокировок по IP/SNI. Скомпилировано максимум 100 штук.`

<details>
<summary>🪞 Зеркала и другие форматы</summary>

**Base64 (рекомендуется):**
- **GitHub RAW:** `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/wl_100.txt`
- **jsDelivr:** `https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/wl_100.txt`
- **GitHack:** `https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/wl_100.txt`
- **Fastly:** `https://fastly.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/wl_100.txt`

**Raw TXT:**
- **GitHub RAW:** `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/whitelists/wl_100.txt`
- **jsDelivr:** `https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/whitelists/wl_100.txt`
- **GitHack:** `https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/whitelists/wl_100.txt`
- **Fastly:** `https://fastly.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/whitelists/wl_100.txt`

| Формат | Ссылка |
| :--- | :--- |
| Base64 | [open](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/wl_100.txt) |
| Raw | [open](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/whitelists/wl_100.txt) |
| Clash | [yaml](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/wl_100.yaml) |
| Sing-Box | [json](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/wl_100.json) |
| QR | [png](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/qr/wl_100.png) |

</details>

---


### 6. Топ 50 белых списков
### ⚪ ТОП 50 БЕЛЫХ СПИСКОВ ⚪ (0)

### [base64/wl_50.txt](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/wl_50.txt)

<details>
<summary>QR-код</summary>

![qr-wl_50](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/qr/wl_50.png)

</details>

`Топ 50 лучших конфигов для обхода жестких белых списков (DPI).`

<details>
<summary>🪞 Зеркала и другие форматы</summary>

**Base64 (рекомендуется):**
- **GitHub RAW:** `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/wl_50.txt`
- **jsDelivr:** `https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/wl_50.txt`
- **GitHack:** `https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/wl_50.txt`
- **Fastly:** `https://fastly.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/wl_50.txt`

**Raw TXT:**
- **GitHub RAW:** `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/whitelists/wl_50.txt`
- **jsDelivr:** `https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/whitelists/wl_50.txt`
- **GitHack:** `https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/whitelists/wl_50.txt`
- **Fastly:** `https://fastly.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/whitelists/wl_50.txt`

| Формат | Ссылка |
| :--- | :--- |
| Base64 | [open](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/wl_50.txt) |
| Raw | [open](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/whitelists/wl_50.txt) |
| Clash | [yaml](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/wl_50.yaml) |
| Sing-Box | [json](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/wl_50.json) |
| QR | [png](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/qr/wl_50.png) |

</details>

---


### 7. Топ 30 белых списков
### ⚪ ТОП 30 БЕЛЫХ СПИСКОВ ⚪ (0)

### [base64/wl_30.txt](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/wl_30.txt)

<details>
<summary>QR-код</summary>

![qr-wl_30](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/qr/wl_30.png)

</details>

`Топ 30 лучших конфигов для обхода жестких белых списков (DPI).`

<details>
<summary>🪞 Зеркала и другие форматы</summary>

**Base64 (рекомендуется):**
- **GitHub RAW:** `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/wl_30.txt`
- **jsDelivr:** `https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/wl_30.txt`
- **GitHack:** `https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/wl_30.txt`
- **Fastly:** `https://fastly.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/wl_30.txt`

**Raw TXT:**
- **GitHub RAW:** `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/whitelists/wl_30.txt`
- **jsDelivr:** `https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/whitelists/wl_30.txt`
- **GitHack:** `https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/whitelists/wl_30.txt`
- **Fastly:** `https://fastly.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/whitelists/wl_30.txt`

| Формат | Ссылка |
| :--- | :--- |
| Base64 | [open](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/wl_30.txt) |
| Raw | [open](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/whitelists/wl_30.txt) |
| Clash | [yaml](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/wl_30.yaml) |
| Sing-Box | [json](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/wl_30.json) |
| QR | [png](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/qr/wl_30.png) |

</details>

---


### 8. Все вместе (50 обычных конфигов, 50 белых списков)
### 🔄 ВСЕ ВМЕСТЕ (50/50) ☯️ (39)

### [base64/mixed_100.txt](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/mixed_100.txt)

<details>
<summary>QR-код</summary>

![qr-mixed_100](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/qr/mixed_100.png)

</details>

`Микс: 50 быстрых обычных конфигураций + 50 для белых списков.`

<details>
<summary>🪞 Зеркала и другие форматы</summary>

**Base64 (рекомендуется):**
- **GitHub RAW:** `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/mixed_100.txt`
- **jsDelivr:** `https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/mixed_100.txt`
- **GitHack:** `https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/mixed_100.txt`
- **Fastly:** `https://fastly.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/mixed_100.txt`

**Raw TXT:**
- **GitHub RAW:** `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/mixed_100.txt`
- **jsDelivr:** `https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/mixed_100.txt`
- **GitHack:** `https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/mixed_100.txt`
- **Fastly:** `https://fastly.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/mixed_100.txt`

| Формат | Ссылка |
| :--- | :--- |
| Base64 | [open](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/mixed_100.txt) |
| Raw | [open](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/mixed_100.txt) |
| Clash | [yaml](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/mixed_100.yaml) |
| Sing-Box | [json](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/mixed_100.json) |
| QR | [png](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/qr/mixed_100.png) |

</details>

---


### 9. Все конфиги белых списков без лимитов на количество
### ⚪ ВСЕ БЕЛЫЕ СПИСКИ (Без лимитов) ⚪ (0)

### [base64/all_wl.txt](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/all_wl.txt)

<details>
<summary>QR-код</summary>

![qr-all_wl](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/qr/all_wl.png)

</details>

`Полный набор всех конфигов, проходящих проверку на белые списки.`

<details>
<summary>🪞 Зеркала и другие форматы</summary>

**Base64 (рекомендуется):**
- **GitHub RAW:** `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/all_wl.txt`
- **jsDelivr:** `https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/all_wl.txt`
- **GitHack:** `https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/all_wl.txt`
- **Fastly:** `https://fastly.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/all_wl.txt`

**Raw TXT:**
- **GitHub RAW:** `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/whitelists/all_wl.txt`
- **jsDelivr:** `https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/whitelists/all_wl.txt`
- **GitHack:** `https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/whitelists/all_wl.txt`
- **Fastly:** `https://fastly.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/whitelists/all_wl.txt`

| Формат | Ссылка |
| :--- | :--- |
| Base64 | [open](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/all_wl.txt) |
| Raw | [open](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/whitelists/all_wl.txt) |
| Clash | [yaml](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/all_wl.yaml) |
| Sing-Box | [json](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/all_wl.json) |
| QR | [png](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/qr/all_wl.png) |

</details>

---


### 10. Топ самых быстрых конфигов (без разницы простые или белые списки)
### ⚡ ТОП САМЫХ БЫСТРЫХ (Любые) ⚡ (39)

### [base64/fastest_all_100.txt](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/fastest_all_100.txt)

<details>
<summary>QR-код</summary>

![qr-fastest_all_100](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/qr/fastest_all_100.png)

</details>

`Топ 100 конфигов с самым низким пингом, без разницы простые они или белые списки.`

<details>
<summary>🪞 Зеркала и другие форматы</summary>

**Base64 (рекомендуется):**
- **GitHub RAW:** `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/fastest_all_100.txt`
- **jsDelivr:** `https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/fastest_all_100.txt`
- **GitHack:** `https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/fastest_all_100.txt`
- **Fastly:** `https://fastly.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/base64/fastest_all_100.txt`

**Raw TXT:**
- **GitHub RAW:** `https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/fastest_all_100.txt`
- **jsDelivr:** `https://cdn.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/fastest_all_100.txt`
- **GitHack:** `https://raw.githack.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/fastest_all_100.txt`
- **Fastly:** `https://fastly.jsdelivr.net/gh/ewecrow78-gif/Free_VPN_Aggregator@output/fastest_all_100.txt`

| Формат | Ссылка |
| :--- | :--- |
| Base64 | [open](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/fastest_all_100.txt) |
| Raw | [open](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/fastest_all_100.txt) |
| Clash | [yaml](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/fastest_all_100.yaml) |
| Sing-Box | [json](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/fastest_all_100.json) |
| QR | [png](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/qr/fastest_all_100.png) |

</details>

---


---

### 📦 Полный список ссылок для клиента

<details>
<summary><b>📋 Раскрыть все Base64 URL (копировать в клиент)</b></summary>

> Рекомендуемые: **[top_50_fast](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/top_50_fast.txt)**, **[wl_100](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/wl_100.txt)**, **[mixed_100](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/mixed_100.txt)**.

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

## ➕ Как добавить свой источник конфигов

Хотите добавить новый источник?
1. Откройте `urls.txt` для добавления прямых ссылок на подписки (TXT, Base64).
2. Откройте `tg_channels.txt` для добавления открытых Telegram каналов.
3. Откройте `tg_forums.txt` для добавления закрытых Telegram форумов (потребуется `TG_SESSION`).
4. Для добавления доверенных доменов для маскировки SNI обновите `sni.txt`.
5. Сделайте Pull Request!

---

## 🛠 Troubleshooting (для разработчиков)

- **Где хранятся сырые данные и логи?** 
  Проверьте папку `data/`. `history.json` хранит историю стабильности нод.
- **Почему в README нули?** 
  Проверьте [configs/stats.json](configs/stats.json). Если там пусто, значит пайплайн упал на этапе парсинга.
- **Out of Memory при пуше?**
  Убедитесь, что в Git установлены лимиты (`git config pack.windowMemory 100m`).

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

## ⚠️ Безопасность и Disclaimer

> [!CAUTION]
> **Бесплатные публичные VPN могут быть опасны.**
> - Не используйте для банков, Госуслуг, крипты, почты без HTTPS.
> - Админ узла теоретически видит незашифрованный трафик.
> - `allowInsecure=1` → отдельный risky-список + штраф в score.
> - На Android с RU-приложениями задайте **логин/пароль локального inbound** (Karing / v2rayNG / Happ).
> - Проект educational / anti-censorship, AS IS, без гарантий. 
> 
> **Disclaimer:** Мы не владеем этими серверами. Конфигурации собираются автоматически из открытых источников в интернете. Используйте на свой страх и риск.

---

## 📊 Статистика

<details>
<summary><b>🌍 По странам</b></summary>

| Страна | Кол-во | Флаг | Подписки |
| :--- | :---: | :---: | :--- |
| United States | 9 | 🇺🇸 | [Base64](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/country_united_states.txt) \| [Raw](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/countries/united_states.txt) \| [Clash](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/country_united_states.yaml) \| [Sing-Box](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/country_united_states.json) |
| Poland | 6 | 🇵🇱 | [Base64](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/country_poland.txt) \| [Raw](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/countries/poland.txt) \| [Clash](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/country_poland.yaml) \| [Sing-Box](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/country_poland.json) |
| Germany | 4 | 🇩🇪 | [Base64](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/country_germany.txt) \| [Raw](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/countries/germany.txt) \| [Clash](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/country_germany.yaml) \| [Sing-Box](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/country_germany.json) |
| The Netherlands | 4 | 🇳🇱 | [Base64](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/country_the_netherlands.txt) \| [Raw](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/countries/the_netherlands.txt) \| [Clash](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/country_the_netherlands.yaml) \| [Sing-Box](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/country_the_netherlands.json) |
| France | 2 | 🇫🇷 | [Base64](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/country_france.txt) \| [Raw](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/countries/france.txt) \| [Clash](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/country_france.yaml) \| [Sing-Box](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/country_france.json) |
| United Kingdom | 2 | 🇬🇧 | [Base64](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/country_united_kingdom.txt) \| [Raw](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/countries/united_kingdom.txt) \| [Clash](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/country_united_kingdom.yaml) \| [Sing-Box](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/country_united_kingdom.json) |
| Sweden | 2 | 🇸🇪 | [Base64](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/country_sweden.txt) \| [Raw](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/countries/sweden.txt) \| [Clash](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/country_sweden.yaml) \| [Sing-Box](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/country_sweden.json) |
| Canada | 2 | 🇨🇦 | [Base64](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/country_canada.txt) \| [Raw](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/countries/canada.txt) \| [Clash](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/country_canada.yaml) \| [Sing-Box](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/country_canada.json) |
| Russia | 1 | 🇷🇺 | [Base64](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/country_russia.txt) \| [Raw](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/countries/russia.txt) \| [Clash](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/country_russia.yaml) \| [Sing-Box](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/country_russia.json) |
| Finland | 1 | 🇫🇮 | [Base64](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/country_finland.txt) \| [Raw](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/countries/finland.txt) \| [Clash](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/country_finland.yaml) \| [Sing-Box](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/country_finland.json) |
| Switzerland | 1 | 🇨🇭 | [Base64](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/country_switzerland.txt) \| [Raw](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/countries/switzerland.txt) \| [Clash](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/country_switzerland.yaml) \| [Sing-Box](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/country_switzerland.json) |
| Estonia | 1 | 🏳️ | [Base64](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/country_estonia.txt) \| [Raw](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/countries/estonia.txt) \| [Clash](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/country_estonia.yaml) \| [Sing-Box](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/country_estonia.json) |
| Ireland | 1 | 🏳️ | [Base64](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/country_ireland.txt) \| [Raw](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/countries/ireland.txt) \| [Clash](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/country_ireland.yaml) \| [Sing-Box](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/country_ireland.json) |
| Romania | 1 | 🏳️ | [Base64](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/country_romania.txt) \| [Raw](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/countries/romania.txt) \| [Clash](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/country_romania.yaml) \| [Sing-Box](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/country_romania.json) |
| India | 1 | 🇮🇳 | [Base64](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/country_india.txt) \| [Raw](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/countries/india.txt) \| [Clash](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/country_india.yaml) \| [Sing-Box](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/country_india.json) |
| Colombia | 1 | 🏳️ | [Base64](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/base64/country_colombia.txt) \| [Raw](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/countries/colombia.txt) \| [Clash](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/clash/country_colombia.yaml) \| [Sing-Box](https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/main/configs/sing-box/country_colombia.json) |

</details>

<details>
<summary><b>🔌 По протоколам</b></summary>

| Протокол | Кол-во | Доля |
| :--- | :---: | :---: |
| VLESS | 32 | 82.1% |
| TROJAN | 4 | 10.3% |
| SS | 3 | 7.7% |

</details>

---

## 📜 Лицензия

MIT — см. [LICENSE](LICENSE).

---

<div align="center">

**⭐ Если проект полезен — поставьте Star**

<sub>Generated automatically by Free VPN Aggregator Pro · 2026-08-11 18:14 UTC</sub>

</div>
