from pydub import AudioSegment, playback
AudioSegment.converter = "ffmpeg\\ffmpeg.exe"
# song1 = AudioSegment.from_mp3("stand by me.mp3")
# song2 = AudioSegment.from_mp3("stand by you.mp3")
# playback.play(song1)


class MediaPlayer():
    song_list = ["stand by you.mp3", "stand by me.mp3"]
    def _init_(self):
        self.song_list = ["stand by you.mp3", "stand by me.mp3"]
    def play(self, index):
        playback.play(AudioSegment.from_mp3(self.song_list[index]))
    def MixandPlay(self, index1, index2):
        song1 = AudioSegment.from_mp3(self.song_list[index1])
        song2 = AudioSegment.from_mp3(self.song_list[index2])
        output = song1.overlay(song2)
        playback.play(output)
linh = MediaPlayer()
linh.MixandPlay(0, 1)
