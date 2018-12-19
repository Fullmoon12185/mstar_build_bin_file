import os.path
import subprocess
import glob


UBC_LOGO = 1
SANCO_LOGO = 0

USB_DRIVE = 'E:/'



MSTAR_BIN_TOOL = './../mstar-bin-tool/'
MSTAR_ANDROID = 'MSTAR_Android/'
USER_APKS = 'temp/system/media/user_system_apks/'
SYSTEM_APKS = 'temp/system/app/'
BOOT_ANIMATION = 'temp/system/media/'


CONFIGS = 'configs/'
PANA_PACK = 'pana_pack/'

NEW_SYSTEM_IMAGE_FILE = 'new_system.img'
SYSTEM_IMAGE_FILE = 'system.img'


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
	copy_new_image = 'cp ' + mstar_android + NEW_SYSTEM_IMAGE_FILE + ' ' + cwd + PANA_PACK
	remove_old_image = 'rm ' + cwd +  PANA_PACK  + SYSTEM_IMAGE_FILE 
	rename_new_image  = 'ren ' + cwd + PANA_PACK  + NEW_SYSTEM_IMAGE_FILE + ' ' + SYSTEM_IMAGE_FILE
	# copy_new_image = copy_new_image.replace('/', '/');
	# remove_old_image = remove_old_image.replace('/', '/');
	rename_new_image = rename_new_image.replace('/', '\\')
	print cwd + mstar_android + NEW_SYSTEM_IMAGE_FILE + '\n'
	if(os.path.isfile(cwd + mstar_android + NEW_SYSTEM_IMAGE_FILE)):
		print copy_new_image
		process = subprocess.call(copy_new_image, shell=True)
		if(os.path.isfile( cwd + PANA_PACK + SYSTEM_IMAGE_FILE)):
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
		
def copy_common_user_apks(user_system_apks):
	list_apks = glob.glob(NEW_USER_APKS + '*.apk')
	print list_apks
	for apk in list_apks:
		apk = apk.replace('\\', '/')
		user_system_apks = user_system_apks.replace('\\', '/')
		copy_apk = 'cp ' + apk + ' ' + user_system_apks
		print copy_apk
		subprocess.call(copy_apk, shell=True)

def copy_boot_animation(option):
    copy_boot_animation_command = 'cp .\\..\\Database\\BootAnimation\\' + option + '\\bootanimiation.zp ' + '.\\..\\mstar-bin-tool\\MSTAR_Android\\temp\\system\\media'
    print copy_boot_animation_command
    subprocess.call(copy_boot_animation_command, shell=True)

def copy_system_apks_for_voice_version():
	list_apks = glob.glob(NEW_SYSTEM_APKS_VOICE_VERSION + '*.apk')
	print list_apks
	for apk in list_apks:
		apk = apk.replace('\\', '/')
		user_system_apks = user_system_apks.replace('\\', '/')
		copy_apk = 'cp ' + apk + ' ' + user_system_apks
		print copy_apk
		subprocess.call(copy_apk, shell=True)

def copy_system_apks_for_no_voice_version():
	list_apks = glob.glob(NEW_SYSTEM_APKS_NO_VOICE_VERSION + '*.apk')
	print list_apks
	for apk in list_apks:
		apk = apk.replace('\\', '/')
		user_system_apks = user_system_apks.replace('\\', '/')
		copy_apk = 'cp ' + apk + ' ' + user_system_apks
		print copy_apk
		subprocess.call(copy_apk, shell=True)

def copy_apks_for_voice_version():
	list_apks = glob.glob(NEW_USER_APKS + '*.apk')
	print list_apks
	for apk in list_apks:
		apk = apk.replace('\\', '/')
		user_system_apks = user_system_apks.replace('\\', '/')
		copy_apk = 'cp ' + apk + ' ' + user_system_apks
		print copy_apk
		subprocess.call(copy_apk, shell=True)

def copy_feature_1(option):
	list_apks = glob.glob(NEW_USER_APKS + '*.apk')
	print list_apks
	for apk in list_apks:
		apk = apk.replace('\\', '/')
		user_system_apks = user_system_apks.replace('\\', '/')
		copy_apk = 'cp ' + apk + ' ' + user_system_apks
		print copy_apk
		subprocess.call(copy_apk, shell=True)

def copy_launcher(option):
	copy_launcher_command = 'cp ' + '.\\..\\Database\\APKs\\Launchers\\' + option + '\\*launcher*.apk ' '.\\..\\mstar-bin-tool\\MSTAR_Android\\temp\\system\\app'
    print(copy_launcher_command)
    subprocess.call(copy_launcher_command, shell=True)

def build_bin_file(ini_file, cwd):
	command = 'python pack.py ' + 'configs/' + ini_file
	process = subprocess.Popen(command, cwd = cwd, stdout=subprocess.PIPE)
	output, err = process.communicate()
	print output
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

def build_rom_procedure(cwd, mstar_android, launcher, boot_animation, ini_file, voice_option = 0):
	delete_user_apks(mstar_android + USER_APKS)
	print('\n')
	print('----------------------------------------------------------------------')
	print('----------------------- Copying new apks -----------------------------')
	print('----------------------------------------------------------------------')
	print('\n')
	print('\n')
	copy_common_user_apks(mstar_android + USER_APKS)
	copy_system_apks(mstar_android + SYSTEM_APKS)
	copy_launcher(launcher)
	copy_boot_animation(boot_animation)
	if(voice_option == 0):
		copy_apks_for_voice_version()
	else:
		copy_apks_for_no_voice_version()

	print('----------------------------------------------------------------------')
	print('---------------------- Building a system image -----------------------')
	print('----------------------------------------------------------------------')
	print('\n')
	print('\n')
	build_system_file(mstar_android)
	print('----------------------------------------------------------------------')
	print('--------------------- Copying a system image -------------------------')
	print('----------------------------------------------------------------------')
	print('\n')
	print('\n')
	copy_system_image(cwd, mstar_android)
	print('----------------------------------------------------------------------')
	print ('---------------------- Modifying CRC --------------------------------')
	print('----------------------------------------------------------------------')
	print('\n')
	print('\n')
	modify_CRC(cwd, ini_file)
	print('----------------------------------------------------------------------')
	print('--------------------- Building bin file ------------------------------')
	print('----------------------------------------------------------------------')
	print('\n')
	print('\n')
	build_bin_file(ini_file, cwd)
	pass	


def Build_System_Image():
    build_rom_procedure(cwd = MSTAR_BIN_TOOL, mstar_android = MSTAR_ANDROID, )

