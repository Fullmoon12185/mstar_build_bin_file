import os
import subprocess

from Tkinter import *
import ttk
from utils.bin_built_scripts import auto_build_bin_file
from utils.unpacked_scripts import unpacked_scripts
from glob import glob

import tkMessageBox

 



SUPPLIER_PATH = '.\..\Database\Suppliers\\'
APKS_PATH = '.\..\Database\Apks\\'

configurations = []
num_of_rows = 5

CONFIGURATION, \
UNPACK, \
COPY_UBC_FILES, \
COPY_PANA_FILES, \
PACK = range (num_of_rows)

num_of_column = 14

COLUMN_SUPPLIERS, \
COLUMN_CHIPSET, \
COLUMN_BOARD, \
COLUMN_SIZE, \
COLUMN_PANEL, \
COLUMN_CURRENT,\
COLUMN_LOGO, \
COLUMN_BOOT_ANIMATION, \
COLUMN_LAUNCHER, \
COLUMN_FEATURE_1, \
COLUMN_FEATURE_2, \
COLUMN_SYSTEM_APK, \
COLUMN_USER_APK, \
COLUMN_BUTTON = range (num_of_column)

SAVING_BIN_FILE_PATH = num_of_column



ROW_SPAN = 5

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
    
    relativePath_Apks = '.\\..\\Database\\APKs\\'
    relativePath_BootAnimation = '.\\..\\Database\\BootAnimation\\'
    relativePath_SystemApks = '.\\..\\mstar-bin-tool\\MSTAR_Android\\temp\\system\\app\\'

    relativePath = '.\\..\\Database\\Suppliers\\'
    tupleOfSuppliers = tuple(os.listdir(relativePath))
    
    relativePath_Supplier =  relativePath + 'CVT\\'
    tupleOfChipsets = tuple(os.listdir(relativePath_Supplier))
    
    relativePath_Board =  relativePath_Supplier + '338\\'
    tupleOfBoards = tuple(os.listdir(relativePath_Board))
    
    relativePath_Size =  relativePath_Board + 'PB801\\'
    tupleOfSizes = tuple(os.listdir(relativePath_Size))
    
    relativePath_Panel =  relativePath_Size + 'TV32\\'
    tupleOfPanels = tuple(os.listdir(relativePath_Panel))
    
    relativePath_Current =  relativePath_Panel + 'ST315\\'    
    tupleOfCurrents = tuple(os.listdir(relativePath_Current))
    
    relativePath_Logo =  relativePath_Current + 'REF_300\\'    
    tupleOfLogos = tuple(os.listdir(relativePath_Logo))
    
    
    tupleOfBootAnimation = tuple(os.listdir(relativePath_BootAnimation))
    tupleOfLaunchers = tuple(os.listdir(relativePath_Apks + '\\Launchers\\338\UBC'))
    tupleOfSystemApks = tuple(os.listdir(relativePath_Apks + 'commonSystemAPKs'))
    tupleOfUserApks = tuple(os.listdir(relativePath_Apks + 'commonUserApks'))
    
    tupleOfFeatuer_1 = tuple(os.listdir('.\\..\\Database\\Feature1'))
    
    tupleOfSystemApksAfterExtracting = tuple(os.listdir(relativePath_SystemApks))
##########################################################################################    
    HIGHT_OF_LIST_BOX = 7



    stringTupleOfSuppliers = StringVar(value=tupleOfSuppliers)
    lboxListOfSuppliers = Listbox(ttkFrameRoot, listvariable=stringTupleOfSuppliers, height=HIGHT_OF_LIST_BOX, exportselection=0)
    lboxListOfSuppliers.grid(column=COLUMN_SUPPLIERS, row=1, rowspan=ROW_SPAN, sticky=(N,S,E,W))
    
    lblListOfSuppliers = ttk.Label(ttkFrameRoot, text="SUPPLIER")
    lblListOfSuppliers.grid(column=COLUMN_SUPPLIERS, row=0, padx=10, pady=5)
    for i in range(0,len(tupleOfSuppliers),2):
        lboxListOfSuppliers.itemconfigure(i, background='#f0f0ff')
    

    

