# Code review workshop

In pairs, on each other's project repository. 20 minutes each way, then 15
minutes with an AI assistant.

## 1. Run it (5 min)

- Clone the repository of your partner. Does the README say how to run it?
- `uv sync`, `uv run pytest`, `uv run ruff check .`: what passes, what fails?

## 2. Read it (15 min)

Note each finding with the file and the line. Look for:

| Question                                              | Example of a finding                                   |
| ----------------------------------------------------- | ------------------------------------------------------ |
| Can a rule be bypassed?                               | `festival.performances.append(...)` works from outside |
| Does a name say what it holds?                        | `data`, `x`, `tmp`, `list2`                            |
| Is some code written twice?                           | the overlap test copied in two methods                 |
| Is an error swallowed?                                | `except Exception: pass`                               |
| Is a value written in the code instead of a constant? | `30` in the middle of a condition                      |
| Is a class doing everything?                          | 300 lines in `Festival`, including display and files   |
| Does a test check something?                          | a test without `assert`                                |
| Is there a docstring on each public class and method? |                                                        |

Give the three findings you consider most important, starting with the one
that can cause a bug. Say what is good too.

## 3. With an AI assistant (15 min)

Give one module of **your own** project to an assistant with this request:

> Review this Python module written by a student learning object-oriented
> programming. List at most five problems, most important first, each with
> the line and a one-sentence explanation. Do not rewrite the code.

Then compare with the review of your partner:

- what did both find?
- what did only the human find? only the AI?
- is one of the AI's findings wrong? Check each one before changing anything.

Write three lines in the README of your repository, section "Review": what
you changed after the review, and why.
