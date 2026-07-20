# HomeHub
## Arquitetura do Sistema

**Versão:** 0.3.1-dev

---

# 1. Introdução

O HomeHub é um gateway de automação residencial desenvolvido para funcionar em hardware de baixo custo, oferecendo serviços locais para integração de dispositivos IoT, armazenamento de arquivos e gerenciamento da residência.

O projeto foi projetado para operar continuamente na rede local, priorizando simplicidade, baixo consumo de recursos e arquitetura modular.

Sua implementação utiliza Python, FastAPI, Mosquitto MQTT e armazenamento local em cartão SD, executando sobre um TV Box Android utilizando Termux.

---

# 2. Objetivos

O HomeHub possui os seguintes objetivos:

- funcionar continuamente (24x7);
- operar completamente na rede local;
- reduzir dependência de serviços em nuvem;
- integrar dispositivos IoT utilizando MQTT;
- disponibilizar uma API REST para integração;
- oferecer armazenamento local para arquivos;
- permitir crescimento através de módulos independentes;
- manter baixo consumo de memória e processamento.

---	

# 3. Visão Geral da Arquitetura

O HomeHub foi projetado seguindo uma arquitetura modular.

Cada componente possui uma responsabilidade específica, reduzindo o acoplamento entre os módulos e facilitando a manutenção do sistema.

A aplicação é composta pelos seguintes blocos principais:

- API REST (FastAPI)
- Managers
- Service Registry
- Arquivos de configuração
- Serviços locais (Mosquitto, Storage e Sistema)
- Schemas Pydantic

Fluxo geral da aplicação:

```text
                    Cliente

                       │
                       ▼

                 FastAPI (API)

                       │
                       ▼

                 Route (Endpoint)

                       │
                       ▼

                  Manager

                       │
      ┌────────────────┼────────────────┐
      ▼                ▼                ▼

 ConfigManager   ServiceRegistry   VersionManager

      │                │                │
      └────────────────┼────────────────┘
                       │
                       ▼

               Serviços do HomeHub

             MQTT   Storage   System

                       │
                       ▼

                Resposta JSON
```

Essa separação permite que a camada HTTP permaneça simples, enquanto toda a lógica de negócio permanece concentrada nos managers.


# 4. Estrutura do Projeto

O HomeHub está organizado em módulos independentes.

Cada diretório possui uma responsabilidade específica, facilitando a manutenção, expansão e organização do projeto.

Estrutura principal:

```text
Homehub/

├── api/
├── configs/
├── dashboard/
├── database/
├── docs/
├── logs/
├── scripts/
├── services/
├── storage/
└── tests/
```

## api/

Contém todo o código-fonte da aplicação.

Inclui a API REST, managers, schemas, serviços internos e componentes do núcleo do sistema.

---

## configs/

Armazena todos os arquivos de configuração utilizados pelo HomeHub.

Exemplos:

- device.conf
- storage.conf
- system.conf
- version.conf
- mosquitto/

Nenhum valor de configuração permanente deve ficar fixo no código.

---

## dashboard/

Reservado para a interface web do HomeHub.

Será responsável pelo gerenciamento do sistema através do navegador.

---

## database/

Diretório destinado aos bancos de dados utilizados pelo sistema.

---

## docs/

Contém toda a documentação oficial do projeto.

Inclui arquitetura, roadmap, documentação da API, histórico de versões e decisões de projeto.

---

## logs/

Armazena os arquivos de log do sistema.

Exemplos:

- homehub.log
- mqtt.log
- system.log

---

## scripts/

Contém scripts auxiliares para administração do HomeHub.

Exemplos:

- start.sh
- stop.sh
- restart.sh
- diagnose.sh
- version.sh

---

## services/

Reservado para serviços independentes que poderão ser adicionados futuramente.

---

## storage/

Diretório utilizado para armazenamento persistente de dados.

Inclui bancos de dados, arquivos enviados pelos usuários, backups e demais recursos locais.

---

## tests/

Contém os testes automatizados do projeto.

Será utilizado para validar o funcionamento dos componentes do HomeHub durante seu desenvolvimento.


# 5. Componentes Principais

Os componentes principais do HomeHub formam o núcleo da aplicação.

Cada componente possui uma responsabilidade única e bem definida, reduzindo o acoplamento e facilitando a manutenção do sistema.

O núcleo atual é composto por:

- ConfigManager
- VersionManager
- HomeHubLogger
- ServiceRegistry
- SystemManager
- MQTTManager
- StorageManager
- DoctorManager


## ConfigManager

### Responsabilidade

O ConfigManager é responsável por localizar e carregar os arquivos de configuração do HomeHub.

Ele centraliza o acesso ao diretório `configs/`, evitando que outros componentes precisem conhecer a localização física dos arquivos.

---

