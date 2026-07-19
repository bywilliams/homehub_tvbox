#!/data/data/com.termux/files/usr/bin/bash

HOMEHUB="$HOME/Homehub"

echo "================================"
echo "     HomeHub Diagnostic"
echo "================================"

echo ""

# Version

echo "Version:"

if [ -f "$HOMEHUB/VERSION" ]
then
    echo "✓ $(cat $HOMEHUB/VERSION)"
else
    echo "✗ VERSION missing"
fi


echo ""

# Directories

echo "Directories:"
echo ""

for DIR in configs storage logs scripts
do

    if [ -d "$HOMEHUB/$DIR" ]
    then
        echo "✓ $DIR"
    else
        echo "✗ $DIR missing"
    fi

done


echo ""

# Network

echo "Network:"
echo ""

IP=$(ip addr show wlan0 | grep "inet " | awk '{print $2}')

if [ ! -z "$IP" ]
then
    echo "✓ IP $IP"
else
    echo "✗ Network unavailable"
fi


echo ""

# MQTT

echo "MQTT:"
echo ""

if pgrep mosquitto > /dev/null
then
    echo "✓ Process running"
else
    echo "✗ Process offline"
fi


if ss -tln | grep 1883 > /dev/null
then
    echo "✓ Port 1883 listening"
else
    echo "✗ Port 1883 closed"
fi


if [ -f "$HOMEHUB/configs/mosquitto/mosquitto.conf" ]
then
    echo "✓ Config found"
else
    echo "✗ Config missing"
fi


echo ""

# Storage

echo "Storage:"
echo ""

df -h "$HOMEHUB" | tail -1


echo ""

echo "================================"
echo "Diagnostic complete"
echo "================================"
