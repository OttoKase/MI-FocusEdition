from config import *
from psychopy import core, event, visual

def show_feedback(result, square):
    if result:
        square.fillColor = 'green'
    else:
        square.fillColor = 'red'
        
    square.draw()
    
def get_feedback(n, reference, keys, square, previous_key=-1):
    key = keys[0]
    correct = (
        (key == 'up' and n > reference) or
        (key == 'down' and n < reference) or
        (key == 'left' and n % 2 == 1) or
        (key == 'right' and n % 2 == 0)
    )
    if previous_key == key:
        correct = False
    show_feedback(correct, square)
    return key, correct

def run_stimulus_trial(win, text_stim, lights, right_square, left_square, n):
    max_time = MAX_TIME                 # seconds total
    light_interval = LIGHT_INTERVAL     # every x seconds one light turns on
    
    event.clearEvents()
    
    clock = core.Clock()
    clock.reset()
    keys = []
    while not keys:
        elapsed = clock.getTime()

        # Update lights
        lights_on = min(int(elapsed // light_interval) + 1, 5)
        for i, light in enumerate(lights):
            if i < lights_on:
                if i < 2:
                    light.fillColor = "yellow"
                elif i < 4:
                    light.fillColor = "orange"
                else:
                    light.fillColor = "red"
            else:
                light.fillColor = "gray"
                light.lineColor = "gray"

        # Draw your main stimuli
        text_stim.draw()
        for light in lights:
            light.draw()
            
        reset_window(win, text_stim, right_square, left_square, n)

        # Check for keypress
        keys = event.getKeys(keyList=['up', 'down', 'left', 'right'])
        
        # Check for timeout
        if elapsed >= max_time:
            keys = ["timeout"]
            break

    rt = clock.getTime()
    return keys, rt

def reset_window(win, text_stim, right_square, left_square, n):
    right_square.draw()
    left_square.draw()
    text_stim.text = str(n)
    text_stim.draw()
    win.flip()