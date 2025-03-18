from TravelAgents import guide_expert, location_expert, Planner_expert
from TravelTask import location_task, guide_task, planner_task
from crewai import crew, Process
import streamlit as st



st.title("TravelGpt")

st.markdown("Welcome to TravelGpt, a travel assistant that helps you plan your trips, find the best places to visit, and get information about your destination. ")

from_city = st.text_input("Enter your Current city" , "Okara")
destination = st.text_input("Enter your Destination city" , "Lahore")
date_from = st.date_input("Departure Date")
date_to = st.date_input("Return Date")
interest = st.text_input("What are you interested in?" , "Historical Places" , "Local cuisiner")


if st.button("Get Travel Plan"):
    if not from_city or not destination or not date_from or not date_to:
        st.error("Please fill all the fields")

    else:
        st.write("Planning Your Trip")

        loc_task = location_task(location_expert,from_city, destination, date_from, date_to)
        guid_task = guide_task(guide_expert, destination, interest , date_from, date_to)
        plan_task = planner_task(loc_task,Planner_expert, from_city, destination, date_from, date_to)

        crew = Crew(
            agents = [location_expert, guide_expert, Planner_expert],
            tasks = [loc_task, guid_task, plan_task],
            process = Process.sequential,
            full_output = True,
            verbose = True,
        )

        results = crew.kickoff()

        st.subheader("Your Travel Agent")
        st.markdown(results)


        travel_plan_text = str(results)
        st.download_button(
            label="Download Travel Plan",
            data=travel_plan_text,
            file_name="travel_plan.txt",
            mime="text/plain",
        )