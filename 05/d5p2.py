TEST = False
if TEST:
    NUMBER_OF_LINES = 3
    FILE = 'd5_test.txt'
else:
    NUMBER_OF_LINES = 8
    FILE = 'd5.txt'

def sort_payload(payload):
    CRANE_CAP = 3
    size = len(payload)
    splits = int((size - size%CRANE_CAP)/CRANE_CAP)
    last_part = size%CRANE_CAP
    output = []
    for i in range(0, size, CRANE_CAP):
        output = payload[i:i + CRANE_CAP] + output
    return output

def read_blueprint(number_of_lines):
    with open(FILE) as f:
        line_count = 1
        array = []

        for line in f.readlines():
            line = line.replace('\n', '')
            line = line.replace('    ', ' [x]')
            line = line.replace(' ', '')
            n=3
            line = [line[i:i+n] for i in range(0, len(line), n)]
            array.append(line)
            line_count += 1
            if line_count > number_of_lines:
                break
            
        f.close()
    
    array = [*zip(*array)]
    array = [list(x) for x in array]

    for element in array:
        while '[x]' in element:
            try:
                element.remove('[x]')
            except ValueError:
                pass
    return array


def process_instructions(number_of_lines, array):
    with open(FILE) as f:
        line_count = 1
        step = 0
        for line in f.readlines():
            if line_count < number_of_lines+3:
                line_count += 1
                continue
            step += 1
            line = line.replace('move ', '')
            line = line.replace('from ', '')
            line = line.replace('to ', '')
            line = line.replace('\n', '')
            input = line.split(' ')

            number = int(input[0])
            source = int(input[1])-1
            destination = int(input[2])-1
            
            print('Input list')
            print(array[source])
            print(array[destination])

            payload = array[source][:number]
            # payload.reverse()
            payload = sort_payload(payload)
            array[source] = array[source][number:]
            array[destination] = payload + array[destination]
            print(f'Payload: {payload}')
            # Expected: NSBZVPWLRCH
            print('Output')
            print(array[source])
            print(array[destination])
            print('------------')
            print(f'Step nr: {step} | Result:')
            for line in array:
                print(line)
            print('-------------')
            print('')
            if step == 4:
                break
            
        try: 
            result = ''.join([x[0] for x in array if len(x) > 0])
        except:
            pass
        result = result.replace('[', '')
        result = result.replace(']', '')
        print(f'Final result: {result}')
        f.close()


if __name__ == "__main__":
    blueprint = read_blueprint(NUMBER_OF_LINES)
    process_instructions(NUMBER_OF_LINES, blueprint)