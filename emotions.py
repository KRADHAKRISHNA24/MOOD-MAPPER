import streamlit as st
import pickle
import base64

#Load the trained model
with open(r"C:\Users\G0d\Machine Learning\Phase 2 Machine Learning\Emotion.pkl", 'rb') as model_file:
    model = pickle.load(model_file)

#Define the label to image path mapping
label_to_image = {
    "Sad": r"C:\Users\G0d\Downloads\Sad_Face_Emoji.png",
    "Joy": r"C:\Users\G0d\Downloads\Happy.png",
    "Love": r"C:\Users\G0d\Downloads\Heart_Eyes_Emoji.png",
    "Anger": r"C:\Users\G0d\Downloads\Angry_Emoji.png",
    "Fear": r"C:\Users\G0d\Downloads\Fearful_Face_Emoji.png",
    "Surprise": r"C:\Users\G0d\Downloads\surprised-face.png"
}

def get_image_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

#Set the title of the Streamlit app
st.title("Emotion Detection")

#Text input
input_text = st.text_area("Enter some text:")

#Button to trigger prediction
if st.button("DETECT"):
    if input_text:
        # Predict the emotion
        predicted_label = model.predict([input_text])[0]
        image_path = label_to_image.get(predicted_label, None)  # Get the image path

        # Display the predicted emotion and corresponding image
        if image_path:
            image_base64 = get_image_base64(image_path)
            st.write(f"Predicted Emotion: {predicted_label}")
            st.markdown(f'<img src="data:image/png;base64,{image_base64}" alt="{predicted_label}" style="width:300px;height:300px;">', unsafe_allow_html=True)
        else:
            st.write(f"Predicted Emotion: {predicted_label}")
    else:
        st.write("Please enter some text.")