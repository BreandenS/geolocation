This Python script processes JSON data containing IP addresses, timestamps, and URLs visited by users. It retrieves geolocation information for each IP address and stores the results in a CSV file. This tool is useful for analyzing user locations based on their IP addresses.

## Features

- **JSON Parsing**: Extracts IP addresses, timestamps, and URLs from a JSON file.
- **Geolocation API Integration**: Fetches country and city information for each IP address using the `ipinfo.io` API.
- **Data Aggregation**: Combines JSON data with geolocation information.
- **CSV Export**: Outputs the combined data into a CSV file for further analysis.
- **Error Handling**: Manages API request failures and handles edge cases like missing data.
