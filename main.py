import json
from datetime import datetime

# Helper function to convert ISO 8601 timestamp to milliseconds since epoch
def iso_to_millis(iso_str):
    # Replace 'Z' with '+00:00' for correct UTC parsing
    dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
    return int(dt.timestamp() * 1000)

# IMPLEMENT: Convert data-1.json format to unified format
def convert_format1(data):
    unified = []
    for entry in data:
        unified.append({
            "timestamp": iso_to_millis(entry["time"]),
            "machine_id": entry["machineID"],
            "temperature": entry["tempC"],
            "vibration": entry["vibrationHz"]
        })
    return unified

# IMPLEMENT: Convert data-2.json format to unified format
def convert_format2(data):
    unified = []
    for entry in data:
        unified.append({
            "timestamp": entry["ts"],  # already in ms
            "machine_id": entry["id"],
            "temperature": entry["temperature_celsius"],
            "vibration": entry["vibration_hz"]
        })
    return unified

# Main execution: load, convert, merge, sort, save
if __name__ == "__main__":
    # Load both JSON files
    with open("data-1.json") as f1:
        data1 = json.load(f1)
    with open("data-2.json") as f2:
        data2 = json.load(f2)

    # Convert both formats
    unified1 = convert_format1(data1)
    unified2 = convert_format2(data2)

    # Merge and sort by timestamp
    final_data = sorted(unified1 + unified2, key=lambda x: x["timestamp"])

    # Save output to result.json
    with open("result.json", "w") as out:
        json.dump(final_data, out, indent=4)

    print("Conversion complete. Check result.json for output.")
