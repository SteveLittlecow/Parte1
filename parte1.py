import pyttsx3
import os


voz = pyttsx3.init('sapi5')


texto = 'Bom, se conseguiu chegar aqui, meus parabéns! Sinta-se inteligente e creio que você deve ter aprendido, ao menos um pouco, sobre a linguagem paiton.'
print(texto)
voz.say(texto)
voz.runAndWait()
texto = 'Posteriormente, vou lhe passar algumas instruções para você conseguir obter o que tenho a lhe oferecer'
print(texto)
voz.say(texto)
voz.runAndWait()
texto = 'Escrevi uma carta que, se tudo não piorar, deverá obter mais partes até para que você consiga entender o motivo em eu ter te mandado esse arquivo'
print(texto)
voz.say(texto)
voz.runAndWait()
texto = 'No mais, por enquanto é somente isso!'
print(texto)
voz.say(texto)
voz.runAndWait()
texto = 'Abraços de perseverença irônica'
print(texto)
voz.say(texto)
voz.runAndWait()
voices = voz.getProperty('voices')
voz.setProperty('voice', voices[1].id)
voz.setProperty('rate', 115)
texto = 'Steve Littecow.'
print(texto)
voz.say(texto)
voz.runAndWait()
print("Acesse esse link para ler a Parte 1: https://drive.google.com/drive/folders/1xgYVS5oyAAAI7XvZfZ5cgy0zYfWPxcz-?usp=sharing")
os.system("PAUSE")