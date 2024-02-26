import tkinter as tk
from tkinter import messagebox

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class UserManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("User Management")

        # Dummy user data for demonstration purposes
        self.users = [
            User("user1", "password1"),
            User("user2", "password2"),
            User("admin", "adminpassword")
        ]

        # Login Frame
        self.login_frame = tk.Frame(root)
        self.login_frame.pack(pady=20)

        tk.Label(self.login_frame, text="Username:").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(self.login_frame, text="Password:").grid(row=1, column=0, padx=10, pady=5)

        self.username_entry = tk.Entry(self.login_frame)
        self.password_entry = tk.Entry(self.login_frame, show="*")

        self.username_entry.grid(row=0, column=1, padx=10, pady=5)
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        login_button.grid(row=2, column=0, columnspan=2, pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if the entered credentials match any user
        for user in self.users:
            if user.username == username and user.password == password:
                messagebox.showinfo("Login Successful", f"Welcome, {username}!")
                self.show_user_management_frame()
                return

        # If no matching user is found
        messagebox.showerror("Login Failed", "Invalid username or password")

    def show_user_management_frame(self):
        # Destroy the login frame
        self.login_frame.destroy()

        # Create user management frame
        self.user_management_frame = tk.Frame(self.root)
        self.user_management_frame.pack(pady=20)

        tk.Label(self.user_management_frame, text="User Management").pack()

        tk.Button(self.user_management_frame, text="Add User", command=self.add_user).pack(pady=10)
        tk.Button(self.user_management_frame, text="View Users", command=self.view_users).pack(pady=10)

    def add_user(self):
        # Dummy function for adding a user (You can implement your own logic)
        messagebox.showinfo("Add User", "Functionality to add a user can be implemented here.")

    def view_users(self):
        # Dummy function for viewing users (You can implement your own logic)
        user_list = "\n".join([f"Username: {user.username}" for user in self.users])
        messagebox.showinfo("View Users", f"Users:\n{user_list}")

def main():
    root = tk.Tk()
    app = UserManagementApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()