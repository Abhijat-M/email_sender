import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
import requests
import smtplib
from email.mime.text import MIMEText

# Load environment variables from .env
load_dotenv()

# Flask app serving static files
app = Flask(__name__, static_folder="static")

# Configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
EMAIL_USER = os.getenv("EMAIL_USER")  # Your Gmail address
GMAIL_PASSWORD = os.getenv("GMAIL_PASSWORD")  # Your Gmail app password

if not all([GROQ_API_KEY, EMAIL_USER, GMAIL_PASSWORD]):
    raise RuntimeError("Missing one of: GROQ_API_KEY, EMAIL_USER, GMAIL_PASSWORD")

# Serve the frontend
@app.route("/")
def home():
    return app.send_static_file("index.html")

# Generate endpoint (unchanged)
@app.route("/generate", methods=["POST"])
def generate():
    try:
        subject = request.json.get("subject", "").strip()
        prompt = f"Write a professional email with the subject: {subject}"

        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "llama-3.1-8b-instant",
            "messages": [{"role": "user", "content": prompt}]
        }

        resp = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
        resp.raise_for_status()
        body = resp.json()["choices"][0]["message"]["content"].strip()

        return jsonify({"body": body})

    except requests.HTTPError as he:
        return jsonify({"error": "LLM API error", "details": str(he)}), 502
    except Exception as e:
        return jsonify({"error": "Internal server error", "details": str(e)}), 500

# Modified send endpoint using SMTP
@app.route("/send", methods=["POST"])
def send_email():
    try:
        data = request.json
        to_email = data["to"]
        subject = data["subject"]
        body = data["body"]

        # Create email message
        msg = MIMEText(body)
        msg['From'] = EMAIL_USER
        msg['To'] = to_email
        msg['Subject'] = subject

        # Connect to Gmail's SMTP server
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(EMAIL_USER, GMAIL_PASSWORD)
            server.sendmail(EMAIL_USER, [to_email], msg.as_string())

        return jsonify({"status": "Email sent successfully!"}), 200

    except KeyError as ke:
        return jsonify({"error": "Missing field", "details": str(ke)}), 400
    except smtplib.SMTPAuthenticationError:
        return jsonify({"error": "SMTP Authentication failed", "details": "Invalid email or password"}), 401
    except smtplib.SMTPException as e:
        return jsonify({"error": "SMTP error", "details": str(e)}), 500
    except Exception as e:
        return jsonify({"error": "Internal server error", "details": str(e)}), 500

# Launch the app
if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 5000)))