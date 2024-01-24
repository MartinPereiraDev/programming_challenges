
#function decode message 
def decode(message_file):
    try:
        # Read the contents of the file open and read 
        with open(message_file, 'r') as file:
            lines = file.readlines()


        # Initialize a dictionary to store pyramid lines
        pyramid_lines = {}

        # Parse the lines and build the pyramid_lines dictionary
        for line_number, line in enumerate(lines, start=1):
            line = line.strip().split()
            
            # Ensure the line has at least two elements if not send message error
            if len(line) >= 2:
                try:
                    num = int(line[0])
                    word = line[1]
                    pyramid_lines[num] = word
                except ValueError:
                    print(f"Error: Unable to convert '{line[0]}' to an integer on line {line_number}.")
            else:
                print(f"Error: Line {line_number} does not have enough elements.")

        # Find the maximum number in the pyramid with function max()
        max_num = max(pyramid_lines.keys())

        # Extract words based on the pyramid structure 
        message_words = [pyramid_lines[i] for i in range(1, max_num + 1)]

        # Join the words to form the decoded message
        decoded_message = ' '.join(message_words)

        return decoded_message

    except FileNotFoundError:
        print(f"Error: File '{message_file}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Path text file in the case is path of me PC, adjust parameters 
message_file = r'C:\Users\Administrador\workspace\Python\retosProgramacion\work_test\text_decode.txt'

# result call function and save message into variable 
result = decode(message_file)

# if check result not is empty, if result not is empty print() message decode
if result is not None:
    print(result)