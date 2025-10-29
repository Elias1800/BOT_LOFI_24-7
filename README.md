# Lofi Bot - Discord Music Bot 24/7

![Versão](https://img.shields.io/badge/versão-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8%2B-brightgreen)
![Discord.py](https://img.shields.io/badge/discord.py-2.0%2B-blue)
![Status](https://img.shields.io/badge/status-Ativo-success)
[![Licença MIT](https://img.shields.io/badge/licença-MIT-yellow)](LICENSE)

![LoFi Bot Banner](imagens/LOFI.png)

> **LoFi Bot** é um bot minimalista para Discord que toca rádio lo-fi 24/7.  
> Simples, leve e eficiente para criar um ambiente relaxante no seu servidor.

##  Tabela de Conteúdos

- [Funcionalidades](#funcionalidades)
- [Requisitos](#requisitos)
- [Tecnologias](#tecnologias)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Como Usar](#como-usar)
- [Comandos](#comandos)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Funcionalidades

-  Toca rádio lo-fi direto do YouTube
-  Volume pré-configurado em 40%
-  Exibe informações da música com embed estilizado
-  Mostra thumbnail da rádio
-  Comandos simples e intuitivos
-  Interface limpa com cor roxa

## Requisitos

- Python 3.8 ou superior
- FFmpeg instalado no sistema
- Token do bot Discord
- Conexão com internet estável

## Tecnologias

| Tecnologia | Versão | Função |
|------------|--------|--------|
| **Python** | 3.8+ | Linguagem principal |
| **discord.py** | 2.0+ | Biblioteca para Discord |
| **yt-dlp** | latest | Streaming de áudio do YouTube |
| **FFmpeg** | latest | Processamento de áudio |

## Instalação

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/Elias1800/BOT_LOFI_24-7.git
```

### 2️⃣ Crie um ambiente virtual (recomendado)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Instale as dependências

```bash
pip install discord.py yt-dlp
```

### 4️⃣ Instale o FFmpeg

**Windows (Chocolatey):**
```bash
choco install ffmpeg
```

**Windows (Manual):**
1. Baixe em [ffmpeg.org](https://ffmpeg.org/download.html)
2. Extraia e adicione ao PATH do sistema

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install ffmpeg
```

**macOS (Homebrew):**
```bash
brew install ffmpeg
```

### 5️⃣ Verifique a instalação

```bash
python --version
ffmpeg -version
```

## Configuração

### 1️⃣ Adicione o Token no código

Abra o arquivo `main.py` e substitua:

```python
bot.run("API BOT KEY")
```

Por:

```python
bot.run("SEU_TOKEN_AQUI")
```


**Permissões necessárias nas configurações do bot:**
- ✅ Conectar a canais de voz
- ✅ Falar em canais de voz
- ✅ Enviar mensagens
- ✅ Inserir links

## Como Usar

### 1️⃣ Inicie o bot

```bash
python bot.py
```

Você verá:
```
✅ Bot conectado como SeuBot#1234
```

### 2️⃣ Entre em um canal de voz

No Discord, conecte-se a qualquer canal de voz.

### 3️⃣ Use o comando

Digite no chat:
```
!lofi
```

### 4️⃣ Aproveite!

O bot irá:
- Conectar no seu canal de voz
- Começar a tocar lo-fi
- Mostrar um embed com informações

## Comandos

| Comando | Descrição |
|---------|-----------|
| `!lofi` | Inicia a rádio lofi no canal de voz |

## Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Faça um Fork do projeto
2. Crie uma branch: `git checkout -b feature/nova-feature`
3. Commit suas mudanças: `git commit -m 'Add nova feature'`
4. Push para a branch: `git push origin feature/nova-feature`
5. Abra um Pull Request


## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

 **Se você gostou do projeto, deixe uma estrela!** ⭐