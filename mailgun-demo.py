import time
from EmailClients import MailGunClient


def main():
    """ Main Program """
    # Instantiate mailgunclient class
    api_key = "" # TODO: Write down the API key here
    domain = "" # TODO: Write down your mail gun's domain 
    emailClient = MailGunClient(domain, api_key)

    _from = "" # TODO: Write sender's email address 
    to = "" # TODO: Write recipient's email address
    subject = "" # TODO: Write email's subject
    text = """ """ # TODO: Write email's body
    response = emailClient.send_mail(_from, to, subject, text)
    print response

if __name__ == '__main__':
    main()