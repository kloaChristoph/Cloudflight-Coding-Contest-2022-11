def get_alphabet(path:str) -> list[str]:
    alphabet = []
    with open(path) as in_file:
        in_file.readline()
        for line in in_file.readlines():
            if line[0] not in alphabet:
                alphabet.append(line[0])
    return alphabet


def count_alphabet(path:str, alphabet:list[str]) -> list:
    counts = []

    for char in alphabet:
        counter = 0
        with open(path) as in_file:
            in_file.readline()
            for line in in_file.readlines():
                counter += line.count(char)

        counts.append(counter)
    
    return counts


def format_output(path:str, counts:list[int]):
    with open(path, "w") as out_file:
        for count in counts:
            out_file.write(f"{str(count)}\n")

            
def main(level):
    path_in = fr"level2/Input/level2_{level}.in"
    path_out = fr"level2/Output/level2_{level}.out"

    alphabet = get_alphabet(path_in)
    counts = count_alphabet(path_in, alphabet) 
    format_output(path_out, counts)

    
if __name__ == "__main__":
    main("example")
    for i in range (5):
        main(i+1)