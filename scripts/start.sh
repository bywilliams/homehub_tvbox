#!/data/data/com.termux/files/usr/bin/bash

HOMEHUB="$HOME/Homehub"
LOG="$HOMEHUB/logs/system.log"

echo "================================"
echo " Starting HomeHub Gateway"
echo "================================"

echo ""

DATE=$(date '+%Y-%m-%d %H:%M:%S')

echo "$DATE - HomeHub start requested" >> $LOG


echo "Checking directories..."

if [ -d "$HOMEHUB/configs" ]; then
    echo "✓ configs"
else
    echo "✗ configs missing"
fi


if [ -d "$HOMEHUB/storage" ]; then
    echo "✓ storage"
else
    echo "✗ storage missing"
fi


if [ -d "$HOMEHUB/logs" ]; then
    echo "✓ logs"
else
    mkdir -p "$HOMEHUB/logs"
    echo "✓ logs created"
fi


echo ""

echo "Starting MQTT..."


if pgrep mosquitto > /dev/null
then
    echo "✓ MQTT already running"
else

    mosquitto \
    -c "$HOMEHUB/configs/mosquitto/mosquitto.conf" \
    >> "$HOMEHUB/logs/mqtt.log" 2>&1 &

    sleep 2

    if pgrep mosquitto > /dev/null
    then
        echo "✓ MQTT started"
        echo "$DATE - MQTT started" >> $LOG
    else
        echo "✗ MQTT failed"
        echo "$DATE - MQTT failed" >> $LOG
    fi

fi


echo ""

echo "HomeHub Ready"

echo "================================"
