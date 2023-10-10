def tests():
    string = "Python\n"
    string_binary = []
    for c in string:
        string_binary.append(format(ord(c), 'b'))
    binary_converted = ' '.join(string_binary)
    print("The Binary Representation is:", binary_converted)

    string_car = []
    for binary in string_binary:
        string_car.append(chr(int(binary, 2)))

    print("Bin to ASCII:", "".join(string_car))

    hexa = hex(65189)
    print("tests int to hexa", hexa)
    print("tests hexa to int", int(hexa, 16))

def generate_file():
    first_address = 1

def convert_char_to_binary(char):
    return format(ord(char), 'b')

def convert_str_to_binary(string):
    string_binary = []
    for c in string:
        string_binary.append(convert_char_to_binary(c))
    return string_binary

def convert_int_to_hex(int):
    return hex(int)

def load_tab_from_file(file_name):
    filein = open(file_name, "r")
    lines = filein.readlines()
    filein.close()
    return lines

def write_line_in_fich(fileout, address, string_content):
    string_content_binary = convert_str_to_binary(string_content)
    fileout.write(convert_int_to_hex(address)+":"+" ".join(string_content_binary)+"\n")

def write_tab_in_fich(fileout, start_address, lines):
    next_address = start_address
    for line in lines :
        write_line_in_fich(fileout, next_address, line)
        next_address+=1
    return next_address

def generate_data_file_addressbinary(data_files, file_out_name):
    fileout = open(file_out_name, 'w')
    next_address = 1
    for file_name in data_files:
        data_to_add = [file_name] + load_tab_from_file(file_name)
        next_address = write_tab_in_fich(fileout, next_address, data_to_add)
    fileout.close()

generate_data_file_addressbinary(["a-ma-femme-endormie.txt", "musique_favs.txt", "mypasswords.txt", "note_de_cours.txt", "films_favs.txt"], "data.txt")