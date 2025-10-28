## Random Fact Generator

This is a simple Python script that connects to an external API to fetch and display a user-specified number of random, useless facts directly in your console.

# How It Works

The script utilizes the requests library to make a GET request to the uselessfacts.jsph.pl API. It then parses the returned JSON data and extracts the fact text. The user is prompted to enter how many facts they want (up to 7 per run), and the script loops through the request process, printing each fact individually.

# Prerequisites

To run this script, you need:

Python 3 (3.6 or higher recommended)

The requests library for making HTTP calls.

# Installation and Setup

1. Save the Code

Save the provided Python code into a file named fact_generator.py.

2. Install Dependencies

You only need to install the requests library. Open your terminal or command prompt and run:

pip install requests

# Usage

1. Run the Script

Navigate to the directory where you saved fact_generator.py and execute it using Python:

python fact_generator.py

2. Enter Input

The script will prompt you for a number:

---Welcome to my random fact generator---

Enter a number:

Enter an integer between 1 and 7 to determine how many facts will be fetched and printed.

If you enter a number greater than 7, the script will output a warning.

If you enter 0 or a negative number, the script will also output a warning.

Example Output

---Welcome to my random fact generator---

Enter a number: 3
The average person spends two weeks of their life waiting for the light to change.

In China, the color white is used for mourning.

You are born with 300 bones, but by the time you are an adult, you will have only 206.

# API Source

This generator uses the following third-party API for fact data:

Useless Facts API: <https://uselessfacts.jsph.pl/>
