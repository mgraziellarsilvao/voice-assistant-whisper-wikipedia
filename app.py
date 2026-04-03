import whisper
import random
from datetime import datetime
from google.colab import files

from utils.wikipedia_utils import limpar_texto, buscar_wikipedia
from utils.speech import falar

# ==============================
# 🧠 Modelo Whisper
# ==============================
model = whisper.load_model("base")

# ==============================
# 🤖 Assistente
# ==============================
def responder(texto):
    texto_original = texto
    texto = texto.lower()

    if "horas" in texto:
        return f"Agora são {datetime.now().strftime('%H:%M')}"

    if "oi" in texto or "olá" in texto:
        return "Olá! Pode perguntar algo."

    termo = limpar_texto(texto_original)
    resultado = buscar_wikipedia(termo)

    if resultado:
        return resultado

    return random.choice([
        "Não encontrei algo específico, tente perguntar de outra forma.",
        "Ainda não consegui encontrar essa informação.",
        "Pode reformular sua pergunta?"
    ])

# ==============================
# 🔁 Loop principal
# ==============================
print("🤖 Assistente iniciado! Envie áudios.\n")

while True:
    uploaded = files.upload()
    arquivo = list(uploaded.keys())[0]

    if "sair" in arquivo.lower():
        print("👋 Encerrando...")
        break

    result = model.transcribe(arquivo)
    texto = result["text"]

    print(f"🧑 Você: {texto}")

    resposta = responder(texto)

    print(f"🤖 Assistente: {resposta}")

    falar(resposta)
