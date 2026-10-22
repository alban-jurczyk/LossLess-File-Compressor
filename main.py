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
					byte_length = power
					break

			comp_part = ""

			with open(CMP_FILE_PATH, "ab") as fcmp:
				comp_part += "0"*16
				comp_part += utils.num_to_bin_str(power, 5)

				for n in res:
					comp_part += utils.num_to_bin_str(n, power)

			utils.append_str(CMP_FILE_PATH, comp_part)

		with open(CMP_FILE_PATH, "ab") as fcmp:
			for n in global_table:
				if n is not None:
					fcmp.write(n.to_bytes(2, "big"))
				else:
					fcmp.write(int("0").to_bytes(2, "big"))

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
