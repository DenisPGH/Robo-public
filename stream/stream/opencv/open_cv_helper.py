
import cv2
import threading



#to capture video class
class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        try:
            while True:
                (self.grabbed, self.frame) = self.video.read()
                if not self.grabbed:
                    break
                    #print("not grabbed")
        except:
            #print("break update")
            self.video.release()
            cv2.destroyAllWindows()

    def stop(self):
        return self.video.release()

def gen(camera):
    while True:
        try:
            frame = camera.get_frame()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n'
                   )
        except:
            #print("break in gen cam")
            VideoCamera.stop(camera)
            cv2.destroyAllWindows()
            break



