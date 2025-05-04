import logging
import requests
import wikipediaapi
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, CallbackContext

# --- Configura logs ---
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# --- Configuração da Wikipedia ---
USER_AGENT = "FURIAFanBot/1.0 (+https://github.com/seuusuario/botfuria; contato@seuemail.com)"
wiki = wikipediaapi.Wikipedia(language='pt', user_agent=USER_AGENT)

# --- Função de fallback para buscar o título mais relevante ---
def buscar_titulo_wiki(query: str) -> str | None:
    api_url = "https://pt.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json",
        "srlimit": 1
    }
    resp = requests.get(api_url, params=params, headers={"User-Agent": USER_AGENT})
    data = resp.json()
    results = data.get("query", {}).get("search", [])
    if results:
        return results[0]["title"]
    return None

# --- Criação dos botões ---
def get_keyboard():
    return InlineKeyboardMarkup([ 
        [InlineKeyboardButton("📅 Fundação", callback_data='fundacao')],
        [InlineKeyboardButton("🎮 Modalidades", callback_data='modalidades')],
        [InlineKeyboardButton("🏆 Conquistas", callback_data='conquistas')],
        [InlineKeyboardButton("🧠 Filosofia", callback_data='filosofia')],
        [InlineKeyboardButton("🌎 Sede", callback_data='sede')],
        [InlineKeyboardButton("🧑‍💼 Fundadores", callback_data='fundadores')],
        [InlineKeyboardButton("👥 Fãs e comunidade", callback_data='comunidade')],
    ])

# --- Handlers ---
async def start(update: Update, context: CallbackContext) -> None:
    IMAGE_URL = "https://upload.wikimedia.org/wikipedia/pt/f/f9/Furia_Esports_logo.png"
    await update.message.reply_photo(IMAGE_URL)

    # Enviar a mensagem com os botões
    await update.message.reply_text(
        "Olá! Eu sou o WikiBot FURIA. Clique em uma opção ou digite sua pergunta:",
        reply_markup=get_keyboard()
    )

async def respond_to_query(update: Update, context: CallbackContext) -> None:
    query = update.message.text.strip().lower()

    # --- Respostas específicas baseadas em palavras-chave ---
    if "kscerato" in query:
        await update.message.reply_text("KSCERATO é um jogador profissional de CS2 da FURIA, conhecido por sua consistência e mira afiada.")
    elif "yuurih" in query:
        await update.message.reply_text("Yuurih é um dos principais jogadores da FURIA no CS2, sendo peça fundamental nas campanhas da equipe.")
    elif "título" in query or "titulo" in query and ("cs" in query or "cs2" in query or "csgo" in query):
        await update.message.reply_text("A FURIA venceu campeonatos como a DreamHack Open e ESL Pro League, mas ainda não conquistou um Major.")
    elif "título" in query or "titulo" in query and ("lol" in query or "league of legends" in query):
        await update.message.reply_text("Até agora, a FURIA ainda não venceu o CBLOL.")
    elif "melhor colocação" in query and "major" in query:
        await update.message.reply_text("A melhor colocação da FURIA em um Major de CS foi o 3º-4º lugar no IEM Rio Major 2022.")
    elif "cbLOL" in query and ("venceu" in query or "ganhou" in query or "campeã" in query):
        await update.message.reply_text("A FURIA ainda não ganhou o CBLOL.")
    elif "fallen" in query and ("entrou" in query or "ingressou" in query):
        await update.message.reply_text("FalleN entrou na FURIA em julho de 2023 para liderar o time de CS2.")
    elif "patrocinador" in query or "patrocina" in query:
        await update.message.reply_text("A FURIA é patrocinada por marcas como Red Bull, PokerStars, Rivalry e outras.")
    elif "youtube" in query:
        await update.message.reply_text("Sim! A FURIA tem um canal no YouTube: https://www.youtube.com/@FURIA")
    elif "twitch" in query or "live" in query:
        await update.message.reply_text("Sim! A FURIA faz transmissões ao vivo na Twitch: https://www.twitch.tv/furia")
    elif "time feminino" in query and ("cs" in query or "cs2" in query or "csgo" in query):
        await update.message.reply_text("Sim, a FURIA possui um time feminino de CS2.")
    elif "rocket league" in query:
        await update.message.reply_text("Os jogadores de Rocket League da FURIA atualmente incluem: CaioTG1, Card e Lostt.")
    elif ("formação" in query or "lineup" in query or "escalação" in query) and ("lol" in query or "league of legends" in query):
        await update.message.reply_text("A formação atual da FURIA no LoL pode mudar a cada split. Confira o site oficial ou redes sociais da FURIA para a lineup atualizada.")
    
    # --- Caso nenhuma resposta personalizada funcione, cai na Wikipedia ---
    else:
        page = wiki.page(query)
        if not page.exists():
            título = buscar_titulo_wiki(query)
            if título:
                page = wiki.page(título)
        if page.exists():
            await update.message.reply_text(page.summary[:1000])
        else:
            await update.message.reply_text(f"Desculpe, não encontrei nada sobre “{query}” na Wikipédia em português.")
    
    # Exibe novamente os botões
    await update.message.reply_text("Escolha outra opção ou digite sua pergunta:", reply_markup=get_keyboard())

async def button_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    data = query.data

    respostas = {
        "fundacao": "📅 A FURIA foi fundada em agosto de 2017, com o objetivo de transformar o cenário competitivo brasileiro e criar uma cultura única de excelência no esporte eletrônico.",
        "modalidades": "🎮 A FURIA atua em diversas modalidades de eSports, incluindo CS2, Valorant, League of Legends, Rocket League, Apex Legends, e outros. A organização busca sempre se destacar em cada uma delas com treinamentos intensos e estratégias inovadoras.",
        "conquistas": "🏆 A FURIA já conquistou títulos expressivos no cenário nacional e internacional, sendo reconhecida como a melhor organização brasileira de eSports em 2020 e 2021. Seus times frequentemente aparecem entre os melhores do mundo.",
        "filosofia": "🧠 A filosofia da FURIA se baseia em disciplina, paixão e superação. Eles acreditam que o talento precisa ser acompanhado de esforço e que o sucesso é consequência de uma mentalidade forte e consistente.",
        "sede": "🌎 A sede principal da FURIA está localizada em São Paulo, Brasil, mas a organização também conta com uma base de operações nos Estados Unidos, mostrando sua expansão internacional.",
        "fundadores": "🧑‍💼 A FURIA foi fundada por Jaime Pádua e André Akkari. Ambos são empreendedores apaixonados por eSports e com grande experiência no mundo dos negócios e do poker profissional.",
        "comunidade": "👥 A FURIA possui uma das comunidades mais apaixonadas do cenário, com torcedores que se identificam com a identidade ousada da organização. Eles frequentemente promovem ações de engajamento e interação com os fãs.",
    }

    texto = respostas.get(data, "❌ Informação não encontrada.")
    # Primeiro, envia a resposta
    await query.message.reply_text(texto)
    # Agora, envia o menu de navegação
    await query.message.reply_text("Escolha outra opção ou digite sua pergunta:", reply_markup=get_keyboard())

def error_handler(update: Update, context: CallbackContext) -> None:
    logger.error("Erro no update %s: %s", update, context.error)

# --- Configuração do bot ---
def main() -> None:
    TOKEN = "7868116621:AAG_g5nfjY2uueQsSozlLRevla1Tg2DgjIY"
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, respond_to_query))
    app.add_error_handler(error_handler)

    app.run_polling()

if __name__ == "__main__":
    main()
