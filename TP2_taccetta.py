import math
import pylab as pl

class Perceptron():


    def __init__(self):
        self.w0 = 0.9 #0.88 | 0.89 | 0.89537 | 0.8987
        self.w1 = 0.66 #0.66 | 0.66 | 0.6625 | 0.6658
        self.w2 = -0.2 #-0.2 | -0.19 | -0.1925 | -0.1892
        self.bias = 1
        
        choice = int(input("Choose 1 for OR, 2 for AND, 3 for XOR: "))
        if choice == 1:
            print("OR")
            self.table = [(0,0,0), (0,1,1), (1,0,1), (1,1,1)]   
        if choice == 2:
            print("AND")
            self.table = [(0,0,0), (0,1,0), (1,0,0), (1,1,1)]
        if choice == 3:
            print("XOR")
            self.table = [(0,0,0), (0,1,1), (1,0,1), (1,1,0)]   
        
        self.real_output = 0
        self.desire_solution = 0
        
        self.w0_evhistory = (self.w0, )
        self.w1_evhistory = (self.w1, )
        self.w2_evhistory = (self.w2, )
        
        self.error_01 = ()
        self.error_02 = ()
        self.error_03 = ()
        self.error_04 = ()
        
        self.count = 0
        self.start()


    def start(self):
        for i in range(10000):
            self.calculate()

                
        self.ploteo()


    def calculate(self):
        for i in range(4):
            self.input_values(self.table[i][0], self.table[i][1])
            self.desire_solution = self.table[i][2]
            print("SD: ", self.table[i][2])
            epsilon = self.desire_solution - self.real_output
            self.error_append(epsilon)
            delta = self.real_output * (1 - self.real_output) * epsilon
            
            delta_w0 = (0.1 * self.bias * delta) + self.w0
            self.w0 = delta_w0
            self.w0_evhistory = self.w0_evhistory + (delta_w0, )
            print("w0: ", self.w0)
            
            delta_w1 = (0.1 * self.table[i][0] * delta) + self.w1
            self.w1 = delta_w1
            self.w1_evhistory = self.w1_evhistory + (delta_w1, )
            print("w1: ", self.w1)
            
            delta_w2 = (0.1 * self.table[i][0] * delta) + self.w2
            self.w2 = delta_w2
            self.w2_evhistory = self.w2_evhistory + (delta_w2, )
            print("w2: ", self.w2, "\n")
            
            self.count += 1
            if self.count == 4:
                self.count = 0

    def input_values(self, e1, e2):
        input_sum_x = self.w0 * self.bias + self.w1 * e1 + self.w2 * e2
        print("sum: ", input_sum_x)
        self.real_output = 1/(1+math.e**-input_sum_x)
        print("SR: ", self.real_output)

    
    def error_append(self, error):
        if self.count == 0:
            self.error_01 = self.error_01 + (error, )
        if self.count == 1:
            self.error_02 = self.error_02 + (error, )
        if self.count == 2:
            self.error_03 = self.error_03 + (error, )
        if self.count == 3:
            self.error_04 = self.error_04 + (error, )
    
    def ploteo(self):
        
        pl.plot(self.error_01)
        pl.plot(self.error_02)
        pl.plot(self.error_03)
        pl.plot(self.error_04)
        pl.show()


if __name__ == '__main__':
    
    bot = Perceptron()