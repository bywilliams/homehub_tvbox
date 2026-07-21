# Changelog

Histórico de versões do HomeHub Gateway.
---

# Próxima versão

# v0.4.1-dev

Planejado:

### Próximos passos

- Interface Web para gerenciamento de arquivos.
- Upload via navegador.
- Download via navegador.
- Gerenciamento visual de pastas.
- Controle de usuários.
- Controle de permissões.

---

# v0.4.0-dev

## Local Cloud / File Server

### Adicionado

- Implementação inicial do servidor local de arquivos.
- Criação do `FileManager`.
- Integração do FileManager ao núcleo HomeHub.
- Registro do serviço Files no `ServiceRegistry`.
- Estrutura de armazenamento no SD Card:


### API de Arquivos

Novos endpoints:

- `GET /api/files`
  - Informações do serviço de arquivos.

- `GET /api/files/list`
  - Lista arquivos disponíveis.

- `POST /api/files/upload`
  - Upload de arquivos.

- `GET /api/files/download/{filename}`
  - Download de arquivos.

- `DELETE /api/files/{filename}`
  - Exclusão de arquivos.


### Segurança

Implementado:

- Proteção contra Path Traversal.
- Sanitização dos nomes de arquivos.
- Restrição de acesso somente ao diretório HomeHub/files.
- Bloqueio de sobrescrita de arquivos existentes.
- Limite máximo de upload:
  - 100 MB por arquivo.


### Testes realizados

- Upload via API funcionando.
- Download via API funcionando.
- Listagem de arquivos funcionando.
- Exclusão de arquivos funcionando.
- Validação de arquivos duplicados funcionando.
- Teste de segurança contra caminhos externos.
- Teste de limite de tamanho:
  - Arquivo de 101 MB rejeitado corretamente.


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

