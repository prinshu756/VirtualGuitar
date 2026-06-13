# VirtualGuitar

A machine learning-based project that enables users to play guitar chords using hand gestures. It uses MediaPipe and OpenCV for real-time hand tracking and Pygame for chord sound playback.

---

## Demo

<p align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcWYzYzJ4bG56eGgxY2o4cGZ4eXp6eG56eGg4eXp6eGg4eXp6eGg4eQ/giphy.gif" alt="Virtual Guitar Demo" width="600"/>
</p>

---

## Features

| Feature | Description |
|---------|-------------|
| **Hand Detection** | Real-time finger position tracking via webcam |
| **Chord Mapping** | 10 chords mapped to individual finger gestures |
| **Dual Hand Support** | Left and right hand recognition with different chord sets |
| **Visual Feedback** | Live landmark overlay and chord display |
| **Audio Playback** | Instant chord sound triggering |

---

## Chord Mapping

### Left Hand
| Finger | Gesture | Chord |
|--------|---------|-------|
| Thumb | Extended outward | A Minor |
| Index | Extended upward | A Major 7 |
| Middle | Extended upward | B Minor |
| Ring | Extended upward | C Major 7 |
| Pinky | Extended upward | D Minor |

### Right Hand
| Finger | Gesture | Chord |
|--------|---------|-------|
| Thumb | Extended outward | D Major 7 |
| Index | Extended upward | E Minor |
| Middle | Extended upward | E Major 7 |
| Ring | Extended upward | F Major 7 |
| Pinky | Extended upward | G Major |

---

## Tech Stack

<div align="center">

| Technology | Purpose |
|------------|---------|
| **Python** | Core language |
| **OpenCV** | Video capture & image processing |
| **MediaPipe** | Hand landmark detection |
| **Pygame** | Audio playback |

</div>

---

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/VirtualGuitar.git
cd VirtualGuitar

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install opencv-python mediapipe pygame
```

---

## Usage

```bash
python virtualGuitar.py
```

Press `q` to quit the application.

---

## How It Works

<details>
<summary><strong>Click to expand</strong></summary>

1. **Video Capture** — Webcam feed captured at 640x480 resolution
2. **Hand Detection** — MediaPipe processes frames to identify 21 hand landmarks
3. **Gesture Recognition** — Finger extension detected via landmark coordinate comparison
4. **Chord Trigger** — New chord detected plays corresponding audio file
5. **Visual Output** — Landmarks drawn on frame with active chord displayed

</details>

---

## Project Structure

```
VirtualGuitar/
├── virtualGuitar.py       # Main application
├── *.wav                  # Chord audio files
├── GuitarForJupyter.ipynb # Jupyter notebook version
├── Hand gesture.ipynb     # Gesture analysis notebook
└── README.md              # This file
```

---

## Requirements

- Python 3.8+
- Webcam
- Dependencies listed in Installation section

---

## Contributing

Contributions are welcome. Please open an issue or submit a pull request.

---

## License

MIT License