import streamlit as st

st.title('Power Calculator')
st.subheader('calculate the square cube and fifth power of input number')


value=st.number_input("enter a number",value=1,step=1)

if value:
    st.write(f'The Square is {value**2}')
    st.write(f'The Cube is {value **3}')
    st.write(f'The Fifth is {value**5}')

