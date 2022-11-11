def count_b(path):
    counter = 0
    with open(path) as in_file:
        message = in_file.readline()

    for char in message:
        if char == "B":
            counter += 1

    return counter


def write_output(path,counter):
    with open(path, "w") as out_file:
        out_file.write(str(counter))


def main(level):
    path_in = fr"level1\Input\level1_{level}.in"
    path_out = fr"level1\Output\level1_{level}.out"

    counter = count_b(path_in)
    write_output(path_out, counter)
    

if __name__ == "__main__":
    for i in range(1,6):
        main(i)

    
