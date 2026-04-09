import os
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips

def create_video():
    print("Files confirmed. Starting the render...")
    
    # 1. Grab the files the robot found
    audio_file = 'audio.mp3'
    images = [f for f in os.listdir('.') if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    images.sort()
    
    # 2. Setup timing
    audio = AudioFileClip(audio_file)
    img_dur = audio.duration / len(images)
    print(f"Total audio length: {audio.duration}s. Each image will show for {img_dur:.2f}s")

    # 3. Build the clips
    clips = []
    for img in images:
        # Resize to fit phone screen (720p height for faster processing)
        clip = ImageClip(img).set_duration(img_dur).resize(height=1280)
        clips.append(clip)

    # 4. Join and Export
    final = concatenate_videoclips(clips, method="compose").set_audio(audio)
    
    print("Writing video file... this will take a few minutes...")
    final.write_videofile("final_video.mp4", fps=24, codec="libx264", audio_codec="aac", threads=4)
    print("SUCCESS: final_video.mp4 is ready!")

if __name__ == "__main__":
    create_video()
