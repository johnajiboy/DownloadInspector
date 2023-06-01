import requests

def check_malicious(download_link):
    scan_url = 'https://www.filescan.io/api/scan/url'
    payload = {
        'url': download_link
        }
    headers = {
        "x-apikey": "fQvcUbP0deGU6dToPidZCBDg8p1t7yXrMNDes49k",
        "content-type": "application/x-www-form-urlencoded"
    }

    response = requests.post(scan_url, data=payload, headers=headers)


    if response.status_code == 200:
        data = response.json()
        flow_id = data['flow_id']
        id = f"https://filescan.io/api/scan/${flow_id}/reportfilter=finalVerdict&sorting=string&other=emulationGraph"
        headers = {
        "x-apikey": "fQvcUbP0deGU6dToPidZCBDg8p1t7yXrMNDes49k",
        "Content-Type": "application/json"
        }

        response = requests.get(id, headers=headers)
        if response.status_code == 200:
            data = response.json()
            verdict = data['finalVerdict']['verdict']
            if verdict == "MALICIOUS":
                return True
    return False