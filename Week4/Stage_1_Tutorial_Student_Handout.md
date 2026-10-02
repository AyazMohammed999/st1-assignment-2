Stage 1 \| Introducing Software Technology Case Study with Python and Guided AI use

# Learning goals

- Explain why software engineering is broader than coding.

- Identify stakeholders in a simple software problem.

- Recognise missing requirements.

- Critically evaluate AI-generated feature suggestions.

- Explain why AI output should not automatically be treated as correct.

# Activity 1 - Think-Pair-Share (10 minutes)

If ChatGPT or Copilot can produce a 100-line Python application very quickly, what knowledge does a software engineer still need?

1\. Knowing what the Client/User actually needs, not just writing code.

2\. Being able to check if the AI code is correct, and if there are any errors and if there are any and fixing it.

3\. Understanding how the code fits into a bigger system.

# Activity 2 - Is This Software Engineering? (10 minutes)

Scenario A: A student writes a 50-line Python calculator.  
Scenario B: A team develops a payroll system used by 5,000 employees.  
Scenario C: An AI assistant generates a simple appointment application from one prompt.

| Scenario | Programming? | Software engineering? | Why?                                                                                                                                                                             |
|----------|--------------|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| A        | Yes          | No                    | A Student writing a 50-line calculator involves basic coding, but no requirements gathering, stakeholders’ management. It’s just a quick script one person wrote for themselves. |
| B        | Yes          | Yes                   | A payroll system used by 5,000 people needs proper planning, testing, and teamwork – not just code.                                                                              |
| C        | Yes          | No                    | The AI just spat out code from one prompt, no one thought about what was actually needed                                                                                         |

# Activity 3 - SmartCare Problem Analysis (20 minutes)

Client statement: SmartCare Community Clinic currently uses spreadsheets and paper records to manage patients and appointments. The clinic wants new software to improve these processes.

## Task 1 - Identify stakeholders

| Stakeholder     | What do they need?                                      |
|-----------------|---------------------------------------------------------|
| Patients        | Easy ways to book appointments and access their records |
| Doctors/Nurses  | Quick access to patient info during visits              |
| Reception staff | Simple ways to manage bookings and check people records |
| Clinic Manager  | Reports on how the clinic is running                    |

## Task 2 - Identify current problems

1\. No easy way to see when the practitioners are actually available

2\. Appointment info isn’t always accurate or up to date

3\. patient records are hard to track down when needed

## Task 3 - Ask client questions

1\. What happens to old paper records – do they need to be digitalized too?

2\. Is there a budget or timeline we should know about?

3\. How many patients do you see in a day?

4\. Do staff need different levels of access to records?

5\. Do you need the system to work offline?

# Activity 4 - Critique an AI Response (15 minutes)

An AI assistant suggests: appointment management; facial-recognition login; AI diagnosis recommendations; patient search; online payment; practitioner schedule view; insurance processing; automatic treatment-plan generation.

| Suggestion                   | Client evidence? | In scope? | Decision                                  |
|------------------------------|------------------|-----------|-------------------------------------------|
| Appointment management       | Yes              | Yes       | Should Keep                               |
| Facial recognition login     | No               | No        | Wasn’t asked, and would be a privacy risk |
| AI diagnosis recommendations | No               | No        | Drop – too risky                          |
| Patient search               | Yes              | Yes       | Keep                                      |
| Online payment               | No               | Maybe     | Ask client if needed                      |
| Practitioner schedule view   | Yes              | Yes       | Keep                                      |
| Insurance processing         | No               | No        | Drop – not mentioned by the client        |
| Treatment-plan generation    | No               | No        | Drop – Too risky, needs a doctor not AI   |

# Exit question

Write one activity that a software engineer must perform and that cannot safely be delegated entirely to AI.

**“A software engineer must decide what the client actually needs, since Ai can’t be trusted to know that on its own”**
