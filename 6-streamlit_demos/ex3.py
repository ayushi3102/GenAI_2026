import streamlit as st

st.markdown("[open google](https://www.google.com/)")  # anchor tag using []

st.markdown("Use ` pip install streamlit ` to install stremalit")  # for decorating using ``

st.markdown("""
```python
def hello():  
    print(hello)
""")                          # ```python - this will make code view in python

st.markdown("""
```javascript
const show =()=>{
    console.log("HELLO")
}
""")   