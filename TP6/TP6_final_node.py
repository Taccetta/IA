import math
import pylab as pl

class Perceptron():


    def __init__(self):
        self.w = []
        self.bias = 1

        self.input_node_exit = []
        self.nodes_attached = 0
        self.real_output = 0
        self.desire_solution = 0
        self.delta_f = 0
        self.error = 0
        self.count = 0



    def calculate(self):
        self.input_values(self.input_node_exit)
        
        #print("SD: ", self.desire_solution)
        epsilon = self.desire_solution - self.real_output
        delta = self.real_output * (1 - self.real_output) * epsilon
        self.w[0] = (0.1 * self.bias * delta) + self.w[0]
        #print("w", self.nodes_attached * 3, ": ", self.w[0], "\n")
        
        for i in range(len(self.input_node_exit)):
            delta_w = (0.1 * self.input_node_exit[i] * delta) + self.w[i+1]
            self.w[i+1] = delta_w
            #print("w", i + 1 + self.nodes_attached * 3, ": ", self.w[i+1], "\n")
            
        self.delta_f = delta
        self.error = epsilon
        self.count += 1
        if self.count == 4:
            self.count = 0

    def input_values(self, en):
        input_sum_x = self.w[0] * self.bias
        for i in range(len(self.w)-1):
            
            input_sum_x = input_sum_x + self.w[i+1] * en[i]
        #print("sum: ", input_sum_x)
        self.real_output = 1/(1+math.e**-input_sum_x)
        #print("SR: ", self.real_output)



if __name__ == '__main__':
    
    bot = Perceptron()