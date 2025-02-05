import numpy as np
import pygame
from collections import namedtuple

Vector2 = namedtuple('Vector2', ['x', 'y'])
g = 9.81
mu = 0.4
k = 0.01


class PhysicalBody:
    def __init__(self, start_pos: Vector2, size: Vector2, speed: float) -> None:
        self._speed: float = speed
        self._size: Vector2 = size
        self._position: Vector2 = start_pos
        self._velocity: Vector2 = Vector2(0, 0)
        self._acceleration: Vector2 = Vector2(0, 0)
        self._body = pygame.Rect(start_pos.x, start_pos.y, size.x, size.y)

    def update(self, applied_force_acceleration: Vector2, delta_time: float) -> None:

        self._acceleration = Vector2(
            applied_force_acceleration.x * self._speed - np.sign(self._velocity.x) * (g*mu + k*self._velocity.x**2),
            applied_force_acceleration.y * self._speed - np.sign(self._velocity.y) * (g*mu + k*self._velocity.y**2)
        )

        self._velocity = Vector2(
            self._velocity.x + self._acceleration.x * delta_time,
            self._velocity.y + self._acceleration.y * delta_time
        )

        self._position = Vector2(
            self._position.x + self._velocity.x * delta_time,
            self._position.y + self._velocity.y * delta_time
        )
        self._body = pygame.Rect(self._position.x, self._position.y, self._size.x, self._size.y)

    def render(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, pygame.Color(123, 123, 123), self._body)
