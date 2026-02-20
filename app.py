import streamlit as st
import hashlib
import traceback
import time

# ---------------- CONFIG ----------------
st.set_page_config(page_title="VLAD :: Developer Mode", page_icon="🟢")

TARGET_NAME = "vlad"
TARGET_AGE = 15
TOTAL_LEVELS = 5

# ---------------- STYLE ----------------
st.markdown("""
<style>
html, body, [class*="css"]  {
    background-color: black;
    color: #00ff88;
    font-family: "Courier New", monospace;
}

textarea {
    background-color: #0d0d0d !important;
    color: #00ff88 !important;
    border: 1px solid #00ff88 !important;
}

.stButton>button {
    background-color: black;
    color: #00ff88;
    border: 1px solid #00ff88;
}

.stButton>button:hover {
    background-color: #00ff88;
    color: black;
}

.blink {
    animation: blink 1s step-start infinite;
}

@keyframes blink {
    50% { opacity: 0; }
}
</style>
""", unsafe_allow_html=True)

# ---------------- SESSION ----------------
if "level" not in st.session_state:
    st.session_state.level = 1

if "completed" not in st.session_state:
    st.session_state.completed = False

# ---------------- HEADER ----------------
st.markdown(f"""
# 🟢 TARGET DETECTED
    > Name: VLAD  
    > Age: {TARGET_AGE}  
    > Status: Developer Candidate  
    > Initializing Birthday Protocol...
""")

progress = st.session_state.level / TOTAL_LEVELS
st.progress(progress)

# ---------------- SUCCESS SCREEN ----------------
if st.session_state.completed:
    st.markdown("""
    ## 🟢 ACCESS GRANTED
    > Well done, Vlad.
    > System confidence: 100%
    > Proceed to next challenge...
    """)
    st.balloons()

    if st.button(">>> CONTINUE"):
        st.session_state.level += 1
        st.session_state.completed = False
        st.rerun()

# ================= LEVEL 1 =================
elif st.session_state.level == 1:
    st.subheader("LEVEL 1 :: Age Verification Protocol")
    st.write("Напиши функцію age_power(x), яка повертає x у степені 2.")

    code = st.text_area(">>> ENTER CODE", """def age_power(x):
    # your code here
    pass
""")

    if st.button(">>> EXECUTE"):
        try:
            env = {}
            exec(code, {}, env)

            if "age_power" in env:
                func = env["age_power"]
                tests = [(2, 4), (3, 9), (15, 225)]

                if all(func(x) == y for x, y in tests):
                    st.session_state.completed = True
                    st.rerun()
                else:
                    st.error("❌ Function logic incorrect")

        except Exception:
            st.error("❌ Function logic incorrect")

# ================= LEVEL 2 =================
elif st.session_state.level == 2:
    st.subheader("LEVEL 2 :: String Encryption")
    st.write("Створи функцію reverse_name(name), яка перевертає рядок.")

    code = st.text_area(">>> ENTER CODE", """def reverse_name(name):
    # your code here
    pass
""")

    if st.button(">>> EXECUTE"):
        try:
            env = {}
            exec(code, {}, env)

            if "reverse_name" in env and env["reverse_name"]("vlad") == "dalv":
                st.session_state.completed = True
                st.rerun()
            else:
                st.error("❌ Decryption failed")

        except Exception:
            st.error("❌ Function logic incorrect")

# ================= LEVEL 3 =================
elif st.session_state.level == 3:
    st.subheader("LEVEL 3 :: Rockstar Algorithm")
    st.write("Обчисли суму чисел від 1 до 15 та збережи у змінну total.")

    code = st.text_area(">>> ENTER CODE", """total = 0

# your code here
""")

    if st.button(">>> EXECUTE"):
        try:
            env = {}
            exec(code, {}, env)

            if "total" in env and env["total"] == 120:
                st.session_state.completed = True
                st.rerun()
            else:
                st.error("❌ Algorithm incorrect")

        except Exception:
            st.error("❌ Algorithm incorrect")

# ================= LEVEL 4 =================
elif st.session_state.level == 4:
    st.subheader("LEVEL 4 :: Guitar Code")
    st.write("Створи рядок secret, який дорівнює 'VLAD_15_ROCKS'")

    code = st.text_area(">>> ENTER CODE", """# create variable secret
""")

    if st.button(">>> EXECUTE"):
        try:
            env = {}
            exec(code, {}, env)

            if "secret" in env and env["secret"] == "VLAD_15_ROCKS":
                st.session_state.completed = True
                st.rerun()
            else:
                st.error("❌ Secret key incorrect")

        except Exception:
            st.error("❌ Secret key incorrect")

elif st.session_state.level == 5:
    st.subheader("FINAL :: Birthday Override")

    if "final_stage" not in st.session_state:
        st.session_state.final_stage = 0

    if st.button(">>> INITIATE FINAL SEQUENCE"):
        st.session_state.final_stage = 1
        st.rerun()

    if st.session_state.final_stage >= 1:

        with st.empty():
            st.markdown("```ACCESSING MAINFRAME...```")
            time.sleep(1)

        with st.empty():
            st.markdown("```DECRYPTING PERSONAL DATA...```")
            time.sleep(1)

        with st.empty():
            st.markdown("```VERIFYING TARGET: VLAD```")
            time.sleep(1)

        with st.empty():
            st.markdown("```AGE CONFIRMED: 15```")
            time.sleep(1)

        with st.empty():
            st.markdown("```DEVELOPER STATUS: ELITE```")
            time.sleep(1)

        st.session_state.final_stage = 2

    if st.session_state.final_stage >= 2:

        st.markdown("""
        # 🟢 SYSTEM OVERRIDE SUCCESSFUL

        ---
        # 🎉 Вітаємо, Влад! 🎉
        ---

        > ### Developer Rank: 🔥 LEGENDARY  
        > ### Guitar Skill: 🎸 ROCKSTAR  
        > ### Intelligence Level: 🧠 OVER 9000  
        > ###   Age Level: 15 UNLOCKED  

        ---

        > Любий Влад, вітаємо тебе з твоїм 15-річчям!  
        > Ти – надзвичайно **розумний**, **творчий**, **талановитий**,  
        > справжній **програміст** і **рок-зірка**.  
        > Твоя наполегливість, кмітливість та допитливість надихають усіх навколо.  
        
        ---
        ### 🎁 Особливий сюрприз чекає на тебе:
        
        Щоб його отримати — пошукай коробку під деревом.  
        Нехай це буде маленька таємниця для справжнього дослідника і легендарного розробника.  
        
        ---
        
        > Продовжуй мріяти, кодувати, грати на гітарі і бути собою.  
        > Світ чекає на твої відкриття!  
        
        ---
        
        # 🟢 Birthday Protocol Completed
        ### З Днем Народження, Влад! 🚀🎂🎸
        """)

        st.balloons()
        st.snow()
