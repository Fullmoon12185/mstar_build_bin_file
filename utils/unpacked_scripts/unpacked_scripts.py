import os.path
import subprocess
import glob
######################################################################
BIN_FILE_32_315 = 'allupgrade_msd338_4G_ref54_led_company_315.bin'
BIN_FILE_32_315_PANA = 'allupgrade_msd338_4G_ref54_led_company_315.bin'

BIN_FILE_32_320 = 'allupgrade_msd338_4G_ref54_led_company_320.bin'
BIN_FILE_TV32_JP = 'allupgrade_msd338_4G_1G_ref30_company.bin'
BIN_FILE_40_JP = 'allupgrade_msd338_4G_1G_ref59_company.bin'
BIN_FILE_40_HL_PANA = 'allupgrade_msd338_4G_ref68_company.bin'

BIN_FILE_50_JP = 'allupgrade_msd338_8G_1G_ref60_company.bin'
BIN_FILE_50_JP_PANA = 'allupgrade_msd338_8G_1G_ref60_company.bin'
BIN_FILE_50_JP_SQ5 = 'allupgrade_msd338_8G_1G_ref60_company_sq5.bin'
BIN_FILE_50_JP_SQ5_PANA = 'allupgrade_msd338_8G_1G_ref60_company_sq5.bin'

BIN_FILE_55_HL = 'allupgrade_msd338_8G_1G_ref60_company_55inch.bin'

BIN_FILE_55_HL_PANA = 'allupgrade_msd338_8G_1G_ref60_company_55inch.bin'
######################################################################
MSTAR_32_315 = './../mstar-bin-tool-32-315-v2/'
MSTAR_32_315_PANA = './../mstar-bin-tool-32-315-v2-pana/'
MSTAR_32_320 = './../mstar-bin-tool-32-320-v2/'
MSTAR_32_JP = './../mstar-bin-tool-32-jp/'
MSTAR_40_JP = './../mstar-bin-tool-40-v3/'
MSTAR_40_HL_PANA = './../mstar-bin-tool-40-v3-HL-pana/'
MSTAR_50_JP = './../mstar-bin-tool-50-v3/'
MSTAR_50_JP_PANA = './../mstar-bin-tool-50-v3-pana/'
MSTAR_50_JP_SQ5 = './../mstar-bin-tool-50-v3-sq5/'
MSTAR_50_JP_SQ5_PANA = './../mstar-bin-tool-50-v3-sq5-pana/'

MSTAR_55_HL = './../mstar-bin-tool-55-v3/'
MSTAR_55_HL_PANA = './../mstar-bin-tool-55-v3-pana/'
######################################################################
TV32_INI_FILE = 'panatv-PT320AT01-ref53-full.ini'
TV32_INI_FILE_PANA = 'panatv-PT320AT01-ref53-full.ini'
TV32_JP_INI_FILE = 'allupgrade_msd338_4G_1G_ref30.ini'
TV40_JP_INI_FILE = 'panatv-PT320AT01-ref59-full.ini'
TV40_HL_INI_FILE_PANA = 'allupgrade_msd338_4G_ref68.ini'

TV50_JP_INI_FILE = 'allupgrade_msd338_8G_1G_ref60.ini'
TV50_JP_INI_FILE_PANA = 'allupgrade_msd338_8G_1G_ref60.ini'
TV50_JP_SQ5_INI_FILE = 'allupgrade_msd338_8G_1G_ref60.ini'
TV50_JP_SQ5_INI_FILE_PANA = 'allupgrade_msd338_8G_1G_ref60.ini'

TV55_HL_INI_FILE = 'allupgrade_msd338_8G_1G_ref60.ini'
TV55_HL_INI_FILE_PANA = 'allupgrade_msd338_8G_1G_ref60.ini'
######################################################################
MSTAR_32_Android = 'MSTAR_32_Android/'
MSTAR_32_Android_PANA = 'MSTAR_32_Android/'
MSTAR_40_Android = 'MSTAR_40_Android/'
MSTAR_40_Android_HL_PANA = 'MSTAR_40_Android/'

MSTAR_50_Android = 'MSTAR_50_Android/'
MSTAR_50_Android_PANA = 'MSTAR_50_Android/'

