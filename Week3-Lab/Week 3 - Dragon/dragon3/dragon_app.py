from dragon import Dragon

name = input(">> Dragon의 이름을 입력해 주세요. ")
if name == "":
    dragon = Dragon()
else:
    dragon = Dragon(name)

status = True
while status:
    print("\n>> commands:  feed, toss, walk, rock, put to bed, exit")
    command = input(">> 명령어를 입력하세요: ")

    if command == "exit":
        print(">> 게임을 종료합니다.")
        status = False
    elif command == "feed":
        dragon.feed()
    elif command == "toss":
        dragon.toss()
    elif command == "walk":
        dragon.walk()
    elif command == "rock":
        dragon.rock()
    elif command == "put to bed":
        dragon.put_to_bed()
    else:
        print(">> 제시된 명령어만 사용해 주세요.")
