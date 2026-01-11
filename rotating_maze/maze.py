"""Maze generation and state management for Rotating Maze eval."""

import random
from typing import Tuple, List, Optional
from collections import deque
from enum import Enum


class Direction(Enum):
    """Cardinal directions for maze navigation."""
    NORTH = (0, -1)
    SOUTH = (0, 1)
    EAST = (1, 0)
    WEST = (-1, 0)


class MazeGenerator:
    """Generates solvable mazes using recursive backtracking."""

    def __init__(self, width: int, height: int):
        """Initialize maze generator.

        Args:
            width: Maze width (must be odd for proper wall generation)
            height: Maze height (must be odd for proper wall generation)
        """
        self.width = width if width % 2 == 1 else width + 1
        self.height = height if height % 2 == 1 else height + 1
        self.grid = [['#' for _ in range(self.width)] for _ in range(self.height)]

    def generate(self) -> Tuple[List[List[str]], Tuple[int, int], Tuple[int, int], int]:
        """Generate a maze with start at top-left and goal at bottom-right.

        Returns:
            Tuple of (grid, start_pos, goal_pos, optimal_path_length)
        """
        # Start carving from top-left
        start_x, start_y = 1, 1
        self._carve_passages(start_x, start_y)

        # Fixed positions: top-left for start, bottom-right for goal
        start_pos = (1, 1)
        goal_pos = (self.width - 2, self.height - 2)

        # Calculate optimal path length using BFS
        optimal_length = self._calculate_optimal_path(start_pos, goal_pos)

        return self.grid, start_pos, goal_pos, optimal_length

    def _carve_passages(self, x: int, y: int):
        """Recursively carve passages using recursive backtracking.

        Args:
            x: Current x coordinate
            y: Current y coordinate
        """
        self.grid[y][x] = ' '

        # Shuffle directions for randomness
        directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # Check if new position is valid and unvisited
            if (0 <= nx < self.width and 0 <= ny < self.height and
                self.grid[ny][nx] == '#'):
                # Carve the wall between current and new cell
                self.grid[y + dy // 2][x + dx // 2] = ' '
                self._carve_passages(nx, ny)

    def _calculate_optimal_path(self, start: Tuple[int, int], goal: Tuple[int, int]) -> int:
        """Calculate optimal path length using BFS.

        Args:
            start: Start position (x, y)
            goal: Goal position (x, y)

        Returns:
            Length of optimal path
        """
        queue = deque([(start, 0)])
        visited = {start}

        while queue:
            (x, y), dist = queue.popleft()

            if (x, y) == goal:
                return dist

            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                nx, ny = x + dx, y + dy

                if (0 <= nx < self.width and 0 <= ny < self.height and
                    self.grid[ny][nx] != '#' and (nx, ny) not in visited):
                    visited.add((nx, ny))
                    queue.append(((nx, ny), dist + 1))

        # Should never reach here if maze is solvable
        raise ValueError("No path found between start and goal")


class Transformation(Enum):
    """Types of visual transformations."""
    ROTATE_90 = "rotate_90"
    ROTATE_180 = "rotate_180"
    ROTATE_270 = "rotate_270"
    FLIP_H = "flip_horizontal"
    FLIP_V = "flip_vertical"


class MazeState:
    """Manages maze state including position, transformations, and view generation."""

    def __init__(self, grid: List[List[str]], start_pos: Tuple[int, int],
                 goal_pos: Tuple[int, int], optimal_path_length: int,
                 max_steps: int, variant: str = "stationary"):
        """Initialize maze state.

        Args:
            grid: 2D array representing the maze
            start_pos: Starting position (x, y)
            goal_pos: Goal position (x, y)
            optimal_path_length: Length of optimal solution
            max_steps: Maximum allowed steps
            variant: "stationary" or "non_stationary"
        """
        self.original_grid = [row[:] for row in grid]  # Deep copy
        self.start_pos = start_pos
        self.goal_pos = goal_pos
        self.current_position = start_pos
        self.optimal_path_length = optimal_path_length
        self.max_steps = max_steps
        self.variant = variant

        # Transformation state
        self.move_count = 0
        self.rotation_count = 0  # 0, 1, 2, 3 for 0°, 90°, 180°, 270°
        self.flip_h = False
        self.flip_v = False

        # Transformation triggers (every 5 moves for non-stationary)
        self.transform_interval = 5

    def get_view(self) -> str:
        """Get current transformed ASCII view of the maze.

        Returns:
            String representation of the maze with transformations applied
        """
        # Start with a copy of the original grid
        view = [row[:] for row in self.original_grid]

        # Mark current position
        cx, cy = self.current_position
        view[cy][cx] = 'P'

        # Mark goal (if not at current position)
        gx, gy = self.goal_pos
        if (gx, gy) != self.current_position:
            view[gy][gx] = 'G'

        # Mark start (if not at current position or goal)
        sx, sy = self.start_pos
        if (sx, sy) != self.current_position and (sx, sy) != self.goal_pos:
            view[sy][sx] = 'S'

        # Apply transformations
        view = self._apply_transformations(view)

        # Convert to string
        return '\n'.join([''.join(row) for row in view])

    def _apply_transformations(self, grid: List[List[str]]) -> List[List[str]]:
        """Apply current transformations to the grid.

        Args:
            grid: Grid to transform

        Returns:
            Transformed grid
        """
        result = grid

        # Apply rotation
        for _ in range(self.rotation_count):
            result = self._rotate_90(result)

        # Apply flips
        if self.flip_h:
            result = self._flip_horizontal(result)
        if self.flip_v:
            result = self._flip_vertical(result)

        return result

    def _rotate_90(self, grid: List[List[str]]) -> List[List[str]]:
        """Rotate grid 90 degrees clockwise."""
        height = len(grid)
        width = len(grid[0])
        rotated = [['' for _ in range(height)] for _ in range(width)]

        for y in range(height):
            for x in range(width):
                rotated[x][height - 1 - y] = grid[y][x]

        return rotated

    def _flip_horizontal(self, grid: List[List[str]]) -> List[List[str]]:
        """Flip grid horizontally."""
        return [row[::-1] for row in grid]

    def _flip_vertical(self, grid: List[List[str]]) -> List[List[str]]:
        """Flip grid vertically."""
        return grid[::-1]

    def should_transform(self) -> bool:
        """Check if transformation should occur at current move count.

        Returns:
            True if transformation should occur
        """
        if self.variant != "non_stationary":
            return False

        return self.move_count > 0 and self.move_count % self.transform_interval == 0

    def apply_transformation(self):
        """Apply a random transformation to the view."""
        transformation = random.choice(list(Transformation))

        if transformation == Transformation.ROTATE_90:
            self.rotation_count = (self.rotation_count + 1) % 4
        elif transformation == Transformation.ROTATE_180:
            self.rotation_count = (self.rotation_count + 2) % 4
        elif transformation == Transformation.ROTATE_270:
            self.rotation_count = (self.rotation_count + 3) % 4
        elif transformation == Transformation.FLIP_H:
            self.flip_h = not self.flip_h
        elif transformation == Transformation.FLIP_V:
            self.flip_v = not self.flip_v

    def translate_visual_to_actual(self, visual_direction: str) -> Tuple[int, int]:
        """Translate visual direction to actual coordinate change.

        Args:
            visual_direction: "up", "down", "left", "right"

        Returns:
            (dx, dy) coordinate change in original grid
        """
        # Define base directions (before transformation)
        base_dirs = {
            "up": (0, -1),
            "down": (0, 1),
            "left": (-1, 0),
            "right": (1, 0)
        }

        dx, dy = base_dirs[visual_direction]

        # Apply reverse rotation transformations
        for _ in range(self.rotation_count):
            # Rotate counter-clockwise to reverse the visual rotation
            dx, dy = dy, -dx

        # Apply reverse flips
        if self.flip_h:
            dx = -dx
        if self.flip_v:
            dy = -dy

        return dx, dy

    def is_valid_move(self, direction: Tuple[int, int]) -> bool:
        """Check if move is valid.

        Args:
            direction: (dx, dy) coordinate change

        Returns:
            True if move is valid
        """
        dx, dy = direction
        nx, ny = self.current_position[0] + dx, self.current_position[1] + dy

        # Check bounds
        if not (0 <= nx < len(self.original_grid[0]) and
                0 <= ny < len(self.original_grid)):
            return False

        # Check if wall
        return self.original_grid[ny][nx] != '#'

    def make_move(self, direction: Tuple[int, int]):
        """Make a move in the specified direction.

        Args:
            direction: (dx, dy) coordinate change
        """
        dx, dy = direction
        self.current_position = (
            self.current_position[0] + dx,
            self.current_position[1] + dy
        )
        self.move_count += 1

    def at_goal(self) -> bool:
        """Check if agent is at goal position.

        Returns:
            True if at goal
        """
        return self.current_position == self.goal_pos

    def exceeded_max_steps(self) -> bool:
        """Check if max steps exceeded.

        Returns:
            True if max steps exceeded
        """
        return self.move_count >= self.max_steps


def generate_maze_instance(size_range: Tuple[int, int] = (12, 18),
                          variant: str = "stationary") -> dict:
    """Generate a single maze instance for the dataset.

    Args:
        size_range: (min_size, max_size) for maze dimensions
        variant: "stationary" or "non_stationary"

    Returns:
        Dictionary with maze data
    """
    # Random size within range (ensure odd for proper maze generation)
    size = random.randint(size_range[0], size_range[1])
    if size % 2 == 0:
        size += 1

    # Generate maze
    generator = MazeGenerator(size, size)
    grid, start_pos, goal_pos, optimal_length = generator.generate()

    # Calculate max steps
    max_steps = optimal_length * 3

    # Create state
    state = MazeState(grid, start_pos, goal_pos, optimal_length, max_steps, variant)

    return {
        "grid": grid,
        "start_pos": start_pos,
        "goal_pos": goal_pos,
        "optimal_path_length": optimal_length,
        "max_steps": max_steps,
        "variant": variant,
        "initial_view": state.get_view()
    }
