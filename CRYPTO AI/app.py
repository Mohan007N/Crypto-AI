from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__, template_folder='template')

# ─── MAIL CONFIG ────────────────────────────────────────────────
app.config['MAIL_SERVER']   = 'smtp.gmail.com'
app.config['MAIL_PORT']     = 587
app.config['MAIL_USE_TLS']  = True
app.config['MAIL_USERNAME'] = os.getenv('EMAIL_USER', '').strip()
app.config['MAIL_PASSWORD'] = os.getenv('EMAIL_PASS', '').strip()
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('EMAIL_USER', '').strip()

mail = Mail(app)

# ─── PAGE ROUTES ────────────────────────────────────────────────
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/what-we-think')
def what_we_think():
    return render_template('what-we-think.html')

@app.route('/who-we-are')
def who_we_are():
    return render_template('who-we-are.html')

@app.route('/careers')
def careers():
    return render_template('careers.html')

@app.route('/founder')
def founder():
    return render_template('founder.html')

# ─── CONTACT API ────────────────────────────────────────────────
@app.route('/api/contact', methods=['POST'])
def contact():
    try:
        data    = request.get_json()
        name    = data.get('name', '').strip()
        email   = data.get('email', '').strip()
        message = data.get('message', '').strip()

        if not name or not email or not message:
            return jsonify({'success': False, 'message': 'All fields required.'}), 400

        print(f"📬 Contact → {name} ({email}): {message}")

        try:
            msg = Message(
                subject=f'[Crypto AI] New message from {name}',
                recipients=[app.config['MAIL_USERNAME']],
                reply_to=email,
                body=(
                    f"Name   : {name}\n"
                    f"Email  : {email}\n"
                    f"Message:\n{message}"
                )
            )
            mail.send(msg)
            return jsonify({'success': True, 'message': 'Message sent! We\'ll be in touch soon.'})
        except Exception as mail_err:
            print(f"⚠️  Mail error: {mail_err}")
            # Still return success — message was logged
            return jsonify({'success': True, 'message': 'Message received! (email delivery pending)'})

    except Exception as e:
        print(f"❌ Contact error: {e}")
        return jsonify({'success': False, 'message': 'Server error. Please try again.'}), 500


# ─── CAREERS APPLY API ──────────────────────────────────────────
@app.route('/api/apply', methods=['POST'])
def apply():
    try:
        data    = request.get_json()
        name    = data.get('name', '').strip()
        email   = data.get('email', '').strip()
        role    = data.get('role', '').strip()
        message = data.get('message', '').strip()

        if not name or not email or not role:
            return jsonify({'success': False, 'message': 'Name, email, and role are required.'}), 400

        print(f"🚀 Application → {name} ({email}) for '{role}': {message}")

        try:
            msg = Message(
                subject=f'[Crypto AI Careers] Application: {role} — {name}',
                recipients=[app.config['MAIL_USERNAME']],
                reply_to=email,
                body=(
                    f"New job application received!\n\n"
                    f"Role   : {role}\n"
                    f"Name   : {name}\n"
                    f"Email  : {email}\n"
                    f"Message:\n{message or '—'}"
                )
            )
            mail.send(msg)
            return jsonify({'success': True, 'message': f'Application for {role} received! We\'ll reach out soon.'})
        except Exception as mail_err:
            print(f"⚠️  Mail error: {mail_err}")
            return jsonify({'success': True, 'message': 'Application received! We\'ll review and reach out.'})

    except Exception as e:
        print(f"❌ Apply error: {e}")
        return jsonify({'success': False, 'message': 'Server error. Please try again.'}), 500


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)