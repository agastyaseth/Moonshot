
import math
import vehicle as vehicle

class EnergyConsumptionModel:
    """ Model used to simulate ev battery consumption. 
        Based on this paper: https://www.researchgate.net/publication/294112610_Power-based_electric_vehicle_energy_consumption_model_Model_development_and_validation
    """
    
    def __init__(self, GravitationAcceleration = 9.98066 , AirDensity = 1.2256 , lion_battery_efficiency = .90 ,   max_SOC = 95 ,min_SOC = 10 , AC = True ,   Music = True ,   Light = True ,   Coolent = True,   SOC = 95  ):
        self.GravitationAcceleration = GravitationAcceleration
        self.AirDensity = AirDensity
        self.lion_battery_efficiency = lion_battery_efficiency
        self.max_SOC = max_SOC
        self.min_SOC= min_SOC
        self.AC = AC
        self.Music = Music
        self.Light = Light
        self.Coolent =  Coolent  
        self.SOC = SOC
        
        
    
    def ComputePowerToWheels(self, vehicle , roadGrade , acceleration = 0, velocity = 45):
        """ Equation:
            Pwheels(t) = (ma(a) + mg * cos(theta) * (c_r/1000)(c_1v(t) + c_2) + (1/2) * rho_air * A_f * C_d * v^2(t) + mg*sin(theta)) * v(t)
            Where:
            Pwheels = the power to the vehicles wheels
            m = vehicle mass (m =1521^2kg for Nissan Leaf)
            a(t) = dv(t)/dt (acceleration of vehicle in [m/s]^2) and can be negative
            g = 9.8066 [m/s^2]
            theta = road grade
            c_r = 1.75 - Rolling resistance parameter
            c_1 = 0.0328 - Rolling resistance parameter
            c_2 = 4.575 - Rolling resistance parameter
            p_air = 1.2256 [kg/m^3] air density
            A_f = frontal area of vehicle (2.3316 m^2 for leaf)
            c_d =  drag coefficient of vehicle (0.28 for leaf)
            v(t) speed of vehicle in [m/s]
        """
        c_r = 1.75
        c_1 = 0.0328
        c_2 = 4.575
        powerToWheels = ((vehicle.Mass * acceleration) + (vehicle.Mass * 9.8) * math.cos(roadGrade) * (c_r/1000) * (c_1 * velocity + c_2) + 0.5 * self.AirDensity * vehicle.FrontalArea * vehicle.DragCoefficient * math.pow(velocity, 2) + (vehicle.Mass * 9.8) * math.sin(roadGrade)) * velocity

        return powerToWheels

    def ComputeTractionPowerAtMotor(self, powerToWheels, vehicle):
        """ Equation:
            Pelectricmotor(t) = Pwheels * 1+ (1 -nu_drivetrain) * 1+ (1 - nu_electricmotor)
        """
        
        powerAtMotor = powerToWheels * (1 + (1 - vehicle.DrivelineEfficiency)) * (1 + (1 - vehicle.MotorEfficiency))
        return powerAtMotor

    def ComputeRegenerationPowerAtMotor(self, powerAtMotor, vehicle ,RegenerativeEfficiency):
        """ Equation:
            Pelectricmotor(t) = Pelectricmotor(t) * nu_rb(t)t
        """
        powerAtMotor = powerAtMotor * (RegenerativeEfficiency)
        return powerAtMotor

    def ComputeChangeInStateOfCharge(self , SOC , Power_Net , vehicle):
        """
            deltaSOC_i(t) = SOC_i-1)(t) - (P_electricmotornet_i(t)/3600*Capacity_battery)
            P_electricmotornet_i(t) = Power consumed considering a battery efficiency of 90% and power consumed by auxilary systems (P_Auxiliary = 700 W)
            Capacity_battery is in Wh
            SOC_0 <= 95% >= 20%
        """
        delta_SOC = SOC - (Power_Net / (3600 * vehicle.BatteryCapacity))
        return delta_SOC

    def ComputeEnergyConsumption(self ,Power_Net , duration_till_now , distance_till_now):
        """
            EC [kWh/km] = (1/3600000) * integral_0^t P_electSricmotor_net(t)dt * (1/d) everything in hours 
        """
        EC = ((1/3600000) * Power_Net * duration_till_now) / distance_till_now
        f = open("EC.txt" , "w+")
        f.write("%d" %(EC))
        return EC

    def predict_range(self , delta_SOC , duration_remaining , EC , vehicle):
        range = ((1/1000) * vehicle.BatteryCapacity * self.SOC * duration_remaining )/EC
        f = open("range.txt" , "w+")
        f.write("%d" %(range))
        return range 
        
    def ComputePoweratMotor_Net(self , powerAtMotor , powerAtAux , powerAtRegen):
        power_Net = powerAtMotor*(1/0.9) + powerAtAux - powerAtRegen
        return power_Net

    def ComputePoweratAux(self , powerAtMotor , powerAtAC , powerAtSound , powerAtLight , powerAtCoolent):
        powerAtAux = 0 
        if self.AC :
            powerAtAux += vehicle.power_AC/60
        if self.Music :
            powerAtAux += vehicle.power_Music/60
        if self.Light :
            powerAtAux += vehicle.power_Light/60
        if self.Coolent :
            powerAtAux += vehicle.power_Coolent/60
        
        return powerAtAux
        
    def ComputeRegenerativeBrakingefficiency(self , acceleration):
        """
            nu_rb [%] = (E_recoverable [kWh]/ E_Available [kWh])
        """
        if acceleration < 0 :
            if acceleration > -0.5 :
                nu_rb = 0
            elif acceleration > -1 :
                nu_rb = 91
            elif acceleration > -1.5 :
                nu_rb = 95
            elif acceleration <= -1.5 :
                nu_rb = 98
        return nu_rb  
