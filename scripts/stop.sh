#!/data/data/com.termux/files/usr/bin/bash

HOMEHUB="$HOME/Homehub"
LOG="$HOMEHUB/logs/system.log"

echo "================================"
echo " Stopping HomeHub Gateway"
echo "================================"

DATE=$(date '+%Y-%m-%d %H:%M:%S')


echo ""

echo "Stopping MQTT..."


if pgrep mosquitto > /dev/null
then

    pkill mosquitto

    sleep 2

    if pgrep mosquitto > /dev/null
    then
        echo "✗ MQTT still running"
    else
        echo "✓ MQTT stopped"
        echo "$DATE - MQTT stopped" >> $LOG
    fi

else

    echo "✓ MQTT already stopped"

fi


echo ""

echo "HomeHub stopped"

echo "================================"
