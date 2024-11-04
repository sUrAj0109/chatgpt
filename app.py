from flask import Flask, request, render_template, jsonify
import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

# Set OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    question = request.form.get("question")

    try:
        # Using the updated method for creating a chat completion
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": question},
            ]
        )
        answer = response.choices[0].message.content  # Updated way to access the answer
        return jsonify({"answer": answer})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True,port=5001)
