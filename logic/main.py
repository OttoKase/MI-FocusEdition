from psychopy import visual, core, sound
from config import *
from utils import *
from datetime import datetime
import random, csv

# detect display resolution
import pyglet
display = pyglet.canvas.get_display()
screen = display.get_default_screen()
width = screen.width
height = screen.height
margin = 50

win = visual.Window(size=(width, height - margin), color="black", allowGUI=True, allowStencil=True)
text_stim = visual.TextStim(win, color="white", height=0.2, pos=(0, 0.2))
info_text = visual.TextStim(win, color="white", height=0.15, wrapWidth=1.5)

left_square = visual.Rect(win, width=0.2, height=0.2, pos=(-0.4, -0.3))
right_square = visual.Rect(win, width=0.2, height=0.2, pos=(0.4, -0.3))

lights = []
x_positions = [-0.3, -0.15, 0, 0.15, 0.3]  # five evenly spaced lights

for x in x_positions:
    lights_square = visual.Rect(win, width=0.1, height=0.1, pos=(x, 0.6), fillColor="gray", lineColor="gray")
    lights.append(lights_square)

# Intro for user
info_text.text = f"Tere tulemast eksperimendi algusesse!\n\nSinu ülesanne on vajutada nelja nooleklahvi ja saada võimalikult palju rohelisi kaste. Punased kastid tähendavad vale vastust.\n\nJätkamiseks vajuta suvalist klahvi."
info_text.draw()
win.flip()
event.waitKeys()

# Trial starts
results = []
for trial in range(NUMBER_OF_TRIALS):
    # Play audio in background
    if (SOUND_USED and GROUP_TYPE == "TEST"):
        bg_sound = sound.Sound(SOUND_FILES[trial])
        bg_sound.play()
    
    reference = random.choice(REFERENCE_NUMBER_RANGE)
    text_stim.text = f"Viitenumber: {reference}"
    text_stim.draw()
    win.flip()
    core.wait(REFERENCE_SHOW_TIME)
    
    for trial_loops in range(NUMBER_OF_LOOPS_INSIDE_TRIAL):
        left_square.fillColor = FEEDBACK_BOX_BASE_COLOR
        right_square.fillColor = FEEDBACK_BOX_BASE_COLOR
        win.color = BACKGROUND_COLOR
        
        trial_range = list(TRIALS_NUMBER_RANGE)
        trial_range.remove(reference)
        n = random.choice(trial_range)
        
        reset_window(win, text_stim, right_square, left_square, n)
        
        keys, rt = run_stimulus_trial(win, text_stim, lights, right_square, left_square, n)
        key_1, correct_1 = get_feedback(n, reference, keys, left_square)
        results.append([trial, reference, trial_loops, n, key_1, correct_1, rt])
        reset_window(win, text_stim, right_square, left_square, n)
        
        keys, rt = run_stimulus_trial(win, text_stim, lights, right_square, left_square, n)
        key_2, correct_2 = get_feedback(n, reference, keys, right_square, key_1)
        results.append([trial, reference, trial_loops, n, key_2, correct_2, rt])
        reset_window(win, text_stim, right_square, left_square, n)
        
        core.wait(FEEDBACK_SHOW_TIME)
    
    if (SOUND_USED and GROUP_TYPE == "TEST"):
        bg_sound.stop()
        
    if (GROUP_TYPE == "CONTROL"):
        core.wait(FEEDBACK_SHOW_TIME)
    elif (GROUP_TYPE == "TEST"):
        info_text.text = f"Oled jõudnud {trial+1}. ringi lõpuni.\n\nJärgmisena tuleb vastata paarile küsimusele.\n\nKui küsimustele on vastatud, vajuta jätkamiseks klahvi 'c'."
        info_text.draw()
        win.flip()
        event.waitKeys(keyList=['c'])

# Outro for user
info_text.text = f"Oled jõudnud eksperimendi lõpuni.\n\nJärgmisena tuleb vastata paarile küsimusele."
info_text.draw()
win.flip()
core.wait(INFO_SHOW_TIME)

# Save results
today = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
with open(f"results/{today}.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["trial", "reference", "trial_loop", "number", "key", "correct", "reaction_time"])
    writer.writerows(results)
    
win.close()