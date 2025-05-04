
## 📚 Documentação do Backend – WikiBot FURIA

### 📌 Descrição

O **WikiBot FURIA** é um bot para Telegram que fornece informações sobre a organização de eSports FURIA. Ele responde automaticamente perguntas sobre a equipe usando dados da Wikipédia e respostas personalizadas. Além disso, oferece botões interativos para facilitar a navegação por tópicos específicos.

---

### 🚀 Tecnologias Utilizadas

* **Python 3.10+**
* **python-telegram-bot (v20+)**
* **wikipedia-api**
* **requests**

---

### 📂 Estrutura do Projeto

```
wikibot_furia/
│
├── main.py                # Código principal do bot
├── requirements.txt       # Lista de dependências
└── README.md              # Documentação (você está aqui)
```

---

### 🔧 Funcionalidades

* `/start`: Envia imagem da logo da FURIA e exibe botões interativos.

* **Botões interativos** com os seguintes tópicos:

  * 📅 Fundação
  * 🎮 Modalidades
  * 🏆 Conquistas
  * 🧠 Filosofia
  * 🌎 Sede
  * 🧑‍💼 Fundadores
  * 👥 Comunidade

* **Respostas personalizadas** com palavras-chave sobre:

  * Jogadores (ex: *KSCERATO*, *Yuurih*, *FalleN*)
  * Modalidades (ex: *Rocket League*, *League of Legends*)
  * Títulos e participações em campeonatos
  * Canais oficiais da FURIA (YouTube, Twitch)
  * Patrocinadores
  * Time feminino

* **Fallback para Wikipédia**: caso a pergunta não seja reconhecida, o bot busca a resposta automaticamente na Wikipédia em português.

---

### ⚙️ Como Executar

1. **Clone o repositório:**


2. **Instale as dependências:**

```bash
pip install -r requirements.txt
```


3. **Execute o bot:**

```bash
python main.py
```

---

### 🧪 Exemplo de Uso

* Envie `/start` no chat com o bot.
* Clique em botões como `🎮 Modalidades` ou digite perguntas como:

  * `Quem é KSCERATO?`
  * `A FURIA ganhou algum Major?`
  * `Qual é a sede da FURIA?`
  * `FURIA tem canal no YouTube?`

## 📱 Como usar?

1. Abra o app do **Telegram** (celular ou desktop).
2. Acesse o bot (https://t.me/furiaDesafio_bot).
3. Clique em **Start** ou envie qualquer mensagem relacionada à FURIA.
4. Explore o menu com botões interativos ou faça perguntas diretamente.

---

## 💡 Exemplo de perguntas válidas

* `títulos cs`
* `qual foi a melhor colocação da FURIA no major`
* `a furia tem canal no youtube?`
* `quando fallen entrou na furia?`
* `lineup lol`
* `furia tem time feminino de cs2?`

## 📄 Sobre

Este projeto foi criado para responder automaticamente perguntas sobre a equipe FURIA, com um backend hospedado pronto para uso público.


### 👨‍💻 Autor

* **Enzo Gabriel Rosa Vinhati**
* GitHub: (https://github.com/GabrielVinhati)
* LinkedIN: (https://www.linkedin.com/in/gabriel-vinhati/)
* Contato: (mailto:gabriel.vinhati@outlook.com)