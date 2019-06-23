from tkinter import *
from tkinter import messagebox
import sqlite3
conn=sqlite3.connect("todo.db")
#conn.execute("create table tasks(task char(50),priority char(20)); ")
root=Tk()
#-----------------------------------------------------------------------------------------------
#func to exit the parent window
def exit():
    conn.close()
    root.destroy()

#function to delete the selected record in database    
def delete():
    
    print("deleted")

#func to ADD NEW TASK in database 
def add_task():
    add_task_window=Tk()
    add_task_window.geometry("500x500")
    
    #function to enter the note in database 
    def save():
        task=entry_task_description.get()
        priority=entry_task_priority.get()
        if task=="" or priority=="":
            messagebox.showinfo('ERROR','Please enter the details in both sections!')
        else:
            conn.execute("insert into tasks values('{}','{}');".format(task,priority))
            print("values saved succesfully")
        
    #func to save and exit the add new task window    
    def ok():
        conn.commit()
        add_task_window.destroy()
    
    l1=Label(add_task_window,text="Enter new task within 50 characters")
    l1.pack()
    entry_task_description=Entry(add_task_window,bd=3)
    entry_task_description.pack()
    
    l2=Label(add_task_window,text="Set the priority of the task")
    l2.pack()
    entry_task_priority=Entry(add_task_window,bd=3)
    entry_task_priority.pack()
    
    bttn_save=Button(add_task_window,text="SAVE",command=save)
    bttn_save.pack()
    bttn_ok=Button(add_task_window,text="OK",command=ok)
    bttn_ok.pack()
    
    add_task_window.mainloop()
#-----------------------------------------------------------------------------------------
#buttons on the parent window    
bttn_new_task=Button(root,text="+",command=add_task)
bttn_new_task.pack()
bttn_del_task=Button(root,text="Delete",command=delete)
bttn_del_task.pack()
bttn_exit=Button(root,text="Exit window",command=exit)
bttn_exit.pack()

#to display the NOTES 
cursor=conn.execute("select * from tasks;")
count=0
lb1=Listbox(root,selectmode=MULTIPLE)
for record in cursor:
    for cell in record:
        count=count+1
        print(cell)
        lb1.insert(count,"{}".format(cell))
lb1.pack()  


root.mainloop()
