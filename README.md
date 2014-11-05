Reverse-APK
===========

Extract the `.class` files from an APK using apktool, Smali and dex2jar.<br/>
The tools required will be downloaded by the script.


### Usage

```shell
$ wget -O reverse-apk.py https://raw.githubusercontent.com/pchaigno/Reverse-APK/master/reverse-apk.py
$ python3 reverse-apk.py <apk file>
```

This will download and run the tools on the APK file.
It will start with apktool to unpack the APK file.
A folder will be created containing the `.smali` files.
Smali will be downloaded and run to generate a `.dex` file.
The last tool, dex2jar, will extract the `.class` files from the `.dex` file.

The script will pause before each download and ask the user if he want to continue or manually download the tool.
This step will be skipped if the tools are already present in the same directory as the script.


### Contact

For any suggestion or bug report, please contact me at paul.chaignon@gmail.com.
