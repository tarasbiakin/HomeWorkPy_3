# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.

import re
text = input('Введите слово  ').upper()


def isCyrillic(text):
	return bool(re.search('[а-яА-Я]', text))

dikt_en = {1:'AEIOULNSTR',
      	2:'DG',
      	3:'BCMP',
      	4:'FHVWY',
      	5:'K',
      	8:'JZ',
      	10:'QZ'}

dikt_ru = {1:'АВЕИНОРСТ',
      	2:'ДКЛМПУ',
      	3:'БГЁЬЯ',
      	4:'ЙЫ',
      	5:'ЖЗХЦЧ',
      	8:'ШЭЮ',
      	10:'ФЩЪ'}

if isCyrillic(text):
	print(sum([k for i in text for k, v in dikt_ru.items() if i in v]))
else:
	print(sum([k for i in text for k, v in dikt_en.items() if i in v]))
