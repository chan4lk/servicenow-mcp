import requests
import json
import sys

def verify_oauth():
    url = "http://localhost:8080/mcp"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    # JSON-RPC request to call list_incidents
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": "list_incidents",
            "arguments": {"limit": 1}
        }
    }
    
    print(f"Sending request to {url}...")
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Body: {response.text}")
        
        if response.status_code == 200:
            data = response.json()
            if "error" in data:
                print("Error in response:", data["error"])
                return False
            else:
                print("Success! Tool call executed.")
                return True
        else:
            print("Request failed.")
            return False
            
    except Exception as e:
        print(f"Exception occurred: {e}")
        return False

if __name__ == "__main__":
    success = verify_oauth()
    sys.exit(0 if success else 1)
