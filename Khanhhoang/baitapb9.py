from pydub import AudioSegment, playback
AudioSegment.converter = "ffmpeg\\ffmpeg.exe"
class MediaPlayer:
    def __init__(self,list):
        self.list = list
    def play(self,index):
        sound = AudioSegment.from_mp3(self.list[index-1])
        playback.play(sound)
    def mixAndPlay(self,index1,index2):
        sound1 = AudioSegment.from_mp3(self.list[index1-1])
        sound2 = AudioSegment.from_mp3(self.list[index2-1])
        output = sound1.overlay(sound2)
        playback.play(output)
list = ["1.mp3","2.mp3","Anh.mp3","Thoi.mp3","Ve nha.mp3","Ve.mp3"]
hoang = MediaPlayer(list)
hoang.play(1)
# hoang.mixAndPlay(3,4)