# !pip install openai
# !pip install pydub
# !pip install srt

import csv
import pydub
import openai

words = []
with open('./verbs.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
    words.append(lines)

# Set your OpenAI API key
openai.api_key = "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"

for idx, word in enumerate(words):
  print(f"{idx}/{len(words)}")
  prompt = f"""Write a simple Japanese sentence using this word in polite present tense: {word[0]}"""

  response = openai.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
          {"role": "user",
            "content": prompt}
      ]
  )
  sentence = response.choices[0].message.content.strip().split(" ")[0]
  word.append(sentence)

with open("./verbs_with_sentence.csv", 'w') as csvfile:
    csvwriter = csv.writer(csvfile)

    # Write the header row (optional)
    for word in words:
      csvwriter.writerow(word)
