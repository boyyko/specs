## Checkrpms

Search and compare executable files(ELF) for their integrity and security.


## About 
This project was created in order to help find executable files in RPM packages that could potentially pose a threat. 
Checkrpms finds all rpm packages installed in the system and ELF files belonging to them.
Then hashes and compares the files, checking their integrity with reference files.

## Requires

* gostsum
* sha256sum
* md5sum

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
1. Suppose we want to check the ELF files of our system that were installed from rpm packages.
   We have "reference" rpm packages in the usb device. Run the program.
```
checkrpms --usb -t (sha256, md5, gost)
```
The hash type allows you to use various hash algorithms for found ELF files.  
During the execution of the program, a separate alt-checksums directory will be created in which the files will be created:

* failed-checksums.list-  A list of ELF files that differ from the "reference" ELF files.  Contains checksums and status FALSE
* failed_rpm_check.list-  List of "reference" rpm packages whose gpg keys are not correct.
* result.list-            The result of comparing all ELF files. Contains checksums and the status TRUE or FASLE.
* rpm-                    The directory that contains the "reference" rpm packages
* files-                  The directory that contains the "reference" ELF files

Example result.list 
```
--------------------------------------------
foo-0.9.0
<hash> /alt-checksums/files/libfoo.so.0.9.0  # "reference" ELF file
<hash> /usr/lib64/libfoo.so.0.9.0            # Installed in system ELF file
TRUE
--------------------------------------------
```
Example failed-checksums.list
```
--------------------------------------------
hello
<hash>  /alt-checksums/files/hello # "reference" ELF file
<hash>  /usr/bin/hello             # Installed in system ELF file 
FALSE
--------------------------------------------
```
2. We have "reference" rpm packages located somewhere in the home directory.
In this case, we run the program like this:
```
checkrpms --home -t (sha256, md5, gost)
```
In this case, a directory and all the necessary files will be created, as in the previous example.
However, now the program searches for "reference" rpm packages inside the home directory, rather than accessing the usb device.

3. We can also use the root directory to search for "reference" rpm packages
However, be extremely careful!!!
USING THE ROOT DIRECTORY CAN LEAD TO SYSTEM PROBLEMS.
```
checkrpms --root -t (sha256, md5, gost)
```
4. We can also combine arguments or use all 3 search points for "reference" rpm packages.
```
checkrpms --home --usb -t (sha256, md5, gost)
checkrpms --root --usb -t (sha256, md5, gost)
checkrpms --home --usb --root -t (sha256, md5, gost)
checkrpms --home --root -t (sha256, md5, gost)
```



