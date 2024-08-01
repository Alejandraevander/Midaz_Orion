import requests
from requests.auth import HTTPBasicAuth
import os
import time

Folder_Location = input("Enter your Folder Path : ")
# WordPress site details
wp_site_url = "https://zetaorion.com/interlec"
media_endpoint = "/wp-json/wp/v2/media"
upload_url = wp_site_url + media_endpoint

# Authentication (basic authentication)
username = "developer"
password = "qqnQ BmmJ o66N 7INe 2XjL j77c"
auth = HTTPBasicAuth(username, password)

# Path to the folder containing files
folder_path = Folder_Location
files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Upload each file
for file_path in files:
    file_name = os.path.basename(file_path)
    with open(file_path, 'rb') as file:
        response = requests.post(
            upload_url,
            headers={
                'Content-Disposition': f'attachment; filename="{file_name}"'
            },
            files={'file': (file_name, file)},
            auth=auth
        )
        if response.status_code == 201:
            print(f"Successfully uploaded: {file_name}")
        else:
            print(f"Failed to upload: {file_name}, Status code: {response.status_code}")
            print(response.text)

time.sleep(30)