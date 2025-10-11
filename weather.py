#!/usr/bin/env python3
"""
Weather App (Tkinter GUI)
Uses Nominatim (OpenStreetMap) to geocode and Open-Meteo for weather (no API key).
"""
import tkinter as tk
from tkinter import ttk, messagebox
import threading
import requests

NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"
OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"
HEADERS = {"User-Agent": "vannu07-weather-app/1.0"}

# Mapping from Open-Meteo weather codes to a simple description and emoji
WEATHER_CODE_MAP = {
    0: ("Clear sky", "☀️"),
    1: ("Mainly clear", "🌤️"),
    2: ("Partly cloudy", "⛅"),
    3: ("Overcast", "☁️"),
    45: ("Fog", "🌫️"),
    48: ("Depositing rime fog", "🌫️"),
    51: ("Light drizzle", "🌦️"),
    53: ("Moderate drizzle", "🌦️"),
    55: ("Dense drizzle", "🌧️"),
    56: ("Light freezing drizzle", "🌧️"),
    57: ("Dense freezing drizzle", "🌧️"),
    61: ("Slight rain", "🌦️"),
    63: ("Moderate rain", "🌧️"),
    65: ("Heavy rain", "🌧️"),
    66: ("Light freezing rain", "🌧️"),
    67: ("Heavy freezing rain", "🌧️"),
    71: ("Slight snow fall", "🌨️"),
    73: ("Moderate snow fall", "🌨️"),
    75: ("Heavy snow fall", "❄️"),
    77: ("Snow grains", "🌨️"),
    80: ("Slight rain showers", "🌦️"),
    81: ("Moderate rain showers", "🌦️"),
    82: ("Violent rain showers", "⛈️"),
    85: ("Slight snow showers", "🌨️"),
    86: ("Heavy snow showers", "❄️"),
    95: ("Thunderstorm", "⛈️"),
    96: ("Thunderstorm with slight hail", "⛈️"),
    99: ("Thunderstorm with heavy hail", "⛈️"),
}

def geocode(city):
    params = {"q": city, "format": "json", "limit": 1}
    r = requests.get(NOMINATIM_URL, params=params, headers=HEADERS, timeout=10)
    r.raise_for_status()
    data = r.json()
    if not data:
        raise ValueError("Location not found")
    return float(data[0]["lat"]), float(data[0]["lon"]), data[0].get("display_name", city)

def fetch_weather(lat, lon, temperature_unit="celsius", windspeed_unit="kmh"):
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
        "timezone": "auto",
        "temperature_unit": temperature_unit,
        "windspeed_unit": windspeed_unit,
        "daily": "weathercode,temperature_2m_max,temperature_2m_min,precipitation_sum,windspeed_10m_max",
        "forecast_days": 5,
    }
    r = requests.get(OPEN_METEO_URL, params=params, timeout=10)
    r.raise_for_status()
    return r.json()

class WeatherApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Weather App")
        self.geometry("680x480")
        self.resizable(False, False)

        # Basic ttk styling
        style = ttk.Style(self)
        try:
            style.theme_use("clam")
        except Exception:
            pass
        style.configure("TButton", padding=6)
        style.configure("TLabel", padding=2)

        frm = ttk.Frame(self, padding=12)
        frm.pack(fill=tk.BOTH, expand=True)

        top_row = ttk.Frame(frm)
        top_row.pack(fill=tk.X)

        ttk.Label(top_row, text="Enter city or place:").pack(anchor=tk.W, side=tk.LEFT)
        self.city_var = tk.StringVar()
        entry = ttk.Entry(top_row, textvariable=self.city_var)
        entry.pack(fill=tk.X, padx=6, pady=6, expand=True, side=tk.LEFT)
        entry.bind("<Return>", lambda e: self.on_get_weather())

        units_row = ttk.Frame(frm)
        units_row.pack(fill=tk.X)
        ttk.Label(units_row, text="Temperature unit:").pack(side=tk.LEFT)
        self.temp_unit_var = tk.StringVar(value="celsius")
        temp_combo = ttk.Combobox(units_row, textvariable=self.temp_unit_var, state="readonly", width=10,
                                  values=["celsius", "fahrenheit"])
        temp_combo.pack(side=tk.LEFT, padx=(6, 12))

        ttk.Label(units_row, text="Wind speed unit:").pack(side=tk.LEFT)
        self.wind_unit_var = tk.StringVar(value="kmh")
        wind_combo = ttk.Combobox(units_row, textvariable=self.wind_unit_var, state="readonly", width=10,
                                  values=["kmh", "ms", "mph", "kn"])
        wind_combo.pack(side=tk.LEFT, padx=(6, 12))

        self.get_btn = ttk.Button(units_row, text="Get Weather", command=self.on_get_weather)
        self.get_btn.pack(side=tk.RIGHT)

        self.status = ttk.Label(frm, text="", foreground="blue")
        self.status.pack(anchor=tk.W)

        content = ttk.Frame(frm)
        content.pack(fill=tk.BOTH, expand=True)

        left = ttk.Frame(content)
        left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 6))
        right = ttk.Frame(content)
        right.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        ttk.Label(left, text="Current conditions").pack(anchor=tk.W)
        self.output = tk.Text(left, height=10, state=tk.DISABLED, wrap=tk.WORD)
        self.output.pack(fill=tk.BOTH, expand=True, pady=6)

        ttk.Label(right, text="5-day forecast").pack(anchor=tk.W)
        columns = ("date", "min", "max", "code", "precip", "wind")
        self.tree = ttk.Treeview(right, columns=columns, show="headings", height=8)
        self.tree.heading("date", text="Date")
        self.tree.heading("min", text="Min")
        self.tree.heading("max", text="Max")
        self.tree.heading("code", text="Weather")
        self.tree.heading("precip", text="Precip")
        self.tree.heading("wind", text="Wind")
        for col, w in zip(columns, (110, 70, 70, 160, 80, 80)):
            self.tree.column(col, width=w, anchor=tk.CENTER)
        self.tree.pack(fill=tk.BOTH, expand=True, pady=6)

    def on_get_weather(self):
        city = self.city_var.get().strip()
        if not city:
            messagebox.showwarning("Input required", "Please enter a city or place name.")
            return
        self.get_btn.config(state=tk.DISABLED)
        self.status.config(text="Fetching...")
        temperature_unit = self.temp_unit_var.get()
        windspeed_unit = self.wind_unit_var.get()
        threading.Thread(target=self._worker, args=(city, temperature_unit, windspeed_unit), daemon=True).start()

    def _worker(self, city, temperature_unit, windspeed_unit):
        try:
            lat, lon, display = geocode(city)
            weather = fetch_weather(lat, lon, temperature_unit=temperature_unit, windspeed_unit=windspeed_unit)
            cw = weather.get("current_weather", {})
            daily = weather.get("daily", {})
            self.after(0, self._update_ui_success, display, cw, daily, temperature_unit, windspeed_unit)
        except requests.exceptions.HTTPError as http_err:
            self.after(0, self._show_error, f"Network error: {http_err}")
        except requests.exceptions.Timeout:
            self.after(0, self._show_error, "Request timed out. Please try again.")
        except ValueError as ve:
            self.after(0, self._show_error, str(ve))
        except Exception as e:
            self.after(0, self._show_error, f"Unexpected error: {e}")
        finally:
            self.after(0, self._finalize_request)

    def _finalize_request(self):
        self.get_btn.config(state=tk.NORMAL)
        self.status.config(text="")

    def _update_ui_success(self, display, cw, daily, temperature_unit, windspeed_unit):
        self._update_output(display, cw, temperature_unit, windspeed_unit)
        self._update_forecast(daily, temperature_unit, windspeed_unit)

    def _update_output(self, display, cw, temperature_unit, windspeed_unit):
        text = []
        text.append(f"Location: {display}")
        if not cw:
            text.append("No current weather available.")
        else:
            code = cw.get('weathercode')
            desc, emoji = WEATHER_CODE_MAP.get(code, ("Unknown", "❔"))
            temp_unit_symbol = "°C" if temperature_unit == "celsius" else "°F"
            wind_unit_label = {
                "kmh": "km/h",
                "ms": "m/s",
                "mph": "mph",
                "kn": "kn",
            }.get(windspeed_unit, windspeed_unit)

            text.append(f"Time: {cw.get('time')}")
            text.append(f"Conditions: {desc} {emoji} (code {code})")
            text.append(f"Temperature: {cw.get('temperature')} {temp_unit_symbol}")
            text.append(f"Wind: {cw.get('windspeed')} {wind_unit_label} from {cw.get('winddirection')}°")
        self._set_text("\n".join(text))

    def _update_forecast(self, daily, temperature_unit, windspeed_unit):
        for iid in self.tree.get_children():
            self.tree.delete(iid)

        if not daily:
            return

        dates = daily.get("time", [])
        tmin = daily.get("temperature_2m_min", [])
        tmax = daily.get("temperature_2m_max", [])
        wcode = daily.get("weathercode", [])
        precip = daily.get("precipitation_sum", [])
        wmax = daily.get("windspeed_10m_max", [])

        temp_unit_symbol = "°C" if temperature_unit == "celsius" else "°F"
        wind_unit_label = {
            "kmh": "km/h",
            "ms": "m/s",
            "mph": "mph",
            "kn": "kn",
        }.get(windspeed_unit, windspeed_unit)

        for i in range(min(len(dates), 5)):
            code = wcode[i] if i < len(wcode) else None
            desc, emoji = WEATHER_CODE_MAP.get(code, ("Unknown", "❔"))
            self.tree.insert(
                "",
                tk.END,
                values=(
                    dates[i],
                    f"{tmin[i]} {temp_unit_symbol}" if i < len(tmin) else "-",
                    f"{tmax[i]} {temp_unit_symbol}" if i < len(tmax) else "-",
                    f"{desc} {emoji}",
                    f"{precip[i]} mm" if i < len(precip) else "-",
                    f"{wmax[i]} {wind_unit_label}" if i < len(wmax) else "-",
                ),
            )

    def _set_text(self, s):
        self.output.config(state=tk.NORMAL)
        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, s)
        self.output.config(state=tk.DISABLED)

    def _show_error(self, msg):
        messagebox.showerror("Error", msg)

if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()
