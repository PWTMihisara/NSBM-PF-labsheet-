def write_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
            print(f"Content written to {file_path}.")
    except FileNotFoundError:
        print(f"The file at {file_path} does not exist.")

write_file("Output.txt", "Python is easy to learn.")