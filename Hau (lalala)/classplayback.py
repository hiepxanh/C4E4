from pydub import AudioSegment,playback
AudioSegment.converter='ffmpeg\\ffmpeg.exe'
songlist=['1.mp3','2.mp3']
class mediaplayer:
    def __init__(self):
        self.songlist = ['1.mp3', '2.mp3']
    def play(self,index):
        sound=AudioSegment.from_mp3(self.songlist[index])
        playback.play(sound)
    def mixandplay(self,index1,index2):
        sound1=AudioSegment.from_mp3(self.songlist[index1])
        sound2=AudioSegment.from_mp3(self.songlist[index2])
        output = sound1.overlay(sound2)
        playback.play(output)
c=mediaplayer()
c.play(1)
c.mixandplay(1,2)