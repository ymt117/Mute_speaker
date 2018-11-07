import wave
import numpy as np
import matplotlib.pyplot as plt

wf = wave.open('../outputs/out.wav', 'rb')

buf = wf.readframes(wf.getnframes())
# バイナリデータを16bit整数に変換
data = np.frombuffer(buf, dtype='int16')
plt.plot(data)
plt.show()