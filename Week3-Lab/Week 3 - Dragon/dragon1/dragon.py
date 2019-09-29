class Dragon:

    def __init__ (self, name="dora"):
        self.name = name
        self.asleep = False
        self.stuff_in_belly = 10
        self.stuff_in_intestine = 0

        print("%s이 태어났습니다." % self.name)

        if self.asleep:
            print("%s은 지금 자고 있어요." % self.name)
        else:
            print("%s은 깨어 있어요." % self.name)

        self.check_variables()

    def feed(self):
        print("===============================")
        print("%s에게 밥을 주고 있어요." % self.name)
        print("===============================")
        self.passage_of_time()
        self.stuff_in_belly = 10
        self.check_variables()

    def walk(self):
        print("===============================")
        print("%s과 산책을 했어요." % self.name)
        print("===============================")
        self.passage_of_time()
        self.stuff_in_intestine = 0
        self.check_variables()

    def passage_of_time(self):
        self.stuff_in_belly = self.stuff_in_belly - 1          # 뱃속은 하나씩 비우고
        self.stuff_in_intestine = self.stuff_in_intestine + 1  # 장은 하나씩 채우고

    def check_variables(self):
        print("%s은 지금 배가 %d인 상태입니다." % (self.name, self.stuff_in_belly))
        print("%s은 지금 장이 %d인 상태입니다." % (self.name, self.stuff_in_intestine))


dragon = Dragon("G-Dragon")
dragon.feed()
dragon.walk()
