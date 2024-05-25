import customtkinter
customtkinter.set_default_color_theme("green")  # green, dark-blue, blue
customtkinter.set_appearance_mode("system")  # system, light, dark

# khởi tạo thư viện => giao diện
root = customtkinter.CTk()

root.title("CyberSoft")
root.geometry("800x500")


for column in range(0,2):
    root.columnconfigure(column, weight=1)
    root.rowconfigure(column,weight=1)
    

frame = customtkinter.CTkFrame(master=root, fg_color="red")
frame.grid(row=0, column=0, sticky="nesw")

frame2 = customtkinter.CTkFrame(master=root, fg_color="blue")
frame2.grid(row=1, column=1, sticky="nesw")

root.mainloop()