### Localização

```
app/core/config.py
```

---

### Dependências

- configparser
- os

---

### Métodos Públicos

#### load(filename)

Carrega um arquivo de configuração localizado no diretório `configs/` e retorna um objeto `ConfigParser`.

Exemplo:

```python
config = ConfigManager()

device = config.load("device.conf")

mqtt = config.load("mqtt.conf")
```

---

### Fluxo de Funcionamento

```text
Manager
    │
    ▼

ConfigManager

    │
    ▼

configs/*.conf

    │
    ▼

ConfigParser

    │
    ▼

Manager
```

---

### Responsabilidades

O ConfigManager deve:

- localizar arquivos de configuração;
- carregar arquivos `.conf`;
- retornar um objeto ConfigParser para leitura dos dados.

---

### O que não deve fazer

O ConfigManager não deve:

- validar regras de negócio;
- interpretar configurações;
- modificar arquivos automaticamente;
- conhecer outros managers.

Sua única responsabilidade é fornecer acesso aos arquivos de configuração.

---

### Boas Práticas

Todo acesso aos arquivos de configuração deve ocorrer através do ConfigManager.

Nenhum componente deve montar caminhos manualmente para acessar arquivos da pasta `configs/`.


## VersionManager

### Responsabilidade

O VersionManager é responsável por centralizar as informações de versão do HomeHub.

Ele é a única fonte de informação sobre:

- nome do software;
- versão atual do sistema;
- modo de operação;
- versão da API.

Nenhum outro componente deve acessar diretamente o arquivo `version.conf` para obter informações de versão.

---

### Localização

```
app/core/version.py
```

---

### Dependências

- ConfigManager

O VersionManager utiliza o ConfigManager para carregar o arquivo:

```
configs/version.conf
```

---

### Métodos Públicos

## info()

Retorna as informações de versão do HomeHub em formato de dicionário.

Exemplo de retorno:

```json
{
    "software": "HomeHub Gateway",
    "version": "0.3.1-dev",
    "mode": "MQTT Gateway",
    "api_version": "1.0"
}
```

---

### Fluxo de Funcionamento

```text
             ConfigManager

                  │

                  ▼

          version.conf

                  │

                  ▼

          VersionManager

                  │

                  ▼

        Informações de versão

                  │

                  ▼

        SystemManager / API
```

---

### Estrutura de Configuração

O VersionManager utiliza o arquivo:

```
configs/version.conf
```

Com a seguinte estrutura:

```ini
[version]

software=HomeHub Gateway

version=0.3.1-dev

mode=MQTT Gateway


[api]

version=1.0
```

---

### Responsabilidades

O VersionManager deve:

- carregar o arquivo de versão;
- interpretar as informações de software;
- fornecer uma interface única para consulta de versão;
- separar versão do software e versão da API.

---

### O que não deve fazer

O VersionManager não deve:

- controlar atualizações;
- modificar arquivos de versão;
- conhecer regras de hardware;
- gerenciar outros componentes.

---

### Decisão Arquitetural

A partir da versão 0.3.1-dev, o HomeHub adota o VersionManager como fonte única de verdade para informações de versão.

Antes desta alteração, componentes como o SystemManager acessavam diretamente o arquivo `version.conf`.

Após a refatoração:

```text
SystemManager
       │
       ▼

VersionManager
       │
       ▼

version.conf
```

Essa abordagem reduz duplicação e mantém a responsabilidade de versionamento centralizada.


## HomeHubLogger

### Responsabilidade

O HomeHubLogger é responsável pelo gerenciamento centralizado dos registros de eventos do HomeHub.

Ele fornece uma interface única de logging para todos os componentes da aplicação, evitando o uso direto da biblioteca de logging dentro dos módulos do sistema.

---

### Localização

```
app/core/logger.py
```

---

### Dependências

- logging
- os

---

### Arquivo de Log

O HomeHubLogger utiliza o arquivo:

```
logs/homehub.log
```

Formato dos registros:

```
data | nível | mensagem
```

Exemplo:

```
2026-07-20 16:30:00 | INFO | HomeHub Core initialized
```

---

### Métodos Públicos

## info(message)

Registra uma mensagem informativa.

Exemplo:

```python
logger.info("MQTT iniciado")
```

---

## error(message)

Registra uma mensagem de erro.

Exemplo:

```python
logger.error("Falha ao conectar MQTT")
```

---

## warning(message)

Registra uma mensagem de alerta.

Exemplo:

```python
logger.warning("Espaço de armazenamento reduzido")
```

---

### Fluxo de Funcionamento

```text
             Componente

                 │

                 ▼

          HomeHubLogger

                 │

                 ▼

          logging Python

                 │

                 ▼

        logs/homehub.log
```

---

### Responsabilidades

O HomeHubLogger deve:

