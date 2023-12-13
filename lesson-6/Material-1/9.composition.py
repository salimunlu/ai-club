class Address:
    def __init__(self, street, city, state, zipcode):
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def __str__(self):
        lines = [self.street]
        lines.append(f"{self.city}, {self.state}, {self.zipcode}")
        return "\n".join(lines)

address1 = Address("Park St.", "NYC", "NY", "12345")
print(address1)


class Employee:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name

        self.address = None

    def set_address(self, address: Address):
        self.address = address

    def __str__(self):
        return f"Employee ID: {self.employee_id}\nName: {self.name}\nAddress:\n{self.address}"


emp1 = Employee(1, "John")
address1 = Address("Park St.", "NYC", "NY", "12345")
print(address1)

emp1.set_address(address1)
print(emp1)


emp2 = Employee(2, "Jill")
emp2.address

adress2 = Address("Central St.", "LA", "CA", 34567)
emp2.set_address(adress2)
emp2.address
print(emp2.address)
print(emp2)


