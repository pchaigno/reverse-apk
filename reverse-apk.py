#!/usr/bin/env python3
import sys
import os

# Check usage:
if len(sys.argv) < 2:
	print("usage: reverse-apk.py <apk file>")
	sys.exit(2)

# Arguments:
apk_file = sys.argv[1]

# Download apktool:
if not os.path.isfile("apktool.jar"):
	print("We will now download apktool to unpack the APK.")
	print("It will downloaded from https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.0.0rc2.jar.")
	print("You can choose to stop the script here and download apktool yourself.")
	print("The tool must be named apktool.jar and placed in the same directory as this script.")
	answer = ''
	while answer!='n' and answer!='y':
		answer = input("Do tou wish to continue and download apktool? [y/n] ").lower()
	if answer=='n':
		sys.exit(0)
	os.system("wget -qO apktool.jar https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.0.0rc2.jar")

# Unpack the APK:
print("Unpacking APK...")
os.system("java -jar apktool.jar d " + apk_file + " -fo apk-dir")

# Downloads Smali:
print()
if not os.path.isfile("smali.jar"):
	print("We will now download Smali to convert the .smali files into a .dex file.")
	print("It will downloaded from https://bitbucket.org/JesusFreke/smali/downloads/smali-2.0.3.jar.")
	print("You can choose to stop the script here and download Smali yourself.")
	print("The tool must be named smali.jar and placed in the same directory as this script.")
	answer = ''
	while answer!='n' and answer!='y':
		answer = input("Do tou wish to continue and download Smali? [y/n] ").lower()
	if answer=='n':
		sys.exit(0)
	os.system("wget -qO smali.jar https://bitbucket.org/JesusFreke/smali/downloads/smali-2.0.3.jar")

# Convert the .smali files to a single .dex file
print("Running Smali...")
os.system("java -jar smali.jar apk-dir/smali")

# Downloads and extract dex2jar:
print()
if not os.path.isfile("dex2jar.zip"):
	print("We will now download dex2jar 0.0.9.15 to convert the .dex file into a .jar file.")
	print("It will downloaded from https://dex2jar.googlecode.com/files/dex2jar-0.0.9.15.zip.")
	print("You can choose to stop the script here and download dex2jar yourself.")
	print("The tool must be named dex2jar.zip and placed in the same directory as this script.")
	answer = ''
	while answer!='n' and answer!='y':
		answer = input("Do tou wish to continue and download dex2jar? [y/n] ").lower()
	if answer=='n':
		sys.exit(0)
	os.system("wget -qO dex2jar.zip https://dex2jar.googlecode.com/files/dex2jar-0.0.9.15.zip")
os.system("unzip dex2jar.zip")

# Convert the .dex file to a .jar file:
print("Converting the .dex file into a JAR...")
os.system("./dex2jar-0.0.9.15/d2j-dex2jar.sh out.dex")

# Extract the JAR file:
os.system("mv out-dex2jar.jar app.zip")
os.system("unzip app.zip -d app")

# Print result:
print()
print("Your .class files are in the app folder.")
print("You now only have to decompile them using a tool such as JD-GUI.")