import wpilib
from wpilib.smartdashboard import SmartDashboard

from commands.fakeautodrivetoswitch import FakeAutoDriveToSwitch
from commands.fakeautoloadswitchfrommid import FakeAutoLoadSwitchFromMid
from commands.fakeautoscale import FakeAutoScale
from commands.fakeautoswitchtoleft import FakeAutoSwitchToLeft
from commands.fakeautoswitchtoright import FakeAutoSwitchToRight


class FakeAutoManager:
    """
    preferred element:
        'crossLine' - cross auto line
        'switch - prefer switch
        'scale' - prefer scale
    starting side:
        'left'
        'middle'
        'right'
    """
    def __init__(self):
        self.preferredElement = None
        self.startingPosition = None
        self.initialized = False

        self.gameData = None
        self.gameDataNearSwitchSide = None
        self.gameDataScaleSide = None

    def initialize(self):
        if self.initialized:
            return

        # initializing auto chooser
        self.preferredElement = wpilib.SendableChooser()
        self.preferredElement.addObject('crossLine', 0)
        self.preferredElement.addObject('switch', 1)
        self.preferredElement.addObject('scale', 2)

        self.startingPosition = wpilib.SendableChooser()
        self.startingPosition.addObject('left', 0)
        self.startingPosition.addObject('middle', 1)
        self.startingPosition.addObject('right', 2)

        SmartDashboard.putData("Preferred Element", self.preferredElement)
        SmartDashboard.putData("Starting Position", self.startingPosition)
        print("AutoManager: Initialized")
        self.initialized = True

    def getStartingPosition(self):
        return self.startingPosition.getSelected()

    def getPreferredElement(self):
        return self.preferredElement.getSelected()

    # parameters are the L or R for each object from game data
    def getAction(self, nearSwitchSide, scaleSide):

        # ---------------------------------------------
        # Middle Starting Spot
        # ---------------------------------------------
        if self.getStartingPosition() == 1: # middle
            print("AutoManager.GetAction: Starting in middle, nearSwitchSide={}, returning AutoLoadSwitchToFromMid".format(nearSwitchSide))
            return FakeAutoLoadSwitchFromMid(nearSwitchSide)

        # ---------------------------------------------
        # Left Starting Spot
        # ---------------------------------------------
        if self.getStartingPosition() == 0: # left

            if self.getPreferredElement() == 0: # 'crossLine'
                print("AutoManager.GetAction: AutoDriveForward - Preferred={}, Starting={}, NearSwitch={}, Scale={}".format(
                        self.getPreferredElement(), self.getStartingPosition(), nearSwitchSide, scaleSide))
                return FakeAutoDriveToSwitch()

            if self.getPreferredElement() == 1 and nearSwitchSide=='L':     # switch preferred
                print("AutoManager.GetAction: AutoLoadSwitchToLeftFromSide - Preferred={}, Starting={}, NearSwitch={}, Scale={}".format(
                        self.getPreferredElement(), self.getStartingPosition(), nearSwitchSide, scaleSide))
                return FakeAutoSwitchToLeft()

            if self.getPreferredElement() == 2 and scaleSide=='L':          # scale preferred
                print("AutoManager.GetAction: AutoLoadScaleToLeft - Preferred={}, Starting={}, NearSwitch={}, Scale={}".format(
                        self.getPreferredElement(), self.getStartingPosition(), nearSwitchSide, scaleSide))
                return FakeAutoScale()

            # Fall back number 1 - the other element
            # if the preferred element isn't on this side
            #  return either of the others if they are...
            if (self.getPreferredElement() == 1 and nearSwitchSide != 'L') or (     # 1 = switch
                            self.getPreferredElement() == 2 and scaleSide != 'L'):  # 2 = scale
                if nearSwitchSide=='L':
                    print("AutoManager.GetAction: AutoLoadSwitchToLeftFromSide - Preferred={}, Starting={}, NearSwitch={}, Scale={}".format(
                            self.getPreferredElement(), self.getStartingPosition(), nearSwitchSide, scaleSide))
                    return FakeAutoSwitchToLeft()
                if scaleSide == 'L':
                    print("AutoManager.GetAction: AutoLoadScaleToLeft - Preferred={}, Starting={}, NearSwitch={}, Scale={}".format(
                            self.getPreferredElement(), self.getStartingPosition(), nearSwitchSide, scaleSide))
                    return FakeAutoScale()

        # ---------------------------------------------
        # Left Starting Spot
        # ---------------------------------------------
        if self.getStartingPosition() == 2:     # right
            if self.getPreferredElement() == 'crossLine':
                print("AutoManager.GetAction: AutoDriveForward - Preferred={}, Starting={}, NearSwitch={}, Scale={}".format(
                        self.getPreferredElement(), self.getStartingPosition(), nearSwitchSide, scaleSide))
                return FakeAutoDriveToSwitch()

            if self.getPreferredElement() == 1 and nearSwitchSide=='R':     # 1 = switch
                print("AutoManager.GetAction: AutoLoadSwitchToRightFromSide - Preferred={}, Starting={}, NearSwitch={}, Scale={}".format(
                        self.getPreferredElement(), self.getStartingPosition(), nearSwitchSide, scaleSide))
                return FakeAutoSwitchToRight()

            if self.getPreferredElement() == 2 and scaleSide=='R':          # 2 = scale
                print("AutoManager.GetAction: AutoLoadScaleToRight - Preferred={}, Starting={}, NearSwitch={}, Scale={}".format(
                        self.getPreferredElement(), self.getStartingPosition(), nearSwitchSide, scaleSide))
                return FakeAutoScale()

            # Fall back number 1 - the other element
            # if the preferred element isn't on this side
            #  return either of the others if they are...
            if (self.getPreferredElement() == 1 and nearSwitchSide != 'R') or (                 # 1 = switch
                            self.getPreferredElement() == 2 and scaleSide != 'R'):              # 2 = scale
                if nearSwitchSide=='R':
                    print("AutoManager.GetAction: AutoLoadSwitchToRightFromSide - Preferred={}, Starting={}, NearSwitch={}, Scale={}".format(
                            self.getPreferredElement(), self.getStartingPosition(), nearSwitchSide, scaleSide))
                    return FakeAutoSwitchToRight()
                if scaleSide == 'R':
                    print("AutoManager.GetAction: AutoLoadScaleToRight - Preferred={}, Starting={}, NearSwitch={}, Scale={}".format(
                            self.getPreferredElement(), self.getStartingPosition(), nearSwitchSide, scaleSide))
                    return FakeAutoScale()

        # ---------------------------------------------
        # Fall back number 2 - cross the line
        # ---------------------------------------------
        print(
            "AutoManager.GetAction: Defaulting to CrossLine - Preferred={}, Starting={}, NearSwitch={}, Scale={}".format(
                self.getPreferredElement(), self.getStartingPosition(), nearSwitchSide, scaleSide))
        return FakeAutoDriveToSwitch()

