from pydub import AudioSegment, playback

AudioSegment.converter = "ffmpeg\\ffmpeg.exe"

sound1 = AudioSegment.from_mp3("1.mp3")
sound2 = AudioSegment.from_mp3("2.mp3")
output = sound1.overlay(sound2) #Lenh overlay

class MediaPlayer:
    def __init__(self):
        l=["Mua tren pho bay xa - Tran Minh Hoang.mp3","Nhu Chua Bat Dau - Minh Hoang.mp3",'Trai Tim Khong Ngu Yen - Tran Minh Hoang.mp3']
        self.list=[]
        for x in l:
            sound = AudioSegment.from_mp3(x)
            self.list.append(sound)
    def Play(self, index):
        for x in self.list:
            if index == (self.list.index(x)+1):
                playback.play(x)
    def MixAndPlay(self, index1, index2):
        for x in self.list:
            if index1 == (self.list.index(x)+1):
                for y in self.list:
                    if index2 == (self.list.index(y)+1):
                        output = x.overlay(y)
                        playback.play(output)

hoang = MediaPlayer()
# hoang.Play(2)
hoang.MixAndPlay(1,3)
