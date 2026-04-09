import os
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips

def create_video():
    # 1. FIND THE AUDIO FILE AUTOMATICALLY
    # This looks for any file ending in .mp3 so you don't have to type the long name
    audio_files = [f for f in os.listdir('.') if f.lower().endswith('.mp3')]
    
    if not audio_files:
        print("Error: No MP3 file found! Please upload your Adam voiceover.")
        return
    
    AUDIO_FILE = audio_files[0]
    print(f"Using audio file: {AUDIO_FILE}")

    # 2. FIND ALL PICTURES
    # This grabs .jpg, .jpeg, .png, and .webp regardless of capital letters
    valid_extensions = ('.jpg', '.jpeg', '.png', '.webp')
    images = [f for f in os.listdir('.') if f.lower().endswith(valid_extensions)]
    
    # Sort them so they play in order
    images.sort()
    
    if not images:
        print("Error: No pictures found! Please upload your Pexels images.")
        return
    print(f"Found {len(images)} images.")

    # 3. BUILD THE VIDEO
    audio = AudioFileClip(AUDIO_FILE)
    duration_per_image = audio.duration / len(images)
    
    clips = []
    for img_path in images:
        try:
            # Create clip and resize for a phone screen (YouTube Shorts/TikTok)
            clip = ImageClip(img_path).set_duration(duration_per_image)
            # Resize to standard vertical 1080x1920
            clip = clip.resize(height=1920) 
            clips.append(clip)
        except Exception as e:
            print(f"Skipping broken image {img_path}: {e}")

    # Stitch everything together
    video = concatenate_videoclips(clips, method="compose")
    video = video.set_audio(audio)

    # 4. EXPORT
    video.write_videofile("final_video.mp4", fps=24, codec="libx264", audio_codec="aac")
    print("Success! Your video 'final_video.mp4' is ready.")

if __name__ == "__main__":
    create_video()
