# ADR-002 — Uso do FastAPI como API Gateway

## Status

Aceito.

---

## Contexto

O HomeHub necessita de uma interface de comunicação entre seus serviços internos e clientes externos.

A API deve permitir:

- consulta do estado do sistema;
- gerenciamento de componentes;
- integração com Dashboard;
- futuras aplicações móveis.

Foram avaliadas opções baseadas em Python para criação da camada HTTP.

---

## Decisão

O HomeHub utilizará:

```
FastAPI
```

como framework principal para sua API REST.

O servidor ASGI utilizado será:

```
Uvicorn
```

---

## Arquitetura

```
Cliente

   |

   ▼

FastAPI REST API

   |

   ▼

HomeHub Core

   |

   ├── SystemManager

   ├── MQTTManager

   ├── StorageManager

   └── DoctorManager
```

---

## Motivos

FastAPI foi escolhido devido a:

### Desempenho

Possui excelente desempenho utilizando ASGI.

---

### Integração com Python

Permite reutilizar toda a lógica desenvolvida no Gateway.

---

### Documentação automática

Gera automaticamente:

- Swagger UI;
- OpenAPI;
- modelos de resposta.

---

### Validação de dados

Integração nativa com:

```
Pydantic
```

permitindo criação de contratos de API.

---

## Consequências

Benefícios:

- API profissional;
- fácil manutenção;
- documentação automática;
- base para Dashboard.

---

Possíveis desafios:

- consumo adicional de memória;
- necessidade de controle de processos;
- gerenciamento de versões da API.

---

## Implementação Atual

A API possui:

Endpoints:

```
GET /

GET /api/system

GET /api/mqtt

GET /api/storage

GET /api/health

GET /api/info
```

Documentação:

```
Swagger/OpenAPI
```

Disponível através de:

```
/docs
```

---

## Status Futuro

A API será expandida com:

```
/api/files

/api/devices

/api/automation

/api/settings
```

mantendo o padrão:

```
Route

   |

Manager

   |

Service
```
