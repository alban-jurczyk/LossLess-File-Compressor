def part_compressor(bytes, redundancy_table):
	for num in bytes:
		if not num in redundancy_table:
			redundancy_table.append(num)

	comp_part = []
	for num in bytes:
		comp_part.append(redundancy_table.index(num))

	return comp_part, redundancy_table

def part_decompressor(bits, bits_length, redundancy_table):
	sliced = [bits[i:i+bits_length] for i in range(0, len(bits), )] #I can confidently say I have a lot of creativity when finding names
	
	decomp_part = ""

	for byte in sliced:
		print(byte)
		print(int(byte, 2))
		decomp_part += str(redundancy_table[int(byte, 2)])

	return decomp_part