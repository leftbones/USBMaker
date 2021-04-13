import os, sys
import psutil

# PROGRAM ENTER
os.system('clear')
print("[ USBMaker by Evan Parker (@evprkr) ]\n")
print("This script must be run with root privileges.\nOnly .ISO and .IMG files are supported.\n")
print("By using this script, you accept the risk of any potential data loss.\n")

# GET DRIVE IDENTIFIER AND IMAGE FILE PATH
print("Available USB drives:\n")
os.system('diskutil list physical external')

target_drive = input("\nTarget drive identifier (eg. /dev/diskX): ")
iso_path = input("Path to disk image: ").replace('\\', '').strip()

if input("\nAll data on the target drive will be erased, continue? [y/N] ").lower() == 'n': sys.exit(0)
print('\n============\n')

# GET DRIVE INFORMATION AND FORMAT IF NECESSARY
for disk in psutil.disk_partitions(all=False):
    if target_drive in disk.device:
        if disk.fstype != 'msdos':
            print("Formatting disk as FAT32...")
            os.system(f'diskutil eraseDisk FAT32 "INSTALL_DRIVE" GPT {target_drive}')

# UNMOUNT TARGET DRIVE AND COPY IMAGE
print("Unmounting target drive...")
os.system(f'diskutil unmountDisk {target_drive}')
print("Creating installation media (this may take awhile)...")
os.system(f'dd if={iso_path} of={target_drive}')

# SCRIPT EXIT
print("\nComplete!")
