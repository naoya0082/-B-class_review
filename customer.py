class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        print(f"{self.first_name} {self.family_name}")

if __name__ == "__main__":
    ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
    ken.full_name()  # "Ken Tanaka" という値を返す

    tom = Customer(first_name="Tom", family_name="Ford", age=57)
    tom.full_name()  # "Tom Ford" という値を返す