###############################################################################################
    stringTupleOfChipsets = StringVar(value=tupleOfChipsets)
    lboxListOfChipsets = Listbox(ttkFrameRoot, listvariable=stringTupleOfChipsets, height=5, exportselection=0)
    lboxListOfChipsets.grid(column=COLUMN_CHIPSET, row=1, rowspan=ROW_SPAN, sticky=(N,S,E,W))
    
    lblListOfChipsets = ttk.Label(ttkFrameRoot, text="CHIPSET")
    lblListOfChipsets.grid(column=COLUMN_CHIPSET, row=0, padx=10, pady=5)
    for i in range(0,len(tupleOfChipsets),2):
        lboxListOfChipsets.itemconfigure(i, background='#f0f0ff')
###############################################################################################
    stringTupleOfBoards = StringVar(value=tupleOfBoards)
    lboxListOfBoards = Listbox(ttkFrameRoot, listvariable=stringTupleOfBoards, height=5, exportselection=0)
    lboxListOfBoards.grid(column=COLUMN_BOARD, row=1, rowspan=ROW_SPAN, sticky=(N,S,E,W))
    
    lblListOfBoards = ttk.Label(ttkFrameRoot, text="BOARD")
    lblListOfBoards.grid(column=COLUMN_BOARD, row=0, padx=10, pady=5)
    for i in range(0,len(tupleOfBoards),2):
        lboxListOfBoards.itemconfigure(i, background='#f0f0ff')        
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

    stringTupleOfCurrents = StringVar(value=tupleOfCurrents)
    lboxListOfCurrents = Listbox(ttkFrameRoot, listvariable=stringTupleOfCurrents, height=5, exportselection=0)
    lboxListOfCurrents.grid(column=COLUMN_CURRENT, row=1, rowspan=ROW_SPAN, sticky=(N,S,E,W))
    
    lblListOfCurrents = ttk.Label(ttkFrameRoot, text="CURRENT")
    lblListOfCurrents.grid(column=COLUMN_CURRENT, row=0, padx=10, pady=5)
    for i in range(0,len(tupleOfCurrents),2):
        lboxListOfCurrents.itemconfigure(i, background='#f0f0ff')
###############################################################################################
    stringTupleOfLogos = StringVar(value=tupleOfLogos)
    lboxListOfLogos = Listbox(ttkFrameRoot, listvariable=stringTupleOfLogos, height=5, exportselection=0)
    lboxListOfLogos.grid(column=COLUMN_LOGO, row=1, rowspan=ROW_SPAN, sticky=(N,S,E,W))
    
    lblListOfLogos = ttk.Label(ttkFrameRoot, text="LOGO")
    lblListOfLogos.grid(column=COLUMN_LOGO, row=0, padx=10, pady=5)
    for i in range(0,len(tupleOfLogos),2):
        lboxListOfLogos.itemconfigure(i, background='#f0f0ff')

# ###############################################################################################
#     stringTupleOfFeature_1 = StringVar(value=tupleOfFeatuer_1)
#     lboxListOfFeature_1 = Listbox(ttkFrameRoot, listvariable=stringTupleOfFeature_1, height=5, exportselection=0)
#     lboxListOfFeature_1.grid(column=COLUMN_FEATURE_1, row=1, rowspan=ROW_SPAN, sticky=(N,S,E,W))

#     lblListOfFeature_1 = ttk.Label(ttkFrameRoot, text="FEATURE 1")
#     lblListOfFeature_1.grid(column=COLUMN_FEATURE_1, row=0, padx=10, pady=5)
#     for i in range(0,len(tupleOfFeatuer_1),2):
#         lboxListOfFeature_1.itemconfigure(i, background='#f0f0ff')

###############################################################################################
    stringTupleOfBootAnimation = StringVar(value=tupleOfBootAnimation)
    lboxListOfBootAnimation = Listbox(ttkFrameRoot, listvariable=stringTupleOfBootAnimation, height=5, exportselection=0)
    lboxListOfBootAnimation.grid(column=COLUMN_BOOT_ANIMATION, row=1, rowspan=ROW_SPAN, sticky=(N,S,E,W))

    lblListOfBootAnimation = ttk.Label(ttkFrameRoot, text="BOOT ANIMATION")
    lblListOfBootAnimation.grid(column=COLUMN_BOOT_ANIMATION, row=0, padx=10, pady=5)


    for i in range(0,len(tupleOfBootAnimation),2):
        lboxListOfBootAnimation.itemconfigure(i, background='#f0f0ff')    
