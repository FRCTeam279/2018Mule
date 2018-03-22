from wpilib.command import CommandGroup, PrintCommand


class FakeAutoSwitchToLeft(CommandGroup):

    def __init__(self):
        super().__init__('FakeAutoSwitchToLeft')
        self.setInterruptible(True)
        self.setRunWhenDisabled(False)
        self.addSequential(PrintCommand("CMD Group FakeAutoSwitchToLeft: Starting"))

        self.addSequential(PrintCommand("CMD Group FakeAutoSwitchToLeft: Drive Forward 132 inches"))
        self.addSequential(PrintCommand("CMD Group FakeAutoSwitchToLeft: Turn Right"))
        self.addSequential(PrintCommand("CMD Group FakeAutoSwitchToLeft: Drop Level"))
        self.addSequential(PrintCommand("CMD Group FakeAutoSwitchToLeft: Eject"))

        self.addSequential(PrintCommand("CMD Group FakeAutoSwitchToLeft: Finished"))






