#!/usr/bin/env python3

def count_metrics(text):
    """
    Count the number of words, characters, and lines in the given text.
    
    Args:
        text (str): The input text to analyze
        
    Returns:
        tuple: (word_count, char_count, line_count)
    """
    # Count characters (including whitespace)
    char_count = len(text)
    
    # Count words (split by whitespace)
    words = text.split()
    word_count = len(words)
    
    # Count lines (split by newline)
    lines = text.splitlines()
    line_count = len(lines) if text else 0
    
    return word_count, char_count, line_count

def analyze_file(file_path):
    """
    Analyze a text file and return its metrics.
    
    Args:
        file_path (str): Path to the text file
        
    Returns:
        tuple: (word_count, char_count, line_count)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            return count_metrics(text)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def main():
    print("Welcome to Word Counter!")
    print("1. Enter text directly")
    print("2. Analyze a text file")
    
    choice = input("\nEnter your choice (1 or 2): ")
    
    if choice == "1":
        print("\nEnter your text (press Ctrl+D or Ctrl+Z on Windows when done):")
        try:
            text = ""
            while True:
                line = input()
                text += line + "\n"
        except EOFError:
            metrics = count_metrics(text)
            if metrics:
                words, chars, lines = metrics
                print(f"\nAnalysis Results:")
                print(f"Words: {words}")
                print(f"Characters: {chars}")
                print(f"Lines: {lines}")
    
    elif choice == "2":
        file_path = input("\nEnter the path to your text file: ")
        metrics = analyze_file(file_path)
        if metrics:
            words, chars, lines = metrics
            print(f"\nAnalysis Results for '{file_path}':")
            print(f"Words: {words}")
            print(f"Characters: {chars}")
            print(f"Lines: {lines}")
    
    else:
        print("Invalid choice. Please run the program again and select 1 or 2.")

if __name__ == "__main__":
    main()
