import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("Google Account Selection")

# Load the Google image
google_image = Image.open("google_image.jpg")
google_photo = ImageTk.PhotoImage(google_image)

# Create the Google image label
google_label = tk.Label(root, image=google_photo)
google_label.pack()

# Create the "Sign in with Google" button
sign_in_button = tk.Button(root, text="Sign in with Google")
sign_in_button.pack()

# Create the "Choose an account" label
choose_account_label = tk.Label(root, text="Choose an account")
choose_account_label.pack()

# Create the "to continue to TeacherMade" label
continue_label = tk.Label(root, text="to continue to TeacherMade")
continue_label.pack()

# Create the account information label
account_info_label = tk.Label(root, text="26sNelson Dustin\\n26snelson.dustin@stu.lavegaisd.org")
account_info_label.pack()

# Create the "Use another account" button
use_another_account_button = tk.Button(root, text="Use another account")
use_another_account_button.pack()

# Create the information label
info_label = tk.Label(root, text="To continue, Google will share your name, email address, language preference, and profile picture with TeacherMade. Before using this app, you can review TeacherMade’s privacy policy and terms of service.")
info_label.pack()

# Run the main loop
root.mainloop()
