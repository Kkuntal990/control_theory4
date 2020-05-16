'''Code by Kuntal Kokate
May 12th,2020
Released under GNU GPL
'''
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import signal

#if using termux
import subprocess
import shlex
#end if



Slopes = np.array([0, 0, -20, -20, -40, -40, -40, -40, -40, -40]);
x = np.array([0 ,1,10,100,1000,10000,1e5,1e6,1e7])
Num = [1e9]
Den =  [1, 1010, 1e4]
s1 = signal.lti(Num ,Den)
w = np.logspace(0, 7, 1000)
w, mag, phase = signal.bode(s1, w)



plt.figure()
plt.xlabel("$\omega$ (rad/s)")
plt.ylabel("Magnitude (dB)")
plt.title("Magnitude Plot")
plt.ylim(-100, 110)
plt.semilogx(w, mag)    # Bode magnitude plot
plt.vlines([10, 1000], -100,100,linestyles = 'dashed', color = 'b')
plt.text(1e5, -45, "-40dB/dec", rotation = -40)
plt.text(1e2*0.5, 70, "-20dB/dec", rotation = -25)
plt.plot(31500, 0, 'o')
plt.vlines([31500], -100, 0, linestyles = 'dashed', color = 'r')
plt.text(32500, 0, '$\omega_{1}$')
y = []
k = 100;
for i in range(len(x)-1):
    y.append(k)
    k+=Slopes[i]
y.append(k)
plt.plot(x,y)
plt.grid()
# if using termux
plt.savefig('./figs/ee18btech11028/ee18btech11028_2_1.pdf')
plt.savefig('./figs/ee18btech11028/ee18btech11028_2_1.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11028/ee18btech11028_2_1.pdf"))
# else



plt.figure()
plt.xlabel("$\omega$ (rad/s)")
plt.ylabel('Phase (deg)')
plt.title('Phase plot')
plt.ylim(phase[-1]-10, 0)
plt.vlines([31500], phase[-1]-10, 0, linestyles = 'dashed', color = 'r')
plt.text(33500, -160, '$\omega_{1}$')
plt.semilogx(w, phase,'g')          # Bode phase plot
plt.grid()
# if using termux
plt.savefig('./figs/ee18btech11028/ee18btech11028_2_2.pdf')
plt.savefig('./figs/ee18btech11028/ee18btech11028_2_2.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11028/ee18btech11028_2_2.pdf"))
# else





Numf = [1e6, 1e9]
Denf = [1, 1010, 1e4+1e9]
s2 = signal.lti(Numf ,Denf)
zeros = zeros = signal.ZerosPolesGain(s2).zeros
poles = signal.ZerosPolesGain(s2).poles
zeros = np.array(zeros)
poles = np.array(poles)




plt.figure()
plt.xlabel("Re{T(j$\omega$)}")
plt.axhline(linewidth=2, color='black')
plt.axvline(linewidth=2, color = 'black')
plt.ylabel('Im{T(j$\omega$)}')
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
plt.savefig('./figs/ee18btech11028/ee18btech11028_2_3.pdf')
plt.savefig('./figs/ee18btech11028/ee18btech11028_2_3.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11028/ee18btech11028_2_3.pdf"))
# else



g = np.linspace(0, 1e5, 10000)
w1, H = signal.freqresp(s2, g)
plt.figure()
plt.plot(w1, abs(H))
plt.ylabel('')
plt.ylim(0,1100)
plt.xlabel("$\omega$ (rad/s)")
plt.ylabel("|T(j$\omega$|")
idx = (np.argmax(abs(H)))
plt.vlines(w1[idx], 0 , 1000, linestyles = 'dashed', color = 'r')
plt.plot(w1[idx], 0,'x', zorder=10, clip_on=False, color='g', label= '$\omega_{0}$ = ' + "{:e}".format(w1[idx]))
plt.legend()
plt.grid()
# if using termux
plt.savefig('./figs/ee18btech11028/ee18btech11028_2_4.pdf')
plt.savefig('./figs/ee18btech11028/ee18btech11028_2_4.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11028/ee18btech11028_2_4.pdf"))
# else


#plt.show()
