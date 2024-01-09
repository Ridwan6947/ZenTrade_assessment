import json
import requests

url = "https://s3.amazonaws.com/open-to-cors/assignment.json"

try:
    response = requests.get(url)
    response.raise_for_status()

    # Save the JSON data to a file
    with open("assignment_data.json", "w") as file:
        file.write(response.text)

    print("Data downloaded successfully.")
except requests.exceptions.HTTPError as errh:
    print(f"HTTP Error: {errh}")