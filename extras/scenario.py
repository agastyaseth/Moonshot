import energy_consumption_model as em 
from nissan_leaf import NissanLeaf

 
wheel_power = em.EnergyConsumptionModel.ComputePowerToWheels(em,vehicle = NissanLeaf , roadGrade = 0 ,  acceleration = 0 ,velocity =  45)
traction_power = em.EnergyConsumptionModel.ComputeTractionPowerAtMotor(em,powerToWheels = wheel_power , vehicle = NissanLeaf )
regenerative_efficiency = em.EnergyConsumptionModel.ComputeRegenerativeBrakingefficiency(em,acceleration = 0 )
regenerative_power = em.EnergyConsumptionModel.ComputeRegenerationPowerAtMotor(em,powerAtMotor = traction_power , vehicle = NissanLeaf , RegenerativeEfficiency = regenerative_efficiency)
aux_power = em.EnergyConsumptionModel.ComputePoweratAux(em,vehicle = NissanLeaf)
net_power = em.EnergyConsumptionModel.ComputePoweratMotor_Net(em,powerAtMotor = traction_power , powerAtAux = aux_power, powerAtRegen = regenerative_power)
EC = em.EnergyConsumptionModel.ComputeEnergyConsumption( em,Power_Net = net_power , duration_till_now = 0.3  ,distance_till_now = 25 )
new_soc = em.EnergyConsumptionModel.ComputeChangeInStateOfCharge(em, SOC = 95 ,Power_Net = net_power , vehicle = NissanLeaf )
print(new_soc)
range = em.EnergyConsumptionModel.predict_range(em, delta_SOC = new_soc ,duration_remaining = 0.5 , EC = EC , vehicle = NissanLeaf )
print(range)