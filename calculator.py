import math
from tkinter import *
import math as m
from pygame import mixer
import speech_recognition #This module is used for converting the audio into text command and do the following#

mixer.init()

#Main Calculation
def click(value):
    ex=entrydata.get()
    answer=''
    try:
        if (value == "C"):
            ex = ex[0:len(ex) - 1]
            entrydata.delete(0, END)
            ex = entrydata.insert(0, ex)
            return
        elif (value == "CE"):
            entrydata.delete(0, END)
        elif (value == "√"):
            answer = m.sqrt(eval(ex))
        elif (value == "π"):
            answer = m.pi
        elif (value == "cosθ"):
            answer = m.cos(m.radians(eval(ex)))
        elif (value == "tanθ"):
            answer = m.tan(m.radians(eval(ex)))
        elif (value == "sinθ"):
            answer = m.sin(m.radians(eval(ex)))
        elif (value == "2π"):
            answer = 2 * m.pi
        elif (value == "cosh"):
            answer = m.cosh(eval(ex))
        elif (value == "tanh"):
            answer = m.tanh(eval(ex))
        elif (value == "sinh"):
            answer = m.sinh(eval(ex))
        elif (value==chr(8731)):
            answer=eval(ex)**(1/3);
        elif (value=="x\u02b8"):
            entrydata.insert(END,"**")
            return
        elif (value=="x\u00B3"):
            answer=eval(ex)**3
        elif (value=="x\u00B2"):
            answer=eval(ex)**2
        elif (value=="ln"):
            answer=m.log2(eval(ex))
        elif (value=="deg"):
            answer=m.degress(eval(ex))
        elif (value=="rad"):
            answer=m.radians(eval(ex))
        elif (value=="e"):
            answer=math.e
        elif (value=="log₁₀"):
            answer=m.log10(eval(ex))
        elif (value=="x!"):
            answer=m.factorial(ex)
        elif (value==chr(247)):
            entrydata.insert(END,"/")
            return
        elif (value=="="):
            answer=eval(ex)
        else:
            entrydata.insert(END,value)
            return
        entrydata.delete(0, END)
        entrydata.insert(0, answer)
    except SyntaxError:
        pass
# Creating the mic-audio to work whuile giving audio for calculation #
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
def lcm(a,b):
    l=m.lcm(a,b)
    return l
def hcf(a,b):
    h=m.gcd(a,b)
    return h
#Dictionary Of keys that the user will use as command for doing operation#
operations={'ADD':add,'ADDITION':add,'SUM':add,'PLUS':add,
            'SUBTRACTION':sub,'DIFFERENCE':sub,'MINUS':sub,'SUBTRACT':sub,
            'PRODUCT': mul,'MULTIPLICATION': mul,'MULTIPLY': mul,
            'DIVISION': div, 'DIV': div, 'DIVIDE': div,
            'LCM':lcm ,'HCF':hcf,
            'MOD':mod,'REMAINDER':mod,'MODULUS':mod }
def findNumbers(t):
    l=[]
    for num in t:
        try:
            l.append(int(num))
        except ValueError:
            pass
    return l

def audio():
    mixer.music.load('music1.mp3')
    mixer.music.play()
    sr = speech_recognition.Recognizer()
    with speech_recognition.Microphone()as m:
        try:
            sr.adjust_for_ambient_noise(m,duration=0.2)
            voice=sr.listen(m)
            text=sr.recognize_google(voice)

            mixer.music.load('music2.mp3')
            mixer.music.play()
            text_list=text.split(' ')
            for word in text_list:
                if word.upper() in operations.keys():
                    l=findNumbers(text_list)
                    print(l)
                    result=operations[word.upper()](l[0],l[1]) #mul(5.0,6.0)
                    entrydata.delete(0,END)
                    entrydata.insert(END,result)

                else:
                    pass


        except:
            pass

root=Tk() # We have made the object of the Tk class named as root #
root.geometry("680x470+100+100")
root.title("Smart Calculator App")
root.config(bg="dodgerblue")

#Creating The Logo of calculator#
logoimage=PhotoImage(file="logo.png")
logolabel=Label(root,image=logoimage,bg="dodgerblue3",relief=SUNKEN)
logolabel.grid(row=0,column=0)

#Creating The Entry Field where we enter the values using the predoidefined class called Entry()#
entrydata=Entry(root,font=("Times New Roman",25,"bold"),bg="white",fg="black",relief=SUNKEN,bd=10,width=30)
entrydata.grid(row=0,column=0,columnspan=8)

#Creating The Mic Button#
micimage=PhotoImage(file="microphone.png")
micbutton=Button(root,image=micimage,bd=0,bg="dodgerblue",activebackground="black",command=audio)
micbutton.grid(row=0,column=7)

#Creating The Buttons#
buttontext_list=["C","CE","√","+","π","cosθ","tanθ","sinθ",
                 "1","2","3","-","2π","cosh","tanh","sinh",
                 "4","5","6","*",chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
                 "7","8","9",chr(247), "ln", "deg", "rad", "e",
                 "0",".","%","=","log₁₀","{","}","x!"]
rowvalue,columnvalue=1,0
for i in buttontext_list:
    button=Button(root,text=i,font=("arial",18,"bold"),bd=2,width=5,height=2,relief=SUNKEN,bg="white",fg="black",
                  activebackground="dodgerblue3",activeforeground="black",command=lambda button=i: click(button))
    button.grid(row=rowvalue,column=columnvalue,pady=1,padx=1)
    columnvalue+=1
    if(columnvalue>7):
        rowvalue+=1
        columnvalue=0

root.mainloop() # We have written the mainloop bcoz we can see our window/GUI multiple times #