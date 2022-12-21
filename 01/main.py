def main():
    with open("input.txt") as f:
        elfs = []
        elf_count = 0
        
        for line in f.readlines():
            
            try:
                line = int(line.replace('\n', ''))
            except ValueError:
                line = None
            if line != None:
                elf_count += line
            elif line == None:
                elfs.append(elf_count)
                elf_count = 0
        elfs.append(elf_count)
        elfs.sort()
        print(sum(elfs[-3:]))
        f.close()

if __name__ == "__main__":
    main()