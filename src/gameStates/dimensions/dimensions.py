# the dimensions of screen
max_x = 40
max_y = 160

# indicates number of bricks
brick_x = 6
brick_y = 30
brick_width = 4

# for the powerups
# time the power up waits for you to get it before dissapearing
time_power = 30
power_speed = 2
# time you have power up for
powerup_time = 100

# for paddle
paddle_length  = 10
paddle_long_length = 14
paddle_short_length= 5
paddle_speed = 2

# score added perbrick
brick_score_add = 20



# game over stirng

game_over_string = ["\t\t\t _______  _______  __   __  _______    _______  __   __  _______  ______",
              "\t\t\t|       ||   _   ||  |_|  ||       |  |       ||  | |  ||       ||    _ |"  ,
              "\t\t\t|    ___||  |_|  ||       ||    ___|  |   _   ||  |_|  ||    ___||   | ||"  ,
              "\t\t\t|   | __ |       ||       ||   |___   |  | |  ||       ||   |___ |   |_||_" ,
              "\t\t\t|   ||  ||       ||       ||    ___|  |  |_|  ||       ||    ___||    __  |",
              "\t\t\t|   |_| ||   _   || ||_|| ||   |___   |       | |     | |   |___ |   |  | |",
              "\t\t\t|_______||__| |__||_|   |_||_______|  |_______|  |___|  |_______||___|  |_|"]

game_over_newlines = 7


# time for ball
ball_standard_time = 2
# this has to be greater than the maximum distance possible between the ball.y and the paddle center during a collision between them both
top_paddle_hit = 5


# proboability of exploding bricks appearing
prob_explode_brick = 2

# time before bricks start falling
brick_fall_time = 100

# for gravity effect
acceleration_gravity = 1

# bullet speed should be negetive
bullet_speed = -1

# bullet delay between shots
bullet_delay = 5

# shooting time period
shooting_time_period = 20

# fireball time
fireball_powerup_time = 30

# boss length
boss_length = 15
boss_health = 10
boss_drop_bomb_time = 20

bomb_speed = 1

# number of lines used to print
number_print_lines = 8

# time after losing health where boss dofends himself
brick_activate_time = 50