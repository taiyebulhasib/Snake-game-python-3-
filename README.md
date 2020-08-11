# Snake-game-python-3-

Run the game

snake game.py

Changing here and there

You can change the game components and their actions very easily by changing and updating in necessary component. For example if you want to spawn some food with more than 1 score. You just have to update in 3 places.

1st change the food class to accept a score as initializing paramete def __init__(self, x, y, score):

Change the score update from score += 1 to score += food.score

Food spawing now should be using self.food = Food(x, y, desired_score) That's all there to do for the simple task.
