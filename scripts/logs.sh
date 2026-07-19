#!/data/data/com.termux/files/usr/bin/bash

HOMEHUB="$HOME/Homehub"

echo "================================"
echo "        HomeHub Logs"
echo "================================"

echo ""

if [ -f "$HOMEHUB/logs/system.log" ]
then

    echo "Últimos eventos:"
    echo ""

    tail -20 "$HOMEHUB/logs/system.log"

else

    echo "Nenhum log encontrado."

fi

echo ""

echo "================================"
