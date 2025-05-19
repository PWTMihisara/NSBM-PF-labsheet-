def read_line(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"The file at {file_path} does not exist.")

read_line("Output.txt")