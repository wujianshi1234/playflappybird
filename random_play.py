import sys
sys.path.append("game/")
import numpy as np
import wrapped_flappy_bird as game

game_state = game.GameState()

while True:
    do = np.random.choice([True, False], p=[0.2, 0.8])
    do = [0,1] if do else [1,0]
    image, reward, terminal = game_state.frame_step(do)
