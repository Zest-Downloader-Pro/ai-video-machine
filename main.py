import os
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips

def create_video():
    # 1. Find any MP3 in the folder
    audio_files = [f for f in os.listdir('.') if f.lower().endswith('.mp3')]
    if not audio_files:
        print("Error: Still no MP3 found!")
        return
    
    # 2. Find all Images
    images = [f for f in os.listdir('.') if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    images.sort()
    
    print(f"Working with: {audio_files[0]} and {len(images)} images")

    audio = AudioFileClip(audio_files[0])
    img_dur = audio.duration / len(images)
    
    # Resize images to fit vertical phone screens
    clips = [ImageClip(m).set_duration(img_dur).resize(height=1920) for m in images]
    
    final = concatenate_videoclips(clips, method="compose").set_audio(audio)
    final.write_videofile("final_video.mp4", fps=24, codec="libx264", audio_codec="aac")
    print("SUCCESS: final_video.mp4 created!")

if __name__ == "__main__":
    create_video()
