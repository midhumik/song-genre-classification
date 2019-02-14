import os
import matplotlib
import pylab
import librosa
import librosa.display
import glob
import time
import numpy as np

#setting the path of the folder where the songs are stored.
path = '/home/midhun/Documents/Project/pgms/v2'

#function to plot the spectrograms of each mp3 file in the directory.
def plot() :
    #to add different filename to different spectrograms.
    moment=time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime())  
    # make pictures name.
    save_path = moment+'.jpg'

    #to remove axis from the matplotlib output file.
    pylab.axis('off')

    #to remove the white edges from the matplotlib output file.
    pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[])

    #plotting and saving the spectrogam with the predefined name.
    S = librosa.feature.melspectrogram(y=sig, sr=fs)
    librosa.display.specshow(librosa.power_to_db(S, ref=np.max))
    pylab.savefig(save_path, bbox_inches=None, pad_inches=0)
    pylab.close()

for song in glob.glob(os.path.join(path,'*.mp3')) :

    matplotlib.use('Agg') #dont know why it is used.
    sig, fs = librosa.load(song) 
    plot()
    
