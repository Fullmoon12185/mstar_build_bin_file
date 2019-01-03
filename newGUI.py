import os
import subprocess

from Tkinter import *
import ttk
from glob import glob
import tkMessageBox
from idlelib.TreeWidget import ScrolledCanvas, FileTreeItem, TreeNode


from utils.bin_built_scripts import auto_build_bin_file
from utils.unpacked_scripts import unpacked_scripts

from utils.unpacked_scripts_338_toptech import unpacked_scripts_338_toptech
from utils.bin_built_scripts_338_toptech import auto_build_bin_file_338_toptech

from utils.unpacked_scripts_638_toptech import unpacked_scripts_638_toptech
from utils.bin_built_scripts_638_toptech import auto_build_bin_file_638_toptech
 
import datetime

import logging


SUPPLIER_PATH = '.\..\Database\Suppliers\\'
APKS_PATH = '.\..\Database\Apks\\'
BOOT_ANIMATION_PATH = '.\\..\\Database\\BootAnimation\\'
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

FONT_SIZE = 15

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
    relativePath_BootAnimation = BOOT_ANIMATION_PATH + 'TV32\\'
    relativePath_SystemApks = '.\\..\\mstar-bin-tool\\MSTAR_Android\\temp\\system\\app\\'

    relativePath = '.\\..\\Database\\Suppliers\\'
    if(os.path.exists(relativePath)):
        tupleOfSuppliers = tuple(os.listdir(relativePath))
    else:
        tupleOfSuppliers = None

    relativePath_Supplier =  relativePath + 'CVT\\'
    if(os.path.exists(relativePath_Supplier)):
        tupleOfChipsets = tuple(os.listdir(relativePath_Supplier))
    else:
        tupleOfChipsets = None

    
    relativePath_Board =  relativePath_Supplier + '338\\'
    if(os.path.exists(relativePath_Board)):
        tupleOfBoards = tuple(os.listdir(relativePath_Board))
    else: 
        tupleOfBoards = None

    relativePath_Size =  relativePath_Board + 'PB801\\'
    if(os.path.exists(relativePath_Size)):
        tupleOfSizes = tuple(os.listdir(relativePath_Size))
    else:
        tupleOfSizes = None

    relativePath_Panel =  relativePath_Size + 'TV32\\'
    if(os.path.exists(relativePath_Panel)):
        tupleOfPanels = tuple(os.listdir(relativePath_Panel))
    else:
        tupleOfPanels = None


    relativePath_Current =  relativePath_Panel + 'ST315\\'    
    if(os.path.exists(relativePath_Current)):
        tupleOfCurrents = tuple(os.listdir(relativePath_Current))
    else:
        tupleOfCurrents = None

    relativePath_Logo =  relativePath_Current + 'REF_300\\' 
    if(os.path.exists(relativePath_Logo)):   
        tupleOfLogos = tuple(os.listdir(relativePath_Logo))
    else:
        tupleOfLogos = None


    if(os.path.exists(relativePath_BootAnimation)): 
        tupleOfBootAnimation = tuple(os.listdir(relativePath_BootAnimation))
    else:
        tupleOfBootAnimation = None

    if(os.path.exists(relativePath_Apks + '\\Launchers\\CVT\\338\UBC')): 
        tupleOfLaunchers = tuple(os.listdir(relativePath_Apks + '\\Launchers\\CVT\\338\UBC'))
    else: 
        tupleOfLaunchers = None

    relatePath_commonSystemAPKs = relativePath_Apks + 'commonSystemAPKs\\338'
    if(os.path.exists(relatePath_commonSystemAPKs)): 
        tupleOfSystemApks = tuple(os.listdir(relatePath_commonSystemAPKs))
    else:
        tupleOfSystemApks = None

    relatePath_commonUserAPKs = relativePath_Apks + 'commonUserApks\\338'
    if(os.path.exists(relatePath_commonUserAPKs)): 
        tupleOfUserApks = tuple(os.listdir(relatePath_commonUserAPKs))
    else: 
        tupleOfUserApks = None

    if(os.path.exists('.\\..\\Database\\Feature1')): 
        tupleOfFeatuer_1 = tuple(os.listdir('.\\..\\Database\\Feature1'))
    else: 
        tupleOfFeatuer_1 = None

    if(os.path.exists(relativePath_SystemApks)): 
        tupleOfSystemApksAfterExtracting = tuple(os.listdir(relativePath_SystemApks))
    else: 
        tupleOfSystemApksAfterExtracting = None
