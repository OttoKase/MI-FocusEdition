from psychopy import visual, core, sound
from config import *
from utils import *
from datetime import datetime
import random, csv

win = visual.Window(size=(800,600), color="black")
text_stim = visual.TextStim(win, color="white", height=0.2, pos=(0, 0.2))
info_text = visual.TextStim(win, color="white", height=0.15, wrapWidth=1.5)

left_square = visual.Rect(win, width=0.2, height=0.2, pos=(-0.4, -0.3))
right_square = visual.Rect(win, width=0.2, height=0.2, pos=(0.4, -0.3))
        
# Play audio in background
if (SOUND_USED):
    bg_sound = sound.Sound(SOUND_FILE)
    bg_sound.play()

# Intro for user
info_text.text = f"Tere tulemast eksperimendi algusesse!\n\nSinu ülesanne on vajutada nelja nooleklahvi ja saada võimalikult palju rohelisi kaste. Punased kastid tähendavad vale vastust.\n\nJätkamiseks vajuta suvalist klahvi."
info_text.draw()
win.flip()
event.waitKeys()

# Trial starts
results = []
for trial in range(NUMBER_OF_TRIALS):
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
        
        keys, rt = run_stimulus_trial()
        key_1, correct_1 = get_feedback(win, text_stim, n, reference, keys, left_square)
        results.append([trial, reference, trial_loops, n, key_1, correct_1, rt])
        reset_window(win, text_stim, right_square, left_square, n)
        
        keys, rt = run_stimulus_trial()
        key_2, correct_2 = get_feedback(win, text_stim, n, reference, keys, right_square, key_1)
        results.append([trial, reference, trial_loops, n, key_2, correct_2, rt])
        reset_window(win, text_stim, right_square, left_square, n)
        
        core.wait(FEEDBACK_SHOW_TIME)

# Outro for user
info_text.text = f"Oled jõudnud eksperimendi lõpuni.\n\n.Järgmisena tuleb vastata paarile küsimusele."
info_text.draw()
win.flip()
core.wait(INFO_SHOW_TIME)

# Save results
today = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
with open(f"results/{today}.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["trial", "reference", "trial_loop", "number", "key", "correct", "reaction_time"])
    writer.writerows(results)

if (SOUND_USED):
    bg_sound.stop()
    
win.close()