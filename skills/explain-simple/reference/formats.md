# Teaching formats

Three formats, chosen by who reads the material. All three use the rules and the
five-part structure in SKILL.md.

## Contents
- Tutor primer card
- Live slide
- Learner reference (two pages per idea)
- Building slide decks and PDFs

## Tutor primer card

For the tutor, read before the session. Markdown. One card per concept.

```markdown
## N. Concept name

**One line.** The idea in one sentence.

**Plain.** 3 to 5 short sentences, or a short numbered list for a process. Bold the one
sentence that matters most.

**Metaphor.** One everyday scene.

| The picture | The concept |
|---|---|
| ... | ... |

Where this breaks: one or two sentences.

**Misconception.** "The wrong belief." The correction.

**Demo.** Under two minutes, on a screen, using tools the learner has. Say "run it
yourself first" when the result is not guaranteed.

**They will ask.** *"The likely pushback?"* The answer.
```

Target 250 to 400 words per card. A card over 450 words is doing two jobs: split it.

## Live slide

For the room, with the tutor talking over it. Exactly five things per slide, and no
more:

1. **Name**: two to four words.
2. **One line**: the idea in one sentence.
3. **Like**: the metaphor in one or two sentences.
4. **So what**: the consequence for the learner, one or two sentences. Use the single
   accent colour behind this block.
5. **Where it breaks**: in the footer.

If a slide needs a sixth thing, the concept is doing two jobs. Split the slide.

## Learner reference (two pages per idea)

For the learner, reading alone, months later. This is the format to share after a
session.

**Page A: what it is**
- The question as the title ("What is a token?")
- The short answer, in a highlighted block
- In plain words: three short paragraphs, technical terms in bold where they first
  appear
- Why it matters to you: two or three bullets

**Page B: remember it**
- Picture it: the metaphor title, the part-by-part table ("In the picture" and "In
  AI"), and "Where the picture stops working"
- The common mistake: "People think" and "In fact"
- Try it yourself, two minutes: three numbered steps the learner can do alone, with no
  code unless the learner codes
- Check yourself: one question, with "Answer on page N"

**Front and back matter**
- Title page, then "How to use this" with a contents list and page numbers
- A "Start here" page: the three or four facts that explain the whole set
- At the back: the whole set on one page, a glossary (plain definitions, alphabetical),
  and the answers to every check question

**Try-its the learner cannot do alone** (it needs code, an API key or a setup they do
not have yet) become predict-then-check exercises: they write down a prediction, and
the tutor runs the real thing in the session.

## Building slide decks and PDFs

- Keep content as data (a list of topics) and generate the pages, so a revision is a
  one-line edit.
- A4 landscape for print. Check the page count, then open and look at the densest pages:
  pages clip in print, so a correct count does not prove nothing was cut.
- A media query written for phone widths can also fire in print. Scope it to
  `@media screen`.
- Light background for decks shown in bright rooms.