- criar o diretório de logs quando necessário;
- configurar o sistema de logging;
- registrar informações, erros e alertas;
- fornecer uma interface simples para os demais módulos.

---

### O que não deve fazer

O HomeHubLogger não deve:

- interpretar erros;
- tomar decisões de negócio;
- controlar outros componentes;
- substituir sistemas de monitoramento externos.

---

### Boas Práticas

Todos os componentes do HomeHub devem utilizar o HomeHubLogger para registrar eventos.

Evitar:

```python
print("MQTT conectado")
```

Preferir:

```python
logger.info("MQTT conectado")
```

Essa padronização permite futuramente integrar logs com:

- Dashboard Web;
- armazenamento histórico;
- diagnóstico remoto;
- relatórios do sistema.


## ServiceRegistry

### Responsabilidade

O ServiceRegistry é responsável por armazenar e disponibilizar os serviços internos do HomeHub.

Ele funciona como um ponto central de registro de componentes, permitindo que diferentes partes da aplicação compartilhem instâncias sem criar dependências diretas entre elas.

---

### Localização

```
app/registry/service_registry.py
```

---

### Dependências

O ServiceRegistry não possui dependências externas.

Ele utiliza apenas estruturas nativas do Python.

---

### Estrutura Interna

Os serviços são armazenados em um dicionário interno:

```python
self._services = {}
```

Cada serviço possui um identificador único.

Exemplo:

```python
{
    "config": ConfigManager,
    "version": VersionManager,
    "mqtt": MQTTManager,
    "storage": StorageManager
}
```

---

### Métodos Públicos

## register(name, service)

Registra um novo serviço no container.

Exemplo:

```python
registry.register(
    "mqtt",
    mqtt_manager
)
```

---

## get(name)

Recupera um serviço registrado.

Exemplo:

```python
mqtt = registry.get("mqtt")
```

Caso o serviço não exista, retorna `None`.

---

## all()

Retorna todos os serviços registrados.

Exemplo:

```python
services = registry.all()
```

---

### Fluxo de Funcionamento

```text
             HomeHub

                │

                ▼

        ServiceRegistry

                │

     ┌──────────┼──────────┐

     ▼          ▼          ▼

 Config      MQTT      Storage

                │

                ▼

        Componentes do sistema
```

---

### Serviços Atuais Registrados

Durante a inicialização do HomeHub são registrados:

```text
config
version
logger
system
mqtt
storage
doctor
```

---

### Responsabilidades

O ServiceRegistry deve:

- armazenar instâncias dos serviços;
- fornecer acesso centralizado aos componentes;
- evitar criação duplicada de objetos;
- facilitar a comunicação entre módulos.

---

### O que não deve fazer

O ServiceRegistry não deve:

- criar serviços automaticamente;
- executar lógica de negócio;
- controlar ciclo de vida complexo dos componentes;
- substituir um sistema de injeção de dependência completo.

---

### Decisão Arquitetural

O HomeHub utiliza o ServiceRegistry como mecanismo simples de compartilhamento de serviços.

A criação dos componentes permanece sob responsabilidade da classe principal:

```
HomeHub
```

O Registry apenas armazena e disponibiliza os objetos já inicializados.

Fluxo:

```text
HomeHub

   │
   ├── cria ConfigManager
   ├── cria VersionManager
   ├── cria MQTTManager
   ├── cria StorageManager
   │
   ▼

ServiceRegistry

   │
   ▼

Componentes utilizam serviços registrados
```

Essa abordagem mantém o sistema modular e preparado para futuras expansões.



## SystemManager

### Responsabilidade

O SystemManager é responsável por fornecer informações sobre a identidade e características do equipamento HomeHub.

Ele reúne informações do hardware, dispositivo e versão do software para disponibilizar uma visão geral do gateway.

---

### Localização

```
app/managers/system_manager.py
```

---

### Dependências

O SystemManager utiliza:

- ConfigManager
- VersionManager
- socket

---

### Arquivos utilizados

## device.conf

Localizado em:

```
configs/device.conf
```

Contém informações do equipamento:

Exemplo:

```ini
[device]

name=HomeHub Casa

id=HH-RK3066-001

hardware=RK3066
```

---

### Métodos Públicos

## info()

Retorna as informações gerais do sistema.

Exemplo:

```json
{
    "device": "HomeHub Casa",
    "id": "HH-RK3066-001",
    "hardware": "RK3066",
    "software": "HomeHub Gateway",
    "version": "0.3.1-dev",
    "mode": "MQTT Gateway",
    "api_version": "1.0",
    "hostname": "localhost"
}
```

---

### Fluxo de Funcionamento

