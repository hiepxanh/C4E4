from pydub import AudioSegment, playback

AudioSegment.converter = "ffmpeg\\ffmpeg.exe"
sound1 = AudioSegment.from_mp3("1.mp3")
sound2 = AudioSegment.from_mp3("2.mp3")
output = sound1.overlay(sound2)
playback.play(output)
