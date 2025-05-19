def copy_file(source_path, destination_path):
    try:
        with open(source_path, 'r') as sfile:
            contents = sfile.read()
        with open(destination_path, 'w') as dfile:
            dfile.write(contents)
        print(f"Content copied from {source_path} to {destination_path}")
    except FileNotFoundError:
        print(f"The file at {source_path} does not exist.")

copy_file("Output.txt", "Output_1.txt")