import logging

logger = logging.getLogger()
log = logging.getLogger(__name__)

logging.info("Entered into GUI Code File")

# Importing Library

from tkinter import *
import os
import PyPDF2
import re
import datetime

from FunctionsCode.functions import merge_pdf
from FunctionsCode.functions import get_all_files

## Submit button Action
def submit_click():
    logging.info("Submit Button Clicked")
    pdf_file_output.delete(0.0,END)
    all_file_output.delete(0.0,END)

    folder_Path = folder_path_text.get()
    logging.info("Entered folder path is : " + folder_Path)

    logging.info("Calling Get All The file Function")
    all_file_list, pdf_file_list = get_all_files(folder_Path)

    logging.info("Printing all file list")
    for file in all_file_list:
        all_file_output.insert(END,f"{file}\n")

    logging.info("Printing PDF file list")
    for file in pdf_file_list:
        pdf_file_output.insert(END,f"{file}\n")

# PDF button Action
def pdf_click():
    logging.info("PDF Merge Button Clicked")
    logging.info("Calling Get All File Function")
    folder_Path = folder_path_text.get()
    logging.info("Enter folder Path is : " + folder_Path)
    all_file_list, pdf_file_list = get_all_files(folder_Path)
    logging.info("Merge PDF Function")
    merge_pdf(folder_Path,pdf_file_list)
    pdf_file_output.delete(0.0,END)
    all_file_list,pdf_file_list = get_all_files(folder_Path)
    logging.info("Updating PDF List after Merging")
    for file in pdf_file_list:
        pdf_file_output.insert(END,f"{file}\n")

# Clear Button Action
def clear_click():
    logging.info("Clear Button clicked")
    pdf_file_output.delete(0.0,END)
    all_file_output.delete(0.0,END)

# Initiating Tk Window
window = Tk()
window.title("PDF Merger")
window.configure(background="#8e5c6e")
window.geometry('900x600')

# Adding title image
# # title.img = PhotoImage(file="Title.png") ## To be used when only running from GUICode.py file
# title_img = PhotoImage(file=r"C:\Users\ashish\Desktop\Ineuron\pythonProjec\GUIPDFMerger\Main Files\GUI File\pngwing.com.png")
# Label(window,image=title_img,fg="black").grid(row=0,column=0,sticky="w")

# Create Label for Enter path
Label(window,text = "Enter Path : ", bg= "#0e5c6e",fg = "white", font= "none 12 bold").grid(row=1,column = 0, sticky ="e")

# Adding Text box folder path entry
folder_path_text = Entry(window,width=40,bg="white")
folder_path_text.grid(row=1,column=1,sticky="w")

# Adding submit button
submit_button = Button(window,text = "Submit", relief=SOLID, width= 8, command= submit_click,pady=10)
submit_button.grid(row=1,column=2,sticky="w")

#print all file List
Label (window,text="\nAvailable Files in enter folder are as below : ",bg = "#0e5c6e",fg="white",
       font=("Arial",10,"bold")).grid(row=3,column=0,sticky="w")
all_file_output = Text(window,width=50,height=20,wrap=WORD,bg="white",fg="black",font=("Arial",10))
all_file_output.grid(row=4,column=0,sticky="w")
#print pdf file List
Label (window,text="\nAvailable PDF Files : ", bg="#0e5c6e",fg="white",font=("Arial",10,"bold")).grid(row=3,column=1,sticky='w')
pdf_file_output = Text(window,width=50,height=20,wrap=WORD,bg="white",fg="black",font=("Arial",10))
pdf_file_output.grid(row=4,column=1,sticky="w")

#Adding button for pdf merger
pdf_button = Button(window,text="Merge PDF and\n Update List",relief=SOLID,width=12,command=pdf_click,pady=10)
pdf_button.grid(row=4,column=3,sticky='w')

#Adding button for clear
clear_button = Button(window,text="clear_all",relief=SOLID,width=12,command=clear_click,pady=10)
clear_button.grid(row=5,column=3,sticky="w")

#Run GUI
logging.info("Opening GUI Window")
window.mainloop()
logging.info("Closed GUI Window")