from collections import defaultdict

def part1(input):
	filesystem = parse_filesystem(input)
	result = find_total_w_restriction(filesystem)
	return result

def part2(input):
	filesystem = parse_filesystem(input)
	result = find_directory_to_delete(filesystem)
	return result


# HELPER FUNCTIONS

def parse_filesystem(input):
	filesystem = defaultdict(int)
	stack = []
	for command in input:
		if command.startswith("$ ls") or command.startswith("dir"):
			continue
		elif command.startswith("$ cd"):
			dest = command.split()[2]
			if dest.startswith(".."):
				stack.pop()
			else:
				if stack:
					path = stack[-1] + "_" + dest
				else:
					path = dest
				stack.append(path)
		else:
			size = command.split()[0]
			for path in stack:
				filesystem[path] += int(size)
	return filesystem

def find_total_w_restriction(filesystem):
	restriction = 100000
	total = 0
	for aggr_size in filesystem.values():
		if aggr_size < restriction:
			total+= aggr_size
	return total

def find_directory_to_delete(filesystem):
	total_disk_space = 70000000
	reqd_unused_space = 30000000
	free_space_reqd = reqd_unused_space - (total_disk_space - filesystem["/"])

	for size in sorted(filesystem.values()):
		if size > free_space_reqd:
			break
	return size