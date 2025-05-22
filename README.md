# 📧 AI-Powered Email Composer & Sender

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg )](https://www.python.org/ )
[![Flask](https://img.shields.io/badge/flask-2.x-green.svg )](https://flask.palletsprojects.com/ )
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg )](https://opensource.org/licenses/MIT )

Effortlessly compose professional emails using AI and send them via a modern web interface. This application uses:
- **Groq API** with LLaMA 3.1 8B Instant for email generation
- **Gmail SMTP** for reliable delivery
- **Flask** for backend services
- Responsive web interface with typing animation

## ✨ Key Features

✅ **AI-Powered Drafting**  
Generate polished email bodies from subjects using natural language processing

✅ **One-Click Sending**  
Seamless integration with Gmail's SMTP for immediate delivery

✅ **Modern Interface**  
- Mobile-responsive design
- Dynamic content area with AI typing animation
- Real-time success/error notifications

✅ **Security First**  
Sensitive credentials stored in environment variables (never hard-coded)

## 🛠️ Tech Stack

| Component       | Technology                                                                 |
|-----------------|---------------------------------------------------------------------------|
| **Backend**     | Python 3.7+, Flask, `smtplib`, `python-dotenv`                            |
| **AI Service**  | Groq API (LLaMA 3.1 8B Instant)                                           |
| **Frontend**    | HTML5, CSS3, Vanilla JavaScript                                           |
| **Deployment**  | Gunicorn (WSGI server)                                                    |
| **Dependencies**| `requests`, `flask`, `python-dotenv`                                      |

## 📂 Project Structure

```plaintext
email_sender/
├── app.py          # Flask application routes and logic
├── requirements.txt# Python dependencies list
├── .env            # Environment variables (add to .gitignore)
├── static/
│   └── index.html  # Frontend interface with embedded CSS/JS
└── README.md       # This documentation
