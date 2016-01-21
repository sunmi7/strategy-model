import math

def compute_score(driving_speed, speed_to_courtyard,
                  speed_to_neutral, shoot_time, shoot_length,
                  point_shot, shot_prob, endtime, end_value):
    outer_length = 4
    oneway_neutral = 12
    points_cross = 5
    outer_to_court = 16 - shoot_length
    shoot_shove = shoot_time
    time_rebound = shoot_shove + 3 + (2*shoot_length)/driving_speed
    offensive_rebound = (1 - shot_prob)*time_rebound
    teleop_time = 135 - endtime
    drive_outer = outer_to_court/driving_speed
    traverse_outer = outer_length/speed_to_neutral
    drive_to_ball = oneway_neutral/driving_speed
    acquire_ball = 3
    drive_to_outerworks = drive_to_ball
    traverse_outerworks = outer_length/speed_to_courtyard
    drive_to_position = drive_outer
    cycle_items = [
        drive_outer,
        traverse_outer,
        drive_to_ball,
        acquire_ball,
        drive_to_outerworks,
        traverse_outerworks,
        drive_to_position,
        shoot_shove,
        time_rebound
    ]
    total_cycle = sum(cycle_items)
    number_cycle = teleop_time / total_cycle
    expect_value = point_shot*shot_prob
    expect_boulder = expect_value*number_cycle
    number_works_court = math.floor(number_cycle)
    points_from_outer = number_works_court*points_cross
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
##driving_speed = float(input("Robot Driving Speed: "))
##speed_to_courtyard = float(input("Speed to Courtyard: "))
##speed_to_neutral = float(input("Speed to the Neutral Zone: "))
##shoot_time = float(input("Time to Shoot or Shove: "))
##shoot_length = float(input("Distance from Tower: "))
##point_shot = float(input("Points per Successful Shot: "))
##shot_prob = float(input("Probability of a Successful Shot: "))
##endtime = float(input("Time Spent on Endgame: "))
##end_value = float(input("Points from Endgame: "))
    
##print("Drive distance to outer works in courtyard:", outer_to_court)
##print("Time for offensive rebound:", offensive_rebound)
##print("Non-end game teleop time:", teleop_time)
##print("Drive to outer works:", drive_outer)
##print("Traverse outer works:", traverse_outer)
##print("Drive to ball:", drive_to_ball)
##print("Drive to outer works 2:", drive_to_outerworks)
##print("Traverse outer works 2:", traverse_outerworks)
##print("Drive to shooting/shoving position:", drive_to_position)
##print("Shoot/shove:", shoot_shove)
##print("Time to rebound:", time_rebound)
##print("Total cycle time:", total_cycle)
##print("Number of cycles:", number_cycle)
##print("Expected value of a shot:", expect_value)
##print("Expected boulder points:", expect_boulder)
##print("Number of times over works to courtyard:", number_works_court)
##print("Teleop points from outer works:", points_from_outer)
##print("Total points scored:", total_points)
