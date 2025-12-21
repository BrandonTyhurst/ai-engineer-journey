# Log

## 2025-12-15
### Shipped
- Day 1 Coding: Worked on Math Functions, Operators, and the data types Int and Float.

- Day 1 AI work: Worked on learning about LLMS and Prompt Engineering

### Learned
- Difference between int and float. 
- operator precedence
- checking types

- LLM's use natural language processing
- Tokens are used in GPT and they each have their own Token ID
- If asked to roll a dice, things aren't completely random. Tokens have a probability chance of following previous tokens and the highest probability can most likely be picked.
- Temperature controls randomness

### Next
- Learning Variables and Strings (str)
- Continuing through the Data Types

- Transformer Model
- Learning the training process

## 2025-12-16
### Shipped
- Day 2 Coding: Learned about Variables, Expressions vs Statements, Augmented Assignment Operator, Strings, String Concatenation, and Type Conversion
- Day 2 AI Work: Worked on looking inside LLMS and understanding parameters. Transformer Model and The Training Process were studied as well.

### Learned
- Learned the rules for naming Variables as well as showing how to indicate a constant.
- Learned the difference between Expressions and Statements. 
- Learned how to make code shorter and cleaner by using Augmented Assignment Operator. 
- Strings can be wrapped in single or double quotes.
- Long strings can be wrapped in 3 single quotes. 
- Strings and variables can be added to create outputs for them. 
- You are able to change the type of a data type by using Type Conversion.

- 300 Billion Tokens is around 45 TB of text data
- LLMs use Nueral Networks similar to our brain which use Nuerons.
- Learned about Parameters, Weights, and Bias's 
- The layers in between the input layer and output layer are known as hidden layers. Not many people know much about what happens in between. Being studied through Mechanistic Interpretability. 
- The Transformer Model allows LLMs to pay more attention.
- Long-Range Attention is able to take in more context and pay attention to words or tokens further away.
- GPT = Generative Pre-Trained Transformer
- Learned about the 2 steps to The Training Process (Pre-Training and Fine-Tuning)
- RLHF = Reinforced Learning from Human Feedback
- End of Pre-Training gives the Base Model
- End of Fine-Tuning gives the Assistant Model. 
- Learned what each step does.

### Next
- Escape Sequences, String Indexes, Immutability, and Built-In Functions + Methods
- Base Model vs. Assistant Model, The Reversal Curse, AGI

## 2025-12-18

### Learned

- What I learned (Python):

- Escape sequences:

- \t = tab

- \n = new line

- Formatted strings:

- Python 3 f-strings: print(f"Hi {name}") (expressions go inside {})

- Older style: "Hi {}".format(name)

- String indexing & slicing:

- Use square brackets:s[start:stop:step]

- Indexes start at 0.

- Slicing rule: [start:stop:step]

- Reverse a string with [::-1].

- Negative indexing starts from the end (e.g., s[-1] is last character).

- Strings are immutable (you can’t change characters in-place).

- Built-in functions vs methods:

- Functions: str(), int(), print(), len()

- len() returns the number of characters (counts spaces) and is not “0-based.”

- Methods belong to an object and use dot syntax, e.g. s.upper()

- Examples I learned: .format(), .upper(), .capitalize(), .find(), .replace(), .lower()

 

- What I learned (AI/LLMs):

- Base model vs assistant model:

- Base model: after pre-training; not tuned to reliably follow instructions or answer in a helpful way.

- Assistant model: fine-tuned (often instruction-tuned and/or RLHF) to answer questions more directly and in more detail.

- “Reversal curse” idea: models trained on relationships like A = B may not reliably infer the reverse B = A (you noted there’s research on this).


- AGI vs ASI: Artificial General Intelligence vs Artificial SuperIntelligence

- AGI: human-level general intelligence.

- ASI: beyond human-level intelligence.

- I learned a definition attributed to a Microsoft Research paper: AGI can involve reasoning, planning, learning from experience, and achieving goals across many environments.

- “Looking inside LLMs” / the stack:

- Models (e.g., GPT, Claude, LLaMA)

- Chat/UIs built on models (e.g., ChatGPT, Claude)

- Task-specific tools built on models (e.g., GitHub Copilot, Amazon CodeWhisperer)

- I learned: Copilot is built from a GPT-family base and trained/tuned for code tasks.

## 2025-12-19

### Learned

- What I learned (Python):

- Booleans (bool): True and False.

- What I learned (AI/LLMs):

- Standard prompt: a prompt that’s only a question or instruction (no extra structure).

- Prompt engineering framework (overview):
Setup (context/role)
Instruction (what to do)
Output (format/constraints)
Evaluation (how to judge success)

- I haven’t learned each piece deeply yet—this is next.

- System message:
The default/initial instruction provided by the model’s creator.

- Acts like a “north star” for behavior and priorities.


### Practiced/Built


- Practiced exercises:
Password checker
Type conversion exercise



- Practice AI: I used prompting to have ChatGPT code a Python Tic-Tac-Toe game with an AI opponent.

## 2025-12-20

### Learned

- What I learned (Python):

- Lists: a data structure (a way to store information).

- Lists use square brackets: [].

- Like string slicing, lists support indexing and slicing: my_list[start:stop:step].

- Key difference from strings: strings are immutable, but lists are mutable (you can change elements).

- Matrices (in code): multi-dimensional lists (lists inside lists).

- Example: matrix = [[1,2,3],[4,5,6],[7,8,9]]

- Accessing the 9: matrix[2][2].

- What I learned (AI/LLMs):

- Context in prompting:
General rule: more relevant context often → better results.
More context → more words → more tokens → more to analyze.
Too much context can hurt (noise, wasted tokens, pushes out important info).

- Context window:

Each model has a maximum token limit it can handle at once (context window = token limit).
Models don’t have long-term memory; they rely on the text in the current context window.
When the window limit is reached, older tokens may be dropped to make room for newer ones.

- Lost in the middle:

Models tend to retain the beginning and end of a prompt better than the middle (especially the beginning).
Similar to primacy and recency effects in psychology.

- My top 3 takeaways:

Put the most important info at the beginning (or end) of the context window.
Provide only the context that’s required.
Focus on how much context is required, not how much context is allowed.