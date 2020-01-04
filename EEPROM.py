import os
from smbus2 import SMBus
from time import sleep
import code

def charArrayToString(array):
	# print(array)
	return ''.join([chr(x) for x in array ])

def stringToByteArray(mystring):
	return bytearray(mystring,'UTF-8')
	# return list(bytes(mystring,"UTF-8"))

# MUST RIGHT IN MAX CHUNKS OF 16 CHARS?
# Default to writing from the beginning
def writeEEPROMlocation(mydata,location=0):
	if len(mydata) > 16:
		print("Data of length ({}) is greater than max, 16.".format(len(mydata) ) ) 
		return False
	with SMBus(1) as bus:
			data = bus.write_i2c_block_data(addr, location, stringToByteArray(mydata) )
	sleep(0.2)
	sanity = readEEPROMlocation(location,len(mydata))
	sleep(0.2)
	if sanity != mydata:
		print("Possible write/read error! %s --> %s" %(mydata,sanity))
		return False

	return True

# MUST READ IN MAX CHUNKS OF 32 CHARS
def readEEPROMlocation(location,length):
	with SMBus(1) as bus:
		data = bus.read_i2c_block_data(addr, location, length )
		d = charArrayToString(data)
		return d

# Each writable chunk is 16 chars
def zeroEEPROMchunk(location):
	writeEEPROMlocation(''.join(['0']*16),location)

def zeroManyChunks(location,num):
	for i in range(0,num):
		zeroEEPROMchunk(location+(16*i))

def readManyChunks(location,num):
	bunch = []
	for i in range(0,num):
		bunch.append(readEEPROMlocation(i*32,32) )
	return bunch

def writeManyChunks(location,chunkarray):
	# writeEEPROMlocation
	loc = 0
	for c in chunkarray:
		writeEEPROMlocation(c,loc)
		loc += len(c)

	pass


addr=0x50


code.interact(local=locals())