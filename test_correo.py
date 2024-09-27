import smtplib 
import ssl
from email.message import EmailMessage

msg = EmailMessage()
msg.set_content("Mensaje del Correo")
msg["Subject"] = "Titulo del Coreo"
msg["From"] = "correo1@hotmail.com"
recipients = ["correo2@hotmail"]
msg["To"] = ", ".join(recipients)

# Adjuntar Archivo
with open("resultados.txt", 'rb') as content_file:
    content = content_file.read()
    msg.add_attachment(content, maintype = 'application', subtype = 'txt', filename = 'resultados.txt')

context = ssl.create_default_context()

with smtplib.SMTP("smtp.office365.com", port=587) as smtp:
    smtp.starttls(context = context)
    smtp.login(msg["From"], "Password1") # -- Password del correo Saliente
    smtp.send_message(msg)