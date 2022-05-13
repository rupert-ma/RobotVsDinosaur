from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.set_dinosaurs()

    def set_dinosaurs(self):
        first_dinosaur = Dinosaur(True)
        second_dinosaur = Dinosaur(True)
        third_dinosaur = Dinosaur(True)
        self.dinosaurs = [first_dinosaur, second_dinosaur, third_dinosaur]