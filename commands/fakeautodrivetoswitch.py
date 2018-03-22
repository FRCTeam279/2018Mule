from wpilib.command import CommandGroup, PrintCommand


class FakeAutoDriveToSwitch(CommandGroup):

    def __init__(self):
        super().__init__('FakeAutoDriveToSwitch')
        self.setInterruptible(True)
        self.setRunWhenDisabled(False)
        self.addSequential(PrintCommand("CMD Group FakeAutoDriveToSwitch: Starting"))

        self.addSequential(PrintCommand("CMD Group FakeAutoDriveToSwitch: Drive Forward 132 inches"))

        self.addSequential(PrintCommand("CMD Group FakeAutoSwitchToLeft: Finished"))






