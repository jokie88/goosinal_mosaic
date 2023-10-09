import json
import requests
import time
import os

def download_svg(data, start_from=None):
    for item in data:
        # Extracting name and ID
        name = item["meta"]["name"]
        name_number = name.split('#')[-1].strip()  # Extracting number from name
        id_ = item["id"]

        # Resume from a specific filename if provided
        if start_from and int(name_number) < start_from:
            continue

        print(f"Processing {name}...")

        # Constructing URL
        url = f"http://localhost:8080/content/{id_}"

        # Making the GET request to download the SVG
        response = requests.get(url)
        if response.status_code == 200:
            with open(f"{name_number}.svg", "wb") as f:
                f.write(response.content)
            # Save the last successfully downloaded filename
            with open("last_downloaded.txt", "w") as f:
                f.write(name_number)
        else:
            print(f"Failed to download {name}. HTTP Status Code: {response.status_code}")

        # Sleeping for 100ms
        #time.sleep(0.1)

if __name__ == "__main__":
    with open("inscriptions.json", "r") as file:
        data = json.load(file)
    
    start_from = None
    if os.path.exists("last_downloaded.txt"):
        with open("last_downloaded.txt", "r") as f:
            start_from = int(f.read().strip())
    download_svg(data, start_from)
