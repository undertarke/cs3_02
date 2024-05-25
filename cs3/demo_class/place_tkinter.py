import customtkinter
customtkinter.set_default_color_theme("green")  # green, dark-blue, blue
customtkinter.set_appearance_mode("system")  # system, light, dark

# khởi tạo thư viện => giao diện
root = customtkinter.CTk()

root.title("CyberSoft")
root.geometry("800x500")

# place
frame = customtkinter.CTkFrame(master=root, fg_color="red")
# 0 - 1: 0.1x100 = 10% , 0.5x100 = 50%



frameYellow = customtkinter.CTkFrame(master=root, fg_color="yellow")
frameYellow.place(relwidth=0.5, relheight=0.5, relx=0, rely=0)

frameRed = customtkinter.CTkFrame(master=root, fg_color="red")
frameRed.place(relwidth=0.5, relheight=0.5, relx=0.5, rely=0)



frameSilver = customtkinter.CTkFrame(master=root, fg_color="silver")
frameSilver.place(relwidth=0.5, relheight=0.5, relx=0, rely=0.5)

frameBlue = customtkinter.CTkFrame(master=root, fg_color="blue")
frameBlue.place(relwidth=0.5, relheight=0.5, relx=0.5, rely=0.5)


root.mainloop()
