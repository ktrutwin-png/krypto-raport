import numpy as np,wave,sys,json
dur=float(sys.argv[1]);sr=44100;bpm=78;beat=60/bpm;eighth=beat/2;bar=beat*4
n=int(sr*(dur+1));L=np.zeros(n);R=np.zeros(n)
def add(buf,sig,start,pan=.5):
    i=int(start*sr);j=min(n,i+len(sig))
    if i<n:
        buf[0][i:j]+=sig[:j-i]*(1-pan)*1.4;buf[1][i:j]+=sig[:j-i]*pan*1.4
out=[L,R]
def pad(freqs,d):
    t=np.arange(int(sr*d))/sr;s=np.zeros_like(t)
    for f in freqs:
        for det in (-.003,0,.003):
            s+=np.sin(2*np.pi*f*(1+det)*t)
    s*=0.05;e=np.minimum(1,t/1.2)*np.minimum(1,(d-t)/1.4);return s*e
def pluck(f,d=1.6):
    t=np.arange(int(sr*d))/sr
    s=np.sin(2*np.pi*f*t)+.35*np.sin(2*np.pi*2*f*t)*np.exp(-t*4)+.15*np.sin(2*np.pi*3*f*t)*np.exp(-t*7)
    return s*np.exp(-t*2.6)*np.minimum(1,t/.006)*0.16
chords=[([110,164.8,220,261.6,329.6],[659.3,0,523.3,0,440,523.3,659.3,0]),
        ([87.3,130.8,174.6,220,261.6],[523.3,0,440,0,698.5,659.3,523.3,0]),
        ([130.8,196,261.6,329.6,392],[392,523.3,659.3,0,784,659.3,523.3,0]),
        ([98,146.8,196,246.9,293.7],[587.3,0,493.9,0,392,493.9,587.3,0])]
t=0;k=0
while t<dur+1:
    ch,mel=chords[k%4];add(out,pad(ch,bar+.8),t)
    if t>=bar*1 or True:
        for i,f in enumerate(mel):
            if f:add(out,pluck(f),t+i*eighth,pan=.35+.3*((i%3)/2))
    t+=bar;k+=1
x=np.stack([L,R],1)[:int(sr*(dur+.5))]
# fades
fi=int(sr*2);fo=int(sr*3);x[:fi]*=np.linspace(0,1,fi)[:,None];x[-fo:]*=np.linspace(1,0,fo)[:,None]
x/=abs(x).max();x*=0.9
w=wave.open('melody.wav','wb');w.setnchannels(2);w.setsampwidth(2);w.setframerate(sr);w.writeframes((x*32767).astype(np.int16).tobytes());w.close()
