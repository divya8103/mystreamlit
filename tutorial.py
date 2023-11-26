import streamlit as st
st.set_page_config(page_title='MyStreamlit',page_icon='shark')
mymenu=st.sidebar.selectbox('My Menu',('Home','FillForm','Downloads'))
st.image('https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA1a1D8N.img?w=48&h=48&q=60&m=6&f=png&u=t')
st.title('Onlie Technologies')
st.header('By Divya')
st.text('This is a tutorial on Streamlit Library')
st.image('https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA1kxsa5.img?w=534&h=300&m=6&x=799&y=90&s=47&d=47.png')
if(mymenu=='Home'):
    st.markdown('<center><h1>STEVE JOBS SPEECH</h1></center>',unsafe_allow_html=True)
    st.video('https://www.youtube.com/watch?v=Ad8_ACQbzVE')
elif(mymenu=='FillForm'):
    with st.form('My Form'):
        name=st.text_input('Enter Name')
        dob=st.date_input('Enter/Choose DOB')
        marks=st.slider('Enter Marks')
        k=st.form_submit_button('Submit Form')
        if k:
            st.write('Name=',name,'DOB:',dob,'Marks:',marks)
     
elif(mymenu=='Downloads'):
    st.header("Downloads")
    st.download_button('Download Now','hello this is the downloaded data','onlie.txt')
