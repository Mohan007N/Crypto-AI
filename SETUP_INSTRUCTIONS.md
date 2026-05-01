# Setup Instructions for Resend Email Integration

## 1. Install Dependencies

Run this command to install the required packages:

```bash
pip install -r requirements.txt
```

## 2. Environment Variables

The `.env` file has been updated with your Resend API key:

```
RESEND_API_KEY=re_557MLCqo_9YFdafntzYnzMgfTgvhM2Si7
RECIPIENT_EMAIL=mohankrishnan4099@gmail.com
```

## 3. Important: Verify Your Domain (Optional but Recommended)

Currently using the default Resend sender: `onboarding@resend.dev`

To use your own domain:
1. Go to https://resend.com/domains
2. Add and verify your domain
3. Update line 32 in `app.py`:
   ```python
   "from": "Crypto AI <noreply@yourdomain.com>",
   ```

## 4. Run the Application

```bash
python app.py
```

The server will start on http://localhost:5000

## 5. Test the Contact Form

1. Go to http://localhost:5000
2. Scroll to the Contact section
3. Fill out the form with:
   - Name
   - Email
   - Service/Domain (dropdown)
   - Message
4. Click "SEND MESSAGE"
5. Check your email at: mohankrishnan4099@gmail.com

## Features

✅ Beautiful HTML email template with styling
✅ Service/Domain selection included in email
✅ Reply-to functionality (you can reply directly to the sender)
✅ Professional formatting
✅ Error handling
✅ Success/failure notifications

## Email Template Includes:

- Sender's name
- Sender's email (clickable)
- Selected service/domain (highlighted badge)
- Message content (formatted)
- Easy reply option

## Troubleshooting

If emails aren't sending:
1. Check your Resend API key is correct
2. Verify you haven't exceeded Resend's free tier limits
3. Check the console for error messages
4. Make sure `resend` package is installed: `pip install resend`

## Resend Free Tier Limits:

- 100 emails per day
- 3,000 emails per month
- Perfect for contact forms!
