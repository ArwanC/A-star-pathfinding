# A-star-pathfinding

Visualization of the A* path finding algorithm in a grid map. Additional functionalities make it possible to edit a grid to create custom maps with the mouse, or adding or removing obstacles while the algorithm is running.

The heuristic function implemented is the Manhattan distance (also called Taxicab metric). This distance represents the sum of the absolute differences of the coordinates of two cells. The A* algorithm needs a heuristic function to approximate the shortest path between two points at any time as well as it can (as long as that path is <= to the real shortest path). In this case, diagonal movements are not allowed and thus a Euclidian distance would be less accurate than a Manhattan distance since this metric will return stair-like paths.

![Random map - Animated gif demo](random_map.gif) | ![Custom map - Animated gif demo](custom_map.gif)

The black circles represent obstacles. Light blue ones are part of the closed set (a set of cells that the algorithm already visited). Dark blue ones are part of the open set (a set of cells that the algorithm can potentialy consider to look at next). The red circles represent the shortest path at a given time. 

## Commands:
* 'Space' - Randomize grid with 25% obstacle probability
* 'Return' - Start path finding algorithm
* Right-click - Set cell as finish zone
* Left-click - Set cell as starting zone
* Mouse-drag - Set cells as obstacles
* 'e' - Toggle between adding obstacle and removing obstacles when mouse-dragging
* 'r' - Reset grid by removing all obstacles and open and closed set visualizations
