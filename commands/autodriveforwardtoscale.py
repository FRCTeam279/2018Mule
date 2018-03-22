from wpilib.command import CommandGroup, PrintCommand

import robotmap
from commands.tankdrivetoencoderdistance import TankDriveToEncoderDistance
from commands.tankdrivetoencoderdistanceonheading import TankDriveToEncoderDistanceOnHeading


class AutoDriveForwardToScale(CommandGroup):

    def __init__(self):
        super().__init__('AutoDriveForwardToScale')
        self.setInterruptible(True)
        self.setRunWhenDisabled(False)
        self.addSequential(PrintCommand("CMD Group AutoDriveForwardToScale: Starting"))

        self.addSequential(PrintCommand("CMD Group AutoDriveForwardToScale: Drive Forward 250 inches"))
        self.addSequential(TankDriveToEncoderDistanceOnHeading(target=robotmap.driveLine.ticksPerInch * 400,
                                                      p=0.02,
                                                      i=0.0,
                                                      d=0.0,
                                                      tolerance=100,
                                                      minSpeed=0.2,
                                                      maxSpeed=0.7,
                                                      headingP=0.035), timeout=5)

        self.addSequential(PrintCommand("CMD Group AutoDriveForwardToScale: Finished"))

