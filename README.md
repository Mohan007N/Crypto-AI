# 🌟 Crypto AI

A modern corporate website built with **Flask**, featuring animated UI, contact and job application APIs, and Docker support.

---

## 📋 Pages

| Route | Description |
|---|---|
| `/` | Home / Landing page |
| `/what-we-think` | Blog / Insights |
| `/who-we-are` | About the company |
| `/careers` | Open positions & applications |
| `/founder` | Founder profile |

---

## ⚙️ API Endpoints

### `POST /api/contact`
Send a contact message.

**Request body (JSON):**
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "message": "Hello!"
}
```

### `POST /api/apply`
Submit a job application.

**Request body (JSON):**
```json
{
  "name": "Jane Doe",
  "email": "jane@example.com",
  "role": "AI Engineer",
  "message": "I'd love to join the team."
}
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Gmail account (for email functionality)

### 1. Clone the repo
```bash
git clone <repo-url>
cd "SIRUS STAR"
```

### 2. Create a virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS / Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:
```env
EMAIL_USER=your-gmail@gmail.com
EMAIL_PASS=your-app-password
PORT=5000
```

> **Note:** Use a [Gmail App Password](https://myaccount.google.com/apppasswords), not your regular account password.

### 5. Run the app
```bash
python app.py
```

The app will be available at `http://localhost:5000`.

---

## 🐳 Docker

### Build the image
```bash
docker build -t sirus-star .
```

### Run the container
```bash
docker run -p 5000:5000 --env-file .env sirus-star
```

---

## 🗂️ Project Structure

```
SIRUS STAR/
├── app.py              # Flask application & API routes
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker configuration
├── .env                # Environment variables (not committed)
├── static/             # Static assets (CSS, JS, images)
└── template/           # Jinja2 HTML templates
    ├── index.html
    ├── what-we-think.html
    ├── who-we-are.html
    ├── careers.html
    └── founder.html
```

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask, Flask-Mail
- **Frontend:** HTML, CSS, JavaScript (vanilla)
- **Email:** Gmail SMTP via Flask-Mail
- **Containerisation:** Docker

---

## 📄 License

© Crypto AI. All rights reserved.
