from translate import Translator

translator = Translator(to_lang='ja')
try:
    with open('./translate.txt') as my_file:
        text = my_file.read()
        result = translator.translate(text)
    with open('./translate-ja.txt', mode='w', encoding='utf-8') as new_file:
        new_file.write(result)
        print('File has been created')
except FileNotFoundError:
    print('File not exist.')
