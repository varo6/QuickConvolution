"""
Streamlit documents: https://docs.streamlit.io/
"""

import streamlit as st
import signalpackage as sp

st.title("QuickConvolution :zap:")

# disable step up and down from input numbers
st.markdown("""
<style>
    button.step-up {display: none;}
    button.step-down {display: none;}
    div[data-baseweb] {border-radius: 4px;}
</style>""",
unsafe_allow_html=True)

st.write("See more details in the [help](#help) section.")

# declare session state parameters,  two objects "signal_1" and "signal_2", and toggle views will be booleans
if "signal_1" not in st.session_state:
    st.session_state["signal_1"] = None
if "signal_2" not in st.session_state:
    st.session_state["signal_2"] = None
if "show_signals" not in st.session_state:
    st.session_state["show_signals"] = [False, False, False]

# ADD SIGNALS SECTION ---------------------------------------------------------------------------------------------------

col1, col2 = st.columns([6, 6], gap="large")

with col1:
    st.subheader("First signal: ")
    subcol1, subcol2, a = st.columns([6, 8, 1], gap="small")

    if subcol1.button("Delete Signal", key="deletefirst"):
        st.session_state["signal_1"] = None
    
    if subcol2.button("Toggle view :bar_chart:", key="showfirst"):
        st.session_state["show_signals"][0] = not st.session_state["show_signals"][0]
    
    if st.session_state["show_signals"][0] == True and st.session_state["signal_1"] is not None:
        st.pyplot(st.session_state["signal_1"].show_values())
    else:
        st.write("Current toggle view: " + str(st.session_state["show_signals"][0]))
    

with col2:
    st.subheader("Second signal: ")
    subcol1, subcol2, a = st.columns([6, 8, 1], gap="small")

    if subcol1.button("Delete Signal", key="deletesecond"):
        st.session_state["signal_2"] = None
    if subcol2.button("Toggle view :bar_chart:", key="showsecond"):
        st.session_state["show_signals"][1] = not st.session_state["show_signals"][1]
    
    if st.session_state["show_signals"][1] == True and st.session_state["signal_2"] is not None:
        st.pyplot(st.session_state["signal_2"].show_values())
    else:
        st.write("Current toggle view: " + str(st.session_state["show_signals"][1]))

# CONVOLUTIONS SECTION-----------------------------------------------------------
st.divider()
c1, c2, c3 = st.columns([11,5,9])

if c2.button("Convolve!"):
    st.session_state["show_signals"][2] = not st.session_state["show_signals"][2]

if st.session_state["show_signals"][2] == True:
    if st.session_state["signal_1"] is not None and st.session_state["signal_2"] is not None:
        st.pyplot(st.session_state["signal_1"].show_convolution(st.session_state["signal_2"]))
elif st.session_state["show_signals"][2] == False:
    st.write("Current toggle view: " + str(st.session_state["show_signals"][2]))

# ---------------------------------------------------------------------------------
st.divider()

container = st.container(border = True)

# Horizontal alignment of two containers
two_containers = st.columns([12,12], gap="small")
 
# Container 1 section: Delta impulse -------------------------------------------------            
container_1 = two_containers[0].container(height=380)
container_1.header("Unit Impulse")    
item_111, item_112 = container_1.columns([3,3], gap="small")  
      
amp_1 = item_111.number_input(label="Amplitude",value=0, placeholder="Amplitude") 
t0_1 = item_112.number_input(label="Centered", value=0, placeholder="Tipe the centered number")  
       
# Disabled buttons
item_111.number_input(label="Width",value=0, disabled=True)   
item_112.number_input(label="input number", value=0, disabled=True, key="asd") 
        
if item_111.button("Add to signal 1", key="adddelta1"):       
    st.session_state["signal_1"] = sp.unitImpulse(amp_1, t0_1)   
if item_112.button("Add to signal2", key="adddelta2"):        
    st.session_state["signal_2"] = sp.unitImpulse(amp_1, t0_1)   
    