MSTAR_55_Android = 'MSTAR_55_Android/'
MSTAR_55_Android_PANA = 'MSTAR_55_Android/'

UNPACKED_FOLDER = 'unpacked/'


def extract_size(line):
	return 'size=' + line.split()[-1] + '\n' 

def load_header_file_store_to_mmc_info(header_file_name):
	fread = open(header_file_name, 'r+')
	line_num = 0
	mmc_info = {}
	list_env = []
	# search for lines that contain 'CEnv_UpgradeCRC_Tmp' and 'CEnv_UpgradeCRC_Val'
	# get the CRC number and add it by 1
	for line in fread:
		if 'mmc create factorydata' in line:
			print(extract_size(line))
			mmc_info['factorydata'] = extract_size(line)
		elif 'mmc create misc' in line:
			mmc_info['misc'] = extract_size(line)
		elif 'mmc create recovery' in line:
			mmc_info['recovery'] = extract_size(line)
		elif 'mmc create boot' in line:
			mmc_info['boot'] = extract_size(line)
		elif 'mmc create RTPM' in line:
			mmc_info['RTPM'] = extract_size(line)
		elif 'mmc create system' in line:
			mmc_info['system'] = extract_size(line)
		elif 'mmc create userdata' in line:
			mmc_info['userdata'] = extract_size(line)
		elif 'mmc create cache' in line:
			mmc_info['cache'] = extract_size(line)
		elif 'mmc create tvservice' in line:
			mmc_info['tvservice'] = extract_size(line)
		elif 'mmc create tvconfig' in line:
			mmc_info['tvconfig'] = extract_size(line)
		elif 'mmc create tvdatabase' in line:
			mmc_info['tvdatabase'] = extract_size(line)
		elif 'mmc create tvcustomer' in line:
			mmc_info['tvcustomer'] = extract_size(line)
		if 'setenv' in line:
			list_env.append('\t' + line)
	fread.close()
	return list_env, mmc_info
	
def copy_env_variable_to_ini_file(cwd, ini_file, list_env, mmc_info):
	file_name = cwd + 'configs/' + ini_file
	print file_name
	#file_name = file_name.replace('/', '\\')
	temp_file_name =  cwd + 'configs/temp.ini'
	fread = open(file_name, 'r')
	fwrite = open(temp_file_name, 'w')
	
	list_index = 0
	env_name = 'nothing'
	index = 0
	# search for lines that contain 'CEnv_UpgradeCRC_Tmp' and 'CEnv_UpgradeCRC_Val'
	# get the CRC number and add it by 1
	for line in fread:
		if (env_name == 'nothing'):
			if 'part/factorydata' in line:
				env_name = 'factorydata'
			elif 'part/misc' in line:
				env_name = 'misc'
			elif 'part/recovery' in line:
				env_name = 'recovery'
			elif 'part/boot' in line:
				env_name = 'boot'
			elif 'part/RTPM' in line:
				env_name = 'RTPM'
			elif 'part/system' in line:
				env_name = 'system'
			elif 'part/userdata' in line:
				env_name = 'userdata'
			elif 'part/cache' in line:
				env_name = 'cache'
			elif 'part/tvservice' in line:
				env_name = 'tvservice'
			elif 'part/tvconfig' in line:
				env_name = 'tvconfig'
			elif 'part/tvdatabase' in line:
				env_name = 'tvdatabase'
			elif 'part/tvcustomer' in line:
				env_name = 'tvcustomer'
			
			if 'setenv' in line:
				fwrite.write(list_env[list_index])
				list_index = list_index + 1
			else:
				fwrite.write(line)
		else:
			index = index + 1
			if (index == 2):
				fwrite.write(mmc_info[env_name])
				env_name = 'nothing'
				index = 0
			else:
				fwrite.write(line)	
			
	fread.close()
	fwrite.close()
	#remove the old file, and rename the temp file
	remove_command = 'rm ' + file_name
	rename_command = 'ren ' + temp_file_name + ' ' + ini_file
	rename_command = rename_command.replace('/', '\\')
	subprocess.call(remove_command, shell=True)
	subprocess.call(rename_command, shell=True)

def unpacked(bin_file, cwd):
	#unpacked_command = 'START /WAIT python unpack.py ' + bin_file +  ' ./pana_pack/'
	unpacked_command = 'python unpack.py ' + bin_file +  ' ./pana_pack/'
	
	print unpacked_command
	print cwd
	subprocess.call(unpacked_command, cwd = cwd, shell = True)
			
