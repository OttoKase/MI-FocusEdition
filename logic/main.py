from psychopy import visual, core, sound
from config import *
from utils import *
import random, csv

win = visual.Window(size=(800,600), color="black")
text_stim = visual.TextStim(win, color="white", height=0.2)

left_square = visual.Rect(win, width=0.2, height=0.2, pos=(-0.4, -0.4))
right_square = visual.Rect(win, width=0.2, height=0.2, pos=(0.4, -0.4))
        
# Play audio in background
# bg_sound = sound.Sound(SOUND_FILE)
# bg_sound.play()

results = []
for trial in range(NUMBER_OF_TRIALS):
    reference = random.choice(REFERENCE_NUMBER_RANGE)
    text_stim.text = f"Reference: {reference}"
    text_stim.draw()
    win.flip()
    core.wait(REFERENCE_SHOW_TIME)
    
    for trial_loops in range(NUMBER_OF_TRIAL_LOOPS):
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
    
# Save results
with open("results/results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["trial", "reference", "trial_loop", "number", "key", "correct", "reaction_time"])
    writer.writerows(results)

# bg_sound.stop()
win.close()