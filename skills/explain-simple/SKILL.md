---
name: explain-simple
description: Explains technical concepts in plain language a school student in India could follow, using one everyday Indian metaphor mapped part by part in a table, naming where it breaks, and correcting the usual misconception. Also writes teaching material in three formats (tutor primer cards, five-part live slides, two-page learner references). Use when the user asks to explain something simply, in layman's terms or "like I'm five", asks for an analogy or metaphor, says they do not understand a concept, asks "what actually is X", or is preparing slides, a deck, tutor notes, a reference PDF or a session to teach or pitch a technical topic.
---

# Explain simple

A simple explanation replaces unfamiliar machinery with familiar machinery, and says
where the swap stops working. **The test: a school student in India could follow it
with nobody talking over it.**

## Rules for every explanation

1. **Short sentences, few words.** One idea per sentence. Draft, then cut a third.
2. **Name who does what.** "The app runs the search", never "your code runs it", "it
   gets processed" or "it is handled".
3. **Plain word first, term second.** Bring in the technical term, in bold or brackets,
   after the plain word that explains it.
4. **Indian everyday life by default.** Rupees and lakh, UPI and GPay, auto and cab, a
   hospital file, sambar, cricket, IRCTC. Use the learner's own world (their job, their
   city) when you know it.
5. **Adult register.** Simple words, never simple thinking.
6. **Say why it matters to them.** One line on what goes wrong in their world if they
   get this wrong.

## Output: five parts, in this order

**In one line**: the whole idea in one sentence a stranger could repeat correctly.
Write it last, put it first.

**The plain version**: 3 to 5 short sentences. For a process, a short numbered list of
who does what. End with a bold one-liner if the idea compresses well ("**The AI asks,
the app does.**").

**The metaphor**: one everyday scene, then a two-column table. Every moving part of the
concept gets its own row.

| The picture | The concept |
|---|---|
| ... | ... |

Then one sentence starting "Where this breaks:".

**The misconception**: the wrong belief, in quotes, then the correction.

**Check yourself**: one question with a right answer, answerable from the explanation.
Never "does that make sense?".

## Choosing the metaphor

The first four are requirements.

1. **Map the parts, not the vibe.** If the concept has four moving parts and the
   metaphor has one, pick another metaphor.
2. **Take it from the learner's world.** Unknown world: everyday Indian life that any
   adult has lived (a blood test, a bank, a railway booking, a kitchen, an exam).
3. **Name the break before they find it.** One sentence buys all the credibility.
4. **One metaphor per concept.** Two halves means two concepts.
5. **Reuse before inventing.** Check [reference/metaphor-bank.md](reference/metaphor-bank.md)
   so the same concept keeps the same picture across all material. If the project keeps
   its own bank, use and extend that one.
6. **Boring and concrete beats clever.** They should remember it next week.

## Failure modes

| Failure | What it looks like | Fix |
|---|---|---|
| Unnamed actor | "Your code runs it", "the request is processed" | Say who: the app, the lab, the bank |
| Jargon smuggling | Defining a term with two more terms they do not know | Ban the whole family of words |
| Foreign example | Dollars, miles, baseball, Thanksgiving for an Indian learner | Rupees, kilometres, cricket, Diwali |
| The vibe metaphor | "It's kind of like a brain" | Map parts in the table, or pick another |
| Wall of words | Correct, but a paragraph where a table or three steps would do | Cut a third, then turn lists into a table |
| Infinite caveats | Every sentence hedged | One honest "where this breaks", then commit |
| Condescension | "Imagine you're a little kid and..." | Simple language, adult register |
| Definition without mechanism | Says what it is, not how it works | They should be able to predict what happens next |

## Teaching material

When the output is for teaching (slides, tutor notes, a handout, a reference PDF), pick
the format by who reads it. Full templates and page limits:
[reference/formats.md](reference/formats.md).

| Format | Reader | Shape |
|---|---|---|
| **Tutor primer card** | The tutor, before the session | One line, Plain, Metaphor table and break, Misconception, Demo, "They will ask" |
| **Live slide** | The room, with the tutor talking | Exactly five things: name, one line, Like, So what, Where it breaks |
| **Learner reference** | The learner, kept for months | Two pages per idea: what it is, then picture, mistake, try-it, check question |

A terse live deck is not a learner reference. Learners reading alone need the two-page
format.

Before teaching material is finished:
- **Ask whether the tutor has run every demo and try-it themselves.** Take "I
  understand it" as a no.
- Facts that drift (app menu labels, free tiers, limits, prices) carry a source and the
  date checked.
- Rendered PDFs get opened, and the densest pages looked at.

## Worked example

**Request:** "What do you mean the app runs the tool? Explain tool calling simply."

> **In one line**
> The AI can only write. When it needs something done, it writes a request, the app
> does the work, and hands the result back for the AI to read.
>
> **The plain version**
> On its own, the AI cannot search Google or open Gmail. The app it lives inside offers
> it a list of jobs it can do, called **tools**.
> 1. The AI writes a short request: which tool, and what to look for. Then it waits.
> 2. The app does the actual work.
> 3. The app hands the result back as text, and the AI carries on.
>
> **The AI asks, the app does.**
>
> **The metaphor**
> A doctor ordering a blood test.
>
> | At the clinic | In AI |
> |---|---|
> | The doctor | The AI |
> | The list of tests the lab offers | The tools the app provides |
> | Writing "CBC, fasting sugar" on the slip | The AI writing a tool request |
> | The lab technician running the test | The app doing the work |
> | The report coming back | The result the AI reads |
>
> Where this breaks: a doctor is trained to order sensible tests. The AI can write a
> silly or harmful request, so the lab, which is the app, must check each slip first.
>
> **The misconception**
> "The AI goes on the internet." It only writes the slip. Telling the AI "please do not"
> is a request. The app refusing is a rule.
>
> **Check yourself**
> When Claude searches the web for you, who actually runs the search?
> (The app. The AI only writes what to search for.)

## Calibration

Length follows the concept, not a quota. A small idea gets a short answer with light
headings. For a whole curriculum, write one card per concept and keep them in one
format.
