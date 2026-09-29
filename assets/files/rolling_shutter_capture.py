# Burst-capture script for the Raspberry Pi Camera Module 3 (IMX708), which has a rolling shutter.
# Takes a series of JPEG images of a spinning fan using a fixed, very short exposure.
# A rolling shutter reads the sensor one row at a time from top to bottom, so fast-moving
# fan blades can look bent or stretched even when the exposure is very short.

from pathlib import Path          # Path builds file and folder paths that work on any OS
from time import sleep            # sleep() pauses the script for a number of seconds
from picamera2 import Picamera2   # Picamera2 is the Python interface to the Pi camera

NUMBER_OF_IMAGES = 50                                   # How many images to take in the burst
SAVE_FOLDER = Path("rolling_shutter_images") / "fan"    # Images are saved in rolling_shutter_images/fan/
SAVE_FOLDER.mkdir(parents=True, exist_ok=True)          # Create the folder (and its parent); no error if it already exists

camera = Picamera2(0)   # Open camera number 0 (the first camera connected to the Pi)

# Build a video-style configuration. It keeps several frame buffers ready,
# which makes back-to-back captures faster than a still configuration.
# The IMX708 has several sensor modes, so one is chosen explicitly here. Without the
# sensor setting, a 1280x720 request picks the fast 120 fps mode (1536x864), which
# only reads the centre of the sensor and gives a narrower view.
config = camera.create_video_configuration(
    main={"size": (1280, 720)},       # Output image size, scaled down from the sensor mode (same 16:9 shape, so no cropping)
    sensor={                          # Settings for the raw sensor mode
        "output_size": (2304, 1296),  # The mode that covers the full sensor area at a lower resolution
        "bit_depth": 10               # 10 bits per pixel, which is what this mode uses
    }
)

camera.configure(config)   # Apply the configuration to the camera

# Lock the exposure settings so every image is taken the same way
camera.set_controls({
    "AeEnable": False,       # Turn off auto exposure so the camera cannot change the two values below
    "ExposureTime": 750,     # Exposure in microseconds (750 us = 1/1333 s); shorter freezes motion better but is darker
    "AnalogueGain": 6.0,     # Sensor amplification to brighten the short exposure; higher values add noise
})

camera.start(show_preview=True)   # Start streaming frames and open a live preview window
sleep(2)                          # Wait 2 seconds so auto white balance (still automatic) can settle

print("Camera configuration:")            # Label for the next line of output
print(camera.camera_configuration())      # Show the full configuration the camera is actually using

print("Metadata:")                        # Label for the next line of output
print(camera.capture_metadata())          # Show the settings reported with one live frame (exposure, gain, etc.)

input("Start the fan, wait for constant speed, then press Enter...")   # Pause here until you press Enter

for image_number in range(1, NUMBER_OF_IMAGES + 1):               # Loop with image_number = 1, 2, ... 50
    filename = SAVE_FOLDER / f"rolling_{image_number:02d}.jpg"    # Zero-padded name (rolling_01.jpg) so files sort in order
    metadata = camera.capture_file(str(filename))                 # Save the next frame as a JPEG and get that frame's metadata
    print(                                                        # Print the settings that were used for this image
        image_number,                                             # Which image this is
        "Exposure:", metadata.get("ExposureTime"),                # Actual exposure time in microseconds
        "Gain:", metadata.get("AnalogueGain"),                    # Actual analogue gain
        "Frame duration:", metadata.get("FrameDuration"),         # Time between frames in microseconds (about 33333 = 30 fps)
    )

camera.stop()    # Stop the camera streaming frames
camera.close()   # Close the preview window and release the camera for other programs