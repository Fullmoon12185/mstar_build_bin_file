from Tkinter import *
import ttk
from utils.bin_built_scripts import auto_build_bin_file
from utils.unpacked_scripts import unpacked_scripts
from glob import glob
import os


SUPPLIER_PATH = '.\..\Database\Suppliers\\'
APKS_PATH = '.\..\Database\Apks\\'

configurations = []
num_of_rows = 5

CONFIGURATION, \
UNPACK, \
COPY_UBC_FILES, \
COPY_PANA_FILES, \
PACK = range (num_of_rows)

num_of_column = 10

COLUMN_SUPPLIERS, \
COLUMN_SIZE, \
COLUMN_PANEL, \
COLUMN_LOGO, \
COLUMN_BOOT_ANIMATION, \
COLUMN_FEATURE_1, \
COLUMN_FEATURE_2, \
COLUMN_SYSTEM_APK, \
COLUMN_USER_APK, \
COLUMN_BUTTON = range (num_of_column)

ROW_SPAN = 10

if __name__ == '__main__':
    root = Tk()
    style = ttk.Style()
    root.title('Building firmware for UBC LOGO')
    # root.geometry("350x300") #You want the size of the app to be 500x500
    #root.resizable(0, 0) #Don't allow resizing in the x or y direction
    #configuration = Checkbar(root, ['Unpack', 'UBC', 'PACK'])
    #tgl = Checkbar(root, ['TV40EK','TV40DM','TV43DM', 'TV50PE5', 'TV50SQ8', 'TV55'])
    #configuration.pack(side=TOP,  fill=X)
    #tgl.pack(side=LEFT)
    #configuration.config(relief=GROOVE, bd=2)

    # Create and grid the outer content frame
    ttkFrameRoot = ttk.Frame(root, padding=(5, 5, 12, 0))
    ttkFrameRoot.grid(column=0, row=0, sticky=(N,W,E,S))
    ttkFrameRoot.grid_columnconfigure(0, weight=1)
    ttkFrameRoot.grid_rowconfigure(5, weight=1)
    
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0,weight=1)
    
    

    tupleOfSuppliers = tuple(os.listdir('.\..\Database\Suppliers'))
    tupleOfSizes = tuple(os.listdir('.\..\Database\Suppliers\CVT'))
    tupleOfPanels = tuple(os.listdir('.\..\Database\Suppliers\CVT\TV32'))
    tupleOfLogos = tuple(os.listdir('.\..\Database\Suppliers\CVT\TV32\JP_801_Ref_300'))
    tupleOfBootAnimation = tuple(os.listdir('.\..\Database\BootAnimation'))
    tupleOfFeatuer_1 = tuple(os.listdir('.\..\Database\Feature1'))
    tupleOfSystemApks = tuple(os.listdir('.\..\Database\APKs\commonSystemAPKs'))
    tupleOfUserApks = tuple(os.listdir('.\..\Database\APKs\commonUserApks'))
    
    
    

    stringTupleOfSuppliers = StringVar(value=tupleOfSuppliers)
    lboxListOfSuppliers = Listbox(ttkFrameRoot, listvariable=stringTupleOfSuppliers, height=20, exportselection=0)
    lboxListOfSuppliers.grid(column=COLUMN_SUPPLIERS, row=1, rowspan=ROW_SPAN, sticky=(N,S,E,W))
    
    lblListOfSuppliers = ttk.Label(ttkFrameRoot, text="SUPPLIER")
    lblListOfSuppliers.grid(column=COLUMN_SUPPLIERS, row=0, padx=10, pady=5)
    for i in range(0,len(tupleOfSuppliers),2):
        lboxListOfSuppliers.itemconfigure(i, background='#f0f0ff')
    

    lblBinFile1 = ttk.Label(ttkFrameRoot, text="BinFile")
    lblBinFile1.grid(column=COLUMN_SUPPLIERS, row=ROW_SPAN + 1)

    lblVariableBinFile = StringVar()
    lblBinFile = ttk.Label(ttkFrameRoot, text="BinFile", textvariable = lblVariableBinFile)
    lblBinFile.grid(column=COLUMN_SIZE, row=ROW_SPAN + 1, columnspan = 3, sticky = W)

    lblProgress1 = ttk.Label(ttkFrameRoot, text="In Progress")
    lblProgress1.grid(column=COLUMN_SUPPLIERS, row=ROW_SPAN + 2)

    lblVariableInProgress = StringVar()
    lblInProgress = ttk.Label(ttkFrameRoot, textvariable = lblVariableInProgress)
    lblInProgress.grid(column=COLUMN_SIZE, row=ROW_SPAN + 2, columnspan = 3, sticky = W)
