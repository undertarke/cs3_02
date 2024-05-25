import customtkinter
customtkinter.set_default_color_theme("green")  # green, dark-blue, blue
customtkinter.set_appearance_mode("system")  # system, light, dark

# khởi tạo thư viện => giao diện
root = customtkinter.CTk()

root.title("CyberSoft")
root.geometry("800x500")

entry = customtkinter.CTkEntry(root, placeholder_text="Hãy gõ gì đó ....")
entry.pack()

def button_event(title):
    print(entry.get()) # lấy dữ liệu nhập từ entry

button = customtkinter.CTkButton(root, text="bấm nút",text_color="red", fg_color="blue", command=lambda: button_event("hello"))
button.pack()

def checkbox_event():
    print("checkbox toggled, current value:", check_var.get())

check_var = customtkinter.StringVar(value="on")
checkbox = customtkinter.CTkCheckBox(root, text="CTkCheckBox", command=checkbox_event,variable=check_var, onvalue="on", offvalue="off")
checkbox.pack()

progressbar = customtkinter.CTkProgressBar(root, orientation="horizontal", determinate_speed=200)
progressbar.pack()

def slider_event(value):
    print(value)

slider = customtkinter.CTkSlider(root, from_=0, to=100, command=slider_event)
slider.pack()

# pip install Pillow 
from PIL import Image


my_image = customtkinter.CTkImage(light_image=Image.open("img/la-ban.png"),
                                  dark_image=Image.open("img/la-ban.png"),
                                  size=(330, 330))

image_label = customtkinter.CTkLabel(root, image=my_image, text="")  # display image with a CTkLabel
image_label.pack()

root.mainloop()
