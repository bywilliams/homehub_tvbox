#!/data/data/com.termux/files/usr/bin/bash

CONFIG="$HOME/Homehub/configs/storage.conf"

echo "================================"
echo "       HomeHub Storage"
echo "================================"

echo ""

if [ ! -f "$CONFIG" ]
then
    echo "Storage configuration not found"
    exit 1
fi


PATH_STORAGE=$(grep "path=" "$CONFIG" | cut -d '=' -f2)
TYPE=$(grep "type=" "$CONFIG" | cut -d '=' -f2)
NAME=$(grep "name=" "$CONFIG" | cut -d '=' -f2)
CAPACITY=$(grep "capacity=" "$CONFIG" | cut -d '=' -f2)


echo "Name:"
echo "$NAME"

echo ""

echo "Type:"
echo "$TYPE"

echo ""

echo "Path:"
echo "$PATH_STORAGE"

echo ""

echo "Storage Information:"
echo ""

df -h "$PATH_STORAGE" | tail -1 | awk '
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


if [ -d "$PATH_STORAGE" ]
then
    echo "Status:"
    echo "✓ ONLINE"
else
    echo "Status:"
    echo "✗ OFFLINE"
fi


echo ""

echo "Directories:"
echo ""

for DIR in files uploads backups database media
do

    if [ -d "$PATH_STORAGE/$DIR" ]
    then
        echo "✓ $DIR"
    else
        echo "✗ $DIR missing"
    fi

done


echo ""

echo "================================"
