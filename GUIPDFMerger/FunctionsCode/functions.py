#file path browser
from tkinter import filedialog
from tkinter import *
import os
import PyPDF2
import datetime

import logging
logger = logging.getLogger()
log = logging.getLogger(__name__)

def get_file_path():
    try:
        filename = filedialog.askopenfilename(title = "open")
        return
    except Exception as e:
        pass

##PDF merger function
def merge_pdf(folder_path,pdf_file_list):
    today = datetime.datetime.now()
    date_time = today.strftime("%m%d%Y_%H%M%S_")
    mergeFile = PyPDF2.PdfFileMerger()
    file_list = pdf_file_list
    log.info("Merge_pdf Function : Merging PDF")
    try:
        for pdf in pdf_file_list:
            if len(pdf_file_list)>1:
                mergeFile.append(PyPDF2.PdfFileReader(folder_path + "//" + pdf, "rb"))
        mergeFile.write(folder_path + "\\" + date_time+"MergedFile.pdf")
        log.info("New Merger PDF Created with name :" + date_time + "MergedFile.pdf")
    except Exception as e:
        log.error("Merge_pdf Function : Error occured while merging pdf")
        log.exception("Exception occured :" + str(e))


#FIle listing Function
def get_all_files(folder_path):
    log.info("Get_all_files_function")
    try:
        all_file_list = os.listdir(folder_path)
    except Exception as e:
        log.error("Get_all_files_function : Error occured while fetching file name")
        log.exception("Exception occured : " + str(e))
    pdf_file_list=[]
    try:
        for file in all_file_list:
            if file.find("pdf") > 0:
                pdf_file_list.append(file)
        return (all_file_list,pdf_file_list)
    except Exception as e :
        log.error("get_all_files Function : Error occured while iterating file name")
        log.exception("Exception occured :" + str(e))