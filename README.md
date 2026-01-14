Building an eval of model's ability to adapt to changing ("non-stationary") environments - end goal = determain how well this precusor ability predicts mdoel perfomance on eg SWE bench.

## How this specific eval works:

Generate an ASCII maze, give the model 4 tools: move up, down, left and right.
Measure perfomance on solving the maze (if solved within a reasonable # steps, and # steps to solve)

Then, measure perfomance on the non-stationary variant - rotate or mirror the maze every 5 turns.

https://github.com/user-attachments/assets/7209355e-653c-49b6-9dcc-bb9530d9726c