###############################################################################################
    stringTupleOfLaunchers = StringVar(value=tupleOfLaunchers)
    lboxListOfLaunchers = Listbox(ttkFrameRoot, listvariable=stringTupleOfLaunchers, height=5, exportselection=0)
    lboxListOfLaunchers.grid(column=COLUMN_LAUNCHER, row=1, rowspan=ROW_SPAN, sticky=(N,S,E,W))

    lblListOfLaunchers = ttk.Label(ttkFrameRoot, text="LAUNCHER")
    lblListOfLaunchers.grid(column=COLUMN_LAUNCHER, row=0, padx=10, pady=5)


    for i in range(0,len(tupleOfLaunchers),2):
        lboxListOfLaunchers.itemconfigure(i, background='#f0f0ff') 

###############################################################################################
    stringTupleOfSystemApks = StringVar(value=tupleOfSystemApks)
    lboxListOfSystemApks = Listbox(ttkFrameRoot, listvariable=stringTupleOfSystemApks, height=7, exportselection=0)
    lboxListOfSystemApks.grid(column=COLUMN_SYSTEM_APK, row=1,  sticky=(N,S,E,W))

    lblListOfSystemApks = ttk.Label(ttkFrameRoot, text="SYSTEM APK")
    lblListOfSystemApks.grid(column=COLUMN_SYSTEM_APK, row=0, padx=10, pady=5)


    for i in range(0,len(tupleOfSystemApks),2):
        lboxListOfSystemApks.itemconfigure(i, background='#f0f0ff') 
###############################################################################################
    stringTupleOfUserApks = StringVar(value=tupleOfUserApks)
    lboxListOfUserApks = Listbox(ttkFrameRoot, listvariable=stringTupleOfUserApks, height=15, exportselection=0)
    lboxListOfUserApks.grid(column=COLUMN_SYSTEM_APK, row=5 + 2,  sticky=(N,S,E,W))

    lblListOfUserApks = ttk.Label(ttkFrameRoot, text="User APK")
    lblListOfUserApks.grid(column=COLUMN_SYSTEM_APK, row=5 + 1, padx=10, pady=5)


    for i in range(0,len(tupleOfUserApks),2):
        lboxListOfUserApks.itemconfigure(i, background='#f0f0ff')

###############################################################################################
    
    stringTupleOfSystemApksAfterExtracting = StringVar(value=tupleOfSystemApksAfterExtracting)
    lboxListOfSystemApksAfterExtracting = Listbox(ttkFrameRoot, listvariable=stringTupleOfSystemApksAfterExtracting, height=30, exportselection=0)
    lboxListOfSystemApksAfterExtracting.grid(column=COLUMN_SYSTEM_APK, row=20 + 2, rowspan=ROW_SPAN, sticky=(N,S,E,W))

    lblListOfSystemApksAfterExtracting = ttk.Label(ttkFrameRoot, text="SYSTEM APK AFTER EXTRACT SYSTEM.IMG")
    lblListOfSystemApksAfterExtracting.grid(column=COLUMN_SYSTEM_APK, row=20 + 1, padx=10, pady=5)


    for i in range(0,len(tupleOfSystemApksAfterExtracting),2):
        lboxListOfSystemApksAfterExtracting.itemconfigure(i, background='#f0f0ff') 
