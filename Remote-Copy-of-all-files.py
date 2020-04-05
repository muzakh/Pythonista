# -*- coding: utf-8 -*-
"""
Grab *.txt files recursiely from present dir and its sub-dirs and copy it on a remote linux machine 

I will use following:
    1. Error Handling
    2. Shell Utility (SHUTIL module) to perform a copy action on all *.txt files

"""

import os
import paramiko
#import shutil
#import subprocess
#import glob


path = os.path.join(os.getcwd(), "")

for parent_dir_char, sub_dir_list, files_list in os.walk(path):
    for files in files_list:
        if files.endswith(".txt"):
            try:
                #subprocess.run(["scp", "{0}" . format(files), "root@192.168.220.2:/tmp/"])
                #shutil.copy(os.path.join(parent_dir_char, files), "root@192.168.220.2:/tmp/")
                #subprocess.call("sshpass -p root scp E:\\E\\latest Stuff\\Python Programing\\CBT Nuggets - Python Programming Python Language\\My Revisions\\third revision\\pickle_file2.txt root@192.168.220.2:/tmp/", shell=True)
                #os.system("sshpass -p password scp -o StrictHostKeyChecking=no local_file_path username@hostname:remote_path")
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
                ssh.connect(hostname = '192.168.220.2', username = 'root' , password = 'root', port = '22' )
                #ssh.connect(hostname = '192.168.220.2', username = 'root' , key_filename = os.path.join(os.getcwd(), "key-prv-2.ppk"), port = '22' )
                
                sftp = ssh.open_sftp()
                
                sftp.chdir("/root")
                sftp.get('test.sh', 'test.sh')
                
                #sftp.chdir("/tmp")
                #sftp.put(files, files)
                
                sftp.close()
                ssh.close()
            except Exception as e:
                print("Execption caught : {0}". format(e))
                #print("Error: SCP execution failed.!")