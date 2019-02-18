#This program is for,
#--> removing the edges( 10 seconds from the beginning and the end ) from the directory.
#--> split the croped songs to 100ms parts and store it in another directory.
#--> generating mel spectrograms of the 100ms splitted songs.

import os
import matplotlib
import pylab
import librosa
import librosa.display
import glob
import time
import numpy as np

path1 = '/home/midhun/Documents/Project/pgms' #<--Where the original songs are stored
path2 = '/home/midhun/Documents/Project/pgms/v2/sample/' #<--where the splitted songs are stored

#function to plot the spectrograms of each mp3 file in the directory.
def plot() :
    #to add different filename to different spectrograms.
    moment = time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime())  
    # make pictures name.
    save_path = moment+'.png'

    #to remove axis from the matplotlib output file.
    pylab.axis('off')

    #to remove the white edges from the matplotlib output file.
    pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[])

    #plotting and saving the spectrogam with the predefined name.
    S = librosa.feature.melspectrogram(y=sig, sr=fs)
    librosa.display.specshow(librosa.power_to_db(S, ref=np.max))
    pylab.savefig(save_path, bbox_inches=None, pad_inches=0)
    pylab.close()

def split() :
    #"""ffmpeg -i Immortals.mp3 -f segment -segment_time 0.1 -c copy out%06d.mp3"""
    for filename in glob.glob(os.path.join(path1,'*.mp3')): 

        os.system("ffmpeg -i {} -c copy path2+'output%06d.png'".format(filename))
    

for song in glob.glob(os.path.join(path2,'*.mp3')) :

    matplotlib.use('Agg') 
    sig, fs = librosa.load(song) 
    split()
    #plot()
    
    
