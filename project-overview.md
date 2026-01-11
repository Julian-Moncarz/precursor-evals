Proxies: Planning Stage 2 (AISI CF)

In stage 1 of the project, we showed that performance on certain “proxy” evals can be predictive of performance on longer-running and more realistic tasks. [Our workshop paper](https://openreview.net/forum?id=bfX0oa2XDr) focuses on 7 proxy evals, 5 models, and 1 “real-world” eval (SWE-bench).

In stage 2, we now focus on two hypothesised “precursor abilities” (ability to handle non-stationarity and stochasticity), and build 8 proxy evals for each precursor, aiming for evals which – as a cohort – have construct validity. This should increase the precision of our predictive [GLM](https://en.wikipedia.org/wiki/Generalized_linear_model). We also aim to predict performance on consequential evals such as Cybench.

[**Summary of planned proxy evals**	**2**](https://docs.google.com/document/d/1ALFPmaS5ji7kBRIqA2fnXS1ovYaZYLwhjGatylx1F1I/edit?tab=t.0#heading=h.za1ra7p5kfxh)

[Precursor 1 of 2: Non-stationarity	2](https://docs.google.com/document/d/1ALFPmaS5ji7kBRIqA2fnXS1ovYaZYLwhjGatylx1F1I/edit?tab=t.0#heading=h.u1i5ocdp0v4y)

[Proxy eval 1 of 8: A-not-B	2](https://docs.google.com/document/d/1ALFPmaS5ji7kBRIqA2fnXS1ovYaZYLwhjGatylx1F1I/edit?tab=t.0#heading=h.z3sopeaghi3c)

[Proxy eval 2 of 8: Changing constraints of brackets-matching task	2](https://docs.google.com/document/d/1ALFPmaS5ji7kBRIqA2fnXS1ovYaZYLwhjGatylx1F1I/edit?tab=t.0#heading=h.2jgvxfpu4f9c)

[Proxy eval 3 of 8: Nested Directories task with changing target	3](https://docs.google.com/document/d/1ALFPmaS5ji7kBRIqA2fnXS1ovYaZYLwhjGatylx1F1I/edit?tab=t.0#heading=h.2kn1x4dyl1to)

[Proxy eval 4 of 8: Key:value addition with dict update	3](https://docs.google.com/document/d/1ALFPmaS5ji7kBRIqA2fnXS1ovYaZYLwhjGatylx1F1I/edit?tab=t.0#heading=h.2nskggmskxr5)

[Proxy eval 5 of 8: Moving Bin	4](https://docs.google.com/document/d/1ALFPmaS5ji7kBRIqA2fnXS1ovYaZYLwhjGatylx1F1I/edit?tab=t.0#heading=h.xdk72y996137)

[Proxy eval 6 of 8: Tower of Hanoi target peg change	4](https://docs.google.com/document/d/1ALFPmaS5ji7kBRIqA2fnXS1ovYaZYLwhjGatylx1F1I/edit?tab=t.0#heading=h.po3ydfqzwspm)

[Proxy eval 7 of 8: Rotating Maze	4](https://docs.google.com/document/d/1ALFPmaS5ji7kBRIqA2fnXS1ovYaZYLwhjGatylx1F1I/edit?tab=t.0#heading=h.hbpj80xhwr)

[Proxy eval 8 of 8: Website Bios with changing destination directory	5](https://docs.google.com/document/d/1ALFPmaS5ji7kBRIqA2fnXS1ovYaZYLwhjGatylx1F1I/edit?tab=t.0#heading=h.qft9m2nk3ir2)

[Stretch: Proxy eval A: Lights-out with tool-change	5](https://docs.google.com/document/d/1ALFPmaS5ji7kBRIqA2fnXS1ovYaZYLwhjGatylx1F1I/edit?tab=t.0#heading=h.33dog4haspv)

[Stretch: Proxy eval B: Multi-armed bandit with payoff step-change	5](https://docs.google.com/document/d/1ALFPmaS5ji7kBRIqA2fnXS1ovYaZYLwhjGatylx1F1I/edit?tab=t.0#heading=h.p0ogfecvljql)

[Precursor 2 of 2: Stochasticity	7](https://docs.google.com/document/d/1ALFPmaS5ji7kBRIqA2fnXS1ovYaZYLwhjGatylx1F1I/edit?tab=t.0#heading=h.qqd55x27lbxi)

[Proxy eval 1 of 8: Noisy Tower of Hanoi	7](https://docs.google.com/document/d/1ALFPmaS5ji7kBRIqA2fnXS1ovYaZYLwhjGatylx1F1I/edit?tab=t.0#heading=h.e52hdf2xqnt0)

[Proxy eval 2 of 8: Sokoban with noisy no-op/undo	7](https://docs.google.com/document/d/1ALFPmaS5ji7kBRIqA2fnXS1ovYaZYLwhjGatylx1F1I/edit?tab=t.0#heading=h.vka6hle6greo)

[Proxy eval 3 of 8: Stochastic A-or-B	7](https://docs.google.com/document/d/1ALFPmaS5ji7kBRIqA2fnXS1ovYaZYLwhjGatylx1F1I/edit?tab=t.0#heading=h.3lu327jkjq7x)

[Proxy eval 4 of 8: Nested Directories with noisy reversible moves	8](https://docs.google.com/document/d/1ALFPmaS5ji7kBRIqA2fnXS1ovYaZYLwhjGatylx1F1I/edit?tab=t.0#heading=h.6vq4nvqxvxqc)

[Proxy eval 5 of 8: “8/15” sliding-tile puzzle with random valid moves	8](https://docs.google.com/document/d/1ALFPmaS5ji7kBRIqA2fnXS1ovYaZYLwhjGatylx1F1I/edit?tab=t.0#heading=h.re8a5bynasp8)

[Proxy eval 6 of 8: Noisy Website Bios (valid moves)	8](https://docs.google.com/document/d/1ALFPmaS5ji7kBRIqA2fnXS1ovYaZYLwhjGatylx1F1I/edit?tab=t.0#heading=h.k760mavq2t8e)

[Proxy eval 7 of 8: Code Factorisation no-op/undo	9](https://docs.google.com/document/d/1ALFPmaS5ji7kBRIqA2fnXS1ovYaZYLwhjGatylx1F1I/edit?tab=t.0#heading=h.78j47ohv1oc)

[Proxy eval 8 of 8: Multi-armed bandit	9](https://docs.google.com/document/d/1ALFPmaS5ji7kBRIqA2fnXS1ovYaZYLwhjGatylx1F1I/edit?tab=t.0#heading=h.nko5tekmx8dn)

[Stretch: Proxy eval A: 

[**Stretch goals / side-projects**	**10**](https://docs.google.com/document/d/1ALFPmaS5ji7kBRIqA2fnXS1ovYaZYLwhjGatylx1F1I/edit?tab=t.0#heading=h.i0kn7vnyx7ga)

[Comparison to prediction based on existing published evals	10](https://docs.google.com/document/d/1ALFPmaS5ji7kBRIqA2fnXS1ovYaZYLwhjGatylx1F1I/edit?tab=t.0#heading=h.18tic461x103)

[Performance curves: Step-difficulty vs number-of-steps	10](https://docs.google.com/document/d/1ALFPmaS5ji7kBRIqA2fnXS1ovYaZYLwhjGatylx1F1I/edit?tab=t.0#heading=h.3kyxt575qpa)

[Wrappers for existing sources of RL-agent games	10](https://docs.google.com/document/d/1ALFPmaS5ji7kBRIqA2fnXS1ovYaZYLwhjGatylx1F1I/edit?tab=t.0#heading=h.skwo0d65x0si)

[Cheating metrics	10](https://docs.google.com/document/d/1ALFPmaS5ji7kBRIqA2fnXS1ovYaZYLwhjGatylx1F1I/edit?tab=t.0#heading=h.s3ouk4lap3bb)

[Self-correction / self-conditioning	11](https://docs.google.com/document/d/1ALFPmaS5ji7kBRIqA2fnXS1ovYaZYLwhjGatylx1F1I/edit?tab=t.0#heading=h.g7bssmeybd44)

[Streamlining of code, for 1-click eval	11](https://docs.google.com/document/d/1ALFPmaS5ji7kBRIqA2fnXS1ovYaZYLwhjGatylx1F1I/edit?tab=t.0#heading=h.j4b8s7xg3p5y)

[Comparison to one-shot solutions	11](https://docs.google.com/document/d/1ALFPmaS5ji7kBRIqA2fnXS1ovYaZYLwhjGatylx1F1I/edit?tab=t.0#heading=h.3t5t87l0t720)

[Other hypothesised precursor capabilities	11](https://docs.google.com/document/d/1ALFPmaS5ji7kBRIqA2fnXS1ovYaZYLwhjGatylx1F1I/edit?tab=t.0#heading=h.1z4rgeerbczf)

## Table of Eval Development 

| **Eval**                                           | **Subdomain** | **Who?** | **Milestone** | **Status**                                                   | **Todo for MS-done**              |
| -------------------------------------------------- | ------------- | -------- | ------------- | ------------------------------------------------------------ | --------------------------------- |
| A-not-B                                            | NST           | S        | 1             | Core complete, 5 models, 1 variantFinal Graph versionAUC is decent metric | done                              |
| NToH                                               | STC           | J        | 2             | Core complete, 5 models, 1 variant                           |                                   |
| ToH Target Peg                                     | NST           | J        | 2             | Core complete, signpost/explanation variants, different “trigger” variants | TestsAll models                   |
| Key Values (KV)                                    | NST           | L        | 2             | Core complete, 1 variant                                     | Needs refactoring + documentation |
| Coin-flip (A-or-B)                                 | STC           | S        | 2             | Core complete, 5 models, 1 variantFinal Graph version        | Check AUC                         |
| MAB                                                | STC           | S        | 2             | Core complete, 5 models, 1 variant                           | Check AUC                         |
| Moving Bin (MB)                                    | NST           | L        | 3             |                                                              |                                   |
| MAB w discontinuity / drift                        | STC / NST     | S        | 3             |                                                              |                                   |
| (Additional NST task)                              | NST           | S        | 3             |                                                              |                                   |
| Rotating Maze                                      | NST           | J        | 3             |                                                              |                                   |
| Wisconsin Card Sorting Test (WCST)                 | NST           | L        | 3             |                                                              |                                   |
| Sokoban with noisy no-op/undo                      | STC           | J        | 4             |                                                              |                                   |
| “8/15” sliding-tile puzzle with random valid moves | STC           | J        | 4             |                                                              |                                   |
| Additional STC task                                | STC           | S        | 4             |                                                              |                                   |
| Additional STC task                                | STC           | L        | 4             |                                                              |                                   |
| (*) WB with changing target                        | NST           | L        | 4             |                                                              |                                   |
| (*) ND with changing target                        | NST           | D        | 4             |                                                              |                                   |
| (*) Brackets-matching with changing constraints    | NST           | D        | 4             |                                                              |                                   |

# 

# Summary of planned proxy evals

## Precursor 1 of 2: Non-stationarity

We define non-stationarity as a change in the environment (possibly continuous) that is deterministically defined. This change may or may not be signposted: the agent may be told at the beginning of the task to expect the change.

By default, all non-stationarity proxies have the following variants:

**Default non-stationarity variants**:

- Signposted / unsignposted: agent told about the expected change in the initial prompt e.g. that object will be hidden in A 10 times before being hidden in B.

### Proxy eval 1 of 8: A-not-B

**Status**: complete

**Description**: The A-not-B test is inspired by animal/developmental cognition, where it tests for an incomplete or absent schema of object permanence. In it, an agent (usually infant or animal) repeatedly sees an object be hidden in location A, and subsequently each time searches location A. After many repetitions, the agent watches as the object is hidden in location B. An A-not-B error occurs when the agent reaches for the incorrect location A on reverse trials (when the agent has seen the object being hidden in location B). In the context of LLM-agents, the A-not-B test sets up conditions which are very conducive to hallucination and repetitive lock-in, while being simple, easy to score and arbitrarily scalable.

**Precursors being targeted**: Responsivity (discontinuous change in system behaviour)

**Variants**: Signposted and non-signposted, relabelled (e.g. B-not-A, rainy or sunny -> whether to take umbrella)

### Proxy eval 2 of 8: Changing constraints of brackets-matching task

**Status**: Not begun

**Description**: A sequence of characters can include opening and closing brackets of various types such as round ‘(‘, square ‘[‘, and curly ‘{‘. Such a sequence is called ‘balanced’ when each open-bracket is followed by a matching close-bracket, for example ‘()’ and is balanced but ‘((‘, ‘)(‘, and ‘(}’ are not.

In the basic version of the task, an agent is given the start of a sequence, e.g. “((()())(({(...“ and told to complete the sequence using as few characters as possible. Constraints can be added, such that the sequence must contain e.g. 3 curly brackets to be valid. This problem could be completed in one step, however the tools available to the agent could be restricted so that each character addition requires a separate move. While stack-based algorithms to solve this are well-known, this proxy eval investigates long-horizon behaviour rather than solution recitation.

In a non-stationary version of the task, the constraints may change part-way through the task (e.g. after 5 moves, the constraint changes from “at least 3 curly brackets” to “at least 2 square brackets”).

**Precursors being targeted**: Discontinuous rule-change (task success constraints)

**Variants**: Signposted and non-signposted, varying moment of step-change.

### Proxy eval 3 of 8: Nested Directories task with changing target

**Status**: Basic task complete, changing target not yet implemented

**Description**: The agent must create a directory structure specified in the prompt. We generate an unbalanced target tree by starting at the root and, under a maximum-depth limit, iteratively attach a new child to a randomly chosen existing node until the tree has n nodes, producing uneven branching and path lengths. The agent sees only the set of leaf paths (e.g., /a/b/c, /a/d) and must recreate the minimal directory structure that makes them valid.

In a non-stationary version of the task, the target directory structure changes part-way through the task (e.g. after 5 moves).

**Precursors being targeted**: Discontinuous target-change

**Variants**: Signposted and non-signposted, path-at-a-time (no subtask ordering constraint since missing parent directories can be automatically created) and directory-at-a-time (where parent directories must be created before their children can be), varying moment of step-change.

### Proxy eval 4 of 8: Key:value addition with dict update

**Status**: Not begun

**Description**: Based on Sinha et al. ([link 2](https://x.com/arvindh__a/status/1966526373922734537/photo/1)), a state-tracking exercise. Given a dict of the form {Apple: 82, Break: 32, Clutch: -12, …}, the agent is asked to repeatedly add some number of elements (e.g. first turn “add Apple & Clutch” -> 70, second turn “add Break and Clutch” -> 90). How many turns does the agent take before first answering incorrectly?

In a non-stationary version of the task, the dict is altered part-way through the task (e.g. after 5 moves).

**Precursors being targeted**: Discontinuous state-change

**Variants**: Signposted and non-signposted, varying moment of step-change.

### Proxy eval 5 of 8: Moving Bin

**Status**: Not begun

**Description**: A bin containing balls moves with a constant trajectory. The agent is tasked with collecting balls, and must provide coordinates of where it wants to “reach” to fetch items from the bin.

**Precursors being targeted**: Continuous state change

**Variants**: Signposted (bin trajectory given) and non-signposted (agent must query for bin trajectory). Different bin speeds and trajectories (linear, oscillating, 1D/2D)

### Proxy eval 6 of 8: Tower of Hanoi target peg change

**Status**: basic task complete, changing target not completed

**Description**: Tower of Hanoi consists of three rods (A, B, C) where rod A is populated with n disks stacked in increasing size, i.e., the largest disk is at the bottom of the rod and the smallest disk is at the top of the stack. The agent must move all disks from rod A to rod C without ever placing a larger disk on top of a smaller one.

In a non-stationary version of the task, the target rod is changed part-way through the task (e.g. from C to B).

**Precursors being targeted**: Discontinuous target change

**Variants**: Signposted and non-signposted (though unclear what the correct agent strategy is in the signposted case: should it just move everything to B pre-emptively? Perhaps a 4-rod version would be one way of avoiding this. Or perhaps the signposting is limited to the agent being told “the rules will change part-way through the game” without being told what the change will be.) Varying moment of step-change. Relabelling (e.g. C->A instead of A->C).

### Proxy eval 7 of 8: Rotating Maze

**Status**: Not begun

**Description**: Agent navigates a simple ASCII maze, one step at a time. At various points, the “view” of the maze is altered / rotated / flipped, such that the progress through the maze is unaffected.

**Precursors being targeted**: Continuous “view” change (state is preserved)

**Variants**: Frequency and type of view alteration, signposted/non-signposted, maze difficulty

### Proxy eval 8 of 8: Website Bios with changing destination directory

**Status**: Basic eval complete, non-stationary extension not begun

**Description**: Website Bios is an evaluation where an agent is tasked to create an HTML webpage for an organisational chart (diagram that maps departments, roles, and reporting lines) of a fictitious dynamically-generated organisation, using a set of website generation tools that we provide to avoid formatting errors. The information we provide the agent includes a JSON file describing the structure of the organisation and a directory of text files containing biographies of employees within the organisation. This evaluation serves to investigate how an agent deals with long-range dependencies and organising information in a hierarchical structure. We constrain the model such that it cannot produce a code solution, but has to rely on its context window, and understanding of dependent relationships.

In a non-stationary version of the task, the target directory of the website is changed part-way through the task (e.g. from `/home/agent/working` to `/home/agent/www/deployment`).

**Precursors being targeted**: Minor detail of target is altered

**Variants**: Frequency of target alteration, signposted/non-signposted

### Stretch: Proxy eval A: Lights-out with tool-change

**Status**: Not begun

**Description**: [Lights Out](https://en.wikipedia.org/wiki/Lights_Out_(game)) is a grid puzzle where cells are arranged in a (typically) 5x5 grid, and cells can be “off” or “on”. When the game starts, a random number or a stored pattern of these lights is switched on. Pressing any of the lights will toggle it and the adjacent lights. The goal of the puzzle is to switch all the lights off, preferably with as few button presses as possible.

In a non-stationary version of the task, the rules which determine cell adjacency could be changed (e.g. from not-diagonals “+” to only-diagonals “X”). However, since we’re not sure that Lights Out can be solved for an arbitrary game-state for only-diagonals, it’s unclear that this game is always solvable.

**Precursors being targeted**: Discontinuous rule change (tool)

**Variants**: Varying switching rules, varying opening patterns, varying moment of step-change

### Stretch: Proxy eval B: Multi-armed bandit with payoff step-change

**Status**: Not begun

**Description**: See the stochastic MAB eval for an introduction. An eval which is both stochastic and non-stationary could be constructed, where the payoffs (mean and variance) of each lever change part-way through the task.

**Precursors being targeted**: Discontinuous state change

**Variants**: Frequency of state change

## 

## Precursor 2 of 2: Stochasticity

Proxies which target stochasticity have a constant set of actions available to the agent, though actions have a constant probability of resulting in one of a set of actions. For example, in the Noisy Tower of Hanoi (0.1), levers unpredictably malfunction 10% of the time; in the Stochastic A-not-B (0.15), the object is hidden in cup ‘A’ 15% of the time, with no predictable pattern.

By default, all stochasticity proxies have the following variants:

**Default stochasticity variants**:

- Signposted / unsignposted: agent told about stochasticity in the initial prompt e.g. that levers malfunction with given probability
- Explained / unexplained: agent receives an explanation each time the stochastic behaviour occurs (e.g. “there was a “lever malfunction”) vs game state is different to expectation for no clear reason
- Varying noise level (10%, 20%, …)

### Proxy eval 1 of 8: Noisy Tower of Hanoi

**Status**: complete (not all variants)

**Description**: The agent plays Tower of Hanoi (move disks of varying size from rod A to rod C without placing a larger disk on a smaller disk) by making calls to a move_disk(src, dst) tool, but the tool replaces the requested move with a random valid move with some probability (noise level). 

**Precursors being targeted**: Responsivity (valid random move)

**Variants**: default stochasticity variants, relabelling (e.g. C->A instead of A->C)

### Proxy eval 2 of 8: Sokoban with noisy no-op/undo

**Status**: complete (not all variants)

**Description**: The agent moves around a grid to push boxes onto target spots. With some probability (noise level) we don’t make the move requested by the agent (no-op) or we undo a certain number of previous moves (undo) by taking the state of the game back.

**Precursors being targeted**: Resilience to no-op/undo

**Variants**: default stochasticity variants

### Proxy eval 3 of 8: Stochastic A-or-B

**Status**: complete (not all variants)

**Description**: Like the non-stationary A-not-B eval, an object is hidden in either cup A or cup B, and the agent must reach for the correct cup. Unlike the non-stationary A-not-B (where the object is placed in A for n repetitions, before being placed in B) in A-or-B there is a constant probability that the object is placed in either A or B.

**Precursors being targeted**: Responsivity (continuous)

**Variants**: default stochasticity variants, varying A:B ratio (instead of noise level), relabelling (e.g. B-or-A, rainy or sunny -> whether to take umbrella)

### Proxy eval 4 of 8: Nested Directories with noisy reversible moves

**Status**: Basic task complete, reversible moves not implemented

**Description**: Nested Directories task as described above, but where tool calls are replaced with random reversible tool calls, meaning they don’t permanently alter the solvability of the task.

**Precursors being targeted**: Resilience to noisy tools which make valid moves

**Variants**: default stochasticity variants

### Proxy eval 5 of 8: “8/15” sliding-tile puzzle with random valid moves

**Status**: complete (not all variants)

**Description**: A sliding-tile board with one blank where the task is to move tiles into the blank to reach a goal permutation. We introduce noise by making a random valid move instead of the requested move.

**Precursors being targeted**: Resilience to noisy tools which make valid moves

**Variants**: default stochasticity variants, no-op/undo

### Proxy eval 6 of 8: Noisy Website Bios (valid moves)

**Status**: Basic task complete, reversible moves not implemented

**Description**: Website Bios is an evaluation where an agent is tasked to create an HTML webpage for an organisational chart (diagram that maps departments, roles, and reporting lines) of a fictitious dynamically-generated organisation, using a set of website generation tools that we provide to avoid formatting errors. We constrain the model such that it cannot produce a code solution, but has to rely on its context window, and understanding of dependent relationships. We add stochasticity by replacing the requested move with one or more randomly generated valid moves with some probability (noise level).

**Precursors being targeted**: Resilience to noisy tools which make valid moves

**Variants**: default stochasticity variants

### Proxy eval 7 of 8: Code Factorisation no-op/undo

**Status**: Basic task 70% complete, reversible moves not implemented

**Description**: The agent is tasked with refactoring a procedurally generated codebase with many duplicated functions and files. With some probability, the requested command is not executed, or one or more previous commands are undone, essentially taking the state of the codebase back.

**Precursors being targeted**: Resilience to no-op/undo

**Variants**: default stochasticity variants

### Proxy eval 8 of 8: Multi-armed bandit

**Status**: complete (not all variants)

**Description**: “In probability theory and machine learning, the [multi-armed bandit problem](https://en.wikipedia.org/wiki/Multi-armed_bandit) [...] is named from imagining a gambler at a row of slot machines (sometimes known as "one-armed bandits"), who has to decide which machines to play, how many times to play each machine and in which order to play them, and whether to continue with the current machine or try a different machine.”

While algorithmic optimal solutions to best-arm identification are well-known, this eval would be multi-step, testing the agent’s ability to follow-through on the execution of its favoured strategy.

**Precursors being targeted**: Sustained optimal play in a stochastic environment

**Variants**: Vary number and payoff of levers, 

### Stretch: Proxy eval A: <template>

Status: Not begun

Description: 

Precursors being targeted: 

Variants

# Stretch goals / side-projects

### Comparison to prediction based on existing published evals

We hope that our proxies target genuine “precursor” capabilities (such as “resilience” and “adaptability”) which underlie more general performance. We therefore build a general linear model (GLM) which predicts general performance (e.g. on SWE-bench or Cybench) from our proxy evals which target precursors.

To test the value of our newly-developed proxy evals, we should compare to a baseline of a GLM whose input comprises existing standard evals such as GPQA.

### Performance curves: Step-difficulty vs number-of-steps

There is a maximum difficulty of atomic step which an agent can complete, and a maximum number of easy steps. Presumably, there is a curve where agents can do more steps if those steps are easier.

For example, suppose an agent has a success rate of 50% at a task comprising two sequential Sudoku puzzles (n=2) each of difficulty-level 5 (d=5). What success rate do we expect for e.g. (n=4, d=5) or (n=2, d=3) ?

For quantitative assessment of difficulty, we could set tasks such as:

- computational graph execution: provide a DAG where nodes are mathematical operations and edges carry values - find the missing values. Depth & width are controllable
- Multi-step equation solving: nested equations / simultaneous equations
- Executing algorithms step-by-step (e.g. sorting, graph traversal)

### Wrappers for existing sources of RL-agent games

The [MiniGrid](https://minigrid.farama.org/) and BabyAI libraries contain simple and easily configurable 2D grid-world environments with goal-oriented tasks, to conduct Reinforcement Learning research. The tasks involve solving different maze maps and interacting with different objects such as doors, keys, or boxes. RL agents have been well-studied in these environments, yet the performance of general-purpose language-model-based agents on this kind of RL environment has not (to our knowledge) been studied.

### Cheating metrics

We sometimes see agents find ways to [reward-hack](https://lilianweng.github.io/posts/2024-11-28-reward-hacking/), generally by finding ways to automate steps which we intended to be completed one-at-a-time. By plotting a function of agent score, number-of-steps-taken and task difficulty (e.g. for nested-directory task: F-score * (n_dirs / n_moves_taken) ), we can detect and investigate outliers.

### Self-correction / self-conditioning

Based on Sinha et al. ([link](https://x.com/arvindh__a/status/1966526369463951424/photo/1)): how resilient are models to seeing themselves make errors (in their execution history)

Pros:

- Engages with literature
- Seems like a likely precursor

Cons:

- Need to work out how to stop/restart agent runs, and/or edit trajectories/logs.
- Not on critical path of 8x non-stationary/stochastic

### Streamlining of code, for 1-click eval

Currently, our code is quite hodge-podge, and data from proxies in manually collated as input into the predictive GLM. While some work to improve the data management pipeline is in scope and ongoing (using cloud storage, MongoDB, and WandB), a full eval which is runnable in 1 click is currently out of scope.

### Comparison to one-shot solutions

Many of our proxy evals have one-shot solutions. For example, rather than execute directory-creation one-directory-at-a-time, an agent could output a single script which – if run – would perfectly complete the task. Performance at this one-shot version would provide a baseline to show that it is the multi-step nature of the proxy evals which limits the agent, rather than its ability to comprehend the problem.

### Other hypothesised precursor capabilities

We focus here on two hypothesised “precursor abilities” (ability to handle non-stationarity and stochasticity), but one could conceive of many more possibilities. For example, in developmental or animal cognition, the A-not-B test looks for an incomplete or absent schema of object permanence, which could be expected to be broadly upstream of general task performance.