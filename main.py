from greets import greetings
from translate import Translator

translator = Translator(to_lang="pt")

for i in greetings:
    print(translator.translate(i).title())

