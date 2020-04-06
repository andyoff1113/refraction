# -*- coding: cp950 -*-
from visual import *
from visual.graph import *

size = 0.5          
height = 15.0       
scene = display(width=600, height=600,x=0, y=0,
                center = (0,height/2,0), background=(0.5,0.5,0))
touchlist=[] #是否已碰觸
Llist=[]
l=0.05 #波通過介質1跟介質2交界處的長度，在介質1的波長為l*cos(theta1)，在介質2的波長為l*cos(theta2)
minDistance = 99999

def refraction_vector(ni, nf, touch_pos, in_vector):#(進折射率, 出折射率, 接觸點, 進向量)
 N_vector=touch_pos-glass.pos
 nor_in_vector=in_vector/abs(in_vector)
 nor_N_vector=N_vector/abs(N_vector)
 th1=diff_angle(in_vector,N_vector)
 th2=acos(sqrt(1-(1-cos(th1)*cos(th1)/e/e))) 
 ref_vector=(nor_in_vector/e)+nor_N_vector*(cos(th1)/e - cos(th2))
 nor_ref_vector=ref_vector/abs(ref_vector)
 print(th1)
 return nor_ref_vector

glass = sphere(radius = 10, color=color.white,opacity=0.1,pos=vector (10,height/2,0),
                    v=vector(0,0,0),make_trail= False, trail_type="points", interval=100,material=materials.glass) 

pointer = arrow(pos=(-25,height/3,0),axis=(0,5,0), shaftwidth=1)

for N in range(3):
      Llist.append(sphere(radius = size/4, color=color.yellow,
              make_trail= True, trail_type="curve", interval=100,pos=(-25,5+N*2.5,0),v=vector(0.01,0,0)) )
      Llist.append(sphere(radius = size/4, color=color.blue,
              make_trail= True, trail_type="curve", interval=100,pos=(-25,5+N*2.5,0),v=vector(0.01,-0.0005,0)))
for N in range(6):
      touchlist.append(0)
      #角膜1.3375 水晶體1.4 空氣1 玻璃1.55
      
gd = gdisplay(x=800,y=0,width=600,height=600,
              title='d-t', xtitle='t', ytitle='distance',
              foreground=color.black,background=color.white,
              xmax=20, xmin=-2, ymax=1.2, ymin=0)
f1 = gcurve(color=color.red)
f2 = gcurve(color=color.blue)
f3 = gcurve(color=color.green)



dt = 0.001                              
t = 0.0


while True:
 rate(500)
 t = t + dt
    
 for n in range(6):  
    if abs(Llist[n].pos-glass.pos)<=10 and (touchlist[n]==0)and t<=2.9:
            Llist[n].v=refraction_vector(1,1.55,Llist[n].pos,Llist[n].v)/100
            touchlist[n]=1
           # print(Llist[n].v)
            
    if abs(Llist[n].pos-glass.pos)>=10 and touchlist[n]==1 and t>=3:
            Llist[n].v=refraction_vector(1.55,1,Llist[n].pos,Llist[n].v)/100
            touchlist[n]=2
            #print(Llist[n].v)
 tempDistance1 = abs(Llist[1].pos-Llist[0].pos)
 tempDistance2 = abs(Llist[3].pos-Llist[2].pos)
 tempDistance3 = abs(Llist[5].pos-Llist[4].pos)
 f1.plot(pos=(t,tempDistance1))
 f2.plot(pos=(t,tempDistance2))
 f3.plot(pos=(t,tempDistance3))
 if tempDistance1 <= minDistance and t>=3:
   minDistance = tempDistance1#儲存兩點距離

 for N in range(6):
      Llist[N].pos=Llist[N].pos+Llist[N].v#光子運動


