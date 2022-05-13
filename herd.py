from dinosaur import Dinosaur

class herd:
    def __init__(self):
        self.dinosaurs = []

    def set_dinosaurs(self):
        first_dinosaur = Dinosaur('', 20)
        second_dinosaur = Dinosaur('', 20)
        third_dinosaur = Dinosaur('',20)
        self.robots = [first_dinosaur, second_dinosaur, third_dinosaur]