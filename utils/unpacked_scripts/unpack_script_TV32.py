#This file must stay under folder mstar-bin-tool-32-v2

import os.path
import subprocess
import glob

BIN_FILE_32 = 'allupgrade_msd338_4G_ref54_led_company.bin'
BIN_FILE_40 = ''
MSTAR_32 = './../mstar-bin-tool-32-v2/'
MSTAR_40 = './../mstar-bin-tool-40-v2/'
TV32_INI_FILE = 'panatv-PT320AT01-ref53-full.ini'
TV40_INI_FILE = 'panatv-PT320AT01-ref59-full.ini'
MSTAR_32_Android = 'MSTAR_32_Android/'
MSTAR_40_Android = 'MSTAR_40_Android/'
UNPACKED_FOLDER = 'unpacked/'


def extract_size(line):
	return 'size=' + line.split()[-1] + '\n' 

def load_header_file_store_to_mmc_info(header_file_name):
	fread = open(header_file_name, 'r+')
	line_num = 0;
	mmc_info = {}
	list_env = [];
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
			list_env.append('\t' + line);
	fread.close()
	return list_env, mmc_info
	
def copy_env_variable_to_ini_file(cwd, ini_file, list_env, mmc_info):
	file_name = cwd + 'configs/' + ini_file
	print file_name
	#file_name = file_name.replace('/', '\\')
	temp_file_name =  cwd + 'configs/temp.ini'
	fread = open(file_name, 'r')
	fwrite = open(temp_file_name, 'w')
	
	list_index = 0;
	env_name = 'nothing';
	index = 0;
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
			index = index + 1;
			if (index == 2):
				fwrite.write(mmc_info[env_name])
				env_name = 'nothing'
				index = 0;
			else:
				fwrite.write(line)	
			
	fread.close()
	fwrite.close()
	#remove the old file, and rename the temp file
	remove_command = 'rm ' + file_name
	rename_command = 'ren ' + temp_file_name + ' ' + ini_file
	rename_command = rename_command.replace('/', '\\');
	subprocess.call(remove_command, shell=True)
	subprocess.call(rename_command, shell=True)
	
if __name__ == "__main__":
	if os.path.exists(MSTAR_32):
		cwd = MSTAR_32
		ini_file = TV32_INI_FILE
		bin_file = BIN_FILE_32
	elif os.path.exists(MSTAR_40):
		cwd = MSTAR_40
		ini_file = TV40_INI_FILE
		bin_file = BIN_FILE_40
	
	unpacked_command = 'START /WAIT python unpack.py ' + bin_file +  ' ./pana_pack/'
	print unpacked_command
	subprocess.call(unpacked_command, cwd = cwd, shell = True)
	list_env, mmc_info = load_header_file_store_to_mmc_info(cwd + 'pana_pack/~header_script')
	print list_env
	print mmc_info
	copy_env_variable_to_ini_file(cwd, ini_file, list_env, mmc_info)
	
	