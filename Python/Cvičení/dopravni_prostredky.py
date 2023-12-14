class Vehicle:
    
    def __init__(self, id, location):
        self.id = id
        self.location = location
        
    def move_to(self):
        raise NotImplementedError("error")
    
class WaterVehicle(Vehicle):
    pass

vehicles = [
    WaterVehicle(id='Titanic', current_location='Liverpool'),
    ##GroundVehicle(id='Humvee', current_location='Baghdad'),
    ##AirVehicle(id='Air Force One', current_location='Washington')
    ]
 
for vehicle in vehicles:
    vehicle.move_to('Prague')
    print(vehicle)