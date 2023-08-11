import requests
import json
import os
from utils.reader import Reader
from dotenv import load_dotenv


load_dotenv()

url = os.environ['API']
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

#primer solicitud
body = {
    "operationName": "LoanFunnel",
    "variables": {
        "funnelName": "car_equity",
        "funnelType": "DESKTOP",
        "applicationData": {
            "loanUses": "OTHERS",
            "vehicleRegistration": "HWN063",
            "identification": "1032392583",
            "identificationType": "ID",
            "fasecoldaSubreference": None,
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
    "query": "mutation LoanFunnel($funnelType: FunnelTypeEnum, $applicationData:"
             " OdinApplicationType!, $funnelName: String) {\n  loanFunnel(\n "
             "   funnelType: $funnelType\n    applicationData: $applicationData\n"
             "    funnelName: $funnelName\n  ) {\n    nextStep\n    token\n    application "
             "{\n      id\n      vehicleModel\n      vehicleLineName\n      vehicleBrandName\n     "
             " subreferences\n      vehicleClass\n      subreferencesDetails {\n        "
             "code\n        doors\n        gearboxType\n        subreference\n        "
             "airConditioning\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}"
}

response = requests.post(url, headers=headers, data=json.dumps(body))

print(response.text)

if response.status_code == 200:
    content = json.loads(response.content)
    print(response, content)
else:
    print("Error en la solicitud: ", response.status_code)

if response.status_code == 200:
    data = response.json()['data']['loanFunnel']
    os.environ['TOKEN1'] = data['token']
    os.environ['APP_ID1'] = data['application']['id']
    os.environ['SUBREF'] = data['application']['subreferences'][0]
else:
    print('Error:', response.status_code)

TOKEN1 = os.environ['TOKEN1']
APP_ID1 = os.environ['APP_ID1']
SUBREF = os.environ['SUBREF']

#segunda solicitud
body = {
    "operationName":"LoanFunnel",
    "variables":{
        "funnelName":"car_equity",
        "funnelType":"DESKTOP",
        "token": TOKEN1,
        "applicationData":{
            "id":APP_ID1,
            "fasecoldaSubreference": SUBREF
            }
    },
    "query":"mutation LoanFunnel($funnelType: FunnelTypeEnum, $applicationData: "
            "OdinApplicationType!, $funnelName: String, $token: String) {\n  loanFunnel(\n    "
            "funnelType: $funnelType\n    applicationData: $applicationData\n    "
            "funnelName: $funnelName\n    token: $token\n  ) {\n    nextStep\n   "
            " application {\n      id\n      fasecoldaValue\n      vehicleModel\n      "
            "vehicleLineName\n      vehicleClass\n      vehicleBrandName\n      __"
            "typename\n    }\n    __typename\n  }\n}"
}

response = requests.post(url, headers=headers, data=json.dumps(body))

if response.status_code == 200:
    content = json.loads(response.content)
    print(response, content)
else:
    print("Error en la solicitud: ", response.status_code)

#tercera peticion
body = {
    "operationName":"LoanFunnel",
    "variables":{
        "funnelType":"DESKTOP",
        "funnelName":"car_equity",
        "token":TOKEN1,
        "applicationData":{
            "id":APP_ID1,
            "amount":30000000
            }
    },
        "query":"mutation LoanFunnel($token: String, $funnelName: String, "
                "$funnelType: FunnelTypeEnum, $applicationData: OdinApplicationType!)"
                " {\n  loanFunnel(\n    funnelType: $funnelType\n    applicationData: "
                "$applicationData\n    funnelName: $funnelName\n    token: $token\n  ) "
                "{\n    nextStep\n    application {\n      vehicleRegistration\n      vehicleGarment\n"
                "      id\n      amount\n      fasecoldaValue\n      vehicleModel\n      vehicleLineName\n      "
                "vehicleClass\n      vehicleBrandName\n      __typename\n    }\n    __typename\n  }\n}"
}

response = requests.post(url, headers=headers, data=json.dumps(body))

if response.status_code == 200:
    content = json.loads(response.content)
    print(response, content)
else:
    print("Error en la solicitud: ", response.status_code)

#Cuarta peticion
body= {
    "operationName":"LoanFunnel",
    "variables":{
        "token": TOKEN1,
        "funnelType":"DESKTOP",
        "funnelName":"car_equity",
        "applicationData":{
            "birthdayDate":"30-07-1986",
            "identification":"1032392583",
            "identificationType":"ID",
            "identificationExpedition":"30-07-2005",
            "firstName":"jonatan",
            "lastName":"albarracin",
            "gender":"MALE",
            "economicActivity":"EMPLOYEE",
            "emailAddress":"nicolas.gaitan+666@grupor5.com",
            "stateResidence":"CUNDINAMARCA"
            ,"cityResidence":"BOGOTA",
            "mobilePhone":"3105564840",
            "authorizationCentrals":True,
            "otherIncome":[],
            "currentDebtValue":0,
            "income":3000000,
            "id":APP_ID1,
            "laborOld":"MORE_12_MONTHS",
            "companyName":"Rcinco",
            "economicSector":"Tecnología"
        }
    },
            "query":"mutation LoanFunnel($token: String, $funnelName: String, "
                    "$funnelType: FunnelTypeEnum, $applicationData: OdinApplicationType!) "
                    "{\n  loanFunnel(\n    funnelType: $funnelType\n    applicationData: "
                    "$applicationData\n    funnelName: $funnelName\n    token: $token\n  ) "
                    "{\n    nextStep\n    application {\n      id\n      cityResidence\n      insuranceOptions\n      __"
                    "typename\n    }\n    __typename\n  }\n}"
}

response = requests.post(url, headers=headers, data=json.dumps(body))

if response.status_code == 200:
    content = json.loads(response.content)
    print(response, content)
else:
    print("Error en la solicitud: ", response.status_code)

# Quinta peticion
body = {
    "operationName":"LoanFunnel",
    "variables":{
        "token": TOKEN1,
        "funnelType":"DESKTOP",
        "funnelName":"car_equity",
        "applicationData":{
            "id": APP_ID1,
            "notMatchIdentificationReason":"RECENTLY_TRANSFERRED"
        }
    },
    "query":"mutation LoanFunnel($funnelType: FunnelTypeEnum, $applicationData: "
            "OdinApplicationType!, $funnelName: String, $token: String) {\n  loanFunnel(\n    "
            "funnelType: $funnelType\n    applicationData: $applicationData\n    funnelName: "
            "$funnelName\n    token: $token\n  ) {\n    nextStep\n    application {\n      id\n      __"
            "typename\n    }\n    __typename\n  }\n}"
}

response = requests.post(url, headers=headers, data=json.dumps(body))

if response.status_code == 200:
    content = json.loads(response.content)
    print(response, content)
else:
    print("Error en la solicitud: ", response.status_code)