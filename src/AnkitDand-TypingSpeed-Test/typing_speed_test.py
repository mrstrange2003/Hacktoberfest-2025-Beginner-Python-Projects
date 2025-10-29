import time
from random_words import RandomWords
import string

rw = RandomWords()

def clean_word(word):
    """Remove punctuation and convert to lowercase."""
    return word.strip(string.punctuation).lower()

def typing_speed_test():
    # Generate a random sentence of 10 words
    sentence_words = [rw.random_word() for _ in range(10)]
    sentence = ' '.join(sentence_words).capitalize() + '.'
    
    print("\nType the following sentence as fast and accurately as you can:\n")
    print(f"--- {sentence} ---\n")
    
    input("Press Enter to start...")
    start_time = time.time()
    
    typed_text = input("\nYour input: ")
    end_time = time.time()
    
    # Time calculation
    time_taken = end_time - start_time
    
    # WPM calculation
    words_typed = len(typed_text.split())
    wpm = words_typed / (time_taken / 60)
    
    # Word-level accuracy
    original_words = [clean_word(w) for w in sentence.split()]
    typed_words = [clean_word(w) for w in typed_text.split()]
    
    correct_words = sum(1 for o, t in zip(original_words, typed_words) if o == t)
    accuracy = (correct_words / len(original_words)) * 100
    
    print("\n--- Results ---")
    print(f"Time Taken: {time_taken:.2f} seconds")
    print(f"Typing Speed: {wpm:.2f} WPM")
    print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    print("=== Typing Speed Test ===")
    typing_speed_test()
