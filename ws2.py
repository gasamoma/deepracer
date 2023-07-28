import math

def reward_function(params):

    progress = params['progress']

    # Read input variables

    waypoints = params['waypoints']

    closest_waypoints = params['closest_waypoints']
    heading = params['heading']

    
    reward = 1.0

        
    if progress == 100:
        reward += 100

    
    # Calculate the direction of the center line based on the closest waypoints
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]

    

    # Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0]) 

    # Convert to degree
    track_direction = math.degrees(track_direction)

    

    # Calculate the difference between the track direction and the heading direction of the car
    direction_diff = abs(track_direction - heading)

    

    # Penalize the reward if the difference is too large

    DIRECTION_THRESHOLD = 10.0
    malus=1

    
    if direction_diff > DIRECTION_THRESHOLD:
        malus=1-(direction_diff/50)
        if malus<0 or malus>1:
            malus = 0
        reward *= malus
    return reward
