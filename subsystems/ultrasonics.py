import wpilib
from wpilib.ultrasonic import Ultrasonic
from wpilib.command.subsystem import Subsystem
import subsystems
import robotmap


class Ultrasonics(Subsystem):

    def __init__(self):
        print('Ultrasonics: init called')
        super().__init__('Ultrasonics')
        self.debug = False
        self.logPrefix = "Ultrasonics: "

()