from pydub import AudioSegment, playback

song1 = AudioSegment.from_mp3("05 Red Sun.mp3")
song2 = AudioSegment.from_mp3("Happy Background Music.mp3")

output = song1.overlay(song2)

playback.play(output)


class MediaPlayer:
    def __init__(self, list):
        self.list = list
    def play (self, index):
        song = AudioSegment.from_mp3(self.list[index])
        playback.play(song)
    def mixAndPlay (self, index1, index2):
        song1 = AudioSegment.from_mp3(self.list[index1])
        song2 = AudioSegment.from_mp3(self.list[index2])
        output = song1.overlay(song2)
        playback.play(output)

list = ["05 Red Sun.mp3","Happy Background Music.mp3"]

ly = MediaPlayer(list)
ly.play(1)
ly.mixAndPlay(0,1)
