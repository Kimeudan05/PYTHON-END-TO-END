# Library Management System
# Add books, borrow books, return books
# Store data in a JSON/CSV file

import json
from datetime import datetime,timezone
class Library:
    def __init__(self):
        self._books = [] # each book {"title":..,"author"...,is_available:..false/true}
        self._borrowed_books={} 
    # --------------------- Public Methods ---------------------
    
    def add_book(self,title,author):
        if self.__find_book_by_title(title):
            print(f"Book '{title}' already exeists")
            return
        self._books.append({
            "title":title,
            "author":author,
            "is_available":True
        }) 
        print(f"Book '{title}' added successifuly")
        
    def borrow_book(self,title,user_id):
        book = self.__find_book_by_title(title)
        if not book:
            print(f"Book '{title}' not found")
            return
        
        if not book["is_available"]:
            print(f"Book '{title} is currenty borrowed")
            return
        
        book['is_available'] = False
        self._borrowed_books[title] ={
            "user_id":user_id,
            "date":datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
        }
        print(f"'{title}' borrowed by user {user_id}")
        
    def return_book(self,title,user_id):
        if title not in self._borrowed_books:
            print(f"No record of '{title}' being borrowed")
            return
        
        if self._borrowed_books[title]['user_id'] != user_id:
            print(f"Book '{title}' was not borrowed by user {user_id}")
            return
        
        book = self.__find_book_by_title(title)
        if book:
            book['is_available'] = True
            
        del self._borrowed_books[title]
        print(f"'{title}' returned by {user_id}")
        
    def search_book(self,keyword):
        results =[
            book for book in self._books
            if keyword.lower() in book['title'].lower() or keyword.lower() in book['author'].lower()
        ]
        if not results:
            print(f"No books found matching '{keyword}'")
            return
        
        for book in results:
            status = "Available" if book['is_available'] else "Borrowed"
            print(f"{book['title']} by {book['author']} - [{status}]")
            
    def list_available_books(self):
        available = [book for book in self._books if book['is_available']]
        if not available:
            print("No books currently available")
            return
        for book in available:
            print(f"{book['title']} by {book['author']}")
        
    def list_borrowed_books(self):
        if not self._borrowed_books:
            print("No borrowed  books at the moment")
            return
        for title , info in self._borrowed_books.items():
            print(f"{title} - borrowed by {info['user_id']} on {info['date']}")
        
# --------------------- Private Helper Method ---------------------
    def __find_book_by_title(self,title):
        for book in self._books:
            if book['title'].lower() == title.lower():
                return book
        return None
    
    
 # --------------------- Fule handling ---------------------

    def save_to_file(self,filepath):
        data ={
            "books":self._books,
            "borrowed_books":self._borrowed_books
        }
        with open(filepath,'w') as f:
            json.dump(data,f,indent=4)
        print(f"Library data saved to '{filepath}'")
        
    @classmethod
    def load_from_dict(cls,filepath):
        try:
            with open(filepath,'r') as f:
                data = json.load(f)
            lib = cls()
            lib._books = data.get("books",[])
            lib._borrowed_books = data.get("borrowed_books",{})
            print(f"libarary loaded from '{filepath}'")
            return lib
        except FileNotFoundError:
            print(f"No existing linarry file at '{filepath}'. Starting fresh")
            return cls()
        
    @staticmethod
    def validate_book_data(book_dict):
        return "title" in book_dict and "author" in book_dict and "is_available" in book_dict
    
# ------------------ CLI Utility Functions ------------------
import os
def clear():
    os.system('cls' if os.name =='nt' else 'clear')

def pause():
    input("\nPress Enter to continue...")
    
def main_menu():
    print("\n Library Management System")
    print("-"*30)
    print("1. Add a Book")
    print("2. Borrow a Book")
    print("3. Return a Book")
    print("4. Search Books")
    print("5. List Available Books")
    print("6. List Borrowed Books")
    print("7. Save & Exit")
    
# ------------------ Main Program Loop ------------------
def run():
    lib = Library.load_from_dict('library_data.json')
    
    while True:
        clear()
        main_menu()
        choice =input("\nEnter your choice (1-7) :").strip()
        
        if choice == "1":
            print("Add a Book")
            title = input("Enter book title :").strip()
            author = input("Enter author name :").strip()
            lib.add_book(title,author)
            pause()
            
        elif choice == "2":
            print("Borrow a Book")
            title = input("Enter book title to borrow :").strip()
            user_id = input("Enter your user ID :").strip()
            lib.borrow_book(title,user_id)
            pause()
            
        elif choice == "3":
            print("Return a Book")
            title = input("Enter book title to return :").strip()
            user_id = input("Enter your user ID :").strip()
            lib.return_book(title,user_id)
            pause()
            
        elif choice == "4":
            print("Search Books ")
            keyword = input("Enter keyword (title or author) :").strip()
            lib.search_book(keyword)
            pause()
            
        elif choice == "5":
            print("\n Available Books")
            lib.list_available_books()
            pause()
            
        elif choice == "6":
            print("\n Borrowed Books")
            lib.list_borrowed_books()
            pause()
            
        elif choice == "7":
            lib.save_to_file("library_data.json")
            print("\n data saved. Exiting.....")
            break
            
        else:
            print("Invalid choice . plaese Try again")
            pause()
            
# ------------------ Entry Point ------------------
if __name__ == "__main__":
    run()
            
        