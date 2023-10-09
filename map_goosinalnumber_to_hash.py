import json

# Load the mapping from inscriptions.json
with open("inscriptions.json", "r") as json_file:
    data = json.load(json_file)

# Create a mapping from "Goosinals #" to "id"
mapping = {}
for entry in data:
    number = int(entry["meta"]["name"].split("#")[1].strip())
    mapping[number] = entry["id"]

# Process output.txt and replace numbers with ids
with open("output.txt", "r") as file:
    lines = file.readlines()

with open("mapped_output.txt", "w") as file:
    for line in lines:
        number = int(line.strip())  # Assuming each line has only a number
        file.write(mapping[number] + "\n")
