 # Details regarding files in the directory:
 ee18btech11028_sim.net is a netlist for simulating the closed loop unit step response of the circuit in the question. 
 
 step.py is a python file to plot the ee18btech11016_sim.dat  
 
 ## Instructions for Simulation and plotting the output.
 
 ### Setup
 --> In the terminal use the 'cd' command to move to the directory where .net files and .py files are present.  
 --> Make Sure that all the .net and .py files are present in your present directory . 'ls' command is used to list out the files in the present directory.
 
 
 ### Simulation : 
 -->Enter the following command . This simulates the 'ee18btech11028_sim.net' file and creates a 'ee18btech11028_sim.dat' file.
 ``` 
ngspice step_response.net
```

--> Exit from ngspice cmd line using the following code . This gets you back to the present working directory.
 ``` 
exit
```

--> Enter the following command . This runs  'step.py'  which plots a plot of 'ee18btech11028_sim.dat' file
and save it as 'spice_step_response.pdf'
``` 
python3 step.py
```
