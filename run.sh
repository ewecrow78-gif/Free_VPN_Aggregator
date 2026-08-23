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

# Устанавливаем прокси-туннель
if ! pgrep -f "ssh -o StrictHostKeyChecking=no -N -D 1080 root@178.253.44.97" > /dev/null; then
    echo "Запускаем Tor прокси..."
    pgrep -f tor > /dev/null || tor &
fi

# Загружаем ключи из .env для Телеграма
set -a
[ -f .env ] && source .env
set +a

# Убиваем зависшие с прошлых запусков процессы xray, чтобы освободить память и порты
pkill -9 -f xray || true

source venv/bin/activate
python main.py

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
