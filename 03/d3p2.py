def priori_num(char):
    if ord(char) > 96:
        return ord(char) - 96
    else:
        return ord(char) - 65 + 27

def IntersecOfSets(group):
    # Converting the arrays into sets
    s1 = set(group[0])
    s2 = set(group[1])
    s3 = set(group[2])
      
    # Calculates intersection of 
    # sets on s1 and s2
    set1 = s1.intersection(s2)         #[80, 20, 100]
      
    # Calculates intersection of sets
    # on set1 and s3
    result_set = set1.intersection(s3)
      
    # Converts resulting set to list
    final_list = list(result_set)
    
    return final_list

def main():
    with open("d3.txt") as f:
        duplicates = []
        groups = []
        group = []
        counter = 1
        for line in f.readlines():
            group.append(list(line.replace('\n', '')))

            if counter == 3:
                groups.append(group)
                group = []
                counter = 0
            
            counter += 1
        result = 0
        for group in groups:
            result += priori_num(IntersecOfSets(group)[0])
        
        print(result)
        f.close()



if __name__ == "__main__":
    main()