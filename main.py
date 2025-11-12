from psychopy import visual, event, core, sound
from config import *
import random, csv

win = visual.Window(size=(800,600), color="black")
text_stim = visual.TextStim(win, color="white", height=0.2)

# Play audio in background
#bg_sound = sound.Sound("audiofile.wav")
#bg_sound.play()

reference = random.choice(REFERENCE_NUMBER_RANGE)
text_stim.text = f"Reference: {reference}"
text_stim.draw()
win.flip()
core.wait(2)

results = []
for trial in range(NUMBER_OF_TRIAL_LOOPS):
    trial_range = list(TRIALS_NUMBER_RANGE)
    trial_range.remove(reference)
    n = random.choice(trial_range)
        
    text_stim.text = str(n)
    text_stim.draw()
    win.flip()
    clock = core.Clock()
    keys = event.waitKeys(keyList=['up', 'down', 'left', 'right'])
    rt = clock.getTime()
    
    key_1 = keys[0]
    correct = (
        (key_1 == 'up' and n > reference) or
        (key_1 == 'down' and n < reference) or
        (key_1 == 'left' and n % 2 == 1) or
        (key_1 == 'right' and n % 2 == 0)
    )
    feedback = "Correct!" if correct else "Wrong!"
    text_stim.text = feedback
    text_stim.draw()
    win.flip()
    core.wait(1)
    results.append([trial, n, key_1, correct, rt])
    
    text_stim.text = str(n)
    text_stim.draw()
    win.flip()
    clock = core.Clock()
    keys = event.waitKeys(keyList=['up', 'down', 'left', 'right'])
    rt = clock.getTime()
    
    key_2 = keys[0]
    correct = (
        (key_2 == 'up' and n > reference) or
        (key_2 == 'down' and n < reference) or
        (key_2 == 'left' and n % 2 == 1) or
        (key_2 == 'right' and n % 2 == 0)
    )
    if key_1 == key_2:
        correct = False
    feedback = "Correct!" if correct else "Wrong!"
    text_stim.text = feedback
    text_stim.draw()
    win.flip()
    core.wait(1)
    results.append([trial, n, key_2, correct, rt])
    

# Save results
with open("results/results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["trial", "number", "key", "correct", "reaction_time"])
    writer.writerows(results)

#bg_sound.stop()
win.close()