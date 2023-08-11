import smtplib

def send_email(reciever_email,message):
    sender_email='aaditworks@gmail.com'
    sender_password='@ILoveMyself'
    with smtplib.SMTP('smtp.gmail.com',587) as server:
        server.starttls()
        server.login(sender_email,sender_password)
        server.sendmail(sender_email,reciever_email,message)
    return 'Mail Sent'

send_email('aaditjainofficial@gmail.com','Hello Aadit')