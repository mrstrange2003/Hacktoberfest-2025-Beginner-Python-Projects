# 💱 Currency Converter

A simple yet powerful currency converter built with Python that uses live exchange rates from a free API.

## 📋 Description

This Currency Converter allows users to convert amounts between different currencies using real-time exchange rates. It's beginner-friendly, interactive, and perfect for learning API integration in Python!

## ✨ Features

- 🌍 **Live Exchange Rates** - Fetches real-time currency data
- 💰 **200+ Currencies** - Support for all major world currencies
- 🎨 **Beautiful UI** - Clean terminal interface with emojis
- 📊 **Detailed Results** - Shows conversion result, exchange rate, and timestamp
- ♻️ **Multiple Conversions** - Convert as many times as you want
- 🛡️ **Error Handling** - Robust input validation and error messages

## 🚀 How to Use

### Prerequisites

- Python 3.6 or higher
- Internet connection (for fetching live rates)

### Installation

1. Clone or download this project
2. Install required dependencies:

```bash
pip install -r requirements.txt
```

### Running the Program

```bash
python currency_converter.py
```

### Example Usage

```
Enter source currency (e.g., USD): USD
Enter target currency (e.g., INR): INR
Enter amount to convert: 100

==================================================
💱 CURRENCY CONVERSION RESULT
==================================================
📅 Date: 2025-10-19 15:30:45
💵 100.00 USD = 8350.00 INR
==================================================

📊 Exchange Rate: 1 USD = 83.5000 INR
```

## 🌍 Supported Currencies

Popular currencies include:
- **USD** - US Dollar
- **EUR** - Euro
- **GBP** - British Pound
- **INR** - Indian Rupee
- **JPY** - Japanese Yen
- **AUD** - Australian Dollar
- **CAD** - Canadian Dollar
- **CNY** - Chinese Yuan

...and 200+ more!

## 🛠️ Technologies Used

- **Python 3** - Programming language
- **requests** - For API calls
- **exchangerate-api** - Free currency exchange rate API

## 📁 Project Structure

```
src/vannu07-currency-converter/
│
├── currency_converter.py    # Main program file
├── README.md                 # Project documentation
└── requirements.txt          # Python dependencies
```

## 🎯 Learning Outcomes

By working on this project, you'll learn:
- API integration in Python
- Working with JSON data
- Exception handling
- User input validation
- String formatting
- Object-oriented programming basics

## 🤝 Contributing

This project is part of **Hacktoberfest 2025**! Contributions are welcome.

### Ideas for Enhancement:
- [ ] Add offline mode with cached rates
- [ ] Support for cryptocurrency conversion
- [ ] Historical exchange rate lookup
- [ ] GUI version using Tkinter
- [ ] Save conversion history to file
- [ ] Add currency symbols display

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Varnit Kumar** ([@vannu07](https://github.com/vannu07))

- GitHub: [github.com/vannu07](https://github.com/vannu07)
- LinkedIn: [Varnit Kumar](https://www.linkedin.com/in/varnit-kumar-0883bb251)

## 🌟 Acknowledgments

- Exchange rate data provided by [exchangerate-api.com](https://www.exchangerate-api.com/)
- Built for Hacktoberfest 2025

---

### 💡 Tips

- Use 3-letter ISO currency codes (e.g., USD, EUR, GBP)
- Make sure you have an active internet connection
- Press `Ctrl+C` to exit anytime

---

⭐ **If you found this helpful, please star the repository!**

🎃 **Happy Hacktoberfest 2025!**