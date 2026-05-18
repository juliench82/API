# Weather Forecast API

Simple Python script that fetches a 5-day weather forecast using the [OpenWeatherMap API](https://openweathermap.org/api).

## Features

- Pulls 3-hour interval forecast data for any city
- Uses environment variables for configuration
- Basic error handling for network and API issues

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/juliench82/API.git
   cd API
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory:
   ```env
   OPENWEATHERMAP_API_KEY=your_api_key_here
   CITY=Kyiv
   COUNTRY_CODE=UA
   ```

4. Run the script:
   ```bash
   python API.py
   ```

## Environment Variables

| Variable                  | Description                        | Example |
|---------------------------|------------------------------------|---------|
| `OPENWEATHERMAP_API_KEY`  | Your OpenWeatherMap API key        | `abc123...` |
| `CITY`                    | City name                          | `Kyiv` |
| `COUNTRY_CODE`            | ISO country code                   | `UA` |

## Notes

- Get a free API key from [OpenWeatherMap](https://openweathermap.org/api).
- The script uses the free 5-day/3-hour forecast endpoint.

## Author

**Julien Chevallier**

- [LinkedIn](https://www.linkedin.com/in/julienc82/)
- [GitHub](https://github.com/juliench82)
