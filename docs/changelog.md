# HomeHub Changelog

Histórico de evolução do projeto HomeHub.

---

# v0.3.1-dev

Data:

Julho de 2026

## Melhorias

### API Gateway

Implementado:

- Endpoint consolidado `/api/info`;
- Integração dos módulos internos;
- Estrutura inicial de Schemas Pydantic.

---

### Versionamento

Implementado:

- VersionManager;
- Separação entre versão do software e API;
- Controle através de:

```
configs/version.conf
```

Informações:

- software;
- versão;
- modo;
- api_version.

---

### Arquitetura

Melhorias:

- ServiceRegistry;
- organização dos Managers;
- documentação da arquitetura.

---

### Sistema

Atualizado:

- SystemManager passou a consumir VersionManager;
- informações completas do Gateway.

Exemplo:

```json
{
"software":"HomeHub Gateway",
"version":"0.3.1-dev",
"api_version":"1.0"
}
```

---

# v0.3.0-dev

## API REST

Implementado:

- FastAPI Gateway;
- Swagger/OpenAPI;
- endpoints iniciais:

```
/api/system

/api/mqtt

/api/storage

/api/health
```

---

## Diagnóstico

Criado:

```
DoctorManager
```

Responsável por verificar:

- configuração;
- MQTT;
- armazenamento;
- sistema.

---

## Gerenciamento

Criados:

```
SystemManager

MQTTManager

StorageManager
```

---

# v0.2.0-dev

## Estrutura inicial do Gateway

Implementado:

- organização modular;
- diretórios principais;
- sistema de configuração;
- logs;
- scripts de gerenciamento.

Estrutura:

```
configs/

logs/

scripts/

storage/

api/
```

---

## MQTT Gateway

Configurado:

- Mosquitto Broker;
- autenticação;
- persistência;
- testes MQTT.

Testes realizados:

```
mosquitto_pub

mosquitto_sub
```

Comunicação validada.

---

# v0.1.0

## Fundação do Projeto

Primeira versão documentada.

Objetivo:

Transformar uma TV Box RK3066 em um Gateway doméstico local.

Hardware:

```
RK3066

1GB RAM

SD Card 250GB
```

Implementado:

- ambiente Termux;
- estrutura inicial do HomeHub;
- armazenamento externo;
- preparação do Gateway.

---

# Próximos Releases

Planejamento:

```
v0.4.x

Local Cloud


v0.5.x

Dashboard Web


v0.6.x

IoT Gateway


v0.7.x

Automação


v1.0

HomeHub Stable
```
