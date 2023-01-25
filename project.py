import streamlit as st
import requests
from streamlit_lottie import st_lottie


st.set_page_config(page_title="A Quiz", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()


#----LOAD ASSETS----
lottie_coding =load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_jamhkybo.json")

#----HEADER SECTION----
st.subheader("Hi!")
st.write("##")
st.write(
    """
    Welcome! This is a quiz that is about yourself! 
    We would love to hear your opinions on differant
    controversial things which is popular in the internet

    """
)


#----Who am I?----
st.write("---")
left_column, right_column = st.columns(2)
with left_column:
    st.header("Who am I?")
    st.write("##")
    st.write(
        """
        I used to be a youtuber with almost 700 subscribers, but now that I lost intrest, I am a developing a website
        Believe it or not, I am actually 15! Coding is my passion and I like it a lot, this is my first website, I hope you like it
        If you are intrested in my yt here it is, [Youtube!](https://www.youtube.com/channel/UCeLDCifVkpKaRBpiwhjAHmQ/videos)"

        """        
    )


with right_column:
    st_lottie(lottie_coding, height=300, key="coding")

#----Quiz----
st.write("---")

name = st.text_input("1.Whats your name?")

st.number_input("2.Whats your age?")

color = st.text_input("3.Whats your favorite color")

st.write("Ok lets get started with the contreversial question in the internet")

ronaldo = st.text_input("4.Who is your favorite football/soccer player? Messi or Ronaldo")

st.text_input("5.What's your favorite movie?")

st.text_input("6.What do you prefer? Pizza or Burgers?")

st.text_input("7.Who is your favorite youtuber?")

st.text_input("8.What is your nationality")

st.text_input("9.What's your favorite drink")

st.text_input("10.What's your favorite country to be in?")

st.subheader("Thank you so much for taking your time taking this Quiz.. I hope it was fun. Thank you!")

#----Contact----

st.write("---")
st.header("CONTACT ME!")


contact_form = """

<form action="https://formsubmit.co/aquizcontact@gmail.com" method="POST">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message" required></textarea>
     <button type="submit">Send</button>
</form> 
"""
st.markdown(contact_form, unsafe_allow_html=True)