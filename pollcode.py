import os, time, string, random, tkinter, qrcode
from pystrich.ean13 import EAN13Encoder
import tkinter.filedialog
import tkinter.messagebox
from tkinter import *
from string import digits
root=tkinter.Tk()
number="1234567890"
letter="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+"
i=0
randstr=[]
fourth=[]
fifth=[]
randfir=""
randsec=""
randthr=""
str_one=""
strone=""
strtwo=""
nextcard=""
userput=""
nres_letter=""

# Create new folder
def mkdir(path):
    isexists = os.path.exists(path)
    if not isexists:
        os.mkdir(path)

# Open file, read file
def openfile(filename):
    f = open(filename)
    fllist = f.read()
    f.close()
    return fllist

# Based on showstr and order, display code
def inputbox(showstr, showorder, length):
    instr = input(showstr)
    if len(instr) != 0:
        # 1. number, no limit on counts
        # 2. letter
        # 3. number, but has limitation on counts
        if showorder == 1:
            if str.isdigit(instr):
                if int(instr) == 0:
                    print(
                        "\033[1;31;40m Value entered is Zero, please re-enter! \033[0m")
                    return "0"
                else:
                    return instr
            else:
                print(
                    "\033[1;31;40m Entered value is invalid, please re-enter! \033[0m")
                return "0"
        if showorder == 2:
            if str.isalpha(instr):
                if len(instr) != length:
                    print("\033[1;31;40m User has to enter " +
                          len(instr)+" letters, please reenter! \033[0m")
                    return "0"
                else:
                    return instr
            else:
                print(
                    "\033[1;31;40m Entered value is invalid, please re-enter! \033[0m")
                return "0"
        if showorder == 3:
            if str.isdigit(length):
                if len(instr) != length:
                    print("\033[1;31;40m User has to enter " +
                          len(instr)+" letters, please reenter! \033[0m")
                    return "0"
                else:
                    return instr
            else:
                print(
                    "\033[1;31;40m Entered value is invalid, please re-enter! \033[0m")
                return "0"
    else:
        print("\033[1;31;40m Empty value is invalid, please re-enter! \033[0m")
        return "0"

# write into file
def wfile(sstr, sfile, typeis, smsg, datapath):
    mkdir(datapath)
    datafile = datapath+"/"+sfile
    file = open(datafile, 'w')
    wrlist = sstr
    pdata = ""
    wdata = ""
    for i in range(len(wrlist)):
        wdata = str(wrlist[i].replace('[','')).replace(']','')
        wdata=wdata.replace("'",'').replace("'",'')
        file.write(str(wdata))
        pdata=pdata+wdata
    file.close()
    print("\033[1;31m"+pdata+"\033[0m")
    if typeis!="no":
        tkinter.messagebox.showinfo("!,", smsg+str(len(randstr))+"\n Security Code file stored at location: "+datafile)
        root.withdraw()

def mainmenu():
    print("""\033[1;35m
        *****************************************************************************************
                                        Product Code Generator
        *****************************************************************************************
            1. Generate 6 digits security code (213563)
            2. Generate 9 digits series product security code (879-335439)
            3. Generate 25 digits mixed product security code (B2R12-H4353-9FHRJ-23HVG-2HGLR)
            4. Generate data analysis security code (5AHFNGJI2345)
            5. Batch generate data analysis security code
            6. Add and generate data analysis security code (5AHFNGJI2345)
            7. Generate EAN-13 Barcode 
            8. Generate QRCode
            9. Fans lottery
            0. Exit
        =========================================================================================
                                Please enter number to choose menu
        =========================================================================================
    \033[0m""")

def input_validation(input):
    if str.isdigit(input):
        if int(input)==0:
            print("\033[1;32m  Invalid value, please enter again!  \33[0m]")
        else:
            return int(input)
    else:
        print("\033[1;32m  Invalid value, please enter again!  \33[0m]")

def scode1(strchoice):
    incount=inputbox("\033[1;32m    Please enter number of code you want to generate: \33[0m", 1, 0)
    while int(incount)==0:
        incount=inputbox("\033[1;32m    Please enter number of code you want to generate: \33[0m", 1, 0)
    randstr.clear()
    for j in range(int(incount)):
        randfir=''
        for i in range(6):
            randfir=randfir+random.choice(number)
        randfir=randfir+"\n"
        randstr.append(randfir)
    wfile(randstr,"score"+str(strchoice)+".txt","","Number of 6 digits security code is generated: ", "codepath")

