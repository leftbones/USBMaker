# USBMaker
Create bootable USB installers from Linux disk images on macOS. This script does NOT work with Windows disk images, but I am working on a possible solution. It's going to be hacky though since macOS does not natively support NTFS. I haven't tested this with a macOS installer image yet, but I think it should work fine.

Your specified target drive will be erased and formatted to FAT32 after the script asks you to confirm your selected target drive. This script is mostly untested, and I am not responsible for any potential data loss caused by this script.

### Installation
Either clone the repo, or download `usbmaker.py` and run it with `sudo python usbmaker.py`
Requires psutil, only tested with Python 3.9+

### Usage
Run the script like any other Python script. It's only tested with Python 3.9+ but may work with older versions.

1. You will be given a list of the available external physical drives on your system. Each drive has an identifier, such as `/dev/diskN` where N is a number. In the prompt, enter the identifier of your desired target drive.
2. After that, it will ask you for the path to your operating system disk image. You can type it in manually, or drag the file into your terminal window. Backslashes are not required for spaces in file names or paths.
3. Then you'll be prompted to confirm your choices, as the target drive will be erased in the next step. When you confirm, the target drive is reformatted as FAT32, then it will be unmounted, and the files from the disk image will be copied to the target drive.

This process can take awhile depending on the size of your disk image, and there is no status indicator, so just be patient and let it run. You will see a message saying `Complete!` when the transfer is finished.
In testing, I found that a 3.5GB ISO file copied to a 16GB USB flash drive over USB 2.0 took around 10 minutes.

Once the transfer is complete, your drive should remain unmounted, and you may get a pop-up message saying that the device was not readable. You can ignore and close this message. Your installer USB is now finished!
