import wave
import numpy as np
import struct
import matplotlib.pyplot as plt

wf = wave.open('../input/flute.wav', 'rb')
ch = wf.getnchannels()
width = wf.getsampwidth()
fr = wf.getframerate()
fn = wf.getnframes()

buf = wf.readframes(wf.getnframes())
# バイナリデータを16bit整数に変換
data = np.frombuffer(buf, dtype='int16')
#print(data)

f = np.fft.fft(data)
#print(f)

F = np.fft.ifft(f)
F = F.real
#print(F)

F_out = []
for i in range(len(F)):
    tmp = int(F[i])
    F_out.append(tmp)

#print(F_out) 

outd = struct.pack("h" * len(F_out), *F_out)

outf = '../outputs/out.wav'
ww = wave.open(outf, 'w')
ww.setnchannels(ch)
ww.setsampwidth(width)
ww.setframerate(fr)
ww.writeframes(outd)
ww.close()