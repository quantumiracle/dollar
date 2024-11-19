import os
import subprocess

def reencode_to_high_profile(input_video):
    """
    Re-encodes a video to H.264 (High Profile) and overwrites the original file.
    Args:
        input_video (str): Path to the input video file.
    """
    temp_output = f"{input_video}.temp.mp4"  # Temporary file to avoid overwriting during encoding
    try:
        # Check the video codec and profile
        probe_cmd = [
            "ffprobe", "-v", "error", "-select_streams", "v:0",
            "-show_entries", "stream=codec_name,profile", "-of", "default=noprint_wrappers=1",
            input_video
        ]
        result = subprocess.run(probe_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output = result.stdout.strip()

        # Skip if already H.264 (High Profile)
        if "h264" in output and "High" in output and "4:4:4" not in output:
            print(f"Video '{input_video}' is already H.264 (High Profile). Skipping re-encoding.")
            return

        print(f"Re-encoding '{input_video}' to H.264 (High Profile)...")

        # Re-encode using ffmpeg
        reencode_cmd = [
            "ffmpeg", "-i", input_video,
            "-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p",  # Convert to High Profile and 4:2:0
            "-crf", "23",  # Compression quality
            "-preset", "medium",  # Encoding speed
            "-c:a", "aac", "-b:a", "128k",  # Audio settings
            temp_output
        ]
        subprocess.run(reencode_cmd, check=True)

        # Overwrite the original file with the re-encoded version
        os.replace(temp_output, input_video)
        print(f"Re-encoded video saved and overwritten: '{input_video}'.")

    except subprocess.CalledProcessError as e:
        print(f"Error during re-encoding of '{input_video}': {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Clean up temporary file if it exists
        if os.path.exists(temp_output):
            os.remove(temp_output)

def process_folder_recursive(folder_path):
    """
    Recursively processes all video files in a folder and subfolders.
    Args:
        folder_path (str): Path to the root folder.
    """
    for root, _, files in os.walk(folder_path):
        for filename in files:
            if filename.lower().endswith(".mp4"):
                input_video = os.path.join(root, filename)
                reencode_to_high_profile(input_video)


# Specify the folder containing the videos
video_folder = "./"  # Change to your folder path
process_folder_recursive(video_folder)