```text
              API

               │

               ▼

        SystemManager

               │

       ┌───────┴────────┐

       ▼                ▼

 ConfigManager    VersionManager

       │                │

       ▼                ▼

 device.conf     version.conf

               │

               ▼

          Informações do sistema
```

---

### Responsabilidades

O SystemManager deve:

- fornecer informações do dispositivo;
- identificar o hardware utilizado;
- integrar informações de versão;
- retornar uma visão consolidada do sistema.

---

### O que não deve fazer

O SystemManager não deve:

- controlar hardware;
- iniciar serviços;
- alterar configurações;
- gerenciar MQTT;
- gerenciar armazenamento.

Essas responsabilidades pertencem aos seus respectivos managers.

---

### Decisão Arquitetural

O SystemManager utiliza outros componentes especializados para obter informações.

Exemplo:

Antes:

```text
SystemManager

      │

      ▼

version.conf
```

Depois:

```text
SystemManager

      │

      ▼

VersionManager

      │

      ▼

version.conf
```

Essa abordagem mantém cada componente responsável pelo seu próprio domínio e reduz acoplamento entre módulos.



## MQTTManager

### Responsabilidade

O MQTTManager é responsável pelo monitoramento do serviço MQTT utilizado pelo HomeHub.

Ele verifica a disponibilidade do broker Mosquitto e fornece informações sobre o estado atual da comunicação MQTT.

O MQTT é o protocolo principal utilizado para comunicação com dispositivos IoT do HomeHub.

---

### Localização

```
app/managers/mqtt_manager.py
```

---

### Dependências

O MQTTManager utiliza:

- os
- subprocess
- ConfigManager

---

### Serviço Monitorado

O broker utilizado pelo HomeHub é:

```
Mosquitto MQTT
```

Configuração:

```
configs/mosquitto/mosquitto.conf
```

Porta padrão:

```
1883
```

---

### Métodos Internos

## _process_running()

Verifica se o processo Mosquitto está em execução.

Utiliza:

```bash
pgrep -f mosquitto
```

Retorno:

```text
True  → processo encontrado

False → processo não encontrado
```

---

## _port_listening()

Verifica se existe um serviço escutando a porta MQTT.

Utiliza:

```bash
ss -tln
```

Procura:

```
:1883
```

Retorno:

```text
True  → porta disponível

False → porta não encontrada
```

---

### Métodos Públicos

## info()

Retorna o estado completo do serviço MQTT.

Exemplo:

```json
{
    "broker": "Mosquitto",
    "config": true,
    "process": true,
    "port": true,
    "status": "ONLINE"
}
```

---

## status()

Retorna somente o estado atual:

Exemplo:

```json
{
    "status": "ONLINE"
}
```

---

### Fluxo de Funcionamento

```text
                 API

                  │

                  ▼

             MQTTManager

                  │

       ┌──────────┴──────────┐

       ▼                     ▼

mosquitto.conf        Processo Mosquitto

       │                     │

       └──────────┬──────────┘

                  ▼

           Status MQTT

        ONLINE / OFFLINE
```

---

### Responsabilidades

O MQTTManager deve:

- verificar existência da configuração MQTT;
- verificar processo Mosquitto;
- verificar porta MQTT;
- informar disponibilidade do broker.

---

### O que não deve fazer

O MQTTManager não deve:

- criar tópicos MQTT;
- controlar dispositivos;
- publicar mensagens;
- assinar tópicos;
- substituir o broker Mosquitto.

Essas responsabilidades pertencem a camadas futuras de comunicação IoT.

---

### Evolução Futura

Atualmente o MQTTManager atua como monitor de saúde do broker.

Futuramente poderão existir componentes especializados:

```text
MQTTManager

      │

      ├── MQTTClient

      │        ├── publish()

      │        └── subscribe()

      │

      └── DeviceManager
```

Essa separação permitirá que o HomeHub evolua de um gateway MQTT para uma plataforma completa de automação residencial.

---

### Decisão Arquitetural

O HomeHub separa:

```
Monitoramento
```

de

```
Comunicação
```

O MQTTManager verifica se o serviço está saudável, enquanto componentes futuros serão responsáveis pela troca de mensagens com dispositivos.



## StorageManager

### Responsabilidade

O StorageManager é responsável pelo gerenciamento da camada de armazenamento físico do HomeHub.

Ele identifica o local onde os dados persistentes serão armazenados e verifica a disponibilidade do armazenamento.

---

### Localização

```
app/managers/storage_manager.py
```

---

### Dependências

O StorageManager utiliza:

- os
- subprocess
- glob
- ConfigManager

---

### Arquivo de Configuração

Utiliza:

```
configs/storage.conf
```

Exemplo:

```ini
[storage]

name=HomeHub Storage

type=SDCARD

capacity=250GB

path=/data/data/com.termux/files/home/storage/external-1/HomeHub
```

---

### Métodos Públicos

