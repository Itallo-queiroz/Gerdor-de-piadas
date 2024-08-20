# importar biblioteca
import pyjokes # pip install pyjokes
from deep_translator import GoogleTranslator # pip install deep_translator

# Mmudando o Transletor 
tradutor = GoogleTranslator(source='auto', target='pt')

while True:
    piada = pyjokes.get_joke()
    piada_traduzida = tradutor.translate(piada)

    # Saida de dados
    print(piada_traduzida)

    repetir = input('Gerar Outra piada (s/n)? ').lower()

    if repetir == 's':
        continue
    else:
        break



















