import streamlit as st
import qrcode
from io import BytesIO

st.set_page_config(
    page_title="QR Code Generator",
    page_icon="📱"
)

st.title("📱 QR Code Generator")
st.write("Enter any text or URL to generate your QR Code.")

text = st.text_input("Enter your Text or URL:")

if "qr_bytes" not in st.session_state:
    st.session_state.qr_bytes = None

if st.button("Generate QR Code"):

    if text.strip():

        qr = qrcode.QRCode(
            version=None,
            box_size=10,
            border=4
        )

        qr.add_data(text.strip())
        qr.make(fit=True)

        img = qr.make_image(
            fill_color="black",
            back_color="white"
        ).convert("RGB")

        buffer = BytesIO()
        img.save(buffer, format="PNG")

        st.session_state.qr_bytes = buffer.getvalue()

    else:
        st.warning("Please enter some text or a URL.")

if st.session_state.qr_bytes:

    st.success("QR Code Generated Successfully!")

    st.image(
        st.session_state.qr_bytes,
        caption="Your QR Code",
        width=250
    )

    st.download_button(
        label="Download QR Code",
        data=st.session_state.qr_bytes,
        file_name="my_qr_code.png",
        mime="image/png"
    )