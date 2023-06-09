import requests
import time
import mysql.connector

def check_malicious(download_link):
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="fumCHI@02%w#",
        database="download_inspector"
    )

    cursor = db_connection.cursor()

    # Create scan_results table if it does not exist
    create_table_query = """
    CREATE TABLE IF NOT EXISTS scan_results (
        id INT AUTO_INCREMENT PRIMARY KEY,
        link VARCHAR(255) NOT NULL,
        result TEXT NOT NULL,
        modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )
    """
    cursor.execute(create_table_query)
    db_connection.commit()

    # Check if the link exists in the database
    check_link_query = "SELECT result FROM scan_results WHERE link = %s"
    cursor.execute(check_link_query, (download_link,))
    result = cursor.fetchone()

    if result:
        # If link exists in the database
        stored_response = result[0]
        cursor.close()
        db_connection.close()
        return stored_response
    else:
        # If link does not exist in the database
        response = perform_scanning(download_link)
        # Store the response in the database
        insert_result_query = "INSERT INTO scan_results (link, result) VALUES (%s, %s)"
        cursor.execute(insert_result_query, (download_link, response,))
        db_connection.commit()

        cursor.close()
        db_connection.close()

        return response
    
def perform_scanning(download_link):
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