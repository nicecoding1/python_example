import random
import operator

game_point = {"human":0, "computer1":0, "computer2":0}

while True:
    print("*"*20)
    print("""    31 숫자게임""")
    print("*"*20)

    game_log = []
    
    current_number = 1

    randnum = random.randint(0, 2)
    if randnum == 0:
        current_player = "human"
    elif randnum == 1:
        current_player = "computer1"
    else:
        current_player = "computer2"

    while current_number <= 31:
      
        print("현재 숫자는 " + str(current_number) + " 입니다.")

        if current_player == "human":

            print("1, 2, 또는 3을 입력하세요. 더해서 31 이상이 되면 게임에서 지는 것입니다.")

            player_choice = ""
            while player_choice not in ["1", "2", "3"]:
                player_choice = input("어떤 값을 더할까요? ")

            player_choice = int(player_choice)
            current_number = current_number + player_choice

            if current_number >= 31:
                print("현재 숫자는 " + str(current_number) + " 입니다.")
                print()
                print("human 이 졌습니다.")
                break

            game_log.append("human")
            current_player = "computer1"


        elif current_player == "computer1":

            computer_choice = random.randint(1, 3)
            current_number = current_number + computer_choice
            print("Computer1 순서입니다. computer1 은(는) " + str(computer_choice) + " 을 선택했습니다.")

            if current_number >= 31:
                print("현재 숫자는 " + str(current_number) + " 입니다.")
                print()
                print("computer1 이 졌습니다.")
                break

            game_log.append("computer1")
            current_player = "computer2"

        else:
            computer_choice = random.randint(1, 3)
            current_number = current_number + computer_choice
            print("Computer2 순서입니다. computer2 은(는) " + str(computer_choice) + " 을 선택했습니다.")

            if current_number >= 31:
                print("현재 숫자는 " + str(current_number) + " 입니다.")
                print()
                print("computer2 이 졌습니다.")
                break

            game_log.append("computer2")
            current_player = "human"

    # 게임포인트 지급
    player = game_log.pop()
    game_point[player] += 2

    player = game_log.pop()
    game_point[player] += 1

    print("게임점수")
    print(game_point)

    play_again = input("게임을 다시 진행하겠습니까? ")
    if play_again.lower().startswith("y"):
        continue
    else:
        print("게임종료")
        break

print("")
print("[게임점수 순위]")
sort_list = sorted(game_point.items(), key=operator.itemgetter(1), reverse=True)
for i in range(len(sort_list)):
    print("{}위 : {}".format(i+1, sort_list[i][0]))

