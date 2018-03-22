from wpilib.command import CommandGroup, PrintCommand

from commands.delay import Delay


class FakeAutoLoadSwitchFromMid(CommandGroup):

    def __init__(self, side):

        super().__init__('FakeAutoLoadSwitchFromMid')
        self.setInterruptible(True)
        self.setRunWhenDisabled(False)

        self.addSequential(PrintCommand("CMD Group FakeAutoLoadSwitchFromMid: Starting"))
        # TODO - Drive to Ultrasonic Distance

        self.addSequential(PrintCommand("CMD Group FakeAutoLoadSwitchFromMid: Drive Forward 12 inches"))

        self.addSequential(PrintCommand("CMD Group FakeAutoLoadSwitchFromMid: Delay"))

        if side == 'L':     # angle to left, then right and unload
            self.addSequential(PrintCommand("CMD Group FakeAutoLoadSwitchFromMid: Turn to -45deg"))
        else:               # angle to right, then left and unload
            self.addSequential(PrintCommand("CMD Group FakeAutoLoadSwitchFromMid: Turn to 45deg"))

        self.addSequential(PrintCommand("CMD Group FakeAutoLoadSwitchFromMid: Delay"))
        self.addSequential(Delay(250))

        self.addSequential(PrintCommand("CMD Group FakeAutoLoadSwitchFromMid: Drive Forward 36 inches"))


        self.addSequential(PrintCommand("CMD Group FakeAutoLoadSwitchFromMid: Delay"))
        self.addSequential(Delay(250))

        self.addSequential(PrintCommand("CMD Group FakeAutoLoadSwitchFromMid: Turn to 0deg"))


        self.addSequential(PrintCommand("CMD Group FakeAutoLoadSwitchFromMid: Delay"))
        self.addSequential(Delay(250))

        # TODO - try with ultrasonics
        self.addSequential(PrintCommand("CMD Group FakeAutoLoadSwitchFromMid: Drive Forward 24 inches"))

        if side == 'L' or side == 'R':
            self.addSequential(PrintCommand("CMD Group FakeAutoLoadSwitchFromMid: Rotate Cube"))
            self.addSequential(PrintCommand("CMD Group FakeAutoLoadSwitchFromMid: Eject"))
        else:
            self.addSequential(PrintCommand("CMD Group FakeAutoLoadSwitchFromMid: invalid value passed for side, will not unload cube"))

        self.addSequential(PrintCommand("CMD Group FakeAutoLoadSwitchFromMid: Finished"))

