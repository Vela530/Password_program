from tkinter import *
from tkinter import messagebox
import random
import csv
import json



#Window ---------------------------------------------------------------------------------------------------

window = Tk()
window.title("Password Manager")
window.geometry("450x325")
window.config(bg="white")





#Labels ---------------------------------------------------------------------------------------------------

website = Label(text="Website:", bg="white")
website.place(x=70, y=200)

email = Label(text="Email/Username:", bg="white")
email.place(x=50, y=225)


password = Label(text="Password:", bg="white")
password.place(x=70, y=250)


#Entry ---------------------------------------------------------------------------------------------------


entry1 = Entry(width=20)
entry1.get()
entry1.place(x=175, y=200)


entry2 = Entry(width=40)
entry2.get()
entry2.place(x=175, y=225)


entry3 = Entry(width=20)
entry3.get()
entry3.place(x=175, y=250)


#Button ---------------------------------------------------------------------------------------------------

def gen_pass():
    entry3.delete(0, END)
    password1 = ""
    password2 = ""
    randpass = "abcdefghijklmnopqrstuvwxyz1234567890 !@#$%^&*()+_=-ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(0, random.randint(10, 15)):
        password1 = random.choice(randpass)
        password2 = password2 + password1
    entry3.insert("end", password2)
    text_to_copy = entry3.get()
    window.clipboard_clear()
    window.clipboard_append(text_to_copy)
    window.update()

generate = Button(text="Generate Password", width=14, bg="white", command=gen_pass)
generate.place(x=311, y=245)



def add_button():
    web = entry1.get()
    email = entry2.get()
    user_password = entry3.get()
    new_data = {
        web: {
            "email": email,
            "password": user_password

        }
    }

    if entry1.get() == "" or entry2.get() == "" or entry3.get() == "":
        messagebox.showwarning("Error", "No fields can be left empty")
    else:
     
        try:

            with open('C:\\Users\\bvela\\OneDrive - Woodlands Church\\Desktop\\passwordkeeper.json', 'r') as textfile:
            #     textfile.write(f"{web} | {email} | {user_password}\n")
                #reading data
                data = json.load(textfile)
                #updating data
                data.update(new_data)
            with open('C:\\Users\\bvela\\OneDrive - Woodlands Church\\Desktop\\passwordkeeper.json', 'w') as textfile:
                #saving updated data
                json.dump(data, textfile, indent=4)
            messagebox.showinfo("Complete", "Your data has been added!")
        except:
            with open('C:\\Users\\bvela\\OneDrive - Woodlands Church\\Desktop\\passwordkeeper.json', 'w') as textfile:
                #Incase a file is not open yet
                json.dump(new_data, textfile, indent=4)
            messagebox.showinfo("Complete", "Your data has been added!")
    
    

    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)



def search_button():
    with open ('C:\\Users\\bvela\\OneDrive - Woodlands Church\\Desktop\\passwordkeeper.json', 'r') as textfile:
        data = json.load(textfile)
        print(data[entry1.get()].values())
        messagebox.showinfo(entry1.get(), f"Email: {data[entry1.get()]['email']}\nPassword: {data[entry1.get()]['password']}")



add = Button(text="Add", width=34, bg="white", command=add_button)
add.place(x=174, y=275)


search = Button(text="Search", width=14, bg="white", command=search_button)
search.place(x=311, y=195)


#Photo ---------------------------------------------------------------------------------------------------

slogo = PhotoImage(file="C:/Users/bvela/VSP/100days/logo.png")
window.iconphoto(True, slogo)

canvas = Canvas(width=175, height=200, bg="white", highlightthickness=0)
logo = PhotoImage(file="C:/Users/bvela/VSP/100days/logo.png")
canvas.create_image(100, 112, image=logo)
canvas.place(x=130, y=-15)













window.mainloop()