def find_winner(c1, c2) -> str:
    if c1 == c2:
        return c1
    if c1 == "R" and c2 == "S" or c1 == "R" and c2 == "L":
        return c1
    if c1 == "S" and c2 == "P" or c1 == "S" and c2 == "L":
        return c1
    if c1 == "P" and c2 == "R" or c1 == "P" and c2 == "Y":
        return c1
    if c1 == "Y" and c2 == "R" or c1 == "Y" and c2 == "S":
        return c1
    if c1 == "L" and c2 == "P" or c1 == "L" and c2 == "Y":
        return c1
    return c2

def printer(match_string:str) -> str:
    output = ""
    i = 0

    while i < len(match_string):
        output += match_string[i]
        output += match_string[i + 1]
        output += " "
        i += 2

    print(output)


if __name__ == "__main__":
    while 1:
        match_string = input("Match: ")
        match_string = match_string.replace(" ", "")

        while len(match_string) != 1:
            printer(match_string)
            new_match_string = ""

            i = 0
            while i < len(match_string):
                new_match_string += find_winner(match_string[i], match_string[i + 1])
                i += 2

            match_string = new_match_string

        print(match_string)



