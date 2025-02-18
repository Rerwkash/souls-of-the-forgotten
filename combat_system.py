"""
Модуль, описывающий систему боевых механик.
"""

def attack(enemy):
    """
    Описывает механику атаки.

    Args:
        enemy (Enemy): Объект врага для атаки.

    Returns:
        None
    """
    enemy.health -= 20