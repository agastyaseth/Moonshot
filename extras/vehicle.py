# -*- coding: utf-8 -*-

class Vehicle(object):
    def __init__(self, mass, frontalArea, dragCoefficient, 
                 drivelineEfficiency, motorEfficiency , 
                 batteryCapacity , voltage , power_AC ,power_Music,power_Light , power_Coolent ):
        self.Mass = mass
        self.FrontalArea = frontalArea
        self.DragCoefficient = dragCoefficient
        self.DrivelineEfficiency = drivelineEfficiency
        self.MotorEfficiency = motorEfficiency
        self.BatteryCapacity = batteryCapacity 
        self.Voltage = voltage
        self.power_AC = power_AC
        self.power_Music = power_Music
        self.power_Light = power_Light
        self.power_Coolent = power_Coolent
        
