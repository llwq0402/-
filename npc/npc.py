class NPC:
    def __init__(self, name, hp, trust):
        self.name = name
        self.hp = hp
        self.trust = trust

    def talk(self):
        print("Who are you?")

    def take_damage(self, damage):
        self.hp -= damage
        print("Player attacks Guard")
        print("Guard HP:", self.hp)

    def change_trust(self, trust):
        self.trust += trust
        print("Player helps Guard")
        print("Guard Trust:", self.trust)
        if trust >= 20:
            print("Guard: Maybe I can trust you.")

Guard = NPC("Guard", 100, 0)

Guard.talk()
Guard.take_damage(30)
Guard.change_trust(20)
