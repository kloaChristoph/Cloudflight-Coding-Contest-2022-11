def get_data(path):
    message = ""
    dictionary:list[str] = []
    decrypt_tables:list[dict] = []

    with open(path) as in_file:
        #get message
        message = in_file.readline().split("\n")[0]

        #get dictionary
        dict_count = int(in_file.readline())

        for count in range(dict_count):
            entry = in_file.readline().split("\n")[0]
            dictionary.append(entry)

        #get decrypt tables 
        table_data = in_file.readline().split(" ")
        table_count = int(table_data[0])
        line_count = int(table_data[1])

        for table in range(table_count):
            table_id = int(in_file.readline())
            decrypt_tables.append({})

            for line in range(line_count):
                entry = in_file.readline().split(" ")
                key = entry[0]
                value = entry[1].split("\n")[0]
                decrypt_tables[table_id].update({key : value})
                
    return message, dictionary, decrypt_tables


def decrypt_message(message:str, decrypt_table: dict):
    new_message = ""
    for char in message:
        if char == " ":
            new_message += char
        else:
            new_char = decrypt_table.get(char)
            new_message += new_char
    return new_message


def check_message(decrypted_message_str:str, dictionary:list[str]):
    decrypted_message = decrypted_message_str.split(" ")
    for word in decrypted_message:
        if word not in dictionary:
            return False
    return True


def format_output(path:str, table_id:int):
    with open(path,"w") as out_file:
        out_file.write(str(table_id))

        
def main(level):
    path_in = fr"level4/Input/level4_{level}.in"
    path_out = fr"level4/Output/level4_{level}.out"
    message, dictionary, decrypt_tables = get_data(path_in)
    
    for table_id in range(len(decrypt_tables)):
        decrypted_message = decrypt_message(message, decrypt_tables[table_id])
        check = check_message(decrypted_message, dictionary)
        if check == True:
            correct_table = table_id
            format_output(path_out,correct_table)
            break
        

if __name__ == "__main__":
    main("example")
    for i in range (5):
        main(i+1)
    