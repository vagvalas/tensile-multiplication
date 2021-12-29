from array import *
import numpy

F = [[1, 2, 3,4], [ 5,6,7,8], [ 9,10,11,12], [13,14,15,16]]
S = [[1,2,3], [4,5,6], [7,8,9]]
print(F,S)
r1 = len(F)
c1 = len(F[0])
r2 = len(S)
c2 = len(S[0])
print ("Oi pinakes einai:")
print ("1os:",r1,"x",c1)
print ("2os:",r2,"x",c2)
T = numpy.zeros((r1*r2,c1*c2)) #pollaplasiazw tis stilles epi tis grammes
r3 = 0
c3 = 0
for i in range (0,r1):
    
    
    for j in range (0,c1):
        k = 0
        for b in range (r3,r3+r2):
            l=0
            for n in range (c3,c3+c2):
                T[b][n] = F[i][j]*S[k][l]
                l = l +1
            k = k +1
        c3 = c3 + c2     #se kathe stili poy teleiwni tou FIRST pinaka, metakinw +c2 stis stiles toses oses itan kai oi stiles toy First antistoixws ston THIRD
    c3 =0                   #midenizw tis kainouries steiles, gia na katevw apo katw grammi me 0 stili
    r3 = r3 +r2         #se kathe teleiwma stilis PRWTOU pinaka, metakinw se +r2 GRAMMI toy THIRD pinaka
print (T)