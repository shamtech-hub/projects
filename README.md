
# Real-Time Green Screen with OpenCV

This project implements a real-time green screen (chroma key) application using Python and OpenCV. It replaces the green areas in one video with content from another, enabling creative video effects and seamless background substitution.

## Features

- Dynamic HSV Range Adjustment: A user-friendly interface with trackbars to fine-tune HSV values for precise green screen masking.
- Real-Time Video Integration: Processes two video streams, combining them based on a green screen mask.
- Efficient Masking and Overlaying: Uses bitwise operations for seamless blending of frames from two videos.

## Technologies Used

- Python: Programming language for implementing the project.
- OpenCV: Library for computer vision tasks, including video processing and masking.
- NumPy: Library for numerical operations and array manipulation.

## How It Works

1. Read Two Video Streams: The program reads frames from two video files simultaneously.
2. Color Space Conversion: Converts frames from BGR to HSV color space for better color masking.
3. Dynamic Masking: Allows users to adjust HSV range dynamically using trackbars.
4. Frame Integration: Replaces the green areas in the first video with content from the second video.
5. Real-Time Display: Displays the original frame, the green screen mask, and the final output in separate windows.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/green-screen-opencv.git
   cd green-screen-opencv
   ```

2. Install the required dependencies:
   ```bash
   pip install opencv-python numpy
   ```

3. Place your video files in the project directory and update their names in the script (e.g., `small.mp4` and `skyvid.mp4`).

## Usage

1. Run the script:
   ```bash
   python green_screen.py
   ```
2. Use the trackbars to adjust HSV values and fine-tune the green screen mask.
3. Press `m` to exit the application.

## Code Overview

The main components of the project:

- HSV Trackbars: For adjusting the HSV range dynamically.
- Mask Creation: Identifies green areas in the video based on HSV values.
- Bitwise Operations: Combines frames from two videos for the green screen effect.
- Video Synchronization: Ensures both videos are processed frame by frame.

## Demo

![Green Screen Demo](demo.gif)

## Project Structure

```
.
├── green_screen.py   # Main script
├── small.mp4         # Example input video
├── skyvid.mp4        # Replacement background video
├── README.md         # Project description
```

## Future Improvements

- Support for live webcam streams.
- Advanced background blending techniques for smoother transitions.
- Add GUI for easier control of HSV values and video selection.

## Acknowledgments

This project was inspired by the capabilities of OpenCV and its robust support for real-time video processing.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
