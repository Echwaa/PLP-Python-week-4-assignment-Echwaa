# CREATING, MODIFYING, READING AND CLOSING FILE

def modify_content(content):
    # Example modification: convert to uppercase
    return content.upper()

def main():
    filename = input("Enter the filename to read: ")
    try:
        with open(filename, "r") as file:
            content = file.read()
        modified_content = modify_content(content)
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)
        print(f"Modified content has been written to {new_filename}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: Could not read the file '{filename}'.")

if __name__ == "__main__":
    main()
