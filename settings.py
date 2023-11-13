# Создание класса Settings
# Регулировка скорости корабля
# Ограничение количества снарядов

class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 34, 255)

        # Настройки корабля
        self.ship_limit = 3

        # Настройки Снаряда
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # Настройки пришельца
        self.fleet_drop_speed = 10

        # Темп ускорения игры
        self.speedup_scale = 1.1
        # Темп роста стоимости пришельцев
        self.score_scale = 1.5

        self.inittialize_dynamic_settings()

    def inittialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 1.0

        # fleet_direction = 1 обозначает движение вправо; а -1 влево
        # Для настройки fleet_direction можно использовать текстовое значение
        # например, 'left' или 'right'
        self.fleet_direction = 1

        self.alien_points = 50

    def incraese_speed(self):
        """Увеличивает настройки скорости и стоимости пришельцев"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
