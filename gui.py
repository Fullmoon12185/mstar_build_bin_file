
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

num_of_rows = 11

TV32_315_ROW_LABEL, \
TV32_315_ROW_LABEL_PANA, \
TV32_320_ROW_LABEL, \
TV40_JP_ROW_LABEL, \
TV40_HL_ROW_LABEL_PANA, \
TV32_JP_ROW_LABEL, \
TV50_JP_ROW_LABEL, \
TV50_JP_ROW_LABEL_PANA, \
TV50_JP_SQ5_ROW_LABEL, \
TV55_HL_ROW_LABEL, \
TV55_HL_ROW_LABEL_PANA = range(num_of_rows)
LABEL_COLUMN = 1

TV32_315_ROW_BUTTON, \
TV32_315_ROW_BUTTON_PANA, \
TV32_320_ROW_BUTTON, \
TV40_JP_ROW_BUTTON, \
TV40_HL_ROW_BUTTON_PANA, \
TV32_JP_ROW_BUTTON, \
TV50_JP_ROW_BUTTON, \
TV50_JP_ROW_BUTTON_PANA, \
TV50_JP_SQ5_ROW_BUTTON, \
TV55_HL_ROW_BUTTON, \
TV55_HL_ROW_BUTTON_PANA = range(num_of_rows)
BUTTON_COLUMN = 3

TV32_315_ROW_BUTTON_COPY, \
TV32_315_ROW_BUTTON_COPY_PANA, \
TV32_320_ROW_BUTTON_COPY, \
TV40_JP_ROW_BUTTON_COPY, \
TV40_HL_ROW_BUTTON_COPY_PANA, \
TV32_JP_ROW_BUTTON_COPY, \
TV50_JP_ROW_BUTTON_COPY, \
TV50_JP_ROW_BUTTON_COPY_PANA, \
TV50_JP_SQ5_ROW_BUTTON_COPY, \
TV55_HL_ROW_BUTTON_COPY, \
TV55_HL_ROW_BUTTON_COPY_PANA = range(num_of_rows)
BUTTON_COLUMN_COPY = 4

TV32_315_ROW_BUTTON_UNPACK, \
TV32_315_ROW_BUTTON_UNPACK_PANA, \
TV32_320_ROW_BUTTON_UNPACK, \
TV40_JP_ROW_BUTTON_UNPACK, \
TV40_HL_ROW_BUTTON_UNPACK_PANA, \
TV32_JP_ROW_BUTTON_UNPACK, \
TV50_JP_ROW_BUTTON_UNPACK, \
TV50_JP_ROW_BUTTON_UNPACK_PANA, \
TV50_JP_SQ5_ROW_BUTTON_UNPACK, \
TV55_HL_ROW_BUTTON_UNPACK, \
TV55_HL_ROW_BUTTON_UNPACK_PANA = range(num_of_rows)
BUTTON_UNPACK_COLUMN = 0


window = Tk() 	
style = ttk.Style()
style.configure('TButton', foreground= 'black', relief= 'sunken', padding= 5)
style.configure('TLabel', foreground= 'blue', padding= 10)
#style.configure('TProgressbar', foreground= 'red', padding= 10)
content = ttk.Frame(window, padding= (3,3,12,12))
 

lblTV32_315_HL = ttk.Label( window, text = "TV32 panel 315 HL!")
lblTV32_320_HL = ttk.Label( window, text = "TV32 panel 320 HL!")
lblTV40_JP = ttk.Label( window, text = "TV40 JP!")
lblTV40_HL_PANA = ttk.Label( window, text = "TV40 HL pana!")
lblTV32_JP = ttk.Label( window, text = "TV32_JP!")
lblTV50_JP = ttk.Label( window, text = "TV50 JP!")
lblTV50_JP_PANA = ttk.Label( window, text = "TV50 JP pana!")
lblTV50_JP_SQ5 = ttk.Label( window, text = "TV50 JP SQ5!")
lblTV55_HL = ttk.Label( window, text = "TV55 HL!")
lblTV55_HL_PANA = ttk.Label( window, text = "TV55 HL PANA!")
lblTV32_315_HL_PANA = ttk.Label( window, text = "TV32 panel 315 HL PANA!")

