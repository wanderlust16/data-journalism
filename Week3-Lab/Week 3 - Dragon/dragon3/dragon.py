class Dragon:

    def __init__ (self, name="dora"):
        """
        Constructor: Dragon 생성과 관련한 변수를 초기화 하고 생성 메시지를 출력한다
        Variables: name, asleep, stuff_in_belly, stuff_in_intestine
        """
        self.name = name
        self.asleep = False
        self.stuff_in_belly = 10
        self.stuff_in_intestine = 0

        print("\n===============================")
        print("%s이 태어났습니다." % self.name)
        print("===============================")
        # self.check_variables()

    def feed(self):
        """
        Feed method: stuff_in_belly 값을 최고치(10)으로 설정
        __passage_of_time()을 한번 실행 (시간을 가게 만드는 역할)
        """
        print("\n===============================")
        print("%s에게 밥을 주고 있어요." % self.name)
        print("===============================")
        self.__passage_of_time()
        self.stuff_in_belly = 10
        # self.check_variables()

    def walk(self):
        """
        Walk method: stuff_in_intestine 값을 최저치(0)으로 설정
        __passage_of_time()을 한번 실행 (시간을 가게 만드는 역할)
        """
        print("\n===============================")
        print("%s과 산책을 했어요." % self.name)
        print("===============================")
        self.__passage_of_time()
        self.stuff_in_intestine = 0
        # self.check_variables()

    def toss(self):
        """
        Toss method: 내부 변수를 변경하지는 않는다.
        __passage_of_time()을 한번 실행 (시간을 가게 만드는 역할)
        """
        print("\n===============================")
        print("%s을 하늘 높이 던졌어요." % self.name)
        print("===============================")
        print("즐거워 하네요.")
        self.__passage_of_time()
        # self.check_variables()

    def rock(self):
        """
        Rock method: asleep 변수를 True로 지정한 후 메시지를 출력하고 다시 False로 지정
        __passage_of_time()을 한번 실행 (시간을 가게 만드는 역할)
        """
        print("\n===============================")
        print("%s을 안아서 흔들어 주었어요." % self.name)
        print("===============================")
        print("잠이 들었네요.")
        self.asleep = True
        self.__passage_of_time()
        if self.asleep:
            self.asleep = False
            print("...그런데 흔들기를 멈췄더니 금새 깨버렸어요.")
        # self.check_variables()

    def put_to_bed(self):
        """
        Put to bed method: asleep 을 True로 설정하고
        __passage_of_time()을 세번 실행한다.
        그 이후에는 asleep을 False로 설정한다.
        """
        print("\n===============================")
        print("%s을 재웠어요." % self.name)
        print("===============================")
        self.asleep = True
        for _ in range(3):
            if self.asleep:
                print("%s이 코를 골아 방안에 연기가 가득찼어요!" % self.name)
                self.__passage_of_time()
        if self.asleep:
            self.asleep = False
            print("%s이 일어나려고 하네요." % self.name)
        # self.check_variables()

    def __passage_of_time(self):
        """
        Passge of Time method: 한 turn 이 돌아가게 하는 메소드.
        stuff_in_belly와 stuff_in_intestine의 값을 turn이 계속됨에 따라 증가/감소 시킨다.
        또한 현재 배가 고픈 상태인지, 장이 가득차 있는 상태인지를 확인하여 관련 메시지를 출력한다.
        """

        # 배가 고픈지 여부를 체크한 후 처리
        if self.stuff_in_belly > 0: # 뱃속에 뭔가라도 차 있으면 내용물을 장으로 이동
            self.stuff_in_belly = self.stuff_in_belly - 1  # 뱃속은 하나씩 비우고
            self.stuff_in_intestine = self.stuff_in_intestine + 1  # 장은 하나씩 채우고
        else:  # 배고픈 상태일 때 (stuff_in_belly <= 0)
            if self.asleep:  # 배고픈 상태로 자고 있을 때에는
                self.asleep = False  # 일단 깨고
                print("갑자기 잠에서 깼네요!")
            print("%s이 몹시 배가 고파요! 당신을 잡아먹었어요." % self.name)
            print("\n===============================")
            print("Dragon 키우기가 종료되었습니다.")
            print("===============================")
            exit()

        # 장이 얼마나 찼는지 여부를 체크한 후 처리
        if self.stuff_in_intestine >= 10:  # 장이 10보다 더 차 있으면
            self.stuff_in_intestine = 0  # 장을 다 비운 후
            print("저런! %s이 그만 아무데나 실례를 했네요..." % self.name)

        # 배가 고픈지 미리 알려주자
        if self.__is_hungry():
            if self.asleep:
                self.asleep = False
                print("갑자기 잠에서 깼네요!")
            print("%s 뱃속에서 꼬르륵 소리가..." % self.name)

        # 화장실이 급한지 미리 알려주자
        if self.__is_poopy():
            if self.asleep:
                self.asleep = False
                print("갑자기 잠에서 깼네요!")
            print("%s가 화장실에 가고 싶어 어쩔 줄 몰라해요." % self.name)

    def __is_hungry(self):
        """
        배가 고프면 (2보다 작거나 같으면 true를 반환)
        """
        if self.stuff_in_belly <= 2:
            return True
        else:
            return False

    def __is_poopy(self):
        """
        장이 차면 (8보다 크거나 같으면 true를 반환)
        """
        if self.stuff_in_intestine >= 8:
            return True
        else:
            return False

    def check_variables(self):
        """
        주요 내부 변인 (stuff_in_belly, stuff_in_intestine) 의 값을 프린팅
        """
        print("\n>> %s은 지금 배가 %d인 상태입니다." % (self.name, self.stuff_in_belly))
        print(">> %s은 지금 장이 %d인 상태입니다." % (self.name, self.stuff_in_intestine))
