import matplotlib.pyplot as plt
import numpy as np

npi = np.pi
f0 = 5
a0 = 100
tdecay = 2
timestep = 0.01
timemax = 100
time = np.arange(0,timemax,timestep)
amplitude = np.sin(0.002*npi*f0*time) * np.cos(5*npi*f0*time)
spectrum = np.fft.fft(amplitude)
frequency = np.fft.fftfreq( spectrum.size, d = timestep )
index = np.where(frequency >= 0.)

clipped_spectrum = timestep*spectrum[index].real
clipped_frequency = frequency[index]

fig = plt.figure()
fig.subplots_adjust(hspace=0.5)
data1 = fig.add_subplot(2,1,1)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Damping')
data1.plot(time,amplitude, color='red', label='Amplitude')
plt.legend()
plt.minorticks_on()
plt.xlim(0., 10.)
data2 = fig.add_subplot(2,1,2)
plt.xlabel('Frequency')
plt.ylabel('Signal')
plt.title('Spectrum of a Damped Oscillator')
data2.plot(clipped_frequency,clipped_spectrum, color='blue', linestyle='solid',
 marker='None', label='FFT', linewidth=1.5)
plt.legend()
plt.minorticks_on()
plt.xlim(0., 50.)
# Show the data
plt.show()
