# HomeHub Gateway v0.2.0-dev

## Python Core + Service Registry + Health Monitoring

**Versão:** 0.2.0-dev  
**Data:** 20/07/2026  
**Hardware:** TV Box RK3066  
**Plataforma:** Android 11.1 + Termux  
**Ambiente:** Python 3.14.6 + Virtual Environment

---

# 1. Visão Geral

A versão **v0.2.0-dev** representa uma evolução arquitetural do HomeHub Gateway.

Na versão anterior (**v0.1.0**) o projeto possuía uma infraestrutura funcional baseada em scripts Bash, MQTT Broker Mosquitto e gerenciamento inicial de armazenamento.

Nesta nova etapa foi criado o **HomeHub Core**, uma camada central desenvolvida em Python responsável por gerenciar serviços, monitorar componentes e preparar a plataforma para futuras integrações como API Web, Dashboard e dispositivos IoT.

O objetivo desta evolução foi transformar o HomeHub de um conjunto de scripts independentes em uma plataforma modular, organizada e expansível.

---

# 2. Motivação da Evolução

Com o crescimento do projeto surgiram limitações na arquitetura inicial.

## Problemas identificados na versão v0.1.0

- Scripts Bash começaram a acumular responsabilidades;
- Cada serviço possuía lógica própria;
- Não existia uma camada central de gerenciamento;
- O diagnóstico precisava ser realizado manualmente;
- A futura criação de uma API Web exigia uma estrutura mais organizada.

---

# Solução implementada

Foi criado o conceito de **HomeHub Core**.

O Core passou a ser responsável por:

- Inicialização dos serviços;
- Registro dos componentes ativos;
- Monitoramento do sistema;
- Organização modular do código;
- Preparação para futuras APIs.

---

# 3. Nova Arquitetura

A versão **v0.2.0-dev** introduziu uma arquitetura baseada em serviços independentes.

Cada componente possui uma responsabilidade específica, permitindo evolução gradual do projeto.


             HomeHub Gateway v0.2.0-dev


                     CLI

                      |

                HomeHub Core

                      |

             Service Registry

                      |

    +-------------------------------+

    |          |          |         |

   MQTT     Storage    System    Doctor


                     |

          Config / Version / Logger




---

# 4. HomeHub Core

O **HomeHub Core** é o núcleo principal da aplicação.

Sua responsabilidade é inicializar e organizar todos os serviços necessários para funcionamento do Gateway.

Arquivo principal: api/app/homehub.py



---

## Responsabilidades

- Carregar configurações;
- Inicializar gerenciadores;
- Registrar serviços;
- Centralizar informações do sistema;
- Disponibilizar dados para futuras interfaces.

---

# 5. Service Registry

Para permitir comunicação organizada entre componentes foi criado o **Service Registry**.

Arquivo: api/app/registry/service_registry.py



O Registry funciona como um catálogo central de serviços disponíveis.

---

## Objetivos

- Evitar dependências diretas entre módulos;
- Facilitar manutenção;
- Permitir novos serviços futuramente;
- Centralizar acesso aos componentes.

---

## Serviços registrados atualmente

config
version
logger
system
mqtt
storage
doctor


---

# 6. Gerenciadores de Serviços (Managers)

Os Managers são módulos responsáveis por controlar funcionalidades específicas do HomeHub.

Estrutura:

api/app/managers/

├── mqtt_manager.py
├── storage_manager.py
├── system_manager.py
└── doctor_manager.py



---

# 6.1 MQTTManager

Arquivo: api/app/managers/mqtt_manager.py



Responsabilidade:

Gerenciar e monitorar o serviço MQTT utilizado pelo HomeHub.

O broker utilizado é o Mosquitto.

---

## Verificações realizadas

O MQTTManager verifica:

- Arquivo de configuração;
- Processo Mosquitto;
- Porta MQTT 1883.

---

## Exemplo de funcionamento

MQTT:

broker : Mosquitto
config : True
process : True
port : True
status : ONLINE


---

