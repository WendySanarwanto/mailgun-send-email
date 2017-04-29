import requests

class MailGunClient:
    def __init__(self, domain, api_key):
        self.api_url = "https://api.mailgun.net/v3/%s" % domain
        print "api_url = %s" % self.api_url
        self.messages_resource_path = "/messages"
        self.api_key = api_key

    def send_mail(self, _from, to, subject, text):
        return requests.post(
            self.api_url + self.messages_resource_path, 
            auth=("api", self.api_key),
            data={"from": _from,
                  "to": to,
                  "subject": subject,
                  "text": text})
