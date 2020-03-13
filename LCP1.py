class Solution:
    def game(self, guess, answer):
        count = 0
        for i in range(len(guess)):
            if(guess[i] == answer[i]):
                count += 1
        return count
