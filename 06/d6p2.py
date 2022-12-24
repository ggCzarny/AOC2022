TEST = False

if TEST == True:
    result = [19, 23, 23, 29, 26]
    file = 'd6_test.txt'
else:
    file = 'd6.txt'



def main():
    with open(file) as f:
        for line in f.readlines():
            line = line.replace('\n', '')
            for i in range(0, len(line)):
                part = line[i:i + 14]
                part_set = set(part)
                if len(part_set) == len(part):
                    print(f'Mamy to: {i+14}')
                    break
            


if __name__ == "__main__":
    main()
