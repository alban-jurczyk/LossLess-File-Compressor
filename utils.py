def num_to_bin_str(num, bits_length=None):
	if bits_length == None:
		return bin(num)[2:]
	else:
		return bin(num)[2:bits_length+2]

def append_str(filename, string):
	with open(filename, "wb") as f:
		for num in [string[i:i+8] for i in range(0, len(string), 8)]:
			f.write(int(num, 2).to_bytes(8, "big"))