###############################################################################################
    stringTupleOfSizes = StringVar(value=tupleOfSizes)
    lboxListOfSizes = Listbox(ttkFrameRoot, listvariable=stringTupleOfSizes, height=5, exportselection=0)
    lboxListOfSizes.grid(column=COLUMN_SIZE, row=1, rowspan=ROW_SPAN, sticky=(N,S,E,W))
    
    lblListOfSizes = ttk.Label(ttkFrameRoot, text="SIZE")
    lblListOfSizes.grid(column=COLUMN_SIZE, row=0, padx=10, pady=5)
    for i in range(0,len(tupleOfSizes),2):
        lboxListOfSizes.itemconfigure(i, background='#f0f0ff')
###############################################################################################

    stringTupleOfPanels = StringVar(value=tupleOfPanels)
    lboxListOfPanels = Listbox(ttkFrameRoot, listvariable=stringTupleOfPanels, height=5, exportselection=0)
    lboxListOfPanels.grid(column=COLUMN_PANEL, row=1, rowspan=ROW_SPAN, sticky=(N,S,E,W))
    
    lblListOfPanels = ttk.Label(ttkFrameRoot, text="PANEL")
    lblListOfPanels.grid(column=COLUMN_PANEL, row=0, padx=10, pady=5)
    for i in range(0,len(tupleOfPanels),2):
        lboxListOfPanels.itemconfigure(i, background='#f0f0ff')
###############################################################################################
    stringTupleOfLogos = StringVar(value=tupleOfLogos)
    lboxListOfLogos = Listbox(ttkFrameRoot, listvariable=stringTupleOfLogos, height=5, exportselection=0)
    lboxListOfLogos.grid(column=COLUMN_LOGO, row=1, rowspan=ROW_SPAN, sticky=(N,S,E,W))
    
    lblListOfLogos = ttk.Label(ttkFrameRoot, text="LOGO")
    lblListOfLogos.grid(column=COLUMN_LOGO, row=0, padx=10, pady=5)
    for i in range(0,len(tupleOfLogos),2):
        lboxListOfLogos.itemconfigure(i, background='#f0f0ff')
###############################################################################################
    stringTupleOfFeature_1 = StringVar(value=tupleOfFeatuer_1)
    lboxListOfFeature_1 = Listbox(ttkFrameRoot, listvariable=stringTupleOfFeature_1, height=5, exportselection=0)
    lboxListOfFeature_1.grid(column=COLUMN_FEATURE_1, row=1, rowspan=ROW_SPAN, sticky=(N,S,E,W))

    lblListOfFeature_1 = ttk.Label(ttkFrameRoot, text="FEATURE 1")
    lblListOfFeature_1.grid(column=COLUMN_FEATURE_1, row=0, padx=10, pady=5)
    for i in range(0,len(tupleOfFeatuer_1),2):
        lboxListOfFeature_1.itemconfigure(i, background='#f0f0ff')

###############################################################################################
    stringTupleOfBootAnimation = StringVar(value=tupleOfBootAnimation)
    lboxListOfBootAnimation = Listbox(ttkFrameRoot, listvariable=stringTupleOfBootAnimation, height=5, exportselection=0)
    lboxListOfBootAnimation.grid(column=COLUMN_BOOT_ANIMATION, row=1, rowspan=ROW_SPAN, sticky=(N,S,E,W))

    lblListOfBootAnimation = ttk.Label(ttkFrameRoot, text="BOOT ANIMATION")
    lblListOfBootAnimation.grid(column=COLUMN_BOOT_ANIMATION, row=0, padx=10, pady=5)


    for i in range(0,len(tupleOfBootAnimation),2):
        lboxListOfBootAnimation.itemconfigure(i, background='#f0f0ff')    
###############################################################################################
    stringTupleOfBootAnimation = StringVar(value=tupleOfBootAnimation)
    lboxListOfBootAnimation = Listbox(ttkFrameRoot, listvariable=stringTupleOfBootAnimation, height=5, exportselection=0)
    lboxListOfBootAnimation.grid(column=COLUMN_BOOT_ANIMATION, row=1, rowspan=ROW_SPAN, sticky=(N,S,E,W))

    lblListOfBootAnimation = ttk.Label(ttkFrameRoot, text="BOOT ANIMATION")
    lblListOfBootAnimation.grid(column=COLUMN_BOOT_ANIMATION, row=0, padx=10, pady=5)


    for i in range(0,len(tupleOfBootAnimation),2):
        lboxListOfBootAnimation.itemconfigure(i, background='#f0f0ff') 

