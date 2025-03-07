#Adds the random command
import random
#Imports the website opporator
import streamlit as st
#Imports os to find if image exists
import os

#Sets up status
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'selected_object' not in st.session_state:
    st.session_state.selected_object = None
if 'answered' not in st.session_state:
    st.session_state.answered = False
if 'quiz_completed' not in st.session_state:
    st.session_state.quiz_completed = False
if 'remaining_objects' not in st.session_state:
    st.session_state.remaining_objects = []  

#list of objects
scienceobjects = [
    "Thermometer", "Beaker", "Mortar and pestle", "Pipette", "Bunsen burner",
    "Heat mat", "Safety glasses", "Hot plate", "Test tubes", "Test tube rack"
]

#resets remaining objects if empty
if not st.session_state.remaining_objects:
    st.session_state.remaining_objects = scienceobjects.copy()

#States title
st.title("Science Objects Quiz")

#Starts loop for 10 questions of quiz
if not st.session_state.quiz_completed:
    
    #Tells them to click submit not enter
    st.write("Click *Submit Answer* Button, not the ENTER key.")

    #Shows question number
    st.write(f"Question {st.session_state.current_question + 1} of 10")

    #Picks objects then removes from list
    if not st.session_state.answered and st.session_state.selected_object is None:
        st.session_state.selected_object = random.choice(st.session_state.remaining_objects)
        st.session_state.remaining_objects.remove(st.session_state.selected_object)

    #Displays image
    try:
        image = f"Images/{st.session_state.selected_object}.webp"
        os.path.exists(image)
        st.image(image)
    except:
        st.write(f"Showing image for: {st.session_state.selected_object}")

    #Input for the answer
    answer = st.text_input("What is the image above?").strip().lower()
    st.session_state.answer = True
    
    #Submit button for answer
    if st.button("Submit Answer") and not st.session_state.answered:
        st.session_state.answered = True

        #Shows that their answer is correct if they guess correctly
        if answer == st.session_state.selected_object.lower():
            st.success(f"Correct! The answer was {st.session_state.selected_object}!")
            st.session_state.score += 1
        
        #Shows answer is incorrect and shows correct answer
        else:
            st.error(f"Incorrect! The correct answer was {st.session_state.selected_object}!")

    #Shows answer button only after clicking submit
    if st.session_state.answered:
        if st.button("Next Question"):
            if st.session_state.current_question < 9:
                st.session_state.current_question += 1
                st.session_state.answered = False
                st.session_state.selected_object = None #resest for next question
                st.rerun()
            else:
                st.session_state.quiz_completed = True
                st.rerun()

#Shows question points after quiz is completed
if st.session_state.quiz_completed:
    st.success(f"Your points are: {st.session_state.score} out of 10")

    #Restarts the quiz and resets everything
    if st.button("Restart Quiz"):
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.session_state.selected_object = None
        st.session_state.quiz_completed = False
        st.session_state.remaining_objects = scienceobjects.copy()  
        st.rerun()
