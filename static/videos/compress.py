import os
import subprocess

def compress_to_h264(input_video):
    """
    Compresses a video using H.264 (libx264) codec and overwrites the original file.
    
    Args:
        input_video (str): Path to the input video file.
    """
    temp_output = f"{input_video}.temp.mp4"  # Temporary file to avoid overwriting during encoding
    try:
        # Build the ffmpeg command
        command = [
            "ffmpeg", "-i", input_video,               # Input file
            "-c:v", "libx264",                        # Use H.264 codec
            "-preset", "slow",                        # Slower preset for better compression
            "-crf", "26",                             # Compression level (lower = better quality, larger size)
            "-c:a", "aac",                            # Use AAC codec for audio
            "-b:a", "128k",                           # Set audio bitrate
            temp_output                               # Temporary output file
        ]
        
        # Run the command
        subprocess.run(command, check=True)
        
        # Overwrite the original file
        os.replace(temp_output, input_video)
        print(f"Compressed and overwritten: {input_video}")
    
    except subprocess.CalledProcessError as e:
        print(f"Error during compression of {input_video}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # Clean up temporary file if it exists
        if os.path.exists(temp_output):
            os.remove(temp_output)

def process_folder(folder_path):
    """
    Compresses all .mp4 videos in a folder and subfolders using H.264.
    
    Args:
        folder_path (str): Path to the folder containing video files.
    """
    for root, _, files in os.walk(folder_path):
        for filename in files:
            if filename.lower().endswith(".mp4"):
                input_video = os.path.join(root, filename)
                compress_to_h264(input_video)

# Specify the folder containing videos
video_folder = "./"  # Replace with your folder path
process_folder(video_folder)
