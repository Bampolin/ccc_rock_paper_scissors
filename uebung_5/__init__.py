import math


def read_file(file_name) -> list[str]:
    list_of_lines = []
    with open(file_name, 'r') as f:
        f.readline()
        for line in f:
            list_of_lines.append(line.strip())

    return list_of_lines


def write_file(file_name, data: list[str]):
    with open(file_name, 'w') as f:
        for line in data:
            f.write(line + "\n")


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


def play_tournament(matches_str: str) -> str:
    next_round = []
    for i in range(0, len(matches_str), 2):
        next_round.append(f"{matches_str[i]}{matches_str[i + 1]}")
    winners = []

    for _ in range(2):
        winners = []
        for i in next_round:
            winners.append(find_winner(i[0], i[1]))
        next_round = []
        for i in range(0, len(winners), 2):
            next_round.append(f"{winners[i]}{winners[i + 1]}")

    return "".join(winners)


def play_full_tournament(matches_str: str) -> str:
    erg = play_tournament(matches_str)

    while len(erg) > 4:
        #print(erg)
        erg = play_tournament(erg)

    if len(erg) == 4:
        final = find_winner(find_winner(erg[0], erg[1]), find_winner(erg[2], erg[3]))

        return final

    return find_winner(erg[0], erg[1])



def line_reader(matches_str: str) -> str:
    lst = matches_str.split()
    erg = []
    for a in lst:
        erg.append(a[:-1])

    return erg


def rekursive_solve(matches_str: str) -> str:
    inputs = line_reader(matches_str)
    rockcount = int(inputs[0])
    papercount = int(inputs[1])
    scissorscount = int(inputs[2])
    totalcount = int(rockcount + papercount + scissorscount)
    rounds = int(math.log2(totalcount))

    #print("totalcount: " + str(totalcount))
    #print("rounds: " + str(rounds))

    # rekursion
    if rounds == 1:
        return_value = ""

        for i in range(scissorscount):
            return_value += "S"

        for i in range(papercount):
            return_value += "P"

        return return_value






    # links
    # ein paper rest rocks
    left_builder = ""
    for i in range(int(totalcount / 2)):
        if i == 0:
            if papercount > 0:
                left_builder += "P"
                papercount -= 1
                continue
            else:
                #print("Zu wenig Papers, unmöglich???")
                continue

        if rockcount > 0:
            left_builder += "R"
            rockcount -= 1
        else:
            if scissorscount > 1:
                left_builder += "S"
                scissorscount -= 1
            elif papercount > 0:
                left_builder += "P"
                papercount -= 1
            else:
                print("Riesiges Problem")



    # rechts
    # rekursion

    right_builder = ""
    matches_str_builder = ""

    # restlichen matches_str bilden

    matches_str_builder += str(rockcount)
    matches_str_builder += "R "
    matches_str_builder += str(papercount)
    matches_str_builder += "P "
    matches_str_builder += str(scissorscount)
    matches_str_builder += "S"

    #print("right side: " + matches_str_builder)

    right_builder = rekursive_solve(matches_str_builder)



    return left_builder + right_builder


