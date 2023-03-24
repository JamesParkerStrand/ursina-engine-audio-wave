from scipy.io.wavfile import read

class AudioPlay:
    def __init__(self,file):
        #just loads in our data
        self.file = file

        self.sampleRate, self.AmplitudeData = read(self.file)

        # the default framerate is 30 frames per second, but we are doing 1 frame per 1/30th of a second. by the standard of putting equations together.
        self.incrementor = int( self.sampleRate * (1/30) )

        self.currentAudioIndex = 0

    def setIncrementPlayRate(self, framesYouHave):
        self.incrementor = int( self.sampleRate * (1 / framesYouHave) )

    def setPlacementPositionOnAudio(self, indexPosition):
        self.currentAudioIndex = int( indexPosition / self.incrementor )

    def incrementByFrameRateTick(self):
        self.currentAudioIndex += self.incrementor

    def sampleAmplitudeDataAtPosition(self):
        previousDataFrame = self.currentAudioIndex - self.incrementor

        if(previousDataFrame < 0):
            previousDataFrame = 0

        return (self.AmplitudeData[previousDataFrame:self.currentAudioIndex, 0],
                self.AmplitudeData[previousDataFrame:self.currentAudioIndex, 1])

    def sampleAmplitudeAtPosition(self):
        return (self.AmplitudeData[self.currentAudioIndex, 0], self.AmplitudeData[self.currentAudioIndex, 1])


