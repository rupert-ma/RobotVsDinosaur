from dinosaur import Dinosaur

class herd:
    def __init__(self):
        self.dinosaurs = []

    def set_dinosaurs(self):
        first_dinosaur = Dinosaur(True)
        second_dinosaur = Dinosaur(True)
        third_dinosaur = Dinosaur(True)
        self.robots = [first_dinosaur, second_dinosaur, third_dinosaur]