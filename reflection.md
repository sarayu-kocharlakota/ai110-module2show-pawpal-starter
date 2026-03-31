# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

My UML design contains four classes. The four classes are: Owner, Pet, Task, and Scheduler. The Owner class' responsibilty is to represent the person using the app and holds the app user's name, email, and a list of their pets. The Pet class represents an animal and holds its species, breed, name, and age. The Task class responsibilty is to hold a care activity such as a walk, medication, feeding, and keeps tabs of the due date, priority, and if it has been completed. The Scheduler class is the main function of the app. It handles every single task and can order them in terms of priority and identify conflicts in scheduling. 

**b. Design changes**

My design changed a bit during implemenation. After referring to AI and asking it if there were any potential missing relationships, I realized that Scheduler had no direct conenction to Owner. Therefore, I included an owners list to the Scheduler class. This way, it can keep note of the owners that are in the system. I made this change as now, it would be much more simpler to look up tasks by owner in the future. 

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

One tradeoff my scheduler makes is that it only verifies for exact hour matches when analyzing conflicts. If there is one task at 8:00am and another at 8:30am, nothing gets flagged. However, if both tasks are at 8:00am, it gets flagged. This tradeoff is reasonable for this scenario as this is a straightforward and easy app for pet care. So, just checking hours works great. The most common timings for tasks for pets such as feedings or walks are scheduled on the hour. This covers frequently occuring cases which prevents the code from being overly complex. 

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
