import streamlit as st
import time

class TrafficSignal:
    def __init__(self, name):
        self.name = name
        self.state = "RED"

    def set_state(self, state):
        self.state = state

    def __str__(self):
        return f"Traffic Signal {self.name} is {self.state}"

def display_traffic_signals(signals, containers):
    for idx, signal in enumerate(signals):
        with containers[idx]:
            st.write(f"**{signal.name}**")
            
            # Display the red light
            red_color = 'red' if signal.state == 'RED' else 'grey'
            st.markdown(f'<div style="background-color: {red_color}; width: 50px; height: 50px; margin-bottom: 10px;"></div>', unsafe_allow_html=True)
            
            # Display the yellow light
            yellow_color = 'yellow' if signal.state == 'YELLOW' else 'grey'
            st.markdown(f'<div style="background-color: {yellow_color}; width: 50px; height: 50px; margin-bottom: 10px;"></div>', unsafe_allow_html=True)
            
            # Display the green light
            green_color = 'green' if signal.state == 'GREEN' else 'grey'
            st.markdown(f'<div style="background-color: {green_color}; width: 50px; height: 50px; margin-bottom: 10px;"></div>', unsafe_allow_html=True)

def update_traffic_signals(signals, active_signal, cycle_times, containers):
    # Set all signals to red initially
    for signal in signals:
        signal.set_state("RED")

    # Activate the active signal
    active_signal.set_state("GREEN")
    display_traffic_signals(signals, containers)
    time.sleep(cycle_times['green'])

    # Change active signal to yellow
    active_signal.set_state("YELLOW")
    display_traffic_signals(signals, containers)
    time.sleep(cycle_times['yellow'])

    # Set active signal to red
    active_signal.set_state("RED")
    display_traffic_signals(signals, containers)
    time.sleep(cycle_times['red'])

def traffic_signal_simulation():
    # Define the traffic signals
    signals = [
        TrafficSignal("1 - North"),
        TrafficSignal("2 - East"),
        TrafficSignal("3 - South"),
        TrafficSignal("4 - West")
    ]

    # Define cycle times
    cycle_times = {
        'green': 5,
        'yellow': 2,
        'red': 5
    }

    # Create empty containers for each signal to update in place
    containers = st.columns(len(signals))

    # Simulate the traffic signals
    while True:
        for signal in signals:
            update_traffic_signals(signals, signal, cycle_times, containers)
            time.sleep(1)

if __name__ == "__main__":
    st.title("Traffic Signal Simulation")
    traffic_signal_simulation()
