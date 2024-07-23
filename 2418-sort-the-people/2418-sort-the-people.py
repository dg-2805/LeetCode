class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d1=list(zip(names,heights))
        people=sorted(d1,key=lambda item:item[1],reverse=True)
        output=[names for names,heights in people]
        return output