from mnemonic import Mnemonic
import binascii

import shamir_mnemonic as shamir
from shamir_mnemonic import MnemonicError

from pprint import pprint
import code

import hashlib
import sys

import pandas

# Take the hash of any old random file
# filename = input("Enter the input file name: ")
sha256_hash = hashlib.sha256()
with open(filename,"rb") as f:
	# Read and update hash string value in blocks of 4K
	for byte_block in iter(lambda: f.read(4096),b""):
		sha256_hash.update(byte_block)
	print(sha256_hash.hexdigest())

m = Mnemonic("english")

# entropy string
# entropy = b'hello123hello123'
# bytes of data must be 32 character

# data = binascii.hexlify(b'hello123hello123')\
print(sha256_hash.digest() )
# print(len(sha256_hash.digest()))
# data = binascii.hexlify(sha256_hash.digest())
data = binascii.hexlify(sha256_hash.hexdigest().encode('UTF-8')[0:16])
print(sys.getsizeof(data))
# len(m.to_mnemonic(data).split(' '))


# Create the mnemonic seed from the entropy data
MS = m.to_mnemonic(data)


# Print out the seed with numbers
# print(MS)
print(f"COPY SEED: {MS}")
msp = MS.split(' ')
wl = pandas.read_csv('english.txt',header=None)
wll = wl.reset_index().set_index(0)
for word in msp:
	print(f'{wll.index.get_loc(word)}: {word} ')


for i in range(0,len(msp)):
	print(f'{i+1}: {msp[i]}')
print("\n\n")

# Compress the seed to make shamirs use less words 
MS_short = ''.join(list(map(lambda x: x[0:4], msp)))
# MS_short += " "

# MS_short = MS_short
print(f"Short: LEN: {len(MS_short)}: {MS_short}")
# MS = MS.encode('UTF-8')


mnemonics = shamir.generate_mnemonics(1, [(3, 5)], MS_short.encode('UTF-8'))
# print(mnemonics)
print(f"{len(mnemonics[0])}: SNACKS Created")
for i in range(0,len(mnemonics[0])) :
	print(f"SNACK: {i+1}:\n{mnemonics[0][i]}\n")

print(shamir.combine_mnemonics(mnemonics[0][0:3]))


# Split shamir into pieces of 16 chars 
a = mnemonics[0][0]
n = 16
split_shamir_eeprom = [a[i:i+n] for i in range(0,len(a),n)]
# TODO: Integrate EEPROM Driver Here
# writeEEPROMlocation(split_shamir_eeprom[i],i*16)
# readEEPROMlocation(0,32)

# Decompress the seed back to list of 24 words 
MS_short = ''.join(list(map(lambda x: x[0:4], msp)))
# MS_short += " "
code.interact(local=locals())