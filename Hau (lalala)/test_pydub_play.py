from pydub import AudioSegment, playback

AudioSegment.converter = "ffmpeg\\ffmpeg.exe"
sound1 = AudioSegment.from_mp3("1.mp3")
playback.play(sound1)
