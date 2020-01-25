import cv2




class CaptureMe(object):
    def __init__(self):
        self.cam = cv2.VideoCapture(0)

    def capture(self):
        print("Image Capture Started...\n")
        print("="*50)
        print("Press SPACE to take a photo\n")
        print("Press ESC to close")
        cv2.namedWindow("Image Capture")

        img_counter = 0

        while True:
            ret, frame = self.cam.read()
            cv2.imshow("test", frame)
            if not ret:
                break
            k = cv2.waitKey(1)

            if k%256 == 27:
                # ESC pressed to close
                print("Escape hit, closing...")
                break
            elif k%256 == 32:
                # SPACE pressed to save
                img_name = "opencv_frame_{}.png".format(img_counter)
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                img_counter += 1

        self.cam.release()

        cv2.destroyAllWindows()

    def record(self):
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter("output.avi",fourcc, 20.0, (640,480))
        print("Press q to save record and quit")
        while(self.cam.isOpened()):
            ret, frame = self.cam.read()
            if ret==True:
                # frame = cv2.flip(frame,0)

                # write the flipped frame
                out.write(frame)

                cv2.imshow('frame',frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break

        # Release everything if job is finished
        self.cam.release()
        out.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    captureme = CaptureMe()
    print("Enter 0 for Image Capture\n")
    print("Enter 1 for Video Record\n")
    print("Enter >=3 for Exit\n")
    choice = int(input("Your Choice is: "))
    if choice == 0:
        captureme.capture()
    elif choice == 1:
        captureme.record()
    else:
        exit()
    
