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


echo "SSH:"

if pgrep -x sshd > /dev/null
then
    SSH_PID=$(pgrep -x sshd | head -1)

    echo "✓ ONLINE"
    echo "PID: $SSH_PID"
else
    echo "✗ OFFLINE"
fi

echo ""

echo "SSH Port:"

if ss -tln | grep 8022 > /dev/null
then
    echo "8022 ✓ LISTENING"
else
    echo "8022 ✗ CLOSED"
fi

echo ""


echo "MQTT:"

if pgrep mosquitto > /dev/null
then
    MQTT_PID=$(pgrep mosquitto | head -1)

    echo "✓ ONLINE"
    echo "PID: $MQTT_PID"

else

    echo "✗ OFFLINE"

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

echo "API:"

API_PID_FILE="$HOMEHUB/runtime/api.pid"


if [ -f "$API_PID_FILE" ]
then

    API_PID=$(cat "$API_PID_FILE")


    if kill -0 $API_PID 2>/dev/null
    then

        echo "✓ ONLINE"
        echo "PID: $API_PID"

    else

        echo "✗ OFFLINE"

    fi

else

    echo "✗ OFFLINE"

fi



echo ""

echo "API Port:"

if ss -tln | grep 8000 > /dev/null
then

    echo "8000 ✓ LISTENING"

else

    echo "8000 ✗ CLOSED"

fi




echo ""

echo "Dashboard:"

DASH_PID_FILE="$HOMEHUB/runtime/dashboard.pid"


if [ -f "$DASH_PID_FILE" ]
then

    DASH_PID=$(cat "$DASH_PID_FILE")


    if kill -0 $DASH_PID 2>/dev/null
    then

        echo "✓ ONLINE"
        echo "PID: $DASH_PID"

    else

        echo "✗ OFFLINE"

    fi

else

    echo "✗ OFFLINE"

fi



echo ""

echo "Dashboard Port:"

if ss -tln | grep 8080 > /dev/null
then

    echo "8080 ✓ LISTENING"

else

    echo "8080 ✗ CLOSED"

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
