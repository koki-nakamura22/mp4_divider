# Install packages
# pip install wheel
# pip install ffmpeg-python

import sys
import ffmpeg


def example():
    input_file = "./source/source.mp4"
    output_file = "./result/result1min.mp4"
    divide_sec = 60
    stream = ffmpeg.input(input_file, ss=0, t=divide_sec)
    audio_stream = stream.audio
    stream = ffmpeg.output(stream, audio_stream, output_file)
    ffmpeg.run(stream)


def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    start_pos_sec = int(sys.argv[3])
    divide_sec = int(sys.argv[4])

    stream = ffmpeg.input(input_file, ss=start_pos_sec, t=divide_sec)
    audio_stream = stream.audio
    stream = ffmpeg.output(stream, audio_stream, output_file)
    ffmpeg.run(stream)


# e.g.
#  python mp4_divider.py "./source/source.mp4" "./result/result_1min.mp4" 0 60
if __name__ == '__main__':
    main()
