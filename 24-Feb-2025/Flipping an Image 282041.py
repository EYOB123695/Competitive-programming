# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n=len(image)
        for i in range(n):
            image[i].reverse()
            
            for j in range(len(image[0])):
                if image[i][j] == 0 :
                    image[i][j] = 1 
                else:
                    image[i][j] = 0
        return image