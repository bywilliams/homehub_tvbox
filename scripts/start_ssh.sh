#!/data/data/com.termux/files/usr/bin/bash

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

if pgrep -x sshd > /dev/null
then
    echo "SSH já está rodando"
    exit 0
fi

echo "Iniciando SSH..."

sshd

if pgrep -x sshd > /dev/null
then
    echo "SSH iniciado com sucesso"
else
    echo "Falha ao iniciar SSH"
    exit 1
fi