# Container 2 section: Square impulse -----------------------------------------------
          
container_2 = two_containers[1].container(height=380)
container_2.header("Square Impulse")    
item_211, item_212 = container_2.columns([3,3], gap="small")  
      
amp_21 = item_211.number_input(label="Amplitude",value=0, placeholder="hola", key="amp_21") 
t0_21 = item_212.number_input(label="Centered", value=0, disabled = False, key="amp_22") 
       
t_21 = item_211.number_input(label="Width",value=0, disabled=False, key="prueba")   
item_212.number_input(label="input number", value=0, disabled=True, key="asd2") 
        
if item_211.button("Add to signal 1", key="b121"):       
    st.session_state["signal_1"] = sp.SquareImpulse(amp_21, t0_21, t_21)   
if item_212.button("Add to signal 2", key="b122"):        
    st.session_state["signal_2"] = sp.SquareImpulse(amp_21, t0_21, t_21)  

# Container 3----------------------------------------------------------------------

          
container_3 = two_containers[0].container(height=380)
container_3.header("Triangle Impulse")    
item_311, item_312 = container_3.columns([3,3], gap="small")  
      
amp_3 = item_311.number_input(label="Amplitude",value=0, placeholder="Amplitude", key="amp31") 
t0_3 = item_312.number_input(label="Centered", value=0, placeholder="Centered", key="amp32")                    
t_3 = item_311.number_input(label="Width",value=0, key="n311") 

item_312.number_input(label="input number", value=0, disabled=True, key="n312") 
        
if item_311.button("Add to signal 1", key="b311"):       
    st.session_state["signal_1"] = sp.TriangleImpulse(amp_3, t0_3, t_3)   
if item_312.button("Add to signal2", key="b312"):        
    st.session_state["signal_2"] = sp.TriangleImpulse(amp_3, t0_3, t_3)   

#Container 4: custom function -----------------------------------------------------

container_4 = two_containers[1].container(height=380)
container_4.header("Custom Function")    
item_311, item_312 = container_4.columns([3,3], gap="small")  
      
item_311.number_input(disabled = True, label="input number",value=0, placeholder="", key="amp41") 
item_312.number_input(disabled = True, label="input number", value=0, placeholder="Type a number...", key="amp42")             
       
item_311.number_input(label="input number",value=0, disabled=True , key="n411")   
item_312.number_input(label="input number", value=0, disabled=True, key="n412") 
 
st.subheader("Help", anchor="help", divider="gray")    
st.write("(Temporary help section)This app is designed to perform convolutions with predefined signals, focusing on some of the most commonly used when starting to learn convolutions. Simply add your first and second signal, and convolve them! To have a reference when creating the signals, check the Delta, Square, and Triangular Pulses sections.")
  
st.subheader("Unit impulse")

st.write("Unit pulses, also known as Dirac's Delta, refers to a pulse whose value is 1 when t=0, and 0 otherwise. we represent it as ")

st.latex(r'''\delta(t) = \begin{cases}
        1 & \text{if } t = 0 \\
        0 & \text{otherwise}
\end{cases}''')


st.write("Therefore, we can change the amplitude and center of the signal in Delta Pulse section, and it will be represented as: ")

st.latex(r'''A\delta(t-t_{0}) = \begin{cases}
        A & \text{if } t = t_{0} \\
        0 & \text{otherwise}
\end{cases}''')

st.subheader("Square impulse")
st.write("A square impulse maintains a constant constant amplitude value (A) over a finite duration (width) and is zero elsewhere. It can be represented as:")
st.latex(r'''\Pi(t) = \begin{cases}
        A & \text{if } t_0 - \frac{T}{2} \leq t \leq t_0 + \frac{T}{2} \\
        0 & \text{otherwise}
\end{cases}''')

st.subheader("Triangle impulse")
st.write("A triangle impulse linearly increases to a peak amplitude value and then linearly decreases back to zero over a finite duration (width), with a center of $t_0$.")

st.write("You can now check how they work by adding plotting them.")

