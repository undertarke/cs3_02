import customtkinter
customtkinter.set_default_color_theme("green")  # green, dark-blue, blue
customtkinter.set_appearance_mode("system")  # system, light, dark


# khởi tạo thư viện => giao diện
root = customtkinter.CTk()

root.title("CyberSoft")
root.geometry("800x500")

# frame => khung
# 1/ pack
# 2/ place
# 3/ grid
# tham số 1: master =>
frameTop = customtkinter.CTkFrame(master=root,  fg_color="black")
frameTop.pack(side="top",expand=True, fill="both")


frameYellow = customtkinter.CTkFrame(master=frameTop, fg_color="yellow")
# side = top , bottom , left , right
# expand = True , False
# fill = both , x , y
frameYellow.pack(side="left", expand=True, fill="both")

frameRed = customtkinter.CTkFrame(master=frameTop, fg_color="red")
frameRed.pack(side="right", expand=True, fill="both")


frameBot = customtkinter.CTkFrame(master=root,  fg_color="black")
frameBot.pack(side="bottom",expand=True, fill="both")


frameSilver = customtkinter.CTkFrame(master=frameBot, fg_color="silver")
frameSilver.pack(side="left", expand=True, fill="both")

frameBlue = customtkinter.CTkFrame(master=frameBot, fg_color="blue")
frameBlue.pack(side="right", expand=True, fill="both")

# widgets

# class

# vòng lặp giao diện
root.mainloop()