def unpacked_TV32_315():
	if os.path.exists(MSTAR_32_315):
		cwd = MSTAR_32_315
		ini_file = TV32_INI_FILE
		bin_file = BIN_FILE_32_315
		
		unpacked(bin_file, cwd)
		list_env, mmc_info = load_header_file_store_to_mmc_info(cwd + 'pana_pack/~header_script')
		print list_env
		print mmc_info
		copy_env_variable_to_ini_file(cwd, ini_file, list_env, mmc_info)
		print('')
		print('=====================================================================')
		print('                              DONE                                   ')
		print('=====================================================================')
	else:
		print('click to unpack TV32_315')
def unpacked_TV32_315_pana():
	if os.path.exists(MSTAR_32_315_PANA):
		cwd = MSTAR_32_315_PANA
		ini_file = TV32_INI_FILE_PANA
		bin_file = BIN_FILE_32_315_PANA
		
		unpacked(bin_file, cwd)
		list_env, mmc_info = load_header_file_store_to_mmc_info(cwd + 'pana_pack/~header_script')
		print list_env
		print mmc_info
		copy_env_variable_to_ini_file(cwd, ini_file, list_env, mmc_info)
		print('')
		print('=====================================================================')
		print('                              DONE                                   ')
		print('=====================================================================')
	else:
		print('click to unpack TV32_PANA_315')		
		
def unpacked_TV32_320():
	if os.path.exists(MSTAR_32_320):
		cwd = MSTAR_32_320
		ini_file = TV32_INI_FILE
		bin_file = BIN_FILE_32_320
		
		unpacked(bin_file, cwd)
		list_env, mmc_info = load_header_file_store_to_mmc_info(cwd + 'pana_pack/~header_script')
		print list_env
		print mmc_info
		copy_env_variable_to_ini_file(cwd, ini_file, list_env, mmc_info)
		print('')
		print('=====================================================================')
		print('                              DONE                                   ')
		print('=====================================================================')
	else:
		print('click to unpacking TV32_320')


def unpacked_TV32_JP():
	if os.path.exists(MSTAR_32_JP):
		cwd = MSTAR_32_JP
		ini_file = TV32_JP_INI_FILE
		bin_file = BIN_FILE_TV32_JP
	
		unpacked(bin_file, cwd)
		list_env, mmc_info = load_header_file_store_to_mmc_info(cwd + 'pana_pack/~header_script')
		print list_env
		print mmc_info
		copy_env_variable_to_ini_file(cwd, ini_file, list_env, mmc_info)
		print('')
		print('=====================================================================')
		print('                              DONE                                   ')
		print('=====================================================================')
	else:
		print('click to unpack TV40')

def unpacked_TV40_JP():
	if os.path.exists(MSTAR_40_JP):
		cwd = MSTAR_40_JP
		ini_file = TV40_JP_INI_FILE
		bin_file = BIN_FILE_40_JP
	
		unpacked(bin_file, cwd)
		list_env, mmc_info = load_header_file_store_to_mmc_info(cwd + 'pana_pack/~header_script')
		print list_env
		print mmc_info
		copy_env_variable_to_ini_file(cwd, ini_file, list_env, mmc_info)
		print('')
		print('=====================================================================')
		print('                              DONE                                   ')
		print('=====================================================================')
	else:
		print('click to unpack TV40')

def unpacked_TV40_HL_pana():
	if os.path.exists(MSTAR_40_HL_PANA):
		cwd = MSTAR_40_HL_PANA
		ini_file = TV40_HL_INI_FILE_PANA
		bin_file = BIN_FILE_40_HL_PANA
	
		unpacked(bin_file, cwd)
		list_env, mmc_info = load_header_file_store_to_mmc_info(cwd + 'pana_pack/~header_script')
		print list_env
		print mmc_info
		copy_env_variable_to_ini_file(cwd, ini_file, list_env, mmc_info)
		print('')
		print('=====================================================================')
		print('                              DONE                                   ')
		print('=====================================================================')
	else:
		print('click to unpack TV40 HL PANA')

