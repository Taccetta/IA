import math
import pylab as pl
import TP6_final_node as fn
import random
import numpy as np
from PIL import Image
import os


class Perceptron():


    def __init__(self):
        
        self.path = str(os.path.abspath(__file__)[:-15])
        
        
        self.bias = 1
        self.table = [(0,0,0), (0,1,1), (1,0,1), (1,1,0)]

        self.w = []
        self.n_nodes = int(input("Set number of nodes: "))
        for i in range(self.n_nodes*7680 + self.n_nodes):
            rand = round(random.uniform(-1, 1), 2)
            self.w.append(rand)

        self.real_output = [0 for i in range(self.n_nodes)]
        self.desire_solution = 0
        
        self.node_iteration = 0
        self.count = 0
        self.RL = 0.01
    
        self.final_node = fn.Perceptron()
        self.final_node.nodes_attached = self.n_nodes
        self.final_node.w = []

        for i in range(self.n_nodes + 1):
            rand = round(random.uniform(-1, 1), 2)
            self.final_node.w.append(rand)
        
        self.w_values_list = [() for i in range(len(self.w)+ self.n_nodes + 1)]
        self.error_list = [() for i in range(4)]

        self.subject_A = [() for i in range(8)]
        self.subject_B = [() for i in range(8)]


        self.start()


    def start(self):
        self.subject_set()
        a = input("pause")
        for iteration in range(10000):
            print("Iteration: ", iteration+1)
            self.calculate()
        self.ploteo()


    def set_final_node(self):
        #print("==================== Final Node ========================")
        self.final_node.input_node_exit = self.real_output
        self.final_node.desire_solution = self.desire_solution
        #print("Desire solution: ", self.final_node.desire_solution)
        self.final_node.calculate()


    def calculate(self):

        for i in range(4):
            for node in range(self.n_nodes):
                #print("========== Node: ", node, "==========")
                self.node_iteration = node
                self.input_values(self.table[i][0], self.table[i][1])
                self.desire_solution = self.table[i][2]
                ##print("SD: ", self.table[i][2])
            
            self.set_final_node()
            #self.w_final_node_value_append(self.final_node.w)
            self.set_feedforward_w()
            #a = input("pause")
            self.error_append()

            self.count += 1
            if self.count == 4:
                self.count = 0
        
        
        #print("Error: ", self.final_node.error)

    def input_values(self, e1, e2):
        input_sum_x = self.w[self.node_iteration*3] * self.bias + self.w[self.node_iteration*3+1] * e1 + self.w[self.node_iteration*3+2] * e2
        #print("sum: ", input_sum_x)
        self.real_output[self.node_iteration] = 1/(1+math.e**-input_sum_x)
        #print("SR: ", self.real_output[self.node_iteration])


    def set_feedforward_w(self):
        count = 0
        for i in range(self.n_nodes):
            soc = self.real_output[i] * (1 - self.real_output[i]) * self.final_node.delta_f
            ##print("soc: ", soc)
            for j in range(3):
                if j == 0:
                    #print("previus value w", count,": ", self.w[count])
                    self.w[count] = (0.1 * self.bias * soc) + self.w[count]
                else:
                    #print("previus value w", count,": ", self.w[count])
                    woc = (0.1 * self.table[self.count][j-1] * soc) + self.w[count]
                    self.w[count] = woc
                #print("w", count, ": ", self.w[count], "\n")
                #self.w_value_append(self.w[count], count)
                count += 1

    def w_value_append(self, w_new, count):
        self.w_values_list[count] = self.w_values_list[count] + (w_new, )
        
    def w_final_node_value_append(self, w_new):
        for i in range(len(w_new)):
            self.w_values_list[i+len(self.w)] = self.w_values_list[i+len(self.w)] + (w_new[i], )
        
    

    def error_append(self):
        self.error_list[self.count] = self.error_list[self.count] + (round(self.final_node.error, 5), )

    def ploteo(self):
        # for i in range(len(self.w_values_list)):
        #     pl.plot(self.w_values_list[i])
        # pl.show()

        for i in range(len(self.error_list)):
            pl.plot(self.error_list[i])
        pl.show()


    def subject_set(self):

        
        for i in range(8):
            img=Image.open(self.path + 'Persona' + "0/" + str(i+1) +'A57190.jpg')
            array= np.array(img)
            
            print(len(array[0]))


if __name__ == '__main__':
    
    bot = Perceptron()