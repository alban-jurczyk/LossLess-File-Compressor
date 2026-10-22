def compress(FILE_PATH):
	from part_comp import part_compressor
	import utils as utils

	CMP_FILE_PATH = FILE_PATH+".cmp"
	with open(CMP_FILE_PATH, "w"):
		pass

	CHUNK = 1024   # 1 KiB

	global_table = [None]
	with open(FILE_PATH, "rb") as f:
		while True:
			part = f.read(CHUNK)
			if not part:
				break
			res, global_table = part_compressor(part, global_table)

			maximum = len(global_table)-1
			for power in range(16):
				if 2**power >= maximum:
					bit_length = power
					break

			with open(CMP_FILE_PATH, "ab") as fcmp:
				fcmp.write(bit_length.to_bytes(2, "big"))

			comp_part = ""
			for n in res:
				comp_part += utils.num_to_bin_str(n, bit_length)

			utils.append_str(CMP_FILE_PATH, comp_part)
			with open(CMP_FILE_PATH, "ab") as fcmp:
				fcmp.write((0).to_bytes(2, "big"))


		with open(CMP_FILE_PATH, "ab") as fcmp:
			for n in global_table:
				if n is not None:
					fcmp.write(n.to_bytes(2, "big"))
	print(global_table[1:])

def decompress(FILE_PATH):
	import utils as utils

	read_steps = 1
	table_start_idx = 0
	checkpoints = []
	with open(FILE_PATH, "rb") as f:
		address = -read_steps
		table_start_idx = 0
		last_was_zero = False
		while True:
			part = f.read(read_steps)
			address += read_steps
			if not part:
				break

			if part[0] == 0:
				if last_was_zero:
					table_start_idx = address
					checkpoints.append(address)
					if len(checkpoints)>=2 and checkpoints[-2] == address-1:
						checkpoints.pop(-2)
				else:
					last_was_zero = True
			else:
				last_was_zero = False
					
	global_table = []
	with open(FILE_PATH, "rb") as f:
		f.seek(table_start_idx)
		while True:
			raw = f.read(2)
			if not raw:
				break

			if len(raw) >= 2:
				num = int(utils.num_to_bin_str(raw[0], 8) + utils.num_to_bin_str(raw[1], 8), 2)
			else:
				num = raw[0]

			global_table.append(num)
	print(global_table)
	print(checkpoints)



if __name__ == "__main__":
	from sys import argv

	try:
		assert len(argv) >= 2
	except AssertionError:
		print("Missing argument. Requires Filename")
		print("	Usage : main [filename] [passes]")
		print("	[filename] path to the file you want to compress")
		#print("	[passes] maximum number of time you want to compress he file.\n	Leaving it blank compresses the maximum amount of times")

	compress(argv[1])
	decompress(argv[1]+".cmp")


