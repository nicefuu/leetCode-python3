"""我们来定义一个函数 f(s)，其中传入参数 s 是一个非空字符串；该函数的功能是统计 s  中（按字典序比较）
最小字母的出现频次。
例如，若 s = "dcce"，那么 f(s) = 2，因为最小的字母是 "c"，它出现了 2 次。
现在，给你两个字符串数组待查表 queries 和词汇表 words，请你返回一个整数数组 answer 作为答案，
其中每个 answer[i] 是满足 f(queries[i]) < f(W) 的词的数目，W 是词汇表 words 中的词。

示例 1

输入：queries = ["cbd"], words = ["zaaaz"]
输出：[1]
解释：查询 f("cbd") = 1，而 f("zaaaz") = 3 所以 f("cbd") < f("zaaaz")。
示例 2：

输入：queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
输出：[1,2]
解释：第一个查询 f("bbb") < f("aaaa")，第二个查询 f("aaa") 和 f("aaaa") 都 > f("cc")。
"""
class Solution:#超时
    def numSmallerByFrequency(self, queries, words) :
        """
        :param queries: list[str]
        :param words: listr[str]
        :return: list[int]
        """
        t=[]
        cnt=0
        for i in range(len(queries)):
            for j in range(len(words)):
                if queries[i].count(min(queries[i]))<words[j].count(min(words[j])):
                    cnt+=1
            t.append(cnt)
            cnt=0
        return t



class Solution2:
    def numSmallerByFrequency(self, queries, words) :
        """
        :param queries: list[str]
        :param words: listr[str]
        :return: list[int]
        """
        ret, queries_count, words_count = [], [], []
        words_count = [word.count(min(word)) for word in words]
        for query in queries:
            c = query.count(min(query))
            # 在 words_count 里数一下有多少是比 c 大的
            ret.append(len([x for x in words_count if c < x]))
        return ret

s=Solution()
q1,w1= ["cbd"],["zaaaz"]
q2,w2=["bbb","cc"],["a","aa","aaa","aaaa"]
q3,w3=["aabbabbb","abbbabaa","aabbbabaa","aabba","abb","a","ba","aa","ba","baabbbaaaa","babaa","bbbbabaa"],\
      ["b","aaaba","aaaabba","aa","aabaabab","aabbaaabbb","ababb","bbb","aabbbabb","aab","bbaaababba","baaaaa"]
print(s.numSmallerByFrequency(q1,w1))
print(s.numSmallerByFrequency(q2,w2))
print(s.numSmallerByFrequency(q3,w3))