# Inspect AI Tools Pattern

## Tool Definition Structure

Tools must follow a factory pattern where the `@tool` decorator wraps a function that **returns** an async callable:

```python
@tool
def move_up():
    async def execute() -> str:
        """Tool description goes HERE on the inner function.
        
        This docstring is parsed by Inspect to extract the tool description.
        Parameter documentation is required for any parameters.
        """
        # implementation
        return "result"
    
    return execute
```

## Critical Requirements

1. **Docstring placement**: Docstring must be on the `execute` function (inner), NOT the outer factory function
2. **Return type annotation**: The `execute` function must have a return type (e.g., `-> str`)
3. **Factory pattern**: The outer function returns the `execute` function (call with `()` when collecting tools)
4. **Tool collection**: When creating tools, call the factory: `tools = [move_up(), move_down()]`

## Custom Solver with Tools

To use tools in a custom solver, set `state.tools` and call `generate()`:

```python
@solver
def custom_solver():
    async def solve(state: TaskState, generate):
        tools = create_movement_tools(maze_state)
        state.tools = tools
        
        # Model will now have access to tools
        state = await generate(state)
        return state
    
    return solve
```

The `generate()` function handles tool calling automatically when `state.tools` is set.

## Common Errors

- **"Description not provided for tool"**: Docstring on wrong function (outer vs inner)
- **"coroutine object has no attribute"**: Calling tools without `()` in return statement
- **Model doesn't use tools**: Missing `state.tools` assignment before `generate()`