################################################################################################
################################################################################################
    def Delete_a_List(list):
        list.delete(0, END)
        pass
    
    def Insert_a_Lists(list, folder_path):
        if(os.path.exists(folder_path)):
            for item in os.listdir(folder_path):
                list.insert(END, item)
        else:
            print 'There is not such folder' + folder_path


    def Insert_an_Item(list, item):
        list.insert(END, item)
    
    def Get_Folder_Path(option):
        folder_path = ''
        if(option == COLUMN_SUPPLIERS):
            folder_path = SUPPLIER_PATH \
                            + lboxListOfSuppliers.get(lboxListOfSuppliers.curselection()) 
        elif(option == COLUMN_CHIPSET):
            folder_path = SUPPLIER_PATH \
                            + lboxListOfSuppliers.get(lboxListOfSuppliers.curselection()) + '\\'\
                            + lboxListOfChipsets.get(lboxListOfChipsets.curselection())
        elif(option == COLUMN_BOARD):
            folder_path = SUPPLIER_PATH \
                            + lboxListOfSuppliers.get(lboxListOfSuppliers.curselection()) + '\\'\
                            + lboxListOfChipsets.get(lboxListOfChipsets.curselection()) + '\\'\
                            + lboxListOfBoards.get(lboxListOfBoards.curselection())
        elif(option == COLUMN_SIZE):
            folder_path = SUPPLIER_PATH \
                            + lboxListOfSuppliers.get(lboxListOfSuppliers.curselection()) + '\\'\
                            + lboxListOfChipsets.get(lboxListOfChipsets.curselection()) + '\\'\
                            + lboxListOfBoards.get(lboxListOfBoards.curselection()) + '\\'\
                            + lboxListOfSizes.get(lboxListOfSizes.curselection())
        elif(option == COLUMN_PANEL):    
            folder_path = SUPPLIER_PATH \
                            + lboxListOfSuppliers.get(lboxListOfSuppliers.curselection()) + '\\'\
                            + lboxListOfChipsets.get(lboxListOfChipsets.curselection()) + '\\'\
                            + lboxListOfBoards.get(lboxListOfBoards.curselection()) + '\\'\
                            + lboxListOfSizes.get(lboxListOfSizes.curselection()) + '\\'\
                            + lboxListOfPanels.get(lboxListOfPanels.curselection())
        elif(option == COLUMN_CURRENT):
            folder_path = SUPPLIER_PATH \
                            + lboxListOfSuppliers.get(lboxListOfSuppliers.curselection()) + '\\'\
                            + lboxListOfChipsets.get(lboxListOfChipsets.curselection()) + '\\'\
                            + lboxListOfBoards.get(lboxListOfBoards.curselection()) + '\\'\
                            + lboxListOfSizes.get(lboxListOfSizes.curselection()) + '\\'\
                            + lboxListOfPanels.get(lboxListOfPanels.curselection()) + '\\'\
                            + lboxListOfCurrents.get(lboxListOfCurrents.curselection())
        elif(option == COLUMN_LOGO):
            folder_path = SUPPLIER_PATH \
                            + lboxListOfSuppliers.get(lboxListOfSuppliers.curselection()) + '\\'\
                            + lboxListOfChipsets.get(lboxListOfChipsets.curselection()) + '\\'\
                            + lboxListOfBoards.get(lboxListOfBoards.curselection()) + '\\'\
                            + lboxListOfSizes.get(lboxListOfSizes.curselection()) + '\\'\
                            + lboxListOfPanels.get(lboxListOfPanels.curselection()) + '\\'\
                            + lboxListOfCurrents.get(lboxListOfCurrents.curselection()) + '\\' \
                            + lboxListOfLogos.get(lboxListOfLogos.curselection())
        elif(option == COLUMN_BOOT_ANIMATION):
            folder_path = relativePath_BootAnimation + lboxListOfBootAnimation.get(lboxListOfBootAnimation.curselection())
        elif(option == COLUMN_LAUNCHER):
            folder_path = relativePath_Apks + 'Launchers\\' \
                            + lboxListOfChipsets.get(lboxListOfChipsets.curselection()) + '\\'\
                            + lboxListOfBootAnimation.get(lboxListOfBootAnimation.curselection())
            pass
        elif(option == SAVING_BIN_FILE_PATH):
            folder_path = SUPPLIER_PATH[14:] \
                            + lboxListOfSuppliers.get(lboxListOfSuppliers.curselection()) + '\\'\
                            + lboxListOfChipsets.get(lboxListOfChipsets.curselection()) + '\\'\
                            + lboxListOfBoards.get(lboxListOfBoards.curselection()) + '\\'\
                            + lboxListOfSizes.get(lboxListOfSizes.curselection()) + '\\'\
                            + lboxListOfPanels.get(lboxListOfPanels.curselection()) + '\\'\
                            + lboxListOfCurrents.get(lboxListOfCurrents.curselection()) + '\\' \
                            + lboxListOfLogos.get(lboxListOfLogos.curselection()) + '\\' \
                            + lboxListOfBootAnimation.get(lboxListOfBootAnimation.curselection()) + '\\' \
                            + lboxListOfLaunchers.get(lboxListOfLaunchers.curselection())
        return folder_path
