
# 📄 Documentação Técnica – Site FURIA eSports

## 📌 Visão Geral

Este projeto é um site institucional fictício para a organização FURIA eSports. Desenvolvido com HTML, CSS e Bootstrap, seu objetivo é apresentar informações sobre o time, seus jogadores, notícias e um canal de contato, incluindo integração com o Telegram.

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia          | Versão | Descrição                                                            |
| ------------------- | ------ | -------------------------------------------------------------------- |
| HTML                | 5      | Estrutura da página                                                  |
| CSS                 | 3      | Estilização visual personalizada                                     |
| Bootstrap           | 5.3.2  | Framework para layout e responsividade                               |
| JavaScript (básico) | —      | Para efeitos de animação via CSS (sem JS puro incluso neste projeto) |

---

## 📁 Estrutura dos Arquivos

```
/seu-projeto
│
├── index.html               # Página principal
├── styles.css               # Estilos personalizados
├── /imagens                 # Pasta de imagens locais
│   ├── fallenzo.png
│   └── Telegram_2019_Logo.svg.png
```

---

## 🧱 Estrutura da Página

### 1. **Navbar**

* Fixa no topo (`fixed-top`)
* Links com rolagem suave para as seções internas:

  * Sobre
  * Jogadores
  * Notícias
  * Destaque
  * Contato

### 2. **Seção Home**

* Tela cheia (`height: 100vh`)
* Exibe o logotipo da FURIA e slogan do time

### 3. **Seção Sobre**

* Explica a história da FURIA e sua importância no cenário competitivo

### 4. **Seção Jogadores**

* Cards com três personagens: Fallen, Dev Gabriel (fictício), e KSCERATO
* Efeito hover nos cards para destaque

### 5. **Seção Notícias**

* Blocos de notícias fictícias da equipe

### 6. **Seção Destaque**

* Tela cheia com CTA (chamada para ação) para acessar um bot no Telegram
* Design roxo com botão estilizado e logo do Telegram

### 7. **Seção Contato**

* Formulário com nome, e-mail e mensagem
* Botão personalizado (`btn-purple`)

### 8. **Rodapé**

* Informações de direitos autorais

---

## 🎨 Estilização (CSS)

* **Fundo escuro padrão:** `#111`

* **Cor roxa personalizada:** `#60349c`

* **Classes de animação:**

  * `.animar-esquerda`
  * `.animar-direita`
    Utilizam `@keyframes` para efeito de entrada lateral com `opacity` e `translateX`.

* **Estilização de botões e links:**

  * `btn-purple` com hover
  * Links do navbar mudam de cor ao passar o mouse

---

## 🔗 Links Importantes

* Bootstrap CDN:
  `https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css`

* Telegram fictício:
  `https://t.me/furiaDesafio_bot`

---

## 📱 Responsividade

* A estrutura usa o grid e as utilidades do Bootstrap para garantir boa experiência em dispositivos móveis.
* O `viewport` está configurado com `<meta name="viewport" content="width=device-width, initial-scale=1.0">`.

