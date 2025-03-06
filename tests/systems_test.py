import transformations as tr
import matplotlib.pyplot as plt
import numpy as np
import transformplot3d as tp3

d2r = np.deg2rad

#Absolute system, at the origin with no rotations
SysA = tr.identity_matrix()
#System B with respect to A
SysBA = tr.translation_matrix([1,0,1.5]) @ tr.euler_matrix(d2r(30),0,d2r(45))
#System C with respect to A
SysCA = [[1,0,0,-5],[0,-1,0,-3],[0,0,-1,-1],[0,0,0,1]]
#System D with respect to A
SysDA = tr.translation_matrix([-4,2,-3]) @ tr.euler_matrix(0,0,d2r(45))

#Origins of systems
OrgA = tr.translation_from_matrix(SysA)
OrgBA = tr.translation_from_matrix(SysBA)
OrgCA = tr.translation_from_matrix(SysCA)
OrgDA = tr.translation_from_matrix(SysDA)

#System C with respect to B = System A with respect to B * System C with respect to A
#System A with respect to B = inverse(SysBA)
SysCB = tr.inverse_matrix(SysBA) @ SysCA

#Point 1 in system C
p1C,P1C = tp3.reduced_and_extended([1,0,1,1])
#Point 1 in system A
p1A,P1A = tp3.reduced_and_extended(np.dot(SysCA,P1C))
#Point 1 in system A
p1B,P1B = tp3.reduced_and_extended(np.dot(SysCB,P1C))

#Points 1, 2 and 3 in system D
p1D,P1D = tp3.reduced_and_extended([-1.5,0,0,1])
p2D,P2D = tp3.reduced_and_extended([0,-2,0,1])
p3D,P3D = tp3.reduced_and_extended([0,0,-1,1])

#Get list to input the quivers with
xAx,yAx,zAx,uAx,vAx,wAx = tp3.draw_axes_from_matrices([SysA,SysBA,SysCA,SysDA])
x1,y1,z1,u1,v1,w1 = tp3.many_vectors_many_systems([p1A,p1B,p1C],[SysA,SysBA,SysCA])
x2,y2,z2,u2,v2,w2 = tp3.many_vectors_one_system([p1D,p2D,p3D],SysDA)

#Use matplotlib to show everything 
ax = plt.figure().add_subplot(111,projection='3d')
ax.quiver(xAx,yAx,zAx,uAx,vAx,wAx,color=('r','g','b'))
ax.quiver(x1,y1,z1,u1,v1,w1,arrow_length_ratio=0.1,color=('C0','C1','C2'))
ax.quiver(x2,y2,z2,u2,v2,w2,arrow_length_ratio=0.1,color=('C4'))

ax.set_xlim([-6, 4])
ax.set_xlabel('X-axis')
ax.set_ylim([-6, 4])
ax.set_ylabel('Y-axis')
ax.set_zlim([-6, 4])
ax.set_zlabel('Z-axis')

ax.text(OrgA[0],OrgA[1],OrgA[2],'A')
ax.text(OrgBA[0],OrgBA[1],OrgBA[2],'B')
ax.text(OrgCA[0],OrgCA[1],OrgCA[2],'C')
ax.text(OrgDA[0],OrgDA[1],OrgDA[2],'D')

ax.view_init(elev=25, azim=50, roll=0)
plt.show()