"""
    def ComputeEAvailable(self):
    #        E_available [kWh] = integrate_0^t P_wheels_negative(t) dt
        pass

    def ComputeNrb(self):
  #          u_rb = a(t) < 0 then e^(0.0411/abs(a(t)))^-1
  #                 a(t) >=0 then 0
        pass


    def ComputeERecoverable(self):
  #         E_recoverable = n_rb * E_available
        pass

# replaced the whoel above caluiculations using graphical data from the reasearch paper  
    
    def kwhToAh(self , kwh):
        return ((kwh * self.kwh_to_watt_hour_conversion_factor) / self.systemVoltage)
    
    def ahToKwh(self , ah):
        return((ah * self.systemVoltage)/self.kwh_to_watt_hour_conversion_factor)
        
    def charge(self , charge_duration , current ):
        charge = (charge_duration * self.lion_battery_efficiency * current )
        return self.ahToKwh(charge) / self.batteryCapacityKwh
    
    def expend(self , distance , elevation , speedTraveled):
        pass
    
    class Battery :

    timecycle = 1
    Capacity = 75000 # WH
    
    def chargeupbattery(self, SOCpresent , chargerate , time ):
        SOC_present += chargerate * time
        self.timecycle += 1 
        return SOC_present

    def capacity(self , SOCpresent , temperature):
        if timecycle = 3000:
            self.capacity = 0.95 * capacity


    def batteryeff(self , temp , road , tyre , weather ) :
        if (temeprature > 30) or (temperature < 15 ) :
            tempdiff = temp - opttemp
            effeiency_effect = 3
        # similarly for other conditions too


     
    
    
     def musicsystem_on(self , duration_left ):
        vehicle_range -= 3*(duration_left/60)
        SOC_present -= 3*(duration_left/60)*(music_conversion_rate)
    

    def musicsystem_off(self , duration_left ):
        vehicle_range += 3*(duration_left/60)
        SOC_present += 3*(duration_left/60)*(music_conversion_rate)
    
        
    def airconditioning_on(self , duration_left ):
        vehicle_range -= 8*(duration_left/60)
        SOC_present -= 8*(duration_left/60)*(aircondition_conversion_rate)
    
        
    def airconditioning_off(self , duration_left ):
        vehicle_range += 8*(duration_left/60)
        SOC_present += 8*(duration_left/60)*(aircondition_conversion_rate)
    
"""
