## Checkrpms

Search and compare executable files(ELF) for their integrity and security.


## About 
This project was created in order to help find executable files in RPM packages that could potentially pose a threat. 
Checkrpms finds all rpm packages installed in the system and ELF files belonging to them.
Then hashes and compares the files, checking their integrity with reference files.

## Requires

gostsum
sha256sum
md5sum

## Usage

The program supports various startup arguments, allowing you to customize its operation according to your needs. 
The main arguments and examples of their use are presented below.

### Arguments

The arguments allow you to specify the mounting points where files will be searched.
```

--home - Launch the program at the mount point of the home directory.
--root - Running the program at the root mount point
--usb - Launch the program with access to USB devices.
```

### Additional encryption options

Specifying the hash option is required 
```

-t sha256 - Using the SHA-256 encryption algorithm.
-t gost - Using the GOST encryption algorithm.
-t md5 - Using the MD5 encryption algorithm.
-h, --help - Help
```

## Example  

To start the program using the default settings:
checkrpms --home


To run the program using the home directory and encryption using the SHA-256 algorithm:
checkrpms --home -t sha256


To run using all three main arguments (--home, --root, --usb):
checkrpms --home --root --usb


To run using all three main arguments and the encryption type (--home, --root, --usb):
checkrpms --home --root --usb -t (sha256, md5, gost)
