import streamlit as st 
import numpy as np
import pandas as pd

material_properties = {
    "Aluminum": {"cp": 0.215, 'h':94.6},  
    "Copper": {"cp": 0.0923, 'h': 49.2},
    "Iron": {"cp": 0.108, 'h': 59},
    "Gold": {"cp": 0.092, 'h': 15},   
    "Silicon": {"cp": 0.170, 'h': 427},
    "White Pig Iron": {'cp': 0.13, 'h': 65},
    "Brass":{'cp':0.09,'h':35.8}
    
}


st.title('PERFORMANCE ASSESMENT OF INDUCTION FURNACE')

col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    st.subheader('Input Parameters')
    material=st.selectbox('Metal Type:',options=list(material_properties.keys()))
    total_energy_input=st.number_input('Electrical energy input(KWh):',min_value=1.0,step=1.0)
    time=st.number_input('Time(hours):',min_value=1.0,step=1.0)
    weight_of_material=st.number_input('Metal Weight(Kg):',min_value=1.0,step=0.1)
    cost_per_kwh=st.number_input('Cost per KWh(Local currency):',min_value=0.01,step=0.01)
    initial_temp=st.number_input('Initial Temperature(Celsius):',min_value=1.0,step=1.0)
    final_temp=st.number_input('Final Temperature(Celsius):',min_value=1.0,step=1.0)
if total_energy_input < 1 or time < 1 or weight_of_material < 1 or cost_per_kwh < 1 :
    st.warning("Please select a value no less than 1 for all inputs.")
    


cp = material_properties[material]['cp']  
Q = (weight_of_material * cp * (final_temp - initial_temp))/860

 

if (total_energy_input > 0):
    efficiency = (Q / total_energy_input) * 100
else:
    efficiency = 0
    
total_cost=total_energy_input*cost_per_kwh

with col2:
    st.subheader('Results')
    st.metric(label="Total Energy Input (KWh)", value=f"{total_energy_input:.2f} KWh")
    st.metric(label="Energy absorbed by metal (Q)", value=f"{Q:.2f} KWh")
    st.metric(label="Efficiency of Furnace", value=f"{efficiency:.2f} %")
    st.metric(label="Cost of operating furnace", value=f"{total_cost:.2f} ₹")
    st.image("C:\\Users\\Rancan\\Pictures\\Screenshots\\Screenshot 2024-09-29 215700.png", caption="Induction furnace losses", use_column_width=True)
   
with col3:
    st.subheader('Graphs')
    st.write('Temperature-Time')
    time_points = np.linspace(0, time, 100)  
    print("Time points:", time_points)  
    if time > 0:  
        temperatures = initial_temp + ((final_temp - initial_temp) / time) * time_points  
        print("Temperatures:", temperatures)  
        df_temp = pd.DataFrame({
            'Time (Hours)': time_points,
            'Temperature (°C)': temperatures
        })
        st.line_chart(df_temp)  
    else:
        st.error("Time must be greater than 0.")

st.subheader('-Healthy operating practices for induction furnaces.')
st.markdown('-Always run the furnace with full power.')
st.markdown('-Use lid mechanism for furnace crucible, radiation heat loss accounts for 4 – 6 % input of energy.')
st.markdown('-Select the correct lining material.')
st.markdown('-Monitor lining performance.')
st.markdown('-Do not allow furnace to cool very slow. Forced air cooling helps in developing cracks of lower depth')
st.markdown('''
<style>
[data-testid="stMarkdownContainer"] ul{
    padding-left:40px;
}
</style>
''', unsafe_allow_html=True)
