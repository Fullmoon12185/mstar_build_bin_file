
import subprocess
import os.path
import glob

from Tkinter import *
#from Tkinter.ttk import Progressbar
import ttk

from utils.bin_built_scripts import auto_build_bin_file
from utils.unpacked_scripts import unpacked_scripts

auto_build_bin_file.test_import()
unpacked_scripts.test_import()

TV32_315_ROW_LABEL = 0
TV32_320_ROW_LABEL = 1
TV40_JP_ROW_LABEL = 2
TV32_JP_ROW_LABEL = 3
LABEL_COLUMN = 1

TV32_315_ROW_BUTTON = 0
TV32_320_ROW_BUTTON = 1
TV40_JP_ROW_BUTTON = 2
TV32_JP_ROW_BUTTON = 3
BUTTON_COLUMN = 3

TV32_315_ROW_BUTTON_COPY = 0
TV32_320_ROW_BUTTON_COPY = 1
TV40_JP_ROW_BUTTON_COPY = 2
TV32_JP_ROW_BUTTON_COPY = 3
BUTTON_COLUMN_COPY = 4

TV32_315_ROW_BUTTON_UNPACK = 0
TV32_320_ROW_BUTTON_UNPACK = 1
TV40_JP_ROW_BUTTON_UNPACK = 2
TV32_JP_ROW_BUTTON_UNPACK = 3
BUTTON_UNPACK_COLUMN = 0

TV32_315_ROW_PROGRESSBAR = 0
TV32_320_ROW_PROGRESSBAR = 1
TV40_ROW_PROGRESSBAR = 2
PROGRESSBAR_COLUMN = 3

PROGRESSBAR_LENGTH = 400

window = Tk() 	
style = ttk.Style()
style.configure('TButton', foreground= 'red', relief= 'sunken', padding= 5)
style.configure('TLabel', foreground= 'blue', padding= 10)
#style.configure('TProgressbar', foreground= 'red', padding= 10)
content = ttk.Frame(window, padding= (3,3,12,12))
 

lblTV32_315_HL = ttk.Label( window, text = "TV32 panel 315 HL!")
lblTV32_320_HL = ttk.Label( window, text = "TV32 panel 320 HL!")
lblTV40_JP = ttk.Label( window, text = "TV40 JP!")
lblTV32_JP = ttk.Label( window, text = "TV32_JP!")

btnTV32_315 = ttk.Button(window, text= "TV32_315", command = auto_build_bin_file.TV_32_Panel_315)
btnTV32_320 = ttk.Button(window, text= "TV32_320", command = auto_build_bin_file.TV_32_Panel_320)
btnTV40_JP = ttk.Button(window, text= "TV40_JP", command = auto_build_bin_file.TV_40_JP)
btnTV32_JP = ttk.Button(window, text= "TV32_JP", command = auto_build_bin_file.TV_32_JP)

btnTV32_315_copy = ttk.Button(window, text= "Copy TV32_315", command = auto_build_bin_file.TV_32_Panel_315_copy)
btnTV32_320_copy = ttk.Button(window, text= "Copy TV32_320", command = auto_build_bin_file.TV_32_Panel_320_copy)
btnTV40_JP_copy = ttk.Button(window, text= "Copy TV40_JP", command = auto_build_bin_file.TV_40_JP_copy)
btnTV32_JP_copy = ttk.Button(window, text= "Copy TV32_JP", command = auto_build_bin_file.TV_32_JP_copy)

btnTV32_315_unpack = ttk.Button (window, text= "TV32_315 unpack", command = unpacked_scripts.unpacked_TV32_315)
btnTV32_320_unpack = ttk.Button (window, text= "TV32_320 unpack", command = unpacked_scripts.unpacked_TV32_320)
btnTV40_JP_unpack = ttk.Button (window, text= "TV40 JP unpack", command = unpacked_scripts.unpacked_TV40_JP)
btnTV32_JP_unpack = ttk.Button (window, text= "TV32 JP unpack", command = unpacked_scripts.unpacked_TV32_JP) 
content.grid(column= 0, row= 0, sticky= (N, S, E, W))
#frame.grid(column= 0, row= 0, columnspan= 3, rowspan= 2, sticky= (N, S, E, W))

