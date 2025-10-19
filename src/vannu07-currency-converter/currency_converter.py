"""
Currency Converter - Hacktoberfest 2025 (IMPROVED VERSION)
Author: vannu07
Description: Enhanced currency converter with validation and fallback rates
"""

import requests
from datetime import datetime

# Fallback exchange rates (in case API fails)
FALLBACK_RATES = {
    'USD': 1.0,
    'EUR': 0.92,
    'GBP': 0.79,
    'INR': 83.12,
    'JPY': 149.50,
    'AUD': 1.53,
    'CAD': 1.36,
    'CNY': 7.24,
    'CHF': 0.88,
    'AED': 3.67,
    'SGD': 1.34,
    'MXN': 17.05,
    'BRL': 4.97,
    'ZAR': 18.75,
    'KRW': 1320.50
}

CURRENCY_NAMES = {
    'USD': 'US Dollar',
    'EUR': 'Euro',
    'GBP': 'British Pound',
    'INR': 'Indian Rupee',
    'JPY': 'Japanese Yen',
    'AUD': 'Australian Dollar',
    'CAD': 'Canadian Dollar',
    'CNY': 'Chinese Yuan',
    'CHF': 'Swiss Franc',
    'AED': 'UAE Dirham',
    'SGD': 'Singapore Dollar',
    'MXN': 'Mexican Peso',
    'BRL': 'Brazilian Real',
    'ZAR': 'South African Rand',
    'KRW': 'South Korean Won'
}

class CurrencyConverter:
    def __init__(self):
        self.api_url = "https://api.exchangerate-api.com/v4/latest/"
        self.use_fallback = False
        
    def get_exchange_rates(self, base_currency):
        """Fetch live exchange rates with fallback"""
        try:
            response = requests.get(f"{self.api_url}{base_currency}", timeout=5)
            response.raise_for_status()
            data = response.json()
            self.use_fallback = False
            return data['rates']
        except Exception as e:
            print(f"⚠️  API unavailable, using offline rates...")
            self.use_fallback = True
            return self.calculate_fallback_rates(base_currency)
    
    def calculate_fallback_rates(self, base_currency):
        """Calculate rates based on fallback data"""
        if base_currency not in FALLBACK_RATES:
            return None
        
        base_rate = FALLBACK_RATES[base_currency]
        rates = {}
        
        for currency, rate in FALLBACK_RATES.items():
            rates[currency] = rate / base_rate
        
        return rates
    
    def is_valid_currency(self, currency_code):
        """Check if currency code is valid"""
        return currency_code.upper() in FALLBACK_RATES
    
    def convert(self, amount, from_currency, to_currency):
        """Convert amount from one currency to another"""
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()
        
        # Validate currencies
        if not self.is_valid_currency(from_currency):
            print(f"❌ Invalid currency code: {from_currency}")
            print(f"💡 Available currencies: {', '.join(FALLBACK_RATES.keys())}")
            return None
        
        if not self.is_valid_currency(to_currency):
            print(f"❌ Invalid currency code: {to_currency}")
            print(f"💡 Available currencies: {', '.join(FALLBACK_RATES.keys())}")
            return None
        
        if from_currency == to_currency:
            print("❌ Source and target currencies cannot be the same!")
            return None
        
        rates = self.get_exchange_rates(from_currency)
        
        if rates is None:
            print("❌ Unable to fetch exchange rates. Please try again later.")
            return None
        
        converted_amount = amount * rates[to_currency]
        rate = rates[to_currency]
        
        return {
            'amount': converted_amount,
            'rate': rate,
            'from': from_currency,
            'to': to_currency,
            'original': amount
        }
    
    def display_conversion(self, result):
        """Display formatted conversion result"""
        print("\n" + "="*55)
        print("💱 CURRENCY CONVERSION RESULT")
        print("="*55)
        
        if self.use_fallback:
            print("⚠️  Note: Using offline rates (API unavailable)")
        
        print(f"📅 Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"\n💵 {result['original']:.2f} {result['from']} ({CURRENCY_NAMES[result['from']]})")
        print(f"   ↓")
        print(f"💰 {result['amount']:.2f} {result['to']} ({CURRENCY_NAMES[result['to']]})")
        print(f"\n📊 Exchange Rate: 1 {result['from']} = {result['rate']:.4f} {result['to']}")
        print("="*55 + "\n")

def print_banner():
    """Display welcome banner"""
    banner = """
    ╔═══════════════════════════════════════════════════╗
    ║                                                   ║
    ║          💱 CURRENCY CONVERTER 💱                 ║
    ║                                                   ║
    ║          Hacktoberfest 2025 Project              ║
    ║          Created by: vannu07                     ║
    ║                                                   ║
    ╚═══════════════════════════════════════════════════╝
    """
    print(banner)

def show_currency_list():
    """Display available currencies"""
    print("\n🌍 AVAILABLE CURRENCIES:")
    print("="*55)
    for code, name in CURRENCY_NAMES.items():
        print(f"  {code} - {name}")
    print("="*55)

def get_valid_input(prompt, input_type=str):
    """Get and validate user input"""
    while True:
        try:
            value = input(prompt).strip()
            if not value:
                print("❌ Input cannot be empty!")
                continue
            
            if input_type == float:
                value = float(value)
                if value <= 0:
                    print("❌ Amount must be greater than 0!")
                    continue
            
            return value
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")
        except KeyboardInterrupt:
            print("\n\n👋 Thank you for using Currency Converter!")
            exit(0)

def main():
    """Main function to run the currency converter"""
    print_banner()
    
    converter = CurrencyConverter()
    
    print("\n💡 TIP: Type 'list' to see all available currencies")
    print("💡 TIP: Press Ctrl+C anytime to exit")
    
    while True:
        print("\n" + "-"*55)
        
        try:
            # Get source currency
            from_currency = get_valid_input("\nEnter source currency (e.g., USD): ")
            
            if from_currency.lower() == 'list':
                show_currency_list()
                continue
            
            # Get target currency
            to_currency = get_valid_input("Enter target currency (e.g., INR): ")
            
            if to_currency.lower() == 'list':
                show_currency_list()
                continue
            
            # Get amount
            amount = get_valid_input("Enter amount to convert: ", float)
            
            # Perform conversion
            print("\n⏳ Converting...")
            result = converter.convert(amount, from_currency, to_currency)
            
            if result is not None:
                converter.display_conversion(result)
            
        except KeyboardInterrupt:
            print("\n\n👋 Thank you for using Currency Converter!")
            break
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}")
        
        # Ask if user wants to continue
        print("-"*55)
        choice = input("Convert another amount? (y/n): ").lower().strip()
        
        if choice != 'y':
            print("\n" + "="*55)
            print("           👋 Thank you for using Currency Converter!")
            print("           ⭐ Don't forget to star the repository!")
            print("="*55 + "\n")
            break

if __name__ == "__main__":
    main()