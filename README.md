# Traitor-Tracer

**Invisible Image Watermarking & Traitor Identification System**

Traitor-Tracer is a web-based security system that embeds invisible watermarks into digital images to enable source tracking and traitor identification. The system also evaluates robustness under various attacks such as cropping, resizing, noise addition, and compression.

## Features

- Invisible watermark embedding using unique user identifiers
- Traitor identification by watermark extraction
- Robustness evaluation under multiple signal-processing and geometric attacks
- Similarity-based detection with interpretable failure analysis
- Modular and extensible architecture
- Web interface built with Flask

## System Modules

### 1. Watermark Embedding

- Accepts an image and a unique user identifier
- Embeds an invisible watermark into the image
- Stores watermark metadata securely in a database

### 2. Traitor Checker

- Extracts watermark from a suspected image
- Matches extracted data with stored records
- Identifies the source (if possible)

### 3. Attack Evaluation Module

- Applies attacks such as:
  - Cropping
  - Resizing
  - Noise addition
  - JPEG compression
- Evaluates watermark robustness
- Displays extracted identifier, similarity score, and detection status

## Supported Attacks

| Attack Type | Description |
|-------------|-------------|
| Crop | Removes a portion of the image |
| Resize | Scales the image resolution |
| Noise | Adds Gaussian noise |
| Compress | Applies JPEG compression |
| All | Runs all attacks sequentially |

## Tech Stack

- **Backend:** Python, Flask
- **Image Processing:** OpenCV, NumPy
- **Signal Processing:** SciPy, PyWavelets
- **Database:** PostgreSQL (Supabase)
- **Security:** Cryptographic hashing
- **Frontend:** HTML, CSS (Jinja2 templates)

## Project Structure
```
traitor-tracer/
├── app.py
├── attacks/
│   ├── dispatcher.py
│   ├── crop.py
│   ├── resize.py
│   ├── noise.py
│   └── compress.py
├── core/
│   ├── embed.py
│   ├── extract.py
│   ├── frequency.py
│   ├── redundancy.py
│   └── error_correction.py
├── templates/
│   ├── index.html
│   └── attack.html
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/forex-911/Traitor-Tracker.git
cd traitor-tracer
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file for database credentials:
```
DB_HOST=your_db_host
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_NAME=your_db_name
DB_PORT=5432
```

### 5. Run the application
```bash
python app.py
```

Access the application at: **http://127.0.0.1:5000**

## Evaluation & Results

- High similarity is achieved for non-attacked images
- Robust detection under noise attacks
- Significant degradation under geometric attacks (crop/resize)

These results demonstrate the trade-off between invisibility and robustness, which is a known limitation of spatial-domain watermarking.

## Limitations

- Reduced robustness against geometric attacks
- Spatial-domain embedding is sensitive to synchronization loss

## Future Work

- Frequency-domain watermarking (DCT / DWT)
- Error-correction coding for improved robustness
- Adaptive thresholding per attack type
- Batch evaluation and CSV export of results

## Academic Note

This project is designed as an educational and research-oriented system. Observed failures under certain attacks are expected behavior and are clearly reported and analyzed.

## License

This project is available under the MIT License.

## Contributing

Contributions are welcome. Please submit pull requests or open issues for bug reports and feature requests.

## Contact

For questions or collaboration opportunities, please contact the project maintainer through GitHub.

---

**Copyright © forex-911** · Invisible Watermarking System
