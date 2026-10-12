import sys
import time

lirik = [
    ("How can you see into my eyes like open doors?", 0.08),
    ("Leading you down into my core where I've become so numb?", 0.08),
    ("Without a soul, my spirit's sleeping somewhere cold", 0.08),
    ("Until you find it there and lead it back home", 0.08),
    ("(Wake me up)", 0.08),
    ("Wake me up inside", 0.08),
    ("(I can't wake up)", 0.08),
    ("Wake me up inside", 0.08),
    ("(Save me)", 0.08),
    ("Call my name and save me from the dark", 0.07),
    ("(Wake me up)", 0.08),
    ("Bid my blood to run", 0.08),
    ("(I can't wake up)", 0.08),
    ("Before I come undone", 0.08),
    ("(Save me)", 0.08),
    ("Save me from the nothing I've become", 0.07),
    ("Bring me to life...", 0.1),
]

delay = [
    1.2,
    1.0,
    1.2,
    1.5,
    0.5,
    0.8,
    0.5,
    0.8,
    0.6,
    1.2,
    0.5,
    0.8,
    0.5,
    0.8,
    0.6,
    1.5,
    2.0,
]

print("\n== Bring Me To Life - Evanescence ==")
time.sleep(2)

for i, (baris_lagu, delay_karakter) in enumerate(lirik):
    for karakter in baris_lagu:
        print(karakter, end="")
        sys.stdout.flush()
        time.sleep(delay_karakter)
    time.sleep(delay[i])
    print("")

print("// code by qy")