## configured_path()

Retorna o caminho configurado manualmente para o armazenamento.

Fonte:

```
storage.conf
```

---

## discover_storage()

Procura automaticamente dispositivos de armazenamento disponíveis no Termux.

Busca:

```
~/storage/external-*
```

e verifica a existência do diretório:

```
HomeHub/
```

---

## resolve_path()

Resolve o caminho final do armazenamento.

Ordem de prioridade:

```text
1 - Caminho configurado

        ↓

2 - Descoberta automática

        ↓

3 - Nenhum armazenamento encontrado
```

---

## disk_info(path)

Obtém informações do disco utilizando:

```bash
df -h
```

Retorna:

```json
{
    "total": "250G",
    "used": "10G",
    "free": "240G",
    "usage": "5%"
}
```

---

## info()

Retorna as informações completas do armazenamento.

Exemplo:

```json
{
    "name": "HomeHub Storage",
    "type": "SDCARD",
    "capacity": "250GB",
    "path": "/storage/HomeHub",
    "status": "ONLINE",
    "total": "250G",
    "used": "10G",
    "free": "240G",
    "usage": "5%"
}
```

---

## status()

Retorna apenas o estado atual:

```json
{
    "status":"ONLINE"
}
```

---

### Fluxo de Funcionamento

```text
              API

               │

               ▼

        StorageManager

               │

       ┌───────┴────────┐

       ▼                ▼

 storage.conf     SD Card / Storage

       │                │

       └───────┬────────┘

               ▼

       Informações do armazenamento
```

---

### Responsabilidades

O StorageManager deve:

- carregar configuração de armazenamento;
- localizar o armazenamento físico;
- verificar disponibilidade;
- informar capacidade do disco.

---

### O que não deve fazer

O StorageManager não deve:

- gerenciar arquivos;
- realizar upload/download;
- controlar permissões;
- fornecer interface web.

Essas responsabilidades pertencem a componentes futuros.

---

### Evolução Futura

A arquitetura atual prepara a criação de uma camada de arquivos:

```text
StorageManager

        │

        ▼

Local Storage

        │

        ▼

FileManager

        │

        ├── Upload

        ├── Download

        ├── Backup

        └── Compartilhamento
```

---

### Decisão Arquitetural

O HomeHub separa:

```
Armazenamento físico
```

de

```
Gerenciamento de arquivos
```

O StorageManager conhece o dispositivo de armazenamento, mas não conhece os dados armazenados nele.


## DoctorManager

### Responsabilidade

O DoctorManager é responsável pelo diagnóstico de saúde dos componentes internos do HomeHub.

Ele verifica se os serviços essenciais estão disponíveis e retorna um resumo do estado geral do sistema.

---

### Localização

```
app/managers/doctor_manager.py
```

---

### Dependências

O DoctorManager utiliza:

- ServiceRegistry

---

### Métodos Públicos

## check()

Executa uma verificação dos principais componentes do HomeHub.

Retorna o estado de:

- Configuração;
- MQTT;
- Storage;
- Sistema.

Exemplo:

```json
{
    "config": "OK",
    "mqtt": "ONLINE",
    "storage": "ONLINE",
    "system": "OK"
}
```

---

### Fluxo de Funcionamento

```text
                 API

                  │

                  ▼

            DoctorManager

                  │

                  ▼

          ServiceRegistry

        ┌─────────┼─────────┐

        ▼         ▼         ▼

    Config      MQTT    Storage

                  │

                  ▼

           Resultado Health
```

---

### Componentes Verificados

## Config

Verifica se o ConfigManager está registrado.

Resultado:

```
OK
```

ou

```
ERROR
```

---

## MQTT

Utiliza:

```python
mqtt.status()
```

Resultado:

```
ONLINE
```

ou

```
OFFLINE
```

---

## Storage

Utiliza:

```python
storage.status()
```

Resultado:

```
ONLINE
```

ou

```
NOT_MOUNTED
```

---

## System

Verifica a existência do SystemManager.

Resultado:

```
OK
```

ou

```
ERROR
```

---

### Responsabilidades

O DoctorManager deve:

- verificar disponibilidade dos serviços;
- consolidar informações de saúde;
- fornecer diagnóstico simples do sistema.

---

### O que não deve fazer

O DoctorManager não deve:

- corrigir problemas automaticamente;
- iniciar serviços;
- reiniciar componentes;
- alterar configurações.

Ele é um componente de diagnóstico, não de gerenciamento.

---

### Decisão Arquitetural

O DoctorManager utiliza o ServiceRegistry para acessar os componentes do sistema.

Isso evita dependências diretas:

Antes:

```
DoctorManager

    |
    ├── MQTTManager
    ├── StorageManager
    └── SystemManager
```

Depois:

```
DoctorManager

    |
    ▼

ServiceRegistry

    |
    ├── MQTTManager
    ├── StorageManager
    └── SystemManager
```

Essa abordagem mantém o diagnóstico desacoplado dos componentes monitorados.

---

### Evolução Futura

O DoctorManager poderá evoluir para um sistema de diagnóstico mais completo:

```text
DoctorManager

      │

      ├── CPU

      ├── Memória

      ├── Temperatura

      ├── Disco

      ├── Rede

      └── Serviços
```

Possibilitando futuramente:

- página de diagnóstico no Dashboard;
- relatórios de saúde;
- alertas automáticos.


# 6. Fluxo de Inicialização do HomeHub

## Visão Geral

O processo de inicialização do HomeHub é responsável por criar o ambiente interno do Gateway, carregar configurações, inicializar serviços e disponibilizar a API Web.

O fluxo inicia através do módulo:

```
app/web.py
```

---

# Entrada da Aplicação

A execução do HomeHub ocorre através de:

```bash
python -m app.web
```

O módulo `web.py` possui como responsabilidade:

- criar a aplicação FastAPI;
- iniciar o servidor Uvicorn quando executado diretamente.

Fluxo:

```text
python -m app.web

        │

        ▼

     web.py

        │

        ▼

 create_server()
```

---

# Criação do Servidor

A função:

```
create_server()
```

está localizada em:

```
app/server.py
```

Responsabilidades:

- criar a instância FastAPI;
- criar o núcleo HomeHub;
- registrar as rotas da API.

Fluxo:

```text
create_server()

        │

        ▼

    FastAPI()

        │

        ▼

    HomeHub()

        │

        ▼

    Rotas API
```

---

# Inicialização do Núcleo HomeHub

A classe principal:

```
app/homehub.py
```

é responsável por criar todos os componentes internos.

Ordem atual de inicialização:

```text
HomeHub()

   │

   ├── ConfigManager

   │

   ├── HomeHubLogger

   │

   ├── VersionManager

   │

   ├── SystemManager

   │

   ├── StorageManager

   │

   ├── MQTTManager

   │

   ├── ServiceRegistry

   │

   └── DoctorManager
```

---

# Inicialização dos Serviços

## ConfigManager

Primeiro serviço criado.

Responsável por fornecer acesso aos arquivos:

```
configs/
```

---

## HomeHubLogger

Inicializa o sistema de logs.

Arquivo:

```
logs/homehub.log
```

Primeiro registro:

```
HomeHub Core initialized
```

---

## VersionManager

Carrega:

```
configs/version.conf
```

Fornecendo:

- software;
- versão;
- modo;
- versão da API.

---

## SystemManager

Recebe:

- ConfigManager;
- VersionManager.

Responsável pela identidade do equipamento.

---

## StorageManager

Carrega:

```
configs/storage.conf
```

Responsável pelo armazenamento local.

---

## MQTTManager

Inicializa o monitoramento do broker:

```
Mosquitto MQTT
```

---

# Registro dos Serviços

Após a criação dos componentes, eles são registrados no:

```
ServiceRegistry
```

Serviços atuais:

```text
config

version

logger

system

mqtt

storage
```

Fluxo:

```text
Componentes criados

        │

        ▼

ServiceRegistry

        │

        ▼

Serviços disponíveis para aplicação
```

---

# Inicialização do DoctorManager

Após o registro dos serviços:

```python
DoctorManager(registry)
```

é criado.

Ele recebe acesso ao Registry e consegue consultar a saúde dos componentes.

Depois também é registrado:

```
doctor
```

---

# Registro das Rotas API

Após o HomeHub estar inicializado, o servidor registra as rotas:

```
/api/health

/api/system

/api/storage

/api/mqtt

/api/info
```

Cada rota recebe a mesma instância:

```
hub
```

permitindo acesso aos serviços internos.

---

# Inicialização do Servidor Web

Após todas as etapas:

```python
uvicorn.run()
```

inicia o servidor.

Configuração atual:

```
host: 0.0.0.0

port: 8000
```

Fluxo final:

```text
              Uvicorn

                 │

                 ▼

             FastAPI

                 │

                 ▼

          HomeHub Gateway API
```

---

# Fluxo Completo

```text
python -m app.web

        │

        ▼

      web.py

        │

        ▼

 create_server()

        │

        ▼

     HomeHub()

        │

        ├── Config

        ├── Logger

        ├── Version

        ├── System

        ├── Storage

        ├── MQTT

        ├── Registry

        └── Doctor

        │

        ▼

  Registro das rotas

        │

        ▼

  Uvicorn inicia

        │

        ▼

 HomeHub Gateway Online
```

---

# Decisão Arquitetural

A inicialização do HomeHub é centralizada na classe:

```
HomeHub
```