###########################################################################################################
btnTV32_315 = ttk.Button(window, text= "TV32_315", command = auto_build_bin_file.TV_32_Panel_315)
btnTV32_320 = ttk.Button(window, text= "TV32_320", command = auto_build_bin_file.TV_32_Panel_320)

btnTV40_JP = ttk.Button(window, text= "TV40_JP", command = auto_build_bin_file.TV_40_JP)
btnTV40_HL_pana = ttk.Button(window, text= "TV40_HL pana", command = auto_build_bin_file.TV_40_HL_pana)
btnTV32_JP = ttk.Button(window, text= "TV32_JP", command = auto_build_bin_file.TV_32_JP)

btnTV50_JP = ttk.Button(window, text= "TV50_JP", command = auto_build_bin_file.TV_50_JP)
btnTV50_JP_pana = ttk.Button(window, text= "TV50_JP pana", command = auto_build_bin_file.TV_50_JP_pana)

btnTV50_JP_SQ5 = ttk.Button(window, text= "TV50_JP_SQ5", command = auto_build_bin_file.TV_50_JP_SQ5)
btnTV55_HL = ttk.Button(window, text= "TV55_HL", command = auto_build_bin_file.TV_55_HL)

btnTV55_HL_pana = ttk.Button(window, text= "TV55_HL pana", command = auto_build_bin_file.TV_55_HL_pana)
btnTV32_315_pana = ttk.Button(window, text= "TV32_315_pana", command = auto_build_bin_file.TV_32_Panel_315_pana)

################################################################################################################


btnTV32_315_copy = ttk.Button(window, text= "Copy TV32_315", command = auto_build_bin_file.TV_32_Panel_315_copy)
btnTV32_320_copy = ttk.Button(window, text= "Copy TV32_320", command = auto_build_bin_file.TV_32_Panel_320_copy)

btnTV40_JP_copy = ttk.Button(window, text= "Copy TV40_JP", command = auto_build_bin_file.TV_40_JP_copy)
btnTV40_HL_copy_pana = ttk.Button(window, text= "Copy TV40_HL pana", command = auto_build_bin_file.TV_40_HL_copy_pana)
btnTV32_JP_copy = ttk.Button(window, text= "Copy TV32_JP", command = auto_build_bin_file.TV_32_JP_copy)

btnTV50_JP_copy = ttk.Button(window, text= "Copy TV50_JP", command = auto_build_bin_file.TV_50_JP_copy)
btnTV50_JP_copy_pana = ttk.Button(window, text= "Copy TV50_JP pana", command = auto_build_bin_file.TV_50_JP_copy_pana)

btnTV50_JP_SQ5_copy = ttk.Button(window, text= "Copy TV50_JP_SQ5", command = auto_build_bin_file.TV_50_JP_SQ5_copy)

btnTV55_HL_copy = ttk.Button(window, text= "Copy TV55_HL", command = auto_build_bin_file.TV_55_HL_copy)
btnTV55_HL_copy_pana = ttk.Button(window, text= "Copy TV55_HL pana", command = auto_build_bin_file.TV_55_HL_copy_pana)
#################################################################################################################################
btnTV32_315_copy_pana = ttk.Button(window, text= "Copy TV32_315_pana", command = auto_build_bin_file.TV_32_Panel_315_copy_pana)

btnTV32_315_unpack = ttk.Button (window, text= "TV32_315 unpack", command = unpacked_scripts.unpacked_TV32_315)
btnTV32_320_unpack = ttk.Button (window, text= "TV32_320 unpack", command = unpacked_scripts.unpacked_TV32_320)
btnTV40_JP_unpack = ttk.Button (window, text= "TV40 JP unpack", command = unpacked_scripts.unpacked_TV40_JP)
btnTV40_HL_unpack_pana = ttk.Button (window, text= "TV40 HL unpack pana", command = unpacked_scripts.unpacked_TV40_HL_pana)
btnTV32_JP_unpack = ttk.Button (window, text= "TV32 JP unpack", command = unpacked_scripts.unpacked_TV32_JP)
btnTV50_JP_unpack = ttk.Button (window, text= "TV50 JP unpack", command = unpacked_scripts.unpacked_TV50_JP) 
btnTV50_JP_unpack_pana = ttk.Button (window, text= "TV50 JP unpack pana", command = unpacked_scripts.unpacked_TV50_JP_pana) 
btnTV50_JP_SQ5_unpack = ttk.Button (window, text= "TV50 JP SQ5 unpack", command = unpacked_scripts.unpacked_TV50_JP_SQ5) 
btnTV55_HL_unpack = ttk.Button (window, text= "TV55 HL unpack", command = unpacked_scripts.unpacked_TV55_HL) 
btnTV55_HL_unpack_pana = ttk.Button (window, text= "TV55 HL unpack pana", command = unpacked_scripts.unpacked_TV55_HL_pana) 
btnTV32_315_unpack_pana = ttk.Button (window, text= "TV32_315_pana unpack", command = unpacked_scripts.unpacked_TV32_315_pana)

