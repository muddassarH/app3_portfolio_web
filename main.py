import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg", width=600)

with col2:
    st.title("Muddassar Hussain")
    text = """
    My name is Muddassar Hussain. I am Electronic Engineer , from University 
of Engineering & technology Peshawar,Abbottabad Campus Pakistan .
I am looking forward to taking this course, unfortunately; I come from a 
lower-middle-class Pakistani family, and the exchange rate from 
Pakistani rupee (my country's currency) to dollars is very high, making 
the possibility of funding the course myself impossible. Presently, I 
work in my community as a part-time home lesson teacher, and my monthly 
stipend, which is below the course fee, is barely enough to cover my 
needs and those of my family members as part of the breadwinner.
I lost my job during the COVID-19 outbreak and have had a tough time 
landing another job because my country's economy is facing a downturn. It 
will be an immense relief to get financial aid for this course. Thank you 
for taking your time to consider my request.
My monthly stipend is less than the course fee, and a part of my family 
depends on it, preventing me from paying for the course.
I'm not even sure I'll be able to pay back the loan, considering my 
financial challenge. As I have a limited source of income.
    I am Electronic Engineer by education and Python developer by Profession. 
    i am working myself on different projects for my practice and ,
    i have created todo app, 
    A Webcam reader app that will access your web cam and take photo by clicking and convert it into a gray scale photo.
    """
    st.info(text)
content = """
Below You can find the app i have built in python .Feel Free to Contact Me:
"""
st.write(content, font=20)