Ela funciona como o ponto de composição do sistema.

Os componentes individuais permanecem independentes, enquanto a classe HomeHub define:

- quais serviços existem;
- ordem de criação;
- dependências;
- registro dos módulos.

Essa abordagem facilita a expansão futura do Gateway.



# 7. Arquitetura da API REST

## Visão Geral

A API REST do HomeHub é a camada responsável pela comunicação entre o Gateway e clientes externos.

Ela permite que aplicações como:

- Dashboard Web;
- aplicativos móveis;
- ferramentas de monitoramento;
- integrações externas;

consultem o estado do sistema.

---

## Tecnologia

A API utiliza:

```
FastAPI
```

Servidor:

```
Uvicorn
```

Porta padrão:

```
8000
```

---

# Estrutura da API

A organização das rotas está localizada em:

```
app/api/routes/
```

Estrutura:

```
routes/

├── health.py

├── system.py

├── mqtt.py

├── storage.py

└── info.py
```

Cada módulo representa um domínio específico do HomeHub.

---

# Registro das Rotas

As rotas são registradas em:

```
app/server.py
```

Durante a criação do servidor:

```python
app.include_router()
```

Cada rota recebe a mesma instância:

```
HomeHub
```

permitindo acesso aos serviços internos.

---

# Endpoint Root

## GET /

Retorna informações básicas da aplicação.

Exemplo:

```json
{
    "name":"HomeHub Gateway",
    "version":"0.3.0-dev",
    "status":"online"
}
```

---

# Endpoint Health

## GET /api/health

Responsável pelo diagnóstico geral do sistema.

Local:

```
routes/health.py
```

Utiliza:

```
DoctorManager
```

Fluxo:

```
API

 |

 ▼

Health Route

 |

 ▼

DoctorManager

 |

 ▼

ServiceRegistry
```

---

Resposta:

```json
{
    "config":"OK",
    "mqtt":"ONLINE",
    "storage":"ONLINE",
    "system":"OK",
    "status":"HEALTHY"
}
```

Estados possíveis:

```
HEALTHY
```

Sistema funcionando corretamente.

ou:

```
DEGRADED
```

Algum componente apresenta problema.

---

# Endpoint System

## GET /api/system

Retorna informações do equipamento.

Utiliza:

```
SystemManager
```

Exemplo:

```json
{
    "device":"HomeHub Casa",
    "id":"HH-RK3066-001",
    "hardware":"RK3066",
    "software":"HomeHub Gateway",
    "version":"0.3.1-dev",
    "mode":"MQTT Gateway",
    "api_version":"1.0",
    "hostname":"localhost"
}
```

---

# Endpoint MQTT

## GET /api/mqtt

Retorna informações do broker MQTT.

Utiliza:

```
MQTTManager
```

Exemplo:

```json
{
    "broker":"Mosquitto",
    "config":true,
    "process":true,
    "port":true,
    "status":"ONLINE"
}
```

---

# Endpoint Storage

## GET /api/storage

Retorna informações do armazenamento local.

Utiliza:

```
StorageManager
```

Exemplo:

```json
{
    "name":"HomeHub Storage",
    "type":"SDCARD",
    "capacity":"250GB",
    "status":"ONLINE"
}
```

---

# Endpoint Info

## GET /api/info

Endpoint consolidado do HomeHub.

Criado para reduzir múltiplas consultas do cliente.

Antes:

```
Dashboard

/api/system

/api/mqtt

/api/storage

/api/health
```

Depois:

```
Dashboard

/api/info
```

---

Resposta:

```json
{
    "system":{},
    "mqtt":{},
    "storage":{},
    "health":{}
}
```

---

# Schemas da API

A API iniciou a utilização de modelos Pydantic.

Local:

```
app/schemas/
```

Objetivo:

- validação automática;
- documentação Swagger;
- contratos claros de resposta.

---

# Swagger / OpenAPI

A documentação automática está disponível em:

```
http://IP_DO_HOMEHUB:8000/docs
```

O FastAPI gera automaticamente:

- documentação dos endpoints;
- modelos de resposta;
- testes interativos.

---

# Padrão de Arquitetura

A API segue o fluxo:

```
Cliente

  |

  ▼

FastAPI Route

  |

  ▼

Manager

  |

  ▼

Core / Sistema
```

Exemplo:

```
GET /api/mqtt

        |

        ▼

mqtt.py

        |

        ▼

MQTTManager

        |

        ▼

Mosquitto
```

---

# Evolução Futura

A API está preparada para receber novos módulos:

```
/api/files

/api/devices

/api/automation

/api/users

/api/settings
```

Mantendo o mesmo padrão:

```
Route

   |

Manager

   |

Service
```

---

# Decisão Arquitetural

A API não contém lógica de negócio.

Sua responsabilidade é:

