#FIX & SEBUAH MODIFIKASI

import smtplib, ssl, getpass, csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

gmail_sender = input(str("Masukkan akun gmail pengirim: "))
password_sender = getpass.getpass(prompt="Masukkan password pengirim (tersembunyi): ")


# context = ssl.create_default_context() #membuat protokol pengiriman email dengan default
# with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server: #mengatur profil protokol server
#     server.ehlo() #menetapkan localhost
#     server.login(gmail_sender, password_sender) #menetapkan email & pass user/sender
#     #emails = []
#     with open('final_reference/receiver_list.txt', 'r') as file: #membaca file rceiver
#         gmail_receiver = csv.reader(file) #mengatur variabel sebagai receiver
#         # for row in gmail_receiver:
#         #     emails.append(row[1])

#         sent_from = gmail_sender #variabel sender
#         sent_to = gmail_receiver #variabel receiver
#         sent_subject = input(str("Masukkan subjek email: ")) #variabel subject
#         sent_body = input(str("Masukkan isi pesan email: ")) #variabel body

#         #deklarasi body email
#         # message = """\
#         # from: %s
#         # to: %s
#         # subject: %s

#         # %s
#         # """ % (sent_from, ", ".join(sent_to), sent_subject, sent_body)
#         message = MIMEMultipart("alternative")
#         message['Subject']=judul_pesan
#         message['From']= user_email
#         message['To']=cetak[1]

#         try:
#             server.sendmail(
#                 sent_from, sent_to, message
#             )
#             server.close()

#             print('Email sent!')
#         except Exception as exception:
#             print("Error: %s!\n\n" % exception)


subj = input(str("Masukkan subjek email: "))
bod = input(str("Masukkan isi pesan email: "))
try:
    file = open('final_reference/receiver_list.txt', 'r')
    receiver = csv.reader(file)
    for data in receiver:
        message = MIMEMultipart('alternative')
        message['Subject'] = subj
        message['From'] = gmail_sender
        message['To'] = data[1]

        bodyPart = bod

        message.attach(MIMEText(bodyPart, 'plain'))

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            try:
                server.ehlo()
                server.login(gmail_sender, password_sender)
                server.sendmail(gmail_sender, data[1], msg=message.as_string())
                server.close()

                print('Email Kepada '+data[0]+' Terkirim!')
            except Exception as exception:
                print("Error: %s!\n\n" % exception)
                #print('Belum Membuat daftar penerima!!\n\n')
    file.close()
except Exception as exception:
    print("Error: %s!\n\n" % exception)


#referensi 
# https://realpython.com/python-send-email/#sending-multiple-personalized-emails
# https://stackoverflow.com/questions/63497437/send-gmail-with-multiple-recipients
# https://stackoverflow.com/questions/38825943/mimemultipart-mimetext-mimebase-and-payloads-for-sending-email-with-file-atta