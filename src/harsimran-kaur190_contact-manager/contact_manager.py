import os
import json
import re 
from tabulate import tabulate 

class Contact:
    """Represents a contact with name, mobile number, and email."""
    def __init__(self,name,mobile,email):
        self.name=name
        self.mobile=mobile
        self.email=email
    def to_dict(self):
        return {"Name":self.name,"Mobile":self.mobile,"Email":self.email}

class ContactBook:
    file_name="contacts.json"
    def add_contact(self,name,mobile,email):
        """Add a new contact or update if it exists."""
        contact=Contact(name, mobile, email).to_dict()
        data=[]
        try:
            if os.path.exists(self.file_name):
                with open(self.file_name,"r") as f:
                    data=json.load(f)
                    updated=False
                    for contacts in data:
                        if contacts["Name"].strip().lower()==name.strip().lower() and contacts["Mobile"].strip()==mobile.strip():
                            update=input("This contact already exists.\nDo you what to update the existing contact?(Yes/No): ").strip().lower() 
                            if update=="yes":
                                contacts["Name"]=name
                                contacts["Mobile"]=mobile
                                contacts["Email"]=email
                                print("Contact has been updated.")
                            else:
                                print("Contact has not been updated.")
                            updated=True
                            break
                    if not updated:
                           data.append(contact)
                           print("New contact has been added.")
            else:
                data.append(contact) 
                print("Contact has been added successfully.")
            with open(self.file_name, "w") as f:
                json.dump(data, f, indent=4)
        except json.JSONDecodeError:
            print("JSON file is corrupted.")             

    def view_contacts(self):
        """Display all saved contacts."""
        try:
            if os.path.exists(self.file_name):
                with open(self.file_name) as f:
                    data=json.load(f)
                new_data = []
                for item in sorted(data, key=lambda x:x["Name"]):
                    new_data.append(item)
                if not data:
                    print("No contacts to show.")
                    return                
                table=[contact.values() for contact in new_data]
                head=["Name".center(20), "Mobile".center(15), "Email".center(30)]
                print(tabulate(table, headers=head, tablefmt="grid",colalign=("center", "center", "center")))             
            else:
                print("No contacts to show.")
        except json.JSONDecodeError:
            print("JSON file is corrupted.")

    def update_contact(self,to_update):
        """Update contact details by name."""
        new=[]
        found=False
        try:
            if os.path.exists(self.file_name):
                with open(self.file_name) as f:
                    data=json.load(f)
                for line in data:
                    if line["Name"].strip().lower()==to_update.strip().lower():
                        found=True
                        new_name=check_name(input("Enter new name: "))
                        new_mobile=check_mobile(input("Enter new mobile number: "))
                        new_email=check_email(input("Enter new email: "))
                        line["Name"]=new_name
                        line["Mobile"]=new_mobile
                        line["Email"]=new_email
                        new.append(line)
                        print("Contact has been updated successfully.")
                    else:
                        new.append(line)
                if not found:
                    print(f"No contact names {to_update} is found.")
                with open(self.file_name,"w")as f:
                    json.dump(new,f,indent=4)
            else:
                print("No contacts available to update.")
        except json.JSONDecodeError:
            print("JSON file is corrupted.")

    def delete_contact(self,to_delete):
        """Delete a contact by name with confirmation."""
        try:
            new=[]
            found=False
            if os.path.exists(self.file_name):
                with open(self.file_name,"r")as f:
                    data=json.load(f)
                for line in data:
                    if line["Name"].strip().lower()==to_delete.strip().lower():
                        found=True
                        confirm=input("Are you sure you want to delete this contact?(Yes/No): ").strip().lower()
                        if confirm=="yes":
                            print("Contact has been deleted successfully.")
                        else:
                            print("Contact has not been deleted.")
                            return
                    else:
                        new.append(line)
                if not found:
                    print(f"No contact named {to_delete} is found.")
                with open(self.file_name,"w")as f:
                    json.dump(new,f,indent=4)
            else:
                print("No contacts available to delete.")
        except json.JSONDecodeError:
            print("JSON file is corrupted.")

    def search_contact(self,name):
        """Search and show contact by name."""
        try:
            if os.path.exists(self.file_name):
                with open(self.file_name,"r")as f:
                    data=json.load(f)
                    found=False
                    for line in data:
                        if line["Name"].strip().lower()==name.strip().lower():
                            print(f"NAME={line['Name']}\tMOBILE={line['Mobile']}\tEMAIL={line['Email']}")
                            found=True
                    if not found:
                        print("No such contact is found.")
            else:
                print("No contacts available to be updated.")
        except json.JSONDecodeError:
            print("json file is corrupted.")
    
    def clear_all(self):
        """Delete all contacts after confirmation."""
        try:
           if os.path.exists(self.file_name):
               confirmation=input("Are you sure you want to delete all cotacts(Yes/No): ")
               with open(self.file_name, "r") as f:
                   data=json.load(f)
                   if not data:
                       print("No contacts available to delete.")
                       return
               if confirmation.strip().lower()=="yes":
                    with open(self.file_name, "w") as f:
                        json.dump([], f, indent=4)
                        print("All contacts have been deleted.")
               else:
                   print("No contact has been deleted.")
           else:
               print("No contacts available to delete.")
        except json.JSONDecodeError:
            print("json file is corrupted.")
        
def check_mobile(mobile):
    """Checks that the mobile number entered by user consits of 10 digits only."""
    while True:
        try:
            lists_mobile=list(mobile)
            if len(lists_mobile)==10 and mobile.isdigit():
                return mobile
            else:
                print("The mobile number should be of 10 digits.")
                mobile=input("Enter mobile number again: ")
        except ValueError:
            print("The mobile number should be of 10 digits.")
            continue

def check_email(email):
    """Checks that the email entered by user is valid"""
    while True:
        pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(pattern,email):
            return email
        else:
            print("Invalid email format.\nPlease try again.")
            email=input("Enter email again: ")

def check_name(name):
    """Checks that the name entered by user is not empty"""
    while True:
        if name.strip()=="":
            print("Name cannot be empty.\nPlease try again.")
            name=input("Enter name again: ")
        else:
            return name
        
def start_contact():
    """
    Runs the main menu loop to interact with the contact book.
    Displays options to add, view, update, delete, search contacts,
    clear all contacts, or exit the program.
    """
    while True:
        try:
            menu=["Add contact","View contact","Update contact","Delete contact","Search contact","Delete all contacts","Exit"]
            print("MENU".center(35,"-"))
            for i,item in enumerate(menu):
                print(f"{i+1}. {item}")
            book=ContactBook()
            user_command=int(input("Enter the command number: "))
            if user_command==1:
                name=check_name(input("Enter name: "))
                mobile=check_mobile(input("Enter mobile number: "))
                email=check_email(input("Enter email: "))
                book.add_contact(name,mobile,email)
            elif user_command==2:
                book.view_contacts()
            elif user_command==3:
                to_update=check_name(input("Enter the contact name you want to update: "))
                book.update_contact(to_update)
            elif user_command==4:
                delete=check_name(input("Enter the contact name you want to delete: "))
                book.delete_contact(delete) 
            elif user_command==5:
                to_search=input("Enter the name you want to search: ")
                book.search_contact(to_search)
            elif user_command==6:
                book.clear_all()
            else:
                print("Thank you!!")
                break 
        except ValueError:
            print(f"Please enter a integer from 1 to {len(menu)}")
            continue

if __name__=="__main__":
    try:
       start_contact()
    except KeyboardInterrupt:
        print("Thank you!!\nExiting the program.") 