def solve_level_5(matches_str: str) -> str:
    inputs = line_reader(matches_str)
    rock_count = int(inputs[0])
    paper_count = int(inputs[1])
    scissors_count = int(inputs[2])
    spock_count = int(inputs[3])
    lizard_count = int(inputs[4])
    totalcount = int(rock_count + paper_count + scissors_count + spock_count + lizard_count)
    rounds = int(math.log2(totalcount))
    links = ""
    rechts = ""

    """
    print("New call with totalcount: " + str(totalcount)
          + ", R: " + str(rock_count)
          + ", P: " + str(paper_count)
          + ", S: " + str(scissors_count)
          + ", Y: " + str(spock_count)
          + ", L: " + str(lizard_count))
    """

    # Idee: wo viele gleiche wie möglich miteinander vernichten
    # Idee: Lizards und Papers bevorzugen, weil von Scissors besiegt
    # Idee: Rock und Spock so oft wie möglich gegen sich selbst, solang sie nicht ins finale kommen
    # Idee: Ähnlicher Rekursiver Ansatz wie bei Übung 4
    #       Links: 1 Paper und so viele andere Sachen wie möglich

    # rekursion
    if rounds == 2:
        #print("catch")
        return_value = ""

        for i in range(rock_count):
            return_value += "R"

        for i in range(spock_count):
            return_value += "Y"

        for i in range(paper_count):
            return_value += "P"

        for i in range(lizard_count):
            return_value += "L"

        for i in range(scissors_count):
            return_value += "S"

        return return_value

    # Linke seite

    counter_links = 0
    length_links = totalcount / 2

    if paper_count > 0:
        #print("paper loop start")
        links += "P"
        paper_count -= 1

        counter_links += 1
        while counter_links < length_links:
            if rock_count > 0:
                links += "R"
                rock_count -= 1
                counter_links += 1

            elif spock_count > 0:
                links += "Y"
                spock_count -= 1
                counter_links += 1

            # Fill Up:
            elif scissors_count > 1:
                links += "S"
                scissors_count -= 1
                counter_links += 1

            elif lizard_count > 0:
                links += "L"
                lizard_count -= 1
                counter_links += 1

            elif paper_count > 0:
                links += "P"
                paper_count -= 1
                counter_links += 1



    # wenn hier hineingegangen wird, ist nicht in die erste Schleife gegangen worden -> counter_links ist noch 0
    else:
        if rock_count > 0:
            links += "Y"
            spock_count -= 1
            counter_links += 1

            while counter_links < length_links / 2:
                if rock_count > 0:
                    links += "R"
                    rock_count -= 1
                    counter_links += 1

                elif spock_count > 0:
                    links += "Y"
                    spock_count -= 1
                    counter_links += 1

                elif scissors_count > 1:
                    links += "S"
                    scissors_count -= 1
                    counter_links += 1

                elif lizard_count > 0:
                    links += "L"
                    lizard_count -= 1
                    counter_links += 1

        else:
            # keine rocks mehr -> möglichst schnell Y wegbringen

            # print("else")
            # print("R: " + str(rock_count)
            #       + ", P: " + str(paper_count)
            #       + ", S: " + str(scissors_count)
            #       + ", Y: " + str(spock_count)
            #       + ", L: " + str(lizard_count))

            if spock_count > 0:
                links += "L"
                lizard_count -= 1
                counter_links += 1

                while counter_links < length_links:
                    if spock_count > 0:
                        links += "Y"
                        spock_count -= 1
                        counter_links += 1

                    elif lizard_count > 0:
                        links += "L"
                        lizard_count -= 1
                        counter_links += 1

                    elif scissors_count > 0:
                        links += "S"
                        scissors_count -= 1
                        counter_links += 1

                    else:
                        print("ehm wild joa")
                        return -1

            else:
                while counter_links < length_links:
                    if lizard_count > 0:
                        links += "L"
                        lizard_count -= 1
                        counter_links += 1

                    elif scissors_count > 0:
                        links += "S"
                        scissors_count -= 1
                        counter_links += 1

            #print("nach else")
            #print(scissors_count)




        # jetzt ist evtl. bis zur hälfte alles aufgefüllt, ergebnis dieser hälfte wird spock sein -> andere hälfte muss lizard sein
        # es kann alles außer paper geben

        # Idee: LY YR  YR RR    YR RR  RR RR
        #        L  Y  Y  R     Y  R    R R
        #          L     Y        Y      R
        #             L               Y

        # Rest mit scissors/lizards auffüllen

        # print("R: " + str(rock_count)
        #       + ", P: " + str(paper_count)
        #       + ", S: " + str(scissors_count)
        #       + ", Y: " + str(spock_count)
        #       + ", L: " + str(lizard_count))

        to_go = length_links - counter_links
        i = 0
        #print(to_go)
        if to_go > 0:

            rounds_to_go = math.log2(to_go)

            while i < rounds_to_go:
                if i == 0:
                    if lizard_count > 0:
                        links += "L"
                        lizard_count -= 1
                        counter_links += 1

                        if spock_count > 0:
                            links += "Y"
                            spock_count -= 1
                            i += 1
                            counter_links += 1
                            continue

                        if lizard_count > 0:
                            links += "L"
                            lizard_count -= 1
                            i += 1
                            counter_links += 1
                            continue


                        print("ach du dickes ei!")
                        return -1

                length_for_this_iteration = 2 ** i
                counter_in_loop = 0

                if spock_count > 0:
                    links += "Y"
                    spock_count -= 1
                    counter_in_loop += 1
                    counter_links += 1

                while counter_in_loop < length_for_this_iteration:
                    #print(str(counter_in_loop) + " < " + str(length_for_this_iteration))
                    if rock_count > 0:
                        links += "R"
                        rock_count -= 1
                        counter_in_loop += 1
                        counter_links += 1

                    elif scissors_count > 1:
                        links += "S"
                        scissors_count -= 1
                        counter_in_loop += 1
                        counter_links += 1

                    elif spock_count > 0:
                        links += "Y"
                        spock_count -= 1
                        counter_in_loop += 1
                        counter_links += 1

                    elif lizard_count > 0:
                        links += "L"
                        lizard_count -= 1
                        counter_in_loop += 1
                        counter_links += 1

                i += 1




    # print("pre rekursion")
    # print("R: " + str(rock_count)
    #       + ", P: " + str(paper_count)
    #       + ", S: " + str(scissors_count)
    #       + ", Y: " + str(spock_count)
    #       + ", L: " + str(lizard_count))

    rechts = solve_level_5(create_match_string(rock_count, paper_count, scissors_count, spock_count, lizard_count))

    #print("left:  " + links)
    #print("right: " + rechts)

    return links + rechts


