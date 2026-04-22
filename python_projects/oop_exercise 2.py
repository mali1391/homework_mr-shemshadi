class Vehicle:

    def __init__(self, inner_city_vehicle, passenger_vehicle):
        self.inner_city_vehicle = inner_city_vehicle
        self.passenger_vehicle = passenger_vehicle

    def describe(self):
        if self.inner_city_vehicle:
            self.passenger_vehicle == False
            message = f"Status of inner_city_vehicle: {self.inner_city_vehicle}"
            return message
        elif self.passenger_vehicle == True:
            self.inner_city_vehicle == False
            massage = f"Status of passenger_vehicle: {self.passenger_vehicle}"
            return massage

class Train(Vehicle):

    def __init__(self, inner_city_vehicle, passenger_vehicle, ticket_price, stations):
        Vehicle.__init__(self, inner_city_vehicle, passenger_vehicle)
        self.ticket_price = ticket_price
        self.stations = stations


    def describe(self):
        base = Vehicle.describe(self)
        message = base + f", ticket price: {self.ticket_price}, stations: {self.stations}"
        return message

class Bus(Train):
    def __init__(self, inner_city_vehicle, passenger_vehicle, ticket_price,traffic_time):
        Train.__init__(self, inner_city_vehicle, passenger_vehicle, ticket_price)
        self.traffic_time = traffic_time

    def describe(self):
        base = Train.describe(self)
        message = base + f"please wait, because the traffic time is :{self.traffic_time}"
        return message

class Plane:
    def __init__(self, inner_city_vehicle, passenger_vehicle, ticket_price, terminal):
        Train.__init__(self, inner_city_vehicle, passenger_vehicle, ticket_price)
        self.terminal = terminal

    def describe(self):
        base = Train.describe(self)
        message = base + f", ticket price: {self.ticket_price}"
        return message

vehicle = input("Enter your vehicle:")
type_of_vehicle = input("Enter type of vehicle:")
if type_of_vehicle == "inner city":
    if vehicle == "train":
        inner_city_train_stations = [
            "shahid dasgheib",
            "shadi doran",
            "zandie",
            "shahed"
            "ehsan"
        ]
        Train_station_result = Train(True, False, 25368, inner_city_train_stations)
        print(Train_station_result.describe())

    elif vehicle == "bus":
        inner_city_bus_station = [
            "zand",
            "fazilat",
            "modares"
        ]
        bus_station = Bus(True, False, 8125, inner_city_bus_station)
        print(bus_station.describe())
elif type_of_vehicle == "passenger":
    if vehicle == "Train":
        passenger_stations = ["shiraz", "ahvaz", "tehran", "esfahan"]
        passenger_Train_result = Train(False, True, 56824, passenger_stations)
        print(passenger_Train_result.describe())

    elif vehicle == "bus":
        passenger_bus_station = ["mashad", "gholestan", "gilan", "tehran"]
        passenger_bus_result = Bus(False, True, 4552, passenger_bus_station)

    elif vehicle == "plane":
        terminals = ["shiraz", "tehran", "mashad", "qeshm"]
        plane_result = Plane(False, True, 4558622, terminals)