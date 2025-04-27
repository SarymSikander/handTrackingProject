# Hand Gesture Controlled Volume and Brightness System

This project implements a real-time hand gesture control system that adjusts system volume and screen brightness based on the distance between two fingers using OpenCV, MediaPipe, and other supporting Python libraries. By detecting the thumb and index fingertips, calculating their distance, and mapping that value to a control range, users can intuitively manage their PC settings without any physical contact — offering a hands-free, seamless experience. The system is modular, highly efficient, and provides visual feedback through live camera feed annotations and an FPS counter.

# Features
🎯 Real-time Hand Detection using MediaPipe.
🖐️ Precise Landmark Tracking of 21 key hand points.
🎚️ Volume Control based on hand gestures (using pycaw).
🌟 Brightness Control (Windows-only, using WMI API).
📈 Live Performance Metrics (Frames Per Second display).
🔁 Smooth Value Interpolation for natural system responses.
🧩 Modular Code Structure (via handTrackingModule).
👋 Visual Annotations (landmarks, lines, dynamic bars).
💻 Cross-platform potential (volume on all platforms, brightness Windows-only).

#Project Structure:
📂 Hand Gesture Control
 ├── handTrackingModule.py    # Hand detection and landmark extraction module
 ├── handtracking.py          # Basic hand landmark visualization
 ├── brightnessControl.py     # Brightness control via gestures
 ├── volumeControl.py         # Volume control via gestures
 └── landmarks.txt            # Landmark reference guide (21 points)

# Technologies Used
- Python 3
- OpenCV (cv2) — for real-time video processing
- MediaPipe — for hand tracking and landmark detection
- pycaw — for controlling system volume
- wmi — for controlling screen brightness
- NumPy — for efficient mathematical operations
- time — for performance monitoring (FPS)
