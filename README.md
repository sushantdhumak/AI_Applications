# Gemma-3 OCR

![gemma3](https://github.com/user-attachments/assets/12e79aac-8d9b-49ca-9434-d10cbe209f6e)

## Overview

Gemma-3 OCR is a Streamlit web application that leverages the Gemma-3 Vision model to extract and structure text from images. This tool makes it easy to convert text in images to well-formatted, editable content with a simple and intuitive user interface.

## Features

- **Simple Image Upload**: Easily upload images containing text using the file picker
- **Powerful Text Extraction**: Uses Gemma-3 Vision model to extract text with high accuracy
- **Structured Output**: Returns extracted text in a well-organized Markdown format
- **Clean Interface**: Intuitive design with clear separation of input and results
- **Instant Processing**: Get results within seconds of uploading an image

## Requirements

- Python 3.7+
- Streamlit
- Ollama
- PIL/Pillow
- An Ollama-compatible system with the Gemma-3 model installed

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/gemma3-ocr.git
   cd gemma3-ocr
   ```

2. Install the required dependencies:
   ```
   pip install streamlit ollama pillow
   ```

3. Make sure Ollama is installed and running with the Gemma-3 model:
   ```
   ollama pull gemma3:12b
   ```

## Usage

1. Start the application:
   ```
   streamlit run app.py
   ```

2. Open your browser and navigate to the provided URL (typically http://localhost:8501)

3. Upload an image containing text using the sidebar upload button

4. Click "Extract Text" to process the image

5. View the extracted text in the main panel

6. Use the "Clear" button to reset results when needed

## Example Use Cases

- Digitizing printed documents
- Extracting text from screenshots
- Converting handwritten notes to digital text
- Capturing text from presentation slides
- Extracting content from diagrams and infographics

## Acknowledgments

This project uses the Gemma-3 Vision model, developed by Google DeepMind and made available through Ollama.

---
