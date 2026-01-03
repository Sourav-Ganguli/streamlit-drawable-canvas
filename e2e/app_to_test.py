import pandas as pd
import streamlit as st
import os
from PIL import Image
from streamlit_drawable_canvas import st_canvas

st.header("Test Application for streamlit-drawable-canvas")

# Minimal test app: no zoom or pan controls
img_path = r"C:\Users\GANGULS\Downloads\Test.jpg"
bg_image = None
if os.path.exists(img_path):
    bg_image = Image.open(img_path)
else:
    st.warning(f"Background image not found: {img_path}")


# Sidebar: drawing mode selection
drawing_mode = st.sidebar.selectbox(
    "Drawing mode",
    ("rect", "freedraw", "line", "circle", "polygon", "transform"),
    index=0,
)



canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",
    stroke_width=10,
    stroke_color="green",
    background_color="#eee",
    background_image=bg_image,
    height=800,
    width=800,
    drawing_mode=drawing_mode,
    key="canvas",
)

st.write("Canvas JSON data:")
if canvas_result.json_data is not None:
    st.write(canvas_result)