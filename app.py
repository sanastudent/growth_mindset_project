import streamlit as st
from datetime import datetime
import os
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="Daily Reflection Journal",
    page_icon="📝",
    layout="centered"
)

# Add title and description
st.title("Daily Reflection Journal")
st.markdown("Take a moment to reflect on your day and document your experiences.")

# Get current date
current_date = datetime.now().strftime("%Y-%m-%d")
st.date_input("Date", datetime.now())

# Create form for daily reflection
with st.form("reflection_form"):
    # Learning section
    st.subheader("Learning")
    learning = st.text_area("What did you learn today?", 
                           placeholder="Reflect on new knowledge or insights gained...")
    
    # Challenges section
    st.subheader("Challenges")
    challenges = st.text_area("What challenges did you face and how did you overcome them?",
                             placeholder="Describe the obstacles you encountered and your solutions...")
    
    # Mistakes and lessons section
    st.subheader("Mistakes and Lessons")
    mistakes = st.text_area("What mistakes did you make, and what did you learn from them?",
                           placeholder="Reflect on your mistakes and the lessons learned...")
    
    # Additional reflections
    st.subheader("Additional Thoughts")
    additional = st.text_area("Any additional reflections or thoughts?",
                             placeholder="Share any other thoughts or feelings about your day...")
    
    # Submit button
    submitted = st.form_submit_button("Save Reflection")
    
    if submitted:
        # Here you can add code to save the reflection to a database
        st.success("Your reflection has been saved!")
        
        # Display a summary of the reflection
        st.subheader("Today's Reflection Summary")
        st.write(f"**Date:** {current_date}")
        st.write(f"**Learning:** {learning}")
        st.write(f"**Challenges:** {challenges}")
        st.write(f"**Mistakes and Lessons:** {mistakes}")
        st.write(f"**Additional Thoughts:** {additional}")

# Add a section to view and delete past reflections
if os.path.exists('reflections.csv'):
    st.subheader("Past Reflections")
    
    # Read the CSV file
    past_reflections = pd.read_csv('reflections.csv')
    
    # Add a delete button for each entry
    for index, row in past_reflections.iterrows():
        with st.expander(f"Reflection from {row['date']}"):
            st.write(f"**Learning:** {row['learning']}")
            st.write(f"**Challenges:** {row['challenges']}")
            st.write(f"**Mistakes and Lessons:** {row['mistakes']}")
            st.write(f"**Additional Thoughts:** {row['additional']}")
            
            # Delete button
            if st.button(f"Delete Entry", key=f"delete_{index}"):
                # Remove the entry
                past_reflections = past_reflections.drop(index)
                # Save back to CSV
                past_reflections.to_csv('reflections.csv', index=False)
                st.success("Entry deleted successfully!")
                st.rerun()

    # Display all entries in a table
    st.dataframe(past_reflections)
