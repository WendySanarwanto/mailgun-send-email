# Unit tests of MailGunClient class
import mock
import requests
import uuid

from EmailClients import MailGunClient

def test_should_be_able_sending_email_successfully(monkeypatch):
    # Arrange
    domain = "mydomain.com"
    api_key_part = str(uuid.uuid4()).strip('-')
    api_key = "key-%s" % api_key_part
    email_client = MailGunClient(domain, api_key)

    _from = "Admin<admin@%s>" % domain
    to = "mymail@gmail.com"
    subject = "Test mail"
    text = """ \
    Hello, \n
    
    This mail is sent from a python program through MailGun API. \n
    Therefore, no need to reply this mail. \n
    
    Cheers.\n
    My Domain's Administrator
    """

    expected_response = "<Response [200]>"
    def mocked_send_email_return(url, auth, data):
        return expected_response

    monkeypatch.setattr(requests, 'post', mocked_send_email_return)
        
    # Act
    response = email_client.send_mail(_from, to, subject, text)

    # Assert
    assert response == expected_response
