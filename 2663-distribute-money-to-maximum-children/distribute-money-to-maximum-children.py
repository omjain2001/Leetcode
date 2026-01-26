class Solution:
    def distMoney(self, money: int, children: int) -> int:

        if money < children:
            return -1
        
        money -= children

        count = 0
        for i in range(children):
            if money >= 7:
                count += 1
                money -= 7
            else:
                if i == children-1 and (money+1) == 4:
                    count -= 1
                money = 0
                break

        if money > 0:
            count -= 1 
        
        return count
        