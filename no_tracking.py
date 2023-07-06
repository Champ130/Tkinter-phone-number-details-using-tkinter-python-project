from tkinter import *
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone
root=Tk()
root.title("phone number details using python")
root.geometry("500x500")
root.configure(bg="red")
root.resizable=(0,0)
#heading
label1= Label(root,text="enter your phone number")
label1.pack()
def getlocation():
    num=number.get("1.0",END)
    print(num)
    num=phonenumbers.parse(num)
    result.insert(END,"the countruy of the number is"+geocoder.description_for_number(num, "en"))
    result.insert(END,"\n the sim card of the number is "+carrier.name_for_number(num, "en"))
    result.insert(END,"\n the timezone in which your number is"+str(timezone.time_zones_for_number(num)))
                 
    
    
    
number=Entry(root,width=20)
number.pack()
bt1=Button(root,text="enter",command=getlocation)
bt1.pack()
result=Text(root,width=75,height=10,x=-500)
result.pack()
root.mainloop()
