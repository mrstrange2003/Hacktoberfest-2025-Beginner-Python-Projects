import os , json
import random
from colorama import Fore, init

#Initialize colorama
init(autoreset = True)

# Loads roasts and compliments from json file
def load_data():
    try: 
        with open("data.json", "r") as f:
            return json.load(f)
          
    except FileNotFoundError:
        print(Fore.YELLOW + "⚠️ Missing data.json file !! Make sure its in the same folder 📂")
        return {"roasts" : [], "compliments" : []}
              
# This function will analyze the python file
def analyze(filename):

    try:
        with open(filename, "r") as f:

            code = f.read();    # read the file
    
            lines = code.count("\n")    #count the number of lines

            if lines < 20:
                return "Your code is sweet and short, just like a python one liner"
            
            elif lines < 100:
                return "Perfect Code Size, neither too long nor short."
            
            else:
                return "So many lines of code, maybe you wrote an entire framework !!"

    except Exception:
            return "Couldn't read file"

def main():
     
    print(Fore.CYAN + "\n💻 Welcome to the Code-Roast-or-Compliment 💻")
    print(Fore.MAGENTA + "Because your code deserves feedback... even if it didn’t ask for it 😅\n")

    data = load_data()
    roasts = data.get("roasts", [])
    compliments = data.get("compliments", [])

    if not roasts or not compliments:
        print(Fore.RED + "⚠️ No roasts or compliments found in data.json")
        return
    
    selection = input(Fore.YELLOW + "Choose mode (r = Roast, c = Compliment, s = Surprise :)").strip().lower()

    if selection == "s":
        selection = random.choice(["r","c"])    # choose random between roast and compliment

    if selection not in ["r", "c"]:
        
        print(Fore.RED + "⚠️ Invalid selection! Please select r, c or s")
        return
    
    file_choice = input(Fore.YELLOW + "😎 Want to analyze your python code just for fun? (y/n)").strip().lower()

    code_comment = ""

    if file_choice == "y":
        
        fileName = input("📁 Input your Python file here :").strip().strip('"').strip("'")

        if os.path.exists(fileName):
            code_comment = analyze(fileName)

        else:
            print(Fore.RED + "\n ❌ File Not Found!!")
            return 
        
    else:
        print(Fore.CYAN + "No code to analyze? Alright, your code lives to see another day! 🚀")
        return

    print(Fore.WHITE + "\n📝 Result:\n")

    if selection == "r":
        
        print(Fore.RED + random.choice(roasts))

    else:

        print(Fore.GREEN + random.choice(compliments))

    if code_comment:

        print(Fore.CYAN + "\n🔍 Code Insight : " + code_comment)        

    print(Fore.MAGENTA + "\n🎮 Thanks for playing Code-Roast-or-Compliment 💻💖")        
   
   
if __name__ == "__main__":
    
    main()

