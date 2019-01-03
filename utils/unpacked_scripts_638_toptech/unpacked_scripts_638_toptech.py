import os.path
import subprocess
import glob
import os

MSTAR_BIN_TOOL = '.\\..\\mstar-bin-tool\\' 
BIN_FOR_UNPACK = 'MstarUpgrade_UNPACK.BIN'
INI_FILE = 'ubctv-tt638-no.ini'
UNPACK_FOLDER = 'unpacked_tt638_no\\'



MSTAR_ANDROID = 'android_tt638\\'
SYSTEM_IMAGE_FILE = 'system.img'
temp = 'abc'
def extract_size(line):
	return 'size=' + line.split()[-1] + '\n' 

def load_header_file_store_to_mmc_info(header_file_name):
    print 'nguyen load_header_file_store_to_mmc_info'
    fread = open(header_file_name, 'r+')
    line_num = 0
    mmc_info = {}
    list_env = []
	# search for lines that contain 'CEnv_UpgradeCRC_Tmp' and 'CEnv_UpgradeCRC_Val'
	# get the CRC number and add it by 1
    for line in fread:
        print 'out nguyen \t' + line
        if 'mmc create factorydata' in line:
            print(extract_size(line))
            mmc_info['factorydata'] = extract_size(line)
        elif 'mmc create misc' in line:
            mmc_info['misc'] = extract_size(line)
        elif 'mmc create license' in line:
            mmc_info['license'] = extract_size(line)
        elif 'mmc create tee' in line:
            mmc_info['tee'] = extract_size(line)
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
            print 'nguyen \t' + line
            list_env.append('\t' + line)
    fread.close()
    return list_env, mmc_info
	
def copy_env_variable_to_ini_file(cwd, binFileName, list_env, mmc_info):
    file_name = cwd + 'configs\\' + INI_FILE
    print file_name
    #file_name = file_name.replace('/', '\\')
    temp_file_name =  cwd + 'configs/temp.ini'
    fread = open(file_name, 'r')
    fwrite = open(temp_file_name, 'w')

    list_index = 0
    env_name = 'nothing'
    index = 0
    bool_modify_firmware_filename = 0
    # search for lines that contain 'CEnv_UpgradeCRC_Tmp' and 'CEnv_UpgradeCRC_Val'
    # get the CRC number and add it by 1
    for line in fread:
        if (env_name == 'nothing'):
            if 'part/factorydata' in line:
                env_name = 'factorydata'
            elif 'part/misc' in line:
                env_name = 'misc'
            elif 'part/license' in line:
                env_name = 'license'
            elif 'part/tee' in line:
                env_name = 'tee'
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


            if 'FirmwareFileName=' in line:
                if bool_modify_firmware_filename == 0:
                    fwrite.write('FirmwareFileName=' + binFileName + '\n')
                    bool_modify_firmware_filename = 1
                else:
                    fwrite.write(line)
            elif 'cleanallenv' in line:
                fwrite.write(line)
                for env in list_env:
                    fwrite.write(env)
            elif 'setenv' in line:
                pass
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
    rename_command = 'ren ' + temp_file_name + ' ' + INI_FILE
    print remove_command
    print rename_command
    rename_command = rename_command.replace('/', '\\')
    subprocess.call(remove_command, shell=True)
    subprocess.call(rename_command, shell=True)



def copy_original_bin_file_for_unpacking(binpath):
    try:
        listFileName = os.listdir(binpath)
        for item in listFileName:
            if('bin' in item):
                binFileName = item
                print binFileName
        copy_command = 'cp ' + binpath + '\\' + binFileName + ' ' + MSTAR_BIN_TOOL + '\\' + BIN_FOR_UNPACK
        print(copy_command)
        subprocess.call(copy_command)
        return binFileName
    except ValueError:
        print ValueError

    

def unpacked(bin_file, cwd):
	#unpacked_command = 'START /WAIT python unpack.py ' + bin_file +  ' ./pana_pack/'
	unpacked_command = 'python3 unpack.py ' + BIN_FOR_UNPACK +  ' ' + UNPACK_FOLDER
	
	print unpacked_command
	print cwd
	subprocess.call(unpacked_command, cwd = cwd, shell = True)

