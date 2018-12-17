
import subprocess
import os.path
import glob

from Tkinter import *
#from Tkinter.ttk import Progressbar
import ttk

from utils.bin_built_scripts import auto_build_bin_file
from utils.unpacked_scripts import unpacked_scripts



num_of_rows = 23

TV32_315_ROW, \
TV32_315_ROW_PANA, \
TV32_320_ROW, \
TV32_320_ROW_PANA, \
TV32_JP_ROW, \
TV32_JP_ROW_PANA, \
TV40_JP_ROW, \
TV40_JP_ROW_REF59_PANA, \
TV40_HL_ROW_REF53, \
TV40_HL_ROW_REF53_PANA, \
TV40_JP_ROW_REF54, \
TV40_JP_ROW_REF54_PANA, \
TV40_JP_ROW_EK_REF59_PANA, \
TV40_JP_ROW_EK_REF59_UBC, \
TV40_HL_ROW_PANA, \
TV43_JP_ROW, \
TV43_JP_ROW_PANA, \
TV50_JP_ROW, \
TV50_JP_ROW_PANA, \
TV50_JP_SQ5_ROW, \
TV50_JP_SQ5_ROW_PANA, \
TV55_HL_ROW, \
TV55_HL_ROW_PANA = range(num_of_rows)


BUTTON_UNPACK_COLUMN = 0
LABEL_COLUMN = 1
BUTTON_COLUMN = 3
BUTTON_COLUMN_COPY = 4
##########################################################################################

auto_build_bin_file.test_import()
unpacked_scripts.test_import()

##########################################################################################
window = Tk() 	
style = ttk.Style()
style.configure('TButton', foreground = 'black', relief = 'sunken', padding = 5)
style.configure('TLabel', foreground = 'blue', padding = 10)
#style.configure('TProgressbar', foreground= 'red', padding= 10)
content = ttk.Frame(window, padding = (3,3,12,12))
content.grid(column = 0, row = 0, sticky = (N, S, E, W))

########################################################################################################
def TV(text_unpack, command_unpack, text_label, text_build, command_build, text_copy, command_copy, row):
    btn_unpack = ttk.Button (window, text= text_unpack, command = command_unpack)
    lbl = ttk.Label( window, text = text_label)
    btn_build = ttk.Button(window, text= text_build, command = command_build)
    btn_copy = ttk.Button(window, text= text_copy, command = command_copy)

    btn_unpack.grid(column = BUTTON_UNPACK_COLUMN, row = row, sticky = (W))
    lbl.grid(column = LABEL_COLUMN, row= row, columnspan= 2, sticky= (N, W), padx= 5)
    btn_build.grid(column = BUTTON_COLUMN, row = row, sticky = (W))
    btn_copy.grid(column = BUTTON_COLUMN_COPY, row = row, sticky = (W))


#####################################################################################
###### TV 32" panel315
###############################
TV( text_unpack         = "TV32_315 unpack", \
    command_unpack      = unpacked_scripts.unpacked_TV32_315, \
    text_label          = "TV32 panel 315 HL!", \
    text_build          = "TV32_315", \
    command_build       = auto_build_bin_file.TV_32_Panel_315, \
    text_copy           = "Copy TV32_315", \
    command_copy        = auto_build_bin_file.TV_32_Panel_315_copy, \
    row = TV32_315_ROW
    )

#####################################################################################
###### TV 32" panel315 pana logo
###############################
TV( text_unpack         = "TV32_315 unpack pana", \
    command_unpack      = unpacked_scripts.unpacked_TV32_315_pana, \
    text_label          = "TV32 panel 315 HL pana!", \
    text_build          = "TV32_315 pana", \
    command_build       = auto_build_bin_file.TV_32_Panel_315_pana, \
    text_copy           = "Copy TV32_315 pana", \
    command_copy        = auto_build_bin_file.TV_32_Panel_315_copy_pana, \
    row                 = TV32_315_ROW_PANA
    )

