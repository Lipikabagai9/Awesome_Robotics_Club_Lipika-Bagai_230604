import numpy as np

# Function to calculate distance between two points
def distance(point1, point2):
    return np.linalg.norm(point2 - point1)

# Function to calculate joint angles from joint positions
def calculate_angles(joint_positions):
    angles = []
    for i in range(len(joint_positions) - 1):
        vec1 = joint_positions[i + 1] - joint_positions[i]
        vec2 = np.array([1, 0, 0])  # Assuming arm is initially along x-axis
        cos_angle = np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
        angle = np.arccos(cos_angle)
        angles.append(angle)
    return angles

# Function to perform FABRIK algorithm
def FABRIK(initial_joint_positions, target_position, link_lengths, tolerance=1e-5, max_iterations=1000):
    # Convert angles to radians
    initial_joint_positions = np.radians(initial_joint_positions)

    # Initialize joint positions
    joint_positions = np.zeros((len(initial_joint_positions), 3))

    # Initialize distance between end effector and target
    error = distance(joint_positions[-1], target_position)

    # Initialize iteration counter
    iteration = 0

    # Iterate until convergence or max iterations reached
    while error > tolerance and iteration < max_iterations:
        # Forward reaching
        joint_positions[-1] = target_position
        for i in range(len(joint_positions) - 2, -1, -1):
            vec = joint_positions[i + 1] - joint_positions[i]
            joint_positions[i] = joint_positions[i + 1] - (link_lengths[i] * (vec / np.linalg.norm(vec)))

        # Backward reaching
        joint_positions[0] = np.array(initial_joint_positions)[:3]  # Ensure only first 3 elements are used
        for i in range(len(joint_positions) - 1):
            vec = joint_positions[i + 1] - joint_positions[i]
            joint_positions[i + 1] = joint_positions[i] + (link_lengths[i] * (vec / np.linalg.norm(vec)))

        # Calculate error
        error = distance(joint_positions[-1], target_position)

        # Output joint angles
        print("Iteration {}: Joint Angles: {}".format(iteration, np.degrees(calculate_angles(joint_positions))))

        # Increment iteration counter
        iteration += 1

    # Output final joint angles
    print("Final Joint Angles: {}".format(np.degrees(calculate_angles(joint_positions))))

    # Output reachability
    if error <= tolerance:
        print("Target position is reachable.")
    else:
        print("Target position is not reachable within specified tolerance.")

# Main code
if __name__ == "__main__":
    # Define link lengths
    link_lengths = [23, 15, 7]

    # Taking input for initial joint position/angles in degrees
    initial_joint_position = []
    print("Enter initial joint positions/angles in degrees:")
    for i in range(3):
        ele = float(input())
        initial_joint_position.append(ele)

    # Taking input for target position coordinate
    target_position = np.zeros(3)
    print("Enter target position coordinates:")
    for i in range(3):
        x = float(input())
        target_position[i] = x

    # Call the FABRIK function with the inputs
    FABRIK(initial_joint_position, target_position, link_lengths)
