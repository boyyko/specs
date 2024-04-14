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

## Start

To start the program using the default settings:
```
checkrpms --home -t sha256
```

To run the program using the root directory and encryption algorithm:
```
checkrpms --root -t (sha256, md5, gost)
```
To run the program using the usb directory and encryption algorithm:
```
checkrpms --usb -t (sha256, md5, gost)
```

To run using all three main arguments (--home, --root, --usb) and encryption algorithm:
```
checkrpms --home --root --usb -t (sha256, md5, gost)
```
## Example
Suppose we want to check the ELF files of our system that were installed from rpm packages.
We have "reference" rpm packages. Let's put the "reference" rpm packages into a usb device and run the program.
```
checkrpms --usb -t (sha256, md5, gost)
```
The hash type allows you to use various hash algorithms for found ELF files.
During the execution of the program, a separate alt-checksums directory will be created in which the files will be created:
```
failed-checksums.list- The result of comparing the ELF files installed from rpm and the "reference" ELF files.
Contains the checksums of the files and the status FALSE

failed_rpm_check.list-
result.list
rpm
files
```








