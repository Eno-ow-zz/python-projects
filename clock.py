import tkinter as tk
import time

# Create the main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("250x100")


# Create a label to display the time
label = tk.Label(root, font=('Helvetica', 40), background='black', foreground='cyan')
label.pack(anchor='center')

# Define the update function to display the time
def update_time():
    current_time = time.strftime('%H:%M:%S')
    label.config(text=current_time)
    label.after(1000, update_time)

# Start the clock
update_time()
root.mainloop()

