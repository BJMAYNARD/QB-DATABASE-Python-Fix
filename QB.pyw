import tkinter
import tkinter as tk
from tkinter import *
import os
import sys
import time
import logging
import GUI2

# Main Function of The GUI


def main():
    # First the QBC Monitor
    def reset_QBCFM():
        os.system("net stop QBCFMonitorService")
        time.sleep(3)
        os.system("net start QBCFMonitorService")
        time.sleep(3)
        logging.basicConfig(format='%(asctime)s - %(message)s',
                            datefmt='%d-%b-%y %H:%M:%S',
                            filemode='w')

        logging.info('QBC Monitor Reset')
        logger = logging.getLogger(QBCFM)

    # Second the QBIDPService

    def reset_QBIDS():
        os.system("net stop QBIDPService")
        time.sleep(3)
        os.system("net start QBIDPService")
        time.sleep(3)
        logging.basicConfig(format='%(asctime)s - %(message)s',
                            datefmt='%d-%b-%y %H:%M:%S',
                            filemode='w')
        logging.info('QBID Service Reset')
        logger = logging.getLogger(QBIDS)

    # Now the QB Database Manager

    def reset_QBDM():
        os.system("net stop QuickBooksDB29")
        time.sleep(2)
        os.system("net start QuickBooksDB29")
        time.sleep(3)
        logging.basicConfig(format='%(asctime)s - %(message)s',
                            datefmt='%d-%b-%y %H:%M:%S',
                            filemode='w')
        logging.info('QB Database Manager Reset')
        logger = logging.getLogger(QBDM)

    # Logging the Results
file_path = r'C:/Test_Reset/Reset_Log_File.txt'
if os.path.exists(file_path):
    if __name__ == '__main__':

        logging.basicConfig(filename="C:/Test_Reset/Reset_Log_File.txt",
                            level=logging.INFO,
                            format='%(levelname)s: %(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S')
        reset_QBCFM()
        reset_QBIDS()
        reset_QBDM()
else:
    # create a file
    with open(file_path, 'w') as fp:
        fp.write()

        if __name__ == '__main__':

            logging.basicConfig(filename="C:/Test_Reset/Reset_Log_File.txt",
                                level=logging.INFO,
                                format='%(levelname)s: %(asctime)s %(message)s',
                                datefmt='%m/%d/%Y %I:%M:%S')
            reset_QBCFM()
            reset_QBIDS()
            reset_QBDM()


# GUI Creation
ws = Tk()
ws.title(string='')
ws.geometry('300x100')

frame1 = LabelFrame(
    ws,
    text='QB QUICK FIX',
    bg='#BFC9CA',
    font=(20),
)
frame1.pack(expand=True, fill=BOTH)

Button(
    frame1,
    bg='white',
    text='Click Here To Fix Services',
    font=(30),
    command=lambda: [GUI2, main]
    # calls the main function and has the 2nd GUI come up

).pack()


frame1.pack(expand=True, fill=BOTH)

Button(
    frame1,
    bg='white',
    text='Click Here To Exit',
    font=(30),
    command=exit
).pack()

ws.mainloop()
