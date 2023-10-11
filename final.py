# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1: Input: strs = ["flower","flow","flight"] Output: "fl"
# Example 2: Input: strs = ["dog","racecar","car"] Output: "" Explanation: There is no common prefix among the input strings.

# Constraints:
#  1 <= strs.length <= 200
#  0 <= strs[i].length <= 200
#  strs[i] consists of only lowercase English letters.

#strs = ["flpower","flpw","flpght", "flpripa", "flpripondio", "flpooar", "arnulflpo", "aflpasfldffla", "inflpa", "runflpa"]
#strs = ["dog","racecar","car"]
#strs = ["rbasower","rbow","rbight", "rboripa", "rboripondio", "rbipar", "arnulrbo", "arbnasrbdfrba", "inrba", "runrba"]
strs = ["flower","flow","flight", "floripa", "floripondio", "flipar", "arnulflo", "aflnasfldffla", "infla", "runfla"]
#strs = ["rbasowerff","rbasw","rbasightff", "rbasoripffa", "rbasipaffr", "arbasnasrbdfrba", "inrbas", "runrbas"]
#strs = ["dog","racecog","caasrog", "asdfffog"]
#strs = ["eadogt","raracecogt","tacaasrogt", "msasdfffogt"]

def vamoarribaquenoperdemo():
    strs.sort(key=len)
    lmc = strs[0]
    m = len(strs[0])
    res = None

    ar = 0
    pa = 2
    sub = ''

    def arpa():
        paarpa = pa
        ararpa = ar
        list = []
        while paarpa != 0 and ararpa <= (m - 1):
            list.append(lmc[ararpa])
            paarpa = paarpa - 1
            ararpa = ararpa + 1
        se = ''.join(list)
        return se

    def estaSubMod():
        val2 = True
        for i in strs:
            if i.count(sub) == 0:
                val2 = False
        return val2

    sub = arpa()

    while ar + pa <= m:
        if estaSubMod() == True:
            res = sub
            pa = pa + 1
            sub = arpa()
        else:
            ar = ar + 1
            sub = arpa()

    return res

y = vamoarribaquenoperdemo()
print(y)