def scode2(strchoice):
    ordstart=inputbox("\033[1;32m    Please enter product code (first 3 digits): \33[0m", 1, 0)
    while int(ordstart)==0 or len(ordstart)!=3:
        ordstart=inputbox("\033[1;32m    Please enter product code (first 3 digits): \33[0m", 1, 0)
    ordcount=inputbox("\033[1;32m    Please enter number of products: \33[0m", 1, 0)
    while int(ordcount)<1 or int(ordcount)>9999:
        ordcount=inputbox("\033[1;32m    Please enter number of products: \33[0m", 1, 0)
    incount=inputbox("\033[1;32m    Please enter number of code you want to generate: \33[0m", 1, 0)
    while int(incount)==0:
        incount=inputbox("\033[1;32m    Please enter number of code you want to generate: \33[0m", 1, 0)
    randstr.clear()
    for m in range(int(ordcount)):
        for j in range(int(incount)):
            randfir=''
            for i in range(6):
                randfir=randfir+random.choice(number)
            randstr.append(str(int(ordstart)+m)+randfir+'\n')
    wfile(randstr,"score"+str(strchoice)+".txt","","Number of 9 digits security code is generated: ", "codepath")

def scode3(strchoice):
    incount=inputbox("\033[1;32m    Please enter number of code you want to generate: \33[0m", 1, 0)
    while int(incount)==0:
        incount=inputbox("\033[1;32m    Please enter number of code you want to generate: \33[0m", 1, 0)
    randstr.clear()
    for j in range(int(incount)):
        strone=''
        for i in range(25):
            strone=strone+random.choice(number)
        strone=strone[:5]+'-'+strone[5:10]+'-'+strone[10:15]+'-'+strone[15:20]+'-'+strone[20:25]+"\n"
        randstr.append(strone)
    wfile(randstr,"score"+str(strchoice)+".txt","","Number of 25 digits security code is generated: ", "codepath")

def scode4(strchoice):
    intype=inputbox("\033[1;32m    Please enter data analysis code (first 3 letters): \33[0m", 1, 0)
    while not str.isalpha(intype) or len(intype)!=3:
        intype=inputbox("\033[1;32m    Please enter data analysis code (first 3 letters): \33[0m", 1, 0)
    incount=inputbox("\033[1;32m    Please enter number of code you want to generate: \33[0m", 1, 0)
    while int(incount)==0:
        incount=inputbox("\033[1;32m    Please enter number of code you want to generate: \33[0m", 1, 0)
    ffcode(incount, intype,"",strchoice)

def ffcode(scount, typestr, ismessage, schoice):
    randstr.clear()
    for j in range(int(scount)):
        strpro=typestr[0].upper()
        strtype=typestr[1].upper()
        strclass=typestr[2].upper()
        randfir=random.sample(number,3)
        randsec=sorted(randfir)
        letterone=''
        for i in range(9):
            letterone=letterone+random.choice(number)
        sim=str(letterone[0:int(randsec[0])]+strpro+letterone[int(randsec[0]):int(randsec[1])]
                +strtype+letterone[int(randsec[1]):int(randsec[2])]
                +strclass+letterone[int(randsec[2]):9]+"\n")
        randstr.append(sim)
    wfile(randstr,typestr+"score"+str(schoice)+".txt",ismessage,"Number of 25 digits security code is generated: ", "codepath")

while i<9:
    mainmenu()
    choice=input("\033[1;32m    Please enter your menu choice: \33[0m")
    if len(choice)!=0:
        choice=input_validation(choice)
        if choice==1:
            scode1(str(choice))
        elif choice==2:
            scode2(str(choice))
        elif choice==3:
            scode3(str(choice))
        elif choice==4:
            scode4(str(choice))
        elif choice==0:
            i=0
            print("Existing the system!")
    else:
        print("\033[1;31;40m  Invalid value, please enter again!  \33[0m")
        time.sleep(2)
