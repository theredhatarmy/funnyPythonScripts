def convert_text_file(input_file, output_file):
    try:
        # Open the input file for reading
        with open(input_file, 'r') as file:
            # Read the content of the input file
            content = file.read()

        # Open the output file for writing
        with open(output_file, 'w') as file:
            # Write the content to the output file
            file.write(content)

        print("File conversion successful!")

    except FileNotFoundError:
        print("Input file not found!")

    except:
        print("An error occurred during file conversion.")

# Usage example
input_file = "input.txt"
output_file = "output.txt"

convert_text_file(input_file, output_file)
