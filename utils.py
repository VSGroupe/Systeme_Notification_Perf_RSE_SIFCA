import requests

def sendMail(subject, bodyHtml, toEmail):
    url = 'https://api-send-mail.onrender.com/api/send-mail'

    # JSON data to be sent in the POST request
    json_data = {
        "subject": subject,
        "toEmail": toEmail,
        "bodyHtml": bodyHtml
    }

    # Sending a POST request with JSON data
    response = requests.post(url, json=json_data)

    # Handling the response
    if response.status_code == 200:
        print("POST request was successful!")
        print("Response:", response.json())
    else:
        print("POST request failed with status code:", response.status_code)
