"""Application module."""


class Application:
    """Maze application class."""

    def __init__(self, choice: str):
        """Init."""
        self.game = Game()

        if choice == "cli":
            self.view = CLIView(self.game)
            self.controller = CLIController(self.game)
        elif choice == "pygame":
            self.view = # ma vue pygame
            self.controller = # mon controller pygame

    def run(self):
        """Run main method."""
        running = True
        while running:
            self.view.display()
            control = self.controller.handle_control()
            self.game.update(control)
