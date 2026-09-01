from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()

app = Flask(__name__)

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

SYSTEM_PROMPT = """
You are an expert email assistant.

Generate a reply to the given email.

Follow these rules:

- Maintain the requested tone.
- Be professional.
- Keep grammar perfect.
- Do not invent facts.
- Format like a real email.
- End politely.
"""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():

    data = request.json

    email = data["email"]
    tone = data["tone"]

    completion = client.chat.completions.create(
        model="llama-3.3-70b-specdec",
        messages=[
            {
                "role":"system",
                "content":SYSTEM_PROMPT
            },
            {
                "role":"user",
                "content":f"""
Tone: {tone}

Reply to this email:

{email}
"""
            }
        ],
        temperature=0.5,
    )

    return jsonify({
        "reply":completion.choices[0].message.content
    })


if __name__=="__main__":
    app.run(debug=True)
