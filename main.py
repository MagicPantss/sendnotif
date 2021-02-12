import smtplib
import ssl
from getpass import getpass
import colorama
import os
import requests
from bs4 import BeautifulSoup
from time import time, sleep


URL = 'https://www.bestjobs.eu/ro/locuri-de-munca?keyword=&location=Sibiu&employment_type%5B0%5D=2'
page = requests.get(URL)

colorama.init()

os.system("cls")

print(colorama.Fore.GREEN, """
   _____           _       _                         _
  / ____|         (_)     | |                       | |
 | (___   ___ _ __ _ _ __ | |_   _ __ ___   __ _  __| | ___
  \___ \ / __| '__| | '_ \| __| | '_ ` _ \ / _` |/ _` |/ _ \\
  ____) | (__| |  | | |_) | |_  | | | | | | (_| | (_| |  __/
 |_____/ \___|_|  |_| .__/ \__| |_| |_| |_|\__,_|\__,_|\___|
                    | |  ____          _____      _ _
                    |_| |  _ \        |_   _|    | (_)
                        | |_) |_   _    | | _   _| |_
                        |  _ <| | | |   | || | | | | |
                        | |_) | |_| |  _| || |_| | | |
                        |____/ \__, | |_____\__,_|_|_|
                                __/ |
                               |___/

""", colorama.Style.RESET_ALL)

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "notificarescript@gmail.com"
receiver_email = "iuli2003iuliboss@gmail.com"
password = getpass("Type your password and press enter: ")
while True:
    os.system("cls")
    print(colorama.Fore.MAGENTA, "I am searching for jobs...", colorama.Style.RESET_ALL)
    sleep(60 - time() % 60)
    print()
    print()
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(class_='card-list')
    job_elems = results.find_all('div', class_='job-card')
    job_elems_body = results.find_all('div', class_="panel-body")
                        
    for t_job in job_elems_body:
        titlu = t_job.find(class_='card-title')
        link = t_job.find(class_='card-link')['href']
        print(titlu.text.strip())
        print(f"Apply here: {link}\n")


        message = f"""\
        Subject: New Job Listing Found

        Hi i just found a new job listing.
        Job title: {titlu.text.strip()}
        Apply here: {link}"""

        # Create a secure SSL context
        context = ssl.create_default_context()

        # Try to log in to server and send email
        try:
            server = smtplib.SMTP(smtp_server,port)
            server.ehlo() # Can be omitted
            server.starttls(context=context) # Secure the connection
            server.ehlo() # Can be omitted
            server.login(sender_email, password)
            # TODO: Send email here
            server.sendmail(sender_email, receiver_email, message)
            print(colorama.Fore.RED, "The email has been sent.", colorama.Style.RESET_ALL)
            sleep(600 - time() % 600)

        except Exception as e:
            # Print any error messages to stdout
            print(e)

        finally: server.quit() 
