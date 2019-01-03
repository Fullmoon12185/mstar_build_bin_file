import os.path
import subprocess
import glob
from Tkinter import *
import ttk
import tkMessageBox

UBC_LOGO = 1
SANCO_LOGO = 0

USB_DRIVE = 'E:/'


INI_FILE = 'ubctv-tt338-yes.ini'
MSTAR_BIN_TOOL = '.\\..\\mstar-bin-tool\\'
MSTAR_ANDROID = 'android_tt338\\'
USER_APKS = 'temp\\system\\media\\user_system_apks\\'
SYSTEM_APKS = 'temp\\system\\app\\'
MEDIA_FOLDER = 'temp\\system\\media\\'

CONFIGS = 'configs\\'

UNPACK_FOLDER = 'unpacked_tt338_yes\\'

NEW_SYSTEM_IMAGE_FILE = 'new_system.img'
SYSTEM_IMAGE_FILE = 'system.img'

SAVING_FOLDER = 'C:\\Users\\NGUYEN\\Dropbox\\UBC\\TV_ROM_Release\\___TIVI_338_CVT_ROM\\'

##########################################################################################
##########################################################################################
##########################################################################################	
def add_hex_value_by_1(hex_str):
	hex_int = int(hex_str, 16)
	new_int = hex_int + 1
	if 'L' in hex(new_int):
		return hex(new_int)[:-1]
	else:	
		return hex(new_int)
def modify_CRC(cwd, ini_file):
	file_name = cwd + 'configs/' + ini_file
	print file_name
	#file_name = file_name.replace('/', '\\')
	temp_file_name =  cwd + 'configs/temp.ini'
	fread = open(file_name, 'r')
	fwrite = open(temp_file_name, 'w')
	line_num = 0
	# search for lines that contain 'CEnv_UpgradeCRC_Tmp' and 'CEnv_UpgradeCRC_Val'
	# get the CRC number and add it by 1
	for line in fread:
		if 'setenv CEnv_UpgradeCRC_Tmp' in line:
			print str(line_num) + ': ' + line
			list_word = line.split()
			list_word[2] = add_hex_value_by_1(list_word[2])
			line = '\t' + list_word[0] + ' ' + list_word[1] + ' ' + list_word[2] + '\n'
			fwrite.write(line)
		elif 'setenv CEnv_UpgradeCRC_Val' in line:
			print str(line_num) + ': ' + line
			list_word = line.split()
			list_word[2] = add_hex_value_by_1(list_word[2])
			line = '\t' + list_word[0] + ' ' + list_word[1] + ' ' + list_word[2] + '\n'
			fwrite.write(line)
		else:
			fwrite.write(line)
	fread.close()
	fwrite.close()
	
	#remove the old file, and rename the temp file
	remove_command = 'rm ' + file_name
	rename_command = 'ren ' + temp_file_name + ' ' + ini_file
	rename_command = rename_command.replace('/', '\\')
	print remove_command
	print rename_command
	subprocess.call(remove_command, shell=True)
	subprocess.call(rename_command, shell=True)
	

	

def copy_system_image(cwd, mstar_android):
	copy_new_image = 'cp ' + mstar_android + NEW_SYSTEM_IMAGE_FILE + ' ' + cwd + UNPACK_FOLDER
	remove_old_image = 'rm ' + cwd +  UNPACK_FOLDER  + SYSTEM_IMAGE_FILE 
	rename_new_image  = 'ren ' + cwd + UNPACK_FOLDER  + NEW_SYSTEM_IMAGE_FILE + ' ' + SYSTEM_IMAGE_FILE
	# copy_new_image = copy_new_image.replace('/', '/');
	# remove_old_image = remove_old_image.replace('/', '/');
	rename_new_image = rename_new_image.replace('/', '\\')
	print cwd + mstar_android + NEW_SYSTEM_IMAGE_FILE + '\n'
	if(os.path.isfile(cwd + mstar_android + NEW_SYSTEM_IMAGE_FILE)):
		print copy_new_image
		process = subprocess.call(copy_new_image, shell=True)
		if(os.path.isfile( cwd + UNPACK_FOLDER + SYSTEM_IMAGE_FILE)):
			print remove_old_image
			subprocess.call(remove_old_image, shell=True) 
		subprocess.call(rename_new_image, shell=True)
		print rename_new_image

