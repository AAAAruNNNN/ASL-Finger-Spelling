 
import cv2 
import os
import image_demo
# function to display the coordinates of 
# of the points clicked on the image  
  
# driver function
if __name__ == "__main__":
    videoname = 'day.mp4'
    cap = cv2.VideoCapture(videoname)  # video_name is the video being called

    totalFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(totalFrames)
    size = totalFrames / 3
    frames = []
    frames.append(int(0.5 * size))
    frames.append(int(1.5 * size))
    frames.append(int(2.5 * size))
  
    for i in frames:
        cap.set(1,i)
        ret, frame = cap.read() # Read the frame
        cv2.imwrite(f"./images/{videoname.split('.')[0]}"+str(i)+'.jpg', frame)
        #cv2.imwrite('img'+str(i)+'.jpg', frame)
    image_demo.word()
        
    
    cv2.waitKey(0) 
  
    # close the window 
    cv2.destroyAllWindows() 
