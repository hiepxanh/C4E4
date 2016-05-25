from pydub import AudioSegment
from pydub.playback import play

# l = ["For A Few Dollars More.mp3","Freedom.mp3"]
#
# song1 = AudioSegment.from_mp3(l[0])
# song2 = AudioSegment.from_mp3(l[1])
#
# output = song1.overlay(song2)
#
# play(output)


class MediaPlayer():
    def __init__(self):
        self.song_list = ["For A Few Dollars More.mp3","Freedom.mp3"]
    def play(self,index):
        play(AudioSegment.from_mp3(self.song_list[index]))
    def MixandPlay(self,index1,index2):
        song1 = AudioSegment.from_mp3(self.song_list[index1])
        song2 = AudioSegment.from_mp3(self.song_list[index2])
        output = song1.overlay(song2)
        play(output)

hoanh = MediaPlayer()
hoanh.MixandPlay(0,1)