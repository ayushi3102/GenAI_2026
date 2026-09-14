import streamlit as st
import datetime


dict = {'Consultation':500,'Preminum':1000,'Emergency':1500}

if "bookings" not in st.session_state:
    st.session_state.bookings = []
st.title("Appointment Booking & Cost Calculator")

app_date = st.date_input("Select appointment date")
app_time = st.time_input("Select appointment time", value  = datetime.time(10,0))
service = st.selectbox("Select Service",['Consultation','Preminum','Emergency'])
duration = st.number_input("Duration(hours)",min_value=1,max_value=8,step=1)
cost = dict[service]*duration
st.write("Estimated Cost :",cost)

agree = st.checkbox("I agree to the terms")
if agree:
    st.info("Thanks for agreeing")

confirm = st.button("Confirm Booking")

if confirm :
    booking = {"date":app_date,"time":app_time,"service":service,"duration":duration,"cost": cost}
    st.session_state.bookings.append(booking)
    st.success("Appointment Booked")

st.subheader("Your Bookings")
if st.session_state.bookings:
    for idx,b in enumerate(st.session_state.bookings,start=1) :
        st.write(idx,'.',b['date'], '|',b['time'], '|',b['service'],  '|',b['duration'], '|',b['cost'])



