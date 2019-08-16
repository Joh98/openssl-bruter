#!/usr/bin/python3

import subprocess

path = INSERT YOUR PASSWORD LIST HERE
counter = 0
previousLine = ''

cipher_list = [
	'AES-128-CBC',
	'AES-128-CBC-HMAC-SHA1',
	'AES-128-CBC-HMAC-SHA256',
	'id-aes128-CCM',
	'id-aes128-GCM',
	'id-aes192-CCM',
	'id-aes192-GCM',
	'id-aes256-CCM',
	'id-aes256-GCM',
	'id-aes256-wrap',
	'id-aes256-wrap-pad',
	'id-smime-alg-CMS3DESwrap',
	'rc2',
	'rc2-128',
	'rc2-40',
	'RC2-40-CBC',
	'rc2-64',
	'RC2-64-CBC',
	'RC2-CBC',
	'RC2-CFB',
	'RC2-ECB',
	'RC2-OFB',
	'RC4',
	'RC4-40',
	'RC4-HMAC-MD5',
	'seed',
	'SEED-CBC',
	'SEED-CFB',
	'SEED-ECB',
	'SEED-OFB',
	'sm4',
	'SM4-CBC',
	'SM4-CFB',
	'SM4-CTR',
	'SM4-ECB',
	'SM4-OFB']


subprocess.call("rm suggestions.txt", shell=True)

for cipher in cipher_list:

	subprocess.call("echo " + cipher + " >> output.txt | bruteforce-salted-openssl -t 10 -1 -d md5 -N -f " + path + " -c "
					+ cipher + " INSERT NAME OF ENNCRYPTED FILE >> output.txt 2>/dev/null", shell=True)


subprocess.call("clear", shell=True)

with open("output.txt", 'r') as unparsed, open('suggestions.txt', 'w+') as parsed:

	parsed.write("\n*****CIPHER & PASSWORD SUGGESTIONS*****\n")

	for line in unparsed:

		if line.startswith("Password"):

			if previousLine.startswith("Password"):
				pass

			else:
				parsed.write("\n \n" + previousLine + "\n" + line)

		previousLine = line

	parsed.write("\n")

unparsed.close()
parsed.close()

subprocess.call("rm output.txt; cat suggestions.txt", shell=True)

