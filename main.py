import os
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips

def create_video():
    print("Files confirmed. Starting the render...")
    
    # 1. Grab the confirmed files
    audio_file = 'audio.mp3'
    # This finds all your pexels and IMG files
    images = [f for f in os.listdir('.') if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    images.sort()
    
    # 2. Setup timing
    audio = AudioFileClip(audio_file)
    img_dur = audio.duration / len(images)
    print(f"Building a {audio.duration}s video with {len(images)} images.")

    # 3. Build the clips
    clips = []
    for img in images:
        # Resize to 720p height for faster processing on GitHub
        clip = ImageClip(img).set_duration(img_dur).resize(height=1280)
        clips.append(clip)

    # 4. Join and Export
    final = concatenate_videoclips(clips, method="compose").set_audio(audio)
    
    print("Writing video file... please wait...")
    final.write_videofile("final_video.mp4", fps=24, codec="libx264", audio_codec="aac", threads=4)
    print("SUCCESS: final_video.mp4 is ready!")

if __name__ == "__main__":
    create_video()