# 6.2 StorageManager

Arquivo: api/app/managers/storage_manager.py


Responsabilidade:

Gerenciar o armazenamento externo utilizado pelo HomeHub.

O armazenamento principal é um cartão SD de 250GB.

---

## Informações monitoradas

- Disponibilidade do cartão;
- Existência do diretório;
- Espaço total;
- Espaço utilizado;
- Espaço livre.

---

## Estrutura do armazenamento

HomeHub Storage

├── files
├── uploads
├── backups
├── database
└── media


---

## Exemplo de funcionamento


Storage:

name : HomeHub Storage
type : SDCARD

total : 250G
used : 224M
free : 250G
usage : 1%

status : ONLINE


---

# 6.3 SystemManager

Arquivo: api/app/managers/system_manager.py




Responsabilidade:

Coletar informações do dispositivo.

Informações:

- Nome do dispositivo;
- Hardware;
- Hostname;
- Rede;
- Sistema.

---

# 6.4 DoctorManager

Arquivo: api/app/managers/doctor_manager.py


Responsabilidade:

Executar diagnóstico geral do HomeHub.

O Doctor consulta os serviços registrados no Service Registry.

---

## Verificações
Config
MQTT
Storage
System


---

## Comando
homehub doctor

---

## Resultado
================================
HomeHub Doctor

Config : OK
Mqtt : ONLINE
Storage : ONLINE
System : OK

Result:

✓ SYSTEM HEALTHY

================================



---

# 7. Problemas Encontrados e Soluções

Durante a implementação da versão v0.2.0-dev alguns problemas foram encontrados e solucionados.

---

# 7.1 Erros de Identação Python

## Problema

Durante o desenvolvimento ocorreram erros:

Storage OFFLINE


---

## Diagnóstico

O Android havia desmontado temporariamente o cartão.

O caminho: /storage/8786-451F


não estava disponível.

---

## Solução

O cartão SD foi removido e conectado novamente.

Após remontagem: /dev/fuse 250G



voltou a aparecer.

---

## Resultado

O Storage voltou ao funcionamento normal:

Status:

✓ ONLINE



---

# 7.3 Melhorias implementadas no Storage

Após o problema do cartão SD, o gerenciamento foi melhorado.

Agora o sistema verifica:

- Existência do caminho;
- Disponibilidade do armazenamento;
- Informações de espaço;
- Estrutura de diretórios.

---

# 8. Comandos Disponíveis

Atualmente o HomeHub possui:

homehub start

homehub stop

homehub restart

homehub status

homehub storage

homehub doctor




---

# 9. Estado Atual do Sistema

Versão:
HomeHub Gateway
0.2.0-dev


---

Serviços ativos:
✓ ConfigManager

✓ VersionManager

✓ Logger

✓ SystemManager

✓ MQTTManager

✓ StorageManager

✓ DoctorManager



---

# 10. Estrutura Atual do Projeto

Homehub

├── api
│
├── configs
│
├── database
│
├── dashboard
│
├── docs
│
├── logs
│
├── scripts
│
├── services
│
├── storage
│
└── tests



---

# 11. Próxima Etapa

## HomeHub Gateway v0.3.0-dev

Próxima evolução:

Implementação do servidor Web/API.

Objetivos:

- FastAPI;
- API REST;
- Dashboard Web;
- Upload e Download de arquivos;
- Monitoramento remoto;
- Integração com ESP32;
- Controle de dispositivos IoT.

---

# Conclusão

A versão **v0.2.0-dev** representa a transformação do HomeHub de um conjunto de scripts para uma plataforma modular.

Principais conquistas:

✅ HomeHub Core criado  
✅ Arquitetura baseada em serviços  
✅ Service Registry implementado  
✅ MQTT monitorado automaticamente  
✅ Storage monitorado automaticamente  
✅ Sistema de diagnóstico criado  
✅ Problemas reais documentados e corrigidos  

O HomeHub está preparado para iniciar a próxima fase: **API Web e Dashboard.**
