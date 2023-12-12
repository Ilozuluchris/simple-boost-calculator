import streamlit as st

from blockchain_helper import boost_calc


@st.cache_data(ttl=4 * 60, show_spinner="Calculating boost")
def get_boost(claimant, number_of_weeks):
    return boost_calc(claimant, number_of_weeks)

def display_boost(claimant, number_of_weeks):
   max_boost, normal_boost = get_boost(claimant, number_of_weeks)
   print(max_boost)
   print(normal_boost)
   st.session_state['boost'] = f"Boost would be {max_boost+normal_boost}"

def run():

    st.title("Simple Boost Calculator")

    st.text_input("Claimant Address", key="claimant")

    st.number_input("No of weeks to lock", key="lock_time", step=1, min_value=0)

    st.button("Calculate claim", on_click=display_boost, args=[st.session_state['claimant'], st.session_state['lock_time']])

    st.text_input("Boost Calculated", key="boost")
    st.caption("Actual amount would be between 50% - 100% of calculated amount")

if __name__ == "__main__":
    run()
