# Создание класса Ship
# Ограничение перемещений
# Управление кораблем
# Обработка нажатия клавиши
# Непрерывное перемещение
# Перемещение влево и вправо

import pygame
from pygame.sprite import Sprite

from settings import Settings


class Ship(Sprite):
    """Класс для управления кораблем."""

    def __init__(self, screen):
        """Инициализирует корабль и задает его начальную позицию."""
        super().__init__()
        self.screen = screen
        self.settings = Settings()
        self.screen_rect = screen.get_rect()

        # Загружает изображение корабля и получает прямоугольник.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom
        # Сохранение вещественной координаты центра корабля.
        self.x = float(self.rect.x)

        # Изменение цвета фона изображения корабля.
        self.image.set_colorkey((0, 255, 0))

        # Флаг перемещения
        self.moving_riqht = False
        self.moving_left = False

    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        if self.moving_riqht and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed_factor
        # if self.moving_riqht:
        #     self.x += self.settings.ship_speed
        # if self.moving_left:
        #     self.x -= self.settings.ship_speed

        # Обновление атрибута rect на основании self.x.
        self.rect.x = self.x

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Размещение корабля в центре нижней стороны."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

