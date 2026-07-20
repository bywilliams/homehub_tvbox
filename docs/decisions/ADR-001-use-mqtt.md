# ADR-001 — Uso do MQTT como Protocolo de Comunicação

## Status

Aceito.

## Contexto

O HomeHub tem como objetivo funcionar como Gateway de automação residencial.

O sistema precisará comunicar-se com:

- ESP32;
- sensores;
- atuadores;
- dispositivos IoT.

Foi necessário escolher um protocolo leve e adequado para dispositivos embarcados.

---

## Decisão

O HomeHub utilizará MQTT como protocolo principal de comunicação IoT.

O broker escolhido é:

```
Mosquitto
```

---

## Arquitetura

```
Dispositivo IoT

        |

        |

      MQTT

        |

        ▼

   Mosquitto Broker

        |

        ▼

    HomeHub Gateway
```

---

## Motivos

MQTT foi escolhido devido a:

- baixo consumo de banda;
- modelo publish/subscribe;
- suporte amplo em microcontroladores;
- simplicidade;
- funcionamento eficiente em redes locais.

---

## Consequências

Benefícios:

- fácil integração com ESP32;
- escalabilidade de dispositivos;
- comunicação desacoplada.

Possíveis desafios:

- necessidade de gerenciamento de tópicos;
- controle de autenticação;
- monitoramento do broker.

---

## Status Futuro

A implementação atual possui:

- Mosquitto instalado;
- autenticação configurada;
- testes publish/subscribe realizados.
