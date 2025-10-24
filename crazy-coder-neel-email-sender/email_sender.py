import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd
from datetime import datetime
import time

def send_single_email(sender_email, sender_password, receiver_email, subject, message, smtp_server, smtp_port):
    """
    Send a single email
    """
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        
        msg.attach(MIMEText(message, 'plain'))
        
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  
        server.login(sender_email, sender_password)
        
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        
        return True, "Email sent successfully!"
    
    except Exception as e:
        return False, f"Error: {str(e)}"

def send_bulk_emails(sender_email, sender_password, emails_data, smtp_server, smtp_port, delay=1):
    """
    Send bulk emails with optional delay between sends
    """
    results = []
    total_emails = len(emails_data)
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for i, (receiver_email, subject, message) in enumerate(emails_data):
        status_text.text(f"Sending email {i+1} of {total_emails} to {receiver_email}")
        
        success, message_result = send_single_email(
            sender_email, sender_password, receiver_email, subject, message, smtp_server, smtp_port
        )
        
        results.append({
            'receiver': receiver_email,
            'subject': subject,
            'status': 'Success' if success else 'Failed',
            'message': message_result,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        progress_bar.progress((i + 1) / total_emails)
        
        if i < total_emails - 1:
            time.sleep(delay)
    
    status_text.text("Completed!")
    return results

def main():
    st.set_page_config(page_title="Automated Email Sender", page_icon="📧", layout="wide")
    
    st.title("Automated Email Sender")
    st.markdown("Send single or bulk emails easily using this tool")

    st.sidebar.header("Email Configuration")

    smtp_server = st.sidebar.selectbox(
        "SMTP Server",
        ["smtp.gmail.com", "smtp.outlook.com", "smtp.office365.com", "smtp.mail.yahoo.com", "Custom"]
    )
    
    if smtp_server == "Custom":
        smtp_server = st.sidebar.text_input("Custom SMTP Server")
    
    smtp_port = st.sidebar.number_input("SMTP Port", min_value=1, max_value=65535, value=587)

    st.sidebar.subheader("Sender Credentials")
    sender_email = st.sidebar.text_input("Your Email")
    sender_password = st.sidebar.text_input("Your Password", type="password")
  
    app_mode = st.sidebar.selectbox("Choose Mode", ["Single Email", "Bulk Emails", "Template Manager"])
    
    if app_mode == "Single Email":
        single_email_mode(sender_email, sender_password, smtp_server, smtp_port)
    
    elif app_mode == "Bulk Emails":
        bulk_email_mode(sender_email, sender_password, smtp_server, smtp_port)
    
    elif app_mode == "Template Manager":
        template_manager_mode()

def single_email_mode(sender_email, sender_password, smtp_server, smtp_port):
    st.header("Send Single Email")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        receiver_email = st.text_input("To Email")
        subject = st.text_input("Subject")

        message_template = st.selectbox(
            "Choose Template",
            ["Custom", "Meeting Invitation", "Follow-up", "Newsletter", "Notification"]
        )
    
    with col2:
        if message_template == "Custom":
            message = st.text_area("Message", height=200)
        else:
            template_content = get_template_content(message_template)
            message = st.text_area("Message", value=template_content, height=200)

    if st.button("Send Email", type="primary"):
        if not all([sender_email, sender_password, receiver_email, subject, message]):
            st.error("Please fill all fields!")
        else:
            with st.spinner("Sending email..."):
                success, result_message = send_single_email(
                    sender_email, sender_password, receiver_email, subject, message, smtp_server, smtp_port
                )
            
            if success:
                st.success(result_message)
                st.balloons()
            else:
                st.error(result_message)

def bulk_email_mode(sender_email, sender_password, smtp_server, smtp_port):
    st.header("Send Bulk Emails")
    input_method = st.radio("Choose input method:", ["Manual Entry", "CSV Upload"])
    
    emails_data = []
    
    if input_method == "Manual Entry":
        st.subheader("Add Email Recipients")
        
        col1, col2, col3 = st.columns([2, 2, 1])
        
        with col1:
            emails_input = st.text_area(
                "Email addresses (one per line)",
                placeholder="user1@example.com\nuser2@example.com"
            )
        
        with col2:
            subject = st.text_input("Subject for all emails")
        
        with col3:
            st.write("")
            st.write("")
            use_template = st.checkbox("Use template")
        
        if use_template:
            template = st.selectbox(
                "Template",
                ["Meeting Invitation", "Follow-up", "Newsletter", "Notification"]
            )
            message = st.text_area("Message", value=get_template_content(template), height=150)
        else:
            message = st.text_area("Message", height=150)
        
        if emails_input and subject and message:
            email_list = [email.strip() for email in emails_input.split('\n') if email.strip()]
            emails_data = [(email, subject, message) for email in email_list]
    
    else:  
        st.subheader("Upload CSV File")
        st.info("CSV should have columns: email, subject, message")
        
        uploaded_file = st.file_uploader("Choose CSV file", type="csv")
        
        if uploaded_file is not None:
            try:
                df = pd.read_csv(uploaded_file)
                required_columns = ['email', 'subject', 'message']
                
                if all(col in df.columns for col in required_columns):
                    emails_data = list(zip(df['email'], df['subject'], df['message']))
                    st.success(f"Loaded {len(emails_data)} emails from CSV")
                    st.dataframe(df.head())
                else:
                    st.error("CSV must contain columns: email, subject, message")
            
            except Exception as e:
                st.error(f"Error reading CSV: {str(e)}")
    
    if emails_data and st.button("Send Bulk Emails", type="primary"):
        if not sender_email or not sender_password:
            st.error("Please configure sender credentials in the sidebar")
        else:
            delay = st.slider("Delay between emails (seconds)", min_value=0, max_value=10, value=1)
            
            results = send_bulk_emails(
                sender_email, sender_password, emails_data, smtp_server, smtp_port, delay
            )
            
            st.subheader("Sending Results")
            results_df = pd.DataFrame(results)
            st.dataframe(results_df)
            
            csv = results_df.to_csv(index=False)
            st.download_button(
                label="Download Results as CSV",
                data=csv,
                file_name=f"email_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv"
            )

def template_manager_mode():
    st.header("Email Templates")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Available Templates")
        template_options = ["Meeting Invitation", "Follow-up", "Newsletter", "Notification"]
        selected_template = st.selectbox("Select Template", template_options)
        
        template_content = get_template_content(selected_template)
        edited_template = st.text_area("Template Content", value=template_content, height=300)
    
    with col2:
        st.subheader("Template Preview")
        st.info(selected_template)
        st.text_area("Preview", value=edited_template, height=300, disabled=True)
        
        if st.button("Save Template", type="primary"):
            st.success("Template saved successfully!")

def get_template_content(template_name):
    templates = {
        "Meeting Invitation": """Dear Recipient,

I hope this email finds you well.

I would like to invite you to a meeting scheduled for [Date] at [Time].

Agenda:
- Topic 1
- Topic 2
- Topic 3

Please let me know if this time works for you.

Best regards,
[Your Name]""",
        
        "Follow-up": """Hi [Name],

I'm following up on our previous conversation about [Topic]. 

I wanted to check if you had any questions or if there's anything else I can help with.

Looking forward to hearing from you.

Best regards,
[Your Name]""",
        
        "Newsletter": """Hello Subscriber,

Welcome to our monthly newsletter!

Here are the latest updates:
- Update 1
- Update 2
- Update 3

Thank you for being with us.

Best regards,
[Your Team]""",
        
        "Notification": """Hello,

This is a notification regarding [Subject].

Important information:
- Point 1
- Point 2

Please take appropriate action.

Thank you,
[Your Organization]"""
    }
    
    return templates.get(template_name, "")

if __name__ == "__main__":
    main()