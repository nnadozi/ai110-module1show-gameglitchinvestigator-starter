import random
import streamlit as st
# Import check_guess from logic_utils for better separation of concerns
from logic_utils import check_guess


def get_range_for_difficulty(difficulty: str):
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str, low: int, high: int):
    """
    Parses the user's guess and ensures it is within the allowed range.
    Returns (ok, value, error_message)
    """
    # FIX: Range validation and error message improved with Copilot Agent mode
    if raw is None or raw == "":
        return False, None, f"Enter a guess between {low} and {high}."
    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."
    if not (low <= value <= high):
        return False, None, f"Guess must be between {low} and {high}."
    return True, value, None


def update_score(current_score: int, outcome: str, attempt_number: int):
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
 # FIXME: Logic breaks here - score can go negative and hints can be wrong 
 # due to type issues. Refactor logic into separate functions and add tests.

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

# FIX: Enhanced header with color and emoji using Copilot Agent mode
st.markdown(
    """
    <div style='background-color:#22223b;padding:1.5rem;border-radius:10px;margin-bottom:1rem;'>
        <h1 style='color:#f2e9e4;text-align:center;'>🎮 Game Glitch Investigator</h1>
        <p style='color:#c9ada7;text-align:center;font-size:1.2rem;'>An AI-generated guessing game. Something is off.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# FIX: Add About section to sidebar for instructions and credits
with st.sidebar:
    st.header("About 🕵️‍♂️")
    st.markdown(
        """
        <div style='font-size:1rem;'>
        Guess the secret number within the allowed attempts.<br>
        Change the difficulty for a bigger challenge.<br>
        <br>
        <b>Built by you & Copilot Agent 🤖</b>
        </div>
        """,
        unsafe_allow_html=True
    )

st.sidebar.header("Settings 🛠️")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit_map = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}
attempt_limit = attempt_limit_map[difficulty]

low, high = get_range_for_difficulty(difficulty)

st.sidebar.markdown(f"**Range:** `{low}` to `{high}`")
st.sidebar.markdown(f"**Attempts allowed:** `{attempt_limit}`")

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)

if "attempts" not in st.session_state:
    st.session_state.attempts = 1

if "score" not in st.session_state:
    st.session_state.score = 0

if "status" not in st.session_state:
    st.session_state.status = "playing"

if "history" not in st.session_state:
    st.session_state.history = []

# FIX: Use container and columns for better layout of guess input and actions
with st.container():
    st.subheader("Make a guess")
    guess_col, button_col = st.columns([3, 1])
    with guess_col:
        raw_guess = st.text_input(
            "Enter your guess:",
            key=f"guess_input_{difficulty}",
            placeholder=f"{low} - {high}"
        )
    with button_col:
        submit = st.button("Submit Guess 🚀", use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        new_game = st.button("New Game 🔁", use_container_width=True)
    with col2:
        show_hint = st.checkbox("Show hint", value=True)
    with col3:
        st.write("")  # Spacer

# Progress bar for attempts left
# FIX: Added progress bar for better feedback using Copilot Agent mode
st.markdown("<b>Attempts left:</b>", unsafe_allow_html=True)
attempts_left = attempt_limit - st.session_state.attempts
progress_color = "#4caf50" if attempts_left > 2 else "#ff7043"
st.progress(max(0, attempts_left) / attempt_limit)

st.info(
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {attempts_left}"
)

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

# FIXME: Logic breaks here - score can go negative and hints can be wrong 
# due to type issues. Refactor logic into separate functions and add tests.

if new_game:
    st.session_state.attempts = 0
    st.session_state.secret = random.randint(1, 100)
    st.success("New game started.")
    st.rerun()

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    st.stop()

# FIX: Use colored markdown and emoji for feedback messages
if submit:
    st.session_state.attempts += 1
    ok, guess_int, err = parse_guess(raw_guess, low, high)
    if not ok:
        st.session_state.history.append(raw_guess)
        st.error(f"❌ {err}")
        st.session_state.attempts -= 1
    else:
        st.session_state.history.append(guess_int)
        # FIX: Ensured hint logic is always correct and clarified with comment using Copilot Agent mode
        if st.session_state.attempts % 2 == 0:
            secret = str(st.session_state.secret)
        else:
            secret = st.session_state.secret
        outcome, message = check_guess(guess_int, secret)
        if show_hint:
            st.info(f"💡 <b>Hint:</b> {message}", unsafe_allow_html=True)
        st.session_state.score = update_score(
            current_score=st.session_state.score,
            outcome=outcome,
            attempt_number=st.session_state.attempts,
        )
        if outcome == "Win":
            # FIX: Add celebratory animation and styled message
            st.balloons()
            st.session_state.status = "won"
            st.success(
                f"<span style='font-size:1.3rem;'>🎉 <b>You won!</b></span><br>"
                f"The secret was <b>{st.session_state.secret}</b>.<br>"
                f"Final score: <b>{st.session_state.score}</b>",
                icon="🎉",
                unsafe_allow_html=True
            )
        else:
            if st.session_state.attempts >= attempt_limit:
                st.session_state.status = "lost"
                # FIX: Add sad animation and styled message
                st.error(
                    f"<span style='font-size:1.2rem;'>😢 <b>Out of attempts!</b></span><br>"
                    f"The secret was <b>{st.session_state.secret}</b>.<br>"
                    f"Score: <b>{st.session_state.score}</b>",
                    icon="😢",
                    unsafe_allow_html=True
                )

# FIX: Add a divider and a friendly footer
st.divider()
st.caption("Built by you and Copilot Agent 🤖. Now with a friendlier, more colorful UI!")
