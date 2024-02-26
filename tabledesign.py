import tkinter as tk
from tkinter import ttk

class TableFloorDesignApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Table Floor Design")

        # Create a Treeview widget
        self.tree = ttk.Treeview(root, columns=("Table Number", "Capacity", "Occupancy"))

        # Define column headings
        self.tree.heading("#0", text="ID")
        self.tree.heading("Table Number", text="Table Number")
        self.tree.heading("Capacity", text="Capacity")
        self.tree.heading("Occupancy", text="Occupancy")

        # Add sample data to the treeview
        self.add_sample_data()

        # Pack the Treeview widget
        self.tree.pack(expand=True, fill=tk.BOTH)

    def add_sample_data(self):
        # Add sample data to the treeview
        self.tree.insert("", "end", values=("1", "Table 1", "4", "Occupied"))
        self.tree.insert("", "end", values=("2", "Table 2", "6", "Vacant"))
        self.tree.insert("", "end", values=("3", "Table 3", "2", "Occupied"))
        self.tree.insert("", "end", values=("4", "Table 4", "8", "Vacant"))

def main():
    root = tk.Tk()
    app = TableFloorDesignApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()