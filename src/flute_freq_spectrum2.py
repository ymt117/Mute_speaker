import wave
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns; sns.set()
import random

wf = wave.open('../input/flute.wav')
ch = wf.getnchannels()

fn = wf.getnframes()
amp = (2**8) ** wf.getsampwidth() / 2
data = wf.readframes(fn)
data = np.frombuffer(data, 'int16')
data = data / amp # 振幅正規化
data = data[::ch]

st = 10000 # サンプリングする開始位置
size = 1024 # FFTのサンプル数
start = 0 # 乱数の開始位置
end = 1000 # 乱数の終点位置

hammingWindow = np.hamming(size)
fs = wf.getframerate()
d = 1.0 / fs
freqList = np.fft.fftfreq(size, d)

n = random.randint(start, end)
windowedData = hammingWindow * data[st:st+size]
data = np.fft.fft(windowedData)
data = data / max(abs(data))
plt.plot(freqList, abs(data))

plt.axis([0, fs/16, 0, 1])
plt.title('flute')
plt.xlabel('Frequency[Hz]')
plt.ylabel('amplitude spectrum')
plt.show()