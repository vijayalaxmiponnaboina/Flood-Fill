from collections import deque
class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        m=len(image)
        n=len(image[0])
        q=deque()
        original_color=image[sr][sc]
        if original_color==color:
            return image
        q.append((sr,sc))
        image[sr][sc]=color

        while q:
            size = len(q)
            for k in range(size):
                r,c = q.popleft()

                # UP
                if r-1>=0 and image[r-1][c]==original_color:
                    image[r-1][c]=color
                    q.append((r-1,c))
                    
                # DOWN
                if r+1<m and image[r+1][c]==original_color:
                    image[r+1][c]=color
                    q.append((r+1,c))

                # LEFT
                if c-1>=0 and image[r][c-1]==original_color:
                    image[r][c-1]=color
                    q.append((r,c-1))

                # RIGHT
                if c+1<n and image[r][c+1]==original_color:
                    image[r][c+1]=color
                    q.append((r,c+1))
        return image