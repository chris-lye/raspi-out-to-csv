# specify original file path: if path is in the same folder, simply put its name with extension
path_to_original = "XXXX.out"
# open the text file, 'r' is reading mode
original_file = open(path_to_original, 'r')
# if the file does not exist, open() creates a new file. 'a' is append mode. the write mode 'w' would overwrite
# everything, so we use append.
output_file = open("XXXX.csv", 'a')

# start copying over the files to a dictionary
original_lines = original_file.readlines()
dictionary = {}
key = None
for line in original_lines:
    if line[0] == "-":
        processed_line = line[2:-1]  # to exclude the "\n" and the "- " at the start
        dictionary[key].append(processed_line)
    else:
        key = line[0:-2]
        dictionary[key] = []  # a line starting with a string represents a new header

# remove any key-value pairs with empty values
for key in list(dictionary.keys()):
    if len(dictionary[key]) == 0:
        del dictionary[key]

# write the first line of headers
header = ""
for key, value in dictionary.items():
    header += key + ","
header = header[:-1]
header += "\n"
output_file.write(header)

# for checking
for key, value in dictionary.items():
    print(len(value))
    
# write the rest of the rows
dict_keys = list(dictionary)
key_1 = dict_keys[0]  # all empty key-value pairs have been removed, this is safe
i = 0
while i < len(dictionary[key_1]):
    row = ""
    for key, value in dictionary.items():
        row += value[i] + ","
    row = row[:-1]
    row += "\n"
    output_file.write(row)
    i += 1
# close the files to prevent errors
original_file.close()
output_file.close()
