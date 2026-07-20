# ADR-004 — Separação do StorageManager e Gerenciamento de Armazenamento

## Status

Aceito.

---

## Contexto

O HomeHub necessita de armazenamento local para:

- arquivos;
- backups;
- banco de dados;
- mídias;
- dados dos dispositivos.

O armazenamento físico pode variar conforme a plataforma.

Atualmente é utilizado:

```
SD Card 250GB
```

Foi necessário criar uma camada de abstração para evitar dependência direta do hardware.

---

## Decisão

O gerenciamento de armazenamento será realizado através do:

```
StorageManager
```

localizado em:

```
app/managers/storage_manager.py
```

---

## Arquitetura

```
API

 |

 ▼

StorageManager

 |

 ├── Descoberta de armazenamento

 ├── Validação de caminho

 ├── Informações de disco

 └── Status do armazenamento

 |

 ▼

Storage físico
```

---

## Responsabilidades

O StorageManager é responsável por:

### Descoberta

Encontrar automaticamente armazenamentos disponíveis.

---

### Configuração

Carregar:

```
configs/storage.conf
```

---

### Monitoramento

Obter:

- capacidade;
- espaço utilizado;
- espaço livre;
- status.

---

### Abstração

A API não precisa conhecer:

- caminho físico;
- sistema de arquivos;
- dispositivo utilizado.

---

## Motivos

A separação foi escolhida para:

- facilitar manutenção;
- permitir troca de hardware;
- preparar servidor de arquivos;
- manter a API independente.

---

## Consequências

Benefícios:

- arquitetura modular;
- suporte futuro a novos dispositivos;
- preparação para Local Cloud.

---

## Evolução Futura

O StorageManager será expandido para suportar:

```
FileManager

Upload

Download

Pastas

Permissões

Backup
```

Arquitetura futura:

```
Dashboard

    |

 File API

    |

StorageManager

    |

SD Card
```

---

## Status Atual

Implementado:

- detecção do SD Card;
- leitura de informações do disco;
- validação do armazenamento;
- integração com API.

Endpoint:

```
GET /api/storage
```