##########################################################################################    
    HIGHT_OF_LIST_BOX = 7



    stringTupleOfSuppliers = StringVar(value=tupleOfSuppliers)
    lboxListOfSuppliers = Listbox(ttkFrameRoot, listvariable=stringTupleOfSuppliers, height=HIGHT_OF_LIST_BOX, exportselection=0)
    lboxListOfSuppliers.grid(column=COLUMN_SUPPLIERS, row=1, rowspan=ROW_SPAN, sticky=(N,S,E,W))
    
    lblListOfSuppliers = ttk.Label(ttkFrameRoot, text="SUPPLIER", font=("Helvetica", FONT_SIZE))
    lblListOfSuppliers.grid(column=COLUMN_SUPPLIERS, row=0, padx=10, pady=5)
    for i in range(0,len(tupleOfSuppliers),2):
        lboxListOfSuppliers.itemconfigure(i, background='#f0f0ff')
    

    

###############################################################################################
    stringTupleOfChipsets = StringVar(value=tupleOfChipsets)
    lboxListOfChipsets = Listbox(ttkFrameRoot, listvariable=stringTupleOfChipsets, height=5, exportselection=0)
    lboxListOfChipsets.grid(column=COLUMN_CHIPSET, row=1, rowspan=ROW_SPAN, sticky=(N,S,E,W))
    
    lblListOfChipsets = ttk.Label(ttkFrameRoot, text="CHIPSET", font=("Helvetica", FONT_SIZE))
    lblListOfChipsets.grid(column=COLUMN_CHIPSET, row=0, padx=10, pady=5)
    for i in range(0,len(tupleOfChipsets),2):
        lboxListOfChipsets.itemconfigure(i, background='#f0f0ff')
###############################################################################################
    stringTupleOfBoards = StringVar(value=tupleOfBoards)
    lboxListOfBoards = Listbox(ttkFrameRoot, listvariable=stringTupleOfBoards, height=5, exportselection=0)
    lboxListOfBoards.grid(column=COLUMN_BOARD, row=1, rowspan=ROW_SPAN, sticky=(N,S,E,W))
    
    lblListOfBoards = ttk.Label(ttkFrameRoot, text="BOARD", font=("Helvetica", FONT_SIZE))
    lblListOfBoards.grid(column=COLUMN_BOARD, row=0, padx=10, pady=5)
    for i in range(0,len(tupleOfBoards),2):
        lboxListOfBoards.itemconfigure(i, background='#f0f0ff')        
###############################################################################################
    stringTupleOfSizes = StringVar(value=tupleOfSizes)
    lboxListOfSizes = Listbox(ttkFrameRoot, listvariable=stringTupleOfSizes, height=5, exportselection=0)
    lboxListOfSizes.grid(column=COLUMN_SIZE, row=1, rowspan=ROW_SPAN, sticky=(N,S,E,W))
    
    lblListOfSizes = ttk.Label(ttkFrameRoot, text="SIZE", font=("Helvetica", FONT_SIZE))
    lblListOfSizes.grid(column=COLUMN_SIZE, row=0, padx=10, pady=5)
    for i in range(0,len(tupleOfSizes),2):
        lboxListOfSizes.itemconfigure(i, background='#f0f0ff')
