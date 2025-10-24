# 📧 Automated Email Sender (Python + Streamlit)

Welcome to the **Automated Email Sender**, a **Streamlit-based web application** that allows you to send **single or bulk emails** efficiently. This project demonstrates the use of Python for **email automation**, **user interfaces**, and **data handling**.

---

## 🎯 Project Overview

This tool simplifies sending emails for personal or business use.  
It supports:

- **Single email sending** with optional templates.
- **Bulk email sending** via manual entry or CSV upload.
- **Progress tracking** and **status reporting**.
- **Template management** for reusable email content.

---

## 🧱 Features

✅ Send single or bulk emails  
✅ Use predefined templates or custom messages  
✅ CSV upload for bulk emails  
✅ Optional delay between emails  
✅ Progress bar and real-time status updates  
✅ Downloadable results CSV with email statuses  
✅ Simple, interactive UI using Streamlit

---

## 🧠 Concepts Demonstrated

- **Python Email Handling**
  - `smtplib`, `MIMEText`, `MIMEMultipart`
- **Web Interface**
  - Streamlit for interactive forms and data display
- **Data Handling**
  - Pandas for CSV input/output
- **Control Flow & Loops**
  - Sending emails with delay, tracking success/failure
- **Time & Date Handling**
  - Timestamps for sent emails
- **Error Handling**
  - Graceful handling of SMTP errors and invalid inputs

---

## 🏗️ Project Structure

---

## ▶️ How to Run

1. **Clone this repository**

```bash
git clone https://github.com/your-username/automated-email-sender.git
cd automated-email-sender
```

2. **Install Dependencies**

```bash
pip install streamlit pandas
```

3.**Run the app**

```bash
streamlit run automated_email_sender.py
```

4. **Follow the on-screen prompts**

Configure your SMTP server and login credentials.

Choose Single or Bulk email mode.

Select or create email templates.

Send emails and view results in real-time.

# 🔐 How to create a **Gmail App Password** (step‑by‑step)

This short README shows exactly how to create an **app-specific password** for a Google/Gmail account (the 16‑digit password you should use in SMTP scripts/apps instead of your main account password). App passwords let apps that don’t support interactive 2‑Step Verification (2FA) sign in securely without exposing your main password.

> **Important:** You **must** enable **2‑Step Verification** on the Google account before creating an app password. :contentReference[oaicite:0]{index=0}

---

## 📋 Quick overview

1. Enable **2‑Step Verification** for your Google account.
2. Open the **App Passwords** page.
3. Create (generate) a new app password — copy the 16‑character code.
4. Paste that app password into your app (or store it in secrets/env vars).
5. Revoke it anytime from the same page if needed. :contentReference[oaicite:1]{index=1}

---

## 🔎 Full step‑by‑step instructions

### 1. Sign in to your Google Account

- Open your browser and go to [myaccount.google.com](https://myaccount.google.com).
- Sign in with the Google account you want to use for sending email. :contentReference[oaicite:2]{index=2}

### 2. Enable 2‑Step Verification (if not already enabled)

- In **Google Account** click **Security** on the left.
- Under **“Signing in to Google”** find **2‑Step Verification** and click **Get started** / **Turn on**.
- Follow the prompts to add a phone number, Google Prompt or other second factor.
- After completing setup, return to the **Security** page.
  > You cannot create an App Password unless 2‑Step Verification is enabled. :contentReference[oaicite:3]{index=3}

### 3. Open the App Passwords page

- On the **Security** page, find **“Signing in to Google” → App passwords** and click it.
- Or open directly: `https://myaccount.google.com/apppasswords` (you may be prompted to sign in again). :contentReference[oaicite:4]{index=4}

### 4. Create a new app password

1. On the **App passwords** screen you’ll see a form titled **“Select app”** and **“Select device”**.
2. Under **Select app**, pick **Mail** (or choose **Other (Custom name)** and type something meaningful like `Streamlit Emailer`).
3. Under **Select device**, choose the device name (or **Other** and enter e.g. `server` or `streamlit-app`).
4. Click **Generate**.
5. A dialog appears with a **16‑character app password** (displayed as four groups of 4 letters/numbers). **Copy this** — Google will not show it again. :contentReference[oaicite:5]{index=5}

### 5. Use the app password in your SMTP app

- Use the app password **in place of your normal account password** when authenticating via SMTP (e.g., `server.login(sender_email, app_password)`).
- Typical SMTP settings for Gmail:
  - Server: `smtp.gmail.com`
  - Port: `587` (STARTTLS) or `465` (SSL). :contentReference[oaicite:6]{index=6}

### 6. Revoke an app password (if compromised or no longer needed)

- Revisit the **App passwords** page.
- Under **“App passwords”** you’ll see a list of created app passwords and device names — click **Remove** (or the trash icon) for the one you want to revoke. :contentReference[oaicite:7]{index=7}

---

**📸 Sample Usage**

Single Email Mode

Enter recipient, subject, and message.

Choose from templates or write a custom message.

Click Send Email.

Bulk Email Mode

Upload a CSV or enter multiple recipients manually.

Set delay between emails if needed.

Track progress and download results.

Template Manager

View, edit, and save email templates for future use.
