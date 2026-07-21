# HomeHub Architecture

## Visão Geral

O HomeHub é uma plataforma modular de automação residencial desenvolvida em Python, projetada para executar integralmente na rede local utilizando hardware de baixo custo, como TV Boxes Android.

Sua arquitetura é baseada em serviços independentes registrados em um Service Registry central, permitindo baixo acoplamento, alta organização e facilidade para expansão.

O núcleo da aplicação é representado pela classe `HomeHub`, responsável por inicializar todos os componentes e disponibilizá-los para a API REST.

---

# Arquitetura Geral

```
                Clientes

        Navegador
            │
        Aplicativo
            │
           ESP32
            │
            ▼

      FastAPI REST API
            │
            ▼

         HomeHub Core
            │
            ▼

     Service Registry
            │
 ┌──────────┼─────────────┐
 │          │             │
 ▼          ▼             ▼

Config   Version      Logger

System   MQTT         Storage

Files    Doctor

            │
            ▼

     SD Card Storage

            │
            ▼

     Mosquitto Broker
```

---

# Camadas da Aplicação

A arquitetura está dividida em camadas independentes.

## API

Responsável por disponibilizar os endpoints REST.

```
app/api/routes
```

Atualmente contém:

- Health
- MQTT
- Storage
- System
- Info
- Files

---

## Core

Responsável pelos componentes fundamentais da aplicação.

```
app/core
```

Componentes:

- ConfigManager
- VersionManager
- HomeHubLogger

---

## Managers

Implementam as regras de negócio da aplicação.

```
app/managers
```

Atualmente:

- SystemManager
- MQTTManager
- StorageManager
- FileManager
- DoctorManager

---

## Registry

Centraliza todos os serviços.

```
app/registry
```

O Service Registry elimina dependências diretas entre módulos e facilita futuras expansões.

---

## Schemas

Define todos os modelos Pydantic utilizados pela API.

```
app/schemas
```

---

## Services

Camada destinada aos serviços reutilizáveis da aplicação.

Atualmente possui apenas serviços básicos, mas será expandida nas próximas versões.

---

# Fluxo de Inicialização

Durante a inicialização do servidor ocorre a seguinte sequência:

```
HomeHub()

↓

ConfigManager

↓

Logger

↓

VersionManager

↓

SystemManager

↓

StorageManager

↓

FileManager

↓

MQTTManager

↓

ServiceRegistry

↓

DoctorManager

↓

FastAPI
```

Todos os serviços ficam registrados no Service Registry.

---

# Fluxo de Upload

```
Cliente

↓

POST /api/files/upload

↓

FastAPI

↓

Files Route

↓

FileManager

↓

StorageManager

↓

SD Card

↓

Resposta JSON
```

---

# Fluxo de Download

```
Cliente

↓

GET /api/files/download/{arquivo}

↓

FastAPI

↓

Files Route

↓

FileManager

↓

SD Card

↓

FileResponse
```

---

# Organização do Projeto

```
HomeHub/

├── api/
│   └── app/
│
│       ├── api/
│       ├── core/
│       ├── managers/
│       ├── registry/
│       ├── schemas/
│       ├── services/
│       ├── models/
│       ├── utils/
│       └── homehub.py
│
├── configs/
├── database/
├── dashboard/
├── docs/
├── logs/
├── scripts/
├── services/
├── storage/
└── tests/
```

---

# Componentes Atuais

| Componente | Responsabilidade |
|------------|------------------|
| HomeHub | Núcleo da aplicação |
| ConfigManager | Configurações |
| VersionManager | Controle de versão |
| HomeHubLogger | Sistema de logs |
| ServiceRegistry | Registro dos serviços |
| SystemManager | Informações do sistema |
| MQTTManager | Gerenciamento do broker MQTT |
| StorageManager | Gerenciamento do armazenamento |
| FileManager | Upload, download e exclusão de arquivos |
| DoctorManager | Verificação de integridade do sistema |

---

# Tecnologias Utilizadas

- Python 3
- FastAPI
- Pydantic
- Mosquitto MQTT
- SQLite (planejado)
- Android + Termux
- SD Card como armazenamento permanente

---

# Evolução da Arquitetura

A arquitetura foi projetada para suportar novos módulos sem necessidade de grandes alterações.

Os próximos componentes previstos são:

- Dashboard Web
- SQLite Database
- Autenticação de usuários
- Device Manager (ESP32)
- Automation Engine
- Scheduler
- Notification Manager
- Backup Manager
- Local Cloud
- Plugin System

---

# Princípios da Arquitetura

A arquitetura do HomeHub segue alguns princípios fundamentais:

- Responsabilidade única por componente.
- Baixo acoplamento entre módulos.
- Facilidade de manutenção.
- Expansão incremental.
- Execução totalmente local.
- Reutilização de hardware de baixo custo.
- Simplicidade na implementação.