################################################################################################
################################################################################################
    def Update_List_Of_Suppliers(*args):
        print(lboxListOfSuppliers.get(lboxListOfSuppliers.curselection()))
        relativePath_Supplier = Get_Folder_Path(COLUMN_SUPPLIERS)
        print(relativePath_Supplier)
        Delete_a_List(lboxListOfChipsets)
        Insert_a_Lists(lboxListOfChipsets, relativePath_Supplier)
    
    def Update_List_Of_Chipsets(*args):
        print(lboxListOfChipsets.get(lboxListOfChipsets.curselection()))
        relativePath_Board = Get_Folder_Path(COLUMN_CHIPSET)
        print(relativePath_Board)
        Delete_a_List(lboxListOfBoards)
        Insert_a_Lists(lboxListOfBoards, relativePath_Board)
    
    def Update_List_Of_Boards(*args):
        print(lboxListOfBoards.get(lboxListOfBoards.curselection()))
        relativePath_Size = Get_Folder_Path(COLUMN_BOARD)
        print(relativePath_Size)
        Delete_a_List(lboxListOfSizes)
        Insert_a_Lists(lboxListOfSizes, relativePath_Size)
    
    def Update_List_Of_Sizes(*args):
        print(lboxListOfSizes.get(lboxListOfSizes.curselection()))
        relativePath_Panel = Get_Folder_Path(COLUMN_SIZE)
        print(relativePath_Panel)
        Delete_a_List(lboxListOfPanels)
        Insert_a_Lists(lboxListOfPanels, relativePath_Panel)

    def Update_List_Of_Panels(*args):
        print(lboxListOfPanels.get(lboxListOfPanels.curselection()))
        print relativePath_Panel
        relativePath_Current = Get_Folder_Path(COLUMN_PANEL)
        print(relativePath_Current)
        Delete_a_List(lboxListOfCurrents)
        Insert_a_Lists(lboxListOfCurrents, relativePath_Current)

    def Update_List_Of_Currents(*args):
        relativePath_Logo = Get_Folder_Path(COLUMN_CURRENT)
        print(relativePath_Logo)
        Delete_a_List(lboxListOfLogos)
        Insert_a_Lists(lboxListOfLogos, relativePath_Logo)

    def Update_List_Of_Logos(*args):
        print(lboxListOfLogos.get(lboxListOfLogos.curselection()))
        relativePath_BinFile = Get_Folder_Path(COLUMN_LOGO)
        if(os.path.exists(relativePath_BinFile)):
            for item in os.listdir(relativePath_BinFile):
                print item
                lblVariableBinFile.set(item)

        # Delete_a_List(lboxListOfPanels)
        # insert_a_Lists(lboxListOfPanels, os.listdir(str))
        pass
    
    

    def Update_List_Of_Feature_1(*args):
        print(lboxListOfFeature_1.get(lboxListOfFeature_1.curselection()))
        strLaunchers = APKS_PATH + 'Launchers\\' + lboxListOfBootAnimation.get(lboxListOfBootAnimation.curselection()) + '\\' +  lboxListOfFeature_1.get(lboxListOfFeature_1.curselection())
        # str = SUPPLIER_PATH + lboxListOfSuppliers.get(lboxListOfSuppliers.curselection()) + '\\' + lboxListOfSuppliers.get(lboxListOfSuppliers.curselection()) + '\\' + lboxListOfPanels.get(lboxListOfPanels.curselection())
        # print(str)
        Delete_a_List(lboxListOfSystemApks)
        Insert_a_Lists(lboxListOfSystemApks, os.listdir('.\..\Database\APKs\commonSystemAPKs'))
        for item in os.listdir(strLaunchers):
            Insert_an_Item(lboxListOfSystemApks,  item)

        pass
    def Update_List_Of_BootAnimation(*args):
        relativePath_BootAnimation = Get_Folder_Path(COLUMN_LAUNCHER)
        print(relativePath_BootAnimation)
        Delete_a_List(lboxListOfLaunchers)
        Insert_a_Lists(lboxListOfLaunchers, relativePath_BootAnimation)
        pass
        
    def Remove_Old_Launcher_Apk(*args):
        remove_launcher_command = 'rm ' + relativePath_SystemApks + lboxListOfSystemApksAfterExtracting.get(lboxListOfSystemApksAfterExtracting.curselection())
        result = tkMessageBox.askokcancel("Delete Launcher APK", "Are you sure you want to delete " + lboxListOfSystemApksAfterExtracting.get(lboxListOfSystemApksAfterExtracting.curselection()))
        print result
        if(result == True):
            subprocess.call(remove_launcher_command, shell=True)
            Delete_a_List(lboxListOfSystemApksAfterExtracting)
            Insert_a_Lists(lboxListOfSystemApksAfterExtracting, relativePath_SystemApks)
    
    lboxListOfSuppliers.bind('<<ListboxSelect>>', Update_List_Of_Suppliers)
    lboxListOfChipsets.bind('<<ListboxSelect>>',  Update_List_Of_Chipsets)
    lboxListOfBoards.bind('<<ListboxSelect>>',  Update_List_Of_Boards)
    lboxListOfSizes.bind('<<ListboxSelect>>',  Update_List_Of_Sizes)
    lboxListOfPanels.bind('<<ListboxSelect>>',  Update_List_Of_Panels)
    lboxListOfCurrents.bind('<<ListboxSelect>>',  Update_List_Of_Currents)
    lboxListOfLogos.bind('<<ListboxSelect>>',  Update_List_Of_Logos)
    # lboxListOfFeature_1.bind('<<ListboxSelect>>', Action_For_List_Of_Feature_1)
    lboxListOfBootAnimation.bind('<<ListboxSelect>>',  Update_List_Of_BootAnimation)

    lboxListOfSystemApksAfterExtracting.bind('<Double-1>', Remove_Old_Launcher_Apk)

