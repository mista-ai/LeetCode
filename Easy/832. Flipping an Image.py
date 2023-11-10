class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i].reverse()
            image[i] = [0 if j == 1 else 1 for j in image[i]]
        return image