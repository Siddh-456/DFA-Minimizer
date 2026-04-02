# The DFA Minimization Visualizer

An interactive, step-by-step visualization tool for understanding how Deterministic Finite Automata are reduced to their simplest form.

---

## Live Demo

**[siddh-456.github.io/dfa-minimizer](https://siddh-456.github.io/dfa-minimizer)**

---

## What is This?

DFA Minimization is a fundamental concept in automata theory, the process of reducing a Deterministic Finite Automaton to its smallest equivalent form by identifying and merging indistinguishable states.

This tool makes that process visual and intuitive. Instead of working through partition tables on paper, you watch the algorithm execute live pair by pair, step by step, with animated grids, highlighted states, and plain English explanations at every stage.

Built as an educational tool for students studying Theory of Computation, Formal Languages, and Compiler Design.

---

## Features

Two input methods: fill in a transition table manually, or draw your DFA on an interactive chalkboard canvas.

Step by step algorithm visualization across 6 annotated sections. An animated distinguishability grid where cells flip as pairs get marked or identified as equivalent. Live node highlighting on the original DFA graph as each pair is evaluated. Dependency highlights during propagation showing exactly why a pair gets marked. Equivalence class display showing which states will be merged. The minimized DFA graph is rendered with animation after the algorithm completes. The final result can be exported as a JSON file. A speed slider lets you adjust playback from slow to fast depending on whether you are learning or reviewing.

---

## How the Algorithm Works

The tool implements the Table-Filling (Myhill-Nerode) Algorithm in three phases.

**Phase 1: Marking Base Pairs**

Every pair of states (p, q) where exactly one is an accepting state is immediately marked as distinguishable. These pairs form the seed for the next phase.

**Phase 2: Iterative Propagation**

For every unmarked pair (p, q) and every input symbol a: if the transitions δ(p, a) and δ(q, a) lead to an already-marked pair, then (p, q) must also be marked. This repeats until no new pairs are marked, which is called fixed-point convergence.

**Phase 3: Equivalence Classes**

Any pair that remains unmarked after propagation means those two states are indistinguishable — they behave identically on all possible inputs. These equivalent states are grouped into equivalence classes and merged into single states in the minimized DFA.

---

## How to Use

**Table Mode**

Set the alphabet (for example a, b) and the number of states. Fill in the transition table by entering the destination state for each state and symbol combination. Select the start state from the dropdown and toggle the accept states using the pill buttons. Adjust the speed slider to your preference and click WATCH IT MINIMIZE.

**Draw Mode**

Click Draw Mode and configure your alphabet and state names in the setup dialog. Use the toolbar on the chalkboard canvas to place states, draw transitions, set the start state, and toggle accept states. The validation badge in the top-right corner of the canvas turns green when your DFA is complete and valid. Then click WATCH IT MINIMIZE.

**Watching the Visualization**

Once minimization starts, the tool walks through 6 sections automatically. Use the floating pause button at the bottom-right to pause and resume at any time.

| Section | What You See |
|---|---|
| 01 Input | Your DFA definition |
| 02 Original Graph | Your DFA rendered as a state diagram |
| 03 Base Pairs | Phase 1: initial distinguishable pairs marked |
| 04 Propagation | Phase 2: iterative marking with dependency highlights |
| 05 Equivalences | Phase 3: equivalent pairs identified and grouped |
| 06 Minimized DFA | Final minimized automaton with transition table |

---

## Running Locally

There is no build step. Clone the repository and open the file directly in your browser.

```bash
git clone https://github.com/Siddh-456/dfa-minimizer.git
cd dfa-minimizer
```

Then open index.html by double-clicking it in your file explorer, or by dragging it into a browser window.

---

## Project Structure

The entire application is a single self-contained file. No frameworks, no build tools, no external libraries are required. Everything runs directly in the browser.

```
dfa-minimizer/
    index.html
    README.md
```

---

## Technical Notes

The algorithm uses Union-Find for partition merging during the equivalence class step. State diagrams are rendered using SVG. The distinguishability grid uses CSS 3D transforms for the flip animation. The draw mode is built on the Pointer Events API directly on an SVG canvas. Fonts are loaded from Google Fonts Playfair Display for headings, DM Sans for body text, and Caveat for the chalkboard aesthetic.

---

## Academic Context

This project was built as part of a course on Theory of Computation and Formal Languages. The minimization algorithm is based on the Myhill Nerode theorem, which states that the minimum DFA for a regular language is unique up to isomorphism, characterized by the equivalence classes of the indistinguishability relation.

Two states p and q are distinguishable if there exists some string w such that exactly one of δ(p, w) and δ(q, w) is an accepting state. The algorithm finds all such distinguishable pairs, and everything remaining is equivalent.

---

## Author

Siddh — [github.com/Siddh-456](https://github.com/Siddh-456)
