import helper

def read_input(input_file):
	parsed_data = input_file.readlines()
	for index in range(len(parsed_data)):
		parsed_data[index] = parsed_data[index].replace("\n", "")
	return parsed_data


if __name__=="__main__":
	config = input("Demo or actual? [demo/actual]:")
	input = open("input.txt", "r") if config == "actual" else \
	open("demo_input.txt", "r")
	
	parsed_data = read_input(input)
	result = helper.part2(parsed_data)
	print(result)