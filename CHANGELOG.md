# Changelog


# Changelog

Histórico de versões do HomeHub Gateway.



---

# Próxima versão

# v0.4.0-dev

## Local Cloud / File Server

Planejado:

- Servidor local de arquivos.
- Upload e download via navegador.
- Interface Web inicial.
- Gerenciamento do armazenamento SD Card.
- API de arquivos.
- Controle de usuários e permissões.



---

# v0.3.1-dev

## Arquitetura e Core

### Adicionado

- Estrutura modular do HomeHub Core.
- Implementação do `HomeHub` como núcleo central da aplicação.
- Criação do `ServiceRegistry` para gerenciamento de serviços.
- Implementação do `ConfigManager` para carregamento das configurações.
- Implementação do `VersionManager` para controle de versão do software.
- Implementação do sistema de logs (`HomeHubLogger`).

### Melhorias

- Separação entre Core, Managers, API e Schemas.
- Padronização da arquitetura interna.
- Organização dos módulos seguindo responsabilidade única.

---

# v0.3.0-dev

## Gateway API

### Adicionado

- Criação da API REST utilizando FastAPI.
- Estrutura inicial do servidor HTTP.
- Rotas:

  - `/api/system`
  - `/api/storage`
  - `/api/mqtt`
  - `/api/health`
  - `/api/info`

- Documentação automática via OpenAPI.

### Schemas

Implementados modelos Pydantic:

- SystemInfo
- MQTTInfo
- StorageInfo
- HealthInfo
- InfoResponse

---

# v0.2.0-dev

## Gerenciamento de Serviços

### Adicionado

- MQTT Manager.
- Storage Manager.
- Doctor Manager.

### MQTT

- Integração com Mosquitto MQTT Broker.
- Verificação automática:
  - arquivo de configuração;
  - processo ativo;
  - porta 1883 disponível.

### Storage

- Suporte inicial ao armazenamento externo.
- Detecção de SD Card.
- Estrutura HomeHub Storage:




## v0.1.0 (Em desenvolvimento)

### Fase 2

- Inicialização do repositório Git
- Organização da estrutura do projeto
- Documentação inicial
- Preparação do Gateway MQTT

