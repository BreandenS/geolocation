import json
import requests
import pandas as pd
import time


def read_json_file_data(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def get_geolocation(ip_address):
    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        data = response.json()

        country = data.get("country")
        region = data.get("region")
        city = data.get("city")
        loc = data.get("loc")

        latitude, longitude = loc.split(",") if loc else (None, None)

        return city, region, country, latitude, longitude

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for IP {ip_address}: {e}")
        return None, None, None, None, None


def load_csv_data(file_path, data):
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)


def main():
    file_path = "data.json"

    
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    csv_file_path = f"geolocation_data_{timestamp}.csv"

    data = read_json_file_data(file_path)

    if isinstance(data, list):
        geolocation_data = []

        for item in data:
            ip_address = item.get("ip")
            if ip_address:
                city, region, country, latitude, longitude = get_geolocation(ip_address)
                print(f"IP: {ip_address} - Country: {country}, City: {city}")

                geolocation_data.append(
                    {
                        "IP": ip_address,
                        "City": city,
                        "Region": region,
                        "Country": country,
                        "Latitude": latitude,
                        "Longitude": longitude,
                    }
                )
            else:
                print("No IP address found in the JSON file.")

        load_csv_data(csv_file_path, geolocation_data)
    else:
        print("The JSON file does not contain a list of IP addresses.")


if __name__ == "__main__":
    main()
