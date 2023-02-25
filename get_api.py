import requests

def get_data(payload):
    url = "https://main--plinuxbeans-team-supergraph.apollographos.net/graphql"
    #payload = "{\"query\":\"{\\r\\n  warehouses  {\\r\\n    name\\r\\n    id\\r\\n    \\r\\n\\r\\n\\r\\n  }\\r\\n}\",\"variables\":{}}"
    headers = {
        'X-Token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTIsIm5hbWUiOiJNYW5pc2ggTWFoYWphbiIsImNvbXBhbnlJZCI6ImYwYjBlOWRkLTkxNjAtNGVkOS04YmI4LTRmMmQ2MWFmNWY5YiIsInVzZXJJZCI6ImVhZmRjNmVjLTcyNDgtNDNmMC04OTJiLTZjN2U1NzRjYjM5MCIsImlhdCI6MTY3MTQ1Mzg3OX0.3Q4uY_TSFyHvIT6G0Uv3y6VKYVvm3oo-5e85DiJsyTQ',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    # print(response.text)
    return response.text

z = get_data("{\"query\":\"{\\r\\n  warehouses  {\\r\\n    name\\r\\n    id\\r\\n    \\r\\n\\r\\n\\r\\n  }\\r\\n}\",\"variables\":{}}")
print(z)

##*****************

# def transform_data():







