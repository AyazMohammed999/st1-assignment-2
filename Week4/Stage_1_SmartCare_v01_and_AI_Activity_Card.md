A2 Case Study Stage 1 student resource

# SmartCare scenario

SmartCare Community Clinic currently uses spreadsheets and paper records to manage patients and appointments. The client says: 'We need software to help manage patients, practitioners and appointments.' This is not yet a complete specification.

# Initial Engineering Brief

## 1. Problem summary

Write approximately 100 words.

**SmartCare is a small community clinic that's currently using spreadsheets, paper records, and manual processes to manage patients and appointments. This is causing a bunch of issues, like duplicate bookings, trouble finding patient records, appointment info that doesn't match up properly, and not being able to see when practitioners are actually free. There's also no reliable history of past appointments, and staff struggle to put together basic reports. Management wants a simple system to handle patients, practitioners, and appointments — nothing overly complicated like a full hospital system. As a junior software engineer, I'll be building this out step by step across Weeks 4 to 8, adding more to the prototype each week.**

## 2. Initial stakeholders

| Stakeholder                    | Possible need                                                    |
|--------------------------------|------------------------------------------------------------------|
| Patients                       | Wants to book an appointment easily and not have their info lost |
| Practitioners (Doctors/Nurses) | Needs fast access to patient records during appointments         |
| Reception staff                | Needs an easy way to manage bookings without double bookings     |
| Clinic Manger                  | Wants reports to see how the clinic is running overall           |

## 3. Initial features

| Feature                | Confirmed or provisional? | Why?                                                                      |
|------------------------|---------------------------|---------------------------------------------------------------------------|
| Patient Management     | Confirmed                 | Client directly said “manage patients”                                    |
| Appointment scheduling | Confirmed                 | Client said “manage appointments”                                         |
| Practitioner Records   | Provisional               | Client said “manage practitioner” but didn’t say what that actually means |
| Reports                | Provisional               | Not mentioned by the client, but likely needed if a manager wants report  |

## 4. Questions for the client

1\. Do you want to keep any of the old paper/spreadsheet records, or start fresh?

2\. Do different staff need different access levels?

3\. Should it work on mobile as well as desktop

4\. How many patients and staff will be using this?

5\. Is there a budget we should know about

## 5. What we do not yet know

1\. What kind of security/privacy requirements do they need for the patient data

2\. Whether the Clinic wants online bookings for the patients or just internal staff use

3\. Whether the software needs to integrate with any existing systems

# AI Activity Card - Ask, Check, Explain

## Before AI

What do I think the code does? What problems can I already identify?

I think the code stores appointment information (patient name, practitioner name, and time) and prints it out when display_appointments() is called. I wasn't fully sure what problems the code might have before looking closer.

## AI request

Act as a tutor. Explain this code and identify potential problems. Do not provide a complete replacement. Ask me questions that help me reason about the solution.

## Evaluate

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th>Suggestion</th>
<th>Useful</th>
<th>Unclear</th>
<th>Incorrect</th>
<th>Out of scope</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Add a check to prevent double booking the same time slot</td>
<td><ul>
<li></li>
</ul></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Use a database instead of a list to store bookings</td>
<td></td>
<td><ul>
<li></li>
</ul></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Add facial recognition for patient login</td>
<td></td>
<td></td>
<td></td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td>Validate that the appointment time is in valid format</td>
<td><ul>
<li></li>
</ul></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

## Decide

For each significant suggestion: Accept / Modify / Reject / Keep unverified.

| Suggestions                 | Decide          |
|-----------------------------|-----------------|
| Incomplete validation       | Modify          |
| Time as plain String        | Modify          |
| Duplicate Appoints          | Accept          |
| Practitioner double booking | Accept          |
| Global state                | Keep unverified |
| Error handling not caught   | Modify          |
| Scalability                 | Keep unverified |

## Verify

- Run the code

- Test normal input

- Test unusual input

- Compare with requirements

Ask tutor/peer

Check documentation

## Explain

Can I explain the final code without reading the AI response? What do I still need to understand?

**No, I couldn't explain the whole thing without looking back at what the AI said — I'm still a bit fuzzy on how the dictionary part actually stores and pulls out each appointment's info.**
