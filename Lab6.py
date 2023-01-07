import math


class Character:
    def __init__(self, health_points, stamina_points, damage) -> None:
        self.health_points = health_points
        self.stamina_points = stamina_points
        self.damage = damage
        self.class_name = 'Character'

    def __add__(self, other):
        return Character(
            self.health_points + other.health_points,
            self.stamina_points + other.stamina_points,
            self.damage + other.damage
        )

    def print_info(self):
        print(f'This character is: {self.class_name}')
        print(f'It has {self.health_points} health points')
        print(f'It has {self.stamina_points} stamina points')
        print(f'It can deal {self.damage} damage')

    def hits_amount(self):
        raise NotImplementedError


class WeakEnemy(Character):
    def __init__(self, health_points, stamina_points, damage) -> None:
        super().__init__(health_points, stamina_points, damage)
        self.stamina_damage = 2
        self.class_name = 'WeakEnemy'

    def __add__(self, other):
        obj = WeakEnemy(
            self.health_points + other.health_points,
            self.stamina_points + other.stamina_points,
            self.damage + other.damage
        )
        obj.class_name = 'StrongEnemy'
        return obj

    def hit(self):
        if self.stamina_points != 0:
            self.stamina_points -= self.stamina_damage
        else:
            print('This character hasnt any stamina points')
        return self.damage

    def hits_amount(self):
        num = math.ceil(self.stamina_points / self.stamina_damage)
        print(f'Character can deal {num} hits until his stamina ended')


class Boss(Character):
    def __init__(self, health_points, stamina_points, damage) -> None:
        super().__init__(health_points, stamina_points, damage)
        self.last_damage = 0
        self.class_name = 'Boss'

    def take_damage(self, damage):
        self.last_damage = damage
        if self.health_points > 0:
            self.health_points -= self.last_damage
        else:
            print('Boss is deaded')

    def hits_amount(self):
        num = math.ceil(self.health_points / self.last_damage)
        print(f'Character can deal {num} hits until its alive')


if __name__ == '__main__':
    # создаем босса
    boss_character = Boss(100, 100, 10)
    # создаем слабого врага
    weak_enemy = WeakEnemy(100, 100, 20)
    # враг бьет босса
    boss_character.take_damage(weak_enemy.hit())
    # печатаем статистику босса
    boss_character.print_info()
    # смотрим сколько таких ударов он еще смодет выдержать
    boss_character.hits_amount()
    # печатаем статистику врага
    weak_enemy.print_info()
    # смотрим сколько осталось выносливости
    weak_enemy.hits_amount()
    # объединяем двух слабых врагов, получая сильного
    strong_enemy = weak_enemy + WeakEnemy(100, 100, 20)
    # печатаем его статистику
    strong_enemy.print_info()
    # враг бьет босса
    boss_character.take_damage(strong_enemy.hit())
    # печатаем статистику босса
    boss_character.print_info()
    # смотрим сколько таких ударов он еще смодет выдержать
    boss_character.hits_amount()
    # печатаем статистику врага
    strong_enemy.print_info()
    # смотрим сколько осталось выносливости
    strong_enemy.hits_amount()