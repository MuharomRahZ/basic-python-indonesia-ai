#TUGAS FINAL PROJECT
#referensi - https://realpython.com/python-send-email/#sending-multiple-personalized-emails

import smtplib, ssl

gmail_sender = input(str("Masukkan akun gmail pengirim: "))
password_sender = input("Masukkan password pengirim: ")


context = ssl.create_default_context() #membuat protokol pengiriman email dengan default
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.ehlo()
    server.login(gmail_sender, password_sender)
    with open(r'C:\Users\ZAKI\Basic-Python-Indonesia-AI\python files\final_3\receiver_list.txt', 'r') as file:
        gmail_receiver = file.read().replace('\n', ',')

        sent_from = gmail_sender
        sent_to = gmail_receiver
        sent_subject = input(str("Masukkan subjek email: "))
        sent_body = input(str("Masukkan isi pesan email: "))

        message = """\
        from: %s
        to: %s
        subject: %s

        %s
        """ % (sent_from, ", ".join(sent_to), sent_subject, sent_body)

        try:
            server.sendmail(
                sent_from, sent_to, message
            )
            server.close()

            print('Email sent!')
        except Exception as exception:
            print("Error: %s!\n\n" % exception)