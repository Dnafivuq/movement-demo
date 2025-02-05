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
        self._clock = pygame.time.Clock()
        self._running = True
        self._body = PhysicalBody(Vector2(960/2, 720/2), Vector2(30, 30), 7)
        self._keyboard = {
            "w": False,
            "s": False,
            "a": False,
            "d": False,
            "LCtrl": False
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
                    self._handle_input("LCtrl" if event.dict["key"] == 1073742048 else event.dict["unicode"],
                                       event.type == pygame.KEYDOWN)

    def _handle_input(self, input: str, isPressed: bool) -> None:
        if input in self._keyboard.keys():
            self._keyboard[input] = isPressed

    def _physics_update(self) -> None:
        input_force = Vector2(self._keyboard["d"] - self._keyboard["a"], self._keyboard["s"] - self._keyboard["w"])
        input_force = normalize_vector(input_force)
        self._body.update(input_force, self._delta_time)

    def _render(self) -> None:
        self._screen.fill(pygame.Color(0, 255, 153))
        self._body.render(self._screen)
        pygame.display.flip()
