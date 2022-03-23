import argparse
import sys, os
import hashlib
from tqdm import tqdm
from datetime import datetime

# Initialize parser
parser = argparse.ArgumentParser(description='Hash cracker project for learning Python scripting')
parser.add_argument('-s', action='store', dest='hash', help='Hash as string', required=True)
parser.add_argument('-t', action='store', dest='hashtype', help='Hash type', required=True)
parser.add_argument('-w', action='store', dest='wordlist', help='Wordlist', required=True)
argresults = parser.parse_args()

inputhash = argresults.hash
inputtype = argresults.hashtype
inputwordlist = argresults.wordlist


def md5(word):
	hexhash = hashlib.md5(f"{word}".encode('utf-8')).hexdigest()	# encode and hash word
	return hexhash

def sha256(word):
	hexhash = hashlib.sha256(f"{word}".encode('utf-8')).hexdigest()	# encode and hash word
	return hexhash

def sha512(word):
	hexhash = hashlib.sha512(f"{word}".encode('utf-8')).hexdigest()	# encode and hash word
	return hexhash

def hasher(hash, algtype, wordlist):
	if not os.path.isfile(wordlist):
		print("Wordlist file not found or incorrect permissions")
		exit()
	else:
		print("Reading wordlist...")
		lines = []	# init list
		with open(wordlist, "r") as file:
			for line in file:
				line = line.strip()	# strip newline
				lines.append(line)	# append to list

	if algtype == "md5":
		cracker = md5
	elif algtype == "sha256":
		cracker = sha256
	elif algtype == "sha512":
		cracker = sha512
	else:
		print("No matching hash type found! :(")
		exit()

	start=datetime.now().replace(microsecond=0)	# start timer

	print("The input hash is {}".format(inputhash))
	print("Generating hashes...")
	progbar = tqdm(lines, leave=False)
	for word in progbar:
		hashed = cracker(word)	# launch function
		if hashed == hash:
			print("\nFinished in {}".format(datetime.now().replace(microsecond=0)-start))	# end timer
			print("\nCleartext found! It is:\n{}".format(word))
			progbar.close()
			exit()

if inputhash and inputtype and inputwordlist:
	hasher(inputhash, inputtype, inputwordlist)
