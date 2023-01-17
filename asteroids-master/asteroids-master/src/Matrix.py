# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 15:40:08 2022

@author: Santiago
"""
import numpy as np
import random as randm


class Matrix():
    
    def __init__(self,rows, columns, data):
        self.rows= rows
        self.columns= columns
        if len(data)==0:
            self.data = np.zeros((rows, columns))
        else:
            self.data= data
            if np.shape(self.data)[0] != rows or np.shape(self.data)[1] !=columns:
                raise Exception("La data no concuerda")
    @staticmethod
    def add_matrix(m0, m1):
        Matrix.check_dimensions(m0, m1)
        mr= Matrix(m0.rows, m0.columns,[])
        
        for x in range(0,m0.rows):
            for y in range(0,m0.columns):
                mr[x][y]=m0[x][y] + m1[x][y]
        return mr
    @staticmethod
    def check_dimensions(m0, m1):
        if m0.rows!=m1.rows or m0.columns!=m1.columns:
            raise Exception("Las matrices no concuerdan")
        
    def rand_matrix(self):
        for x in range(0,self.rows):
            for y in range(0,self.columns):
                self.data[x][y]=randm.random()*2 -1

