#!/data/data/com.termux/files/usr/bin/bash

CONFIG="$HOME/Homehub/configs/system.conf"

echo "================================"
echo "      HomeHub Version"
echo "================================"

echo ""

if [ -f "$CONFIG" ]
then

    echo "Software:"
    echo "HomeHub Gateway"

    echo ""

    echo "Version:"
    grep "version=" "$CONFIG" | cut -d '=' -f2

    echo ""

    echo "Hardware:"
    grep "hardware=" "$CONFIG" | cut -d '=' -f2

    echo ""

    echo "Mode:"
    grep "mode=" "$CONFIG" | cut -d '=' -f2

else

    echo "Configuration not found"

fi


echo ""

echo "================================"
