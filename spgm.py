import os
import matplotlib
import pylab
import librosa
import librosa.display
import glob
import time
import numpy as np

path = '/home/midhun/Documents/Project/pgms/v2/sample/' #<--where the splitted songs are stored
count = 0
def plot() :
    #moment = time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime())  
    save_path = str(count)+'.png'
    pylab.axis('off')

    pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[])

    S = librosa.feature.melspectrogram(y=sig, sr=fs)
    librosa.display.specshow(librosa.power_to_db(S, ref=np.max))
    pylab.savefig(save_path, bbox_inches=None, pad_inches=0)
    pylab.close()



for song in glob.glob(os.path.join(path,'*.mp3')) :

    #matplotlib.use('Agg') 
    sig, fs = librosa.load(song, mono=True) 
    plot()
    count+=1
    #print (song)
    