def delete_user_apks(user_system_apks):
	list_apks = glob.glob(user_system_apks + '*.apk')
	print list_apks
	for apk in list_apks:
		apk = apk.replace('\\', '/')
		delete_apk = 'rm ' + apk
		print delete_apk
		subprocess.call(delete_apk, shell=True)
def delete_old_launcher():
    try:
        list_apk = os.listdir(MSTAR_BIN_TOOL + MSTAR_ANDROID + 'temp\\system\\app\\')
        for item in list_apk:
            if 'launcher' in item.lower():
                print item
                delete_command = 'rm ' + MSTAR_BIN_TOOL + MSTAR_ANDROID + '\\temp\\system\\app\\' + item
                subprocess.call(delete_command, shell=True)		
    except ValueError:
        print ValueError

def copy_common_user_apks(user_apks, user_system_apks):
    try:
        list_apks = glob.glob(user_apks + '*.apk')
        print list_apks
        for apk in list_apks:
            apk = apk.replace('\\', '/')
            user_system_apks = user_system_apks.replace('\\', '/')
            copy_apk = 'cp ' + apk + ' ' + user_system_apks
            print copy_apk
            subprocess.call(copy_apk, shell=True)
    except ValueError:
        print ValueError


def copy_common_system_apks(common_system_apks, system_apks):
    try:
        for item in os.listdir(common_system_apks):
            if 'rocket' in item:
                copy_common_system_apks_command = 'cp ' + common_system_apks + '\\' + item + ' ' + system_apks
                print 'copy_common_system_apks_command'
                print(copy_common_system_apks_command)
                subprocess.call(copy_common_system_apks_command, shell=True)
    except ValueError:
        print ValueError

def copy_launcher(launcher, system_launcher):
    delete_old_launcher()
    try: 
        for item in os.listdir(launcher):
            copy_launcher_command = 'cp ' + launcher + '\\' + item + ' ' + system_launcher
            print 'copy_launcher_command'
            print(copy_launcher_command)
            subprocess.call(copy_launcher_command, shell=True)
    except ValueError:
        print ValueError
    pass
def copy_boot_animation(boot_animation, media_folder, tvsize, version = 'UBC'):
    try:
        if(tvsize == 'TV32'):
            copy_boot_animation_command = '.\\bmc\\Debug\\bmc.exe -t "' + version + '" -i ' + boot_animation + ' -o ' + media_folder + '-w 1280 -h 720 -s 30 --color green --size 13 --back #fffdfd --bold -v'
        else: 
            copy_boot_animation_command = '.\\bmc\\Debug\\bmc.exe -t "' + version + '" -i ' + boot_animation + ' -o ' + media_folder + '-w 1920 -h 1080 -s 30 --color green --size 13 --back #fffdfd --bold -v'
        print(copy_boot_animation_command)
        subprocess.call(copy_boot_animation_command, shell=True)
    except ValueError:
        print ValueError

def copy_system_apks_for_voice_version():
    try:
        list_apks = glob.glob(NEW_SYSTEM_APKS_VOICE_VERSION + '*.apk')
        print list_apks
        for apk in list_apks:
            apk = apk.replace('\\', '/')
            user_system_apks = user_system_apks.replace('\\', '/')
            copy_apk = 'cp ' + apk + ' ' + user_system_apks
            print copy_apk
            subprocess.call(copy_apk, shell=True)
    except ValueError:
        print ValueError


def build_bin_file(ini_file, cwd):
    command = 'python3 pack.py ' + 'configs/' + ini_file
    print command
    print cwd
    process = subprocess.call(command, cwd = cwd, shell=True)
    
    print('=================================================================')
    print('                            COMPLETED                            ')
    print('=================================================================')
    #subprocess.call('python pack.py ' + 'configs/' + ini_file, cwd = cwd, shell=True) 
    #pass
def build_system_file(cwd):
	subprocess.call('START /WAIT ' + cwd + 'START.exe', shell=True)


