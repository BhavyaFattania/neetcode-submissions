class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in range(0,len(strs)):
            encoded +=str(len(strs[i]))+ "#" + strs[i]
        print(encoded)
        return encoded
            
    def decode(self, s: str) -> List[str]:
        ans = []
        i=0
        while i < len(s):
            if s[i] >="0" and s[i]<="9" and s[i+1]=="#":
                length_word = int(s[i])
                i+=2
                word=""
                j=0
                while j < length_word:
                    word+=s[i]
                    i+=1
                    j+=1
                ans.append(word)
        return ans
                