class Main:
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

    def find_highest_scenic_score(self):
        size = len(self.array)
        max_score = 0

        def count_view_distance(view_list, element):
            if len(view_list) == 0:
                return 0
            output = [view_list.index(i) for i in view_list if i >= element]
            if len(output) == 0:
                return len(view_list)
            return  output[0] + 1

        for x in range(size):
            for y in range(size):
                element = int(self.array[x][y])
                element_column = [int(i[y] )for i in self.array]
                element_row = [int(i) for i in self.array[x]]
                view_right = element_row[y+1:]
                view_left = element_row[:y]
                view_left.reverse()
                view_up = element_column[:x]
                view_up.reverse()
                view_down = element_column[x+1:]
                
                score = count_view_distance(view_left, element) * count_view_distance(view_right, element) * count_view_distance(view_up, element) * count_view_distance(view_down, element)
                if max_score < score:
                    max_score = score
        print(f'Max Score: {max_score}')

if __name__ == "__main__":
    lesgo = Main(test=False)
    lesgo.print_array()
    lesgo.find_highest_scenic_score()


