import json
import urllib.request
import urllib.error
import time

# Wait for server to start
time.sleep(2)

url = "http://127.0.0.1:8002/api/tasks/"
data = {"title": "debug task"}
headers = {"Content-Type": "application/json"}

req = urllib.request.Request(url, data=json.dumps(data).encode(), headers=headers)

print(f"Sending POST to {url}...")
try:
    with urllib.request.urlopen(req) as f:
        print("Success!")
        print(f.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e.code}")
    print(e.read().decode('utf-8'))
except Exception as e:
    print(f"Error: {e}")
