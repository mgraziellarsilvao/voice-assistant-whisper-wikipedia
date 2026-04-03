import wikipedia

wikipedia.set_lang("pt")

def limpar_texto(texto):
    palavras_remover = [
        "o que é", "quem é", "me fale sobre",
        "explique", "gostaria de saber", "pode me dizer"
    ]

    texto = texto.lower()

    for p in palavras_remover:
        texto = texto.replace(p, "")

    return texto.strip()


def buscar_wikipedia(termo):
    try:
        return wikipedia.summary(termo, sentences=2)
    except:
        return None