def unpacked_TV50_JP():
	if os.path.exists(MSTAR_50_JP):
		cwd = MSTAR_50_JP
		ini_file = TV50_JP_INI_FILE
		bin_file = BIN_FILE_50_JP
	
		unpacked(bin_file, cwd)
		list_env, mmc_info = load_header_file_store_to_mmc_info(cwd + 'pana_pack/~header_script')
		print list_env
		print mmc_info
		copy_env_variable_to_ini_file(cwd, ini_file, list_env, mmc_info)
		print('')
		print('=====================================================================')
		print('                              DONE                                   ')
		print('=====================================================================')
	else:
		print('click to unpack TV50')
def unpacked_TV50_JP_pana():
	if os.path.exists(MSTAR_50_JP_PANA):
		cwd = MSTAR_50_JP_PANA
		ini_file = TV50_JP_INI_FILE_PANA
		bin_file = BIN_FILE_50_JP_PANA
	
		unpacked(bin_file, cwd)
		list_env, mmc_info = load_header_file_store_to_mmc_info(cwd + 'pana_pack/~header_script')
		print list_env
		print mmc_info
		copy_env_variable_to_ini_file(cwd, ini_file, list_env, mmc_info)
		print('')
		print('=====================================================================')
		print('                              DONE                                   ')
		print('=====================================================================')
	else:
		print('click to unpack TV50 pana')

def unpacked_TV50_JP_SQ5():
	if os.path.exists(MSTAR_50_JP_SQ5):
		cwd = MSTAR_50_JP_SQ5
		ini_file = TV50_JP_SQ5_INI_FILE
		bin_file = BIN_FILE_50_JP_SQ5
	
		unpacked(bin_file, cwd)
		list_env, mmc_info = load_header_file_store_to_mmc_info(cwd + 'pana_pack/~header_script')
		print list_env
		print mmc_info
		copy_env_variable_to_ini_file(cwd, ini_file, list_env, mmc_info)
		print('')
		print('=====================================================================')
		print('                              DONE                                   ')
		print('=====================================================================')
	else:
		print('click to unpack TV50 SQ 5')

def unpacked_TV50_JP_SQ5_pana():
	if os.path.exists(MSTAR_50_JP_SQ5_PANA):
		cwd = MSTAR_50_JP_SQ5_PANA
		ini_file = TV50_JP_SQ5_INI_FILE_PANA
		bin_file = BIN_FILE_50_JP_SQ5_PANA
	
		unpacked(bin_file, cwd)
		list_env, mmc_info = load_header_file_store_to_mmc_info(cwd + 'pana_pack/~header_script')
		print list_env
		print mmc_info
		copy_env_variable_to_ini_file(cwd, ini_file, list_env, mmc_info)
		print('')
		print('=====================================================================')
		print('                              DONE                                   ')
		print('=====================================================================')
	else:
		print('click to unpack TV50 SQ5 PANA')


def unpacked_TV55_HL():
	if os.path.exists(MSTAR_55_HL):
		cwd = MSTAR_55_HL
		ini_file = TV55_HL_INI_FILE
		bin_file = BIN_FILE_55_HL
	
		unpacked(bin_file, cwd)
		list_env, mmc_info = load_header_file_store_to_mmc_info(cwd + 'pana_pack/~header_script')
		print list_env
		print mmc_info
		copy_env_variable_to_ini_file(cwd, ini_file, list_env, mmc_info)
		print('')
		print('=====================================================================')
		print('                              DONE                                   ')
		print('=====================================================================')
	else:
		print('click to unpack TV50')

def unpacked_TV55_HL_pana():
	if os.path.exists(MSTAR_55_HL_PANA):
		cwd = MSTAR_55_HL_PANA
		ini_file = TV55_HL_INI_FILE_PANA
		bin_file = BIN_FILE_55_HL_PANA
	
		unpacked(bin_file, cwd)
		list_env, mmc_info = load_header_file_store_to_mmc_info(cwd + 'pana_pack/~header_script')
		print list_env
		print mmc_info
		copy_env_variable_to_ini_file(cwd, ini_file, list_env, mmc_info)
		print('')
		print('=====================================================================')
		print('                              DONE                                   ')
		print('=====================================================================')
	else:
		print('click to unpack TV50 PANA')

def test_import():
	print('Unpacked scripts imported')			