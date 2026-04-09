import os
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips

def create_video():
    # 1. FIND THE MP3
    audio_files = [f for f in os.listdir('.') if f.lower().endswith('.mp3')]
    if not audio_files:
        print("Error: NO MP3 FOUND. Please upload your audio file directly (not in a zip).")
        return
    
    # 2. FIND THE IMAGES
    images = [f for f in os.listdir('.') if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    images.sort()
    
    if not images:
        print("Error: NO IMAGES FOUND. Please upload your pictures directly.")
        return

    print(f"Combining {len(images)} images with {audio_files[0]}")

    # 3. LOW-MEMORY RENDERING
    audio = AudioFileClip(audio_files[0])
    img_duration = audio.duration / len(images)
    
    clips = []
    for img in images:
        # We resize to a smaller 720p to save memory so it doesn't crash
        clip = ImageClip(img).set_duration(img_duration).resize(height=1280)
        clips.append(clip)

    final_video = concatenate_videoclips(clips, method="compose").set_audio(audio)
    
    # We use 'threads=4' to make it faster and 'logger=None' to save memory
    final_video.write_videofile("final_video.mp4", fps=24, codec="libx264", audio_codec="aac", threads=4, logger=None)
    print("SUCCESS: Video created!")

if __name__ == "__main__":
    create_video()
