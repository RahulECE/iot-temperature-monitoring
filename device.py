import time
import random
import requests

SERVER_URL = 'http://localhost:5000/data'

def send_data():
    while True:
        temperature = random.uniform(15.0, 25.0)  # Simulate temperature data
        data = {'temperature': temperature}
        response = requests.post(SERVER_URL, json=data)
        print(f"Sent data: {data}, Response: {response.status_code}")
        time.sleep(5)  # Send data every 5 seconds

if __name__ == '__main__':
    send_data()
