import random
import os

def read_names(names_file_name):
    with open(names_file_name, 'r') as names_file:
        names = names_file.readlines()
        for name_index in range(len(names)):
            names[name_index] = names[name_index].replace('\n', '')
    return names


def mix_names(names):
    pairs = []; taken = []
    for name_index in range(0, len(names)):
        pair = name_index
        while pair == name_index or pair in taken:
            pair = random.randint(0, len(names)-1)
        taken.append(pair)
        pairs.append((names[name_index], names[pair]))
    return pairs


def save_file(pair):
    results_dir = '.\\results'
    if not os.path.exists(results_dir):
        os.mkdir(results_dir)

    file_name = f"Od {pair[0]} prezent otrzyma"
    with open(f'{results_dir}\\{file_name}', 'w') as f:
        f.write(pair[1])


if __name__ == "__main__":
    def main():
        names = read_names("imiona.txt")
        pairs = mix_names(names)
        for pair in pairs:
            save_file(pair)
    main()