#####################################################################################
###### TV 32 in panel320
###############################
TV( text_unpack         = "TV32_320 unpack", \
    command_unpack      = unpacked_scripts.unpacked_TV32_320, \
    text_label          = "TV32 panel 320 HL!", \
    text_build          = "TV32_320", \
    command_build       = auto_build_bin_file.TV_32_Panel_320, \
    text_copy           = "Copy TV32_320", \
    command_copy        = auto_build_bin_file.TV_32_Panel_320_copy, \
    row                 = TV32_320_ROW
    )
#####################################################################################
###### TV 32 in panel320
###############################
TV( text_unpack         = "TV32_320 unpack PANA", \
    command_unpack      = unpacked_scripts.unpacked_TV32_320_pana, \
    text_label          = "TV32 panel 320 HL_pana!", \
    text_build          = "TV32_320 pana", \
    command_build       = auto_build_bin_file.TV_32_Panel_320_pana, \
    text_copy           = "Copy TV32_320 pana", \
    command_copy        = auto_build_bin_file.TV_32_Panel_320_copy_pana, \
    row                 = TV32_320_ROW_PANA
    )
#####################################################################################
###### TV 32 JP
###############################
TV( text_unpack         = "TV32_JP unpack", \
    command_unpack      = unpacked_scripts.unpacked_TV32_JP, \
    text_label          = "TV32 JP!", \
    text_build          = "TV32_JP", \
    command_build       = auto_build_bin_file.TV_32_JP, \
    text_copy           = "Copy TV32_JP", \
    command_copy        = auto_build_bin_file.TV_32_JP_copy, \
    row                 = TV32_JP_ROW
    )    
#####################################################################################
###### TV 32 JP PANA
###############################
TV( text_unpack         = "TV32_JP unpack PANA", \
    command_unpack      = unpacked_scripts.unpacked_TV32_JP_pana, \
    text_label          = "TV32 JP pana!", \
    text_build          = "TV32_JP pana", \
    command_build       = auto_build_bin_file.TV_32_JP_pana, \
    text_copy           = "Copy TV32_JP pana", \
    command_copy        = auto_build_bin_file.TV_32_JP_copy_pana, \
    row                 = TV32_JP_ROW_PANA
    )    
#####################################################################################
###### TV 40 JP
###############################
TV( text_unpack         = "TV40_JP unpack", \
    command_unpack      = unpacked_scripts.unpacked_TV40_JP, \
    text_label          = "TV40 JP!", \
    text_build          = "TV40_JP", \
    command_build       = auto_build_bin_file.TV_40_JP, \
    text_copy           = "Copy TV40_JP", \
    command_copy        = auto_build_bin_file.TV_40_JP_copy, \
    row                 = TV40_JP_ROW
    )
# #####################################################################################
# ###### TV 40 JP REF59 PANA
# ###############################
# TV( text_unpack         = "TV40_JP 59 PANA unpack", \
#     command_unpack      = unpacked_scripts.unpacked_TV40_JP_REF59_PANA, \
#     text_label          = "TV40 JP 59 PANA!", \
#     text_build          = "TV40_JP 59 PANA", \
#     command_build       = auto_build_bin_file.TV_40_JP_REF59_PANA, \
#     text_copy           = "Copy TV40_JP", \
#     command_copy        = auto_build_bin_file.TV_40_JP_REF59_PANA_copy, \
#     row                 = TV40_JP_ROW_REF59_PANA
#     )
#####################################################################################
###### TV 40 JP ref53
###############################
TV( text_unpack         = "TV40_JP ref53 unpack", \
    command_unpack      = unpacked_scripts.unpacked_TV40_JP_ref53, \
    text_label          = "TV40 JP ref53!", \
    text_build          = "TV40_JP ref53", \
    command_build       = auto_build_bin_file.TV_40_JP_ref53, \
    text_copy           = "Copy TV40_JP ref53", \
    command_copy        = auto_build_bin_file.TV_40_JP_ref53_copy, \
    row                 = TV40_HL_ROW_REF53
    ) 
#####################################################################################
###### TV 40 JP ref53 PANA
###############################
TV( text_unpack         = "TV40_JP ref53 unpack PANA", \
    command_unpack      = unpacked_scripts.unpacked_TV40_JP_ref53_pana, \
    text_label          = "TV40 JP ref53_pana!", \
    text_build          = "TV40_JP ref53_pana", \
    command_build       = auto_build_bin_file.TV_40_JP_ref53_pana, \
    text_copy           = "Copy TV40_JP ref53_pana", \
    command_copy        = auto_build_bin_file.TV_40_JP_ref53_copy_pana, \
    row                 = TV40_HL_ROW_REF53_PANA
    )       
