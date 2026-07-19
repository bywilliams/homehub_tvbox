# HomeHub Gateway v0.1.0

## Core + MQTT Gateway + Storage Foundation

**Versão:** 0.1.0
**Data:** 19/07/2026
**Hardware:** TV Box RK3066
**Plataforma:** Android 11.1 + Termux

---

# 1. Visão Geral

O HomeHub é um projeto de transformação de uma TV Box RK3066 em um gateway doméstico de automação, comunicação e armazenamento local.

O objetivo do projeto é criar uma plataforma independente capaz de:

* Comunicação com dispositivos IoT através de MQTT;
* Gerenciamento local de serviços;
* Armazenamento privado utilizando cartão SD;
* Execução futura de APIs e dashboards web;
* Integração com dispositivos como ESP32 e assistentes de automação.

A versão **v0.1.0** representa o primeiro marco estável do projeto, contendo a infraestrutura base do gateway.

---

# 2. Hardware

## Dispositivo

```
TV Box RK3066
```

## Especificações

| Item                  | Informação          |
| --------------------- | ------------------- |
| CPU                   | Dual Core Cortex-A9 |
| GPU                   | Mali-400 MP         |
| RAM                   | 1 GB                |
| Armazenamento interno | 8 GB                |
| Cartão SD             | 250 GB              |
| Sistema operacional   | Android 11.1        |
| Ambiente Linux        | Termux              |

---

# 3. Arquitetura Atual

A arquitetura do HomeHub está dividida em duas áreas principais:

```
                 HomeHub Gateway v0.1.0


                    Android 11.1

                         |

                      Termux

                         |

        +----------------+----------------+

        |                                 |

  HomeHub Core                    HomeHub Storage

  Memória interna                 Cartão SD 250GB


  scripts                         files
  configs                         uploads
  logs                            backups
  services                        database
  mqtt                            media

```

---

# 4. Estrutura do Projeto

Diretório principal:

```
Homehub/

├── api
├── configs
│
│   ├── mosquitto
│   │   ├── data
│   │   │   └── mosquitto.db
│   │   ├── mosquitto.conf
│   │   └── passwd
│   │
│   ├── system.conf
│   └── storage.conf
│
├── dashboard
├── database
├── docs
├── logs
├── scripts
├── services
├── storage
└── tests
```

---

# 5. Ambiente Instalado

Pacotes principais instalados no Termux:

```
openssh
nano
tree
htop
rsync
mosquitto
```

Recursos configurados:

* SSH remoto;
* Estrutura organizada do projeto;
* Scripts administrativos;
* Broker MQTT;
* Sistema de logs.

---

# 6. Sistema de Gerenciamento CLI

O HomeHub possui uma interface administrativa através do comando:

```
homehub
```

Comandos disponíveis:

---

## Inicializar serviços

```bash
homehub start
```

Responsável por:

* Verificar diretórios;
* Iniciar serviços;
* Registrar eventos.

---

## Parar serviços

```bash
homehub stop
```

---

## Reiniciar serviços

```bash
homehub restart
```

---

## Verificar status

```bash
homehub status
```

Apresenta:

* Identidade;
* Versão;
* Rede;
* Serviços ativos;
* Armazenamento.

---

## Visualizar logs

```bash
homehub logs
```

---

## Diagnóstico

```bash
homehub diagnose
```

Realiza verificações:

* Diretórios;
* Rede;
* MQTT;
* Configurações;
* Armazenamento.

---

## Informações do dispositivo

```bash
homehub info
```

Exemplo:

```
Device:
HomeHub Casa

ID:
HH-RK3066-001

Hardware:
RK3066
```

---

## Informações da versão

```bash
homehub version
```

Resultado:

```
Software:
HomeHub Gateway

Version:
0.1.0

Hardware:
RK3066

Mode:
MQTT Gateway
```

---

## Informações do armazenamento

```bash
homehub storage
```

---

# 7. MQTT Gateway

O HomeHub possui um broker MQTT utilizando Mosquitto.

