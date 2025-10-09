# Python Weather App (Tkinter GUI)

A simple, desktop-based weather application built using Python's Tkinter for the graphical user interface (GUI). It retrieves real-time current conditions and a 5-day forecast without requiring an API key, utilizing free and open-source weather and geocoding services.

## 🚀 Features

* **Location Search**: Easily search for weather in any city or place name worldwide.
* **Non-Blocking UI**: Uses threading to perform network requests (geocoding and weather fetching) in the background, ensuring the GUI remains responsive.
* **Unit Selection**: Allows the user to select preferred units for:
   * **Temperature**: Celsius (°C) or Fahrenheit (°F)
   * **Wind Speed**: km/h, m/s, mph, or knots (kn)
* **Current Conditions**: Displays the current time, temperature, wind speed/direction, and a description with an emoji.
* **5-Day Forecast**: Provides a detailed table showing minimum/maximum temperatures, precipitation, and maximum wind speed for the next five days.
* **APIs Used**:
   * **Geocoding**: [Nominatim (OpenStreetMap)](https://nominatim.openstreetmap.org/) - Converts place names into latitude and longitude coordinates
   * **Weather Data**: [Open-Meteo](https://open-meteo.com/) - Provides free and open-source weather forecast data

## 🛠️ Prerequisites

To run this application, you need:

* **Python 3.x** installed on your system
* **requests** library to handle HTTP requests (Tkinter is included in the standard Python library)

### Check Python Installation

```bash
# Check if you have Python installed
python3 --version
```

## 📦 Installation and Setup

### 1. Install the `requests` library

```bash
pip install requests
```

### 2. Save the file

Save the provided code (e.g., `weather.py`) to your local machine.

### 3. Run the application

Execute the Python script from your terminal:

```bash
python3 weather.py
```

## 📝 Usage

1. The GUI window will open.
2. Enter the name of the city or place (e.g., "London", "Tokyo", "Eiffel Tower").
3. Optionally, select your preferred **Temperature unit** and **Wind speed unit** from the dropdown menus.
4. Click the **"Get Weather"** button.
5. The **Current conditions** and **5-day forecast** will update with the retrieved data. If a location is not found or a network error occurs, an error message will be displayed.

## 👨‍💻 Author
Varnit Kumar

GitHub: https://github.com/vannu07


## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

* [Open-Meteo](https://open-meteo.com/) for providing free weather API
* [Nominatim/OpenStreetMap](https://nominatim.openstreetmap.org/) for geocoding services
* Python Tkinter for the GUI framework
