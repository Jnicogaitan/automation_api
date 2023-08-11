import requests
import json
import os

url = "https://xhds9ppm77.execute-api.us-east-1.amazonaws.com/dev3/api"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Primera solicitud
body = {
    "operationName": "LoanFunnel",
    "variables": {
        "funnelType": "DESKTOP",
        "funnelName": "car_finance",
        "applicationData": {
            "amount": 21000000,
            "hasInitialFee": True,
            "initialFee": 5000000,
            "installments": 48,
            "gaCampaing": None,
            "gaContent": None,
            "gaSource": None,
            "gaMedium": None,
            "gaLandingPage": None,
            "gaKeyword": None,
            "utmCampaign": None,
            "utmKeyword": None,
            "utmLandingPage": None,
            "utmMedium": None,
            "utmSource": None,
            "analyticsClientId": "No track",
            "fbclid": "",
            "gaGclid": ""
        }
    },
    "query": "mutation LoanFunnel($funnelType: FunnelTypeEnum, $app"
             "licationData: OdinApplicationType!, $funnelName: String) {\n  "
             "loanFunnel(\n    funnelType: $funnelType\n    applicationData: "
             "$applicationData\n    funnelName: $funnelName\n  ) {\n   "
             " nextStep\n    token\n    application {\n      id\n      __typename\n"
             "    }\n    __typename\n  }\n}"
}
response = requests.post(url, headers=headers, data=json.dumps(body))

if response.status_code == 200:
    content = json.loads(response.content)
    print(response, content)
else:
    print("Error en la solicitud: ", response.status_code)

if response.status_code == 200:
    data = response.json()['data']['loanFunnel']
    os.environ['TOKEN'] = data['token']
    os.environ['APP_ID'] = data['application']['id']
else:
    print('Error:', response.status_code)

TOKEN = os.environ['TOKEN']
APP_ID = os.environ['APP_ID']

# Segunda solicitud
body = {
    "operationName": "LoanFunnel",
    "variables": {
        "token": TOKEN,
        "funnelType": "DESKTOP",
        "funnelName": "car_finance",
        "applicationData": {
            "laborOld": "MORE_12_MONTHS",
            "companyName": "r7",
            "otherIncome": [],
            "economicSector": "Consultoria y asesorias",
            "currentDebtValue": 0,
            "id": APP_ID,
            "lastName": "Albarracin Cardenas",
            "firstName": "Johnatan",
            "economicActivity": "EMPLOYEE",
            "income": 3000000,
            "cityResidence": "BOGOTA",
            "stateResidence": "CUNDINAMARCA",
            "mobilePhone": "3105564840",
            "birthdayDate": "30-07-1985",
            "identificationExpedition": "30-07-2005",
            "whenExpectedBuyVehicle": "SOONER",
            "identificationType": "ID",
            "identification": "1032392583",
            "gender": "MALE",
            "emailAddress": "nicolas.gaitan+666@grupor5.com",
            "authorizationCentrals": True
        }
    },
    "query": "mutation LoanFunnel($funnelType: FunnelTypeEnum, "
             "$applicationData: OdinApplicationType!, $funnelName: String, "
             "$token: String) {\n  loanFunnel(\n    funnelType: $funnelType\n   "
             " applicationData: $applicationData\n    funnelName: $funnelName\n   "
             " token: $token\n  ) {\n    nextStep\n    application {\n      id\n     "
             " cityResidence\n      insuranceOptions\n      __typename\n    }\n    __typename\n  }\n}"
}

response = requests.post(url, headers=headers, data=json.dumps(body))

if response.status_code == 200:
    content = json.loads(response.content)
    print(response, content)
else:
    print("Error en la solicitud: ", response.status_code)
