# Mass-spring problem
This code numerically solves the spring-mass system problem and determines the mass displacement, velocity, and acceleration for n time steps using the central difference method.


![image](https://user-images.githubusercontent.com/89813720/141689087-b5ed5b39-68d5-470e-9aac-44ac7f4be26b.png)

The central difference method is an explicit numerical method.
This method  is based on finite difference expressions in time for velocity and acceleration at a time ***t*** given by:

![ken1](https://user-images.githubusercontent.com/89813720/141689208-b2962fa8-2550-4e33-b4db-e45be65b0fc4.png)

Numerical integration:

![ken9](https://user-images.githubusercontent.com/89813720/141689648-9d32c1a4-dcb4-4485-ad64-d99a5282df41.png)

The procedure for a solution is then as follows:

***Step1: determine displacement, velocity, and force at t=0***

***Step2: determine acceleration at t=0***


![ken3](https://user-images.githubusercontent.com/89813720/141689380-848de26c-7ef7-4753-a82e-ea352bdcd573.png)

***Step3: determine displacement (i=-1)***

![ken4](https://user-images.githubusercontent.com/89813720/141689436-5cee9fb4-5a52-4971-8896-2e47b1738fb1.png)

***Step4: determine displacement (i=1)***

![ken5](https://user-images.githubusercontent.com/89813720/141689480-eb2ac7e9-5942-4244-9e22-0010a6477cd1.png)

***Step5: determine displacement (i=2)***

![ken6](https://user-images.githubusercontent.com/89813720/141689504-30905b5f-f97d-44ca-b266-29e4a3a7d140.png)

***Step6: determine acceleration (i=1)***

![ken7](https://user-images.githubusercontent.com/89813720/141689556-62f8a0c8-2a40-4791-b721-3277bfefbacd.png)

***Step7: determine velocity (i=1)***

![ken8](https://user-images.githubusercontent.com/89813720/141689590-072b7144-f819-43eb-a801-34b19ac02ae6.png)

Use steps 5 through 7 repeatedly to obtain the displacement, acceleration, and velocity for all other time steps.


 
