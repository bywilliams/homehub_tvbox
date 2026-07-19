#!/data/data/com.termux/files/usr/bin/bash

CONFIG="$HOME/Homehub/configs/system.conf"

echo "================================"
echo "        HomeHub Info"
echo "================================"

echo ""

if [ -f "$CONFIG" ]
then

    echo "Device Information:"
    echo ""

    grep -v "#" "$CONFIG" | grep -v "\[" | grep -v "^$"

else

    echo "Configuration not found"

fi


echo ""

echo "================================"
