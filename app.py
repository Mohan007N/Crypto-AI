from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
import resend

load_dotenv()

app = Flask(__name__, template_folder='template')

# ─── RESEND API CONFIG ──────────────────────────────────────────
resend.api_key = os.getenv('RESEND_API_KEY', 're_557MLCqo_9YFdafntzYnzMgfTgvhM2Si7')
RECIPIENT_EMAIL = os.getenv('RECIPIENT_EMAIL', 'mohankrishnan4099@gmail.com')  # Your email to receive messages

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

# ─── CONTACT API ────────────────────────────────────────────────
@app.route('/api/contact', methods=['POST'])
def contact():
    try:
        data    = request.get_json()
        name    = data.get('name', '').strip()
        email   = data.get('email', '').strip()
        domain  = data.get('domain', '').strip()
        message = data.get('message', '').strip()

        if not name or not email or not domain or not message:
            return jsonify({'success': False, 'message': 'All fields required.'}), 400

        print(f"📬 Contact → {name} ({email}) - {domain}: {message}")

        try:
            # Send email using Resend API
            params = {
                "from": "Crypto AI <onboarding@resend.dev>",  # Use your verified domain
                "to": [RECIPIENT_EMAIL],
                "reply_to": email,
                "subject": f"[Crypto AI] New Inquiry: {domain} - {name}",
                "html": f"""
                <html>
                    <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                        <div style="max-width: 600px; margin: 0 auto; padding: 20px; background-color: #f9f9f9; border-radius: 10px;">
                            <h2 style="color: #00e5a0; border-bottom: 2px solid #00e5a0; padding-bottom: 10px;">New Contact Form Submission</h2>
                            
                            <div style="background-color: white; padding: 20px; border-radius: 8px; margin-top: 20px;">
                                <p><strong style="color: #555;">Name:</strong> {name}</p>
                                <p><strong style="color: #555;">Email:</strong> <a href="mailto:{email}" style="color: #00e5a0;">{email}</a></p>
                                <p><strong style="color: #555;">Service/Domain:</strong> <span style="background-color: #00e5a0; color: white; padding: 4px 12px; border-radius: 4px; font-size: 14px;">{domain}</span></p>
                                
                                <div style="margin-top: 20px; padding: 15px; background-color: #f5f5f5; border-left: 4px solid #00e5a0; border-radius: 4px;">
                                    <p style="margin: 0;"><strong style="color: #555;">Message:</strong></p>
                                    <p style="margin-top: 10px; white-space: pre-wrap;">{message}</p>
                                </div>
                            </div>
                            
                            <div style="margin-top: 20px; padding: 15px; background-color: #e8f5f1; border-radius: 8px; text-align: center;">
                                <p style="margin: 0; color: #555; font-size: 14px;">Reply directly to this email to respond to {name}</p>
                            </div>
                        </div>
                    </body>
                </html>
                """
            }
            
            resend.Emails.send(params)
            return jsonify({'success': True, 'message': 'Message sent! We\'ll be in touch soon.'})
            
        except Exception as mail_err:
            print(f"⚠️  Resend API error: {mail_err}")
            return jsonify({'success': False, 'message': 'Failed to send email. Please try again.'}), 500

    except Exception as e:
        print(f"❌ Contact error: {e}")
        return jsonify({'success': False, 'message': 'Server error. Please try again.'}), 500


# ─── CAREERS APPLY API (REMOVED - No longer needed) ────────────


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)