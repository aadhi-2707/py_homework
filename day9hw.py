class Employee:
    def __init__(self, name: str, role: str):   # fixed __init__
        self.name = name
        self.role = role

    def display(self):
        print(f"Name: {self.name}, Role: {self.role}")


class Trainer(Employee):
    def __init__(self, name: str, role: str, specialization: str):  # fixed __init__
        super().__init__(name, role)  # fixed super call
        self.specialization = specialization

    def display(self):
        print(f"Name: {self.name}, Role: {self.role}, Specialization: {self.specialization}")


class YogaInstructor(Employee):
    def __init__(self, name: str, role: str, yoga_style: str):  # fixed __init__
        super().__init__(name, role)
        self.yoga_style = yoga_style

    def display(self):
        print(f"Name: {self.name}, Role: {self.role}, Yoga Style: {self.yoga_style}")


class MultiTrainer(Trainer, YogaInstructor):
    def __init__(self, name: str, role: str, specialization: str, yoga_style: str):  # fixed __init__
        Employee.__init__(self, name, role)  # explicitly call Employee init
        self.specialization = specialization
        self.yoga_style = yoga_style

    def display(self):
        print(
            f"Name: {self.name}, Role: {self.role}, "
            f"Specialization: {self.specialization}, Yoga Style: {self.yoga_style}"
        )


# ----------- Example Usage -----------
emp = Employee("Alice", "Receptionist")
trainer = Trainer("Bob", "Trainer", "Strength Training")
yoga_instructor = YogaInstructor("Clara", "Yoga Instructor", "Hatha Yoga")
multi_trainer = MultiTrainer("David", "MultiTrainer", "CrossFit", "Ashtanga Yoga")

emp.display()
trainer.display()
yoga_instructor.display()
multi_trainer.display()
