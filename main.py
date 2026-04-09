import os
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips

def create_video():
    print("Starting video machine...")
    
    # 1. Find Audio
    audio_files = [f for f in os.listdir('.') if f.lower().endswith('.mp3')]
    if not audio_files:
        print("ERROR: No MP3 found!")
        return
    
    # 2. Find Images
    valid_ext = ('.jpg', '.jpeg', '.png')
    images = [f for f in os.listdir('.') if f.lower().endswith(valid_ext)]
    if not images:
        print("ERROR: No images found!")
        return
    
    print(f"Processing {len(images)} images with {audio_files[0]}")

    try:
        audio = AudioFileClip(audio_files[0])
        img_duration = audio.duration / len(images)
        
        clips = []
        for img in images:
            # Added 'letterbox' to handle different image sizes safely
            clip = ImageClip(img).set_duration(img_duration).resize(height=1920)
            clips.append(clip)

        video = concatenate_videoclips(clips, method="compose")
        video = video.set_audio(audio)
        
        # Write file
        video.write_videofile("final_video.mp4", fps=24, codec="libx264", audio_codec="aac")
        print("VIDEO CREATED SUCCESSFULLY!")
        
    except Exception as e:
        print(f"CRITICAL ERROR: {e}")

if __name__ == "__main__":
    create_video()
