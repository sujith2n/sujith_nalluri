def main():
    filename = "output.txt"

    # Step 1: Write user input to the file
    text_to_write = input("Enter text to write to the file: ")
    with open(filename, "w") as file:
        file.write(text_to_write + "\n")
    print("Data successfully written to output.txt.\n")

    # Step 2: Append additional user input
    text_to_append = input("Enter additional text to append: ")
    with open(filename, "a") as file:
        file.write(text_to_append + "\n")
    print("Data successfully appended.\n")

    # Step 3: Read and display the final content
    print("Final content of output.txt:")
    with open(filename, "r") as file:
        for line in file:
            print(line.rstrip())

if __name__ == "__main__":
    main()
