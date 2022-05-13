from robot import Robot

class fleet:
    def __init__(self):
        self.robots = []
    
    def set_robots(self):
        first_robot = Robot(True)
        second_robot = Robot(True)
        third_robot = Robot(True)
        self.robots = [first_robot, second_robot, third_robot]