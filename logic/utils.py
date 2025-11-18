from config import *
from psychopy import core, event

def show_feedback(result, square):
    if result:
        square.fillColor = 'green'
    else:
        square.fillColor = 'red'
        
    square.draw()
    
def get_feedback(win, text_stim, n, reference, keys, square, previous_key=-1):
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

def run_stimulus_trial():
    clock = core.Clock()
    keys = event.waitKeys(keyList=['up', 'down', 'left', 'right'])
    rt = clock.getTime()
    return keys, rt

def reset_window(win, text_stim, right_square, left_square, n):
    right_square.draw()
    left_square.draw()
    text_stim.text = str(n)
    text_stim.draw()
    win.flip()