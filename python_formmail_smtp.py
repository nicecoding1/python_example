from flask import Flask, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        email = request.form.get("email")
        memo = request.form.get("memo")
        file1 = request.files.get("file1")
        file2 = request.files.get("file2")

        msg = MIMEMultipart()
        msg['From'] = "id@naver.com"
        msg['To'] = "id@naver.com"
        msg['Subject'] = "Formmail"
        
        body = f"Name: {name}\nPhone: {phone}\nEmail: {email}\nMemo: {memo}"
        msg.attach(MIMEText(body, 'plain'))

        if file1:
            filename = file1.filename
            attachment = MIMEBase('application', "octet-stream")
            attachment.set_payload((file1.read()))
            encoders.encode_base64(attachment)
            attachment.add_header('Content-Disposition', f'attachment; filename= {filename}')
            msg.attach(attachment)

        if file2:
            filename = file2.filename
            attachment = MIMEBase('application', "octet-stream")
            attachment.set_payload((file2.read()))
            encoders.encode_base64(attachment)
            attachment.add_header('Content-Disposition', f'attachment; filename= {filename}')
            msg.attach(attachment)

        server = smtplib.SMTP('smtp.naver.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login("id@naver.com", "password")
        text = msg.as_string()
        server.sendmail("id@naver.com", "id@naver.com", text)
        server.quit()

        return "Form submitted!"

    return """
        <html>
          <head>
            <title>Formmail</title>
          </head>
          <body>
            <h1>Formmail</h1>
            <form method="post" enctype="multipart/form-data">
              <p>
                <label for="name">Name:</label>
                <input type="text" id="name" name="name">
              </p>
              <p>
                <label for="phone">Phone:</label>
                <input type="text" id="phone" name="phone">
              </p>
              <p>
                <label for="email">Email:</label>
                <input type="text" id="email" name="email">
             </p>
              <p>
                <label for="memo">Memo:</label>
                <textarea id="memo" name="memo"></textarea>
              </p>
              <p>
                <label for="file1">File 1:</label>
                <input type="file" id="file1" name="file1">
              </p>
              <p>
                <label for="file2">File 2:</label>
                <input type="file" id="file2" name="file2">
              </p>
              <p>
                <input type="submit" value="Submit">
              </p>
            </form>
          </body>
        </html>
    """

if __name__ == "__main__":
    app.run()