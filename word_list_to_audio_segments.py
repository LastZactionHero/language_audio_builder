import os
import csv
import pydub

def say_it(text, language, filename):
  voice = "allison"
  if language == 'ja':
    voice = "kyoko"

  command = f"say -v {voice} \"{text}\" -o {filename}"
  os.system(command)


words = []
with open('./verbs_with_sentence.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
    words.append(lines)

for idx, word in enumerate(words):
  print(f"{idx}/{len(words)}")
  text_ja = word[0]
  text_en = word[2]
  text_sentence = word[3]

  filename = f"./segments/ja_{idx}.aiff"
  say_it(text_ja, "ja", filename)

  filename = f"./segments/en_{idx}.aiff"
  say_it(text_en, "en", filename)

  filename = f"./segments/sentence_{idx}.aiff"
  say_it(text_sentence, "ja", filename)