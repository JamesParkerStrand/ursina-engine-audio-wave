import numpy as np
from scipy.io.wavfile import read
from ursina import *
import AudioPlayer

app = Ursina()

file = "home - hold"

audioData = AudioPlayer.AudioPlay(file + ".wav")

audio = Audio(file + ".mp3")

pointMeshes = Mesh(vertices = [], mode='point', thickness=2)

pointsToGraph = audioData.incrementor

for i in range(pointsToGraph):
    pointMeshes.vertices.append([0,0,0])

pointGraph = Entity(model=pointMeshes, position=(-pointsToGraph / 2,0,0))

camera.z = -2800

def update():

    audioData.incrementByFrameRateTick()

    leftChannel, rightChannel = audioData.sampleAmplitudeDataAtPosition()

    stereo = np.stack((leftChannel,rightChannel))

    mono = np.mean(stereo, axis=0)

    sampleData = mono[len(leftChannel) - pointsToGraph: len(leftChannel)]

    for x in range(len(sampleData)):
        pointMeshes.vertices[x] = [x,0.01 * sampleData[x],0]

    pointMeshes.generate()

    pointGraph.model = pointMeshes

EditorCamera()

app.run()


