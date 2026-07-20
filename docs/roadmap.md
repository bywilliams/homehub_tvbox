# HomeHub Roadmap

## Visão Geral

O HomeHub será evoluído de um Gateway MQTT para uma plataforma local de automação residencial.

A evolução será dividida em fases incrementais.

---

# v0.x — Gateway Foundation

## Objetivo

Criar a base técnica do sistema.

Status:

Em desenvolvimento.

Recursos:

- Gateway Python;
- API REST;
- MQTT Broker;
- Gerenciamento de serviços;
- Diagnóstico;
- Configuração centralizada.

---

# v0.4.x — Local Cloud

## Objetivo

Transformar o armazenamento SD Card em uma nuvem local.

Recursos:

- upload de arquivos;
- download;
- gerenciamento de pastas;
- informações de armazenamento.

Arquitetura:

```
Dashboard

   |

File API

   |

Storage Manager

   |

SD Card
```

---

# v0.5.x — Dashboard Web

## Objetivo

Criar interface visual para administração do HomeHub.

Recursos:

- status do sistema;
- monitoramento MQTT;
- gerenciamento de arquivos;
- configurações.

---

# v0.6.x — IoT Gateway

## Objetivo

Integração com dispositivos inteligentes.

Exemplos:

- ESP32;
- sensores;
- atuadores.

Comunicação:

```
Dispositivo

      |

     MQTT

      |

   HomeHub
```

---

# v0.7.x — Automação Residencial

## Objetivo

Adicionar inteligência ao sistema.

Recursos:

- regras;
- eventos;
- agendamento;
- cenas.

---

# v1.0 — HomeHub Stable

Objetivo:

Primeira versão completa da plataforma.

Recursos:

- Gateway;
- Dashboard;
- Arquivos;
- IoT;
- Automação;
- Segurança.
