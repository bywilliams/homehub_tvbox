#!/data/data/com.termux/files/usr/bin/bash

HOMEHUB="$HOME/Homehub"
PIDFILE="$HOMEHUB/runtime/api.pid"

echo "Stopping API..."

if [ -f "$PIDFILE" ]; then

    PID=$(cat "$PIDFILE")

    if kill -0 $PID 2>/dev/null
    then
        kill $PID
        sleep 2

        echo "✓ API stopped"

    else
        echo "✓ API already stopped"
    fi

    rm "$PIDFILE"

else

    echo "✓ API PID not found"

fi
