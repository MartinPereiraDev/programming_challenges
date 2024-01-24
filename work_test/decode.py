def decode(message_file):
    # Read the contents of the file
    with open(message_file, 'r') as file:
        lines = file.readlines()

    # Initialize a dictionary to store pyramid lines
    pyramid_lines = {}

    # Parse the lines and build the pyramid_lines dictionary
    for line in lines:
        line = line.strip().split()
        num = int(line[0])
        word = line[1]
        pyramid_lines[num] = word

    # Find the maximum number in the pyramid
    max_num = max(pyramid_lines.keys())

    # Extract words based on the pyramid structure
    message_words = [pyramid_lines[i] for i in range(1, max_num + 1)]

    # Join the words to form the decoded message
    decoded_message = ' '.join(message_words)

    return decoded_message


message_file = r'C:\Users\Administrador\workspace\Python\retosProgramacion\work_test\text_decode.txt'
result = decode(message_file)
print(result)