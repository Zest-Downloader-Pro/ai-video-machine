import os

def check_files():
    print("--- ROBOT SEARCH START ---")
    files = os.listdir('.')
    print(f"I found these files: {files}")
    
    mp3s = [f for f in files if f.lower().endswith('.mp3')]
    imgs = [f for f in files if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    
    print(f"Count of MP3s: {len(mp3s)}")
    print(f"Count of Images: {len(imgs)}")
    
    if len(mp3s) == 0 or len(imgs) == 0:
        print("ERROR: I am blind! I don't see your MP3 or your Images.")
    else:
        print("SUCCESS: I can see everything. We can build now.")
    print("--- ROBOT SEARCH END ---")

if __name__ == "__main__":
    check_files()
