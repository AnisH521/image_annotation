import streamlit as st
from streamlit_image_coordinates import streamlit_image_coordinates

from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import os

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from image_db import img_db, Base

engine = create_engine(os.environ.get("DATABASE_URL"))
Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
sess = Session()

with st.container():
    st.title("An Application for taking Annotated Pictorial data from Users")
    st.header("How to :green[USE] :star:")
    st.write(
        """
        upload an image of any object then annotate it in suitable position
        - First upload an image
        - Then click on any position of image to know its coordinate
        - After knowing the coordinate Enter the appropriate text for the uploaded image
        - Then Enter the known coordinates in appropriate box to annotate the image
        - Also don't forget to enter appropriate font colour and size of text :cat: 
        - Finally submit the image for the betterment of human civilization :frog: 
        """
    )
    name_input = st.text_input(
            "So what is your name ? :clown_face:",
            value = ""
        )

with st.container():
    st.write("---")
    uploaded_image = st.file_uploader('upload the image file here', type = ['png', 'jpg', 'jpeg'])
    if uploaded_image:      
        image = Image.open(uploaded_image)
        rgb_image = image.convert('RGB')
        st.text("click on any position of image to know its coordinate")
        value = streamlit_image_coordinates(
            rgb_image,
            key = "local",
        )
        st.write(value)
    else:
        pass

with st.container():
    st.write("---")
    col1, col2 = st.columns(2)

    with col1:
        text_input = st.text_input(
            "Enter the text you want to enter in image 👇",
            value = ""
        )
        text_colour = st.radio(
            "select the colour of text",
            ("Red", "Green", "Blue")
        )
        if text_colour == 'Red':
            txt_clr = (255, 0, 0)
        elif text_colour == "Green":
            txt_clr = (0, 128, 0)
        elif text_colour == "Blue":
            txt_clr = (0, 0, 255)

        font_size = st.number_input(
            "Enter the font size of text 👇",
            key = int,
            min_value = 5, 
            max_value = 70,
            step = 1
        )
        col3, col4 = st.columns(2)

        with col3:
            val1 = st.number_input(
                "Enter x-coordinate",
                min_value = 0,
                step = 5
            )

        with col4:
            val2 = st.number_input(
                "Enter y-coordinate",
                min_value = 0,
                step = 5
            )

        list_val = [val1, val2]
        tuple_val = tuple(int(value) for value in list_val)

    with col2:
        if uploaded_image:
            I1 = ImageDraw.Draw(rgb_image)

            font = ImageFont.truetype('arial.ttf', font_size)    
            I1.text(tuple_val, text_input, font = font, fill = txt_clr)
            st.image(rgb_image, caption = 'uploaded_image')

            buf = BytesIO()
            rgb_image.save(buf, format = "JPEG")
            byte_im = buf.getvalue()

            btn = st.download_button(
                label = "Download Image",
                data = byte_im,
                file_name = "image.jpg",
                mime = "image/jpg",
            )

            submit = st.button("submit image")
            if submit:
                try:
                    entry = img_db(
                        name = name_input,
                        img = byte_im
                    )
                    sess.add(entry)
                    sess.commit()
                    st.success("Successful Submission :cow:")
                    st.snow()
                except Exception as e:
                    st.error(f"Error Occured {e}")
        else:
            pass
