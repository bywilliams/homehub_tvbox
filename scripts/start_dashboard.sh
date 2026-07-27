#!/data/data/com.termux/files/usr/bin/bash

HOMEHUB="$HOME/Homehub"

PIDFILE="$HOMEHUB/runtime/dashboard.pid"

LOG="$HOMEHUB/logs/dashboard.log"


echo "Starting Dashboard..."


if [ -f "$PIDFILE" ]; then

    PID=$(cat "$PIDFILE")

    if kill -0 "$PID" 2>/dev/null; then
        echo "Dashboard already running PID=$PID"
        exit 0
    fi

fi


cd "$HOMEHUB/dashboard" || exit 1


nohup python -m http.server 8080 --bind 0.0.0.0 \
>> "$LOG" 2>&1 &


PID=$!


echo $PID > "$PIDFILE"


sleep 2


if kill -0 "$PID" 2>/dev/null
then
    echo "✓ Dashboard ONLINE PID=$PID"
else
    echo "✗ Dashboard FAILED"
fi
