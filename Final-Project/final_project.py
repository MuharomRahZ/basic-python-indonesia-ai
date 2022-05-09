#TUGAS FINAL PROJECT

import smtplib, ssl, getpass, csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

gmail_sender = input(str("Masukkan akun gmail pengirim: ")) #variabel pengirim
password_sender = getpass.getpass(prompt="Masukkan password pengirim (tersembunyi): ") #variabel password pengirim
sent_subject = input(str("Masukkan subjek email: ")) #variabel subject
sent_body = input(str("Masukkan isi pesan email: ")) #variabel body


try:
    file = open(r'C:\Users\ZAKI\Basic-Python-Indonesia-AI\basic-python-indonesia-ai\Final-Project\receiver_list.txt', 'r') #membuka file receiver_list.txt
    receiver = csv.reader(file) #variabel receiver email
    for data in receiver: #untuk setiap data receiver dilakukan
        message = MIMEMultipart('alternative') #penggunaan MIMEMultipart sebagai template pesan
        message['Subject'] = sent_subject #menyertakan subjek email
        message['From'] = gmail_sender #menyertakan pengirim email
        message['To'] = data[1] #menyertakan penerima email

        bodyPart = sent_body #variabel penampung bodypart email

        message.attach(MIMEText(bodyPart, 'plain')) #menyertakan bodypart pesan email

        context = ssl.create_default_context() #membuat protokol pengiriman email dengan default
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server: #mengatur profil protokol server
            try: #dilakukan
                server.ehlo() #menetapkan localhost
                server.login(gmail_sender, password_sender) #menetapkan akun user pengirim
                server.sendmail(gmail_sender, data[1], msg=message.as_string()) #menetapkan pengirim, penerima, & isi pesan email
                server.close() #setelah selesai mengirim, server akan berhenti

                print('Email Kepada '+data[0]+' Berhasil Terkirim!') #menyampaikan pesan berhasil terkirim
            except Exception as exception: #exception handling - jika try di atas error
                print("Error: %s!\n\n" % exception) #menyertakan / memberitahukan alasan error try
    file.close() #data selesai
except Exception as exception: #exception handling - jika try di atas error
    print("Error: %s!\n\n" % exception) #menyertakan / memberitahukan alasan error try




#referensi 
# https://realpython.com/python-send-email/#sending-multiple-personalized-emails
# https://stackoverflow.com/questions/63497437/send-gmail-with-multiple-recipients
# https://stackoverflow.com/questions/38825943/mimemultipart-mimetext-mimebase-and-payloads-for-sending-email-with-file-atta