def copy_system_file(cwd):
	remove_old_image = 'rm ' + cwd +  MSTAR_ANDROID  + SYSTEM_IMAGE_FILE 
	copy_new_image = 'cp ' + cwd + UNPACK_FOLDER + SYSTEM_IMAGE_FILE + ' ' + cwd + MSTAR_ANDROID  
	print(remove_old_image)
	print(copy_new_image)
	if(os.path.isfile( cwd + MSTAR_ANDROID + SYSTEM_IMAGE_FILE)):
		subprocess.call(remove_old_image, shell=True) 
	process = subprocess.call(copy_new_image, shell=True)

def extract_system_file(cwd):
	subprocess.call('START /WAIT ' + cwd + MSTAR_ANDROID + 'START.exe', shell=True)

    
def copy_libdecode():
    if(os.path.exists(MSTAR_BIN_TOOL + MSTAR_ANDROID + '\\temp\\system\\lib\\libdecode.so') == False):
        copy_lib = 'cp .\\..\\Database\Libs\\libdecode.so ' + MSTAR_BIN_TOOL + MSTAR_ANDROID + 'temp\\system\\lib'
        print(copy_lib)
        process = subprocess.call(copy_lib, shell=True)
    else:
        print 'libdecode is already created!!!'

def copy_tvconfig(tvconfigPath):
    try:
        copy_command = 'cp ' + tvconfigPath + 'tvconfig.img' + ' ' + MSTAR_BIN_TOOL + UNPACK_FOLDER
        print(copy_command)
        subprocess.call(copy_command)
    except ValueError:
        print ValueError

def make_a_user_apk_folder():
    if(os.path.exists(MSTAR_BIN_TOOL + MSTAR_ANDROID + '\\temp\\system\\media\\user_system_apks') == False):
        mkdir_user_apk_folder = 'mkdir ' + MSTAR_BIN_TOOL + MSTAR_ANDROID + '\\temp\\system\\media\\user_system_apks'
        print(mkdir_user_apk_folder)
        process = subprocess.call(mkdir_user_apk_folder, shell=True)
        pass
    else: 
        print 'user_system_apks folder is already created!!!!'
def modify_build_prop(cwd):
    file_name = cwd + MSTAR_ANDROID + 'temp/system/build.prop'
    print file_name
    #file_name = file_name.replace('/', '\\')
    temp_file_name =  cwd + MSTAR_ANDROID + 'temp/system/build.prop.temp'
    fread = open(file_name, 'r')
    fwrite = open(temp_file_name, 'w')

    for line in fread:
        if ('ro.config.low_ram' in line):
            fwrite.write('ro.config.low_ram=false\r')
        elif ('heapstartsize' in line):
            fwrite.write('dalvik.vm.heapstartsize=8m\r')
        elif ('heapgrowthlimit' in line):
            fwrite.write('dalvik.vm.heapgrowthlimit=128m\r')
        elif ('heapsize' in line):
            fwrite.write('dalvik.vm.heapsize=384m\r')	
        elif ('heapmaxfree' in line):
            fwrite.write('dalvik.vm.heapmaxfree=8m\r')		
        else:
            fwrite.write(line)		
    fread.close()
    fwrite.close()
    remove_command = 'rm ' + file_name
    rename_command = 'ren ' + temp_file_name + ' ' + 'build.prop'

    rename_command = rename_command.replace('/', '\\')
    print remove_command
    print rename_command
    subprocess.call(remove_command, shell=True)
    subprocess.call(rename_command, shell=True)



def unpack_procedure(cwd, ini_file = None, bin_file = None, binpath=None):
    if(binpath != None):
        bin_file = copy_original_bin_file_for_unpacking(binpath)
        unpacked(bin_file, cwd)
        list_env, mmc_info = load_header_file_store_to_mmc_info(cwd + UNPACK_FOLDER + '~header_script')
        print list_env
        print mmc_info
        copy_env_variable_to_ini_file(cwd, bin_file, list_env, mmc_info)
        # print('')
        copy_system_file(cwd)
        extract_system_file(cwd)
        copy_libdecode()
        make_a_user_apk_folder()
        # copy_tvconfig(binpath + 'tvconfig.img\\')
        # modify_build_prop(cwd)
        print('=====================================================================')
        print('                  DONE UNPACK BIN FILE                               ')
        print('=====================================================================')
    else:
        print('No bin file!!!')

#######################################################################################################
def Unpack_Bin_File(binpath = None):
    cwd = MSTAR_BIN_TOOL
    unpack_procedure(cwd, binpath = binpath)


	