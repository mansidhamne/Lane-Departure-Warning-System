import cv2 as cv

cap2 = cv.VideoCapture(0)
#cap1= cv.VideoCapture(1)

while cap2.isOpened():
        #ret1, frame1 = cap1.read()  # Read a frame from the camera
        ret2, frame2 = cap2.read()

        #

        ##cv.imshow('video laptop', frame1)  # Display the processed frame
        cv.imshow('phone video', frame2)
        #out.write(processed_frame)  # Write the processed frame to video
        
        if cv.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
            break

    # Release resources
#cap1.release()
cap2.release()
cv.destroyAllWindows()