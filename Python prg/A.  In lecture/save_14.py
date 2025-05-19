def append_file(file_path, content):
    try:
        with open(file_path, 'a') as file:
            file.write(content)
            print(f"Content append to {file_path}.")
    except FileNotFoundError:
        print(f"The file at {file_path} does not exist.")

append_file("Output.txt", "\n The new content.")