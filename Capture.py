import ArDroneVideo
import sys
class Capture:

    def __init__(self):
        self.vdrone = ArDroneVideo.ArVideo()
        self.vdrone.connect()

    def __del__(self):
        self.vdrone.disconnect()

    def capture(self,size=0):
        self.vdrone.capture(size)

if __name__== '__main__':
    try:
        capture = Capture()
        capture.capture(0)
    except:
        print "Error"
        sys.exit()
