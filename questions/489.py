class Robot:
    def move(self):
        """
        Returns true if the cell in front is open and robot moves into the cell.
        Returns false if the cell in front is blocked and robot stays in the current cell.
        :rtype bool
        """
        pass

    def turnLeft(self):
        """
        Robot will stay in the same cell after calling turnLeft/turnRight.
        Each turn will be 90 degrees.
        :rtype void
        """
        pass

    def turnRight(self):
        """
        Robot will stay in the same cell after calling turnLeft/turnRight.
        Each turn will be 90 degrees.
        :rtype void
        """
        pass

    def clean(self):
        """
        Clean the current cell.
        :rtype void
        """
        pass


class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        
        def go_back():
            robot.turnRight()            
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
            
        def backtrack(cell=(0,0), d=0):
            visited.add(cell)
            robot.clean()
            
            for i in range(4):
                new_d = (d+ i)%4
                new_cell = (cell[0] + directions[new_d][0], \
                           cell[1] + directions[new_d][1])
                
                if new_cell not in visited and robot.move():
                    backtrack(new_cell, new_d)
                    go_back()
                    
                robot.turnRight()
            
        # Clockwise: 0 -> up, 1 -> right, 2 -> down, 3 -> left
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()
        backtrack()