content.grid(column= 0, row= 0, sticky= (N, S, E, W))
#frame.grid(column= 0, row= 0, columnspan= 3, rowspan= 2, sticky= (N, S, E, W))

lblTV32_315_HL.grid(column = LABEL_COLUMN, row= TV32_315_ROW_LABEL, columnspan= 2, sticky= (N, W), padx= 5)
lblTV32_320_HL.grid(column = LABEL_COLUMN, row= TV32_320_ROW_LABEL, columnspan= 2, sticky= (N, W), padx= 5)
lblTV40_JP.grid(column = LABEL_COLUMN, row= TV40_JP_ROW_LABEL, columnspan= 2, sticky= (N, W), padx= 5 )
lblTV40_HL_PANA.grid(column = LABEL_COLUMN, row= TV40_HL_ROW_LABEL_PANA, columnspan= 2, sticky= (N, W), padx= 5 )
lblTV32_JP.grid(column = LABEL_COLUMN, row= TV32_JP_ROW_LABEL, columnspan= 2, sticky= (N, W), padx= 5)
lblTV50_JP.grid(column = LABEL_COLUMN, row= TV50_JP_ROW_LABEL, columnspan= 2, sticky= (N, W), padx= 5 )
lblTV50_JP_PANA.grid(column = LABEL_COLUMN, row= TV50_JP_ROW_LABEL_PANA, columnspan= 2, sticky= (N, W), padx= 5 )
lblTV50_JP_SQ5.grid(column = LABEL_COLUMN, row= TV50_JP_SQ5_ROW_LABEL, columnspan= 2, sticky= (N, W), padx= 5 )
lblTV55_HL.grid(column = LABEL_COLUMN, row= TV55_HL_ROW_LABEL, columnspan= 2, sticky= (N, W), padx= 5 )
lblTV55_HL_PANA.grid(column = LABEL_COLUMN, row= TV55_HL_ROW_LABEL_PANA, columnspan= 2, sticky= (N, W), padx= 5 )
lblTV32_315_HL_PANA.grid(column = LABEL_COLUMN, row= TV32_315_ROW_LABEL_PANA, columnspan= 2, sticky= (N, W), padx= 5)

#name.grid(column= 3, row= 1, columnspan= 2, sticky= (N, E, W), pady= 5, padx= 5)
btnTV32_315.grid(column = BUTTON_COLUMN, row = TV32_315_ROW_BUTTON, sticky = (W))
btnTV32_320.grid(column = BUTTON_COLUMN, row = TV32_320_ROW_BUTTON, sticky = (W))
btnTV40_JP.grid(column = BUTTON_COLUMN, row = TV40_JP_ROW_BUTTON, sticky = (W))
btnTV40_HL_pana.grid(column = BUTTON_COLUMN, row = TV40_HL_ROW_BUTTON_PANA, sticky = (W))
btnTV32_JP.grid(column = BUTTON_COLUMN, row = TV32_JP_ROW_BUTTON, sticky = (W))
btnTV50_JP.grid(column = BUTTON_COLUMN, row = TV50_JP_ROW_BUTTON, sticky = (W))
btnTV50_JP_pana.grid(column = BUTTON_COLUMN, row = TV50_JP_ROW_BUTTON_PANA, sticky = (W))
btnTV50_JP_SQ5.grid(column = BUTTON_COLUMN, row = TV50_JP_SQ5_ROW_BUTTON, sticky = (W))
btnTV55_HL.grid(column = BUTTON_COLUMN, row = TV55_HL_ROW_BUTTON, sticky = (W))
btnTV55_HL_pana.grid(column = BUTTON_COLUMN, row = TV55_HL_ROW_BUTTON_PANA, sticky = (W))
btnTV32_315_pana.grid(column = BUTTON_COLUMN, row = TV32_315_ROW_BUTTON_PANA, sticky = (W))

