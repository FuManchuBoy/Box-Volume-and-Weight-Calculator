import tkinter as tk
from tkinter import messagebox

def get_volume(length, height, width):
    return length * height * width

def get_volumetric_weight(volume, density):
    return volume * density

def calculate_volume_weight():
    try:
        system_choice = int(system_choice_var.get())
        length_cm = float(entry_length.get())
        height_cm = float(entry_height.get())
        width_cm = float(entry_width.get())

        # Convert measurements from cm to meters
        length_m = length_cm / 100.0
        height_m = height_cm / 100.0
        width_m = width_cm / 100.0

        material_choice = int(material_choice_var.get())
        if material_choice == 1:
            density_g_cm3 = 0.3  # Density of cardboard in g/cm³
        elif material_choice == 2:
            density_g_cm3 = 0.7  # Density of wood in g/cm³
        else:
            messagebox.showerror("Error", "Invalid material choice. Please choose 1 or 2.")
            return

        # Convert density from g/cm³ to kg/m³
        density_kg_m3 = density_g_cm3 * 1000

        volume = get_volume(length_m, height_m, width_m)
        volumetric_weight = get_volumetric_weight(volume, density_kg_m3)

        messagebox.showinfo("Result", f"The total volume of the box is: {volume:.2f} cubic meters.\n"
                                      f"The volumetric weight of the box is approximately: {volumetric_weight:.2f} kilograms.")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numeric values for length, height, and width.")

# Create the main window
root = tk.Tk()
root.title("Box Volume and Weight Calculator")

# Make the window non-resizable
root.resizable(True, True)

# Create widgets for user input
label_system = tk.Label(root, text="Please choose the metric system:")
label_system.pack()

system_choice_var = tk.StringVar()
system_choice_var.set("1")  # Default choice: European (cm)

radio_european = tk.Radiobutton(root, text="European (cm)", variable=system_choice_var, value="1")
radio_european.pack()

radio_american = tk.Radiobutton(root, text="American (inches)", variable=system_choice_var, value="2")
radio_american.pack()

label_length = tk.Label(root, text="Enter the length:")
label_length.pack()

entry_length = tk.Entry(root)
entry_length.pack()

label_height = tk.Label(root, text="Enter the height:")
label_height.pack()

entry_height = tk.Entry(root)
entry_height.pack()

label_width = tk.Label(root, text="Enter the width:")
label_width.pack()

entry_width = tk.Entry(root)
entry_width.pack()

label_material = tk.Label(root, text="Please choose the material of the box:")
label_material.pack()

material_choice_var = tk.StringVar()
material_choice_var.set("1")  # Default choice: Cardboard

radio_cardboard = tk.Radiobutton(root, text="Cardboard", variable=material_choice_var, value="1")
radio_cardboard.pack()

radio_wood = tk.Radiobutton(root, text="Wood", variable=material_choice_var, value="2")
radio_wood.pack()

button_calculate = tk.Button(root, text="Calculate", command=calculate_volume_weight)
button_calculate.pack()

root.mainloop()
