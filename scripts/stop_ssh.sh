#!/data/data/com.termux/files/usr/bin/bash

echo "Parando SSH..."

pkill -x sshd

if pgrep -x sshd > /dev/null
then
    echo "Falha ao parar SSH"
    exit 1
else
    echo "SSH parado"
fi
