# Changelog

Histórico de versões do **HomeHub Gateway**.

O HomeHub evolui de forma incremental, adicionando novos serviços e módulos para transformar um hardware de baixo custo em uma plataforma local de automação residencial, armazenamento e gerenciamento IoT.

---

# Próxima versão

# v0.5.0-dev

## Dashboard Web

Planejado:

* Criação da interface Web do HomeHub.
* Dashboard de monitoramento do sistema.
* Visualização do status dos serviços.
* Monitoramento do MQTT.
* Monitoramento do armazenamento.
* Gerenciamento visual de arquivos.
* Upload via navegador.
* Download via navegador.
* Interface preparada para futuras integrações.

---

# v0.4.0-dev

# Local Cloud / File Server

## Adicionado

Implementação da primeira versão do armazenamento privado local do HomeHub.

Principais funcionalidades:

* Criação do `FileManager`.
* Integração do gerenciamento de arquivos ao núcleo HomeHub.
* Registro do serviço Files no `ServiceRegistry`.
* Integração com o armazenamento externo SD Card.
* Criação da estrutura:

```
HomeHub/
├── files/
│   ├── documents
│   ├── images
│   ├── shared
│   └── videos
├── uploads
├── backups
├── database
└── media
```

---

## API de Arquivos

Criados novos endpoints REST:

### Informações do serviço

```
GET /api/files
```

Retorna informações do serviço de arquivos.

---

### Listagem de arquivos

```
GET /api/files/list
```

Permite consultar os arquivos disponíveis no armazenamento local.

---

### Upload

```
POST /api/files/upload
```

Permite enviar arquivos para o HomeHub.

Implementado:

* Recepção via `multipart/form-data`.
* Escrita no armazenamento SD Card.
* Bloqueio de arquivos duplicados.
* Validação de tamanho máximo.

---

### Download

```
GET /api/files/download/{filename}
```

Permite baixar arquivos armazenados localmente.

Implementado:

* Retorno utilizando `FileResponse`.
* Controle do caminho dos arquivos.
* Restrição ao diretório HomeHub.

---

### Exclusão

```
DELETE /api/files/{filename}
```

Permite remover arquivos armazenados.

---

## Segurança

Implementado:

* Proteção contra Path Traversal.
* Restrição dos arquivos ao diretório HomeHub/files.
* Normalização dos caminhos.
* Bloqueio de acesso fora do armazenamento permitido.
* Bloqueio de sobrescrita de arquivos existentes.
* Limite máximo de upload:

```
100 MB por arquivo
```

---

## Testes realizados

Validado:

* Upload via API.
* Download via API.
* Listagem de arquivos.
* Exclusão de arquivos.
* Bloqueio de arquivos duplicados.
* Teste contra caminhos externos.
* Teste de limite de tamanho.

Teste realizado:

```
Arquivo de 101 MB rejeitado corretamente.
```

---

# v0.3.1-dev

# Arquitetura e Organização do Core

## Adicionado

Reestruturação completa da arquitetura interna do HomeHub.

Implementado:

* Criação do núcleo central `HomeHub`.
* Organização modular da aplicação.
* Separação entre responsabilidades.

Nova estrutura:

```
core/
managers/
services/
registry/
schemas/
api/
models/
utils/
```

---

## Service Registry

Criado:

```
ServiceRegistry
```

Responsável pelo gerenciamento dos serviços internos.

Serviços registrados:

* Config.
* Version.
* Logger.
* System.
* MQTT.
* Storage.
* Files.
* Doctor.

---

## Core Managers

Implementados:

### ConfigManager

Responsável por:

* Carregamento das configurações.
* Centralização dos parâmetros do sistema.

---

### VersionManager

Responsável por:

* Controle da versão do HomeHub.
* Informações do software.

---

### HomeHubLogger

Implementado sistema inicial de logs.

---

## Melhorias arquiteturais

Realizado:

* Separação entre Core, Managers, API e Schemas.
* Padronização dos módulos.
* Organização seguindo responsabilidade única.
* Preparação para crescimento futuro.

---

# v0.3.0-dev

# Gateway REST API

## Adicionado

Criação da API REST utilizando FastAPI.

Implementado:

* Servidor HTTP.
* Rotas REST.
* Modelos Pydantic.
* Documentação automática OpenAPI.

---

## Endpoints

Criados:

```
GET /api/system
GET /api/storage
GET /api/mqtt
GET /api/health
GET /api/info
```

---

## Schemas

Implementados:

* `SystemInfo`
* `MQTTInfo`
* `StorageInfo`
* `HealthInfo`
* `InfoResponse`

---

## Informações fornecidas pela API

Sistema:

* Hardware.
* Versão.
* Hostname.
* Modo de operação.

MQTT:

* Status do broker.
* Configuração.
* Porta.

Storage:

* Tipo.
* Capacidade.
* Status.

Health:

* Estado geral dos serviços.

---

# v0.2.0-dev

# Core Services

## Adicionado

Implementação dos serviços fundamentais do HomeHub.

Criados:

* MQTT Manager.
* Storage Manager.
* Doctor Manager.

---

# MQTT Manager

Integração com Mosquitto MQTT Broker.

Implementado:

* Verificação do arquivo de configuração.
* Verificação do processo MQTT.
* Verificação da porta 1883.
* Status ONLINE/OFFLINE.

---

# Storage Manager

Implementado:

* Detecção do armazenamento externo.
* Integração com SD Card.
* Estrutura inicial do HomeHub Storage.

---

# Doctor Service

Criado sistema de diagnóstico.

Responsável por:

* Verificar serviços registrados.
* Informar estado geral do Gateway.
* Auxiliar testes de funcionamento.

---

# v0.1.0

# HomeHub Gateway Foundation

Primeira versão funcional do projeto.

## Adicionado

Fundação inicial do HomeHub.

Implementado:

* Criação do repositório Git.
* Estrutura inicial do projeto.
* Organização dos diretórios.
* Documentação inicial.
* Preparação do Gateway MQTT.

---

## MQTT Foundation

Implementado:

* Instalação do Mosquitto no Termux.
* Configuração do broker MQTT.
* Autenticação por usuário e senha.
* Persistência MQTT.
* Testes de publicação e inscrição.

Testado:

```
mosquitto_pub
mosquitto_sub
```

Comunicação MQTT validada.

---

## Hardware inicial

Ambiente:

* TV Box RK3066.
* Android + Termux.
* Rede local.
* Armazenamento SD Card.

---

# Histórico do Projeto

O HomeHub iniciou como um Gateway MQTT utilizando uma TV Box antiga e evoluiu para uma plataforma local contendo:

* Gateway IoT.
* API REST.
* Gerenciamento de serviços.
* Armazenamento local.
* Base para nuvem privada doméstica.
* Futuro Dashboard Web.
