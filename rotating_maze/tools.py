"""Movement tools for Rotating Maze eval."""

from inspect_ai.tool import tool
from .maze import MazeState


def create_movement_tools(state: MazeState):
    """Create movement tools bound to a specific maze state.

    Args:
        state: MazeState instance to bind tools to

    Returns:
        List of tool functions
    """

    @tool
    def move_up():
        async def execute():
            """Move one step up in the current maze view."""
            # Translate visual "up" to actual coordinate change
            direction = state.translate_visual_to_actual("up")

            if not state.is_valid_move(direction):
                return f"Cannot move up - wall or boundary.\nSteps: {state.move_count}/{state.max_steps}\n\n{state.get_view()}"

            # Make the move
            state.make_move(direction)

            # Check if transformation should occur
            if state.should_transform():
                state.apply_transformation()

            # Check terminal conditions
            if state.at_goal():
                return f"Success! Reached the goal in {state.move_count} moves.\n\n{state.get_view()}"

            if state.exceeded_max_steps():
                return f"Max steps ({state.max_steps}) reached. Task failed.\n\n{state.get_view()}"

            return f"Moved up.\nSteps: {state.move_count}/{state.max_steps}\n\n{state.get_view()}"

        return execute

    @tool
    def move_down():
        async def execute():
            """Move one step down in the current maze view."""
            direction = state.translate_visual_to_actual("down")

            if not state.is_valid_move(direction):
                return f"Cannot move down - wall or boundary.\nSteps: {state.move_count}/{state.max_steps}\n\n{state.get_view()}"

            state.make_move(direction)

            if state.should_transform():
                state.apply_transformation()

            if state.at_goal():
                return f"Success! Reached the goal in {state.move_count} moves.\n\n{state.get_view()}"

            if state.exceeded_max_steps():
                return f"Max steps ({state.max_steps}) reached. Task failed.\n\n{state.get_view()}"

            return f"Moved down.\nSteps: {state.move_count}/{state.max_steps}\n\n{state.get_view()}"

        return execute

    @tool
    def move_left():
        async def execute():
            """Move one step left in the current maze view."""
            direction = state.translate_visual_to_actual("left")

            if not state.is_valid_move(direction):
                return f"Cannot move left - wall or boundary.\nSteps: {state.move_count}/{state.max_steps}\n\n{state.get_view()}"

            state.make_move(direction)

            if state.should_transform():
                state.apply_transformation()

            if state.at_goal():
                return f"Success! Reached the goal in {state.move_count} moves.\n\n{state.get_view()}"

            if state.exceeded_max_steps():
                return f"Max steps ({state.max_steps}) reached. Task failed.\n\n{state.get_view()}"

            return f"Moved left.\nSteps: {state.move_count}/{state.max_steps}\n\n{state.get_view()}"

        return execute

    @tool
    def move_right():
        async def execute():
            """Move one step right in the current maze view."""
            direction = state.translate_visual_to_actual("right")

            if not state.is_valid_move(direction):
                return f"Cannot move right - wall or boundary.\nSteps: {state.move_count}/{state.max_steps}\n\n{state.get_view()}"

            state.make_move(direction)

            if state.should_transform():
                state.apply_transformation()

            if state.at_goal():
                return f"Success! Reached the goal in {state.move_count} moves.\n\n{state.get_view()}"

            if state.exceeded_max_steps():
                return f"Max steps ({state.max_steps}) reached. Task failed.\n\n{state.get_view()}"

            return f"Moved right.\nSteps: {state.move_count}/{state.max_steps}\n\n{state.get_view()}"

        return execute

    return [move_up(), move_down(), move_left(), move_right()]
