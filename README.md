# Phone Number Details Finder

This Python script extracts various details from a phone number, such as the time zone, carrier, and region, using the `phonenumbers` library.

## Features

- Parses and validates phone numbers.
- Retrieves time zone(s) associated with the phone number.
- Identifies the carrier of the phone number.
- Provides the geographical region or country for the phone number.

## Requirements

- Python 3.x
- `phonenumbers` library

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/phone-number-details-finder.git
    ```
2. **Navigate to the project directory:**
    ```bash
    cd phone-number-details-finder
    ```
3. **Install the required library:**
    ```bash
    pip install phonenumbers
    ```

## Usage

1. **Run the script:**
    ```bash
    python find_phone_details.py
    ```
2. **Enter the phone number when prompted.** The phone number should be in international format (e.g., +14155552671).

## Example

When you run the script and enter a phone number, you will see output similar to this:

```plaintext
Enter phone number: +14155552671
Phone Number: Country Code: 1 National Number: 4155552671
Time Zones: ('America/Los_Angeles',)
Carrier: AT&T Wireless
Region: United States
```

## Error Handling

- The script will notify you if the phone number is not possible or not valid.
- It gracefully handles exceptions related to parsing errors.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## Acknowledgements

- [Google's libphonenumber](https://github.com/google/libphonenumber): The original library on which the `phonenumbers` Python library is based.

---

Feel free to customize it further based on your specific needs and repository details.
