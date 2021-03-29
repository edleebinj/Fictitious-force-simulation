from vpython import*
import sys

ballradius=0.05
kspring=20000
kair=0.02
m=0.1
M=3000
g=vector(0,-9.8,0)
ropelength=1

scene=canvas(title="press left or right to move, down to brake",width=1200,height=600,x=0,y=0,center=vector(0,1,0),background=color.black,range=4)
bus=box(pos=vector(0,1,0),width=2,height=2,length=5,opacity=0.3,v=vector(0,0,0),a=vector(0,0,0))
floor=box(width=100,height=0.01,length=100,pos=vector(0,0,0),texture={'file':"https://i.imgur.com/IPcmVFn.jpg",'turn':-1})#texture={'file':"https://i.imgur.com/IPcmVFn.jpg",'turn':4})
scene.camera.follow(bus)

ball=sphere(radius=ballradius,color=color.yellow,make_trail=True,retain=1000,interval=1,trail_radius=0.01,trail_color = color.white,pos=vector(0,1,0),v=vector(0,0,0))
rope=cylinder(radius=ballradius/5,pos=vector(0,2,0),axis=vector(0,-ropelength,0),color=color.green)
def springforce(r,l):
    return -kspring*(mag(r)-l)*r/mag(r)
#r is the current length of the spring l is the original length

def keyinput(evt):
    global pos, axis ,angle_v
    move={'left':vector(-1,0,0),'right':vector(1,0,0),'down':vector(0,0,0)}
    stop={'down':1.1}
    s=evt.key
    if s in move:bus.a=move[s]
    if s in stop:
        if mag(bus.v)<0.5:
            bus.v/=stop[s]*2
        else: bus.v/=stop[s]
        if mag(bus.v)<10**-1:
            bus.v=vector(0,0,0)
    
scene.bind('keydown', keyinput)              

ball.pos=vector(0,-1,0)+rope.pos

t=0
dt=0.01

ropelength=mag(ball.pos-rope.pos)

while True:
    rate(1/dt)

    t+=dt
    
    bus.v+=bus.a*dt
    bus.pos+=bus.v*dt

    ball.a=(m*g+springforce(ball.pos-rope.pos,ropelength))-kair*ball.v/m
    ball.v+=ball.a*dt
    ball.pos+=ball.v*dt

    rope.pos=bus.pos+vector(0,1,0)

    rope.axis=ball.pos-rope.pos
    #print(mag(ball.pos-rope.pos))
    #print(bus.v)
sys.exit()