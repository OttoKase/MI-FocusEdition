from config import *
from psychopy import core, event

def reset_background(win):
    win.color = 'black'
    win.flip()

def show_feedback(win, text_stim, result):
    if result:
        win.color = 'green'
        text_stim.text = "Correct!"
    else:
        win.color = 'red'
        text_stim.text = "Wrong!"
        
    win.flip()
    text_stim.draw()
    reset_background(win)
    core.wait(FEEDBACK_SHOW_TIME)
    
def get_feedback(win, text_stim, n, reference, keys, previous_key=-1):
    key = keys[0]
    correct = (
        (key == 'up' and n > reference) or
        (key == 'down' and n < reference) or
        (key == 'left' and n % 2 == 1) or
        (key == 'right' and n % 2 == 0)
    )
    if previous_key == key:
        correct = False
    show_feedback(win, text_stim, correct)
    return key, correct

def run_stimulus_trial(win, text_stim, n):
    win.color = 'black'
    text_stim.text = str(n)
    text_stim.draw()
    
    win.flip()
    
    clock = core.Clock()
    keys = event.waitKeys(keyList=['up', 'down', 'left', 'right'])
    rt = clock.getTime()
    return keys, rt