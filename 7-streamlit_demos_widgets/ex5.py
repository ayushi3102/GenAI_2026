import streamlit as st
import datetime

date = st.date_input("Select date")
print(type(date))

st.write("You selected",date)
st.write("You selected",date.strftime("%d-%m-%Y"))
st.write("Day",date.day)
st.write("Month",date.month)
st.write("Year",date.year)

custom_date = st.date_input("Select date",min_value = datetime.date(2020,1,1),max_value= datetime.date(2027,12,31))
st.write("You selected",custom_date)


time = st.time_input("Select time ")
st.write("You selected",time)
st.write("hour :",time.hour)
st.write("mins :",time.minute)
st.write("seconds :",time.second)