###############################################################################################

    stringTupleOfPanels = StringVar(value=tupleOfPanels)
    lboxListOfPanels = Listbox(ttkFrameRoot, listvariable=stringTupleOfPanels, height=5, exportselection=0)
    lboxListOfPanels.grid(column=COLUMN_PANEL, row=1, rowspan=ROW_SPAN, sticky=(N,S,E,W))
    
    lblListOfPanels = ttk.Label(ttkFrameRoot, text="PANEL", font=("Helvetica", FONT_SIZE))
    lblListOfPanels.grid(column=COLUMN_PANEL, row=0, padx=10, pady=5)
    for i in range(0,len(tupleOfPanels),2):
        lboxListOfPanels.itemconfigure(i, background='#f0f0ff')
###############################################################################################

    stringTupleOfCurrents = StringVar(value=tupleOfCurrents)
    lboxListOfCurrents = Listbox(ttkFrameRoot, listvariable=stringTupleOfCurrents, height=5, exportselection=0)
    lboxListOfCurrents.grid(column=COLUMN_CURRENT, row=1, rowspan=ROW_SPAN, sticky=(N,S,E,W))
    lblListOfCurrents = ttk.Label(ttkFrameRoot, text="CURRENT", font=("Helvetica", FONT_SIZE))
    lblListOfCurrents.grid(column=COLUMN_CURRENT, row=0, padx=10, pady=5)
    for i in range(0,len(tupleOfCurrents),2):
        lboxListOfCurrents.itemconfigure(i, background='#f0f0ff')
###############################################################################################
    stringTupleOfLogos = StringVar(value=tupleOfLogos)
    lboxListOfLogos = Listbox(ttkFrameRoot, listvariable=stringTupleOfLogos, height=5, exportselection=0)
    lboxListOfLogos.grid(column=COLUMN_LOGO, row=1, rowspan=ROW_SPAN, sticky=(N,S,E,W))
    
    lblListOfLogos = ttk.Label(ttkFrameRoot, text="LOGO", font=("Helvetica", FONT_SIZE))
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

    lblListOfBootAnimation = ttk.Label(ttkFrameRoot, text="ANIMATION", font=("Helvetica", FONT_SIZE))
    lblListOfBootAnimation.grid(column=COLUMN_BOOT_ANIMATION, row=0, padx=10, pady=5)


    for i in range(0,len(tupleOfBootAnimation),2):
        lboxListOfBootAnimation.itemconfigure(i, background='#f0f0ff')    
###############################################################################################
    stringTupleOfLaunchers = StringVar(value=tupleOfLaunchers)
    lboxListOfLaunchers = Listbox(ttkFrameRoot, listvariable=stringTupleOfLaunchers, height=5, exportselection=0)
    lboxListOfLaunchers.grid(column=COLUMN_LAUNCHER, row=1, rowspan=ROW_SPAN, sticky=(N,S,E,W))

    lblListOfLaunchers = ttk.Label(ttkFrameRoot, text="LAUNCHER", font=("Helvetica", FONT_SIZE))
    lblListOfLaunchers.grid(column=COLUMN_LAUNCHER, row=0, padx=10, pady=5)


    for i in range(0,len(tupleOfLaunchers),2):
        lboxListOfLaunchers.itemconfigure(i, background='#f0f0ff') 

###############################################################################################
    stringTupleOfSystemApks = StringVar(value=tupleOfSystemApks)
    lboxListOfSystemApks = Listbox(ttkFrameRoot, listvariable=stringTupleOfSystemApks, height=7, exportselection=0)
    lboxListOfSystemApks.grid(column=COLUMN_SYSTEM_APK, row=1,  sticky=(N,S,E,W))

    lblListOfSystemApks = ttk.Label(ttkFrameRoot, text="USER SYSTEM APKS", font=("Helvetica", FONT_SIZE))
    lblListOfSystemApks.grid(column=COLUMN_SYSTEM_APK, row=0, padx=10, pady=5)


    for i in range(0,len(tupleOfSystemApks),2):
        lboxListOfSystemApks.itemconfigure(i, background='#f0f0ff') 
