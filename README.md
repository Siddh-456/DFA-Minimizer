# The Minimization Visualizer — DFA Edition

> An interactive, step-by-step visualization tool for understanding how Deterministic Finite Automata are reduced to their simplest form.

---

## 🔗 Live Demo

**[siddh-456.github.io/dfa-minimizer](https://siddh-456.github.io/dfa-minimizer)**

---

## What is This?

DFA Minimization is a fundamental concept in automata theory — the process of reducing a Deterministic Finite Automaton to its smallest equivalent form by identifying and merging indistinguishable states.

This tool makes that process **visual and intuitive**. Instead of working through dry partition tables on paper, you watch the algorithm execute live — pair by pair, step by step — with animated grids, highlighted states, and plain-English explanations at every stage.

Built as an educational tool for students studying Theory of Computation, Formal Languages, and Compiler Design.

---

## Features

- **Two input methods** — fill in a transition table manually, or draw your DFA on an interactive chalkboard canvas
- **Step-by-step algorithm visualization** across 6 annotated sections
- **Animated distinguishability grid** — cells flip as pairs get marked or identified as equivalent
- **Live node highlighting** on the original DFA graph as each pair is evaluated
- **Dependency arrows** during propagation showing exactly why a pair gets marked
- **Equivalence class display** showing which states merge together
- **Minimized DFA graph** rendered with spring animation after the algorithm completes
- **Downloadable output** — export the minimized DFA as JSON
- **Speed control** — adjust playback speed from slow (for learning) to fast (for review)

---

## How the Algorithm Works

The tool implements the **Table-Filling (Myhill-Nerode) Algorithm** in three phases:

### Phase 1 — Marking Base Pairs
Every pair of states (p, q) where exactly one is an accepting state is immediately marked as **distinguishable**. These pairs form the seed for the next phase.

### Phase 2 — Iterative Propagation
For every unmarked pair (p, q) and every input symbol `a`: if δ(p, a) and δ(q, a) lead to an already-marked pair, then (p, q) must also be marked. This repeats until no new pairs are marked — a fixed-point convergence.

### Phase 3 — Equivalence Classes
Any pair that remains unmarked after propagation means those two states are **indistinguishable** — they behave identically on all possible inputs. These equivalent states are grouped into equivalence classes and merged into single states in the minimized DFA.

---

## How to Use

### Option 1 — Table Mode
1. Set the **alphabet** (e.g. `a, b`) and **number of states**
2. Fill in the **transition table** — for each state and symbol, enter the destination state
3. Select the **start state** from the dropdown
4. Toggle the **accept states** using the pill buttons
5. Adjust the **speed slider** to your preference
6. Click **▶ WATCH IT MINIMIZE**

### Option 2 — Draw Mode
1. Click **🎨 Draw Mode** and configure your alphabet and state names in the setup dialog
2. Use the toolbar on the chalkboard canvas:
   - **➕ State** — click anywhere to place a state, drag to reposition
   - **✏️ Trans** — drag from one state to another to draw a transition
   - **🏁 Start** — click a state to mark it as the start state
   - **✅ Accept** — click a state to toggle it as an accept state
   - **🧹 Erase** — click a state or arrow to delete it
3. The **validation badge** (top-right of canvas) turns green when your DFA is valid
4. Click **▶ WATCH IT MINIMIZE**

### Watching the Visualization
Once minimization starts, the tool walks through 6 sections automatically:

| Section | What you see |
|---|---|
| 01 Input | Your DFA definition |
| 02 Original Graph | Your DFA rendered as a state diagram |
| 03 Base Pairs | Phase 1 — initial distinguishable pairs marked |
| 04 Propagation | Phase 2 — iterative marking with dependency highlights |
| 05 Equivalences | Phase 3 — equivalent pairs identified and grouped |
| 06 Minimized DFA | Final minimized automaton with transition table |

Use the **floating pause button** (bottom-right) to pause and resume at any time.

---

## Try the Built-in Example

Not sure where to start? Click **See Example** on the hero screen — it loads a classic 5-state DFA with alphabet `{a, b}` that minimizes down to 3 states, making it easy to see all three phases of the algorithm in action.

---

## Project Structure

```
dfa-minimizer/
│
└── index.html          # Entire application — self-contained single file
                        # Includes all HTML, CSS, and JavaScript
```

This is a pure front-end project. No build tools, no dependencies, no server required. Everything runs in the browser.

---

## Running Locally

Since there's no build step, just open the file:

```bash
# Clone the repository
git clone https://github.com/Siddh-456/dfa-minimizer.git

# Open in browser
cd dfa-minimizer
open index.html        # macOS
start index.html       # Windows
xdg-open index.html    # Linux
```

Or simply double-click `index.html` in your file explorer.

---

## Technical Details

| Concern | Approach |
|---|---|
| Algorithm | Table-Filling (Myhill-Nerode) with Union-Find for partition merging |
| Rendering | SVG-based state diagrams, pure CSS 3D flip animations for the grid |
| Draw Mode | Pointer Events API on an SVG canvas |
| Fonts | Playfair Display (headings), DM Sans (body), Caveat (chalkboard) via Google Fonts |
| Dependencies | None — zero external libraries |
| Browser support | All modern browsers (Chrome, Firefox, Safari, Edge) |

---

## Academic Context

This project was built as part of a course on **Theory of Computation / Formal Languages**. The minimization algorithm implemented is based on the Myhill-Nerode theorem, which states that the minimum DFA for a regular language is unique (up to isomorphism) and is characterized by the equivalence classes of the indistinguishability relation on strings.

**Key concept:** Two states p and q are *distinguishable* if there exists some string w such that exactly one of δ(p, w) and δ(q, w) is an accepting state. The algorithm finds all such distinguishable pairs, and everything left over is equivalent.

---

## Author

**Siddh** — [github.com/Siddh-456](https://github.com/Siddh-456)

---

## License

MIT License — free to use, modify, and distribute.
