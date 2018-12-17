from Tkinter import *
import ttk
from utils.bin_built_scripts import auto_build_bin_file
from utils.unpacked_scripts import unpacked_scripts
from glob import glob
import os

configurations = []
num_of_rows = 5

CONFIGURATION, \
UNPACK, \
COPY_UBC_FILES, \
COPY_PANA_FILES, \
PACK = range (num_of_rows)

FIRST_COLUMN = 1
SECOND_COLUMN = 2
THIRD_COLUMN = 3


class Checkbar(Frame):
   def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
      Frame.__init__(self, parent)
      self.vars = []
      for pick in picks:
         var = IntVar()
         chk = ttk.Checkbutton(self, text=pick, variable=var)
         chk.pack(side=side, anchor=anchor, expand=YES)
         self.vars.append(var)
   def state(self):
      return map((lambda var: var.get()), self.vars)



if __name__ == '__main__':
    root = Tk()
    style = ttk.Style()
    root.title('Building firmware for UBC LOGO')
    root.geometry("350x300") #You want the size of the app to be 500x500
    #root.resizable(0, 0) #Don't allow resizing in the x or y direction
    #configuration = Checkbar(root, ['Unpack', 'UBC', 'PACK'])
    #tgl = Checkbar(root, ['TV40EK','TV40DM','TV43DM', 'TV50PE5', 'TV50SQ8', 'TV55'])
    #configuration.pack(side=TOP,  fill=X)
    #tgl.pack(side=LEFT)
    #configuration.config(relief=GROOVE, bd=2)

    # Create and grid the outer content frame
    listPanelsFrame = ttk.Frame(root, padding=(5, 5, 12, 0))
    listPanelsFrame.grid(column=0, row=0, sticky=(N,W,E,S))
    listPanelsFrame.grid_columnconfigure(0, weight=1)
    listPanelsFrame.grid_rowconfigure(5, weight=1)
    
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0,weight=1)
    


    tupleOfPanels = tuple(os.listdir('.\..\OriginalBinFiles'))
    tupleOfOptions = ('Voice', 'No Voice')
    tupleOfLogos = ('UBC', 'Sanco')





    stringTupleOfPanels = StringVar(value=tupleOfPanels)
    lboxListOfPanels = Listbox(listPanelsFrame, listvariable=stringTupleOfPanels, height=5, exportselection=0)
    lboxListOfPanels.grid(column=0, row=1, rowspan=6, sticky=(N,S,E,W))
    
    lblListOfPanels = ttk.Label(listPanelsFrame, text="List of Panels")
    lblListOfPanels.grid(column=0, row=0, padx=10, pady=5)
    for i in range(0,len(tupleOfPanels),2):
        lboxListOfPanels.itemconfigure(i, background='#f0f0ff')
###############################################################################################
    stringTupleOfOptions = StringVar(value=tupleOfOptions)
    lboxListOfOptions = Listbox(listPanelsFrame, listvariable=stringTupleOfOptions, height=5, exportselection=0)
    lboxListOfOptions.grid(column=1, row=1, rowspan=6, sticky=(N,S,E,W))

    lblListOfOptions = ttk.Label(listPanelsFrame, text="List of Options")
    lblListOfOptions.grid(column=1, row=0, padx=10, pady=5)
    for i in range(0,len(tupleOfOptions),2):
        lboxListOfOptions.itemconfigure(i, background='#f0f0ff')

###############################################################################################
    stringTupleOfLogos = StringVar(value=tupleOfLogos)
    lboxListOfLogos = Listbox(listPanelsFrame, listvariable=stringTupleOfLogos, height=5, exportselection=0)
    lboxListOfLogos.grid(column=2, row=1, rowspan=6, sticky=(N,S,E,W))

    lblListOfLogos = ttk.Label(listPanelsFrame, text="List of Logos")
    lblListOfLogos.grid(column=2, row=0, padx=10, pady=5)


    for i in range(0,len(tupleOfLogos),2):
        lboxListOfLogos.itemconfigure(i, background='#f0f0ff')    

    def showOptions(*args):
        print(lboxListOfPanels.curselection())
        print(lboxListOfOptions.curselection())
        print(lboxListOfLogos.curselection())

    lboxListOfPanels.bind('<<ListboxSelect>>', showOptions)
    lboxListOfOptions.bind('<<ListboxSelect>>', showOptions)
    lboxListOfLogos.bind('<<ListboxSelect>>', showOptions)
    # Grid all the widgets

    
    
    
    # g1.grid(column=1, row=1, sticky=W, padx=20)
    # g2.grid(column=1, row=2, sticky=W, padx=20)
    # g3.grid(column=1, row=3, sticky=W, padx=20)
    # send.grid(column=2, row=4, sticky=E)
    # sentlbl.grid(column=1, row=5, columnspan=2, sticky=N, pady=5, padx=5)
    # status.grid(column=0, row=6, columnspan=2, sticky=(W,E))
    
    # Set event bindings for when the selection in the listbox changes,
    # when the user double clicks the list, and when they hit the Return key
    # lbox.bind('<<ListboxSelect>>', showPopulation)
    # lbox.bind('<Double-1>', sendGift)
    # root.bind('<Return>', sendGift)

    # Colorize alternating lines of the listbox
   

    

