from flask import Flask, render_template
import os
import random

app = Flask(__name__)

images = [
"https://firebasestorage.googleapis.com/v0/b/rickroll-a0455.appspot.com/o/Rick%20Astley%20-%20Never%20Gonna%20Give%20You%20Up%20(Official%20Music%20Video).mp4?alt=media&token=dbadf4e7-edf9-4dfb-812f-27fa12a0598f"
]

@app.route("/")
def index():
    url = random.choice(images)
    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
