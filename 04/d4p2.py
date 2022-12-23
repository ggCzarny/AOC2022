import numpy as np

def main():
    list = np.arange(0, 100000, 1)
    count = 0
    with open("d4.txt") as f:
        for line in f.readlines():
            line = line.replace('\n', '')
            fs = int(line.split(',')[0].split('-')[0]) #first start 
            fe = int(line.split(',')[0].split('-')[1]) #first start 

            ss = int(line.split(',')[1].split('-')[0]) #first start 
            se = int(line.split(',')[1].split('-')[1]) #first start 

            list1 = list[fs:fe+1]
            list2 = list[ss:se+1]
            if set(list1).intersection(list2):
                count += 1
        f.close()
        print(count)

if __name__ == "__main__":
    main()