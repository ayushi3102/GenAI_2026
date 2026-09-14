import streamlit as st

from datetime import datetime
import time

placeholder = st.empty()   #this create a websection on our web page and return its reference
while True:
    obj = datetime.now()
    placeholder.write(f"{obj.strftime('%H:%M:%S')}")
    time.sleep(1)
    


