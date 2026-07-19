#!/data/data/com.termux/files/usr/bin/bash

HOMEHUB="$HOME/Homehub"
INTERNAL_STORAGE="/data"
SD_STORAGE="$HOME/storage/external-1"

echo "================================"
echo "       HomeHub Gateway"
echo "================================"

echo ""

if [ -f "$HOMEHUB/VERSION" ]; then
    echo "Version:"
    cat "$HOMEHUB/VERSION"
else
    echo "Version: unknown"
fi

echo ""

CONFIG="$HOME/Homehub/configs/system.conf"

echo "Device:"

grep "name=" "$CONFIG" | cut -d '=' -f2

echo ""

echo "ID:"

grep "device_id=" "$CONFIG" | cut -d '=' -f2

echo ""

echo "Hardware:"

grep "hardware=" "$CONFIG" | cut -d '=' -f2

echo ""

echo "Network:"
ip addr show wlan0 | grep "inet "

echo ""

echo "Services:"
echo ""

if pgrep mosquitto > /dev/null
then
    echo "MQTT     ✓ ONLINE"
else
    echo "MQTT     ✗ OFFLINE"
fi

echo ""

echo "MQTT Port:"

if ss -tln | grep 1883 > /dev/null
then
    echo "1883 ✓ LISTENING"
else
    echo "1883 ✗ CLOSED"
fi


echo ""


echo "Storage:"
echo ""

echo "Internal Storage:"
echo ""

df -h "$INTERNAL_STORAGE" | tail -1 | awk '
{
print "Total:"
print $2
print ""
print "Used:"
print $3
print ""
print "Free:"
print $4
print ""
print "Usage:"
print $5
}
'

echo ""

echo "SD Card:"
echo ""

df -h "$SD_STORAGE" | tail -1 | awk '
{
print "Total:"
print $2
print ""
print "Used:"
print $3
print ""
print "Free:"
print $4
print ""
print "Usage:"
print $5
}
'


echo ""

echo "================================"