#####################################################################################
###### TV 40 JP ref54
###############################
TV( text_unpack         = "TV40_JP DM ref54 unpack", \
    command_unpack      = unpacked_scripts.unpacked_TV40_JP_ref54, \
    text_label          = "TV40 JP DM ref54!", \
    text_build          = "TV40_JP DM ref54", \
    command_build       = auto_build_bin_file.TV_40_JP_ref54, \
    text_copy           = "Copy TV40_JP DM ref54", \
    command_copy        = auto_build_bin_file.TV_40_JP_ref54_copy, \
    row                 = TV40_JP_ROW_REF54
    )
#####################################################################################
###### TV 40 JP ref54 PANA
###############################
TV( text_unpack         = "TV40_JP DM ref54 unpack PANA", \
    command_unpack      = unpacked_scripts.unpacked_TV40_JP_ref54_pana, \
    text_label          = "TV40 JP DM ref54_pana!", \
    text_build          = "TV40_JP DM ref54_pana", \
    command_build       = auto_build_bin_file.TV_40_JP_ref54_pana, \
    text_copy           = "Copy TV40_JP DM ref54_pana", \
    command_copy        = auto_build_bin_file.TV_40_JP_ref54_copy_pana, \
    row                 = TV40_JP_ROW_REF54_PANA
    )  
#####################################################################################
###### TV 40 JP EK ref59
###############################
TV( text_unpack         = "TV40_JP EK unpack pana", \
    command_unpack      = unpacked_scripts.unpacked_TV40_JP_EK_ref59_pana, \
    text_label          = "TV40 JP EK pana!", \
    text_build          = "TV40_JP EK pana", \
    command_build       = auto_build_bin_file.TV_40_JP_EK_ref59_pana, \
    text_copy           = "Copy TV40_JP EK pana", \
    command_copy        = auto_build_bin_file.TV_40_JP_EK_ref59_pana_copy, \
    row                 = TV40_JP_ROW_EK_REF59_PANA
    )  
#####################################################################################
###### TV 40 JP EK ref59
###############################
TV( text_unpack         = "TV40_JP EK unpack ubc", \
    command_unpack      = unpacked_scripts.unpacked_TV40_JP_EK_ref59_ubc, \
    text_label          = "TV40 JP EK ubc!", \
    text_build          = "TV40_JP EK ubc", \
    command_build       = auto_build_bin_file.TV_40_JP_EK_ref59_ubc, \
    text_copy           = "Copy TV40_JP EK ubc", \
    command_copy        = auto_build_bin_file.TV_40_JP_EK_ref59_ubc_copy, \
    row                 = TV40_JP_ROW_EK_REF59_UBC
    )        
# #####################################################################################
# ###### TV 40 HL pana
# ###############################
# TV( text_unpack         = "TV40_HL unpack pana", \
#     command_unpack      = unpacked_scripts.unpacked_TV40_HL_pana, \
#     text_label          = "TV40 HL pana !", \
#     text_build          = "TV40_HL_pana", \
#     command_build       = auto_build_bin_file.TV_40_HL_pana, \
#     text_copy           = "Copy TV40_HL pana", \
#     command_copy        = auto_build_bin_file.TV_40_HL_copy_pana, \
#     row                 = TV40_HL_ROW_PANA
#     )
#####################################################################################
###### TV 43 JP 
###############################
TV( text_unpack         = "TV43_JP unpack", \
    command_unpack      = unpacked_scripts.unpacked_TV43_JP, \
    text_label          = "TV43 JP ref57!", \
    text_build          = "TV43_JP ref57", \
    command_build       = auto_build_bin_file.TV_43_JP, \
    text_copy           = "Copy TV43_JP ref57", \
    command_copy        = auto_build_bin_file.TV_43_JP_copy, \
    row                 = TV43_JP_ROW
    )
