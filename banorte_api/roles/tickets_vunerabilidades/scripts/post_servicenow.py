import requests

def get_shas():
    ids = []
    url = "https://example-registry-quay-openshift-operators.apps.cluster-fb9nt.fb9nt.sandbox2847.opentlc.com/api/v1/repository/adminquay/servicenow?vulnerabilities=true"
    headers = {
        "Authorization":"Token JwW3WTiLYjJBbfvbtfKkoBtzdZZ7HPF0c05KMkHp"
    }
    response = requests.get(url,headers=headers, timeout=10)

    if response.status_code == 200:
        data = response.json()
    # por cada tag que se encuentre en quay se obtendran los id llamados 'sha'
        for tag in data['tags']:
            ids.append(data['tags'][tag]['manifest_digest'])
    else:
        print("Error con la solicitud")
    return ids
    
    
shas = get_shas()
print(shas)