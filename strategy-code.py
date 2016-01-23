import math

def compute_score(driving_speed, speed_to_courtyard,
                  speed_to_neutral, shoot_time, shoot_length,
                  point_shot, shot_prob, endtime, end_value):

    outer_length = 4
    # 1 Way Drive Distance in Neutral Zone
    oneway_neutral = 12
    points_cross = 5
    outer_to_court = 16 - shoot_length
    shoot_shove = shoot_time
    time_rebound = shoot_shove + 3 + (2*shoot_length)/driving_speed
    offensive_rebound = (1 - shot_prob)*time_rebound
    teleop_time = 135 - endtime
    # Drive to the scoring position from outer works
    drive_outer_to_court = outer_to_court/driving_speed 
    # Traverse the outer works to the courtyard
    traverse_outer_to_court = outer_length/speed_to_neutral
    drive_to_ball = oneway_neutral/driving_speed
    acquire_ball = 3
    # Drive to outerworks going otherway
    drive_court_to_outer = drive_to_ball
    # Traverse outerworks otherway
    traverse_court_to_outer = outer_length/speed_to_courtyard
    drive_to_position = drive_outer_to_court
    cycle_items = [
        drive_outer_to_court,
        traverse_outer_to_court,
        drive_to_ball,
        acquire_ball,
        drive_court_to_outer,
        traverse_court_to_outer,
        drive_to_position,
        shoot_shove,
        time_rebound
    ]
    total_cycle = sum(cycle_items)
    number_cycle = teleop_time / total_cycle
    expect_value = point_shot*shot_prob
    expect_boulder = expect_value*number_cycle
    number_cycle = math.floor(number_cycle)
    points_from_outer = number_cycle*points_cross
    total_points = expect_boulder + points_from_outer + end_value

    return (expect_boulder, points_from_outer, total_points)

input_items = [
    10, # driving speed
    2, # speed to courtyard
    3, # speed to neutral
    2, # shoot time
    7, # shoot length
    5, # points per shot
    0.8, # probability of successful shot
    0, # time spent on endgame
    0 # points from endgame
    ]
input_items2 = [
    10,
    2,
    3,
    1,
    0,
    2,
    0.95,
    1,
    5
    ]
input_items3 = [
    10,
    2,
    3,
    1,
    0,
    2,
    0.95,
    10,
    15
    ]
items_list = [
    input_items,
    input_items2,
    input_items3
    ]
for item in items_list:
    print(item)
    expect_boulder, points_from_outer, total_points = compute_score(*item)
    print(expect_boulder)
    print(points_from_outer)
    print(total_points)
