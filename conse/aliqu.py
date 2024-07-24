# Example dictionary containing locale information
locale_info = {
    "offset": 100  # example offset value
}

# Open a file in binary read mode
with open('example_file.bin', 'rb') as file:
    # Seek to the position specified by the offset in the dictionary
    file.seek(locale_info["offset"])
    
    # Read some data from this position (for example, 10 bytes)
    data = file.read(10)
    
    # Print the data or process it as needed
    print(data)
