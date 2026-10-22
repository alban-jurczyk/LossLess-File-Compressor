def part_compressor(bytes, redundancy_table):
	for num in bytes:
		if not num in redundancy_table:
			redundancy_table.append(num)

	comp_part = []
	for num in bytes:
		comp_part.append(redundancy_table.index(num))

	return comp_part, redundancy_table