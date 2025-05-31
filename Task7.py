def read_file_line_by_line(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.rstrip())  # rstrip to remove trailing newline
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point
myfile = input("Enter the file text : ")
read_file_line_by_line(myfile)
