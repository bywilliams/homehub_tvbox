# ADR-005 — Uso do Service Registry para Gerenciamento de Dependências

## Status

Aceito.

---

## Contexto

O HomeHub possui diversos componentes internos:

- configuração;
- sistema;
- MQTT;
- armazenamento;
- diagnóstico;
- logs.

Com o crescimento do projeto, tornou-se necessário organizar a comunicação entre esses serviços.

Uma abordagem baseada em importações diretas poderia criar forte acoplamento entre módulos.

---

## Decisão

O HomeHub utilizará um:

```
Service Registry
```

como mecanismo central de registro e acesso aos serviços internos.

Implementação:

```
app/registry/service_registry.py
```

---

## Arquitetura

```
                 HomeHub

                    |

                    ▼

           ServiceRegistry

        ┌───────────┼───────────┐

        ▼           ▼           ▼

     Config      MQTT       Storage

        ▼           ▼           ▼

     System     Doctor     Logger
```

---

## Funcionamento

Durante a inicialização:

```python
registry.register(
    "mqtt",
    mqtt_manager
)
```

O serviço fica disponível.

Outros componentes podem acessar:

```python
registry.get(
    "mqtt"
)
```

---

## Motivos

A decisão foi tomada para:

- reduzir acoplamento;
- facilitar expansão;
- permitir novos serviços;
- centralizar dependências.

---

## Benefícios

A arquitetura permite adicionar novos módulos:

```
DeviceManager

AutomationManager

FileManager

UserManager

NotificationManager
```

sem alterar os serviços existentes.

---

## Consequências

Benefícios:

- código mais organizado;
- maior flexibilidade;
- manutenção simplificada.

Possíveis cuidados:

- nomes de serviços devem ser padronizados;
- registro deve acontecer antes do uso.

---

## Status Atual

Serviços registrados:

```
config

version

logger

system

mqtt

storage

doctor
```

---

## Evolução Futura

O Service Registry poderá evoluir para:

- gerenciamento de ciclo de vida;
- inicialização automática;
- dependências entre serviços;
- descoberta de plugins.
