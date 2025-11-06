from flask import Flask, render_template, request, send_from_directory
import pyttsx3
import os

app = Flask(__name__)

# Directory to save generated audio files
AUDIO_FOLDER = "static/audio"
os.makedirs(AUDIO_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def home():
    audio_file = None

    if request.method == "POST":
        text = request.form["text"]
        if text.strip():
            engine = pyttsx3.init()
            engine.setProperty('rate', 150)  # speed
            engine.setProperty('volume', 0.9)

            # You can change the voice if needed
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)  # 0 for male, 1 for female (on Windows)

            # Save speech file
            filename = "speech.mp3"
            filepath = os.path.join(AUDIO_FOLDER, filename)
            engine.save_to_file(text, filepath)
            engine.runAndWait()

            audio_file = f"{AUDIO_FOLDER}/{filename}"

    return render_template("index.html", audio_file=audio_file)

if __name__ == "__main__":
    app.run(debug=True)