## Configuração

Arquivo:

```
configs/mosquitto/mosquitto.conf
```

Configuração principal:

```
listener 1883 0.0.0.0

allow_anonymous false

password_file passwd

persistence true
```

---

## Segurança

O broker utiliza autenticação:

Usuário:

```
homehub
```

Senha:

```
Home123
```

---

## Persistência

Ativada:

```
persistence true
```

Banco:

```
configs/mosquitto/data/mosquitto.db
```

---

## Teste realizado

Publicação:

```bash
mosquitto_pub
```

Assinatura:

```bash
mosquitto_sub
```

Resultado:

```
✓ Comunicação MQTT validada
```

---

# 8. Identidade do Dispositivo

Arquivo:

```
configs/system.conf
```

Conteúdo:

```
name=HomeHub Casa

device_id=HH-RK3066-001

hardware=RK3066

version=0.1.0

mode=MQTT Gateway
```

Essa identidade será utilizada futuramente por:

* APIs;
* Dashboard;
* MQTT Topics;
* Monitoramento.

---

# 9. HomeHub Storage Manager

O HomeHub utiliza um cartão SD externo de 250GB para armazenamento de dados.

## Configuração

Arquivo:

```
configs/storage.conf
```

Configuração:

```
path=/data/data/com.termux/files/home/storage/external-1/HomeHub

type=SDCARD

name=HomeHub Storage
```

---

# 10. Estrutura do Storage

Local:

```
~/storage/external-1/HomeHub
```

Estrutura:

```
HomeHub/

├── files
├── uploads
├── backups
├── database
└── media
```

---

# 11. Monitoramento de Armazenamento

O sistema realiza leitura real do espaço disponível.

Exemplo:

```
Internal Storage:

Total:
5.3G

Used:
2.6G

Free:
2.6G

Usage:
51%


SD Card:

Total:
250G

Used:
224M

Free:
250G

Usage:
1%
```

---

# 12. Diagnóstico do Sistema

Comando:

```bash
homehub diagnose
```

Resultado esperado:

```
Directories:

✓ configs
✓ storage
✓ logs
✓ scripts


Network:

✓ IP encontrado


MQTT:

✓ Process running
✓ Port 1883 listening
✓ Config found


Storage:

✓ Available

Diagnostic complete
```

---

# 13. Histórico de Implementação

## Fase MQTT

Concluído:

* Instalação Mosquitto;
* Configuração personalizada;
* Autenticação;
* Persistência;
* Testes publish/subscribe.

---

## Fase Core

Concluído:

* Estrutura inicial do projeto;
* Scripts administrativos;
* Logs;
* Diagnóstico;
* CLI HomeHub.

---

## Fase Identidade

Concluído:

* Nome do dispositivo;
* ID único;
* Hardware;
* Versão;
* Modo operacional.

---

## Fase Storage

Concluído:

* Reconhecimento do cartão SD;
* Configuração persistente;
* Estrutura de diretórios;
* Monitoramento real.

---

# 14. Estado Atual do Projeto

HomeHub Gateway v0.1.0:

```
✓ Android + Termux configurado

✓ Projeto organizado

✓ MQTT Gateway operacional

✓ Autenticação MQTT

✓ Persistência MQTT

✓ CLI administrativa

✓ Logs

✓ Diagnóstico

✓ Identidade do dispositivo

✓ Storage Manager

✓ Cartão SD integrado
```

---

# 15. Próxima Versão

## HomeHub Gateway v0.2.0

Objetivo:

Criar a camada de serviços web.

Planejamento:

```
FastAPI

+

Servidor de arquivos

+

Dashboard Web

+

Gerenciamento pelo navegador
```

Recursos planejados:

* Upload de arquivos;
* Download;
* Navegação de diretórios;
* API REST;
* Interface web;
* Controle remoto.

---

# Release

## HomeHub Gateway v0.1.0

Primeira versão funcional da plataforma.

Marco:

**Gateway MQTT + Core Administrativo + Storage Foundation**
