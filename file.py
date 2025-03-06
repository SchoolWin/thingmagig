#imports the randomised as character
import random
import streamlit as st
#.venv\scripts\activate

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


#the random chance of the characters
scienceobjects = ["Thermometer", "Beaker", "Mortar and pestle", "Pipette", "Bunsen burner", "Heat mat", "Safety glasses", "Hot plate", "Test tubes", "Test tube rack"]

st.title("Science Objects Quiz")

#The quiz about what object
if not st.session_state.quiz_completed:
    #Fix to code sometimes
    st.write("If it comes up with an error try press the button again")
    # Show current question number
    st.write(f"Question {st.session_state.current_question + 1} of 10")
    
    # If we need a new question
    if not st.session_state.answered:
        st.session_state.selected_object = random.choice(scienceobjects)  # Chooses a random object
        
    # Display image based on selected object
    try:
        image = f"Images/{st.session_state.selected_object}.webp"
        st.image(image)
    except:
        st.write(f"Showing image for: {st.session_state.selected_object}")
    
    # Get user answer
    answer = st.text_input(f"What is the image above?").strip().lower() #The answer they input
    
    if st.button("Submit Answer") and not st.session_state.answered:
        st.session_state.answered = True
        
        if answer == st.session_state.selected_object.lower(): #If the answer is = the ramdom object they score a point
            st.success("Correct!")
            st.session_state.score += 1

        #They get told it's inccorect, get told what it was and don't score an point
        else:
            st.error(f"Incorrect! The correct answer was {st.session_state.selected_object}.") #They get told it's inccorect, get told what it was and don't score an point
        
        # Advance to next question or end quiz
        if st.session_state.current_question < 9:
            if st.button("Next Question"):
                st.session_state.current_question += 1
                st.session_state.answered = False
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
        st.session_state.quiz_completed = False
        st.rerun()