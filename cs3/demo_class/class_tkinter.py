import customtkinter



class FrameGrid(customtkinter.CTkScrollableFrame):
    def __init__(self, master, fg_color):
        super().__init__(master=master, fg_color=fg_color)
        self.grid(row=0, column=0, sticky="news")

        for index in range(0,50):
            button = customtkinter.CTkButton(self, text=f"nut so {index}", command= lambda index=index : self.button_event(index))

            button.pack(pady=10)

    def button_event(self,index):
        print(f"nut so {index}")



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("CyberSoft")
        self.geometry("800x500")

        FrameGrid(self, "silver")


app = App()

for column in range(0, 1):
    app.columnconfigure(column, weight=1)
    app.rowconfigure(column, weight=1)
app.mainloop()
