import tkinter as tk
from tkinter import ttk,messagebox

class RestaurentOrderManagement:
    def __init__(self, root):
        self.root= root
        self.root.title("Restaurent Order Management System")

        self.menu_items = {
            "BIGMAC" : 6.99,
            "MACFILLET" : 5.99,
            "CHEESEBURGER" : 4.99,
            "FRIES" : 2.99,
            "COKE" : 1.99,
            "ICE CREAM" : 3.99,
            "CHIKEN SANDWICH" : 5.49,
            "FISH SANDWICH" : 5.49,
        }

        self.exchange_rate = 121.93

        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5,anchor=tk.CENTER)

        ttk.Label(
            frame,
            text="Restaurent Order Management System",
            font=("Cursive", 20, "bold")
        ).grid(row=0, columnspan=3, pady=10)

        self.menu_label = {}
        self.menu_quantities = {}

        for i, (item,price) in enumerate(self.menu_items.items(), start=1):
            label = ttk.Label(
                frame,
                text=f"{(item)} (${price}):",
                font=("Cursive", 12)
            )
            label.grid(row=i, column=0, padx=0, pady=5)
            self.menu_label[item] = label

            quantity_entry= ttk.Entry(frame, width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)
            self.menu_quantities[item] = quantity_entry

        self.currency_var= tk.StringVar()
        ttk.Label(frame, text="Currency:",font=("Cursive",12)
                  ).grid(
                      row=len(self.menu_items) + 1,
                      column=0,
                      padx=10,
                      pady=5
                  ) 
        
        currency_dropdown = ttk.Combobox(
            frame,
            textvariable=self.currency_var,
            state="readonly",
            width=18,
            values=["USD", "BDT"]
        )
        currency_dropdown.grid(
            row=len(self.menu_items) + 1,
            column=1,
            padx=10,
            pady=5
        )
        currency_dropdown.current(0)
        self.currency_var.trace('w', self.update_menu_prices)

        order_button = ttk.Button(
            frame,
            text="Place Order",
            command=self.place_order
        )
        order_button.grid(
            row=len(self.menu_items) + 2,
            columnspan=3,
            padx=10,
            pady=10
        )

    def  update_menu_prices(self, *args):
        currency = self.currency_var.get()
        symbol = "৳" if currency == "BDT" else "$"
        rate= self.exchange_rate if currency == "BDT" else 1

        for item, entry in self.menu_quantities.items():
            quantity = entry.get()
            if quantity.isdigit():
                quantity = int(quantity)
                price = self.menu_items[item] * rate
                cost= price * quantity
                total_cost += cost

                if quantity > 0:
                    order_summary += (
                        f"{item}: {quantity} x {symbol}{price} = {symbol}{cost}\n"
                    )

        if total_cost > 0:
            order_summary += f"\nTotal Cost: {symbol}{total_cost}"
            messagebox.showinfo("Order Placed", order_summary)
        else:
            messagebox.showerror("Error", "Please order at least one item.")

# Main block to run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurentOrderManagement(root)
    root.geometry("800x600")  # Set the size of the window
    root.mainloop()           # Start the GUI loop



