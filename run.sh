#!/usr/bin/env bash
set -Eeuo pipefail
cd /root/Free_VPN_Aggregator || exit

git pull origin main --rebase || true

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
