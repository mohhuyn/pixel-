import cv2
from time import sleep
evt=0
pnt=(0,0)
def Mouse(event,xpos,ypos,flags,params):
    global evt,pnt
    if event==cv2.EVENT_LBUTTONDOWN:
        print('Th event is: ',event)
        print('at pos: ',xpos,ypos)
        evt=event
        pnt=(xpos,ypos)
    if event==cv2.EVENT_LBUTTONUP:
        print('Th event is: ',event)
        print('at pos: ',xpos,ypos)
        evt=event
        pnt=(xpos,ypos)
    if event==cv2.EVENT_RBUTTONDOWN:
        print('Th event is: ',event)
        print('at pos: ',xpos,ypos)
        evt=event
        pnt=(xpos,ypos)
      


width=640
height=460
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow('My webCam')
cv2.setMouseCallback('My webCam',Mouse)
while True:

    ignore, frame=cam.read()
    if evt==1:
        cv2.circle(frame,pnt,30,(0,255,0),2)
    if evt==4:
        cv2.circle(frame,pnt,30,(0,255,0),2)  
    cv2.imshow('My webCam', frame)
    cv2.moveWindow('My webCam',0,0)
    
    if cv2.waitKey(1) == ord('q'):

        break
    
cam.release()
