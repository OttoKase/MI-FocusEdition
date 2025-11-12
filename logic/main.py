from psychopy import visual, core, sound
from config import *
from utils import *
import random, csv

win = visual.Window(size=(800,600), color="black")
text_stim = visual.TextStim(win, color="white", height=0.2)

# Play audio in background
bg_sound = sound.Sound(SOUND_FILE)
bg_sound.play()

reference = random.choice(REFERENCE_NUMBER_RANGE)
text_stim.text = f"Reference: {reference}"
text_stim.draw()
win.flip()
core.wait(REFERENCE_SHOW_TIME)

results = []
for trial in range(NUMBER_OF_TRIAL_LOOPS):
    trial_range = list(TRIALS_NUMBER_RANGE)
    trial_range.remove(reference)
    n = random.choice(trial_range)
        
    keys, rt = run_stimulus_trial(win, text_stim, n)
    
    key_1, correct_1 = get_feedback(win, text_stim, n, reference, keys)
    results.append([trial, n, key_1, correct_1, rt])
    
    keys, rt = run_stimulus_trial(win, text_stim, n)
    
    key_2, correct_2 = get_feedback(win, text_stim, n, reference, keys, key_1)
    results.append([trial, n, key_2, correct_2, rt])
    
# Save results
with open("results/results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["trial", "number", "key", "correct", "reaction_time"])
    writer.writerows(results)

bg_sound.stop()
win.close()