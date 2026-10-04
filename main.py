import streamlit as st

st.set_page_config(page_title="EduGenie")
st.title("EduGenie - Your Teacher 🔥")
st.write("En kitta etha vena kelu da!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

if q := st.chat_input("Un doubt enna da?"):
    with st.chat_message("user"):
        st.markdown(q)
    st.session_state.messages.append({"role":"user","content":q})

    with st.chat_message("assistant"):
        low = q.lower()
        
        if "largest ocean" in low or "biggest ocean" in low:
            ans = """**1. Which is the largest ocean?**

**Pacific Ocean da!**

- World la periya ocean ithu than da
- 165 million sq.km area da
- Earth la 30% ithu than cover pannuthu
- Mariyana Trench kooda ithula than irukku da! 😎"""

        elif "pythagoras" in low:
            ans = """**2. The Pythagoras Theorem**

**Formula: a² + b² = c² da!**

- Right angle triangle ku than da ithu
- 'a' & 'b' - 2 chinna sides
- 'c' - Periya side (Hypotenuse) da
- Example: 3² + 4² = 5² -> 9+16=25 da! 🔥"""

        elif "sql" in low:
            ans = """**3. SQL Learning Path - Full Plan da!**

**Beginner (Week 1-2):**
- SELECT, WHERE, ORDER BY
- INSERT, UPDATE, DELETE

**Intermediate (Week 3-4):**
- JOIN (INNER, LEFT, RIGHT)
- GROUP BY, HAVING
- Functions: SUM, COUNT, AVG

**Advanced (Week 5-6):**
- Subqueries, Views
- Stored Procedures
- Indexing & Optimization

**Timeline: 6 Weeks da!**
**Suggestion: Daily 1 hour practice pannu, W3Schools la try pannu da! 💪"""

        else:
            ans = f"'{q}' - Sema question da! Ippo naan 3 main question ku mattum train aayirukken da - Ocean, Pythagoras, SQL pathu da kela da! 😎"

        st.markdown(ans)
        st.session_state.messages.append({"role":"assistant","content":ans})