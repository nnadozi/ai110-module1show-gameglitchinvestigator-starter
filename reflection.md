# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

When I ran the game for the first time, the UI looked pretty generic, and a little buggy (styling inconsistencies, clipping, low saturation, etc.). There are two conrete bugs that I noticed:
1 -  The final guess is outside of the range 1 to 100. It often goes below 0
2 -   The hints were not showing when the checknox was selected
3 -  The number of attempts left is not being updated properly
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  I used Co Pilot
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  One suggestion was a code snippet that fixed the attempt rendering logic (so the proper number of remaining attemps is shown). I verified this by writing some pytest, and also running the game in my browser
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  One suggestion I have to copilot was to improve the UI in the current application. However, it generated a button that was not visible, because the z-index was wrong. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
