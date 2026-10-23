def num_to_bin_str(num, bits_length=None):
	if bits_length == None:
		return bin(num)[2:]
	else:
		rnum = bin(num)[2:]
		len_diff = bits_length - len(rnum)
		if len_diff > 0:
			for _ in range(len_diff):
				rnum = "0" + rnum
			return rnum
		else:
			return rnum[:bits_length]

def append_str(filename, string):
	with open(filename, "ab") as f:
		for num in [string[i:i+8] for i in range(0, len(string), 8)]: #This line was bought to you by OpenAI
			f.write(int(num, 2).to_bytes(1, "big"))