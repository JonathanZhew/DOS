"""PyAudio example: Record a few seconds of audio and save to a WAVE file."""

import pyaudio
import wave
import struct

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
SIZE = 4
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"
ofdm_dat =[ 0.50438429, -0.02383506,  0.58791467,  0.2348634 ,  0.13485915,
       -0.11080575,  0.14255649, -0.17816969,  0.07934755,  0.36257679,
        0.01484431, -0.25610312,  0.06222003,  0.06184105,  0.06806754,
        0.12414788,  0.49612403,  0.23745308, -0.12500415,  0.05437249,
       -0.1667376 , -0.30418769,  0.67402855, -0.23875165,  0.17123811,
       -0.57676341, -0.00702546, -0.42336599, -0.64073441,  0.24434204,
        0.09062861, -0.21336967,  0.48288104,  0.68359124, -0.28106374,
        0.22394743,  0.36567368,  0.39685505, -0.07354058, -0.02984401,
       -0.24900601, -0.01224511, -0.0380252 ,  0.31660546, -0.06931986,
       -0.05525473,  0.01330985, -0.38139859,  0.64287817,  0.35205044,
       -0.17678054,  0.10771653, -0.22297873,  0.22141464, -0.04991556,
       -0.00640337,  0.10272111,  0.0126348 ,  0.21784318, -0.08430732,
        0.30544285,  0.03461279,  0.26233411, -0.0879713 , -0.29783648,
        0.04154521, -0.28042301,  0.05050151,  0.15700041, -0.31364443,
       -0.26617446,  0.19041035,  0.21914105,  0.39092318,  0.03046041,
       -0.17279023,  0.26434422,  0.25970431, -0.53973321,  0.11569725,
        0.12715331,  0.36844235, -0.1567974 , -0.09376671, -0.36435549,
        0.42930377, -0.24807916, -0.5036447 ,  0.03835237, -0.09138526,
       -0.05349345, -0.50167206,  0.03966604, -0.12352192, -0.44959255,
       -0.38403248, -0.50200066,  0.35599741,  0.26445099, -0.16419684,
        0.07820834, -0.50926054, -0.27228183,  0.05997032, -0.25109844,
       -0.15001374, -0.48008597,  0.19983176,  0.29863763, -0.04363729,
        0.01569846,  0.23966606, -0.49605922,  0.4489218 ,  0.18496298,
        0.31201434, -0.45289119,  0.22127547,  0.24891608, -0.00809848,
        0.23583416, -0.31085401,  0.08028209,  0.12650228, -0.08718121,
       -0.51353974, -0.2406631 , -0.29602705, -0.48039771,  0.50438429,
       -0.02383506,  0.58791467,  0.2348634 ,  0.13485915, -0.11080575,
        0.14255649, -0.17816969,  0.07934755,  0.36257679,  0.01484431,
       -0.25610312,  0.06222003,  0.06184105,  0.06806754,  0.12414788]

print(len(ofdm_dat))
frames = []
for i in range(len(ofdm_dat)):
    data = bytearray(struct.pack("f", ofdm_dat[i]))
    frames.append(data)

print(len(frames))        
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(SIZE)
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

wf = wave.open("output.wav", 'rb')

data = wf.readframes(CHUNK)
print(len(data))
read_data=[]
for i in range(int(len(data)/4)):
    value = struct.unpack('f', data[i*4:i*4+4])
    read_data.append(value)
while data != b'':
    #stream.write(data)
    data = wf.readframes(CHUNK)
    print(len(data))
#print(read_data)
    

