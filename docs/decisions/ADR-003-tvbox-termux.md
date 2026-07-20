# ADR-003 — Uso de TV Box RK3066 + Termux como Plataforma do Gateway

## Status

Aceito.

---

## Contexto

O HomeHub tem como objetivo funcionar como um servidor doméstico local de baixo consumo.

Foi necessário escolher uma plataforma de hardware que pudesse executar:

- broker MQTT;
- API REST;
- serviços Python;
- armazenamento local;
- futuras integrações IoT.

A solução deveria possuir:

- baixo consumo energético;
- funcionamento contínuo;
- conectividade de rede;
- possibilidade de expansão.

---

## Decisão

O HomeHub será executado inicialmente em uma TV Box baseada no chipset:

```
RK3066
```

utilizando:

```
Android + Termux
```

como ambiente de execução.

---

## Hardware

Plataforma atual:

```
TV Box RK3066

CPU:
Dual Core Cortex A9

Memória:
1GB RAM

Armazenamento interno:
8GB

Armazenamento externo:
SD Card 250GB

Rede:
Ethernet / WiFi
```

---

## Arquitetura de Execução

```
Hardware TV Box

        |

        ▼

Android

        |

        ▼

Termux

        |

        ▼

HomeHub Gateway

        |

        ├── Python API

        ├── Mosquitto MQTT

        ├── Storage

        └── Services
```

---

## Motivos

A plataforma foi escolhida devido a:

### Reaproveitamento de hardware

Permite transformar um equipamento antigo em um servidor dedicado.

---

### Baixo consumo

Comparado a computadores tradicionais:

- menor consumo energético;
- operação contínua;
- baixo custo.

---

### Conectividade

A TV Box possui:

- rede Ethernet;
- WiFi;
- suporte a armazenamento externo.

---

### Flexibilidade

O Termux permite executar:

- Python;
- servidores;
- ferramentas Linux;
- scripts de automação.

---

## Consequências

Benefícios:

- servidor doméstico compacto;
- baixo custo;
- funcionamento local;
- independência de nuvem externa.

---

## Limitações Conhecidas

A plataforma possui restrições:

### Memória

```
1GB RAM
```

Exige cuidado com:

- quantidade de serviços;
- processos em background;
- consumo da API.

---

### Processamento

O RK3066 é adequado para:

- MQTT;
- APIs leves;
- gerenciamento de arquivos.

Porém pode ser limitado para:

- processamento pesado;
- inteligência artificial local;
- grandes bancos de dados.

---

## Estratégia de Evolução

A arquitetura foi criada para permitir futura migração.

Possíveis plataformas:

```
Raspberry Pi

Mini PC

Servidor ARM

Outro hardware Linux
```

Os serviços deverão permanecer independentes do hardware.

---

## Status Atual

A plataforma já possui:

- Termux configurado;
- estrutura HomeHub criada;
- Mosquitto funcionando;
- API FastAPI funcionando;
- armazenamento SD detectado.
