mystr = "GTCACTTCGGGTTCAACTCGGTTAGCCCTCACCGCGAGCCTCATCAGATAATCTTCCCGCGAACCGATCCGGGAACGTTTCAGGCCTTTACCCAAATATCCTGGGGAAGCACAGGCGTCCGTCTTAAATCAGGAACTCCCATCAATTTTTGGTTGTTCCCGCGGAGGCAGCGTCATGGACGGAGTCCCTTGGTGTTATGCTGACTCTGACAAGGTGTGTAATTTGGCTGGAGATTTGAGCAGCACTCCCTCAAAAACCTGTGAGGGCCGCTCATTTTCACTCAGGGATCCAGGCTCGGATGTCTTGCCGTATGACCAGTGGACATATCGAAGAGTCGCAATCACGGCCCTTCCGTCCGGTTAACGACGAACACTACGGAAAAGCGATGGCGCAGCCTTTAAAGCATACGACAGATTTGATAGAATATAGATTCGCAAGGGCTATCGCGGTAGCAGACCGGACGGGTCCAGGCCATAACTGGGGCTCATAGGGCCTGCCAGCAAACATCCCCTTCTTCGTCAAGTGTATGACTTTTACGTCTAGCCTCGGAGTGTAGGAACAATTTCCGTGTATATCGAAGCCCATTGTTTCTCGGCCCCCGAGGGCTGTGATCGCAGGAGACTTAGTTGACCGCAACTTCATCTTCACCCGCTTACAACTTGCTTCCCCGATATTGGCGGGCAAGAATGTCACGCGGACTCGACTACGCCGGTTGACGTTTAGTAGTGCGTAGATAAATACTGTCTGGCTACCCGAGATGTTTGCTCGTCTTCTCGTGAGTCCAAAGTGTTTAAGCAAAGAGGTAGCGTACCAGTTCTTACGATTTGCCTCCCGAATAATACGAGACTCGGGTTCCCGGCTGGCAGACTTATCATATGGTTACTTTTTCACATTGGGGTCCCGTATAGAATCATACTTTACTGGCTTACTAGTGATCGAAAAAGAAACGGCCAGCAGCGCAAACCTTAGCTTGAAGCAGGAAACGCGCGCA"
mylist = []
reverse = mystr[::-1]
mystr1 = ""
print(reverse)
for x in reverse:
    mylist.append(x)
print(mylist)
length = len(mylist)
for x in range(length):
    if mylist[x] == "A":
       mylist[x] = "T"
       continue
    if mylist[x] == "T":
       mylist[x] = "A"
       continue
    if mylist[x] == "C":
       mylist[x] = "G"
       continue
    if mylist[x] == "G":
       mylist[x] = "C"
for x in mylist:
    mystr1 = mystr1 + x
print(mystr1)