###############################################################################################
    stringTupleOfUserApks = StringVar(value=tupleOfUserApks)
    lboxListOfUserApks = Listbox(ttkFrameRoot, listvariable=stringTupleOfUserApks, height=15, exportselection=0)
    lboxListOfUserApks.grid(column=COLUMN_SYSTEM_APK, row=5 + 2,  sticky=(N,S,E,W))

    lblListOfUserApks = ttk.Label(ttkFrameRoot, text="User APKS", font=("Helvetica", FONT_SIZE))
    lblListOfUserApks.grid(column=COLUMN_SYSTEM_APK, row=5 + 1, padx=10, pady=5)


    for i in range(0,len(tupleOfUserApks),2):
        lboxListOfUserApks.itemconfigure(i, background='#f0f0ff')

###############################################################################################
    
    stringTupleOfSystemApksAfterExtracting = StringVar(value=tupleOfSystemApksAfterExtracting)
    lboxListOfSystemApksAfterExtracting = Listbox(ttkFrameRoot, listvariable=stringTupleOfSystemApksAfterExtracting, height=30, exportselection=0)
    lboxListOfSystemApksAfterExtracting.grid(column=COLUMN_SYSTEM_APK, row=20 + 2, rowspan=ROW_SPAN, sticky=(N,S,E,W))

    lblListOfSystemApksAfterExtracting = ttk.Label(ttkFrameRoot, text="SYSTEM APKS", font=("Helvetica", FONT_SIZE))
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
    

    def Get_Version():
        version = lboxListOfBootAnimation.get(lboxListOfBootAnimation.curselection()) + '_'
        if('TV32' in lboxListOfSizes.get(lboxListOfSizes.curselection())):
            version = version + '32'
        elif('TV40' in lboxListOfSizes.get(lboxListOfSizes.curselection())):
            version = version + '40'
        elif('TV43' in lboxListOfSizes.get(lboxListOfSizes.curselection())):
            version = version + '43'
            
        version = version + lboxListOfPanels.get(lboxListOfPanels.curselection())
        version = version + lboxListOfCurrents.get(lboxListOfCurrents.curselection())
            
        if('Hinh_Binh_Hanh' in lboxListOfLaunchers.get(lboxListOfLaunchers.curselection())):
            version = version + 'UXBH'
        elif('Hinh_Chu_Nhat' in lboxListOfLaunchers.get(lboxListOfLaunchers.curselection())):
            version = version + 'UXCN'
        elif('Chin_Cuc' in lboxListOfLaunchers.get(lboxListOfLaunchers.curselection())):    
            version = version + 'UX9C'
        
        version = version + lboxListOfBoards.get(lboxListOfBoards.curselection())
        now = datetime.datetime.now()
        strDate = str(now.year) + str(now.month) + str(now.day) + '_' + str(now.hour) + str(now.minute) + str(now.second)
        # version = version + strDate
        return version
        
    def Get_Folder_Path(option):
        folder_path = ''
        if(option == COLUMN_SUPPLIERS):
            folder_path = SUPPLIER_PATH \
                            + lboxListOfSuppliers.get(lboxListOfSuppliers.curselection()) + '\\'
        elif(option == COLUMN_CHIPSET):
            folder_path = SUPPLIER_PATH \
                            + lboxListOfSuppliers.get(lboxListOfSuppliers.curselection()) + '\\'\
                            + lboxListOfChipsets.get(lboxListOfChipsets.curselection()) + '\\'
        elif(option == COLUMN_BOARD):
            folder_path = SUPPLIER_PATH \
                            + lboxListOfSuppliers.get(lboxListOfSuppliers.curselection()) + '\\'\
                            + lboxListOfChipsets.get(lboxListOfChipsets.curselection()) + '\\'\
                            + lboxListOfBoards.get(lboxListOfBoards.curselection()) + '\\'
        elif(option == COLUMN_SIZE):
            folder_path = SUPPLIER_PATH \
                            + lboxListOfSuppliers.get(lboxListOfSuppliers.curselection()) + '\\'\
                            + lboxListOfChipsets.get(lboxListOfChipsets.curselection()) + '\\'\
                            + lboxListOfBoards.get(lboxListOfBoards.curselection()) + '\\'\
                            + lboxListOfSizes.get(lboxListOfSizes.curselection()) + '\\' 
        elif(option == COLUMN_PANEL):    
            folder_path = SUPPLIER_PATH \
                            + lboxListOfSuppliers.get(lboxListOfSuppliers.curselection()) + '\\'\
                            + lboxListOfChipsets.get(lboxListOfChipsets.curselection()) + '\\'\
                            + lboxListOfBoards.get(lboxListOfBoards.curselection()) + '\\'\
                            + lboxListOfSizes.get(lboxListOfSizes.curselection()) + '\\'\
                            + lboxListOfPanels.get(lboxListOfPanels.curselection()) + '\\'
        elif(option == COLUMN_CURRENT):
            folder_path = SUPPLIER_PATH \
                            + lboxListOfSuppliers.get(lboxListOfSuppliers.curselection()) + '\\'\
                            + lboxListOfChipsets.get(lboxListOfChipsets.curselection()) + '\\'\
                            + lboxListOfBoards.get(lboxListOfBoards.curselection()) + '\\'\
                            + lboxListOfSizes.get(lboxListOfSizes.curselection()) + '\\'\
                            + lboxListOfPanels.get(lboxListOfPanels.curselection()) + '\\'\
                            + lboxListOfCurrents.get(lboxListOfCurrents.curselection()) + '\\'
        elif(option == COLUMN_LOGO):
            folder_path = SUPPLIER_PATH \
                            + lboxListOfSuppliers.get(lboxListOfSuppliers.curselection()) + '\\'\
                            + lboxListOfChipsets.get(lboxListOfChipsets.curselection()) + '\\'\
                            + lboxListOfBoards.get(lboxListOfBoards.curselection()) + '\\'\
                            + lboxListOfSizes.get(lboxListOfSizes.curselection()) + '\\'\
                            + lboxListOfPanels.get(lboxListOfPanels.curselection()) + '\\'\
                            + lboxListOfCurrents.get(lboxListOfCurrents.curselection()) + '\\' \
                            + lboxListOfLogos.get(lboxListOfLogos.curselection()) + '\\'
        elif(option == COLUMN_BOOT_ANIMATION):
            folder_path = BOOT_ANIMATION_PATH \
                                + lboxListOfSizes.get(lboxListOfSizes.curselection()) + '\\' \
                                + lboxListOfBootAnimation.get(lboxListOfBootAnimation.curselection()) + '\\'
        elif(option == COLUMN_LAUNCHER):
            folder_path = relativePath_Apks + 'Launchers\\' \
                            + lboxListOfSuppliers.get(lboxListOfSuppliers.curselection()) + '\\'\
                            + lboxListOfChipsets.get(lboxListOfChipsets.curselection()) + '\\'\
                            + lboxListOfBootAnimation.get(lboxListOfBootAnimation.curselection()) + '\\'
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
                            + lboxListOfLaunchers.get(lboxListOfLaunchers.curselection()) + '\\'
        elif(option == COLUMN_SYSTEM_APK):
            folder_path = relativePath_Apks + 'commonSystemAPKs\\' + lboxListOfChipsets.get(lboxListOfChipsets.curselection()) + '\\'
        elif(option == COLUMN_USER_APK):
            folder_path = relativePath_Apks + 'commonUserAPKs\\' + lboxListOfChipsets.get(lboxListOfChipsets.curselection()) + '\\'
        return folder_path
