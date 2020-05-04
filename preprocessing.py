import numpy as np
from filter import butterworth_filter


def preprocessing(signal):
    fs=9620 #sampling frequency
    emg_correctmean=signal-np.mean(signal) # to remove DC value
    #to remove inherent noise
    #bandpass filter with pass band 20-450 Hz, order = 5
    emg_filt = butterworth_filter(emg_correctmean, 20, 450, fs, 5, 'bandpass') 
    #to remove ECG artefacts
    #band stop filter with stop band 49-52 Hz, order = 3
    emg_filtered = butterworth_filter(emg_filt, 49, 52, fs, 3, 'bandstop')
    emg_rectified=abs(emg_filtered) #rectification
    return(emg_rectified) #return rectified signal