def copy_bin_file_to_thumb_drive(mstar_bin_file, mstar_folder):
	bin_file = USB_DRIVE + mstar_bin_file
	if(os.path.exists(bin_file)):
		remove_command = 'rm ' + bin_file
		subprocess.call(remove_command, shell = True)
	print('=================================================================')
	print('                            Copying bin file                     ')
	print('=================================================================')
	copy_command = 'cp ' + mstar_folder + mstar_bin_file + ' ' + USB_DRIVE
	subprocess.call(copy_command, shell=True)
	print('=================================================================')
	print('                            Done                                 ')
	print('=================================================================')
	pass	
def get_building_system_image_size(folder_path):
    temp_file_name = 'output_size.txt'
    du_command = 'du -sh ' + folder_path + '> ' + temp_file_name
    print du_command
    subprocess.call(du_command, shell=True)
    fread = open(temp_file_name, 'r')
    for line in fread:
        print line[:3]
        print int(line[:3]) + 50
        tkMessageBox.showinfo("Bin File Size", 'BIN_FILE_SIZE: ' + str(int(line[:3]) + 50) + 'M')

def build_rom_procedure(user_apks, system_apks, launcher, boot_animation, tvsize, version):
    delete_user_apks(MSTAR_BIN_TOOL + MSTAR_ANDROID + USER_APKS)
    print('\n')
    print('----------------------------------------------------------------------')
    print('----------------------- Copying new apks -----------------------------')
    print('----------------------------------------------------------------------')
    print('\n')
    print('\n')
    copy_common_user_apks(user_apks, MSTAR_BIN_TOOL + MSTAR_ANDROID + USER_APKS)
    copy_common_system_apks(system_apks, MSTAR_BIN_TOOL + MSTAR_ANDROID + SYSTEM_APKS)
    copy_launcher(launcher, MSTAR_BIN_TOOL + MSTAR_ANDROID + SYSTEM_APKS)
    copy_boot_animation(boot_animation, MSTAR_BIN_TOOL + MSTAR_ANDROID + MEDIA_FOLDER, tvsize, version)

    get_building_system_image_size(MSTAR_BIN_TOOL + MSTAR_ANDROID + 'temp')
    print('----------------------------------------------------------------------')
    print('---------------------- Building a system image -----------------------')
    print('----------------------------------------------------------------------')
    print('\n')
    print('\n')
    build_system_file(MSTAR_BIN_TOOL + MSTAR_ANDROID)
    print('----------------------------------------------------------------------')
    print('--------------------- Copying a system image -------------------------')
    print('----------------------------------------------------------------------')
    print('\n')
    print('\n')
    copy_system_image(MSTAR_BIN_TOOL, MSTAR_BIN_TOOL + MSTAR_ANDROID)
    # print('----------------------------------------------------------------------')
    # print ('---------------------- Modifying CRC --------------------------------')
    # print('----------------------------------------------------------------------')
    # print('\n')
    # print('\n')
    # modify_CRC(MSTAR_BIN_TOOL, INI_FILE)
    print('----------------------------------------------------------------------')
    print('--------------------- Building bin file ------------------------------')
    print('----------------------------------------------------------------------')
    print('\n')
    print('\n')
    build_bin_file(INI_FILE, MSTAR_BIN_TOOL)
    pass	


def Build_System_Image(user_apks, system_apks, launcher, boot_animation, tvsize, version):
    print user_apks
    print system_apks
    print launcher
    print boot_animation
    build_rom_procedure(user_apks = user_apks, \
                        system_apks = system_apks,\
                        launcher = launcher, \
                        boot_animation = boot_animation, \
                        tvsize = tvsize, \
                        version = version)

def Save_Bin_File_To_Dropbox(path, bin_file_name):
    absolutePath = SAVING_FOLDER + path
    if(os.path.exists(absolutePath) == False):
        mkdir_command = 'mkdir ' + absolutePath
        print mkdir_command
        subprocess.call(mkdir_command, shell = True)
    copy_command = 'cp ' + MSTAR_BIN_TOOL + bin_file_name + ' ' + absolutePath
    print copy_command
    subprocess.call(copy_command, shell = True)
    print('=================================================================')
    print('                            Done                                 ')
    print('=================================================================')
