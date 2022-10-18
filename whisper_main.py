import whisper

model = whisper.load_model("large")
result = model.transcribe("Kai Eskildsen.mp3", verbose=True)
text_file = open("tiny_net_text.txt", "w")
n = text_file.write(result["text"])
text_file.close()
