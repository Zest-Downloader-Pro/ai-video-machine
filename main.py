import os
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips

def create_video():
    print("--- STARTING FINAL BUILD ---")
    
    # 1. FIND ANY MP3 (No matter the name)
    audio_files = [f for f in os.listdir('.') if f.lower().endswith('.mp3')]
    if not audio_files:
        print("ERROR: I still don't see an MP3 file in the main folder!")
        return
    
    target_audio = audio_files[0]
    print(f"Using audio file: {target_audio}")
    
    # 2. FIND ALL IMAGES
    images = [f for f in os.listdir('.') if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    images.sort()
    
    if len(images) < 2:
        print(f"ERROR: Only found {len(images)} images. Need more to make a video!")
        return

    # 3. BUILD THE VIDEO
    try:
        audio = AudioFileClip(target_audio)
        img_dur = audio.duration / len(images)
        
        clips = []
        for img in images:
            # Resize and soften the process so GitHub doesn't get overwhelmed
            clip = ImageClip(img).set_duration(img_dur).resize(height=720)
            clips.append(clip)

        final = concatenate_videoclips(clips, method="compose").set_audio(audio)
        
        print("Rendering... this is the part that takes 5-10 minutes...")
        final.write_videofile("final_video.mp4", fps=24, codec="libx264", audio_codec="aac")
        print("SUCCESS: YOUR VIDEO IS READY!")
        
    except Exception as e:
        print(f"CRITICAL ERROR DURING RENDER: {e}")

if __name__ == "__main__":
    create_video()