lblTV32_315_HL.grid(column = LABEL_COLUMN, row= TV32_315_ROW_LABEL, columnspan= 2, sticky= (N, W), padx= 5)
lblTV32_320_HL.grid(column = LABEL_COLUMN, row= TV32_320_ROW_LABEL, columnspan= 2, sticky= (N, W), padx= 5)
lblTV40_JP.grid(column = LABEL_COLUMN, row= TV40_JP_ROW_LABEL, columnspan= 2, sticky= (N, W), padx= 5 )
lblTV32_JP.grid(column = LABEL_COLUMN, row= TV32_JP_ROW_LABEL, columnspan= 2, sticky= (N, W), padx= 5)

#name.grid(column= 3, row= 1, columnspan= 2, sticky= (N, E, W), pady= 5, padx= 5)
btnTV32_315.grid(column = BUTTON_COLUMN, row = TV32_315_ROW_BUTTON, sticky = (W))
btnTV32_320.grid(column = BUTTON_COLUMN, row = TV32_320_ROW_BUTTON, sticky = (W))
btnTV40_JP.grid(column = BUTTON_COLUMN, row = TV40_JP_ROW_BUTTON, sticky = (W))
btnTV32_JP.grid(column = BUTTON_COLUMN, row = TV32_JP_ROW_BUTTON, sticky = (W))

#name.grid(column= 3, row= 1, columnspan= 2, sticky= (N, E, W), pady= 5, padx= 5)
btnTV32_315_copy.grid(column = BUTTON_COLUMN_COPY, row = TV32_315_ROW_BUTTON_COPY, sticky = (W))
btnTV32_320_copy.grid(column = BUTTON_COLUMN_COPY, row = TV32_320_ROW_BUTTON_COPY, sticky = (W))
btnTV40_JP_copy.grid(column = BUTTON_COLUMN_COPY, row = TV40_JP_ROW_BUTTON_COPY, sticky = (W))
btnTV32_JP_copy.grid(column = BUTTON_COLUMN_COPY, row = TV32_JP_ROW_BUTTON_COPY, sticky = (W))


btnTV32_315_unpack.grid(column = BUTTON_UNPACK_COLUMN, row = TV32_315_ROW_BUTTON, sticky = (W))
btnTV32_320_unpack.grid(column = BUTTON_UNPACK_COLUMN, row = TV32_320_ROW_BUTTON, sticky = (W))
btnTV40_JP_unpack.grid(column = BUTTON_UNPACK_COLUMN, row = TV40_JP_ROW_BUTTON, sticky = (W))
btnTV32_JP_unpack.grid(column = BUTTON_UNPACK_COLUMN, row = TV32_JP_ROW_BUTTON, sticky = (W))

#btnTV40.pack(padx= 20, pady= 20)

""" prbTV32_315 = ttk.Progressbar(	window, 
								orient = "horizontal",
								length = PROGRESSBAR_LENGTH, 
								mode = "determinate"
							)
prbTV32_315.grid(	column = PROGRESSBAR_COLUMN, 
					row = TV32_315_ROW_PROGRESSBAR, 
					sticky= (W)
				)
prbTV32_315["maximum"] = 100


prbTV32_320 = ttk.Progressbar(	window, 
								orient = "horizontal",
								length = PROGRESSBAR_LENGTH, 
								mode = "determinate"
							)
prbTV32_320.grid(	column = PROGRESSBAR_COLUMN, 
					row = TV32_320_ROW_PROGRESSBAR, 
					sticky= (W)
				)
prbTV32_320["maximum"] = 100
prbTV32_320["value"] = 0

prbTV40 = ttk.Progressbar(	window, 
							orient = "horizontal",
							length = PROGRESSBAR_LENGTH, 
							mode = "determinate"
						)
prbTV40.grid(	column = PROGRESSBAR_COLUMN, 
				row = TV40_ROW_PROGRESSBAR, 
				sticky= (W)
			)
prbTV40["maximum"] = 100
prbTV40["value"] = 50 """


window.mainloop()