################################################################################################
################################################################################################

    def Update_System_Apks():
        Delete_a_List(lboxListOfSystemApksAfterExtracting)
        Insert_a_Lists(lboxListOfSystemApksAfterExtracting, relativePath_SystemApks)    

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

        relatePath_commonSystemAPKs = Get_Folder_Path(COLUMN_SYSTEM_APK)
        print(relatePath_commonSystemAPKs)
        Delete_a_List(lboxListOfSystemApks)
        Insert_a_Lists(lboxListOfSystemApks, relatePath_commonSystemAPKs)

        relatePath_commonUserAPKs = Get_Folder_Path(COLUMN_USER_APK)
        print(relatePath_commonUserAPKs)
        Delete_a_List(lboxListOfUserApks)
        Insert_a_Lists(lboxListOfUserApks, relatePath_commonUserAPKs)
        


    
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

        relativePath_BootAnimation = BOOT_ANIMATION_PATH + lboxListOfSizes.get(lboxListOfSizes.curselection())
        print(relativePath_BootAnimation)
        Delete_a_List(lboxListOfBootAnimation)
        Insert_a_Lists(lboxListOfBootAnimation, relativePath_BootAnimation)


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
                if('bin' in item):
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
            Update_System_Apks()
    def Update_List_Of_System_Apks(*args):
        Update_System_Apks()


