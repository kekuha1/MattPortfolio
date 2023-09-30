from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":tada", layout="wide")

def load_lottueurl(url):
     r = requests.get(url)
     if r.status_code != 200:
          return None
     return r.json()
#use CSS
def local_css(file_name):
     with open(file_name) as f:
          st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")          

#---asset---
lottie_coding = load_lottueurl("https://lottie.host/ebad370d-3ed6-4d97-900a-0b5235e55c51/7WmeRy7pig.json")
img_cybertruck_1 = Image.open("images/cybertruck1.jpg")
#----Header----
with st.container():
    st.subheader("Hi, I am Matt :wave:")
    st.title("A Manufacturing Quality Engineer from California")
    st.write(" I am passionate about improving quality standards by meeting craftsmanship targets")
    st.write("[Learn More >](https://www.linkedin.com/in/matthew-rayes-829452105)")


#----What I do----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
            st.header("What I do")
            st.write("##")
            st.write(
                 """
                 At Tesla I am:
                  - Reducing the frequency of #1 nonconformity from 30% to 1% through identification and validation of design improvements
                  - Supported a 300 percent ramp in 1 year through quality improvements onsite and at suppliers
                  - Visioned and championed work content reduction to reduce headcount, saving $200,000+ annually
                  - Partnered with cross functional teams to improve fit, increase repeatability and balance cycle times
                  - Sustained daily yield through identification and implementation of short term countermeasures  
                 """)
            
        
    with right_column:       
            st.lottie(lottie_coding, height=300, key="tesla")

            #---Projects---
with st.container():
        st.write("---")
        st.header("My Projects")
        st.write("##")
        image_column, text_column = st.columns((1, 2))
        with image_column:
              st.image(img_cybertruck_1)  
              with text_column:
               st.subheader("Cybertruck")
               st.write(
                    """
                    - Systematically developed RFQ’s for various stamping / metal forming equipment such as blanking, Transfer line & Tandem Lines ($10-30 million Capex). 
                    
                    - Evaluated & selected equipment for stamping facilities based technical capability of various suppliers according to Tesla requirements.

                    - Managed design optimization of new blanking equipment projects in Texas, Berlin & Shanghai resulting in an estimated ~11% OEE improvement compared to previous projects. 

                
                    """)  
               
#----Contact----
with st.container():
     st.write("---")
     st.header("Contact Me")
     st.write("##")

     #----form----
     contact_form = """
    <form action="https://formsubmit.co/matthewrayes@gmail.com" method="POST">
     <input type ="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea> 
     <button type="submit">Send</button>
    </form>
    """  
     
left_column, right_column = st.columns(2)
with left_column:
     st.markdown(contact_form, unsafe_allow_html=True)
    