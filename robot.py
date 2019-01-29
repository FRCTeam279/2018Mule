import wpilib
from commandbased import CommandBasedRobot
from wpilib.command import Scheduler
from wpilib import SmartDashboard
from wpilib.driverstation import DriverStation
#from robotpy_ext.common_drivers import navx
import navx


# import items in the order they should be initialized to avoid any suprises
import robotmap
import subsystems
import oi


from fakeautomanager import FakeAutoManager


autoManager = None


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

        global autoManager
        autoManager = FakeAutoManager()
        autoManager.initialize()

    def autonomousInit(self):
        super().autonomousInit()
        autoManager.gameData = None

    def autonomousPeriodic(self):
        global autoManager
        try:
            if not autoManager.gameData:
                autoManager.gameData = str(DriverStation.getInstance().getGameSpecificMessage())
                print("Auto Periodic: Game Data = {}".format(str(autoManager.gameData)))

                if len(str(autoManager.gameData)) > 0:
                    gameDataNearSwitchSide = autoManager.gameData[0]
                    gameDataScaleSide = autoManager.gameData[1]
                    autoCommandToRun = autoManager.getAction(gameDataNearSwitchSide, gameDataScaleSide)
                    autoCommandToRun.start()
                    print("Auto Periodic: Started command received from AutoManager")
                else:
                    print("Auto Periodic: Error - gameData was zero length!")
        except Exception as e:
            print('autonomousPeriodic: Error! Exception caught running autoManager: {}'.format(e))
        super().autonomousPeriodic()

    def teleopPeriodic(self):
        Scheduler.getInstance().run()

    def testPeriodic(self):
        wpilib.LiveWindow.run()


if __name__ == '__main__':
    wpilib.run(MyRobot)