###########################################################################################
    lboxListOfSuppliers.bind('<<ListboxSelect>>', Update_List_Of_Suppliers)
    lboxListOfChipsets.bind('<<ListboxSelect>>',  Update_List_Of_Chipsets)
    lboxListOfBoards.bind('<<ListboxSelect>>',  Update_List_Of_Boards)
    lboxListOfSizes.bind('<<ListboxSelect>>',  Update_List_Of_Sizes)
    lboxListOfPanels.bind('<<ListboxSelect>>',  Update_List_Of_Panels)
    lboxListOfCurrents.bind('<<ListboxSelect>>',  Update_List_Of_Currents)
    lboxListOfLogos.bind('<<ListboxSelect>>',  Update_List_Of_Logos)
    # lboxListOfFeature_1.bind('<<ListboxSelect>>', Action_For_List_Of_Feature_1)
    lboxListOfBootAnimation.bind('<<ListboxSelect>>',  Update_List_Of_BootAnimation)

    # lboxListOfSystemApksAfterExtracting.bind('<<ListboxSelect>>', Update_List_Of_System_Apks)
    lboxListOfSystemApksAfterExtracting.bind('<Double-1>', Remove_Old_Launcher_Apk)

##########################################################################################    
    def Unpack_Bin_File():
        print('Run unpack...!')
        bin_file_path = Get_Folder_Path(COLUMN_LOGO)
        # bin_file_path = os.listdir(temp_path)
        print('bin_file_path'+ bin_file_path)
        if('CVT' in lboxListOfSuppliers.get(lboxListOfSuppliers.curselection())):
            unpacked_scripts.Unpack_Bin_File(binpath = bin_file_path)
        elif ('TopTech' in lboxListOfSuppliers.get(lboxListOfSuppliers.curselection())):
            if('338' in lboxListOfChipsets.get(lboxListOfChipsets.curselection())):
                unpacked_scripts_338_toptech.Unpack_Bin_File(binpath = bin_file_path)
            elif('638' in lboxListOfChipsets.get(lboxListOfChipsets.curselection())):
                unpacked_scripts_638_toptech.Unpack_Bin_File(binpath = bin_file_path)
