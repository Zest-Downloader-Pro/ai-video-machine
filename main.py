import os
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips

def create_video():
    print("Checking files...")
    # List all files so we can see what the robot sees
    print(f"Files in folder: {os.listdir('.')}")
    
    # 1. Find Audio
    audio_files = [f for f in os.listdir('.') if f.lower().endswith('.mp3')]
    if not audio_files:
        raise Exception("STOP: No MP3 found. Upload your Adam voiceover first!")
    
    # 2. Find Images
    images = [f for f in os.listdir('.') if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    if not images:
        raise Exception("STOP: No images found. Upload your Pexels pictures first!")
    
    images.sort()
    print(f"Found {len(images)} images and {audio_files[0]}")

    # 3. Create Video
    audio = AudioFileClip(audio_files[0])
    img_dur = audio.duration / len(images)
    
    clips = [ImageClip(m).set_duration(img_dur).resize(height=1920) for m in images]
    
    final = concatenate_videoclips(clips, method="compose").set_audio(audio)
    
    # This is the important part - the write command
    final.write_videofile("final_video.mp4", fps=24, codec="libx264", audio_codec="aac")
    print("DONE! final_video.mp4 has been created.")

if __name__ == "__main__":
    try:
        create_video()
    except Exception as e:
        print(f"FAILED: {e}")
        exit(1) # This tells GitHub it actually failed
