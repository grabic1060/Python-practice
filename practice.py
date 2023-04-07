class Card:
    def __init__(self, name, effect):
        self.name = name  # 카드 이름
        self.effect = effect  # 효과
        self.set = False  # 카드 세트 여부

    # 문제 1
    def set_card(self):
        self.set=True
        print(self.name+'카드가 세팅되었습니다')

        # 문제 2
    def card_activate(self):
        if self.set==True:
            print(self.name+'카드의 효과 발동')
            print(self.effect)
            self.set=False


class BattleCard(Card):
    def __init__(self, name, effect, priority):
        super().__init__(name, effect)
        self.priority = priority  # 우선도

# 문제 3
    def card_battle(self, other):
        if(self.priority)