- receber requisições;
- chamar os componentes corretos;
- retornar respostas.

As regras do sistema permanecem dentro dos Managers.


# 8. Modelo de Dados e Schemas da API

## Visão Geral

Os Schemas da API definem os contratos de dados utilizados pelo HomeHub Gateway.

Eles são responsáveis por:

- validar respostas da API;
- documentar estruturas JSON;
- garantir consistência entre backend e clientes;
- fornecer modelos para o Swagger/OpenAPI.

---

## Localização

Os schemas estão localizados em:

```
app/schemas/
```

Estrutura atual:

```
schemas/

├── system.py

├── mqtt.py

├── storage.py

├── health.py

└── info.py
```

---

# Tecnologia

Os modelos utilizam:

```
Pydantic
```

através de:

```python
from pydantic import BaseModel
```

---

# Arquitetura dos Schemas

O modelo de dados segue uma composição:

```
              InfoResponse

                  │

        ┌─────────┼─────────┐

        ▼         ▼         ▼

   SystemInfo  MQTTInfo  StorageInfo

                  │

                  ▼

             HealthInfo
```

---

# SystemInfo

Arquivo:

```
schemas/system.py
```

Representa a identidade do equipamento.

Modelo:

```python
class SystemInfo(BaseModel):
```

Campos:

```text
device

id

hardware

software

version

mode

api_version

hostname
```

Exemplo:

```json
{
    "device":"HomeHub Casa",
    "id":"HH-RK3066-001",
    "hardware":"RK3066",
    "software":"HomeHub Gateway",
    "version":"0.3.1-dev",
    "mode":"MQTT Gateway",
    "api_version":"1.0",
    "hostname":"localhost"
}
```

---

# MQTTInfo

Arquivo:

```
schemas/mqtt.py
```

Representa o estado do broker MQTT.

Modelo:

```python
class MQTTInfo(BaseModel):
```

Campos:

```text
broker

config

process

port

status
```

Exemplo:

```json
{
    "broker":"Mosquitto",
    "config":true,
    "process":true,
    "port":true,
    "status":"ONLINE"
}
```

---

# StorageInfo

Arquivo:

```
schemas/storage.py
```

Representa o armazenamento local.

Modelo:

```python
class StorageInfo(BaseModel):
```

Campos:

```text
name

type

capacity

status
```

Exemplo:

```json
{
    "name":"HomeHub Storage",
    "type":"SDCARD",
    "capacity":"250GB",
    "status":"ONLINE"
}
```

---

# HealthInfo

Arquivo:

```
schemas/health.py
```

Representa o diagnóstico dos componentes.

Modelo:

```python
class HealthInfo(BaseModel):
```

Campos:

```text
config

mqtt

storage

system
```

Exemplo:

```json
{
    "config":"OK",
    "mqtt":"ONLINE",
    "storage":"ONLINE",
    "system":"OK"
}
```

---

# InfoResponse

Arquivo:

```
schemas/info.py
```

É o modelo consolidado da API.

Modelo:

```python
class InfoResponse(BaseModel):
```

Composição:

```python
system: SystemInfo

mqtt: MQTTInfo

storage: StorageInfo

health: HealthInfo
```

---

Exemplo completo:

```json
{
    "system":{
        "device":"HomeHub Casa",
        "version":"0.3.1-dev"
    },

    "mqtt":{
        "status":"ONLINE"
    },

    "storage":{
        "status":"ONLINE"
    },

    "health":{
        "system":"OK"
    }
}
```

---

# Integração com FastAPI

Atualmente o endpoint que utiliza schema é:

```
GET /api/info
```

Implementação:

```python
@app.get(
    "/api/info",
    response_model=InfoResponse
)
```

O FastAPI utiliza o modelo para:

- validar resposta;
- gerar documentação Swagger;
- criar contrato OpenAPI.

---

# Evolução da API

A utilização de schemas permite futuras versões:

Exemplo:

```
API v1

SystemInfo

      ↓

API v2

SystemInfo + MetricsInfo
```

Sem quebrar clientes existentes.

---

# Novos Schemas Futuros

Conforme o HomeHub evoluir, novos modelos poderão ser adicionados:

```
schemas/

├── device.py

├── file.py

├── user.py

├── automation.py

└── metrics.py
```

Preparando a API para:

- automação residencial;
- servidor de arquivos;
- gerenciamento de dispositivos;
- monitoramento avançado.

---

# Decisão Arquitetural

Os Managers são responsáveis por obter informações.

Os Schemas são responsáveis por definir como essas informações são expostas.

Fluxo:

```
Manager

   |

   ▼

Dados internos

   |

   ▼

Schema Pydantic

   |

   ▼

Resposta JSON da API
```

Essa separação mantém o backend organizado e permite evolução independente das camadas.