#####################################################################################
###### TV 43 JP 
###############################
TV( text_unpack         = "TV43_JP unpack PANA", \
    command_unpack      = unpacked_scripts.unpacked_TV43_JP_pana, \
    text_label          = "TV43 JP ref57_pana!", \
    text_build          = "TV43_JP ref57_pana", \
    command_build       = auto_build_bin_file.TV_43_JP_pana, \
    text_copy           = "Copy TV43_JP ref57_pana", \
    command_copy        = auto_build_bin_file.TV_43_JP_copy_pana, \
    row                 = TV43_JP_ROW_PANA
    )               
#####################################################################################
###### TV 50 JP
###############################
TV( text_unpack         = "TV50_JP unpack", \
    command_unpack      = unpacked_scripts.unpacked_TV50_JP, \
    text_label          = "TV50 JP!", \
    text_build          = "TV50_JP", \
    command_build       = auto_build_bin_file.TV_50_JP, \
    text_copy           = "Copy TV50_JP", \
    command_copy        = auto_build_bin_file.TV_50_JP_copy, \
    row                 = TV50_JP_ROW
    )
# #####################################################################################
# ###### TV 50 JP pana
# ###############################
# TV( text_unpack         = "TV50_JP unpack pana", \
#     command_unpack      = unpacked_scripts.unpacked_TV50_JP_pana, \
#     text_label          = "TV50 JP pana!", \
#     text_build          = "TV50_JP pana", \
#     command_build       = auto_build_bin_file.TV_50_JP_pana, \
#     text_copy           = "Copy TV50_JP pana", \
#     command_copy        = auto_build_bin_file.TV_50_JP_copy_pana, \
#     row                 = TV50_JP_ROW_PANA
#     )   

#####################################################################################
###### TV 50 JP SQ5
###############################
TV( text_unpack         = "TV50_JP unpack sq5", \
    command_unpack      = unpacked_scripts.unpacked_TV50_JP_SQ5, \
    text_label          = "TV50 JP SQ5!", \
    text_build          = "TV50_JP SQ5", \
    command_build       = auto_build_bin_file.TV_50_JP_SQ5, \
    text_copy           = "Copy TV50_JP SQ5", \
    command_copy        = auto_build_bin_file.TV_50_JP_SQ5_copy, \
    row                 = TV50_JP_SQ5_ROW
    ) 
# #####################################################################################
# ###### TV 50 JP SQ5 pana
# ###############################
# TV( text_unpack         = "TV50_JP unpack sq5 pana", \
#     command_unpack      = unpacked_scripts.unpacked_TV50_JP_SQ5_pana, \
#     text_label          = "TV50 JP SQ5 pana!", \
#     text_build          = "TV50_JP SQ5 pana", \
#     command_build       = auto_build_bin_file.TV_50_JP_SQ5_pana, \
#     text_copy           = "Copy TV50_JP SQ5 pana", \
#     command_copy        = auto_build_bin_file.TV_50_JP_SQ5_copy_pana, \
#     row                 = TV50_JP_SQ5_ROW_PANA
#     )


#####################################################################################
###### TV 55 HL
###############################
TV( text_unpack         = "TV55_HL unpack", \
    command_unpack      = unpacked_scripts.unpacked_TV55_HL, \
    text_label          = "TV55 HL!", \
    text_build          = "TV55_HL", \
    command_build       = auto_build_bin_file.TV_55_HL, \
    text_copy           = "Copy TV55_HL", \
    command_copy        = auto_build_bin_file.TV_55_HL_copy, \
    row                 = TV55_HL_ROW
    )
#####################################################################################
###### TV 55 HL pana
###############################
TV( text_unpack         = "TV55_HL unpack pana", \
    command_unpack      = unpacked_scripts.unpacked_TV55_HL_pana, \
    text_label          = "TV55 HL pana !", \
    text_build          = "TV55_HL_pana", \
    command_build       = auto_build_bin_file.TV_55_HL_pana, \
    text_copy           = "Copy TV55_HL pana", \
    command_copy        = auto_build_bin_file.TV_55_HL_copy_pana, \
    row                 = TV55_HL_ROW_PANA
    )    

window.mainloop()
