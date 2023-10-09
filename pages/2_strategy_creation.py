import streamlit as st
from utils import workflow

st.header("Strategy Generator")
st.write("Generate the entire marketing strategy with the click of a button")
business_goals = st.text_input("Business Objectives")
target_market = st.text_input("Target Market")
generate_strategy = st.button("Generate Strategy")

if generate_strategy:

    st.header("Swot Analysis")
    swot = workflow.get_swot_analysis_from_form()
    st.write(swot)

    st.header("Strategy Goals")
    strategy_goals = workflow.get_strategy_goals(business_goals)
    st.write(strategy_goals)

    st.header("High Level Strategy")
    high_level_strategy = workflow.get_strategy_high_level(business_goals)
    st.write(high_level_strategy)

    st.header("Why, Mission, Values")
    why_mission_values = workflow.get_why_mission_values(business_goals,target_market)
    st.write(why_mission_values)

    st.header("Strategy Mapping")
    strategy_mapping = workflow.get_strategy_mapping()
    st.write(strategy_mapping)

    st.header("Marketing Objectives")
    marketing_objectives = workflow.get_marketing_objectives(business_goals)
    st.write(marketing_objectives)

    st.header("Marketing Plan")
    marketing_plan = workflow.get_marketing_plan()
    st.write(marketing_plan)



    
    
    