def create_match_string(rock_count:int, paper_count:int, scissors_count:int, spock_count:int, lizard_count:int) -> str:
    matches_str_builder = ""

    matches_str_builder += str(rock_count)
    matches_str_builder += "R "
    matches_str_builder += str(paper_count)
    matches_str_builder += "P "
    matches_str_builder += str(scissors_count)
    matches_str_builder += "S "
    matches_str_builder += str(spock_count)
    matches_str_builder += "Y "
    matches_str_builder += str(lizard_count)
    matches_str_builder += "L"

    return matches_str_builder

def check_line(line):
    results = play_tournament(line)

    if "R" in results or not "S" in results:
        return False

    return True


def tournament_printer(tournament):
    builder = ""

    for i in range(len(tournament)):

        if i % 4 == 0 and i != 0:
            builder += " "
            builder += tournament[i]
        else:
            builder += tournament[i]

    print(builder)

if __name__ == '__main__':
    #lines = read_file(f"./level_5/level5_example.in")

    #for line in lines:
        #print(solve_level_5(line))
        #print(play_full_tournament(solve_level_5(line)))

    for i in range(1, 6):
        lines = read_file(f"./level_5/level5_{i}.in")
        print(i)

        for line in lines:
            if play_full_tournament(solve_level_5(line)) != "S":
                print("----------------------------------------------------------------------")
                print(line)
                print(solve_level_5(line))
                print(play_full_tournament(solve_level_5(line)))
                print("----------------------------------------------------------------------")



        winners = [solve_level_5(line) for line in lines]
        write_file(f"./level_5/level5_{i}.out", winners)


    # 104R 2P 1S 15Y 6L
    # 97R 2P 8S 12Y 9L

    print("6R 5P 2S 3Y 0L")
    print(solve_level_5("6R 5P 2S 3Y 0L"))
    print("\n\n\n-------------------------------------------------------------------------------\n\n\n")
    print(play_full_tournament(solve_level_5("6R 5P 2S 3Y 0L")))
    print("\n\n\n===============================================================================\n\n\n")

    print("7R 1P 1S 2Y 5L")
    print(solve_level_5("7R 1P 1S 2Y 5L"))
    print("\n\n\n-------------------------------------------------------------------------------\n\n\n")
    print(play_full_tournament(solve_level_5("7R 1P 1S 2Y 5L")))
    print("\n\n\n===============================================================================\n\n\n")

    print("97R 2P 8S 12Y 9L")
    print(solve_level_5("97R 2P 8S 12Y 9L"))
    print("\n\n\n-------------------------------------------------------------------------------\n\n\n")
    print(play_full_tournament(solve_level_5("97R 2P 8S 12Y 9L")))
    print("\n\n\n===============================================================================\n\n\n")

    print("0R 0P 4S 4Y 8L")
    print(solve_level_5("0R 0P 4S 4Y 8L"))
    print("\n\n\n-------------------------------------------------------------------------------\n\n\n")
    print(play_full_tournament(solve_level_5("0R 0P 4S 4Y 8L")))

    print("\n\n\n===============================================================================\n\n\n")

    print("104R 2P 1S 15Y 6L")
    print(solve_level_5("104R 2P 1S 15Y 6L"))
    print("\n\n\n-------------------------------------------------------------------------------\n\n\n")
    print(play_full_tournament(solve_level_5("104R 2P 1S 15Y 6L")))