###############################################################################################
    stringTupleOfSystemApks = StringVar(value=tupleOfSystemApks)
    lboxListOfSystemApks = Listbox(ttkFrameRoot, listvariable=stringTupleOfSystemApks, height=5, exportselection=0)
    lboxListOfSystemApks.grid(column=COLUMN_SYSTEM_APK, row=1, rowspan=ROW_SPAN, sticky=(N,S,E,W))

    lblListOfSystemApks = ttk.Label(ttkFrameRoot, text="SYSTEM APK")
    lblListOfSystemApks.grid(column=COLUMN_SYSTEM_APK, row=0, padx=10, pady=5)


    for i in range(0,len(tupleOfSystemApks),2):
        lboxListOfSystemApks.itemconfigure(i, background='#f0f0ff') 
###############################################################################################
    stringTupleOfUserApks = StringVar(value=tupleOfUserApks)
    lboxListOfUserApks = Listbox(ttkFrameRoot, listvariable=stringTupleOfUserApks, height=5, exportselection=0)
    lboxListOfUserApks.grid(column=COLUMN_USER_APK, row=1, rowspan=ROW_SPAN, sticky=(N,S,E,W))

    lblListOfUserApks = ttk.Label(ttkFrameRoot, text="User APK")
    lblListOfUserApks.grid(column=COLUMN_USER_APK, row=0, padx=10, pady=5)


    for i in range(0,len(tupleOfSystemApks),2):
        lboxListOfUserApks.itemconfigure(i, background='#f0f0ff')
################################################################################################
################################################################################################
    def Delete_a_List(list):
        list.delete(0, END)
        pass
    def Insert_a_Lists(list, list_of_str):
        for item in list_of_str:
            list.insert(END, item)
    def Insert_an_Item(list, item):
        list.insert(END, item)
################################################################################################
################################################################################################
    def Action_For_List_Of_Suppliers(*args):
        print(lboxListOfSuppliers.get(lboxListOfSuppliers.curselection()))
        str = SUPPLIER_PATH + lboxListOfSuppliers.get(lboxListOfSuppliers.curselection())
        Delete_a_List(lboxListOfSizes)
        Insert_a_Lists(lboxListOfSizes, os.listdir(str))
    
    def Action_For_List_Of_Sizes(*args):
        print(lboxListOfSizes.get(lboxListOfSizes.curselection()))
        str = SUPPLIER_PATH + lboxListOfSuppliers.get(lboxListOfSuppliers.curselection()) + '\\' + lboxListOfSizes.get(lboxListOfSizes.curselection())
        print(str)
        Delete_a_List(lboxListOfPanels)
        Insert_a_Lists(lboxListOfPanels, os.listdir(str))
    def Action_For_List_Of_Panels(*args):
        print(lboxListOfPanels.get(lboxListOfPanels.curselection()))
        str = SUPPLIER_PATH + lboxListOfSuppliers.get(lboxListOfSuppliers.curselection()) + '\\' + lboxListOfSizes.get(lboxListOfSizes.curselection()) + '\\' + lboxListOfPanels.get(lboxListOfPanels.curselection())
        print(str)
        Delete_a_List(lboxListOfLogos)
        Insert_a_Lists(lboxListOfLogos, os.listdir(str))
    def Action_For_List_Of_Logos(*args):
        print(lboxListOfLogos.get(lboxListOfLogos.curselection()))
        temp_path = SUPPLIER_PATH + lboxListOfSuppliers.get(lboxListOfSuppliers.curselection()) + '\\' + lboxListOfSizes.get(lboxListOfSizes.curselection()) + '\\' + lboxListOfPanels.get(lboxListOfPanels.curselection()) + '\\' + lboxListOfLogos.get(lboxListOfLogos.curselection())
        lblVariableBinFile.set(os.listdir(temp_path))
        # str = SUPPLIER_PATH + lboxListOfSuppliers.get(lboxListOfSuppliers.curselection()) + '\\' + lboxListOfSuppliers.get(lboxListOfSuppliers.curselection()) + '\\' + lboxListOfPanels.get(lboxListOfPanels.curselection())
        # print(str)
        # Delete_a_List(lboxListOfPanels)
        # Insert_a_Lists(lboxListOfPanels, os.listdir(str))
        pass
    def Action_For_List_Of_Feature_1(*args):
        print(lboxListOfFeature_1.get(lboxListOfFeature_1.curselection()))
        strLaunchers = APKS_PATH + 'Launchers\\' + lboxListOfBootAnimation.get(lboxListOfBootAnimation.curselection()) + '\\' +  lboxListOfFeature_1.get(lboxListOfFeature_1.curselection())
        # str = SUPPLIER_PATH + lboxListOfSuppliers.get(lboxListOfSuppliers.curselection()) + '\\' + lboxListOfSuppliers.get(lboxListOfSuppliers.curselection()) + '\\' + lboxListOfPanels.get(lboxListOfPanels.curselection())
        # print(str)
        Delete_a_List(lboxListOfSystemApks)
        Insert_a_Lists(lboxListOfSystemApks, os.listdir('.\..\Database\APKs\commonSystemAPKs'))
        for item in os.listdir(strLaunchers):
            Insert_an_Item(lboxListOfSystemApks,  item)

        pass
    def Action_For_List_Of_BootAnimation(*args):
        print(lboxListOfBootAnimation.get(lboxListOfBootAnimation.curselection()))
        str = APKS_PATH + 'Launchers\\' + lboxListOfBootAnimation.get(lboxListOfBootAnimation.curselection())
        # print(str)
        Delete_a_List(lboxListOfFeature_1)
        Insert_a_Lists(lboxListOfFeature_1, os.listdir(str))
        pass
        
    
    
    lboxListOfSuppliers.bind('<<ListboxSelect>>', Action_For_List_Of_Suppliers)
    lboxListOfSizes.bind('<<ListboxSelect>>', Action_For_List_Of_Sizes)
    lboxListOfPanels.bind('<<ListboxSelect>>', Action_For_List_Of_Panels)
    lboxListOfLogos.bind('<<ListboxSelect>>', Action_For_List_Of_Logos)
    lboxListOfFeature_1.bind('<<ListboxSelect>>', Action_For_List_Of_Feature_1)
    lboxListOfBootAnimation.bind('<<ListboxSelect>>', Action_For_List_Of_BootAnimation)



    
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
    
