#!/data/data/com.termux/files/usr/bin/bash

HOMEHUB="$HOME/Homehub"
PIDFILE="$HOMEHUB/runtime/dashboard.pid"

echo "Stopping Dashboard..."

if [ -f "$PIDFILE" ]; then

    PID=$(cat "$PIDFILE")

    if kill -0 $PID 2>/dev/null
    then
        kill $PID
        sleep 2

        echo "✓ Dashboard stopped"

    else
        echo "✓ Dashboard already stopped"
    fi

    rm "$PIDFILE"

else

    echo "✓ Dashboard PID not found"

fi
