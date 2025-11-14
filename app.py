from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

BOT_TOKEN = "8560880538:AAEErDIpS-eOgu38aIr3v3tmUxsh3w5Ef7M"
CHAT_ID = "-1003269524862"

@app.route("/send", methods=["POST"])
def send_message():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "Campo 'text' é obrigatório"}), 400

    text = data["text"]

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        return jsonify({"status": "Mensagem enviada com sucesso!"})
    else:
        return jsonify({"error": "Falha ao enviar mensagem", "details": response.text}), 500

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "API do Bot Telegram está ativa!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)