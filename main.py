import os
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips, TextClip, CompositeVideoClip

# 1. SETUP - Change these names to match your files
AUDIO_FILE = "adam_voiceover.mp3"  # Put your ElevenLabs file here
IMAGE_FOLDER = "images"            # Put your Pexels pictures in a folder named 'images'
OUTPUT_NAME = "final_video.mp4"

def create_video():
    # Load the audio to know how long the video should be
    audio = AudioFileClip(AUDIO_FILE)
    audio_duration = audio.duration
    
    # Get all pictures from the folder
    images = [os.path.join(IMAGE_FOLDER, img) for img in os.listdir(IMAGE_FOLDER) if img.endswith(('.jpg', '.png'))]
    
    if not images:
        print("No images found! Add some pictures to the 'images' folder.")
        return

    # Calculate how long each picture should stay on screen
    duration_per_image = audio_duration / len(images)
    
    clips = []
    for img_path in images:
        # Create a 9:16 (Shorts) sized clip for each image
        clip = ImageClip(img_path).set_duration(duration_per_image)
        clip = clip.resize(height=1920) # Standard Vertical Height
        clips.append(clip)

    # Stitch the pictures together
    video = concatenate_videoclips(clips, method="compose")
    video = video.set_audio(audio)

    # Save the final result
    video.write_videofile(OUTPUT_NAME, fps=24, codec="libx264")
    print(f"Success! Your video is ready: {OUTPUT_NAME}")

if __name__ == "__main__":
    create_video()
