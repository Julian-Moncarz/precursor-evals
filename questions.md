400 word paper critique

- **Clear** - puts claims up front, backs them up with evidance, simply written etc
- **Correct** - critique is true
- **Non-obvious issues** - things they *didn't* acknowledge
- **Conceptual/methodological critique** - not "do more" but "this design choice is problematic because..."
- **Constructive** shows you'd be useful to work with

Core goal: cheaply predict model performance in a way that is scaleable as performance increases - any critique I make should keep this in mind: does it block the core goal? if not, not a critique.



Structure:
Critique {one sentence}

Evidence {one sentence}

Proposed fix {one sentence}

construct validity - far too little data in the original paper → hard to tell if these tests are actually testing the underlying capabilities (adaptability etc) or other things. 

Evidence: some stats things but mostly just hard to tell here. Suggested patches - think of possible confounders and try to control for them?

SWE bench issue - swe bench uses the mini-swe-bench agent whereas the proxy evals us the react agent - possible extensions: try running these evals over many different agent architectures, see how results change



Could be good to test this causally as well - ex train a model which crushes the precursor tasks and see if it's ability at SWE bench goes up (big weakness here is that the model may learn to succeed on the core tasks without getting better at the *skills* which the tasks are ment to measure). Possible solution: Use DSPy to find a prompt which optimizes model performance on the proxy evals, verify that it does not give them specific details about the evals but rather tells them to "adapt to changes in the env" or "never assume the env is in X state". Run an agent with that promo through SWE bench and see if the score goes up?





Other precursor things to test:

- Ability to recognize when not there is not enough info to complete a tasks / when more specification is needed
- 