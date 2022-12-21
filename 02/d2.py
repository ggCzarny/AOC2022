def result(game):
    score = 0
    match game:
        
        case "AX": score = 4 # rock rock drwa 3+1
        case "AY": score = 8 # rock paper win 6+2
        case "AZ": score = 3 # rock scisors loss 0+3

        case "BX": score = 1 # paper rock loss 0+1
        case "BY": score = 5 # paper paper draw 3+2
        case "BZ": score = 9 # paper scisors win 6+3

        case "CX": score = 7 # scisors rockwin 6+1
        case "CY": score = 2 # scisors paper loss 0+2
        case "CZ": score = 6 # scisors scisors draw 3+3
    return score
        
def main():
    with open("d2.txt") as f:
        games =[]
        for line in f.readlines():
            games.append(line.replace('\n', '').replace(' ', ''))
        f.close()
    score = 0
    for game in games:
        score += result(game)
    print(score)

if __name__ == "__main__":
    main()