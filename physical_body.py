import numpy as np
import pygame
from collections import namedtuple

Vector2 = namedtuple('Vector2', ['x', 'y'])
g = 9.81
mu = 0.9
k = 0.01


def normalize_vector(vector: Vector2) -> Vector2:
    lenght = np.sqrt(vector.x**2 + vector.y**2)
    if lenght != 0:
        return Vector2(
            vector.x / lenght,
            vector.y / lenght
        )
    return vector


def round_to_zero(vector: Vector2, acceleration: Vector2, threshold: float = 0.005) -> Vector2:
    x = vector.x
    y = vector.y
    if (x**2 < threshold and acceleration.x**2 < threshold):
        x = 0
    if (y**2 < threshold and acceleration.y**2 < threshold):
        y = 0
    return Vector2(
        x,
        y
    )


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
            applied_force_acceleration.x * self._speed - np.sign(self._velocity.x) * k*self._velocity.x**2,
            applied_force_acceleration.y * self._speed - np.sign(self._velocity.y) * k*self._velocity.y**2
        )

        self._velocity = Vector2(
            self._velocity.x + (self._acceleration.x - normalize_vector(self._velocity).x*mu*g) * delta_time,
            self._velocity.y + (self._acceleration.y - normalize_vector(self._velocity).y*mu*g) * delta_time
        )
        self._velocity = round_to_zero(self._velocity, self._acceleration)

        self._position = Vector2(
            self._position.x + self._velocity.x * delta_time,
            self._position.y + self._velocity.y * delta_time
        )
        self._body = pygame.Rect(self._position.x, self._position.y, self._size.x, self._size.y)

    def render(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, pygame.Color(123, 123, 123), self._body)
