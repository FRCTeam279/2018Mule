from wpilib.command import CommandGroup, PrintCommand


class FakeAutoScale(CommandGroup):

    def __init__(self):
        super().__init__('FakeAutoScale')
        self.setInterruptible(True)
        self.setRunWhenDisabled(False)
        self.addSequential(PrintCommand("CMD Group FakeAutoScale: Starting"))

        self.addSequential(PrintCommand("CMD Group FakeAutoScale: Drive Forward 250 inches"))

        self.addSequential(PrintCommand("CMD Group FakeAutoSwitchToRight: Finished"))






