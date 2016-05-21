from pydub import AudioSegment, playback
AudioSegment.converter = "ffmpeg\\ffmpeg.exe"

class MediaPlayer:
    def __init__(self, list):
        self.list = ["1.mp3","2.mp3"]
    def play(self,index):
        sound1 = AudioSegment.from_mp3(self.list[index])
        playback.play(sound1)
    def mixAndPlay(self, index1, index2):
        sound1 = AudioSegment.from_mp3(self.list[index1])
        sound2 = AudioSegment.from_mp3(self.list[index2])
        output = sound1.overlay(sound2)
        playback.play(output)
hoa = MediaPlayer(list)
hoa.play(1)
hoa.mixAndPlay(0,1)
