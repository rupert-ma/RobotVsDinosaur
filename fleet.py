from robot import Robot

class fleet:
    def __init__(self):
        self.robots = []
    
    def set_robots(self):
        first_robot = Robot('')
        second_robot = Robot('')
        third_robot = Robot('')
        self.robots = [first_robot, second_robot, third_robot]