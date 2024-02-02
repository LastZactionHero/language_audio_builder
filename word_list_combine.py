import os
import csv
from pydub import AudioSegment

PAUSE_MS = 2000
REPETITION_SPACING = 5

words = []
with open("./verbs_with_sentence.csv", mode="r") as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        words.append(lines)


combined_audio = AudioSegment.empty()

z
def combine_segments(combined_audio, segment_en, segment_ja, segment_sentence):
    combined_audio += segment_en
    combined_audio += AudioSegment.silent(duration=PAUSE_MS)
    combined_audio += segment_ja
    combined_audio += AudioSegment.silent(duration=PAUSE_MS)
    combined_audio += segment_ja
    combined_audio += AudioSegment.silent(duration=PAUSE_MS)
    combined_audio += segment_sentence
    combined_audio += AudioSegment.silent(duration=PAUSE_MS)
    combined_audio += segment_sentence
    combined_audio += AudioSegment.silent(duration=PAUSE_MS)
    return combined_audio


for i in range(len(words)):
    print(f"{i}/{len(words)}")

    audio_en = f"./segments/en_{i}.aiff"
    audio_ja = f"./segments/ja_{i}.aiff"
    audio_sentence = f"./segments/sentence_{i}.aiff"

    segment_en = AudioSegment.from_file(audio_en)
    segment_ja = AudioSegment.from_file(audio_ja)
    segment_sentence = AudioSegment.from_file(audio_sentence)

    combined_audio = combine_segments(
        combined_audio, segment_en, segment_ja, segment_sentence
    )

    if i > REPETITION_SPACING:
        repeat_i = i - REPETITION_SPACING
        audio_en = f"./segments/en_{repeat_i}.aiff"
        audio_ja = f"./segments/ja_{repeat_i}.aiff"
        audio_sentence = f"./segments/sentence_{repeat_i}.aiff"

        segment_en = AudioSegment.from_file(audio_en)
        segment_ja = AudioSegment.from_file(audio_ja)
        segment_sentence = AudioSegment.from_file(audio_sentence)

        combined_audio = combine_segments(
            combined_audio, segment_en, segment_ja, segment_sentence
        )

combined_audio.export("./combined_audio.mp3", format="mp3")
