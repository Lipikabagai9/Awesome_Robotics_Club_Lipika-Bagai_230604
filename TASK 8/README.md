EXPLANATION OF CODE FOR ROBOTIC ARM
Used FABRIK (Forward and Backward Reaching Inverse Kinematics) ALGORITHM to optimize the movement of a robotic arm .

1. Importing Numpy library : imported Numpy as np . It is used for numerical computations.

2. Function to calculate distance between two points: calculate the norm of two vectors using np.linalg.norm function . The "distance" function is used for the calculation of distance between joint positions and target position. 

3. Function to Calculate Joint Angles: The "calculate_angles" function calculates the angles between the joints of a robotic arm based on the positions of the joints. It assumes that the arm is initially aligned along the x-axis and calculates the angles using the dot product and arccosine function.

4. FABRIK Algorithm Implementation:
Basically, the FABRIK function adjusts the position of the joints in a robotic arm iteratively . First, it tries reaching the arm from the end effector ( the end of the arm) and adjust the positions of joints from the base (first joint) and aligns the arm correctly.
•Initialization: Convert the initial joint positions from degrees to radians.
Create an array to store the positions of all the joints.
•Loop Until Convergence or Maximum Iterations: Repeat the following steps until the distance between the end effector (the last joint) and the target position is small enough, or until a maximum number of iterations is reached.
•Forward Reaching: Start from the end effector and adjust each joint position towards the target position. This is like trying to reach for the target by bending each joint starting from the end.
•Backward Reaching: Start from the base (first joint) and adjust each joint position towards the end effector. This is like adjusting the position of each joint from the base to the end to ensure the entire arm is correctly aligned.
•Calculate Error: Measure the distance between the current end effector position and the target position.
•Print Information: Print the joint angles at each iteration to see how they change.
Print the final joint angles after convergence.
Print whether the target position is reachable or not.
•Return: The function finishes after convergence or reaching the maximum number of iterations.

5. Main Code:
• It defines the link length of the robotics arm .
• Takes input for initial joint positions/angles in degrees and target position coordinates .
• Calls the FABRIK function with the inputs.