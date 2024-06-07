import requests

def sendMail(subject, bodyHtml, toEmail):

    url = 'https://api-send-mail-mvxl.onrender.com' #http://127.0.0.1:4535/send-mail #https://api-send-mail-mvxl.onrender.com

    # JSON data to be sent in the POST request
    json_data = {
        "subject": subject,
        "recipient": toEmail,
        "message": bodyHtml
    }

    # Sending a POST request with JSON data
    response = requests.post(url, json=json_data)

    # Handling the response
    if response.status_code == 200:
        print("POST request was successful!")
        print("Response:", response.json())
    else:
        print("POST request failed with status code:", response.status_code)

import calendar

def convert_month_to_french(month):
    mois = {
        'jan': 'janvier',
        'feb': 'février',
        'mar': 'mars',
        'apr': 'avril',
        'may': 'mai',
        'jun': 'juin',
        'jul': 'juillet',
        'aug': 'août',
        'sep': 'septembre',
        'oct': 'octobre',
        'nov': 'novembre',
        'dec': 'décembre'
    }
    
    month_key = month[:3].lower()
    
    if month_key in mois:
        return mois[month_key]
    else:
        return month

