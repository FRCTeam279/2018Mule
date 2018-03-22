from wpilib.command import CommandGroup, PrintCommand


class FakeAutoSwitchToRight(CommandGroup):

    def __init__(self):
        super().__init__('FakeAutoSwitchToRight')
        self.setInterruptible(True)
        self.setRunWhenDisabled(False)
        self.addSequential(PrintCommand("CMD Group FakeAutoSwitchToRight: Starting"))

        self.addSequential(PrintCommand("CMD Group FakeAutoSwitchToRight: Drive Forward 132 inches"))
        self.addSequential(PrintCommand("CMD Group FakeAutoSwitchToRight: Turn Left"))
        self.addSequential(PrintCommand("CMD Group FakeAutoSwitchToRight: Drop Level"))
        self.addSequential(PrintCommand("CMD Group FakeAutoSwitchToRight: Eject"))

        self.addSequential(PrintCommand("CMD Group FakeAutoSwitchToRight: Finished"))






