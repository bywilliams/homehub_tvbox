#!/data/data/com.termux/files/usr/bin/bash

echo "================================"
echo " HomeHub Boot Manager"
echo "================================"
echo ""


echo "Verificando estado do HomeHub..."
echo ""

SSH_OK=0
MQTT_OK=0
API_OK=0
DASH_OK=0

pgrep -x sshd >/dev/null && SSH_OK=1
pgrep mosquitto >/dev/null && MQTT_OK=1
ss -tln | grep -q ":8000 " && API_OK=1
ss -tln | grep -q ":8080 " && DASH_OK=1


if [ $SSH_OK -eq 1 ] && \
   [ $MQTT_OK -eq 1 ] && \
   [ $API_OK -eq 1 ] && \
   [ $DASH_OK -eq 1 ]
then
    echo "✓ HomeHub já está em execução."
    exit 0
fi


echo "Aguardando Wi-Fi..."

while ! ip addr show wlan0 | grep -q "inet "
do
    sleep 2
done

echo "Wi-Fi OK"


sleep 10

echo ""

echo "Iniciando HomeHub..."

$HOME/Homehub/scripts/start.sh

echo ""

echo "Boot concluído."
