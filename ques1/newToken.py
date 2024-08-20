import requests

# on every req a new token is generated
def newToken(): 
    url = "http://20.244.56.144/test/auth"

    payload = {
        "companyName": "braveTech",
        "clientID": "9c763c9e-d233-4aee-8cb8-6e2a11d6ab6e",
        "clientSecret": "HebdmHHDIbqHKERQ",
        "ownerName": "Anurag singh",
        "ownerEmail": "anuragbais10@gmail.com",
        "rollNo": "1210439018"
    }

    res = requests.post(url, json=payload)
    
    token = res.json()
    
    return {"access_token": token['access_token'], "token_type": token["token_type"]}