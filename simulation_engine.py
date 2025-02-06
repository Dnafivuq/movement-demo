import pygame
import numpy as np
from collections import namedtuple
from physical_body import PhysicalBody
Vector2 = namedtuple('Vector2', ['x', 'y'])


def normalize_vector(vector: Vector2) -> Vector2:
    lenght = np.sqrt(vector.x**2 + vector.y**2)
    if lenght != 0:
        return Vector2(
            vector.x / lenght,
            vector.y / lenght
        )
    return vector


class SimulationEngine:
    def __init__(self) -> None:
        self._delta_time = 0
        self._screen = pygame.display.set_mode((960, 720))
        self._font = pygame.font.SysFont('Comic Sans MS', 30)
        self._input_force = Vector2(0, 0)
        self._clock = pygame.time.Clock()
        self._running = True
        self._body = PhysicalBody(Vector2(960/2, 720/2), Vector2(50, 50), 15)
        self._keyboard = {
            "w": False,
            "s": False,
            "a": False,
            "d": False,
            "b": False
        }

    def run(self) -> None:
        self._delta_time = self._clock.tick(60) / 1000
        while (self._running):
            self._process_events()
            self._physics_update()
            self._render()

    def _process_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            else:
                if "unicode" in event.dict.keys():
                    self._handle_input(event.dict["unicode"],
                                       event.type == pygame.KEYDOWN)

    def _handle_input(self, input: str, isPressed: bool) -> None:
        if input in self._keyboard.keys():
            self._keyboard[input] = isPressed

    def _physics_update(self) -> None:
        self._input_force = Vector2(self._keyboard["d"] - self._keyboard["a"], self._keyboard["s"] - self._keyboard["w"])
        self._input_force = normalize_vector(self._input_force)
        if self._keyboard["b"]:
            self._input_force = Vector2(
                self._input_force.x * 1.5,
                self._input_force.y * 1.5
            )
        self._body.update(self._input_force, self._delta_time)

    def _render(self) -> None:
        self._screen.fill(pygame.Color(0, 255, 153))
        self._body.render(self._screen)

        self._screen.blit(self._font.render(f'Input | x:{self._input_force.x} y:{self._input_force.y}',
                                            True, (0, 0, 0)), (0, 0))
        self._screen.blit(self._font.render(f'Acceleration | x:{self._body._acceleration.x} y:{self._body._acceleration.y}',
                                            True, (0, 0, 0)), (0, 25))
        self._screen.blit(self._font.render(f'Velocity | x:{self._body._velocity.x} y:{self._body._velocity.y}',
                                            True, (0, 0, 0)), (0, 50))
        self._screen.blit(self._font.render(f'Position | x:{self._body._position.x} y:{self._body._position.y}',
                                            True, (0, 0, 0)), (0, 75))
        pygame.display.flip()
