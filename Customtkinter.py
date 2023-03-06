import customtkinter
#comment
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("800x500")

def combobox_callback(choice):
    print("combobox dropdown clicked: ", choice)
    if choice == "light":
        customtkinter.set_appearance_mode("light")
    elif choice == "dark":
        customtkinter.set_appearance_mode("dark")
    elif choice == "system":
        customtkinter.set_appearance_mode("System")

def login():
    print("Test")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login System")
label.pack(pady=12,padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="#")
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="login", command=login)
button.pack(pady=12, padx=10)

combobox_var = customtkinter.StringVar(value="Theme")



combobox = customtkinter.CTkComboBox(master=frame, values=["light","dark","system"], command=combobox_callback, variable=combobox_var)
combobox.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)

root.mainloop()