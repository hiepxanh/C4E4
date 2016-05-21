from pydub import AudioSegment, playback
AudioSegment.converter = "ffmpeg\\ffmpeg.exe"

class MediaPlayer:
    def __init__(self, list):
        self.list = ["SauTatCa.mp3","ChuaBaoGio.mp3"]
    def play(self,index):
        sound1 = AudioSegment.from_mp3(self.list[index])
        playback.play(sound1)
    def mixAndPlay(self, index1, index2):
        sound1 = AudioSegment.from_mp3(self.list[index1])
        sound2 = AudioSegment.from_mp3(self.list[index2])
        output = sound1.overlay(sound2)
        playback.play(output)
tu = MediaPlayer(list)
tu.play(1)
tu.mixAndPlay(0,1)