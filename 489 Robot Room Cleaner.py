# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
		# to match robot's turning direction, here is in a clockwise order
        directions = [(-1,0),(0,1),(1,0),(0, -1)]
        
        def dfs(r, c, curr_dir, visited):
            robot.clean()
            visited.add((r, c))

            for i in range(4):
                new_dir = (curr_dir + i) % 4
				# get neighbour's coordinates
                new_x = r + directions[new_dir][0]
                new_y = c + directions[new_dir][1]
                
                if (new_x, new_y) not in visited and robot.move():
                    dfs(new_x, new_y, new_dir, visited)
                
                # change to the next direction, turnleft can also pass tests, but for consistency with choices in directions list showing in a clockwise way, robot turns right. 
                robot.turnRight()

            # go backward by turning 180 degree
            robot.turnRight()
            robot.turnRight()
			# going back to previous cell
            robot.move()
            # change back to original direction by turning 180 degree again
            robot.turnRight()
            robot.turnRight()
        dfs(0, 0, 0, set())

#https://leetcode.com/problems/robot-room-cleaner/solutions/2176720/backtracking-with-explanation-about-directions-and-move/?languageTags=python
