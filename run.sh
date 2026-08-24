#!/usr/bin/env bash
set -Eeuo pipefail
cd "$(dirname "$0")" || exit

LOCKFILE="$(pwd)/run.lock"
if [ -e "${LOCKFILE}" ] && kill -0 `cat "${LOCKFILE}"` 2>/dev/null; then
    echo "Скрипт уже запущен."
    exit 1
fi
echo $$ > "${LOCKFILE}"
trap 'rm -f "${LOCKFILE}"; exit' INT TERM EXIT

git pull origin main --rebase || true

# Убиваем зависшие с прошлых запусков процессы xray
pkill -9 -f xray || true
pkill -9 -f tor || true

source venv/bin/activate

echo "Запускаем локальный Xray-прокси для сбора Telegram..."
export PROXY_PORT=10000
python bootstrap_proxy.py || true

# Загружаем ключи из .env для Телеграма
set -a
[ -f .env ] && source .env
set +a

python -u main.py

git config user.name "VPN Aggregator VPS"
git config user.email "root@myserver.com"

git add .
if git diff --cached --quiet; then
    echo "Новых изменений нет, отправлять нечего."
    exit 0
fi

echo "[Git] Отправка обновленных подписок на GitHub..."
git commit -m "Auto-update VPN subscriptions"
git push origin main
echo "[Git] Успешно завершено!"
