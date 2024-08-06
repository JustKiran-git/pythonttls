class Vehicle:
    def __init__(self, max_speed: int, mileage: float):
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    def __init__(self, max_speed: int, mileage: float, seating_capacity: int):
        super().__init__(max_speed, mileage)
        self.seating_capacity = seating_capacity

    def fare(self) -> float:
        return self.seating_capacity * 100 * 1.1  # Add 10% maintenance charge for Bus

if __name__ == "__main__":
    bus1 = Bus(120, 12, 50)
    print(f"Max Speed: {bus1.max_speed} km/h")
    print(f"Mileage: {bus1.mileage} km/l")
    print(f"Seating Capacity: {bus1.seating_capacity}")
    print(f"Total Fare: ${bus1.fare():.2f}")

    bus2 = Bus(100, 10, 30)
    print(f"Max Speed: {bus2.max_speed} km/h")
    print(f"Mileage: {bus2.mileage} km/l")
    print(f"Seating Capacity: {bus2.seating_capacity}")
    print(f"Total Fare: ${bus2.fare():.2f}")
