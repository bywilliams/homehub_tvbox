#!/data/data/com.termux/files/usr/bin/bash

HOMEHUB="$HOME/Homehub"
SERVICES_DIR="$HOMEHUB/services"

list_services() {

    for service in "$SERVICES_DIR"/*.service
    do
        [ -f "$service" ] || continue

        source "$service"

        echo "$NAME"
    done

}

show_status() {

    for service in "$SERVICES_DIR"/*.service
    do

        [ -f "$service" ] || continue

        unset NAME
        unset PORT
        unset PID_FILE
        unset PID_NAME

        source "$service"

        STATUS="OFFLINE"
        PID="-"

        if [ -n "$PID_FILE" ]; then

            PID_PATH="$HOMEHUB/$PID_FILE"

            if [ -f "$PID_PATH" ]; then

                PID=$(cat "$PID_PATH")

                if kill -0 "$PID" 2>/dev/null; then
                    STATUS="ONLINE"
                fi

            fi

        elif [ -n "$PID_NAME" ]; then

            PID=$(pgrep "$PID_NAME" | head -1)

            if [ -n "$PID" ]; then
                STATUS="ONLINE"
            else
                PID="-"
            fi

        fi

        printf "%-15s %-10s %s\n" "$NAME" "$STATUS" "$PID"

    done

}
