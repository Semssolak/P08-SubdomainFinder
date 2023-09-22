import requests
from tkinter import *
from PIL import Image, ImageTk


def make_request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        status_label.config(text="The site address you were looking for was not found")


url = None
driver = None

def website_finder():
    global url
    target_site = my_site_entry.get()
    target_word = my_word_entry.get()
    if len(my_site_entry.get()) == 0 or len(my_word_entry.get()) == 0:
        status_label.config(text="Please enter all info!")
    else:
        target_word = target_word.strip()
        url = "http://" + target_word + "." + target_site
        response = make_request(url)
        if response:
            my_url_label.config(text=url)

def on_entry_click(event):
    if my_site_entry.get() == "e.g. google.com":
        my_site_entry.delete(0, END)
        my_site_entry.config(fg='black')  # Yazı rengini değiştirmek isterseniz

def on_entry_leave(event):
    if my_site_entry.get() == "":
        my_site_entry.insert(0, "e.g. google.com")
        my_site_entry.config(fg='grey')  # Yazı rengini değiştirmek isterseniz



my_window = Tk()
my_window.title("Subdomain Finder")
my_window.minsize(width=300,height=200)
my_window.config(background="#4FC1E9")

my_icon = PhotoImage(file='sdficon.png')
my_window.iconphoto(False, my_icon)


my_img = Image.open("sdfimage.png")
new_width = 150
new_height = 100
my_img = my_img.resize((new_width, new_height))
tk_img = ImageTk.PhotoImage(my_img)
label = Label(my_window, image=tk_img)
label.grid(row=0, column=0, columnspan=2)
label.config(background="#4FC1E9")


my_word_label = Label(text="Select the Target Word")
my_word_label.grid(row=1, column=0, sticky="w")
my_word_label.config(background="#4FC1E9")

my_word_entry = Entry(width=25)
my_word_entry.grid(row=1, column=1)
my_word_entry.config(background="#E6E9ED")

my_site_label = Label(text="Select the Target Website")
my_site_label.grid(row=2, column=0, sticky="w")
my_site_label.config(background="#4FC1E9")

my_site_entry = Entry(width=25)
my_site_entry.grid(row=2, column=1)
my_site_entry.config(background="#E6E9ED")
my_site_entry.insert(0, "e.g. google.com")
my_site_entry.bind('<FocusIn>', on_entry_click)  # Giriş alanına tıklandığında
my_site_entry.bind('<FocusOut>', on_entry_leave)  # Giriş alanından çıkıldığında

find_button = Button(text="Find",command=website_finder)
find_button.grid(row=3, column=0, columnspan=2)
find_button.config(background="#B4DD7F")

status_label = Label(text="")
status_label.grid(row=4, column=0, columnspan=2)
status_label.config(background="#4FC1E9",fg="red")

my_url_label = Label(text="", fg="red", cursor="hand2")  # "cursor" ile fareyi el işareti yaparız
my_url_label.grid(row=5, column=0, columnspan=2)
my_url_label.config(background="#4FC1E9")

def open_url(event):
    if url:
        import webbrowser
        webbrowser.open(url)

my_url_label.bind("<Button-1>", open_url)  # <Button-1> sol fare tıklamasını temsil eder


my_window.mainloop()
