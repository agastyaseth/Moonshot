    # -*- coding: utf-8 -*-

from vehicle import Vehicle

class NissanLeaf(Vehicle):
    Mass = 1521
    FrontalArea = 2.3316
    DragCoefficient = 0.28
    DrivelineEfficiency = .92
    MotorEfficiency = .91
    BatteryCapacity = 100
    Voltage = 360
    power_AC = 0.7
    power_Music = 0.4
    power_Light = 0.1
    power_Coolent = 0.3
    

    def __init__(self):
        super(NissanLeaf, self).__init__(self.Mass, self.FrontalArea, 
             self.DragCoefficient, self.DrivelineEfficiency, 
             self.MotorEfficiency , self.BatteryCapacity ,
             self.Voltage , self.power_AC, self.power_Music,  self.power_Light,
        self.power_Coolent )
