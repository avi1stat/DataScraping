# Qantas Hotel Scraper

This repository contains a Python script that scrapes hotel data from the Qantas website using the `requests` library and BeautifulSoup. The script extracts specific details about available hotel rooms and saves the data in CSV and Excel formats.

## Overview

Fornova is a leader in market intelligence solutions for the online travel and hospitality industries. We provide actionable insights and a unified view of business intelligence to help hotels maximize their revenue potential. One of the essential skills for joining our Support Engineering teams is the ability to scrape, manipulate, and normalize web page content.

## Task

Your task is to:
1. Analyze the provided Qantas hotel URL and determine the necessary requests to extract the required fields.
2. Scrape the website page using the `requests` library in Python.
3. Extract the following information for each hotel rate:
   - Room Name
   - Rate Name
   - Number of Guests
   - Cancellation Policy
   - Price
   - Boolean value indicating if the room is a Top Deal
   - Currency
4. Save the extracted data into a CSV file and an Excel file.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `pandas` library

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/avi1stat/DataScraping.git
   cd DataScraping
   ```

2. Install the required libraries:
   ```bash
   pip install requests beautifulsoup4 pandas
   ```

## Usage

1. Update the check-in and check-out dates in the script as needed.
2. Run the script:
   ```bash
   python script.py
   ```

## Script Description

The script `script.py` performs the following steps:

1. Constructs the URL for the hotel search page with the specified check-in and check-out dates.
2. Sends an HTTP GET request to the URL and retrieves the HTML content.
3. Parses the HTML content using BeautifulSoup.
4. Extracts the required information for each hotel rate and stores it in a list of dictionaries.
5. Converts the list of dictionaries into a Pandas DataFrame.
6. Saves the DataFrame to both CSV and Excel files.

## Example

The following is an example of the extracted data saved in the CSV and Excel files:

| Room Name         | Rate Name     | Number of Guests | Cancellation Policy | Price | Top Deal | Currency |
|-------------------|---------------|------------------|---------------------|-------|----------|----------|
| Deluxe Room       | Standard Rate | 2 guests         | Free cancellation   | $200  | Yes      | USD      |
| Standard Room     | Non-refundable| 2 guests         | Non-refundable      | $150  | No       | USD      |
| ...               | ...           | ...              | ...                 | ...   | ...      | ...      |

## Notes

- Make sure to use a valid User-Agent header to mimic a browser request and avoid being blocked by the website.
- Handle any potential errors or changes in the HTML structure of the target website.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the Apache License.

---

Feel free to modify the `checkin_date` and `checkout_date` variables in the script to scrape data for different date ranges. If you have any questions or encounter issues, please open an issue in this repository.