#     TVs = [
#         ("TV_32_JP_801"),
#         ("TV_32_JP_802_LSC"),
#         ("TV_32_JP_802_315"),
#         ("TV_40_DM"),
#         ("TV_40_EK"),
#         ("TV_43_DM")
#     ]

#     def ShowChoice():
#         print(TVs[radioTVType.get()])

#     Label(root, text="""""", justify = LEFT, padx = 20).pack(anchor=W)
#     Label(root, text="""CHOOSE TV TYPE""", justify = LEFT, padx = 20).pack(anchor=W)

#     for val, TV in enumerate(TVs):
#         Radiobutton(root, 
#                     text = TV,
#                     padx = 20, 
#                     variable = radioTVType, 
#                     command = ShowChoice,
#                     value = val).pack(anchor=W)
    
# ##########################################################################################    
#     def Unpack_Bin_File():
#         print('Hello' + TVs[radioTVType.get()])
#         print('Run unpack...!')
#         if("TV_32_JP_801" in TVs[radioTVType.get()]):
#             unpacked_scripts.unpacked_TV32_JP()
#         if("TV_32_JP_802_LSC" in TVs[radioTVType.get()]):
#             unpacked_scripts.unpacked_TV32_JP_802_LSC()
#         if("TV_32_JP_802_315" in TVs[radioTVType.get()]):
#             unpacked_scripts.unpacked_TV32_JP_802_315()
#         elif("TV_40_DM" in TVs[radioTVType.get()]):
#             unpacked_scripts.unpacked_TV40_JP_ref54()
#         elif("TV_40_EK" in TVs[radioTVType.get()]):
#             unpacked_scripts.unpacked_TV40_JP_EK_ref59_ubc()
#         elif("TV_43_DM" in TVs[radioTVType.get()]):
#             unpacked_scripts.unpacked_TV43_JP()        
# ##########################################################################################            
#     def Pack_Bin_File():
#         print('Hello' + TVs[radioTVType.get()])
#         print('Run pack...!')
#         temp_voice_option = VoiceOption[radioVoiceOption.get()]
#         if("TV_32_JP_801" in TVs[radioTVType.get()]):
#             auto_build_bin_file.TV_32_JP(temp_voice_option)
#         if("TV_32_JP_802_LSC" in TVs[radioTVType.get()]):
#             auto_build_bin_file.TV_32_JP_802_LSC(temp_voice_option)
#         if("TV_32_JP_802_315" in TVs[radioTVType.get()]):
#             auto_build_bin_file.TV_32_JP_802_315(temp_voice_option)
#         elif("TV_40_DM" in TVs[radioTVType.get()]):
#             auto_build_bin_file.TV_40_JP_ref54(temp_voice_option)
#         elif("TV_40_EK" in TVs[radioTVType.get()]):
#             auto_build_bin_file.TV_40_JP_EK_ref59_ubc(temp_voice_option)
#         elif("TV_43_DM" in TVs[radioTVType.get()]):
#             auto_build_bin_file.TV_43_JP(temp_voice_option)     

    
    
# ##########################################################################################           
# ##########################################################################################            
#     def Start_Build_Bin_File(): 
#         if(radioOperation.get() == 0): #unpack option
#             Unpack_Bin_File()
#         elif (radioOperation.get() == 1): #pack option
#             Pack_Bin_File()
        

#     ttk.Button(root, text='Quit', command=root.quit).pack(side=RIGHT)
#     ttk.Button(root, text='Build', command=Start_Build_Bin_File).pack(side=RIGHT)
#     #ttk.Button(root, text='BUILD', command=root.quit).grid(row = num_of_rows + 1, sticky=W, pady=4)
#     #ttk.Button(root, text='COPY', command=allstates).grid(column = SECOND_COLUMN, row = num_of_rows + 1, sticky=W, pady=4)

    root.mainloop()