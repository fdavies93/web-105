from glob import glob
from time import sleep
from os.path import splitext, split
import subprocess

POLL_TIME = 1
FILE_PATH = "files"

def extract_file_name(path):
    out = splitext(path)[0]
    return split(out)[1]

def main():
    while True:
        files = glob(FILE_PATH + "/*")
        mp4 = filter(lambda f : splitext(f)[1] == ".mp4", files)
        mp4 = set(map(extract_file_name, mp4))
        mov = filter(lambda f : splitext(f)[1] == ".mov", files)
        mov = set(map(extract_file_name, mov))
        
        unmatched_mp4 = mp4.difference(mov)
        unmatched_mov = mov.difference(mp4)

        for mp4 in unmatched_mp4:
            file_in = FILE_PATH + "/" + mp4 + ".mp4"
            file_out = FILE_PATH + "/" + mp4 + ".mov"
            subprocess.run(["ffmpeg", "-i", file_in, file_out])

        for mov in unmatched_mov:
            file_in = FILE_PATH + "/" + mov + ".mov"
            file_out = FILE_PATH + "/" + mov + ".mp4"
            subprocess.run(["ffmpeg", "-i", file_in, file_out])

        sleep(POLL_TIME)
 
if __name__ == "__main__":
    main()