##########################################################################################    
    def Unpack_Bin_File():
        print('Run unpack...!')
        bin_file_path = Get_Folder_Path(COLUMN_LOGO)
        # bin_file_path = os.listdir(temp_path)
        print('bin_file_path'+ bin_file_path)
        unpacked_scripts.Unpack_Bin_File(binpath = bin_file_path)
         
##########################################################################################            
    def Pack_Bin_File():
        user_apks = relativePath_Apks + 'commonUserAPKs\\' 
        system_apks = relativePath_Apks + 'commonSystemAPKs\\'
        launcher = Get_Folder_Path(COLUMN_LAUNCHER) 
        boot_animation = Get_Folder_Path(COLUMN_BOOT_ANIMATION)
        auto_build_bin_file.Build_System_Image(user_apks, system_apks, launcher, boot_animation)
        pass
       
    def Save_Bin_File():
        relativePath = Get_Folder_Path(SAVING_BIN_FILE_PATH)
        relativePath_BinFile = Get_Folder_Path(COLUMN_LOGO)
        if(os.path.exists(relativePath_BinFile)):
            for item in os.listdir(relativePath_BinFile):
                print item
                lblVariableBinFile.set(item)
                bin_file_name = item
        
        auto_build_bin_file.Save_Bin_File_To_Dropbox(relativePath, bin_file_name)
    
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
        Pack_Bin_File()

        print('Start_Copy_Bin_File')
        lblVariableInProgress.set('Start_Copy_Bin_File')
        Save_Bin_File()
        # COLUMN_BUTTON
    
    
    lblBinFile1 = ttk.Label(ttkFrameRoot, text="BinFile")
    lblBinFile1.grid(column=COLUMN_PANEL, row=ROW_SPAN + 1)

    lblVariableBinFile = StringVar()
    lblBinFile = ttk.Label(ttkFrameRoot, text="BinFile", textvariable = lblVariableBinFile)
    lblBinFile.grid(column=COLUMN_CURRENT, row=ROW_SPAN + 1, columnspan = 3, sticky = W)

    lblProgress1 = ttk.Label(ttkFrameRoot, text="In Progress")
    lblProgress1.grid(column=COLUMN_PANEL, row=ROW_SPAN + 2)

    lblVariableInProgress = StringVar()
    lblInProgress = ttk.Label(ttkFrameRoot, textvariable = lblVariableInProgress)
    lblInProgress.grid(column=COLUMN_CURRENT, row=ROW_SPAN + 2, columnspan = 3, sticky = W)
    
    ttkButtonBuildBinFile = ttk.Button(ttkFrameRoot, text='BUILD', command=Start_Build_Bin_File, default='active')
    ttkButtonBuildBinFile.grid(column=4, row=ROW_SPAN + 3, padx=10, pady=5)
    ttkButtonQuit = ttk.Button(ttkFrameRoot, text='QUIT', command=root.quit, default = 'active')
    ttkButtonQuit.grid(column=5, row=ROW_SPAN + 3, padx=10, pady=5)



    root.mainloop()