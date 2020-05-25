'''Code by Kuntal Kokate
May 12th,2020
Released under GNU GPL
'''
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import signal
import control

#if using termux
import subprocess
import shlex
#end if


#Defining the system
Slopes = np.array([0, 0, -20, -20, -40, -40, -40, -40, -40, -40]);
x = np.array([0 ,1,10,100,1000,10000,1e5,1e6,1e7])
Num = [1e9]
Den =  [1, 1010, 1e4]
s1 = signal.lti(Num ,Den)
w = np.logspace(0, 7, 1000)
w, mag, phase = signal.bode(s1, w)


#plotting the bode plot of loop gain
plt.figure()
plt.xlabel("$\omega$ (rad/s)")
plt.ylabel("Magnitude (dB)")
plt.title("Magnitude Plot")
plt.ylim(-100, 110)
plt.semilogx(w, mag)    # Bode magnitude plot
plt.vlines([10, 1000], -100,100,linestyles = 'dashed', color = 'b')
plt.text(1e5, -45, "-40dB/dec", rotation = -40)
plt.text(1e2*0.5, 70, "-20dB/dec", rotation = -25)
plt.vlines([31500], -100, 0, linestyles = 'dashed', color = 'r')
plt.text(32500-5000, -115, '$\omega_{1}$', color='r')
y = []
k = 100;
for i in range(len(x)-1):
    y.append(k)
    k+=Slopes[i]
y.append(k)
plt.plot(x,y)
plt.plot(31500, 0, 'o')
plt.grid()
# if using termux
plt.savefig('./figs/ee18btech11028/fig_1.pdf')
plt.savefig('./figs/ee18btech11028/fig_1.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11028/fig_1.pdf"))
# else


#Phase of loop gain
plt.figure()
plt.xlabel("$\omega$ (rad/s)")
plt.ylabel('Phase (deg)')
plt.title('Phase plot')
plt.xlim(1, 1e7)
plt.ylim(phase[-1]-10, 0)
plt.vlines([31500], phase[-1]-10, 0, linestyles = 'dashed', color = 'r')
plt.text(32500-5000, phase[-1]-23, '$\omega_{1}$', color='r')
plt.semilogx(w, phase,'g')          # Bode phase plot
plt.grid()
# if using termux
plt.savefig('./figs/ee18btech11028/fig_2.pdf')
plt.savefig('./figs/ee18btech11028/fig_2.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11028/fig_2.pdf"))
# else




#defining closed loop system
Numf = [1e6, 1e9]
Denf = [1, 1010, 1e4+1e9]
s2 = signal.lti(Numf ,Denf)
zeros = zeros = signal.ZerosPolesGain(s2).zeros
poles = signal.ZerosPolesGain(s2).poles
zeros = np.array(zeros)
poles = np.array(poles)



#pole zero plot
plt.figure()
plt.xlabel("$Re$")
plt.axhline(linewidth=2, color='black')
plt.axvline(linewidth=2, color = 'black')
plt.ylabel('$Im$')
plt.title("Pole zero plot")
plt.plot(np.real(zeros), np.imag(zeros), 'or', label = 'Zeros')
plt.plot(np.real(poles), np.imag(poles), 'Xb', label = 'Poles')
plt.vlines(np.real(poles)[0], -np.imag(poles)[0], np.imag(poles)[0], linestyles = 'dashed', color = 'r')
plt.text(-1000, 4000, "Z1")
plt.text(40, 2000, '(0,0)')
plt.text(np.real(poles)[0]+50, np.imag(poles)[0], "P1")
plt.legend()
plt.text(np.real(poles)[0]+50, np.imag(poles)[1], "P2")
plt.xlim(-1100, 200)
plt.grid()
# if using termux
plt.savefig('./figs/ee18btech11028/fig_3.pdf')
plt.savefig('./figs/ee18btech11028/fig_3.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11028/fig_3.pdf"))
# else


#Bode plot of closed loop system
w, Magf, Phasef = signal.bode(s2, w)
plt.figure()
plt.subplot(2,1,1)
plt.semilogx(w, Magf)
plt.ylabel("20log|T(j$\omega$| (dB)")
plt.title("Bode plot")
idx = (np.argmax(Magf))
plt.ylim(-20, 65)
plt.vlines(w[idx], -20 , 60, linestyles = 'dashed', color = 'g')
plt.plot(w[idx], -20,'x', zorder=10, clip_on=False, color='r', label= '$\omega_{0}$ = ' + "{:e}".format(w[idx]))
plt.text(w[idx]-5000, -29,'$\omega_{0}$',color = 'r')
plt.legend()
plt.grid()
plt.subplot(2,1,2)
plt.semilogx(w, Phasef)
plt.ylabel("Phase")
plt.xlabel("$\omega$ (rad/s)")
plt.grid()
# if using termux
plt.savefig('./figs/ee18btech11028/fig_4.pdf')
plt.savefig('./figs/ee18btech11028/fig_4.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11028/fig_4.pdf"))
# else



#For step response
T = np.linspace(0, 0.012, 10000)
sys = control.tf(Numf, Denf)
T, yout  = control.step_response(sys, T)

plt.figure()
plt.xlim(0, 0.013)
plt.xlabel("Time (seconds)")
plt.ylabel("$V_{0}$(t)")
plt.title('Step response')
plt.grid()
plt.plot(T, yout)
# if using termux
plt.savefig('./figs/ee18btech11028/step_response.pdf')
plt.savefig('./figs/ee18btech11028/step_response.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11028/step_response.pdf"))
# else




# plt.show()
