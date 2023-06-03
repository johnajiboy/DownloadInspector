import requests
import time

def check_malicious(download_link):
    scan_url = 'https://www.filescan.io/api/scan/url'
    payload = {
        'url': download_link
        }
    headers = {
        "x-apikey": "cggo-adW_tAzg1KrML9eXpqXy4VVca8hmuxEBAgj",
        "content-type": "application/x-www-form-urlencoded"
    }

    response = requests.post(scan_url, data=payload, headers=headers)


    if response.status_code == 200:
        data = response.json()
        flow_id = data['flow_id']
        id = f"https://filescan.io/api/scan/{flow_id}/report?filter=general&filter=finalVerdict&sorting=string&other=emulationGraph"
        headers = {
        "x-apikey": "cggo-adW_tAzg1KrML9eXpqXy4VVca8hmuxEBAgj",
        "Content-Type": "application/json"
        }

        while True:
            response = requests.get(id, headers=headers)
            if response.status_code == 200:
                data = response.json()
                if data["allFinished"]:
                    is_malicious = False

                    for _, report in data['reports'].items():
                        print(report['finalVerdict']['verdict'])
                        if report['finalVerdict']['verdict'] == 'MALICIOUS':
                            is_malicious = True
                    return is_malicious
                if not data['allFinished']:
                    time.sleep(5)