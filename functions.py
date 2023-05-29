import requests

def check_malicious(download_link):
    scan_url = 'https://www.virustotal.com/api/v3/urls'
    payload = {
        'url': download_link
        }
    headers = {
        "accept": "application/json",
        "x-apikey": "73d0d5c20acbbfaf894d712fb9ba17992ffaedf60fe16807a774340990a65bf4",
        "content-type": "application/x-www-form-urlencoded"
    }

    response = requests.post(scan_url, data=payload, headers=headers)


    if response.status_code == 200:
        data = response.json()
        if 'data' in data and data['data']['attributes']['last_analysis_stats']['malicious'] > 0:
            return True

    return False
