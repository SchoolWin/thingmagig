import random
import streamlit as st

# Initialize session state variables
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
    st.session_state.remaining_objects = []  # Store objects that haven't been used

# List of science objects
scienceobjects = [
    "Thermometer", "Beaker", "Mortar and pestle", "Pipette", "Bunsen burner",
    "Heat mat", "Safety glasses", "Hot plate", "Test tubes", "Test tube rack"
]

# Reset the remaining objects at the start of the quiz
if not st.session_state.remaining_objects:
    st.session_state.remaining_objects = scienceobjects.copy()

st.title("Science Objects Quiz")

if not st.session_state.quiz_completed:
    st.write("Click Submit answer button, not enter key")
    st.write(f"Question {st.session_state.current_question + 1} of 10")

    # Generate a new question only if one hasn't been answered yet
    if not st.session_state.answered and st.session_state.selected_object is None:
        st.session_state.selected_object = random.choice(st.session_state.remaining_objects)
        st.session_state.remaining_objects.remove(st.session_state.selected_object)

    # Display image based on selected object
    try:
        image = f"Images/{st.session_state.selected_object}.webp"
        st.image(image)
    except:
        st.write(f"Showing image for: {st.session_state.selected_object}")

    # User input
    answer = st.text_input("What is the image above?").strip().lower()

    # Submit Answer button
    if st.button("Submit Answer") and not st.session_state.answered:
        st.session_state.answered = True

        if answer == st.session_state.selected_object.lower():
            st.success(f"Correct! The answer was {st.session_state.selected_object}!")
            st.session_state.score += 1
        else:
            st.error(f"Incorrect! The correct answer was {st.session_state.selected_object}!")

    # Show Next Question button **only after answering**
    if st.session_state.answered:
        if st.button("Next Question"):
            if st.session_state.current_question < 9:
                st.session_state.current_question += 1
                st.session_state.answered = False
                st.session_state.selected_object = None  # Reset for next question
                st.rerun()
            else:
                st.session_state.quiz_completed = True
                st.rerun()

# Show final score when quiz is completed
if st.session_state.quiz_completed:
    st.success(f"Your points are: {st.session_state.score} out of 10")

    if st.button("Restart Quiz"):
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.session_state.selected_object = None
        st.session_state.quiz_completed = False
        st.session_state.remaining_objects = scienceobjects.copy()  # Reset objects list
        st.rerun()
