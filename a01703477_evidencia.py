import streamlit as st
import pandas as pd

with open(file_name, "rb") as template_file:
        template_byte = template_file.read()

    st.download_button(label="Click to Download Template File",
                        data=template_byte,
                        file_name="Police_Department_Incident_Reports__2018_to_Present.xlsx",
                        mime='application/octet-stream')

st.title('Police Incident Reports from 2018 and 2020 in San Francisco')

df = pd.read_csv("https://drive.google.com/file/d/1ioUp8979nNLh9h-CYVyJcRgAhxBhCLIm/view?usp=sharing")

st.markdown('The data shown below belongs to incident reports in the city of San Francisco, from the year 2018 to 2020, with details from each case such as date, day of the week, police district, neighborhood in which it happened, type of incident in category and subcategory, exact location and resolution.')

mapa=pd.DataFrame(longitude)
mapa['Latitude'] = df['Latitude']
mapa['Longitude'] = df['Longitude']
mapa=mapa.dropna()
st.map(mapa.astype(int))
