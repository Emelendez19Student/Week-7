def main():
    # Prompt the user for a filename
    filename = input("Enter the filename: ")

    try:
        # Read the lines from the file into a list
        with open(filename, 'r') as files:
            lines = file.readlines()
    except FileNotFoundError:
        print("File not found.")
        return

    num_lines = len(lines)

    while True:
        # Print the number of lines in the file
        print(f"\nThe file '{filename}' has {num_lines} lines.")

        # Prompt the user for a line number
        line_num_input = input("Enter a line number (1 to {}), or 0 to quit: ".format(num_lines))

        # Check if the input is '0' to quit
        if line_num_input == '0':
            print("Exiting the program.")
            break

        try:
            line_num = int(line_num_input)
            if 1 <= line_num <= num_lines:
                # Print the line associated with the line number
                print("Line {}: {}".format(line_num, lines[line_num - 1].strip()))
            else:
                print("Invalid line number. Please enter a number between 1 and {}.".format(num_lines))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
