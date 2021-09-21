import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for k,v in kwargs.items():
            for i in range(0,v):
                self.contents.append(k)
            
    def draw(self, number):
        if number >= len(self.contents):
            return self.contents
        
        drawn_balls = []
        for n in range(number):
            len_contents = len(self.contents)
            index = random.randrange(len_contents)
            ball = self.contents[index]
            drawn_balls.append(ball)
            self.contents.remove(ball)
        
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    for n in range(num_experiments):
        copy_hat = copy.deepcopy(hat)
        drawn_balls = copy_hat.draw(num_balls_drawn)
        Flag = True
        for key in expected_balls.keys():
            if drawn_balls.count(key) < expected_balls[key]:
                Flag = False
                break
        if Flag:
            m += 1

    probability = m / num_experiments
    return probability