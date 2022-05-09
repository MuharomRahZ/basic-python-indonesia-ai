#COPY PASTE / REFERENSI DARI GITHUB TEMEN2 MENTEE

import smtplib, ssl, getpass, csv

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


judul_pesan = input(f"Masukan Subject Email: ")
user_email =input(f"Email Pengirim: ")
user_pass=getpass.getpass(prompt = "Pass email pengirim(Hidden): \n")

def kirimEmail():
    # judul_pesan = input(f"Masukan Subject Email: ")
    # user_email =input(f"Email Pengirim: ")
    # user_pass=getpass.getpass(prompt = "Pass email pengirim(Hidden): \n")
    try:
        data= open('final_reference/receiver_list.txt','r')
        read_file = csv.reader(data)
        if data=='':
            print('Data Tujuan Masih Kosong')
        for cetak in read_file:
            #message
            pesan = MIMEMultipart("alternative")
            pesan['Subject']=judul_pesan
            pesan['From']= user_email
            pesan['To']=cetak[1]

            body = input(str("Masukkan isi pesan: "))

            pesan.attach(MIMEText(body, 'plain'))

            # #template
            # html = open("Final-Project/template.html")
            # template = MIMEText(html.read(),"html") #membaca file sebagai HTML
            # pesan.attach(template) #masukan template ke pesan

            # #attach file
            # filenameCV='Final-Project/cv.pdf'
            # with open(filenameCV,'rb') as lampiran:
            #     pdf=MIMEBase("application","octet-stream")
            #     pdf.set_payload(lampiran.read())
            #     encoders.encode_base64(pdf)
            #     pesan.attach(pdf)
            #     pdf.add_header(
            #         "Content-Disposition",
            #         "attachment",
            #         filename=filenameCV
            #     )

            #send email
            context = ssl.create_default_context()
            
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:

                try:
                    #server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)
                    server.ehlo()
                    server.login(user_email, user_pass)
                    server.sendmail(user_email, cetak[1], msg=pesan.as_string())
                    server.close()

                    print('Email Kepada '+cetak[0]+' Terkirim!')
                except Exception as exception:
                    print("Error: %s!\n\n" % exception)
                    print('Belum Membuat daftar penerima!!\n\n')
        data.close()
    except Exception as exception:
        print("Error: %s!\n" % exception)

kirimEmail()