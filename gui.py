import tkinter as tk
from tkinter import scrolledtext 
from secret_santa import *

names = [key for key, _ in exclusions.items()]

def secret_santa_outputs(output_widget):
    # Generate the list of items
    secret_santa_list = secret_santa_generator(exclusions) # names and spouses from secret_santa.py

    # Clear previous content in the Text widget
    output_widget.config(state="normal") # Make the widget editable temporarily
    output_widget.delete('1.0', tk.END)  

    # Insert each item from the list into the Text widget
    for item in secret_santa_list:
        output_widget.insert(tk.END, item + "\n") # Insert at the end, followed by a newline

    # Make the widget read-only again to prevent user editing
    output_widget.config(state="disabled")

def display_exclusions_dict(exclusions_list_widget):
    # Check for new exclusions pairs!!!!
    gift_giver = exclusions_name1_box.get()
    ex = exclusions_name2_box.get()

    if gift_giver and ex:
        # String scrubbing
        ex = ex.replace(" ","") #remove spaces
        ex = ex.split(",")

        exclusions.update({gift_giver:ex})
        # Empty the textboxes
        exclusions_name1_box.delete(0, tk.END)
        exclusions_name2_box.delete(0, tk.END)

    # Clear previous content in the Text widget
    exclusions_list_widget.config(state="normal") # Make the widget editable temporarily
    exclusions_list_widget.delete('1.0', tk.END) 
    
    for key, value in exclusions.items():
        exclusions_list_widget.insert(tk.END, f"{key}:{value}" + "\n")

    # Make the widget read-only again to prevent user editing
    exclusions_list_widget.config(state="disabled")


def display_all_names(names_text_widget):
    # Check for added names
    new_name = add_name_box.get()
    if new_name:
        exclusions.update({new_name:[]})
        names.append(new_name)
        # Empty the textboxes
        add_name_box.delete(0, tk.END)

    # Display all names in santa draw
    names_text_widget.config(state="normal") # Make the widget editable temporarily
    names_text_widget.delete('1.0', tk.END)
    for name in names:
        names_text_widget.insert(tk.END, name + "\n")
        
    # Make the widget read-only again to prevent user editing
    names_text_widget.config(state="disabled")


# --- Main Tkinter Application ---
root = tk.Tk()
root.title("Secret Santa Generator")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window geometry to match the screen size
root.geometry(f"{screen_width}x{screen_height}+0+0")

### Displaying ALL names of people in secret santa pool, regardless of exclusion relationship
names_textbox = scrolledtext.ScrolledText(root, wrap=tk.WORD, state="disabled", height=10, padx=5, pady=5)
names_textbox.pack(pady=10, fill=tk.BOTH, expand=True)

add_name_box = tk.Entry(root, width=30)
add_name_box.pack(pady=10)

display_button = tk.Button(root, text="Display Names", command=lambda: display_all_names(names_textbox))
display_button.pack(pady=10)

### Displaying the names and exclusions pairings
exclusions_textbox = scrolledtext.ScrolledText(root, wrap=tk.WORD, state="disabled", height=10, padx=5, pady=5)
exclusions_textbox.pack(pady=10, fill=tk.BOTH, expand=True)

row_frame = tk.Frame(root)
row_frame.pack(fill="x", padx=10, pady=10)

gift_giver_label = tk.Label(row_frame, text="Gift Giver Name:")
gift_giver_label.pack(side="left", padx=(0, 10))

exclusions_name1_box = tk.Entry(row_frame, width=30)
exclusions_name1_box.pack(side="left", fill="x")

###

row_frame2 = tk.Frame(root)
row_frame2.pack(fill="x", padx=10, pady=10)

exclusions_label = tk.Label(row_frame2, text="Gift Giver Name:")
exclusions_label.pack(side="left", padx=(0, 10))

exclusions_name2_box = tk.Entry(row_frame2, width=30)
exclusions_name2_box.pack(side="left", fill="x")

display_button = tk.Button(root, text="Display/Add Exclusions", command=lambda: display_exclusions_dict(exclusions_textbox))
display_button.pack(pady=10)

### OUTPUT!
# Create a Button that triggers the secret santa generator function
display_button = tk.Button(root, text="DRAW NAMES!", command=lambda: secret_santa_outputs(output_area))
display_button.pack(pady=10)

# Create a ScrolledText widget to display the secret santa pairings
output_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state="disabled", height=10, padx=5, pady=5)
output_area.pack(pady=10, fill=tk.BOTH, expand=True)

# Start Tkinter loop
root.mainloop()