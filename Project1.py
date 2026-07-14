import pandas as pd
import numpy as np
class Saxena_Home:
    def __init__(self,name):
        self.name=name
        self.menu=pd.read_excel("Home_Food.xlsx","Sheet1",engine="openpyxl")
    def menu_choice(self):
        print("Hope You Are Doing Awesome")
        print("Please Select The Operation")
        print("1) View Menu")
        print("2) Add Items")
        print("3) Make A Draw For Today")
    def create(self):
        print(f"Welcome {self.name} !")
        self.menu_choice()
        choice=int(input("Enter Your Choice"))
        match(choice):
            case 1: self.view_Data()
            case 2: self.add_Data()
            case 3: self.choose_Data()
        print("Hope You Would Like The Service\nPlease Visit Again")
    def view_Data(self):
        new_view=self.menu.groupby("Course")
        for course,group in new_view:
            print(course)
            print(group)
    def add_Data(self):
        cname=input("Enter Type of Course: ")
        food=input("Enter Name of Food: ")
        shift=input("Enter Shift: ")
        time=input("Enter Time Slot: ")
        store=np.array([[cname,food,shift,time]])
        new_Data=pd.DataFrame(store,columns=["Course","Food Item","Shift","Time"])
        self.menu=pd.concat([self.menu,new_Data],ignore_index=True)
        self.menu.to_excel("Home_Food.xlsx",sheet_name="Sheet1",index=False)
    def choose_Data(self):
        new_view=self.menu.groupby("Course")
        for course,group in new_view:
            print(group.sample(n=1))
name=input("Please Enter Your Name: ")
Response=Saxena_Home(name)
Response.create()


