# app.py
from flask import Flask, render_template
import pandas as pd
from datetime import datetime
import os

app = Flask(__name__)

@app.route("/")
def home():
    today = datetime.today().strftime("%Y%m%d")
    filename = f"picks_{today}.txt"

    if os.path.exists(filename):
        df = pd.read_csv(filename, sep="\t")
        data = df.to_dict(orient="records")
    else:
        data = []  # 파일 없으면 빈 값 표시

    return render_template("index.html", data=data)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

