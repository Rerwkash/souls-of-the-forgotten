"""
Модуль, описывающий искусственный интеллект противников.
"""

class OpponentAI:
    """
    Класс, представляющий систему ИИ для противников.

    Attributes:
        health (int): Текущее здоровье противника.
        level (int): Уровень сложности ИИ.
    """

    def __init__(self, health: int, level: int):
        """
        Инициализация объекта OpponentAI.

        Args:
            health (int): Начальное здоровье противника.
            level (int): Уровень сложности ИИ.
        """
        self.health = health
        self.level = level

    def make_decision(self) -> str:
        """
        Метод, определяющий решение ИИ.

        Returns:
            str: Решение, принятое ИИ (например, "атаковать" или "обороняться").
        """
        return "атаковать"