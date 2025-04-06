import streamlit as st
import pandas as pd



# Setup session state to track if the quiz has started
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False

# --- START PAGE ---
if not st.session_state.quiz_started:
    st.title("What Smiski are you?")
    st.markdown(
        """ 
        Over the last year, Smiski collectables have gone viral and we can totally see why!  
    
        The adorable green characters have caught everyone's eye with their unique look of representing everyday life in their collections.  
        
        Whether it is a Work series for the workaholics, the Exercise Series for those who love an active life, or the Sunday series for those who try new things, there is a Smiski for everyone!  

        But the best part is that they come in surprise boxes.  You’ll never know which Smiski of the series you will get. Therefore this unboxing experience makes it extra fun for those who love a good surprise!
        """
    )

    if st.button("Start Quiz"):
        st.session_state.quiz_started = True

# --- QUIZ PAGE ---
homebody = 0
work = 0
exercise = 0
fashion = 0
hippers = 0
sundays = 0
if st.session_state.quiz_started:
    st.title("Smiski Personality Quiz")

    selected_q1 = st.selectbox(
       "If you’re at home alone, what’s your usual way to relax in the evening?",
       [   "Choose answer",
           "I enjoy reading a book or watching TV without distractions.",
           "I might spend time cooking or doing a hobby to unwind.",
           "I spend time scrolling through social media or watching videos on my phone.",
           "I spend time reflecting, journaling, or planning for the next day."
       ])

    selected_q2 = st.selectbox(
       "How do you prefer to spend your free time?",
       [   "Choose answer",
           "I like to work on my to do list and get some chores or work done.",
           "I might go shopping or do some online shopping.",
           "I usually go for a run, hit the gym, or do something active to relieve stress.",
           "I relax and do nothing—preferably on the couch or in bed."
       ])

    selected_q3 = st.selectbox(
       "When you feel stressed or overwhelmed, what’s your usual way of coping?",
       [   "Choose answer",
           "I like to take a break and practice a hobby.",
           "I might spend some time on TikTok.",
           "I like to go to the gym, take a fitness class, or even take a walk.",
           "I usually just power through the stress without doing much about it."
       ])

    selected_q4 = st.selectbox(
       "How do you typically choose what to wear for the day?",
       [   "Choose answer",
           "I grab whatever is clean and easy to put on.",
           "I choose something comfortable but still nice enough for the day ahead.",
           "I spend a good amount of time selecting an outfit that expresses my style and makes me feel confident.",
           "I usually wear whatever is closest, as long as it’s practical."
       ])

    selected_q5 = st.selectbox(
       "Choose something to watch…",
       [   "Choose answer",
           "A soccer game",
           "Anyone but You",
           "The Office",
           "Clueless"
       ])

    selected_q6 = st.selectbox(
       "Who was your favorite pop culture couple?",
       [   "Choose answer",
           "Justin Bieber and Selena Gomez",
           "Ronaldo and Georgina",
           "Taylor Swift and Travis Kelce",
           "Tom Holland and Zendaya" ])

    selected_q7 = st.selectbox(
       "Pick a snack!",
       [   "Choose answer",
           "Almonds",
           "Raspberries",
           "Chips",
           "Acai bowl"
       ])

    selected_q8 = st.selectbox(
       "Which Disney character would you go on a road trip with?",
       [   "Choose answer",
           "Stitch",
           "Maui",
           "Vanellope",
           "Olaf"
       ])

    selected_q9 = st.selectbox(
       "What skill do you wish you were better at?",
       [   "Choose answer",
           "Balancing things",
           "Being consistent",
           "Focusing",
           "Sewing"
       ])

    selected_q10 = st.selectbox(
       "Choose a hobby:",
       [   "Choose answer",
           "Working out",
           "Sleeping",
           "Baking",
           "Doing a puzzle"
       ])

    if st.button("Finish Quiz"):
        homebody = 0
        work = 0
        exercise = 0
        fashion = 0
        hippers = 0
        sundays = 0

        # Q1
        if selected_q1 == 'I enjoy reading a book or watching TV without distractions.':
            homebody += 1
        elif selected_q1 == 'I might spend time cooking or doing a hobby to unwind.':
            sundays += 1
        elif selected_q1 == 'I spend time scrolling through social media or watching videos on my phone.':
            hippers += 1
        elif selected_q1 == 'I spend time reflecting, journaling, or planning for the next day.':
            work += 1

        # Q2
        if selected_q2 == 'I like to work on my to do list and get some chores or work done.':
            work += 1
        elif selected_q2 == 'I might go shopping or do some online shopping.':
            fashion += 1
        elif selected_q2 == 'I usually go for a run, hit the gym, or do something active to relieve stress.':
            exercise += 1
        elif selected_q2 == 'I relax and do nothing—preferably on the couch or in bed.':
            homebody += 1

        # Q3
        if selected_q3 == 'I like to take a break and practice a hobby.':
            sundays += 1
        elif selected_q3 == 'I might spend some time on TikTok.':
            hippers += 1
        elif selected_q3 == 'I like to go to the gym, take a fitness class, or even take a walk.':
            exercise += 1
        elif selected_q3 == 'I usually just power through the stress without doing much about it.':
            work += 1

        # Q4
        if selected_q4 == 'I spend a good amount of time selecting an outfit that expresses my style and makes me feel confident.':
            fashion += 1

        # Q5
        if selected_q5 == 'A soccer game':
            exercise += 1
        elif selected_q5 == 'Anyone but You':
            homebody += 1
        elif selected_q5 == 'The Office':
            work += 1
        elif selected_q5 == 'Clueless':
            fashion += 1

        # Q6
        if selected_q6 == 'Justin Bieber and Selena Gomez':
            hippers += 1
        elif selected_q6 == 'Ronaldo and Georgina':
            exercise += 1
        elif selected_q6 == 'Taylor Swift and Travis Kelce':
            sundays += 1
        elif selected_q6 == 'Tom Holland and Zendaya':
            homebody += 1

        # Q7
        if selected_q7 == 'Almonds':
            work += 1
        elif selected_q7 == 'Raspberries':
            sundays += 1
        elif selected_q7 == 'Chips':
            hippers += 1
        elif selected_q7 == 'Acai bowl':
            fashion += 1

        # Q8
        if selected_q8 == 'Stitch':
            sundays += 1
        elif selected_q8 == 'Maui':
            exercise += 1
        elif selected_q8 == 'Vanellope':
            fashion += 1
        elif selected_q8 == 'Olaf':
            homebody += 1

        # Q9
        if selected_q9 == 'Balancing things':
            work += 1
        elif selected_q9 == 'Being consistent':
            sundays += 1
        elif selected_q9 == 'Focusing':
            hippers += 1
        elif selected_q9 == 'Sewing':
            fashion += 1

        # Q10
        if selected_q10 == 'Working out':
            exercise += 1
        elif selected_q10 == 'Sleeping':
            homebody += 1
        elif selected_q10 == 'Baking':
            sundays += 1
        elif selected_q10 == 'Doing a puzzle':
            work += 1

        # Determine top trait
        scores = {
            "Homebody": homebody,
            "Sunday": sundays,
            "Phone": hippers,
            "Work": work,
            "Fashion": fashion,
            "Exercise": exercise
        }

        top_trait = max(scores, key=scores.get)

        # Result output
        st.write(f"Thanks for completing the quiz! 💫 Your Smiski is: **{top_trait}**")

        if top_trait == 'Fashion':
            st.image('https://smiski.com/e/wp-content/uploads/2022/10/img_sweater.png')
        elif top_trait == 'Exercise':
            st.image('https://smiski.com/e/wp-content/uploads/2023/05/img_dumbbell.png')
        elif top_trait == 'Work':
            st.image('https://smiski.com/wp-content/uploads/2022/02/img_work_products_03.png')
        elif top_trait == 'Sunday':
            st.image('https://smiski.com/e/wp-content/uploads/2025/02/img_product_sunday05.png')
        elif top_trait == 'Homebody':
            st.image('https://smiski.com/e/wp-content/uploads/2019/07/img_bed_products_05.png')
        else:
            st.image('https://smiski.com/e/wp-content/uploads/2024/09/hippers_01.png')









