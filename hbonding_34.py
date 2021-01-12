#!/usr/bin/env python
# coding: utf-8

# python3.5 hbond_34.py

import getopt
import sys
import os,os.path
import math
import numpy as np
class Atom:
	def __init__(self,atype,resid,x,y,z):
		self.x =x
		self.y =y
		self.z =z
		self.resid = resid
		self.atype = atype

	def findDistance(self,another_atom):
		del_x = self.x - another_atom.x
		del_x = del_x * del_x
		del_y = self.y - another_atom.y
		del_y = del_y * del_y
		del_z = self.z - another_atom.z
		del_z = del_z * del_z
		val = math.sqrt(del_x + del_y + del_z)
		return val
	def findangle(self,another_atom1,another_atom2):
		a = np.array([self.x, self.y,self.z])
		b = np.array([another_atom1.x, another_atom1.y,another_atom1.z])
		c = np.array([another_atom2.x, another_atom2.y,another_atom2.z])
		ba = a - b
		bc = c - b
		cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
		angle = np.arccos(cosine_angle)
		angle_deg=np.degrees(angle)
		return angle_deg  


# In[23]:
def frange(start, stop, step):
	i = start
	while i <= stop:
		yield i
		i += step

for tw in range(5,65,5):
	for slide in frange(-2.5,2.5,0.5):
		for roll in range(-20,25,5):
			my_file="tw"+str(tw)+"/"+"str"+str(tw)+"."+str(roll)+"."+str(slide)+".pdb"
			if os.path.exists(my_file):
				fp=open(my_file,'r')

#fp = open("str30.10.0.5.pdb" ,"r")
			my_file1="str"+str(tw)+"."+str(roll)+"."+str(slide)+".pdb"
			my_out="tw"+str(tw)+"_34.out"
			fw=open(my_out,'a')
			allatoms = []
			for line in fp:
				if line[0:4]=="ATOM":
					atype=str(line[13:16]).strip()
					x=float(line[30:38])
					y=float(line[38:46])
					z =float(line[48:56])
					resid=int(line[25:26])
					atom = Atom(atype,resid,x,y,z)
					allatoms.append(atom)


# In[35]:

			p="yes"
			q="no"
			l=len(allatoms)
			list1=[]
			list12=[]
			list2=[]
			list3=[]
			for i in range(0,l):
				if (allatoms[i].atype=="H61") and (allatoms[i].resid==4):
					list1.append(allatoms[i])
				if (allatoms[i].atype=="H62") and (allatoms[i].resid==4):
					list12.append(allatoms[i])
				if (allatoms[i].atype=="O4") and (allatoms[i].resid==3):
					list2.append(allatoms[i])
				if (allatoms[i].atype=="N6") and (allatoms[i].resid==4):
					list3.append(allatoms[i])
#			for i in range(0,len(list1)):
#    				print(list1[i].x)
#			for i in range(0,len(list2)):
#				print(list2[i].x)
#				print(list3[i].x)
			for i in range(0,len(list1)):
				print(type(list1[i]))
				h_dist= list1[i].findDistance(list2[i])
#				print(str(h_dist) + "##")
				h_dist1= list12[i].findDistance(list2[i])
#				print(str(h_dist1) + "###")
				h_ang = list3[i].findangle(list1[i],list2[i])
				h_ang1 = list3[i].findangle(list12[i],list2[i])
				if ((h_dist < 3.0) and (h_ang > 90)) or ((h_dist1 < 3.0) and (h_ang1 > 90)):
					line = '%s   %s  \n' % (str(my_file1), str(p))
					fw.write(line)
				else:
					line = '%s   %s  \n' % (str(my_file1), str(q))
					fw.write(line)
 




