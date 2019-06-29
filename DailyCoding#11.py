# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Twitter.
#
# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
#
# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
#
# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

string="do"
stringlist=['dog','deer','deal']

def autocomplete(stringlist,string):
    string_dict={}
    final_list=[]
    for i in stringlist:
        if i[0] in string_dict:
            string_dict[i[0]].append(i)
        else:
            string_dict[i[0]] = [i]

    for i in string_dict:
        if i == string[0]:
            for j in string_dict[i]:
                if string in j:
                    final_list.append(j)
    return final_list



list=autocomplete(stringlist,string)
print(list)