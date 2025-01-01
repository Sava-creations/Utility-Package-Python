def read_file(file_name):
    """Read the contents of a file."""
    with open(file_name, 'r') as file:   #this automatically closes the file instead file = open(file_name, 'w') file.close()
        return file.read()

def write_file(file_name, content):
    """Write content to a file."""
    with open(file_name, 'w') as file:
        file.write(content)
    return f"File '{file_name}' written successfully."

def append_to_file(file_name, content):
    """Append content to a file."""
    with open(file_name, 'a') as file:
        file.write(content)
    return f"Content appended to '{file_name}' successfully."


