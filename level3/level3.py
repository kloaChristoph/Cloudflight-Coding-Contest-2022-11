def get_alphabet(path):
    alphabet = []
    with open(path) as in_file:
        in_file.readline()
        in_file.readline()
        for line in in_file.readlines():
            if line[0] not in alphabet:
                alphabet.append(line[0])
    return alphabet


def read_message(path, alphabet):
    with open(path) as in_file:
        count = []
        message = in_file.readline()
        for letter in alphabet:
            c=0
            for char in message:
                if char == str(letter):
                    c +=1
            count.append(c)
    return count


def read_dic(path, alphabet):
    with open(path) as in_file:
        in_file.readline()
        in_file.readline()
        count = []
        dic_entries = []

        for line in in_file:
            dic_entries.append(line)
        big_string = "".join(dic_entries)

        message = in_file.readline()
        for letter in alphabet:
            c=0
            for char in big_string:
                if char == str(letter):
                    c +=1
            count.append(c)
    return count


def get_decode(count_message:list[str],count_dic:list[str],alphabet:list[str]):
    count_message_copy = count_message.copy()
    count_message.sort(reverse=True)
    message_letters = []
    decode_dic = {}
    
    for count in count_message:
        index = count_message_copy.index(count)
        message_letters.append(alphabet[index])

    count_dic_copy = count_dic.copy()
    count_dic.sort(reverse=True)
    dic_letters = []
    for count in count_dic:
        index = count_dic_copy.index(count)
        dic_letters.append(alphabet[index])

    for (message_letter, dic_letter) in zip(message_letters,dic_letters):
        decode_dic[message_letter] = dic_letter

    return decode_dic


def sort_dic(decode_dic:dict, alphabet):
    sorted_dic = {}
    for char in alphabet:
        sorted_dic[char] = decode_dic.get(char)
    
    return sorted_dic


def format_output(path:str, sorted_dic:dict, alphabet:list[str]):
    with open(path, "w") as out_file:
        for char in alphabet:
            out_file.write(f"{char} {sorted_dic.get(char)}\n")

            
def main(level):
    path_in = fr"coding_contest_2022_11/Input/level3_{level}.in"
    path_out = fr"coding_contest_2022_11/Output/level3_{level}.out"
    alphabet = get_alphabet(path_in)
    count_message = read_message(path_in,alphabet)
    count_dic = read_dic(path_in,alphabet)

    decode_dic = get_decode(count_message, count_dic, alphabet)
    sorted_dic = sort_dic(decode_dic, alphabet)
    format_output(path_out, sorted_dic, alphabet)   

    
if __name__ == "__main__":
    for i in range (5):
        main(i+1)