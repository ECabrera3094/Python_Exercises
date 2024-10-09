import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from_email = 'usuarioshitsss@gmail.com'
password = 'sgxc uknf fibw xbfy'
report_file = "C:\\Automation\\Reportes_Mensuales\\Reporte_Mensual_Usuarios_CD\\Downloads\\Reporte Mensual de Usuarios de Claro Drive - 2024 Sep.txt"

        # Validacion del resultado
if True:
    subject = 'Prueba No Exitosa - Estatus prueba semanal CVMAX'
    body = 'Las validaciones no fueron exitosas.'
else:
    subject = 'Prueba Exitosa - Estatus prueba semanal CVMAX'
    body = 'Las validaciones fueron exitosas.'

msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = 'cabreraemi@globalhitss.com'
msg['Subject'] = subject

msg.attach(MIMEText(body, 'plain'))

with open(report_file, 'rb') as attachment:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header(
        'Content-Disposition',
        f'attachment; filename={os.path.basename(report_file)}',
    )
    msg.attach(part)

try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(from_email, password)
        server.send_message(msg)
        print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {e}")