"""
  836. Rectangle Overlap
  
  https://leetcode.com/problems/rectangle-overlap/description/
  
  An axis-aligned rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) is the coordinate of its bottom-left corner, and (x2, y2) is the coordinate of its top-right corner. 
  Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.
  Two rectangles overlap if the area of their intersection is positive. 
  To be clear, two rectangles that only touch at the corner or edges do not overlap.
  Given two axis-aligned rectangles rec1 and rec2, return true if they overlap, otherwise return false.
  
  Example 1:
  Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
  Output: true
  
  Example 2:
  Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
  Output: false
  
  Example 3:
  Input: rec1 = [0,0,1,1], rec2 = [2,2,3,3]
  Output: false
"""

# time: beats 100%
# memory: beats 13.35%
class Solution:
  def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
    found = False
    base = min(rec1[2], rec2[2]) - max(rec1[0], rec2[0])
    height = min(rec1[3], rec2[3]) - max(rec1[1], rec2[1])
    if (base < 0) or (height < 0):
      return False
    intersection_area = base*height
    if intersection_area > 0:
      return True
    return False 
