from bs4 import BeautifulSoup # Importing the BeautifulSoup package
import requests # Importing requests library
import csv
import pandas as pd
import datetime

# for timezone()
import pytz
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import tkinter.messagebox

main_win = tkinter.Tk()
main_win.title("Web Scrapping")
main_win.geometry("400x500")
main_win.sourceFile = ''


Title_text = Label(text="Data Extraction using Web Scrapping")
Title_text.place(x=15,y=20)

path = StringVar()
first_name_entry = Entry(textvariable=path, width="40")
first_name_entry.place(x=15, y=150)


def chooseFile():
    main_win.sourceFile = filedialog.askopenfilename(parent=main_win, initialdir= "/", title='Please select a file')
    path.set(main_win.sourceFile)

b_chooseFile = tkinter.Button(main_win, text = "Choose File", width = 20, height = 3, command = chooseFile)
b_chooseFile.place(x = 15,y = 80)
b_chooseFile.width = 100


def save_info():
    links=[]
    datalist=[]
    file_path=main_win.sourceFile
    file1 = open(file_path, 'r')
    Lines = file1.readlines()
    for i in Lines:
        size=len(i)
        temp=i[:size-2]
        links.append(temp)
    print(links)
    for link in range(len(links)):
        # print(link)
        req = requests.get(links[link])  # Requesting the content of the URLcontent = req.content # Getting the cont
        content = req.content
        soup = BeautifulSoup(content, 'html.parser')
        # print(soup.prettify())
        desc = soup.find_all('li', class_='spec-highlight__item')
        descriptions = []
        for i in range(len(desc)):
            descriptions.append(desc[i].text)
        #descriptions
        len(descriptions)
        d = descriptions
        commonclass = soup.find_all('li', class_='spec-highlight__item')
        resolution = []
        bluetooth = []
        # series = []
        motionrate = []
        hdr = []

        for i in range(0, len(commonclass)):
            p = commonclass[i].text  # Extracting the text from the tags
            n = "None"
            if "Resolu" in p:
                resolution.append(p)

            if "Blueto" in p:
                bluetooth.append(p)

            #    if("Series" in p):
            #        series.append(p)
            if "Motion R" in p:
                motionrate.append(p)

            if "HDR" in p:
                hdr.append(p)

        # print(len(series))
        # print(resolution)
        # print(bluetooth)

        # print(motionrate)
        # print(hdr)
        # import openpyxl
        # from openpyxl import load_workbook
        # print(link)
        tabl_link = []
        tabl_link.append(links[link])
        d = {'Link': tabl_link, 'Resolution': resolution, 'Bluetooth': bluetooth, 'Motion Rate': motionrate, 'HDR': hdr}
        dataset = pd.DataFrame.from_dict(d, orient='index')
        datalist.append(dataset)
        #print(dataset)

        tabl_link.clear()
    datalist = pd.concat(datalist)
    # print(datalist)

    datalist.to_excel('output_reports/Report_Generated_{}.xlsx'.format(pd.datetime.today().strftime('%y%m%d-%H%M%S')))

    tkinter.messagebox.showinfo("Message","Data Extraction Completed.")
    path.set("")
process_btn = tkinter.Button(main_win, text = "Export Excel", width = 20, height = 3, command = save_info)
process_btn.place(x=15,y=200)

main_win.mainloop()
#print(main_win.sourceFile )
