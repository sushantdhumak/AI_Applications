# ===============================================
# OCR with Gemma-3
# ===============================================

import streamlit as st  # to create web applications with Python
import ollama           # to interact with Ollama models (in this case, Gemma-3)
from PIL import Image   # for image processing
import base64           # for encoding and decoding binary data


# -----------------------------------------------
# Page configuration
# Configures the Streamlit page with a title, icon, layout, and sidebar state.
# -----------------------------------------------

st.set_page_config(
    page_title="OCR with Gemma-3",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="expanded"
)


# -----------------------------------------------
# Title and description in main area
# Creates a title with an embedded image. It reads the Gemma-3 logo from a file, 
# converts it to base64, and embeds it directly in the HTML using a data URL.
# -----------------------------------------------

st.markdown("""
    # <img src="data:image/png;base64,{}" width="50" style="vertical-align: -12px;"> Gemma-3 OCR
""".format(base64.b64encode(open("./gemma3.jpg", "rb").read()).decode()), unsafe_allow_html=True)


# -----------------------------------------------
# Add clear button to top right

col1, col2 = st.columns([6,1])


# -----------------------------------------------
# Places a "Clear" button in the second column. When clicked, 
# it removes any previous OCR results from the session state 
# and reruns the app
# -----------------------------------------------

with col2:
    if st.button("Clear 🗑️"):
        if 'ocr_result' in st.session_state:
            del st.session_state['ocr_result']
        st.rerun()


# -----------------------------------------------
# Adds a description with custom styling below the title

st.markdown('<p style="margin-top: -20px;">Extract structured text from images using Gemma-3 Vision!</p>', unsafe_allow_html=True)

st.markdown("---") # Adds a horizontal divider line


# -----------------------------------------------
# Begins a section where UI elements will be placed in the sidebar.
# -----------------------------------------------

# Move upload controls to sidebar

with st.sidebar:
    st.header("Upload Image") # Adds a header to the sidebar
    uploaded_file = st.file_uploader("Choose an image...", type=['png', 'jpg', 'jpeg']) # Adds a file uploader to the sidebar

    if uploaded_file is not None: # Checks if a file has been uploaded
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image")

        if st.button("Extract Text 🔍", type="primary"): # Creates a primary button labeled "Extract Text"
            with st.spinner("Processing image..."): # Shows a spinner animation while processing the image
                # Calls the Ollama API to process the image with Gemma-3 12B model. 
                # It sends a prompt asking to extract text from the image and 
                # format it as Markdown, along with the image data.
                try:
                    response = ollama.chat(
                        model='gemma3:12b',
                        messages=[{
                            'role': 'user',
                            'content': """Analyze the text in the provided image. Extract all readable content
                                        and present it in a structured Markdown format that is clear, concise, 
                                        and well-organized. Ensure proper formatting (e.g., headings, lists, or
                                        code blocks) as necessary to represent the content effectively.""",
                            'images': [uploaded_file.getvalue()]
                        }],
                        options={"timeout": 120}
                    )

                    # Stores the extracted text result in the session state.
                    st.session_state['ocr_result'] = response.message.content 

                except Exception as e:
                    st.error(f"Error processing image: {str(e)}")


# -----------------------------------------------
# Main content area for results
# -----------------------------------------------

# If OCR results exist in the session state, displays them formatted as Markdown.
if 'ocr_result' in st.session_state:
    st.markdown(st.session_state['ocr_result'])
else:
    # If no results exist yet, displays an informational message.
    st.info("Upload an image and click 'Extract Text' to see the results here.")


# Footer
st.markdown("---")


# -----------------------------------------------