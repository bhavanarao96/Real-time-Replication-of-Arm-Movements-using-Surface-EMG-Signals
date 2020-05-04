from scipy.signal import butter, lfilter

#to fiter the given signal using bandpass or bandstop butterworth filter
def butterworth_filter(data, lowcut, highcut, fs, order, type):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype=type)
    y = lfilter(b, a, data)
    return y