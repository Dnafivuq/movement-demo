import pygame


class SimulationEngine:
    def __init__(self):
        self._delta_time = 0
        self._screen = pygame.display.set_mode((960, 720))
        self._clock = pygame.time.Clock()
        self._running = True

    def run(self) -> None:
        self._delta_time = self._clock.tick(60) / 1000
        while (self._running):
            self._process_events()
            self._physics_update()
            self._render()

    def _process_events(self):
        pass

    def _physics_update(self):
        pass

    def _render(self):
        pass
