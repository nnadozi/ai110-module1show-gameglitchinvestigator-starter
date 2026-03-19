# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I first ran the game, the UI looked plain and had several visual glitches, like inconsistent styling and low color contrast. I noticed three main bugs: the final guess could go outside the allowed range (sometimes even below zero), the hints were not always showing when the checkbox was selected, and the number of attempts left was not updating correctly. These issues made the game confusing and hard to play.
---

## 2. How did you use AI as a teammate?

I used Copilot as my main AI tool for this project. One helpful suggestion was a code snippet that fixed the attempt rendering logic, which I verified by running pytest and testing the game in my browser. On the other hand, Copilot once suggested a UI improvement that added a button, but it was not visible due to a z-index issue, which I discovered by inspecting the page and checking the CSS.
---

## 3. Debugging and testing your fixes

I decided a bug was fixed when the game behaved as expected and all related pytest cases passed. For example, I wrote a test to check that the hint logic was correct, and verified it by running pytest and seeing it pass. The AI helped me design these tests by suggesting what to check and how to structure the assertions.

---

## 4. What did you learn about Streamlit and state?

Streamlit reruns the script from top to bottom on every user interaction, so you need to use session state to persist values like the secret number or score. Session state acts like a dictionary that keeps your variables safe between reruns. Without it, your game would reset every time you click a button.

---

## 5. Looking ahead: your developer habits

One habit I want to reuse is writing small, focused tests to confirm each bug is fixed. Next time, I would be more specific in my prompts to the AI to avoid UI issues. This project showed me that AI-generated code can be helpful, but it still needs careful review and testing to work well.
