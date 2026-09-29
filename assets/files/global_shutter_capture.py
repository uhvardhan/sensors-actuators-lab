# Burst-capture script for the Raspberry Pi Global Shutter Camera (IMX296).
# Takes a series of JPEG images of a spinning fan using a fixed, very short exposure.

from time import sleep            # sleep() pauses the script for a number of seconds
from pathlib import Path          # Path builds file and folder paths that work on any OS
from picamera2 import Picamera2   # Picamera2 is the Python interface to the Pi camera

NUMBER_OF_IMAGES = 50                                  # How many images to take in the burst
SAVE_FOLDER = Path("global_shutter_images") / "fan"    # Images are saved in global_shutter_images/fan/
SAVE_FOLDER.mkdir(parents=True, exist_ok=True)         # Create the folder (and its parent); no error if it already exists

camera = Picamera2(0)   # Open camera number 0 (the first camera connected to the Pi)

# Build a video-style configuration. It keeps several frame buffers ready,
# which makes back-to-back captures faster than a still configuration.
# The IMX296 has only one sensor mode (1456x1088, 10-bit), so it is selected automatically.
config = camera.create_video_configuration(
    main={"size": (1456, 1088)}   # Output image size: the full sensor resolution, so nothing is cropped or scaled
)

camera.configure(config)   # Apply the configuration to the camera

# Lock the exposure settings so every image is taken the same way
camera.set_controls({
    "AeEnable": False,       # Turn off auto exposure so the camera cannot change the two values below
    "ExposureTime": 500,     # Exposure in microseconds (500 us = 1/2000 s); shorter freezes motion better but is darker
    "AnalogueGain": 8.0,     # Sensor amplification to brighten the short exposure; higher values add noise
})

camera.start(show_preview=True)   # Start streaming frames and open a live preview window
sleep(2)                          # Wait 2 seconds so auto white balance (still automatic) can settle

print("Camera configuration:")            # Label for the next line of output
print(camera.camera_configuration())      # Show the full configuration the camera is actually using

print("Metadata:")                        # Label for the next line of output
print(camera.capture_metadata())          # Show the settings reported with one live frame (exposure, gain, etc.)

input("Start the fan, wait for constant speed, then press Enter...")   # Pause here until you press Enter

for image_number in range(1, NUMBER_OF_IMAGES + 1):              # Loop with image_number = 1, 2, ... 50
    filename = SAVE_FOLDER / f"global_{image_number:02d}.jpg"    # Zero-padded name (global_01.jpg) so files sort in order
    metadata = camera.capture_file(str(filename))                # Save the next frame as a JPEG and get that frame's metadata
    print(                                                       # Print the settings that were used for this image
        image_number,                                            # Which image this is
        "Exposure:", metadata.get("ExposureTime"),               # Actual exposure time in microseconds
        "Gain:", metadata.get("AnalogueGain"),                   # Actual analogue gain
        "Frame duration:", metadata.get("FrameDuration"),        # Time between frames in microseconds (about 33333 = 30 fps)
    )

camera.stop()    # Stop the camera streaming frames
camera.close()   # Close the preview window and release the camera for other programs