##########################################################################################    
    def Unpack_Bin_File():
        print('Run unpack...!')
        bin_file_path = SUPPLIER_PATH + lboxListOfSuppliers.get(lboxListOfSuppliers.curselection()) + '\\' + lboxListOfSizes.get(lboxListOfSizes.curselection()) + '\\' + lboxListOfPanels.get(lboxListOfPanels.curselection()) + '\\' + lboxListOfLogos.get(lboxListOfLogos.curselection())
        # bin_file_path = os.listdir(temp_path)
        print(bin_file_path)
        unpacked_scripts.Unpack_Bin_File(binpath = bin_file_path)
        # if("TV_32_JP_801" in TVs[radioTVType.get()]):
        #     unpacked_scripts.unpacked_TV32_JP(bin_file_path)
        # if("TV_32_JP_802_LSC" in TVs[radioTVType.get()]):
        #     unpacked_scripts.unpacked_TV32_JP_802_LSC()
        # if("TV_32_JP_802_315" in TVs[radioTVType.get()]):
        #     unpacked_scripts.unpacked_TV32_JP_802_315()
        # elif("TV_40_DM" in TVs[radioTVType.get()]):
        #     unpacked_scripts.unpacked_TV40_JP_ref54()
        # elif("TV_40_EK" in TVs[radioTVType.get()]):
        #     unpacked_scripts.unpacked_TV40_JP_EK_ref59_ubc()
        # elif("TV_43_DM" in TVs[radioTVType.get()]):
        #     unpacked_scripts.unpacked_TV43_JP()        
##########################################################################################            
    def Pack_Bin_File():
        print('Run pack...!')
       

    
    
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
    def Start_Build_Bin_File(): 
        print('Start_Unpack_Bin_File')
        lblVariableInProgress.set('Start_Unpack_Bin_File')
        Unpack_Bin_File()
        print('Start_Build_Bin_File')
        lblVariableInProgress.set('Start_Build_Bin_File')
        # Pack_Bin_File()
        # COLUMN_BUTTON
    ttkButtonBuildBinFile = ttk.Button(ttkFrameRoot, text='BUILD', command=Start_Build_Bin_File, default='active')
    ttkButtonBuildBinFile.grid(column=4, row=ROW_SPAN + 2, padx=10, pady=5)
    ttkButtonQuit = ttk.Button(ttkFrameRoot, text='QUIT', command=root.quit, default = 'active')
    ttkButtonQuit.grid(column=5, row=ROW_SPAN + 2, padx=10, pady=5)

    root.mainloop()