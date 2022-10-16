import math
import pylab as pl

class Perceptron():


    def __init__(self):
        self.w = []
        self.bias = 1

        self.table = []
        
        self.real_output = 0
        self.desire_solution = 0

        self.count = 0



    def calculate(self):
        print("============================================")
        self.input_values(self.table[0], self.table[1], self.table[2])
        
        print("SD: ", self.desire_solution)
        epsilon = self.desire_solution - self.real_output
        delta = self.real_output * (1 - self.real_output) * epsilon
        
        for i in range(len(self.w)):
            delta_w = (0.1 * self.bias * delta) + self.w[i]
            self.w[i] = delta_w
            print("w", i, ": ", self.w[i], "\n")
            
        self.count += 1
        if self.count == 4:
            self.count = 0

    def input_values(self, e1, e2, e3):
        input_sum_x = self.w[0] * self.bias + self.w[1] * e1 + self.w[2] * e2 +  self.w[3] * e3
        print("sum: ", input_sum_x)
        self.real_output = 1/(1+math.e**-input_sum_x)
        print("SR: ", self.real_output)



if __name__ == '__main__':
    
    bot = Perceptron()