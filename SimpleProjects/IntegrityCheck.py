#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#emreYbs
#Operating System was based on Windows 10. But it can also work on Linux and Mac OS.( os.path ) will handle it.

import hashlib
import os
import re
import os
from time import sleep

# Define a function to calculate the hash of a file
def calculate_hash(file_path, algorithm):
    try:
        with open(file_path, 'rb') as file:
            data = file.read()
            hash = hashlib.new(algorithm)
            hash.update(data)
            hexdigest = hash.hexdigest()
            return hexdigest
    except PermissionError:
        print("\033[31mYou do not have permission to read this file.\033[0m")
    except FileNotFoundError:
        print("\033[31mFile not found.\033[0m")
    except Exception as e:
        print(f"\033[31mError: {e}\033[0m")

def calculate_folder_hash(folder_path, algorithm):
    try:
        hash = hashlib.new(algorithm)
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, 'rb') as f:
                    data = f.read()
                    hash.update(data)
        hexdigest = hash.hexdigest()
        return hexdigest
    except PermissionError:
        print("\033[31mYou do not have permission to read files in this folder.\033[0m")
    except FileNotFoundError:
        print("\033[31mFolder not found.\033[0m")
    except Exception as e:
        print(f"\033[31mError: {e}\033[0m")

print("")
print("*" * 25)
print("\033[1mIntegrityCheck by emreYbs\033[0m")
print("*" * 25)
sleep (0.2)
print("""\033[35mThis script will calculate 
      the hash of any file or folder with 
            available algorithms such as MD5, SHA1, SHA256, etc.\n\033[0m""") 

sleep (0.3)
print("\033[34m\tHashing algorithms available: \n\033[0m")
sleep (0.2)
for algorithm in hashlib.algorithms_guaranteed:
    print(algorithm)
print("")


sleep (0.2)
file_or_folder = input("\033[34mEnter file or folder path: \033[0m")  # Get file or folder path from user
sleep (0.4)
# Validate if the path exists
if not os.path.exists(file_or_folder):
    print("\033[31mInvalid file or folder path.\033[0m")
    print("Exitting...")
    sleep (0.1)
    exit()

# Validate if the path is a file or folder
if not os.path.isfile(file_or_folder) and not os.path.isdir(file_or_folder):
    print("\033[31mInvalid file or folder path.\033[0m")
    sleep (0.1)
    print("Exitting...")
    exit()


# Validate file or folder path
if not re.match(r'^[a-zA-Z0-9:/\\_\-. ]+$', file_or_folder):
    print("\033[31mInvalid file or folder path.\033[0m")
    print("Exitting...")
    exit()

print("\033[35msha256 is the default hashing algorithm. Press ENTER to use default algorithm.\033[0m") 
print("Other Options: md5, sha1, sha224, sha384, sha512, blake2b, blake2s, sha3_224, sha3_256, sha3_384, sha3_512, shake_128, shake_256\n")


algorithm = input("\033[32mEnter hashing algorithm: \n\033[0m") or "sha256" # Default algorithm is sha256, You can change it or press ENTER to use default algorithm

supported_algorithms = ["md5", "sha1", "sha224", "sha256","sha384", "sha512", "blake2b", "blake2s", "sha3_224", "sha3_256", "sha3_384", "sha3_512", "shake_128", "shake_256"]

if algorithm not in supported_algorithms:
    print("\033[31mInvalid hashing algorithm.\033[0m")
    sleep (0.1)
    exit()

print("\033[35mCalculating hash...\033[0m")
print("")

if os.path.isfile(file_or_folder):
    file_hash = calculate_hash(file_or_folder, algorithm)
    if file_hash:
        print(f"{algorithm} hash for {file_or_folder}: {file_hash}")
        output_file = "hash_output.txt"
        with open(output_file, 'w') as file:
            file.write(f"{algorithm} hash for {file_or_folder}: {file_hash}\n")
            print(f"\033[32mOutput saved to {output_file}\033[0m")
    else:
        print("\033[31mError calculating hash.\033[0m")
elif os.path.isdir(file_or_folder):
    folder_hash = calculate_folder_hash(file_or_folder, algorithm)
    if folder_hash:
        print(f"{algorithm} hash for files in {file_or_folder}: {folder_hash}")
        output_file = os.path.join(file_or_folder, "hash_output.txt")
        #with open(output_file, 'w') as file:
        with open(output_file, 'a') as file:
            file.write(f"{algorithm} hash for files in {file_or_folder}: {folder_hash}\n")  
            sleep (0.1)
        print(f"\033[32mOutput saved to {output_file}\033[0m")
    else:
        print("\033[31mError calculating folder hash.\033[0m")
else:
    print("\033[31mInvalid file or folder path.\033[0m")

print("")
print("Exiting...")
print("")


