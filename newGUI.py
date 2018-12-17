from Tkinter import *
import ttk
from utils.bin_built_scripts import auto_build_bin_file
from utils.unpacked_scripts import unpacked_scripts


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
    #root.geometry("350x300") #You want the size of the app to be 500x500
    #root.resizable(0, 0) #Don't allow resizing in the x or y direction
    #configuration = Checkbar(root, ['Unpack', 'UBC', 'PACK'])
    #tgl = Checkbar(root, ['TV40EK','TV40DM','TV43DM', 'TV50PE5', 'TV50SQ8', 'TV55'])
    #configuration.pack(side=TOP,  fill=X)
    #tgl.pack(side=LEFT)
    #configuration.config(relief=GROOVE, bd=2)

    
    
    radioOperation = IntVar()
    radioOperation.set(1)
    radioVoiceOption = IntVar()
    radioVoiceOption.set(0)    
    radioTVType = IntVar()
    radioTVType.set(0)  # initializing the choice, i.e. Python

##########################################################################################
#   OPERATION TYPES 
##########################################################################################
    Operations = [("UNPACK"), ("PACK")]
    
    def Show_Operation_Choice():
        print(Operations[radioOperation.get()])
    
    Label(root, 
            text="""CHOOSE AN OPERATION""",
            justify = LEFT,
            padx = 20).pack(anchor=W)
   
    for val, op in enumerate(Operations):
        Radiobutton(root, 
                    text = op,
                    padx = 20, 
                    variable = radioOperation, 
                    command = Show_Operation_Choice,
                    value = val).pack(anchor=W)


##########################################################################################
#   VOICE OPTION
##########################################################################################
##########################################################################################
    VoiceOption = [("Voice"), ("No Voice")]
    
    def Show_Voice_Option_Choice():
        print(TVs[radioVoiceOption.get()])
    Label(root, 
            text="""CHOOSE VOICE OPTION""",
            justify = LEFT,
            padx = 20).pack(anchor=W)
    for val, op in enumerate(Operations):
        Radiobutton(root, 
                    text = op,
                    padx = 20, 
                    variable = radioVoiceOption, 
                    command = Show_Voice_Option_Choice,
                    value = val).pack(anchor=W)

##########################################################################################
#   TV TYPES 
##########################################################################################
   
    
    TVs = [
        ("TV_32_JP_801"),
        ("TV_32_JP_802_LSC"),
        ("TV_32_JP_802_315"),
        ("TV_40_DM"),
        ("TV_40_EK"),
        ("TV_43_DM")
    ]

    def ShowChoice():
        print(TVs[radioTVType.get()])

    Label(root, text="""""", justify = LEFT, padx = 20).pack(anchor=W)
    Label(root, text="""CHOOSE TV TYPE""", justify = LEFT, padx = 20).pack(anchor=W)

    for val, TV in enumerate(TVs):
        Radiobutton(root, 
                    text = TV,
                    padx = 20, 
                    variable = radioTVType, 
                    command = ShowChoice,
                    value = val).pack(anchor=W)
    
##########################################################################################    
    def Unpack_Bin_File():
        print('Hello' + TVs[radioTVType.get()])
        print('Run unpack...!')
        if("TV_32_JP_801" in TVs[radioTVType.get()]):
            unpacked_scripts.unpacked_TV32_JP()
        if("TV_32_JP_802_LSC" in TVs[radioTVType.get()]):
            unpacked_scripts.unpacked_TV32_JP_802_LSC()
        if("TV_32_JP_802_315" in TVs[radioTVType.get()]):
            unpacked_scripts.unpacked_TV32_JP_802_315()
        elif("TV_40_DM" in TVs[radioTVType.get()]):
            unpacked_scripts.unpacked_TV40_JP_ref54()
        elif("TV_40_EK" in TVs[radioTVType.get()]):
            unpacked_scripts.unpacked_TV40_JP_EK_ref59_ubc()
        elif("TV_43_DM" in TVs[radioTVType.get()]):
            unpacked_scripts.unpacked_TV43_JP()        
##########################################################################################            
    def Pack_Bin_File():
        print('Hello' + TVs[radioTVType.get()])
        print('Run pack...!')
        temp_voice_option = VoiceOption[radioVoiceOption.get()]
        if("TV_32_JP_801" in TVs[radioTVType.get()]):
            auto_build_bin_file.TV_32_JP(temp_voice_option)
        if("TV_32_JP_802_LSC" in TVs[radioTVType.get()]):
            auto_build_bin_file.TV_32_JP_802_LSC(temp_voice_option)
        if("TV_32_JP_802_315" in TVs[radioTVType.get()]):
            auto_build_bin_file.TV_32_JP_802_315(temp_voice_option)
        elif("TV_40_DM" in TVs[radioTVType.get()]):
            auto_build_bin_file.TV_40_JP_ref54(temp_voice_option)
        elif("TV_40_EK" in TVs[radioTVType.get()]):
            auto_build_bin_file.TV_40_JP_EK_ref59_ubc(temp_voice_option)
        elif("TV_43_DM" in TVs[radioTVType.get()]):
            auto_build_bin_file.TV_43_JP(temp_voice_option)     

    
    
##########################################################################################           
##########################################################################################            
    def Start_Build_Bin_File(): 
        if(radioOperation.get() == 0): #unpack option
            Unpack_Bin_File()
        elif (radioOperation.get() == 1): #pack option
            Pack_Bin_File()
        

    ttk.Button(root, text='Quit', command=root.quit).pack(side=RIGHT)
    ttk.Button(root, text='Build', command=Start_Build_Bin_File).pack(side=RIGHT)
    #ttk.Button(root, text='BUILD', command=root.quit).grid(row = num_of_rows + 1, sticky=W, pady=4)
    #ttk.Button(root, text='COPY', command=allstates).grid(column = SECOND_COLUMN, row = num_of_rows + 1, sticky=W, pady=4)

    root.mainloop()