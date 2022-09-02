class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        result = 0
        tr_x, tr_y = topRight.x, topRight.y
        bl_x, bl_y = bottomLeft.x, bottomLeft.y
        q = [(tr_x, tr_y, bl_x, bl_y)]  #Create a queue to store the coordinates of the sea
        while len(q) > 0:
            tr_x, tr_y, bl_x, bl_y = q.pop(0)  #Pop the first element in the queue
            
            if bl_x > tr_x or bl_y > tr_y: #If the bottom left coordinate is greater than the top right coordinate, then there is no ship in this area
                continue
            
            hasShip = sea.hasShips(Point(tr_x, tr_y), Point(bl_x, bl_y))#Check if there is a ship in this area
            if hasShip == False:
                continue
            if bl_x == tr_x and tr_y == bl_y:  #If the bottom left coordinate is equal to the top right coordinate, then there is only one ship in this area
                result += 1
            else:
                midX = (bl_x + tr_x) // 2
                midY = (tr_y + bl_y) // 2
                q.append((tr_x, tr_y, midX+1, midY+1))  #Top right quadrant
                q.append((tr_x, midY, midX+1, bl_y))  # Bottom right quadrant
                q.append((midX, midY, bl_x, bl_y))    # Bottom left quadrant
                q.append((midX, tr_y, bl_x, midY+1))     # Top left quadrant
        return result

    '''

    Check this for detailed explanation using recursion:
    https://leetcode.com/problems/number-of-ships-in-a-rectangle/discuss/1024086/Divide-and-Conquer-or-Visual-%2B-Explanation-or-Python

    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
	   def d_c(bottom, top):     
            if bottom.x > top.x or bottom.y > top.y:return 0
            if (top.x, top.y)  == (bottom.x, bottom.y): 
                # has a ship 
                return int(sea.hasShips(top, bottom)) 
            else:
                # does not have ship 
                if not sea.hasShips(top, bottom):return 0
                
                x0, y0 = bottom.x, bottom.y
                x1, y1 = top.x, top.y
                center_x, center_y = (x0 + x1)//2, (y0+y1)//2
                q1 = d_c(bottom, Point(center_x, center_y))
                q2 = d_c(Point(center_x+1, center_y+1), top)
                q3 = d_c(Point(x0, center_y+1), Point(center_x, y1))
                q4 = d_c(Point(center_x+1, y0), Point(x1, center_y))

                return q1 + q2 + q3 + q4
            
        return d_c(bottomLeft, topRight)  
    '''