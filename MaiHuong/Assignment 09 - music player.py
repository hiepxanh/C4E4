from pydub import AudioSegment, playback

AudioSegment.converter = "ffmpeg\\ffmpeg.exe"
# sound1 = AudioSegment.from_mp3("Lonely.mp3")
# playback.play(sound1)

# sound1 = AudioSegment.from_mp3("Lonely.mp3")
# sound2 = AudioSegment.from_mp3("Loca.mp3")
# output = sound1.overlay(sound2)
# playback.play(output)


class MediaPlayer:
    def __init__(self, list):
        self.list = list
    def play(self, index):
        sound = AudioSegment.from_mp3(self.list[index])
        playback.play(sound)
    def mixAndPlay(self, index1, index2):
        sound1 =  AudioSegment.from_mp3(self.list[index1])
        sound2 =  AudioSegment.from_mp3(self.list[index2])
        output = sound1.overlay(sound2)
        playback.play(output)

list = ['Loca.mp3', 'Lonely.mp3', 'Em dao nay co.mp3']
huong = MediaPlayer(list)
huong.play(2)
huong.mixAndPlay(1,2)