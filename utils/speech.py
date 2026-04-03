from gtts import gTTS
from IPython.display import Audio

def falar(texto):
    tts = gTTS(text=texto, lang='pt')
    arquivo = "resposta.mp3"
    tts.save(arquivo)
    
    return Audio(arquivo, autoplay=True)
