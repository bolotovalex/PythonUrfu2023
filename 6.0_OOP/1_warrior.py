'''1. Напишите программу следующему описанию. Есть класс "Воин".
От него создаются два экземпляра-юнита. Каждому устанавливается здоровье в 100 очков.
В случайном порядке они бьют друг друга. Тот, кто бьет, здоровья не теряет.
У того, кого бьют, оно уменьшается на случайное количество очков от одного удара
(можно также указать куда пришелся удар).
После каждого удара надо выводить сообщение, какой юнит атаковал, и сколько у противника осталось здоровья.
Как только у кого-то заканчивается ресурс здоровья, программа завершается сообщением о том, кто одержал победу.
'''
import random


class Warrior:
    def __init__(self, warrior_name):
        self.__name = warrior_name
        self.health = 100
        self.body_parts_multplier = {'head': 1.2,
                                     'body': 1.0,
                                     'left_hand': 0.8,
                                     'right_hand': 0.8,
                                     'left_leg': 0.7,
                                     'right_leg': 0.7}

        self.lexixaly_print = {'head': 'голове',
                               'body': 'телу',
                               'left_hand': 'левой руке',
                               'right_hand': 'правой руке',
                               'left_leg': 'левой ноге',
                               'right_leg': 'правой ноге'
                               }

    def get_name(self):
        return self.__name

    def hit_damage(self):
        random_body_part = random.choice(list(self.body_parts_multplier.keys()))
        hit = round(random.randint(5, 20) * self.body_parts_multplier[random_body_part])
        print(f"{self.__name} попал по {self.lexixaly_print[random_body_part]} и нанес удар силы: {hit}",
              end=' | ')
        return hit

    def damage_recieved(self, damage):
        self.health = self.health - damage
        if self.health <= 0:
            print(f"{self.__name} погиб.")
        else:
            print(f"{self.__name} Остаток здоровья: {self.health}")

    def check_state(self):
        if self.health >= 0:
            return True
        else:
            return False


def get_attack_defence_wariors(warriors_list: list):
    return tuple(random.sample(warriors_list, k=2))


if __name__ == "__main__":

    warrior1 = Warrior('Воин-1')
    warrior2 = Warrior('Воин-2')
    warriors_on_battale = [warrior1, warrior2]

    while True:
        attack_warrior, defence_warrior = get_attack_defence_wariors(warriors_on_battale)
        hit_size = attack_warrior.hit_damage()
        defence_warrior.damage_recieved(hit_size)

        if defence_warrior.check_state() is False:
            break
