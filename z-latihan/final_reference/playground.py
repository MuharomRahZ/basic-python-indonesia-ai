#TUGAS FINAL PROJECT

import smtplib, ssl, getpass, csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

gmail_sender = input(str("Masukkan akun gmail pengirim: "))
password_sender = getpass.getpass(prompt="Masukkan password pengirim (tersembunyi): ")

    #server.set_debuglevel(1)
    # server.ehlo() #menetapkan localhost
    # server.login(gmail_sender, password_sender) #menetapkan email & pass user/sender

    # emails = []
    # with open('final_reference/receiver_list.txt', 'r') as file: #membaca file rceiver
    #     gmail_receiver = csv.reader(file) #mengatur variabel sebagai receiver
    #     for row in gmail_receiver:
    #         emails.append(row)

    #     # sent_from = gmail_sender #variabel sender
    #     # sent_to = gmail_receiver #variabel receiver
    #     sent_subject = input(str("Masukkan subjek email: ")) #variabel subject
    #     sent_body = input(str("Masukkan isi pesan email: ")) #variabel body

    

sent_subject = input(str("Masukkan subjek email: ")) #variabel subject
sent_body = input(str("Masukkan isi pesan email: ")) #variabel body

emails = []
file = open('final_reference/receiver_list.txt', 'r')
gmail_receiver = csv.reader(file)
for data in gmail_receiver:
    emails.append(data[1])

def sender(recipients, from_email, password, body, subj):
    for data in recipients:
        #deklarasi body email
        message = MIMEMultipart("alternative")

        message['Subject'] = subj
        message['From'] = from_email
        message['To'] =  data[1] #(', ').join(recipients)

        message.attach(MIMEText(body,'plain'))

        context = ssl.create_default_context() #membuat protokol pengiriman email dengan default
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server: #mengatur profil protokol server
            try:
                server.ehlo() #menetapkan localhost
                server.login(from_email, password) #menetapkan email & pass user/sender
                server.send_message(message)
                server.close()

                print('Email sent!')
            except Exception as exception:
                print("Error: %s!\n\n" % exception)


sender(gmail_receiver, gmail_sender, password_sender, sent_body, sent_subject)






# emails = []
# with open('final_reerence/receiver_list.txt', 'r') as file: 
#   gmail_receiver = csv.reader(file) 
#   for row in gmail_receiver: 
#     emails.append(row)

# def sender(recipients, from_email, password, body, subj): 
#   msg = MIMEMultipart()

#   msg['Subject'] = subj
#   msg['From'] = from_email
#   msg['To'] = (', ').join(recipients)

#   msg.attach(MIMEText(body,'plain'))

#   context = ssl.create_default_context()
#   server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)
#   try:
#     server.ehlo
#     #server.starttls()
#     server.login(from_email, password)
#     server.send_message(msg)
#     server.quit()

#     print('Email sent!')
#   except Exception as exception:
#     print("Error: %s!\n\n" % exception)


# sent_subject = input(str("Masukkan subjek email: ")) #variabel subject
# sent_body = input(str("Masukkan isi pesan email: ")) #variabel body
# sender(emails, gmail_sender, password_sender, sent_body, sent_subject)


