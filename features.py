import numpy as np
import scipy

def getfeatures(emg_rectified): #returns the feature set of the given signal
    mean=np.mean(emg_rectified) ##mean absolute value
    var=np.var(emg_rectified) #varience
    sd=np.sqrt(var) #standard deviation
    rms = np.sqrt(np.mean(emg_rectified**2)) #root mean square
    fs=9620 #sampling rate
    N=2**14
    xf=scipy.fftpack.fft(emg_rectified,N)
    psd=(abs(xf)**2)/N
    psd=psd/np.sum(psd) 
    ent=scipy.stats.entropy(psd,qk=None,base=None) #power spectral entropy
    
    ld=np.exp(np.sum(np.log(emg_rectified))/len(emg_rectified)) #log detector
    
    n=len(emg_rectified)
    mav=0
    for i in range(n):
        if i>(0.25*n) and i<(0.75*n):
            mav=mav +(emg_rectified[i])
        else:
            w=0.5
            mav=mav+ (w*emg_rectified[i])
        
    mav1=mav/n #modified mean absolute value

    iemg=np.sum(emg_rectified) #integrated EMG

    psd1=(abs(xf)**2)/N
    n=np.arange(0,N/2)
    freq=((n*fs)/N)
    mnf=np.sum(freq*psd1[0:int(N/2)])/np.sum(psd1[0:int(N/2)]) #mean frequency

    ttp= np.sum(psd1[0:N]) #total power
    mnp=ttp/N #mean power
    
    hp=ttp/2
    s=0
    mdf =0
    for idx, val in enumerate(psd1[0:N]):
        if s<hp:
            s=s+val
        else:
            mdf=((idx*fs)/N/2) #median freq
        break
    #feature set
    feat_array=np.array([mean, var, sd, rms, ent, ld, mav1, iemg, mnf, mdf, ttp, mnp]) 
  

    return(feat_array)

    