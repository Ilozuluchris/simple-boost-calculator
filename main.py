import streamlit as st

from blockchain_helper import boost_calc


@st.cache_data(show_spinner="Calculating boost")
def get_boost(claimant, number_of_weeks, token_amount):
    return boost_calc(claimant, number_of_weeks, token_amount)


def display_boost(claimant, number_of_weeks, token_amount_to_lock):
    max_boost, normal_boost = get_boost(claimant, number_of_weeks,
                                        token_amount_to_lock)
    scaled_num = (normal_boost / 1e18)  # handle the decimals of the token
    num_in_thousands = scaled_num / 1000
    st.session_state['boost'] = f"Boost would be {round(num_in_thousands,2)}k"


def run():

    st.title("Simple Boost Calculator")

    st.text_input("Claimant Address", key="claimant")

    st.number_input("Token Amount To Lock", key="lock_amount", step=1,
                    min_value=0)

    st.number_input("No of weeks to lock", key="lock_time", step=1,
                    min_value=0, max_value=52)

    st.button("Calculate Boost", on_click=display_boost,
              args=[st.session_state['claimant'], st.session_state['lock_time'],
                    st.session_state['lock_amount']])

    st.text_input("Boost Calculated", key="boost")
    st.caption("Boost amount at week specified. Actual amount would be between"
               " 50% - 100% of calculated amount and changes per week ")


if __name__ == "__main__":
    run()
