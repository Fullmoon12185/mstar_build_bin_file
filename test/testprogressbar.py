import sys
import ttk
from Tkinter import *

mGui = Tk()

mGui.geometry('450x450')
mGui.title('Hanix Downloader')

mpb = ttk.Progressbar(mGui,orient ="horizontal",length = 200, mode ="determinate")
mpb.pack()
mpb["maximum"] = 100
mpb["value"] = 50

mGui.mainloop()