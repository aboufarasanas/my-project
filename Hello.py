import streamlit as st
import PIL.Image
import pytesseract

def main():
    st.set_page_config(page_title="Image to Text", page_icon=":guardsman:", layout="wide")

    st.title("Extract Text from Image")
    st.subheader("Upload an image and see the magic!")

    # Add a file uploader
    uploaded_file = st.file_uploader("Upload an Image", type=['jpg', 'jpeg', 'png'])

    if uploaded_file is not None:
        image = PIL.Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Perform OCR on the image
        text = pytesseract.image_to_string(image)

        # Display the extracted text
        st.subheader("Extracted Text")
        st.text(text)

if __name__ == "__main__":
    main()