##########################################################################################            
    def Pack_Bin_File():
        user_apks = relativePath_Apks + 'commonUserAPKs\\' + lboxListOfChipsets.get(lboxListOfChipsets.curselection()) + '\\'
        system_apks = relativePath_Apks + 'commonSystemAPKs\\' + lboxListOfChipsets.get(lboxListOfChipsets.curselection()) + '\\'
        launcher = Get_Folder_Path(COLUMN_LAUNCHER) + '\\' + lboxListOfLaunchers.get(lboxListOfLaunchers.curselection())
        tvsize = lboxListOfSizes.get(lboxListOfSizes.curselection())
        boot_animation = Get_Folder_Path(COLUMN_BOOT_ANIMATION)
        version = Get_Version()
        if('CVT' in lboxListOfSuppliers.get(lboxListOfSuppliers.curselection())):
            auto_build_bin_file.Build_System_Image(user_apks, system_apks, launcher, boot_animation, tvsize, version)
        elif('TopTech' in lboxListOfSuppliers.get(lboxListOfSuppliers.curselection())):
            if('338' in lboxListOfChipsets.get(lboxListOfChipsets.curselection())):
                auto_build_bin_file_338_toptech.Build_System_Image(user_apks, system_apks, launcher, boot_animation, tvsize, version)
            elif ('638' in lboxListOfChipsets.get(lboxListOfChipsets.curselection())):   
                auto_build_bin_file_638_toptech.Build_System_Image(user_apks, system_apks, launcher, boot_animation, tvsize, version) 
        pass
       
    def Save_Bin_File():
        try:
            relativePath = Get_Folder_Path(SAVING_BIN_FILE_PATH)
            relativePath_BinFile = Get_Folder_Path(COLUMN_LOGO)
            if(os.path.exists(relativePath_BinFile)):
                for item in os.listdir(relativePath_BinFile):
                    if 'bin' in item:
                        print item
                        lblVariableBinFile.set(item)
                        bin_file_name = item
            
            auto_build_bin_file.Save_Bin_File_To_Dropbox(relativePath, bin_file_name)
        except ValueError:
            print ValueError
    
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
        Update_System_Apks()
        print('Start_Build_Bin_File')
        lblVariableInProgress.set('Start_Build_Bin_File')
        Pack_Bin_File()

        print('Start_Copy_Bin_File')
        lblVariableInProgress.set('Start_Copy_Bin_File')
        Save_Bin_File()
        
    def Start_Pack_Bin_File(): 
        print('Start_Build_Bin_File')
        lblVariableInProgress.set('Start_Build_Bin_File')
        
        Pack_Bin_File()
        Update_System_Apks()
        print('Start_Copy_Bin_File')
        lblVariableInProgress.set('Start_Copy_Bin_File')
        Save_Bin_File()
        # COLUMN_BUTTON
    



#################################################################################################################
    BUILD_BUTTON_COLUMN = 3
    PACK_BUTTON_COLUMN = 4
    QUIT_BUTTON_COLUMN = 5

    lblBinFile1 = ttk.Label(ttkFrameRoot, text="BinFile")
    lblBinFile1.grid(column=BUILD_BUTTON_COLUMN, row=2*ROW_SPAN + 1, rowspan = 1)

    lblVariableBinFile = StringVar()
    lblBinFile = ttk.Label(ttkFrameRoot, text="BinFile", textvariable = lblVariableBinFile)
    lblBinFile.grid(column=PACK_BUTTON_COLUMN, row=2*ROW_SPAN + 1, rowspan = 1, columnspan = 3, sticky = W)

    
    lblProgress1 = ttk.Label(ttkFrameRoot, text="In Progress")
    lblProgress1.grid(column=BUILD_BUTTON_COLUMN, row=2*ROW_SPAN + 2, rowspan = 1,)

    lblVariableInProgress = StringVar()
    lblInProgress = ttk.Label(ttkFrameRoot, textvariable = lblVariableInProgress)
    lblInProgress.grid(column=PACK_BUTTON_COLUMN, row=2*ROW_SPAN + 2, rowspan = 1, columnspan = 3, sticky = W)
    

    ttkButtonBuildBinFile = ttk.Button(ttkFrameRoot, text='BUILD', command=Start_Build_Bin_File, default='active')
    ttkButtonBuildBinFile.grid(column=BUILD_BUTTON_COLUMN, row=2*ROW_SPAN + 3, rowspan = 1, padx=10, pady=5)

    ttkButtonPackBinFile = ttk.Button(ttkFrameRoot, text='PACK', command=Start_Pack_Bin_File, default='active')
    ttkButtonPackBinFile.grid(column=PACK_BUTTON_COLUMN, row=2*ROW_SPAN + 3, rowspan = 1, padx=10, pady=5)

    ttkButtonQuit = ttk.Button(ttkFrameRoot, text='QUIT', command=root.quit, default = 'active')
    ttkButtonQuit.grid(column=QUIT_BUTTON_COLUMN, row=2*ROW_SPAN + 3, rowspan = 1, padx=10, pady=5)

    
    root.mainloop()