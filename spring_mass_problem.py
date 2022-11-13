import numpy as np
import matplotlib.pyplot as plt

class SpringMassProblem:

    def get_solution(n, o):
        m=2 #mass
        k=1200 #stiffnes
        F=[]
        # n = int(input('Enter the number of steps : '))
        # o = int(input('Enter F when t=0 : '))
        dt=0.1/n

        t=np.arange(0,0.1,dt)
        # print(t)
        for q in range (0,n):
            F.append(-200*t[q]+o)

        #zero arrays for displacements, velocity and acceleration
        d=[]
        v=[]
        a=[]

        # Step.1 initial conditions for t=0
        d.append(0)
        v.append(0)

        #Step.2 calculate a(t=0)
        a.append((F[0]-k*d[0])/m)

        #Step.3 calculate d(i=-1), central difference method
        e=d[0]-dt*v[0]+((dt**2)/2)*a[0]

        #Step.4 calculate d(i=1) for t=0.02
        d.append(((dt**2)*F[0]+(2*m-dt**2*k)*d[0]-m*e)/m)

        #Step.5 calculate d(i+1) for different t
        for i in range (1,n):
            d.append(((dt**2)*F[i]+(2*m-dt**2*k)*d[i]-m*d[i-1])/m)

        #Step.6 calculate a(i) for different t
        for j in range (1,n):
            a.append((F[j]-k*d[j])/m)

        #Step.7 calculate v(i) for different t
        for r in range (1,n):
            v.append((d[r+1]-d[r-1])/(2*dt))
        del d[-1]   
        # print (d,'displacement')
        # print (a, 'acceleration')
        # print (v, 'velocity')


        # plt.figure()
        # plt.plot(t, d,label='displacement')
        # plt.scatter(t, d)
        # plt.xlabel("t,sec")
        # plt.ylabel("displacement,ft")
        # plt.legend()

        # plt.figure()
        # plt.plot(t, v,label='velocity')
        # plt.scatter(t, v)
        # plt.xlabel("t,sec")
        # plt.ylabel("velocity,ft/s")
        # plt.legend()

        # plt.figure()
        # plt.plot(t, a,label='acceleration')
        # plt.scatter(t, a)
        # plt.xlabel("t,sec")
        # plt.ylabel("acceleration,ft/s^2")
        # plt.legend()

        # plt.show()
        return t, d
