class main():
    def __init__(self, test=False):
        TEST = test
        if TEST:
            self.file = 'd8_test.txt'
        else:
            self.file = 'd8.txt'

        self.array = self.read_array()
        
    def read_array(self):
        array = []
        with open(self.file) as f:
            for line in f.readlines():
                line = list(str(line.replace('\n', '')))
                array.append(line)
            if len(array) != len(array[0]):
                raise "Uneven array!"
        return(array)

    def print_array(self):
        print('-----------------------------------')
        for line in self.array:
            print(line)
        print('-----------------------------------')

    def find_uncovered(self, print_map=False):
        size = len(self.array)
        uncovered_array = [['X' for x in range(size)] for y in range(size)]
        count = 0
        for x in range(size):
            for y in range(size):
                element = int(self.array[x][y])
                element_column = [int(i[y] )for i in self.array]
                element_row = [int(i) for i in self.array[x]]

                if x == 0:
                    uncovered_array[x][y] = 'O'
                    count += 1
                    continue
                elif y == 0:
                    uncovered_array[x][y] = 'O'
                    count += 1
                    continue
                elif x == size-1:
                    uncovered_array[x][y] = 'O'
                    count += 1
                    continue
                elif y == size-1:
                    uncovered_array[x][y] = 'O'
                    count += 1
                    continue
                elif element > max(element_row[:y]) or element > max(element_row[y+1:]):
                    uncovered_array[x][y] = 'O'
                    count += 1
                    continue
                elif element > max(element_column[:x]) or element > max(element_column[x+1:]):
                    uncovered_array[x][y] = 'O'
                    count += 1
                    continue
                else:
                    continue
        if print_map:
            for x in uncovered_array:
                print(x)
        print(f'Numer of visible trees: {count}')

if __name__ == "__main__":
    main(test=False).print_array()
    print()
    main(test=False).find_uncovered()


