'''
from pathlib import Path
from glob import glob
s = 'C:\\Users\\Matthew\\AppData\\Local\\osu!\\Skins\\- elohere\\ranking-[A-DSX].png'
x = 'C:\\Users\\Matthew\\AppData\\Local\\osu!\\Skins\\- elohere\\ranking-[A-DSX]H.png'
f = Path('C:\\Users\\Matthew\\AppData\\Local\\osu!\\Skins\\- elohere\\approachcircle - Copy.png')
#fl = [x for x in f.iterdir() if f.is_dir()]
#print(fl)
t = [x[52:] for x in glob(s)]
for i in glob(x):
    t.append(i[52:])
print(t)
#f.unlink()
'''

hit_indicators             = ['hit0*.png', 'hit50*.png', 'hit100*.png', 'hit300*.png', 'particle*.png', 'lighting*.png', 'sliderpoint*.png']
hitcircles                 = ['hitcircle*.png']

s = hit_indicators + hitcircles
print([x for x in {x for x in s}])

