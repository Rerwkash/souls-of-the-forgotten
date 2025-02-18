"""
Модуль, описывающий систему персонажей.
"""

class Character:
    """
    Базовый класс для всех персонажей.

    Attributes:
        name (str): Имя персонажа.
        health (int): Текущее здоровье персонажа.
    """

    def __init__(self, name: str, health: int):
        """
        Инициализация объекта Character.

        Args:
            name (str): Имя персонажа.
            health (int): Начальное здоровье персонажа.
        """
        self.name = name
        self.health = health

    def take_damage(self, damage: int):
        """
        Метод, уменьшающий здоровье персонажа при получении урона.

        Args:
            damage (int): Количество урона.
        """
        self.health -= damage