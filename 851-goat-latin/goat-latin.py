class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split()
        words = [ele for ele in words if ele != ""]

        result = []
        vowels = "aeiouAEIOU"
        for i,w in enumerate(words):
            gl = ""
            if w[0] in vowels:
                gl = w + "ma"
            else:
                gl = w[1:] + w[0] + "ma"
            
            gl += 'a'*(i+1)
            result.append(gl)
        
        return ' '.join(result)
        