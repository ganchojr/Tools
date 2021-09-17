import eyed3
import sys

if len(sys.argv) != 2:
    print("Usage: python MP3_Metadata.py track.mp3")
else:
    audio = eyed3.load(sys.argv[1])
    if eyed3.load(sys.argv[1]) is not None: 
        print("===== MP3 METADATA =====")
        print(f"Title: {audio.tag.title}")
        print(f"Artist: {audio.tag.artist}")
        print(f"Album: {audio.tag.album}")
        print(f"Genre: {audio.tag.genre}")
        print(f"Year: {audio.tag.recording_date}")
        print(f"Track Number: {audio.tag.track_num[0]}")
    else:
        print("Error opening file.")

