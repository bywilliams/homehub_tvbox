#!/data/data/com.termux/files/usr/bin/bash

HOMEHUB="$HOME/Homehub"

PIDFILE="$HOMEHUB/runtime/api.pid"

LOG="$HOMEHUB/logs/api.log"


echo "Starting HomeHub API..."


if [ -f "$PIDFILE" ]; then

    PID=$(cat "$PIDFILE")

    if kill -0 "$PID" 2>/dev/null; then
        echo "API already running PID=$PID"
        exit 0
    fi

fi


cd "$HOMEHUB/api" || exit 1


source venv/bin/activate


nohup python -m app.web \
>> "$LOG" 2>&1 &


PID=$!


echo $PID > "$PIDFILE"


sleep 3


if kill -0 "$PID" 2>/dev/null
then
    echo "✓ API ONLINE PID=$PID"
else
    echo "✗ API FAILED"
fi
