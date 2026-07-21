# 🏠 HomeHub Gateway

HomeHub é uma plataforma self-hosted para automação residencial, gerenciamento de dispositivos IoT e serviços domésticos locais, desenvolvida para executar em hardware de baixo custo.


![Status](https://img.shields.io/badge/status-em%20desenvolvimento-orange)
![Version](https://img.shields.io/badge/version-v0.4.0--dev-blue)
![Python](https://img.shields.io/badge/python-3.x-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-REST-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

## Visão Geral

O HomeHub Gateway é uma plataforma desenvolvida em Python utilizando FastAPI, projetada para executar em dispositivos de baixo consumo, como TV Boxes Android executando Termux.

O objetivo é oferecer uma solução completa para automação residencial local, integrando dispositivos IoT, armazenamento de arquivos, comunicação MQTT e gerenciamento centralizado sem depender de serviços em nuvem.

Todo o processamento ocorre localmente, garantindo maior privacidade, independência e baixo custo de implantação.

O HomeHub foi concebido para crescer de forma incremental, adicionando novos módulos como automações residenciais, gerenciamento de dispositivos ESP32, banco de dados local, dashboard web, autenticação de usuários, armazenamento de arquivos e integração com assistentes virtuais.

A arquitetura modular permite que novos serviços sejam incorporados sem impactar os módulos existentes, tornando o sistema escalável, organizado e de fácil manutenção.

---

## 🎯 Principais Objetivos

O HomeHub busca oferecer uma plataforma completa para automação residencial local, baseada nos seguintes princípios:

- Executar todos os serviços dentro da rede local.
- Eliminar a dependência de serviços em nuvem.
- Garantir maior privacidade e controle dos dados.
- Reaproveitar hardware de baixo custo, como TV Boxes Android.
- Centralizar os serviços da casa inteligente em um único servidor.
- Fornecer uma arquitetura modular, organizada e escalável.
- Facilitar futuras integrações com ESP32, MQTT, SQLite, Dashboard Web e outros dispositivos IoT.

---

## Objetivos

- Gateway MQTT
- API REST
- Servidor de Arquivos
- Dashboard Web
- Integração com ESP32
- Automação Residencial

Projeto em desenvolvimento.

---

## ✨ Funcionalidades Atuais (v0.4.0-dev)

Atualmente o HomeHub já possui os seguintes módulos implementados:

### 🏠 HomeHub Core

- Núcleo central da aplicação (`HomeHub`).
- Inicialização e gerenciamento de todos os serviços.
- Arquitetura modular baseada em componentes.

---

### ⚙️ Gerenciamento de Serviços

- Service Registry para registro e localização de serviços.
- ConfigManager para carregamento das configurações.
- VersionManager para gerenciamento de versões.
- Sistema centralizado de logs.

---

### 📡 Gateway MQTT

- Integração com o Mosquitto MQTT Broker.
- Verificação automática do broker.
- Verificação do arquivo de configuração.
- Verificação da porta MQTT.
- Monitoramento do processo do broker.

---

### 💾 Gerenciamento de Armazenamento

- Detecção automática do armazenamento.
- Suporte ao cartão SD externo.
- Gerenciamento do HomeHub Storage.
- Monitoramento do espaço disponível.

---

### ☁️ Local Cloud (File Server)

- Gerenciamento centralizado de arquivos.
- Upload de arquivos via API REST.
- Download de arquivos.
- Exclusão de arquivos.
- Listagem de arquivos.
- Estrutura organizada por diretórios.
- Proteção contra Path Traversal.
- Validação de tamanho máximo dos arquivos.

> **Status:** 🚧 Em desenvolvimento ativo.
>
> O File Server já oferece upload, download, exclusão e listagem de arquivos. Nas próximas versões serão adicionados interface web, gerenciamento de usuários, permissões e compartilhamento de arquivos.

---

### 🌐 API REST

API desenvolvida utilizando FastAPI.

Endpoints disponíveis:

| Método | Endpoint | Descrição |
|---------|----------|-----------|
| GET | `/api/info` | Informações gerais |
| GET | `/api/system` | Informações do sistema |
| GET | `/api/storage` | Status do armazenamento |
| GET | `/api/mqtt` | Status do MQTT |
| GET | `/api/health` | Saúde dos serviços |
| GET | `/api/files` | Informações do File Server |
| GET | `/api/files/list` | Lista arquivos |
| POST | `/api/files/upload` | Upload de arquivo |
| GET | `/api/files/download/{arquivo}` | Download de arquivo |
| DELETE | `/api/files/{arquivo}` | Exclui arquivo |

---

### 🩺 Monitoramento

- Doctor Service.
- Verificação da saúde dos serviços.
- Monitoramento do MQTT.
- Monitoramento do armazenamento.
- Monitoramento das configurações.
- Diagnóstico geral do sistema.

---

## 🏗 Arquitetura do Sistema

O HomeHub foi desenvolvido utilizando uma arquitetura modular baseada em serviços independentes. Todos os componentes são inicializados pelo núcleo da aplicação (`HomeHub`) e registrados em um **Service Registry**, permitindo baixo acoplamento e fácil expansão do sistema.

```text
                         HomeHub Gateway

                    +----------------------+
                    |      HomeHub Core    |
                    +----------+-----------+
                               |
                 +-------------+-------------+
                 |                           |
          Service Registry             Config Manager
                 |                           |
      +----------+----------+                |
      |          |          |                |
   Version     Logger    Doctor              |
      |                     |                |
      +----------+----------+                |
                 |                           |
      +----------+----------+----------------+
      |          |          |
    System     MQTT     Storage
                            |
                      File Manager
                            |
                      HomeHub Storage
                       (SD Card / USB)

                            |
                      FastAPI REST API
                            |
      +---------+-----------+-----------+---------+
      |         |           |           |         |
   /system   /mqtt     /storage    /files    /health
```

### Organização dos módulos

- **HomeHub Core:** inicializa todos os serviços da aplicação.
- **Service Registry:** registra e disponibiliza os serviços para os demais componentes.
- **Managers:** encapsulam a lógica de cada módulo.
- **FastAPI:** disponibiliza os serviços através da API REST.
- **HomeHub Storage:** representa o armazenamento local utilizado pelo servidor.

---

### Princípios da Arquitetura

O projeto foi desenvolvido seguindo alguns princípios fundamentais:

- Arquitetura modular.
- Baixo acoplamento entre componentes.
- Alta coesão.
- Facilidade de manutenção.
- Fácil expansão através de novos módulos.
- Separação entre regras de negócio, API e gerenciamento de serviços.
- Prioridade para execução em hardware de baixo consumo.

---

## 📁 Estrutura do Projeto

A organização do projeto segue uma arquitetura modular, separando claramente o núcleo da aplicação, os serviços, a documentação e os recursos utilizados pelo sistema.

```text
HomeHub/
│
├── api/                # API REST e núcleo da aplicação
│   ├── app/
│   │   ├── api/         # Rotas da API
│   │   ├── core/        # Configuração, versão e logs
│   │   ├── managers/    # Regras de negócio
│   │   ├── registry/    # Registro de serviços
│   │   ├── schemas/     # Modelos Pydantic
│   │   ├── services/    # Serviços auxiliares
│   │   ├── models/      # Modelos de domínio
│   │   └── utils/       # Utilitários
│   │
│   ├── doctor.py
│   └── venv/
│
├── configs/            # Arquivos de configuração
│
├── database/           # Banco de dados (SQLite futuramente)
│
├── dashboard/          # Interface Web (em desenvolvimento)
│
├── docs/               # Documentação técnica
│
├── logs/               # Logs da aplicação
│
├── scripts/            # Scripts de inicialização
│
├── services/           # Serviços do sistema
│
├── storage/            # Estrutura do armazenamento local
│
├── tests/              # Testes automatizados
│
├── README.md
├── CHANGELOG.md
├── VERSION
└── LICENSE
```

### Diretórios Principais

| Diretório | Finalidade |
|------------|------------|
| `api/` | API REST e núcleo do HomeHub |
| `configs/` | Arquivos de configuração dos serviços |
| `database/` | Banco de dados local |
| `dashboard/` | Interface Web |
| `docs/` | Documentação técnica e ADRs |
| `logs/` | Arquivos de log |
| `scripts/` | Scripts de gerenciamento |
| `services/` | Serviços executados pelo sistema |
| `storage/` | Área de armazenamento local |
| `tests/` | Testes automatizados |


---

### Estrutura do HomeHub Storage

```text
HomeHub/
│
├── backups/
├── database/
├── files/
│   ├── documents/
│   ├── images/
│   ├── shared/
│   └── videos/
│
├── media/
└── uploads/
```

O armazenamento é mantido em um cartão SD externo (quando disponível), permitindo separar os dados da aplicação do sistema operacional e facilitando backups e migrações.

---

## 🛠 Tecnologias Utilizadas

O HomeHub é construído utilizando tecnologias consolidadas, leves e voltadas para execução em hardware de baixo consumo.

| Tecnologia | Finalidade |
|------------|------------|
| Python 3 | Linguagem principal da aplicação |
| FastAPI | API REST de alto desempenho |
| Pydantic | Validação e serialização de dados |
| Uvicorn | Servidor ASGI |
| Mosquitto | Broker MQTT |
| SQLite *(planejado)* | Banco de dados local |
| Termux | Ambiente Linux para Android |
| Git | Controle de versão |
| GitHub | Hospedagem do código-fonte |
| REST API | Comunicação entre clientes e serviços |
| MQTT | Comunicação com dispositivos IoT |

---

### Hardware de Referência

O projeto está sendo desenvolvido e testado utilizando o seguinte hardware:

| Componente | Especificação |
|------------|---------------|
| Dispositivo | TV Box Android |
| Processador | Rockchip RK3066 |
| Memória RAM | 1 GB |
| Armazenamento interno | 8 GB |
| Armazenamento externo | Cartão SD 256 GB |
| Sistema Operacional | Android + Termux |

O objetivo é demonstrar que é possível executar uma plataforma completa de automação residencial utilizando equipamentos de baixo custo.

---

## 🚀 Roadmap

### ✅ Concluído

- HomeHub Core
- Service Registry
- Config Manager
- Version Manager
- Logger
- MQTT Manager
- Storage Manager
- Doctor Manager
- API REST
- File Manager
- Upload de arquivos
- Download de arquivos
- Exclusão de arquivos
- Listagem de arquivos

---

### 🚧 Em desenvolvimento

- Dashboard Web
- Interface para gerenciamento de arquivos
- Navegação entre diretórios
- Upload pelo navegador

---

### 📌 Planejado

- Autenticação de usuários
- Controle de permissões
- Banco de dados SQLite
- Cadastro de dispositivos IoT
- Integração com ESP32
- Automações
- Agendamentos
- API MQTT avançada
- Backup automático
- Compartilhamento de arquivos
- Integração com Alexa
- Integração com Home Assistant

---

## 🚀 Instalação

### 1. Clonar o repositório

```bash
git clone https://github.com/bywilliams/homehub.git
cd HomeHub
```

---

### 2. Criar o ambiente virtual

```bash
cd api

python -m venv venv
```

Ativar o ambiente virtual:

**Linux / macOS**

```bash
source venv/bin/activate
```

**Windows**

```cmd
venv\Scripts\activate
```

---

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

---

### 4. Configurar o armazenamento

Crie a estrutura do HomeHub Storage:

```text
HomeHub/
├── backups/
├── database/
├── files/
│   ├── documents/
│   ├── images/
│   ├── shared/
│   └── videos/
├── media/
└── uploads/
```

No ambiente de desenvolvimento atual, essa estrutura está localizada em um cartão SD externo através do Termux.

---

### 5. Iniciar a API

```bash
python -m app.web
```

Servidor:

```
http://127.0.0.1:8000
```

---

### 6. Documentação automática

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```


---

## 🧪 Testando a API

Verificar informações gerais:

```bash
curl http://127.0.0.1:8000/api/info
```

Listar arquivos:

```bash
curl http://127.0.0.1:8000/api/files/list
```

Upload:

```bash
curl \
-F "file=@teste.txt" \
http://127.0.0.1:8000/api/files/upload
```

Download:

```bash
curl \
-O \
http://127.0.0.1:8000/api/files/download/teste.txt
```

Excluir:

```bash
curl \
-X DELETE \
http://127.0.0.1:8000/api/files/teste.txt
```

Health Check:

```bash
curl http://127.0.0.1:8000/api/health
```

---

## 🤝 Como Contribuir

Contribuições são bem-vindas!

Caso queira colaborar com o projeto:

1. Faça um fork do repositório.
2. Crie uma branch para sua funcionalidade.
3. Realize as alterações e testes necessários.
4. Envie um Pull Request descrevendo as mudanças.

Sugestões, correções e melhorias também podem ser abertas através da área de *Issues* do GitHub.

---

## 📄 Licença

Este projeto está licenciado sob a licença MIT.

Consulte o arquivo `LICENSE` para mais informações.

---

## 👨‍💻 Autor

Desenvolvido por **William Silva Sebastião**.

GitHub:

https://github.com/bywilliams



## 💡 Filosofia do Projeto

O HomeHub nasceu com o objetivo de demonstrar que é possível construir uma plataforma completa de automação residencial utilizando hardware acessível e software livre.

Os principais pilares do projeto são:

- Privacidade dos dados.
- Execução totalmente local.
- Independência de serviços em nuvem.
- Arquitetura modular.
- Facilidade de expansão.
- Reutilização de hardware.

Mais do que um gateway MQTT, o HomeHub busca se tornar uma plataforma aberta para estudos, experimentação e desenvolvimento de soluções IoT.
