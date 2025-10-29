# ⌨️ Typing Speed Test (Python CLI)

A terminal-based Python script to test your typing speed and accuracy with randomly generated words. The script generates a random sentence of English words, and calculates your **words per minute (WPM)** and **word-level accuracy**.

---

## 🎮 Features

* **Random Sentence Generation**: Each round gives a new sentence with random English words.
* **Word-Level Accuracy**: Only mistyped words are counted wrong, not every character after the first typo.
* **WPM Calculation**: Measures your typing speed in words per minute.
* **Single-File Script**: Easy to use, minimal Python code.
* **Beginner-Friendly**: Clean, readable, and easy to modify.

---

## ⚙️ Getting Started

### 🧠 Prerequisites

* Python 3.x installed
* `random-words` library (install with pip):

```bash
pip install RandomWords
```

---

### 🚀 How to Run

1. Clone or download the repository and navigate to the project folder:

```bash
cd src/AnkitDand-Typing-Speed-Test
```

2. Run the script:

```bash
python typing_speed_test.py
```

3. Follow the on-screen instructions to start typing the generated sentence.

---

### 🎯 How it Works

* The script generates a **random sentence of 8–12 words**.
* Press **Enter** to start typing the sentence.
* After you finish, the script calculates:

  * **Time Taken**
  * **Typing Speed (WPM)**
  * **Word-Level Accuracy (%)**

Example output:

```
Type the following sentence:

--- The cat dog runs quickly bright school plays. ---

Your input: Honks injections forearms whip builder halts tons beds bangs inception

--- Results ---
Time Taken: 14.57 seconds
Typing Speed: 41.19 WPM
Accuracy: 100.0%
```

---

## 🧩 Code Overview

### `generate_sentence()` Function

* Creates a random sentence using words from the `random-words` library.
* Capitalizes the first word and adds a period at the end.

### `typing_speed_test()` Function

* Displays the sentence for the user to type.
* Measures the time taken to type the sentence.
* Calculates **words per minute** and **word-level accuracy**.

---

## 💡 Project Structure

```
src/
└── AnkitDand-Typing-Speed-Test/
    ├── typing_speed_test.py
    └── README.md
```
