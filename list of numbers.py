from tkinter import*
import random
root=Tk()

root.title("list of numbers")
root.geometry("400x400")
root.configure(background="red")

numbers=Label(root,text="list of random numbers: ")
numbers.place(relx=0.5,rely=0.2,anchor=CENTER)

sorted_numbers=Label(root,text="list of sorted numbers: ")
sorted_numbers.place(relx=0.5,rely=0.3,anchor=CENTER)

def generate():
    r=random.sample(range(50,100),10)
    numbers["text"]+=str(r)
    
    r.sort()
    sorted_numbers["text"]+=str(r)
    

btn=Button(root,text="numbers",command=generate)
btn.place(relx=0.5,rely=0.6,anchor=CENTER)

root.mainloop()



