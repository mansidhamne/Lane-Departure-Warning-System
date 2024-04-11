from lane import *
from driver_drowsiness import *
import os
#os.environ["IMAGEIO_FFMPEG_EXE"] = "/Users/mansi/anaconda3/lib/python3.11/site-packages"
os.environ["IMAGEIO_FFMPEG_EXE"] = "/usr/local/bin/ffmpeg"
from moviepy.editor import VideoFileClip
import cv2
from imutils.video import VideoStream
from imutils import face_utils
import imutils
import av


# start rear camera - usb
# start front camera - phone
# if warning in lane departure - display just that
# if just drowsiness - small alarm


if __name__ == "__main__":

    demo = 2 # 1: image, 2 video

    # if demo == 1:
    #     imagepath = 'examples/test2.jpg'
    #     img = cv2.imread(imagepath)
    #     img_aug = process_frame(img)
    #     img_aug = cv2.cvtColor(img_aug, cv2.COLOR_BGR2RGB)
    #     #cv2.imshow("Augmented", img_aug)
    #     plt.imshow(img_aug)
    #     #plt.axis("off")
    #     plt.show()

    # else:   
    # video_output = 'examples/project_video_solution.mp4'
    # clip1 = VideoFileClip("examples/project_video.mp4")
    # clip = clip1.fl_image(process_frame) #NOTE: it should be in BGR format
    # clip.write_videofile(video_output, audio=False)    

    #video_output = 'output/harder_challenge_augmented.mp4'

        # Initialize VideoCapture object for camera feed (usually 0 for primary camera)
    #droidcam_url = 'http://192.168.1.12:4747'
    cap1 = cv2.VideoCapture(1)
    cap2 = cv2.VideoCapture(0)
    #cap2 = cv2.VideoCapture(droidcam_url)  # Replace with your phone's IP address and port

        # Check if camera was opened successfully
    if not (cap1.isOpened() and cap2.isOpened()):
        print("Error: Could not open camera.")
        exit()

    # # Define a VideoWriter object to write the processed frames to video
    # fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    # #out = cv2.VideoWriter(video_output, fourcc, 30.0, (int(cap.get(3)), int(cap.get(4))))
    
    # Process each frame from the camera feed
    while cap1.isOpened() and cap2.isOpened():
        ret1, frame1 = cap1.read()  # Read a frame from the camera
        ret2, frame2 = cap2.read()

        if not ret1:
            print("Error: Could not read frame1.")
            break

        # if not ret2:
        #     print("Error: Could not read frame2.")
        #     break

        # processed_frame = process_frame(frame1)  # Process the frame
        # face_frame = drowsiness_detection(frame2)

        #cv2.imshow('Processed Frame', frame1)  # Display the processed frame
        cv2.imshow('Driver Drowsiness', frame2)
        #out.write(processed_frame)  # Write the processed frame to video
        
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
            break

    # Release resources
    cap1.release()
    cap2.release()
    cv2.destroyAllWindows()
        
