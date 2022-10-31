import math
import pylab as pl
import TP6_final_node as fn
import random
import numpy as np
from PIL import Image
import os
from itertools import product



class Perceptron():


    def __init__(self):
        
        self.rango = int(input("Set number of images (even number, min: 2, max: 16): "))
        self.rounding = int(input("Set rounding factor (10 recomended): "))
        
        self.path = str(os.path.abspath(__file__)[:-15])
        
        self.bias = 1
        self.table = []

        self.w = []
        self.n_nodes = int(input("Set number of nodes: "))
        for i in range(self.n_nodes*7680 + self.n_nodes):
            rand = round(random.randint(-100, 100), 2)
            self.w.append(np.float64(rand/100))


        self.real_output = [0 for i in range(self.n_nodes)]
        self.desire_solution = 0
        
        self.node_iteration = 0
        self.count = 0
        self.RL = 0.5
    
        self.final_node = fn.Perceptron()
        self.final_node.nodes_attached = self.n_nodes
        self.final_node.w = []

        for i in range(self.n_nodes + 1):
            rand = round(random.uniform(-1, 1), 2)
            self.final_node.w.append(rand)
        
        self.w_values_list = [() for i in range(len(self.w)+ self.n_nodes + 1)]
        self.error_list = [() for i in range(self.rango)]

        self.image_tuple = []

        self.row = 96
        self.column = 80
        
        self.divisor_for_inputvalues = 1000000
        self.supersum = 0
        
        self.persona_error = 0

        self.start()

    
    def start(self):

        self.subject_set()
        iterations = int(input("Number of iterations: "))
        for iteration in range(iterations):
            print("Iteration: ", iteration+1)
            self.calculate()
        self.ploteo()
        
        self.open_to_check()
        #self.learning_w_exporter()


    def set_final_node(self):
        #print("==================== Final Node ========================")
        self.final_node.input_node_exit = self.real_output
        self.final_node.desire_solution = self.desire_solution
        #print("Desire solution: ", self.final_node.desire_solution)
        self.final_node.calculate()

    
    def calculate(self):
        self.persona_error = 0
        for i in range(self.rango):
            for node in range(self.n_nodes):
                #print("========== Node: ", node, "==========")
                self.node_iteration = node
                self.input_values(self.table[i])
                self.desire_solution = self.table[i][7680]
                #print("DS: ", self.table[i][7680])
            
            self.set_final_node()
            #self.w_final_node_value_append(self.final_node.w)
            self.set_feedforward_w()
            #a = input("pause")
            self.error_append()

            self.count += 1
            if self.count == self.rango:
                self.count = 0
            
            if self.count == self.rango/2:
                self.persona_error = 1
        
        
        print("Error: ", self.final_node.error)
        #print(self.w[0])

    
    def input_values(self, table):
        input_sum_x = self.w[self.node_iteration*7680] * self.bias 
        for i in range(7680):
            input_sum_x += np.float64(self.w[self.node_iteration*7680+1+i] * table[i]/self.divisor_for_inputvalues)
        input_sum_x = round(input_sum_x, self.rounding)
        #print("sum: ", input_sum_x)
        self.real_output[self.node_iteration] = np.float64(1/(1+np.exp(- input_sum_x)))
        #print("SR: ", self.real_output[self.node_iteration])
        


    def set_feedforward_w(self):
        count = 0
        for i in range(self.n_nodes):

            #iterations = input("hola: ")
            soc = self.real_output[i] * (1 - self.real_output[i]) * self.final_node.delta_f
            #print("soc: ", soc)
            for j in range(7680):
                if j == 0:
                    #print("previus value w", count,": ", self.w[count])
                    self.w[count] = np.float64((0.1 * self.bias * soc) + self.w[count])
                    #print(self.w[count])
                else:
                    #print("previus value w", count,": ", self.w[count])
                    woc = np.float64((0.1 * self.table[self.count][j-1] * soc) + self.w[count])
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
        #self.error_list[self.persona_error] = self.error_list[self.persona_error] + (round(self.final_node.error, 5), )
        self.error_list[self.count] = self.error_list[self.count] + (round(self.final_node.error, 5), )


    def ploteo(self):
        # for i in range(len(self.w_values_list)):
        #     pl.plot(self.w_values_list[i])
        # pl.show()

        for i in range(len(self.error_list)):
            pl.plot(self.error_list[i])
        pl.show()


    def subject_set(self):

        #Armar una lista con 7680 elementos y anexarlas a las listas de cada persona, 
        #seria una lista de 8 listas
        #despues pasarlos a los nodos, son 7680 por nodo
        #y comparar la salida, 0 si es persona A y 1 si es persona B
        #de hecho habria que agergar un valor 7681 que sea 0 o 1 respectivamente
        persona = 0
        count = 1
        
        for i in range(self.rango):
            #img=Image.open(self.path + 'Persona' + "0/" + str(i+1) +'A57190.jpg')
            img=Image.open(self.path + 'Persona' + str(persona) +'/' + str(count) +'.jpg')
            array= np.array(img)
            
            self.image_tuple = self.convert_to_tuple(array)
            self.table.append(self.image_tuple)
            self.table[i] = self.table[i] + (persona,)
            count += 1
            if count == self.rango/2+1:
                persona = 1
                count = 1
        
    def open_to_check(self):
        persona = 0
        count = 1
        for i in range(16-self.rango, self.rango, 1):
            #img=Image.open(self.path + 'Persona' + "0/" + str(i+1) +'A57190.jpg')
            img=Image.open(self.path + 'Persona' + str(persona) +'/' + str(count) +'.jpg')
            array= np.array(img)
            
            self.image_tuple = self.convert_to_tuple(array)
            self.table.append(self.image_tuple)
            self.table[i] = self.table[i] + (persona,)
            count += 1
            if count == self.rango/2+1:
                persona = 1
                count = 1
            
        for iteration in range(16-self.rango):
            print("Iteration check: ", iteration+1)
            self.calculate()
        self.ploteo()
        
            
    def learning_w_exporter(self):
        learning = open("learning.txt","w")
        learning.write(str((self.w, self.final_node.w)))
        learning.close()
    
    def convert_to_tuple(self, lista):
        tupleted = ()
        for i, j in product(range(0, self.row), range(0, self.column)):
            pixel = np.sum((int(lista[i][j][0]) + int(lista[i][j][1]) + int(lista[i][j][2]))) // 3
            
            tupleted = tupleted + (pixel,)
        
        return tupleted


if __name__ == '__main__':
    
    bot = Perceptron()