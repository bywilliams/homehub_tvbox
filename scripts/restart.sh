#!/data/data/com.termux/files/usr/bin/bash

HOMEHUB="$HOME/Homehub"

echo "================================"
echo " Restarting HomeHub Gateway"
echo "================================"

echo ""

echo "Stopping MQTT..."

"$HOMEHUB/scripts/stop.sh"

echo ""

sleep 2

echo "Starting MQTT..."

"$HOMEHUB/scripts/start.sh"

echo ""

echo "Checking service..."

echo ""

"$HOMEHUB/scripts/status.sh"

