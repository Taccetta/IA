import math
import pylab as pl
import TP3_final_node as fn
import os

class Perceptron():


    def __init__(self):
        self.w = [0.9, 0.7, 0.5, 0.3, -0.9, -1, 0.8, 0,35, 0.1]

        self.bias = 1
        self.table = [(0,0,0), (0,1,1), (1,0,1), (1,1,0)]
        
        self.n_nodes = 3
        #self.n_nodes = int(input("Set number of nodes: "))
        self.real_output = [0 for i in range(self.n_nodes)]
        self.desire_solution = 0
        self.node_output = []

        self.node_iteration = 0
        self.count = 0
        self.final_node = fn.Perceptron()
        self.final_node.w = [-0.23, -0.79, 0.56, 0.6]

        self.start()


    def start(self):
        for i in range(1):
            self.calculate()
        #self.ploteo()


    def set_final_node(self):
        self.final_node.table = self.real_output
        self.final_node.desire_solution = self.desire_solution
        print("$·!$·!", self.final_node.desire_solution)
        self.final_node.calculate()


    def calculate(self):
        for i in range(4):
            for node in range(self.n_nodes):
                print("============================================")
                self.node_iteration = node
                self.input_values(self.table[i][0], self.table[i][1])
                self.desire_solution = self.table[i][2]
                print("SD: ", self.table[i][2])
                epsilon = self.desire_solution - self.real_output[self.node_iteration]
                delta = self.real_output[self.node_iteration] * (1 - self.real_output[self.node_iteration]) * epsilon
                delta_w = (0.1 * self.bias * delta) + self.w[i]
                self.w[i] = delta_w
                print("w", node, ": ", self.w[i], "\n")
            
            self.set_final_node()
            self.set_backforward_w()
            a = input("pausa")

            self.node_iteration = 0
            self.count += 1
            if self.count == 4:
                self.count = 0

    def input_values(self, e1, e2):
        input_sum_x = self.w[self.node_iteration*3] * self.bias + self.w[self.node_iteration*3+1] * e1 + self.w[self.node_iteration*3+2] * e2
        print("sum: ", input_sum_x)
        self.real_output[self.node_iteration] = 1/(1+math.e**-input_sum_x)
        print("SR: ", self.real_output[self.node_iteration])


    def set_backforward_w(self):
        final_error = self.desire_solution - self.final_node.real_output
        print(final_error)
        delta_f = self.final_node.real_output * (1 - self.final_node.real_output) * final_error
        for i in range(self.n_nodes * 3):
            woc = 0.1 * ent * asdfasd


if __name__ == '__main__':
    
    bot = Perceptron()