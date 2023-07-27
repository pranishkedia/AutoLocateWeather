import requests

def get_ip_address():
    try:
        response = requests.get("https://ipinfo.io")
        if response.status_code == 200:
            data = response.json()
            return data.get('ip')
    except Exception as e:
        print("Error getting IP address:", e)
    return None

def get_location_info(ip_address):
    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}")
        if response.status_code == 200:
            data = response.json()
            return data
    except Exception as e:
        print("Error getting location info:", e)
    return None