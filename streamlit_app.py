import streamlit as st
from traffic_signal import update
from update_sheet import update_sheets

def run_input_interface():
    st.title("Traffic Signal Simulator - Input")

    img1 = st.file_uploader("Upload North Image", type=["jpg", "png", "jpeg"])
    img2 = st.file_uploader("Upload East Image", type=["jpg", "png", "jpeg"])
    img3 = st.file_uploader("Upload South Image", type=["jpg", "png", "jpeg"])
    img4 = st.file_uploader("Upload West Image", type=["jpg", "png", "jpeg"])

    if st.button("Process Images"):
        if img1 and img2 and img3 and img4:
            return img1, img2, img3, img4
        else:
            st.error("Please upload all four images.")
    return None, None, None, None

def run_output_interface(red, yellow, green):
    st.title("Traffic Signal Simulator - Results")

    st.write("### Signal Times")

    signal_directions = ['North', 'East', 'South', 'West']
    
    for i, direction in enumerate(signal_directions):
        st.write(f"**{direction} Signal Times:**")
        st.write(f"- Red: {red[i]} seconds")
        st.write(f"- Yellow: {yellow[i]} seconds")
        st.write(f"- Green: {green[i]} seconds")

    st.success("Processing complete and results displayed!")

def process_traffic_signals():
    if 'first_run' not in st.session_state:
        st.session_state.first_run = True

    if 'red' not in st.session_state:
        st.session_state.red = [84, 84, 84, 84]
    if 'yellow' not in st.session_state:
        st.session_state.yellow = [3, 3, 3, 3]
    if 'green' not in st.session_state:
        st.session_state.green = [25, 25, 25, 25]

    img1, img2, img3, img4 = run_input_interface()

    if img1 and img2 and img3 and img4:
        if st.session_state.first_run:
            st.write("### Initial Signal Times")
            run_output_interface(
                st.session_state.red, 
                st.session_state.yellow, 
                st.session_state.green
            )
            st.session_state.first_run = False
        else:
            st.session_state.red, st.session_state.yellow, st.session_state.green = update(
                img1, img2, img3, img4, 
                st.session_state.red, 
                st.session_state.yellow, 
                st.session_state.green
            )
            
            update_sheets(st.session_state.red, st.session_state.green)
            
            run_output_interface(
                st.session_state.red, 
                st.session_state.yellow, 
                st.session_state.green
            )

if __name__ == "__main__":
    process_traffic_signals()
