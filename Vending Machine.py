# Question
"""
Your task is to create a Vending Machine program using the Python programming language.
The program should demonstrate your knowledge of programming and make use of the techniques 
introduced over the course of the module. 
Your application should be accompanied by a development docu"""
# Creating Vending Machine
import tkinter as tk
from tkinter import messagebox
# Insulting root function into the code
class VendingMachine:
    def _init_(self, root):
        self.root = root
# Adding title to the Machine
        self.root.title("Vending Machine")
        self.root.geometry("1920x1080")  # Fullscreen window
# Making menu of the Vending Machine
        self.snacks = {
            "111": {"name": "Oman Chips", "price": 0.50, "stock": 15},
            "112": {"name": "Breaks", "price": 1.00, "stock": 20},
            "113": {"name": "Kitkat", "price": 2.50, "stock": 18},
            "114": {"name": "Max", "price": 2.50, "stock": 14},
            "115": {"name": "Snickers", "price": 3.50, "stock": 23},
            "116": {"name": "Lays", "price": 3.00, "stock": 14},
            "117": {"name": "Kinder Joy", "price": 4.50, "stock": 10}
        }
        self.drinks = {
            "118": {"name": "Laban Up", "price": 0.75, "stock": 16},
            "119": {"name": "Water", "price": 1.00, "stock": 22},
            "120": {"name": "Chocolate Milkshake", "price": 2.00, "stock": 17},
            "121": {"name": "Strawberry Milkshake", "price": 2.00, "stock": 15},
            "122": {"name": "Dew", "price": 2.50, "stock": 13},
            "123": {"name": "7up", "price": 2.50, "stock": 14}
        }
        self.create_widgets()
# Adding a welcome text to the code
    def create_widgets(self):
        tk.Label(self.root, text="𝓦𝓮𝓵𝓬𝓸𝓶𝓮 𝓽𝓸 𝓽𝓱𝓮 𝓥𝓮𝓷𝓭𝓲𝓷𝓰 𝓜𝓪𝓬𝓱𝓲𝓷𝓮❗", font=("cooper black", 50)).pack(pady=10)
# Asking the user to select either Snacks or Drinks they want 
# Saparating Snacks items into the Snacks 
        self.snacks_button = tk.Button(self.root, text="𝑺𝒏𝒂𝒄𝒌𝒔", font=("Arial", 20), command=self.show_snacks)
        self.snacks_button.pack(pady=5)
# Saparating Drinks items into the Drinks 
        self.drinks_button = tk.Button(self.root, text="𝑫𝒓𝒊𝒏𝒌𝒔", font=("Arial", 20), command=self.show_drinks)
        self.drinks_button.pack(pady=5)

        self.items_frame = tk.Frame(self.root)
        self.items_frame.pack(pady=10)
# Asking the user to write the Code of the item
        self.selection_label = tk.Label(self.root, text="Enter Item Code : ", font=("Arial", 12))
        self.selection_label.pack(pady=5)
        self.item_entry = tk.Entry(self.root, font=("Arial", 12))
        self.item_entry.pack(pady=5)
# Asking the user to write the Quantity they want 
        self.quantity_label = tk.Label(self.root, text="Enter Quantity : ", font=("Arial", 12))
        self.quantity_label.pack(pady=5)
        self.quantity_entry = tk.Entry(self.root, font=("Arial", 12))
        self.quantity_entry.pack(pady=5)
# Asking the user to Insert the Money they have
        self.money_label = tk.Label(self.root, text="Insert Money : ", font=("Arial", 12))
        self.money_label.pack(pady=5)
        self.money_entry = tk.Entry(self.root, font=("Arial", 12))
        self.money_entry.pack(pady=5)
# Making to the user that the order is confirming or not
        self.purchase_button = tk.Button(self.root, text="Pᴜʀᴄʜᴀsᴇ", font=("Arial", 18), command=self.purchase_item)
        self.purchase_button.pack(pady=10)

        self.exit_button = tk.Button(self.root, text="E̷x̷i̷t̷", font=("Arial", 16), command=self.root.quit)
        self.exit_button.pack(pady=10)

    def show_snacks(self):
        for widget in self.items_frame.winfo_children():
            widget.destroy()
# Telling to the user that what all are Available Snacks 
        tk.Label(self.items_frame, text="𝑨𝒗𝒂𝒊𝒍𝒂𝒃𝒍𝒆 𝑺𝒏𝒂𝒄𝒌𝒔 :", font=("Arial", 18)).pack(pady=5)
        for code, item in self.snacks.items():
            tk.Label(self.items_frame, text=f"{code}. {item['name']} - ${item['price']} ({item['stock']} in stock)", font=("Arial", 12)).pack(anchor="w")

    def show_drinks(self):
        for widget in self.items_frame.winfo_children():
            widget.destroy()
# Telling to the user that what all are Available Drinks 
        tk.Label(self.items_frame, text="𝘼𝙫𝙖𝙞𝙡𝙖𝙗𝙡𝙚 𝘿𝙧𝙞𝙣𝙠𝙨 :", font=("Arial", 18)).pack(pady=5)
        for code, item in self.drinks.items():
            tk.Label(self.items_frame, text=f"{code}. {item['name']} - ${item['price']} ({item['stock']} in stock)", font=("Arial", 12)).pack(anchor="w")

    def purchase_item(self):
        choice = self.item_entry.get()
        quantity = self.quantity_entry.get()
        item = None

        if choice in self.snacks:
            item = self.snacks[choice]
        elif choice in self.drinks:
            item = self.drinks[choice]
# To show if anythings which given by the user is wrong or not
        if not item:
            messagebox.showerror("Error", "Invalid selection. Please try again.")
            return
# To show the quantity given by the user is invalid 
        try:
            quantity = int(quantity)
            if quantity <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid quantity.")
            return

        total_cost = item['price'] * quantity
# To show the the chosen item is out of stock
        if item['stock'] < quantity:
            messagebox.showinfo("Out of Stock", f"Sorry, not enough stock for {item['name']}.")
            return
# To show the money given by the user is invalid 
        try:
            money_inserted = float(self.money_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount of money.")
            return
# The Insufficient funds and Transaction canceled
        if money_inserted < total_cost:
            messagebox.showerror("Error", "Insufficient funds. Transaction canceled.")
            return

        item['stock'] -= quantity
        change = money_inserted - total_cost
        
# To show the item chosen by the user is Dispensing
        messagebox.showinfo("Vending Machine", f"Dispensing {quantity} x {item['name']}...")
# Showing the remaining balance amount of the user 
        messagebox.showinfo("Vending Machine", f"Remaining balance: ${change:.2f}")

# Ask if the user wants to continue shopping
        continue_shopping = messagebox.askyesno("Continue Shopping", "Do you want to add more snacks or drinks?")

        if continue_shopping:
# Clear the item code entry
            self.item_entry.delete(0, tk.END) 
# Clear the quantity entry
            self.quantity_entry.delete(0, tk.END)
# Clear the money entry
            self.money_entry.delete(0, tk.END)
            self.show_snacks()  
        else:
            messagebox.showinfo("Vending Machine", "Thank you for using the Vending Machine!")
            self.root.quit()

if _name_ == "_main_":
    root = tk.Tk()
    app = VendingMachine(root)
    root.mainloop()