#name.grid(column= 3, row= 1, columnspan= 2, sticky= (N, E, W), pady= 5, padx= 5)
btnTV32_315_copy.grid(column = BUTTON_COLUMN_COPY, row = TV32_315_ROW_BUTTON_COPY, sticky = (W))
btnTV32_320_copy.grid(column = BUTTON_COLUMN_COPY, row = TV32_320_ROW_BUTTON_COPY, sticky = (W))
btnTV40_JP_copy.grid(column = BUTTON_COLUMN_COPY, row = TV40_JP_ROW_BUTTON_COPY, sticky = (W))
btnTV40_HL_copy_pana.grid(column = BUTTON_COLUMN_COPY, row = TV40_HL_ROW_BUTTON_COPY_PANA, sticky = (W))
btnTV32_JP_copy.grid(column = BUTTON_COLUMN_COPY, row = TV32_JP_ROW_BUTTON_COPY, sticky = (W))
btnTV50_JP_copy.grid(column = BUTTON_COLUMN_COPY, row = TV50_JP_ROW_BUTTON_COPY, sticky = (W))
btnTV50_JP_copy_pana.grid(column = BUTTON_COLUMN_COPY, row = TV50_JP_ROW_BUTTON_COPY_PANA, sticky = (W))
btnTV50_JP_SQ5_copy.grid(column = BUTTON_COLUMN_COPY, row = TV50_JP_SQ5_ROW_BUTTON_COPY, sticky = (W))
btnTV55_HL_copy.grid(column = BUTTON_COLUMN_COPY, row = TV55_HL_ROW_BUTTON_COPY, sticky = (W))
btnTV55_HL_copy_pana.grid(column = BUTTON_COLUMN_COPY, row = TV55_HL_ROW_BUTTON_COPY_PANA, sticky = (W))
btnTV32_315_copy_pana.grid(column = BUTTON_COLUMN_COPY, row = TV32_315_ROW_BUTTON_COPY_PANA, sticky = (W))
#######################################################################################################
btnTV32_315_unpack.grid(column = BUTTON_UNPACK_COLUMN, row = TV32_315_ROW_BUTTON, sticky = (W))
btnTV32_320_unpack.grid(column = BUTTON_UNPACK_COLUMN, row = TV32_320_ROW_BUTTON, sticky = (W))
btnTV40_JP_unpack.grid(column = BUTTON_UNPACK_COLUMN, row = TV40_JP_ROW_BUTTON, sticky = (W))
btnTV40_HL_unpack_pana.grid(column = BUTTON_UNPACK_COLUMN, row = TV40_HL_ROW_BUTTON_PANA, sticky = (W))
btnTV32_JP_unpack.grid(column = BUTTON_UNPACK_COLUMN, row = TV32_JP_ROW_BUTTON, sticky = (W))
btnTV50_JP_unpack.grid(column = BUTTON_UNPACK_COLUMN, row = TV50_JP_ROW_BUTTON, sticky = (W))
btnTV50_JP_unpack_pana.grid(column = BUTTON_UNPACK_COLUMN, row = TV50_JP_ROW_BUTTON_PANA, sticky = (W))
btnTV50_JP_SQ5_unpack.grid(column = BUTTON_UNPACK_COLUMN, row = TV50_JP_SQ5_ROW_BUTTON, sticky = (W))
btnTV55_HL_unpack.grid(column = BUTTON_UNPACK_COLUMN, row = TV55_HL_ROW_BUTTON, sticky = (W))
btnTV55_HL_unpack_pana.grid(column = BUTTON_UNPACK_COLUMN, row = TV55_HL_ROW_BUTTON_PANA, sticky = (W))
btnTV32_315_unpack_pana.grid(column = BUTTON_UNPACK_COLUMN, row = TV32_315_ROW_BUTTON_PANA, sticky = (W))

window.mainloop()
