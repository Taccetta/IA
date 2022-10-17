import math
import pylab as pl
import TP3_final_node as fn
import random
import os

class Perceptron():


    def __init__(self):
        self.w = [0.9, 0.7, 0.5, 0.3, -0.9, -1, 0.8, 0.35, 0.1]

        self.bias = 1
        self.table = [(0,0,0), (0,1,1), (1,0,1), (1,1,0)]
        
        self.n_nodes = int(input("Set number of nodes: "))
        if self.n_nodes > 3:
            for i in range((self.n_nodes-3)*3):
                rand = round(random.uniform(-1, 1), 2)
                self.w.append(rand)
        self.real_output = [0 for i in range(self.n_nodes)]
        self.desire_solution = 0
        self.node_output = []
        self.node_iteration = 0
        self.count = 0
        self.RL = 0.1
    
        self.final_node = fn.Perceptron()
        self.final_node.nodes_attached = self.n_nodes
        self.final_node.w = [-0.23, -0.79, 0.56, 0.6]
        if self.n_nodes > 3:
            for i in range(self.n_nodes-3):
                rand = round(random.uniform(-1, 1), 2)
                self.final_node.w.append(rand)
        
        self.error_list = [() for i in range(len(self.w)+ self.n_nodes + 1)]

        self.start()


    def start(self):
        for iteration in range(10000):
            print("\n###\nIteration: ", iteration+1, "\n###")
            self.calculate()
        #self.ploteo()


    def set_final_node(self):
        print("==================== Final Node ========================")
        self.final_node.input_node_exit = self.real_output
        self.final_node.desire_solution = self.desire_solution
        print("Desire solution: ", self.final_node.desire_solution)
        self.final_node.calculate()


    def calculate(self):

        for i in range(4):
            for node in range(self.n_nodes):
                print("========== Node: ", node, "==========")
                self.node_iteration = node
                self.input_values(self.table[i][0], self.table[i][1])
                self.desire_solution = self.table[i][2]
                #print("SD: ", self.table[i][2])
            
            
            self.set_final_node()
            self.set_backforward_w()
            #a = input("pause")

            self.count += 1
            if self.count == 4:
                self.count = 0
        
        print("Error: ", self.final_node.error)

    def input_values(self, e1, e2):
        input_sum_x = self.w[self.node_iteration*3] * self.bias + self.w[self.node_iteration*3+1] * e1 + self.w[self.node_iteration*3+2] * e2
        print("sum: ", input_sum_x)
        self.real_output[self.node_iteration] = 1/(1+math.e**-input_sum_x)
        print("SR: ", self.real_output[self.node_iteration])


    def set_backforward_w(self):
        count = 0
        for i in range(self.n_nodes):
            soc = self.real_output[i] * (1 - self.real_output[i]) * self.final_node.delta_f
            #print("soc: ", soc)
            for j in range(3):
                if j == 0:
                    print("previus value w", count,": ", self.w[count])
                    self.w[count] = (0.1 * self.bias * soc) + self.w[count]
                else:
                    print("previus value w", count,": ", self.w[count])
                    woc = (0.1 * self.table[self.count][j-1] * soc) + self.w[count]
                    self.w[count] = woc
                print("w", count, ": ", self.w[count], "\n")
                count += 1


if __name__ == '__main__':
    
    bot = Perceptron()