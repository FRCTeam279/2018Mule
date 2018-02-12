import wpilib
from commandbased import CommandBasedRobot
from wpilib.command import Scheduler
from wpilib import SmartDashboard
from wpilib.driverstation import DriverStation
from robotpy_ext.common_drivers import navx


# import items in the order they should be initialized to avoid any suprises
import robotmap
import subsystems
import oi

from commands.tankdrivetoencoderdistance import TankDriveToEncoderDistance


class MyRobot(CommandBasedRobot):
    # for parent code see:
    # https://github.com/robotpy/robotpy-wpilib-utilities/blob/master/commandbased/commandbasedrobot.py

    def robotInit(self):
        print('2018Mule - robotInit called')
        if robotmap.sensors.hasAHRS:
            try:
                robotmap.sensors.ahrs = navx.AHRS.create_spi()
                # use via robotmap.sensors.ahrs.getAngle()
                print('robotInit: NavX Setup')
            except:
                if not DriverStation.getInstance().isFmsAttached():
                    raise

        # subsystems must be initialized before things that use them
        subsystems.init()
        oi.init()

        #SmartDashboard.putData("TankDrive", subsystems.driveline)

        # setup buttons for testing
        #SmartDashboard.putData("Test DriveToEncoderDistance", TankDriveToEncoderDistance(
        #    useDashboardValues=True))


    def autonomousPeriodic(self):
        # game data with be three character string made up of L and R for each position from
        # your alliance's perspective
        gameData = DriverStation.getInstance().getGameSpecificMessage()

        if len(gameData) > 0:
            nearSwitchSide = gameData[0]
            scaleSide = gameData[1]
            farSwitchSide = gameData[2]

        else:
            print("Auto Periodic: Error - gameData was zero length!")

        Scheduler.getInstance().run()


    def teleopPeriodic(self):
        Scheduler.getInstance().run()
        SmartDashboard.putNumber("DL Enc Left", subsystems.driveline.leftEncoder.get())
        SmartDashboard.putNumber("DL Enc Right", subsystems.driveline.rightEncoder.get())

    def testPeriodic(self):
        wpilib.LiveWindow.run()


if __name__ == '__main__':
    wpilib.run(MyRobot)

