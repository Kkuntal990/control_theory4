

import numpy as np
import matplotlib.pyplot as plt


#if using termux
import subprocess
import shlex
#end if

data=np.loadtxt('./codes/ee18btech11028/spice/ee18btech11028_sim.dat')
plt.plot(data[:,0],data[:,1])
plt.grid()
plt.xlabel("time (secs)")
plt.ylabel("Step response")
plt.title('Spice simulation results')

#if using termux

plt.savefig('./figs/ee18btech11028/ee18btech11028_spice_step_response.pdf')
plt.savefig('./figs/ee18btech11028/ee18btech11028_spice_step_response.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11028/ee18btech11028_spice_step_response.pdf"))

#else
plt.show()
