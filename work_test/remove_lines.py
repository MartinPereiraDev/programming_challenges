def remove_line_breaks(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            content = file.read()

        # Remove line breaks
        content = content.replace('\n', '').replace('\r', '')

        with open(output_file, 'w') as file:
            file.write(content)

        print(f"Line breaks removed and saved to '{output_file}'.")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
input_file = r'C:\Users\Administrador\workspace\Python\retosProgramacion\work_test\text_decode.txt'
output_file = r'C:\Users\Administrador\workspace\Python\retosProgramacion\work_test\text_decode2.txt'
remove_line_breaks(input_file, output_file)