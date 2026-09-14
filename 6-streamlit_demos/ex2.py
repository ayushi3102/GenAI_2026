import streamlit as st

st.markdown("This is plain text")
st.markdown("**This** is bold example - **Ayushi**")  # ** is for bold
st.markdown("*This* is italic example - *Ayushi*")   # * is for italic
st.markdown("""This is italic example of new line    
             Ayushi""")                             # double space is for next line

st.markdown("This is strike through example - ~~Ayushi~~")   # ~~ double tilde is for strile through
st.markdown("*This* is bold+italic example - ***Ayushi Chaurasia***")   # *** for both bold italic

st.markdown(""" # heading 1  
## heading 2
### heading 3""")   #  # to represent headings

st.markdown("Ayushi  \n works in  \n company ")          # another way to next line is double space with /n     
st.markdown("""
 -Python
 -Java
 -CSS
""")                             # unordered list             

st.markdown("""
 - Python
    - Core python 
 - JavaScript
    - NodeJS
    - ReactJS
 - CSS
   - Tailwind
""")                             # nested unordered list 


 
