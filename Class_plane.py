import numpy as np
import string

class Plane:

    def __init__(self,file_name):
        self.data=[]
        Config_file=open(file_name,"r")
        file_lines=Config_file.readlines()
        for line in file_lines:
            line=line.split()
            list_temp=[]
            for digit in line:
                digit=float(digit)
                list_temp.append(digit)
            self.data.append(list_temp)
        Config_file.close

        self.velo_x=0
        self.velo_y=0
        self.cord_x=0
        self.cord_y=0

    @property
    def Weight(self):#质量
        return self.data[0][0]

    @property    
    def MotionInertia(self):#转动惯量
        return self.data[0][1]

    @property    
    def AeroCenter(self):#气动中心位置
        return self.data[0][2]

    @property    
    def Elevator(self):#升降舵位置
        return self.data[0][3]

    def get_Cm(self,alpha):#获取该迎角下的Cm,alpha>=-180,alpha<=180
        for i in range(1,len(self.data)):
            if (alpha==self.data[i][0]):
                return self.data[i][1]
            elif (alpha<self.data[i][0]):
                scale=(alpha-self.data[i][0])/(self.data[i][0]-self.data[i-1][0])
                return ((self.data[i][1]-self.data[i-1][1])*scale+self.data[i][1])
        return 0


    def get_Cd(self,alpha):#获取该迎角下的Cd,alpha>=-180,alpha<=180
        for i in range(1,len(self.data)):
            if (alpha==self.data[i][0]):
                return self.data[i][2]
            elif (alpha<self.data[i][0]):
                scale=(alpha-self.data[i][0])/(self.data[i][0]-self.data[i-1][0])
                return ((self.data[i][2]-self.data[i-1][2])*scale+self.data[i][2])
        return 0

    def get_Cl(self,alpha):#获取该迎角下的Cl,alpha>=-180,alpha<=180
        for i in range(1,len(self.data)):
            if (alpha==self.data[i][0]):
                return self.data[i][3]
            elif (alpha<self.data[i][0]):
                scale=(alpha-self.data[i][0])/(self.data[i][0]-self.data[i-1][0])
                return ((self.data[i][3]-self.data[i-1][3])*scale+self.data[i][3])
        return 0


    def show(self):
        print(self.data)

    def update_status(self,acce_x,acce_y):
        self.cord_x+=self.velo_x
        self.cord_y+=self.velo_y
        self.velo_x+=acce_x
        self.velo_y+=acce_x
        return (self.cord_x,self.velo_x)

     



#plane01=Plane("D:\\buaa_flight_simulator\\data\\Config_Cessna172.txt")
#plane01.show()
#print(plane01.get_Cl(60))