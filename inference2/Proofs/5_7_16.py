from openpyxl import load_workbook
from collections import Counter
import copy
import time
import operator
import sys
from ex_dict_new import large_dict
from claims_new import pop_sent

tot_tim = time.time()
# averaged .076 on 5.22 (proof type 'n'), .039 definitions, .004 statement logic
# averaged .059 on 5.22 proof type 'n', .023 definitions, .004 statement
# but just prior to that the speed was .066
# time spent in instantiation is .029

#right now type o renders 33,35,36 as false
j = 2 # was 35
proof_type = 'l' # if l then long proof showing decision procedure for instantiation
strt = 2 # if n then proof type before may 1
stp = 3
print_to_doc = True
if j == 1:
    django2 = False
    temp17 = False
    excel = True
    one_sent = False
    mysql = False
    debug = False
    words_used = True
elif j == 2:
    django2 = False
    excel = False
    temp17 = False
    one_sent = True
    bool1 = True
    wb4 = load_workbook('/Users/kylefoley/PycharmProjects/inference_engine2/inference2/temp_proof.xlsx')
    # wb4 = load_workbook('../temp_proof.xlsx')
    w4 = wb4.worksheets[0]
    mysql = False
    debug = False
    words_used = False
elif j == 3:
    django2 = False
    excel = False
    one_sent = False
    mysql = True
    debug = False
    words_used = False
elif j == 4:
    django2 = False
    temp17 = True
    excel = False
    one_sent = False
    mysql = False
    debug = False
    words_used = False
elif j == 5:
    django2 = True
    temp17 = False
    excel = False
    one_sent = False
    mysql = False
    debug = False




########################
# new code



if mysql:
    from inference2.models import Define3, Archives, Input
    from inference2 import views
if mysql:
    import os
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    print BASE_DIR
    sys.path.append(BASE_DIR)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "inference_engine2.settings")
    import django
    django.setup()
    from inference2 import views
    from inference2.models import Define3, Archives, Input


anaphoric_relations = []
prop_name = []
prop_var = []
plural_c = []
embed = []
affneg = []
anaphora = ""
impl = ""
time1 = 0
band_aid_axiom = "" # the sentence x is a thing in axioms is getting placed
# in the standard_cj list because the counting of premises is messed up
# this is a temporary fix for that problem
definite = []
psent = []
definite2 = []
ant_cond = []
cnjts = []
never_used = []
conditionals = []
def_used = []
candd = []
candd2 = []
rel_conj = []
ind_var = []
gen_var = []
already_defined = []
conc = []
prop_sent = []
tagged_nouns = []
tagged_nouns2 = []
dv_nam = []
basic_objects = []
result_data = {}
st_log_tim = 0
def_tim = 0
inst_tim = 0
cond_r = unichr(8835)
const = u"\u2102" #consistency
top = unichr(8868)
bottom = unichr(8869)
neg = unichr(172)
idd = unichr(8781) # translation symbol
iff = unichr(8801)
mini_c = unichr(8658)
mini_e = unichr(8703)
implies = unichr(8866)
conditional = unichr(8594)
nonseq = unichr(8876)
xorr = unichr(8891)
idisj = unichr(8744)
cj = unichr(8896)
aid = unichr(8776)
disj = unichr(8855)
equi = unichr(8660)
ne = u"\u2260" # not equal

sn = 1
instan_used = 0 # the number of times the instan function is used
instan_time = 0 # measures the time used in instantiation
qn = 300 # numbers the property sent list
pn = 400
id_num=0

l1 = u"\u2081"
l2 = u"\u2082"
l3 = u"\u2083"
l4 = u"\u2084" #if you increase to l5 then change convert function
ua = u"\u1d43"
ub = u"\u1d47"
uc = u"\u1d9c"
ud = u"\u1d48"
ue = u"\u1d49"
uf = u"\u1da0"
ug = u"\u1d4d"
ui = u"\u2071"
uk = u"\u1d4f"
um = u"\u1d50"
un = u"\u207f"
uo = u"\u1d52"
up = u"\u1d56"
ut = u"\u1d57"
uv = u"\u1d5b"
uu = u"\u1d58"
uw = u"\u02b7"
uy = u"\u02b8"
uj = u"\u02B2"
ul = u"\u02E1"
ur = u"\u02b3"
us = u"\u02e2"
uh = u"\u02b0"

tot_prop_name = []
tot_prop_sent = []
prop_var4 = [unichr(97 + t) for t in range(26)]
prop_var2 = [unichr(97 + t) + u"\u2081" for t in range(26)]
prop_var3 = [unichr(97 + t) + u"\u2082" for t in range(26)]
prop_var5 = [unichr(97 + t) + u"\u2083" for t in range(26)]
prop_var6 = [unichr(97 + t) + u"\u2084" for t in range(26)]
prop_var4 = prop_var4 + prop_var2 + prop_var3 + prop_var5 + prop_var6
idf_var2 = [unichr(122 - t) for t in range(25)]
idf_var2.remove("i")
idf_var2.remove("l")
idf_var3 = [unichr(122 - t) + l1 for t in range(25)]
idf_var4 = [unichr(122 - t) + l2 for t in range(25)]
idf_var2 = idf_var2 + idf_var3 + idf_var4
greek = [unichr(945 + t) for t in range(50)]
p = 1
subscripts = [l1,l2,l3,l4]

if excel:
    wb4 = load_workbook('../inference engine new.xlsx')
    w4 = wb4.worksheets[0]
    wb5 = load_workbook('../dictionary4.xlsx')
    ws = wb5.worksheets[0]
elif temp17:
    wb4 = load_workbook('../inference engine new.xlsx')
    w4 = wb4.worksheets[0]
elif one_sent:
    pass
else:
    ws = Define3.objects.all() #Kyle
    w4 = Input.objects.all()

#
# >> 8835
# ta^ 8868
# co^ 8869
# nt+ 172
# x^ 8801
# c^ 8658
# # 8703
# i^ 8866
# t^ 8594
# nf^ 8876
# ed^ 8891
# v+ 8744
# && 8896
# @ 8855
# if^ 8660


def tran_str(str1,type3):

    list2 = []
    str2 = ""
    if 'co^' in str1:
        str1 = str1.replace('co^ ',"")
        str2 = 'co'
    if "|" in str1:
        for i in range(len(str1)):
            if str1[i:i+1] == "|":
                str3 = str1[i+1:i+2]
                str4 = get_super(str3)
                str1 = str1[:i] + str4 + str1[i+2:]
                bb = 8

    if type3 == 3:

        if "t^" in str1:
            str1 = str1.replace("t^",conditional)
        if "nt+" in str1:
            str1 = str1.replace("nt+",neg)
        if "zzz" in str1:
            str1 = str1.replace("zzz",ne)
        if "x^" in str1:
            str1 = str1.replace("x^",iff)
        if "b^" in str1:
            str1 = str1.replace("b^",mini_e)
        if "c^" in str1:
            str1 = str1.replace("c^",mini_c)
        if "ed^" in str1:
            str1 = str1.replace("ed^",xorr)
        if "v+" in str1:
            str1 = str1.replace("v+",idisj)
    if type3 == 1:
        list2 = str1.split(" % ")
    else:
        list2 = str1

    return [list2,str2]



def get_super(str1):

    if str1 == "a":
        return u"\u1d43"
    elif str1 == "b":
        return u"\u1d47"
    elif str1 == "c":
        return u"\u1d9c"
    elif str1 == "d":
        return u"\u1d48"
    elif str1 == "e":
        return u"\u1d49"
    elif str1 == "f":
        return u"\u1da0"
    elif str1 == "g":
        return u"\u1d4d"
    elif str1 == "h":
        return u"\u02b0"
    elif str1 == "i":
        return u"\u2071"
    elif str1 == "j":
        return u"\u02B2"
    elif str1 == "k":
        return u"\u1d4f"

     # ua = u"\u1d43"
    # ub = u"\u1d47"
    # uc = u"\u1d9c"
    # ud = u"\u1d48"
    # ue = u"\u1d49"
    # uf = u"\u1da0"
    # ug = u"\u1d4d"
    # uh = u"\u02b0"
    # ui = u"\u2071"
    # uj = u"\u02B2"
    # uk = u"\u1d4f"
    # ul = u"\u02E1"
    # um = u"\u1d50"
    # un = u"\u207f"
    # uo = u"\u1d52"
    # up = u"\u1d56"
    # ur = u"\u02b3"
    # us = u"\u02e2"
    # ut = u"\u1d57"
    # uu = u"\u1d58"
    # uv = u"\u1d5b"
    # uw = u"\u02b7"
    # uy = u"\u02b8"

    elif str1 == "l":
        return u"\u02E1"
    elif str1 == "m":
        return u"\u1d50"
    elif str1 == "n":
        return u"\u207f"
    elif str1 == "o":
        return u"\u1d52"
    elif str1 == "p":
        return u"\u1d56"
    elif str1 == "r":
        return u"\u02b3"
    elif str1 == "s":
        return u"\u02e2"
    elif str1 == "t":
        return u"\u1d57"
    elif str1 == "u":
        return u"\u1d58"
    elif str1 == "v":
        return u"\u1d5b"
    elif str1 == "w":
        return u"\u02b7"
    elif str1 == "y":
        return u"\u02b8"









def remove_outer_paren(str1,bool1 = False):

    if str1 == "":
        return ""
    elif str1.count(")") == 0:
        if not bool1:
            return str1
        else:
            return False

    j = 0
    # on very rare occasions we will encounter strings of the following form ((p))
    if str1[0] != "(" and str1[-1] != ")":
        if not bool1:
            return str1
        else:
            return True
    if str1[:2] == "((" and str1[-2:] == "))":
        d = 2
    else:
        d = 1

    for k in range(0, d):
        for i in range(0, len(str1)):
            str2 = str1[i:i + 1]
            if str2 == "(":
                j += 1
            elif str2 == ")":
                j -= 1
            if j == 0 and i + 1 != len(str1):
                break
            elif j == 0 and i + 1 == len(str1):
                str1 = str1[1:len(str1) - 1]
                if bool1:
                    return True
    if not bool1:
        return str1
    else:
        return False


def remove_redundant_paren(str1):
    j = 0
    str2 = str1[:2]
    str3 = str1[2:]
    if str2 == '((' and str3 == '))':

        for i in range(0, len(str1)):
            str2 = str1[i:i + 1]
            if str2 == "(":
                j += 1
            elif str2 == ")":
                j -= 1
            if j == 1 and i + 1 != len(str1):
                break
            elif j == 0 and i + 1 == len(str1):
                str1 = str1[1:len(str1) - 1]
    return str1

def mainconn(str1):

    ostring = copy.copy(str1)
    if os(str1):
        return ["", 0]
    if str1.find("&") < -1 and str1.find(idisj) < -1 and str1.find(iff) < -1 and str1.find(conditional) < -1 and \
            str1.find(implies) < -1 and str1.find(nonseq) < -1 and str1.find(xorr) < -1:
        return ["", 0]

    str3 = str1
    bool1 = False

    if str1[0] == "~":
        str1 = str1[1:]
        bool1 = True

    j = 0
    bool2 = False
    for i in range(0, len(str1)):
        str2 = str1[i:i + 1]
        if str2 == "(":
            j += 1
        elif str2 == ")":
            j -= 1

        if j == 0 and i + 1 != len(str1):
            break
        elif j == 0 and i + 1 == len(str1):
            str1 = str1[1:len(str1) - 1]
            bool2 = True

    j = -1
    for i in range(0, len(str1)):
        str2 = str1[i:i + 1]
        if str2 == conditional:
            f = -1
        if str2 == idisj or str2 == "&" or str2 == iff or str2 == implies or \
                str2 == nonseq or str2 == conditional or str2 == xorr:
            if str3 != str2 and str3 != "":
                j = j + 1

            str3 = str2

    if j == -1:
        i = ostring.find(str3)
        return [str3, i]
    k = -1
    j = -1
    while True:
        k += 1
        if k > 150:
            break
        for i in range(0, len(str1)):
            str2 = str1[i:i + 1]

            if str2 == "(":
                j += 1
            elif str2 == ")":
                j -= 1

            if j == -1 and (str2 == idisj or str2 == "&" or str2 == iff or str2 == implies
                            or str2 == nonseq or str2 == conditional or str2 == xorr):
                if bool1 and bool2:
                    return [str2, i+2]
                elif bool2 or bool1:
                    return [str2, i+1]
                else:
                    return [str2, i]
        else:
            str1 = str1[1:-1]

def isvariable(str3,kind=""):

    bool2 = True
    if str3 == None:
        return False

    if str3 == 'a':
        return False
    elif str3 == 'i':
        return False
    try:
        if str3 != "":
            str3 = str3.replace(l1, "")
            str3 = str3.replace(l2, "")
            str3 = str3.replace(neg, "")
            if len(str3) == 1 and str3.islower():
                bool2 = True
            else:
                bool2 = False
    except AttributeError:
        print ('error in isvariable function')
        sys.exit()
    if kind == "":
        return bool2
    else:
        return isidef

def os(str1):

    cnx = [xorr, iff, idisj, conditional, implies, nonseq, "&"]
    for i in range(0, len(cnx)):
        if str1.find(cnx[i]) > -1:
            os = False
            return os
    os = True
    return os

def enclose(str1):

    i = -1
    global subscripts
    while i < len(str1) -1:
        i += 1
        str2 = str1[i:i+1]
        str3 = str1[i-1:i]
        str4 = str1[i+1:i+2]
        if str2.islower() and str4 in subscripts:
            if str3 == "~":
                str1 = str1[:i-1] + "(~" + str2 + str4 + ")" + str1[i+2:]
            else:
                str1 = str1[:i] + "(" + str2 + str4 + ")" + str1[i+2:]
            i += 4
        elif str2.islower():
            if str3 == "~":
                str1 = str1[:i-1] + "(~" + str2 + ")" + str1[i+1:]
            else:
                str1 = str1[:i] + "(" + str2 + ")" + str1[i+1:]
            i += 3
    return str1

def is_natural_language(sentence,i):
    # this determines if the sentence is natural or an abbreviation
    if sentence[i+1] == "~":
        if sentence[i+3] in subscripts and sentence[i+4] == ")":
            return True
        elif sentence[i+3] == ")":
            return True
    else:
        if sentence[i+2] in subscripts and sentence[i+3] == ")":
            return True
        elif sentence[i+2] == ")":
            return True
    return False

def find_sentences(sentence):

    global subscripts
    if sentence == None:
        return
    g = sentence.count('(')
    h = sentence.count(')')
    if g != h:
        print 'wrong number of parentheses in sentence:' + sentence
        sys.exit()
    if sentence.startswith("(~g)"):
        bb = 8
    marker = False
    il = -1
    total = -1
    c = -1
    neg_value = []
    str1 = ""
    sent1 = []
    sent_type2 = []
    wneg = []
    output = [None] * 9
    # the skel name list names each single sentence after a greek letter, even if
    # the same sentence appears twice it obtains a different name on the second
    # appearance
    skel_nam = []
    sent_num = []
    if sentence.find("~(") > -1:
        sentence = sentence.replace("~(", "(!")
    if sentence.find(implies) > -1:
        str2 = implies
    elif sentence.find(nonseq) > -1:
        str2 = nonseq
    str3 = mainconn(sentence)
    sentence = sentence.strip()
    str4 = str3[0]
    f = str3[1]
    id_num = []
    id_num.append(["1",str4,f])
    sent_num.append([1, '1', sentence, str4,f])
    str21 = ""
    p = 947
    unenclose_at_end = False
    connectives = ["&", idisj, iff, conditional, nonseq, implies,xorr]
    arr1 = []
    mini_c2 = mini_c + neg
    sentence2 = copy.copy(sentence)
    prt = copy.copy(sentence)
    more_num = [unichr(945 + x) for x in range(24)]
    if os(sentence) == False:
        temp_string = mainconn(sentence)

        if sentence.find(implies) > -1:
            str1 = implies
        elif sentence.find(nonseq) > -1:
            str1 = nonseq
        else:
            if temp_string == iff:
                str1 = "bicond"
            elif temp_string == conditional:
                str1 = "cond"
            elif temp_string == "&":
                str1 = "cj"

        sent1.append(sentence)
        neg_value.append("")
        sent_type2.append(str1)
        wneg.append(sentence)
        skel_nam.append(None)

    j = 0
    n = 0
    for i in range(0, len(sentence)):
        str1 = sentence[i:(i + 1)]
        for o in connectives:
            if str1 == o:
                j += 1

    while n < j + 1:

        il += 1
        if il > 15:
            break

        e = 0
        l = len(sentence)
        x = -1
        while x < l - 1:
            x += 1
            temp_string = sentence[x:x+1]
            if sentence[x:x+1] == "(":
                if not unenclose_at_end:
                    unenclose_at_end = is_natural_language(sentence,x)

                if marker == False:
                    z = x
                    marker = True

                total += 1
            elif sentence[x: x + 1] == ")":
                total -= 1
                if total == -1:
                    marker = False
                    e += 1
                    c += 1

                    temp_sent = sentence[z: x + 1]
                    if temp_sent == '(bIc)':
                        pp = 7
                    otemp_sent = copy.copy(temp_sent)

                    if (len(sentence) - len(temp_sent)) > 2:
                        if temp_sent in prt and temp_sent in str21 and prt != str21:
                            prtnum = findinlist(str21,sent_num,2,1,False)
                            numb = prtnum + "1"
                        elif temp_sent in prt:
                            prtnum = findinlist(prt,sent_num,2,1,False)
                            numb = prtnum + "1"
                        else:
                            prtnum = ""
                            for bb in range(len(sent_num)-1,-1,-1):
                                str3 = sent_num[bb][2]
                                if os(temp_sent) and str21 != "":
                                    if str21 == str3 and temp_sent in sent_num[bb][2]:
                        # this is for those basic molecules for which the same sentence appears
                        # in the definition several times
                                        prtnum = sent_num[bb][1]
                                        break
                                else:
                                    if temp_sent in sent_num[bb][2]:
                                        prtnum = sent_num[bb][1]
                                        break
                            # if prtnum == "":
                            #     easygui.msgbox('your sentences are not numbered properly')
                            g = len(prtnum) + 1
                            f = 0

                            for bb in range(len(sent_num)-1,-1,-1):
                                temp_sn = sent_num[bb][1]
                                h = temp_sn[:g-1]
                                hh = sent_num[bb][0]
                                if g > sent_num[bb][0]:
                                    break
                                if sent_num[bb][0] == g and temp_sn[:g-1] == prtnum:
                                    f += 1

                            f += 1
                            if f < 10:
                                numb = prtnum + str(f)
                            else:
                                numb = prtnum + more_num[f-10]

                        prt = temp_sent
                        temp_mc = mainconn(temp_sent)
                        mc = temp_mc[0]
                        str3 = temp_mc[0]
                        g = temp_mc[1]
                        mc_num = temp_mc[1]
                        sent_num.append([len(numb), numb, temp_sent, str3,g])


                        if os(temp_sent):

                            # n counts the number of single sentences
                            n += 1
                            if temp_sent.find("~") > -1:
                                neg_value.append("~")
                                temp_sent = temp_sent.replace("~", "")

                            elif temp_sent.find(mini_c2) > -1:
                                neg_value.append("~")
                                temp_sent = temp_sent.replace(mini_c2, mini_c)

                            elif temp_sent.find(mini_c2) == -1 and temp_sent.find(mini_c) > -1:
                                neg_value.append("")
                            elif temp_sent.find("~") == -1:
                                neg_value.append("")
                            else:
                                break  # stop
                        else:
                            neg_value.append("")

                        sent1.append(temp_sent)
                        wneg.append(otemp_sent)
                        id_num.append([numb,mc,mc_num])

                        if os(otemp_sent):
                            p += 1
                            skel_nam.append([otemp_sent, unichr(p)])
                        else:
                            skel_nam.append(None)
                    else:
                        sentence = sentence[1:len(sentence) - 1]
                        l = len(sentence)
                        x = -1
                        c -= - 1
                        e -= - 1

        total = -1
        marker = False
        w = -1

        if n < j + 1:
            if len(sent1) > w:
                while w + 1 < len(sent1):
                    if w == 13:
                        pp = 7
                    w += 1
                    str21 = sent1[w]
                    if not os(str21) and w != 0:
                        if str21 not in arr1:
                            sentence = str21
                            arr1.append(sentence)
                            break

    for i in range(len(sent1)):
        temp_string = sent1[i]
        if temp_string.find("(!") > -1:
            sent1[i] = sent1[i].replace("(!", "~(")
            wneg[i] = wneg[i].replace("(!", "~(")
    m = 0
    bool1 = False
    for i in range(len(id_num)):
        if (id_num[i][1] == iff or id_num[i][1] == conditional) \
                and not bool1:
            m = i
            break

    sdefinition = cut_def([sent1,id_num],sentence2)
    str1 = copy.copy(sdefinition)
    for i in range(len(wneg)):
        if os(wneg[i]):
            str1 = str1.replace(skel_nam[i][0],skel_nam[i][1])

    skel_string = str1
    # skel_string = remove_outer_paren(skel_string)
    if skel_string.find("(!") > -1:
        skel_string = skel_string.replace("(!","~(")

    if unenclose_at_end:
        for i in range(len(sent1)):
            sent1[i] = unenclose(sent1[i])
            wneg[i] = unenclose(wneg[i])

    output[0] = sent1
    output[1] = neg_value
    output[2] = sent_type2
    output[3] = wneg
    output[4] = id_num
    output[5] = skel_string
    output[6] = skel_nam
    output[7] = m # m is the first sentence to be used when changing variables in a definition
    output[8] = sdefinition

    return output

def add_to_dv(dv_nam,all_sent,m,k,idf_var,str2):

    if isvariable(str2) == False:
        str3 = findinlist(str2, dv_nam,1,0)
        if str3 == None:
            telist7 = [idf_var[0], str2]
            if k == 69 or k == 70:
                all_sent[m][k] = idf_var[0] + "'s"
            else:
                all_sent[m][k] = idf_var[0]
            del idf_var[0]
            dv_nam.append(telist7)
        elif k == 69 or k == 70:
            all_sent[m][k] = str3 + "'s"
        else:
            all_sent[m][k] = str3

def word_sub(idf_var, dv_nam, tot_sent, all_sent, words,id_num):

    all_sent = remove_duplicates(all_sent,0)
    relations = words[18]
    relations2 = words[19]
    pronouns = words[24]
    num = [4, 5, 13, 14, 17, 18, 22, 26, 30,34,35,36,51,52,63,64,65,67,69,70]
    # num2 = [9,15,19,23,27,31,49]
    num3 = [8,12,49,50,51,52]
    other = ['there','it'+up]
    global sn
    m = -1
    while m < len(all_sent) -1:
        m += 1
        if all_sent[m][47] != "no word sub":
            bool1 = False
            list4 = copy.deepcopy(all_sent[m][46])
            old_sent = all_sent[m][0]
            oldp = all_sent[m][42]
            for i in range(len(all_sent[m][46])):
                k = all_sent[m][46][i]
                if k == 8:
                    bb = 8
                str2 = all_sent[m][k]
                if str2 != None:
                    if str2 == "~":
                        str2 = None
                    elif str2 not in def_used and not str2.isupper():
                        def_used.append(str2)
                if k in num3 and str2 != None:
                    bool1 = True
                    str5 = findinlist(str2,words[16],0,1)
                    if k == 12:
                        all_sent[m][8] = str5
                        all_sent[m][12] = None
                    else:
                        all_sent[m][k] = str5
                if k == 69 or k == 70:
                    str2 = str2[:-2]
                    dummy = add_to_dv(dv_nam,all_sent,m,k,idf_var,str2)
                elif k in num and all_sent[m][45] != k:
                    bool1 = True
                    if str2 != None and str2 not in pronouns and str2 not in other:
                        dummy = add_to_dv(dv_nam,all_sent,m,k,idf_var,str2)

            if bool1:
                new_sent = build_sent(all_sent[m])
                newp = name_sent(new_sent)
                all_sent[m][0] = new_sent
                all_sent[m][42] = newp
                dummy = new_sentence2(old_sent,oldp,new_sent,newp,tot_sent,"SUB",id_num)
                all_sent[m][46] = list4
                bool1 = False

            # decision = []
            # decision = dec_pro(decision,all_sent[m],pronouns)
            # all_sent[m][56] = decision

    return

def assigned_var(str1, dv_nam, idf_var):

    bool1 = False
    for i in range(len(dv_nam)):
        if dv_nam[i][1] == str1:
            bool1 = True
            return dv_nam[i][0]

    if bool1 == False:
        str2 = idf_var[0]
        list1 = [str2, str1]
        dv_nam.append(list1)
        del idf_var[0]
        return str2

def there(all_sent,m,tot_sent,def_sent):

    global sn
    old_sent = all_sent[m][0]
    oldp = all_sent[m][42]
    list1 = copy.deepcopy(all_sent[m])
    list1[5] = all_sent[m][14]
    list1[3] = all_sent[m][10]
    list1[4] = all_sent[m][13]
    list1[14] = None
    list1[10] = None
    list1[13] = None
    new_sent = build_sent(list1)
    newp = name_sent(new_sent)
    list1[0] = new_sent
    def_sent.append(new_sent)
    list1[42] = newp
    all_sent[m][46] = [200]
    all_sent[m][56] = [200]
    all_sent.append(list1)
    bool1 = check_dimension(tot_sent,1,new_sent)
    if not bool1:
        dummy = new_sentence2(old_sent,oldp,new_sent,newp,tot_sent,"DE there")

def scope_rel_pro(list,i):

    if i == 10 and list[59] != None:
        return False
    elif i == 16 and list[60] != None:
        return False
    elif i == 20 and list[61] != None:
        return False
    elif i == 24 and list[62] != None:
        return False
    else:
        return True

def cia(all_sent,m,tot_sent,i):

    list1 = [None] * 80
    old_sent = all_sent[m][0]
    oldp = all_sent[m][42]
    rule = "CIA"
    if i == 35:
        j = 5
    elif i == 36:
        j = 14
    elif i == 37:
        j = 18
    elif i == 38:
        j = 22
    str1 = all_sent[m][j]
    all_sent[m][j] = all_sent[m][i]
    list1[14] = str1
    list1[5] = all_sent[m][i]
    list1[9] = "I"
    list1[46] = [200]
    list1[56] = [200]
    all_sent[m][i] = None
    dummy = new_sent_prelim(old_sent,oldp,all_sent,list1,m,rule,tot_sent,1)


def adje(all_sent,m,tot_sent,i,words,idf_var):

    rule = 'ADJ E'
    list1 = [None] * 80
    old_sent = all_sent[m][0]
    oldp = all_sent[m][42]
    if i == 13:
        n = 10
        r = 9
    else:
        r = i-2
        n = i-1
    if all_sent[m][8] != None or all_sent[m][12] != None:
        str7 = "~"
        all_sent[m][8] = None
        all_sent[m][12] = None
    else:
        str7 = None
    list1[8] = str7
    list1[3] = all_sent[m][n]
    if all_sent[m][r] != "I":
        list1[5] = all_sent[m][i+1]
    else:
        list1[5] = all_sent[m][5]
    list1[9] = "J"
    list1[14] = all_sent[m][i]
    list1[46] = [200]
    list1[56] = [200]
    all_sent[m][i] = None
    list2 = all_sent[m][46]
    list2.remove(i)
    all_sent[m][46] = list2
    dummy = new_categories(all_sent[m],words,idf_var,all_sent)

    dummy = new_sent_prelim(old_sent,oldp,all_sent,list1,m,rule,tot_sent,1)

def rel_pro_elim(all_sent,m,tot_sent,i,words,idf_var):

    list1 = [None] * 80
    old_sent = all_sent[m][0]
    oldp = all_sent[m][42]
    rule = "DE " + all_sent[m][i]
    list1 = rel_pro(i,m,all_sent,list1,words,idf_var)
    dummy = new_sent_prelim(old_sent,oldp,all_sent,list1,m,rule,tot_sent,1)

def ande(all_sent,m,tot_sent,i,words,idf_var):
    # this seperates a sentence with an 'and' coordinator into two
    all_sent[m][66] = None
    old_sent = all_sent[m][0]
    oldp = all_sent[m][42]
    list1 = [None] * 80
    list1[5] = all_sent[m][67]
    all_sent[m][67] = None
    rule = "DE and" + uc
    for i in range(6,20):
        list1[i] = all_sent[m][i]
    list1 = new_categories(list1,words,idf_var,all_sent,True)
    dummy = new_sent_prelim(old_sent,oldp,all_sent,list1,m,rule,tot_sent,1)

def define(tot_sent,all_sent,idf_var,dv_nam,words,rep_rel,identities,\
        def_atoms,num_sent):

    zz = time.time()
    all_sent = remove_duplicates(all_sent,0)
    pronouns2 = copy.deepcopy(words[24])
    if "it" in pronouns2:
        pronouns2.remove("it")
    pronouns = pronouns2
    definitions = words[16]
    relations = words[6]
    poss_pro = words[25]
    posp = words[28] #part of speech
    atomic_relations = words[22]
    atomic_relata = words[23]
    compound = words[34]
    not_oft_def = words[36]
    uniq_obj = words[37]
    # we have not included group in this list because it seems to make things confusing
    atoms = ['moment','relationship','point','number','thought','imagination',\
            'property','possible world','possible relationship','word','reality']
    atoms2 = [['moment','T',14],['relationship',"IR",5],['point','S',14],['number','N',14],\
              ['thought','TK',14],['imagination',"M",14],\
            ['property',"J",14],['possible world','U',14],\
              ['possible relationship',"U",5],['word','AW',"b"],['reality',"IR",14]]

    h_tim = time.time()
    def_relat = ["J","I",'=','H']
    used_atoms = []
    ua_relat = [] #used atomic relations
    #unique objects which form a group, in the definiednum the relation is = but in the
    #definiens the IG relation appears
    # unq_gr = ['time'] #unique group
    global sn,anaphora,gen_var,def_tim
    i_defined = False
    def_sent = []
    al_def = [] #already defined
    numbers_def = []
    defined = []
    universal = ['every','no']
    indefinite = ['a',"many"+un,"a"+ua]


    for i in range(len(dv_nam)):
        if i == 3:
            bb = 7
        if not isinmdlist(dv_nam[i][1],relations,1):
            g = findposinlist(dv_nam[i][1],definitions,0)
            if dv_nam[i][1] in atoms:
                used_atoms.append(dv_nam[i][0])
                str1 = findinlist(dv_nam[i][1],atoms2,0,1)
                ua_relat.append(str1)
            if g > -1:
                list1 = [None] * 80
                list1[5] = dv_nam[i][0]
                list1[9] = '='
                list1[14] = dv_nam[i][1]
                str1 = build_sent(list1)
                str2 = name_sent(str1)
                list1[0] = str1
                list1[42] = str2
                list1[41] = 1
                list1[46] = [200]
                list1[56] = [200]
                all_sent.append(list1)
                # say you have the word 7 in your claim, then the code will define all numbers
                # down to 0 if you do not have the following code
                numbers_def.append(dv_nam[i][1])


    num10 = [5,14,18,22,26,30,34,63,64,65] # pronouns
    num20 = [3,10,16,20,24,28,32] # determiners
    num30 = [69,70] # proper name possessive
    # num40 = [66] # and
    num50 = [4,13,17,21,25,33] # adjective
    num60 = [35,36] # cia
    num70 = [59,60,61,62] # relative pronouns
    num80 = [62,61,60,7] # that-c
    num85 = [3,10,16,20,24,28,32] # possessive pronouns
    num90 = [69,70] # possessives
    num100 = [15,19] # RDA,RDB
    num110 = [5,63,64] # there
    num120 = [3,10,16,20,24,28,32] # every, many-n
    num130 = [9,14]


    m = -1
    while m < (len(all_sent)) -1:
        m += 1
        if 10 in all_sent[m][56]:
            for i in num10:
                if i in all_sent[m][46]:
                    str1 = all_sent[m][i]
                    definition = findinlist(str1,definitions,0,1)
                    if all_sent[m][0] not in def_sent and str1 not in universal and \
                        definition != None and str1 in pronouns:
                        if str1 != "i" or not i_defined:
                            dummy = def_rn(defined,al_def,definition, str1,0, tot_sent, \
                                dv_nam, idf_var,words,rep_rel, all_sent,m,[],[],\
                                    "pronoun",i)
                            if str1 != "i":
                                del all_sent[m]
                                m -= 1
                                break
                            else:
                                i_defined = True

    m = -1
    while m < (len(all_sent)) -1:
        m += 1
        if 20 in all_sent[m][56]:
            for i in num20:
                if i in all_sent[m][46] and all_sent[m][i] not in poss_pro:
                    str1 = all_sent[m][i]
                    definition = findinlist(str1,definitions,0,1)
                    if all_sent[m][0] not in def_sent and str1 not in universal:
                        dummy = def_rn(defined,al_def,definition, str1,0, tot_sent, \
                            dv_nam, idf_var,words,rep_rel, all_sent,m,[],[],\
                                "determinative",i)
                        del all_sent[m]
                        m -= 1
                        break

    m = -1
    while m < (len(all_sent)) -1:
        m += 1
        if 30 in all_sent[m][56]:
            for i in num30:
                if i in all_sent[m][46]:
                    definition = findinlist("the",definitions,0,1)
                    if all_sent[m][0] not in def_sent:
                        if i == 69:
                            i = 5
                        elif i == 70:
                            i = 14
                        dummy = def_rn(defined,al_def,definition, "the",0, tot_sent, \
                            dv_nam, idf_var,words,rep_rel, all_sent,m,[],[],\
                                "proper name possessive",i)
                        del all_sent[m]
                        m -= 1
                        break


    m = -1
    while m < (len(all_sent)) -1:
        m += 1
        start = False
        if all_sent[m][66] != None and all_sent[m][9] not in compound:
            dummy = ande(all_sent,m,tot_sent,i,words,idf_var)
            del all_sent[m]
            start = True
            m -= 1

        if 50 in all_sent[m][56] and not start:
            for i in num50:
                if i in all_sent[m][46] and scope_uni(all_sent,m,i):
                    dummy = adje(all_sent,m,tot_sent,i,words,idf_var)
                    break # this only works for one adjective

        if (36 in all_sent[m][46] or 35 in all_sent[m][46]) and not start:
            for i in num60:
                if all_sent[m][i] != None:
                    dummy = cia(all_sent,m,tot_sent,i)

        if 70 in all_sent[m][56] and not start:
            for i in num70:
                if i in all_sent[m][46] and scope_uni(all_sent,m,i,1) and \
                    all_sent[m][i] != 'that'+uc:
                    dummy = rel_pro_elim(all_sent,m,tot_sent,i,words,idf_var)
                    break

        if 80 in all_sent[m][56] and not start:
            for i in num80:
                if i in all_sent[m][46] and scope_uni(all_sent,m,i,1):
                    dummy = that(all_sent,m,i,tot_sent,dv_nam,words,idf_var)
                    del all_sent[m]
                    start = True
                    m -= 1
                    break

        if 85 in all_sent[m][56] and not start:
            for i in num85:
                if all_sent[m][i] != None and all_sent[m][i] in poss_pro:
                    str1 = all_sent[m][i]
                    definition = findinlist(str1,definitions,0,1)
                    if all_sent[m][0] not in def_sent:
                        dummy = def_rn(defined,al_def,definition, str1,0, tot_sent, \
                            dv_nam, idf_var,words,rep_rel, all_sent,m,[],[],\
                                "poss pro",i)
                        del all_sent[m]
                        m -= 1
                        start = True
                        break

        if 90 in all_sent[m][56] and not start:
            for i in num90:
                if i in all_sent[m][46]:
                    dummy = poss_elim(all_sent,m,i,tot_sent)
                    del all_sent[m]
                    start = True
                    m -= 1
                    break
        if m == 1:
            bb = 8
        if 100 in all_sent[m][56] and not start:
            for i in num100:
                if i in all_sent[m][46] and uni_scope_rel(all_sent,m,i):
                    dummy = rel_div(all_sent,m,tot_sent,i,posp,words,idf_var)
                    break

        if 110 in all_sent[m][56] and not start:
            for i in num110:
                if all_sent[m][i] == 'there':
                    dummy = there(all_sent,m,tot_sent,def_sent)
                    start = True
                    del all_sent[m]
                    m -= 1
                    break

        if 120 in all_sent[m][56] and not start:
            for i in num120:
                if i in all_sent[m][46]:
                    str1 = all_sent[m][i]
                    definition = findinlist(str1,definitions,0,1)
                    if all_sent[m][0] not in def_sent:
                        dummy = def_rn(defined,al_def,definition, str1,0, tot_sent, \
                            dv_nam, idf_var,words,rep_rel, all_sent,m,[],[],\
                                "determinative",i)
                        start = True
                        del all_sent[m]
                        m -= 1
                        break

    m = -1
    while m < len(all_sent)-1:
        m += 1
        for i in num130:
            adverb = False
            id = False
            kind = ""
            bool2 = False
            relat = all_sent[m][9]
            str1 = all_sent[m][i]
            if relat == 'B':
                bb = 8
            if m == 7 and i == 14:
                bb = 8

            if all_sent[m][43] != 'cc':
                if relat in def_relat and i == 14:
                    definiendum = findinlist(str1,dv_nam,0,1)
                    if definiendum in atomic_relata:
                        bool2 = False
                    else:
                        bool2 = True

                elif i == 48 and all_sent[m][48] != None:
                    definiendum = str1
                    bool2 = True
                    adverb = True
                    kind = 'R'
                elif i == 9 and relat == 'AS':
                    kind = 'AS'
                    definiendum = str1
                    bool2 = True
                elif i == 9 and relat in ua_relat:
                    dummy = add_atomic(all_sent,m,atoms2,tot_sent,dv_nam)
                elif relat == '=' and all_sent[m][41] == 1:
                    id = True
                    bool2 = True
                    definiendum = all_sent[m][14]
                    all_sent[m][41] = None
                    try:
                        str4 = int(definiendum)
                        if definiendum not in numbers_def:
                            bool2 = False
                    except ValueError:
                        pass
                elif relat == "=" and all_sent[m][41] != 1:
                    bool2 = False
                    identities.append([[all_sent[m][5],all_sent[m][14]],"","",""])
                    all_sent[m][46] = [200]
                    all_sent[m][56] = [200]
                elif i == 9 and relat != "J" and relat != "I" and relat != '=' \
                    and str1 not in atomic_relations:
                    definiendum = str1
                    bool2 = True
                    kind = 'R'
                if (bool2 and isdefineable(all_sent[m]) and definiendum != None and \
                        definiendum != '') or id:
                    if definiendum in not_oft_def:
                        break
                    if (id and definiendum not in uniq_obj) or (definiendum == "concept"+un and id):
                        break

                    g = findposinlist(definiendum,definitions,0)
                    definition = definitions[g][1]
                    if definition == 'natural':
                        definition = "(c'=" + definiendum + ") & (d'=natural_whole) & ((bIc') " + conditional \
                        + " (bId'))"
                    pos = definitions[g][2]
                    circ = definitions[g][3]
                    circ2 = all_sent[m][43]
                    basic_molecule = definitions[g][4]
        #this prevents us from getting caught in an infinite loop.
                    if basic_molecule == 'b' and all_sent[m][9] == "I":
                        break
                    # if relat == "I" and definiendum in unq_gr:
                    #     break
                    if circ2 == 'c':
                        circ += circ2
                    if (relat == "J" and pos == 'a') or (relat == "I" and pos == 'n') or (relat == 'H' and pos == 'n') \
                        or pos == 'r' or pos == 'e' or pos == 's' or (relat== '=' and pos == 'n') or adverb or id:
                        if definition != None and all_sent[m][0] not in def_sent:
                            def_sent.append(all_sent[m][0])
                            dummy = def_rn(defined,al_def,definition, definiendum,0,tot_sent,dv_nam, idf_var,\
                                words,rep_rel,all_sent,m,[],[],kind,i,circ)
                            break

    if def_atoms != []:
        for i in range(len(def_atoms)):
            a_relat = findinlist(def_atoms[i],atoms2,0,1)
            for j in range(len(all_sent)):
                if all_sent[j][46] != "x":
                    if all_sent[j][9] == a_relat and all_sent[j][8] != "~":
                        dummy = add_atomic(all_sent,j,atoms2,tot_sent,dv_nam)

# if we state that something is not a concept then we need to falisfy that
    dummy = concept(all_sent,tot_sent,dv_nam,definitions,posp)
    j = time.time()
    j = j - zz
    def_tim += j
    #end7
    return

def uni_scope_rel(all_sent,m,i):

    univ = ['every','no']
    if i == 15:
        if all_sent[m][3] in univ or all_sent[m][10] in univ:
            return False
        else:
            return True
    elif i == 19:
        if all_sent[m][3] in univ or all_sent[m][10] in univ \
            or all_sent[m][16] in univ:
            return False
        else:
            return True
    else:
        return True


def add_atomic(all_sent,m,atoms2,tot_sent,dv_nam):

    relat = all_sent[m][9]
    if all_sent[m][8] == "~":
        return
    pos = findinlist(relat,atoms2,1,2) #position = position
    str1 = all_sent[m][pos]
    str2 = findinlist(relat,atoms2,1,0)
    nobj = findinlist(str2,dv_nam,1,0) # new object = nobj
    list1 = [None] * 80
    if str1 != nobj:
        list1[5] = str1
        list1[9] = "I"
        list1[14] = nobj
        nsent = build_sent(list1) # new sent = nsent
        bool1 = check_dimension(all_sent,0,nsent)
        if not bool1:
            osent = all_sent[m][0]
            oldp = all_sent[m][42]
            nprop = name_sent(nsent) # new proposition = nprop
            list1[0] = nsent
            list1[42] = nprop
            list1[43] = "cc"
            all_sent.append(list1)
            dummy = new_sentence2(osent,oldp,nsent,nprop,tot_sent,"DE " + str2,"",iff)
        else:
            bb = 8


def concept(all_sent,tot_sent,dv_nam,definitions,posp):

    global sn
    str1 = ""
    list2 = []
    list1 = [None] * 80
    for i in range(len(dv_nam)):
        if dv_nam[i][1] == 'concept'+un or dv_nam[i][1] == 'concept'+ua:
            str1 = dv_nam[i][0]
        if str1 != "":
            for j in range(len(all_sent)):
                if all_sent[j][9] == "I" and all_sent[j][14] == str1 and all_sent[j][46] != "x"\
                        and all_sent[j][46] != "y":
                    str2 = all_sent[j][5]
                    con = findinlist(str2,dv_nam,0,1)
                    pos = findinlist(con,posp,0,1)
                    if pos == None:
                        bb = 7
                    if con != None:
                        if pos == 'a':
                            str4 = "J"
                        elif pos == 'n':
                            str4 = "I"
                        b = 0
                        bool1 = False
                        for k in range(len(all_sent)):
                            if all_sent[k][9] == str4 and all_sent[k][14] == str2 and \
                                str1 != str2 and str2 not in list2:
                                bool1 = True
                                str6 = all_sent[k][5]
                                list2.append(str2)
                                b += 1
                        if b > 1:
                            print 'you have not coded for multiple concepts'
                        olda = "(" + "b" + ' = ' + con + ")"
                        oldc = "(" + "c " +str4 + " b" + ")"
                        rn1 = ""
                        if str2 != "b":
                            rn1 = "(" + "b" + mini_c + str2 + ") & (" + "c" + mini_c + str6 + ")"
                        else:
                            rn1 = "(" + "c" + mini_c + str6 + ")"
                        newa = "(" + str2 + ' = ' + con + ")"
                        newc = "(" + str6 + " " + str4 + " " + str2 + ")"
                        oldcon = olda + " " + conditional + " " + oldc
                        sn += 1
                        tot_sent.append([sn,oldcon,"","","NC concept " + con,"","","",""])
                        sn += 1
                        tot_sent.append([sn,rn1,"","","RN","","","",""])
                        oldp = name_sent(newa)
                        newp = name_sent(newc)
                        if not bool1:
                            list1[0] = newc
                            list1[5] = str6
                            list1[9] = str4
                            list1[14] = str2
                            list1[40] = False
                            list1[42] = newp
                            all_sent.append(list1)
                        str3 = newa + " " + conditional + " " + newc
                        str3p = oldp + " " + conditional + " " + newp
                        sn += 1
                        tot_sent.append([sn,str3,str3p,"","SUB",sn-2,sn-1,"",""])
                        return

def name_sent(str1,bool2 = False,str4 = ""):
    global prop_var,affneg,prop_name

    no_space = copy.copy(str1)
    if str1.find('~') > -1:
        no_space = str1.replace("~","")
        str1 = str1.replace("~","")
        ng = '~'
    else:
        ng = ''

    if "  " in str1:
        str1 = str1.replace("  "," ")

    no_space = remove_outer_paren(no_space)
    no_space = no_space.replace(" ","")

    if bool2:
        if str4 == 'something':
            no_space = no_space.replace("something","some thing")
        elif str4 == 'anything':
            no_space = no_space.replace("anything","any thing")
        elif str4 == 'everything':
            no_space = no_space.replace("everything","every thing")
        elif str4 == 'anything'+ua:
            no_space = no_space.replace("anything"+ua,"a" + ua + " thing")

    h = findinlist(no_space,prop_name,1,0)
    if h != None:
        return ng + h
    else:
        prop_name.append([prop_var[0], no_space, str1])
        str2 = prop_var[0]
        del prop_var[0]
        return ng + str2

def assign_var(str1, str2, dv_nam):

    list1 = [str2, str1]
    dv_nam.append(list1)

def determ(idf_var, all_sent, tot_sent,words,dv_nam,m):

    global sn
    # def_det contains the determinatives and their definitions
    def_det = words[15]
    detm = words[2]
    list1 = copy.deepcopy(all_sent[m][46])
    num = [3,10]
    for i in range(len(all_sent[m][46])):
        k = all_sent[m][46][i]
        if k in num:
            str1 = all_sent[m][k]
            if str1 in detm:
                defin = findinlist(str1,def_det,0,2)
                all_sent[m][k] = None
                list1.remove(k)
                if i == 10:
                    if "z~Rc" in defin:
                        defin = defin.replace("z~Rc","c~Rz")
                    else:
                        defin = defin.replace("zRc","cRz")
                dummy = def_rn(defin,str1,tot_sent, dv_nam,idf_var)
    all_sent[m][46] = list1


def insert_space(str, integer):
    return str[0:integer] + ' ' + str[integer:]

def space_words(str1):
    # this function place a space between variables and relations
    # so as to make it easier to categorize words in a sentence
    str1 = str1.replace("~", " ~ ")
    str1 = str1.replace("=", " = ")
    str1 = str1.replace(neg, " " + neg + " ")
    str1 = str1.replace(mini_e, " " + mini_e + " ")
    str1 = str1.replace(ne, " " + ne + " ")
    i = -1
    while i + 1 < len(str1):
        i += 1
        temp_str = str1[i:(i + 1)]
        nxt_str = str1[(i + 1):(i + 2)]
        if nxt_str.isupper() == True and temp_str.islower() == True:
            str1 = insert_space(str1, i + 1)
        elif nxt_str.islower() == True and temp_str.isupper() == True:
            str1 = insert_space(str1, i + 1)
    return str1


def id_def(list1,words,idf_var,all_sent):
    # this function picks out that variables in the id sentences of the
    # definition

    list2 = []
    list3 = []
    list4 = []
    list6 = []
    list7 = []
    has_plural = False
    for i in range(len(list1[0])):
        if os(list1[0][i]) and mini_e in list1[0][i]:
            list3.append(list1[0][i])
        elif os(list1[0][i]) and "=" in list1[0][i]:
            str1 = list1[0][i]
            g = str1.find("=")
            var = str1[1:g]
            wrd = str1[g+1:-1]
            if isvariable(var):
                if wrd == 'plural form':
                    has_plural = True
                if not isvariable(wrd):
                    list2.append([var,wrd])

    if list3 != []:
        for i in range(len(list3)):
            prop_con = list3[i][1]
            str2 = list3[i].replace(" ","")
            str2 = str2[3:-1]
            str3 = space_words(str2)
            list5 = categorize_words(words,str3,idf_var,all_sent,1)
            list4.append(prop_con)
            str4 = list5[0].replace(" ","")
            list6.append(str4)
            list7.append(list5)

    return [list2,has_plural,list4,list6,list7]

def is_atomic(list1, atomic_relations):

    relat = [9,15,19,23,27,31]
    must_be_blank = [2,3,4,6,7,10,11,12,16,17,20,21,24,25,28,29,32,33]
    noun = [5,14,18,26,30,34]
    for i in range(len(list1)):
        str1 = list1[i]
        if str1 != None:
            if i in relat:
                if str1 in atomic_relations:
                    pass
                else:
                    pass
            elif i in must_be_blank:
                return False
            elif i in noun:
                if not isvariable(str1):
                    return False
    return True


def isdefineable(list1):


    must_be_blank = [2,3,4,6,7,10,11,13,16,17,18,20,21,23,24,25,27,28,29,31,32,33,\
        35,36,49,50,51,52,55]
    must_be_variable = [5,14,18,22]


    for i in must_be_blank:
        if list1[i] != None and list1[i] != '':
            return False
    for i in must_be_variable:
        if list1[i] != None:
            if not isvariable(list1[i]) and list1[i] != 'i':
                return False
    return True

def build_sent(list1,g=0,cat_sent=False):

    #if you revise this list then then you must also revise it in
    #the add_sent2, as well as the function 'that', as well as new_categories
    #g=1 means that it is a sentence that identifies a propositional constant, in some cases
    # the proposition itself need not be named
    # also fix list in word sub and isatomic

    str1 = "("
    num = [11,1,2,47,3,69,4,55,5,66,67,35,48,59,6,8,9,7,48,12,10,70,13,14,36,60,63,49,15,16,17,18,\
           61,64,50,19,20,21,22,62,65,51,23,24,25,26,52,27,28,\
           29,30,31,32,33,34]
    if g == 1:
        str1 = ""
        num = [47,3,69,4,55,5,66,67,35,48,59,6,8,9,7,48,12,10,70,13,14,36,60,63,49,15,16,17,18,\
           61,64,50,19,20,21,22,62,65,51,23,24,25,26,52,27,28,\
           29,30,31,32,33,34]

    for i in num:
        temp_str = list1[i]
        if temp_str != None and temp_str != "":
            if str1 == "(":
                str1 = str1 + temp_str
            else:
                str1 = str1 + " " + temp_str
    if g == 0:
        str1 += ")"
    else:
        str1 = str1.replace(" ","")

    return str1

def build_sent2(list1,bool1 = False):

    if bool1:
        g = len(list1) - 3
    else:
        g = len(list1)
    for i in range(0,g):
        if i == 0:
            str1 = list1[i]
        else:
            str1 += " " + list1[i]
    return "(" + str1 + ")"

def build_sent_list(list1):
    # this list builder does not have the ~ separated from the sentence
    str2 = None
    for i in range(len(list1)):
        if str2 == None:
            str2 = list1[i]
        else:
            str2 = str2 + ' & ' + list1[i]
    return str2

def build_sent_list2(list1):
    # this list builder has the ~ separated from the sentence
    str2 = None
    for i in range(len(list1)):
        if str2 == None:
            str2 = list1[i][1] + list1[i][0]
        else:
            str2 = str2 + ' & ' + list1[i][1] + list1[i][0]
    return str2

def remove_duplicates(list1,i):

    list2 = []
    j = -1
    while j < len(list1) -1:
        j += 1
        if list1[j][i] in list2:
            del list1[j]
            j -= 1
        else:
            list2.append(list1[j][i])

    return list1

def remove_duplicates2d(list1,i,h):

    list2 = []
    j = -1
    while j < len(list1) -1:
        j += 1
        for k in range(len(list1)):
            if k != j:
                if list1[k][i] == list1[j][i] and list1[k][h] == list1[j][h]:
                    del list1[j]
                    j -= 1
                    break
        else:
            list2.append(list1[j])
    return list2

def id_sent(list4,all_sent,irrel_group,embed_var):
    # this turns the dv_nam into a string of conjuncts

    global gen_var
    global ind_var
    global definite2

    dv_nam = []
    # this loop removes duplicates in a multidimensional list
    for i in range(len(list4)):
        if list4[i] not in dv_nam:
            dv_nam.append(list4[i])
    spec_prop = ["general","indefinite","definite"]
    prop2 = None
    str2 = None
    for i in range(len(dv_nam)):
        if isvariable(dv_nam[i][0]):
            irrel_group.append(dv_nam[i][0])
            list1 = [None] * 80
            list1[5] = dv_nam[i][0]
            if len(dv_nam[i]) > 2:
                list1[9] = mini_e
            else:
                list1[9] = "="
            list1[14] = dv_nam[i][1]
            str1 = build_sent(list1)
            list1[0] = str1
            bool1 = check_dimension(all_sent,0,str1)
            prop1 = name_sent(str1)
            list1[42] = prop1
            if not bool1 and dv_nam[i][1] not in spec_prop:
                all_sent.append(list1)
            if dv_nam[i][0] not in gen_var and dv_nam[i][0] not in ind_var \
                    and dv_nam[i][0] not in definite2:
                definite2.append(dv_nam[i][0])
            if mini_e in str1:
                embed_var.append(dv_nam[i][0])
        else:
            if len(dv_nam[i]) >2:
                str1 = '(' + dv_nam[i][0] + mini_e + dv_nam[i][1] + ')'
            else:
                str1 = '(' + dv_nam[i][0] + "=" + dv_nam[i][1] + ')'
            prop1 = name_sent(str1)
        if str2 == None:
            str2 = str1
            prop2 = prop1
        else:
            str2 = str2 + ' & ' + str1
            prop2 = prop2 + " & " + prop1
    return [str2, prop2]

def cut_string(str1,str2):

    if str1.find(str2) == -1:
        return str1
    g = str1.find(str2)
    str1 = str1[:g]
    str1 = str1.strip()
    return str1

def remove_values_from_list(the_list, val):

    while val in the_list:
        the_list.remove(val)
    return the_list

def divide_sent(words, list2, idf_var,tot_sent,all_sent):

    global sn
    global impl
    redundant = words[21]
    conn = words[4]
    relations = words[6]
    not_oft_def = words[36]
    uniq_obj = words[37]
    nonsq = False
    for i in range(len(list2)):
        str2 = list2[i][1]
        str2 = str2.lower()
        str3 = name_sent(str2)
        tot_sent.append([list2[i][0],str2,str3,"","","","","",""])
        all_sent.append(str2)

    # the following changes it is necessary that if p then q to if p then it is necessary q
    modals = ['possible','necessary','impossible']
    h = copy.copy(len(all_sent))
    i = -1
    while i < h - 1:
        i += 1
        all_sent[i] = all_sent[i].strip()
        all_sent[i] = all_sent[i].split(" ")
        all_sent[i] += ["("+tot_sent[i][1]+")",tot_sent[i][2],""]
        for j in range(len(all_sent[i])):
            if all_sent[i][j] not in def_used:
                def_used.append(all_sent[i][j])
            if all_sent[i][j] in modals:
                if all_sent[i][j+1] == 'that' and all_sent[i][j+2] == 'if':
                    old_sent = all_sent[i][-3]
                    old_p = tot_sent[i][2]
                    str1 = copy.copy(all_sent[i][j])
                    del all_sent[i][j+1]
                    del all_sent[i][j]
                    del all_sent[i][j-1]
                    del all_sent[i][j-2]
                    g = all_sent[i].index('then')
                    all_sent[i].insert(g+1,'it'+up)
                    all_sent[i].insert(g+2,'is'+ua)
                    all_sent[i].insert(g+3,str1)
                    all_sent[i].insert(g+4,'that')
                    del all_sent[i][-1]
                    del all_sent[i][-1]
                    new_sent = build_sent2(all_sent[i])
                    newp = name_sent(new_sent)
                    all_sent[i] += [new_sent,newp,""]
                    dummy = new_sentence2(old_sent,old_p,new_sent,newp,tot_sent,"modal transfer")
                    break
    str1 = ""
    bool1 = False

    for i in range(len(all_sent)):
        old_sent = all_sent[i][-3]
        old_p = all_sent[i][-2]
        str2 = ""
        for j in range(len(redundant)):
            str1 = redundant[j]
            if str1 in all_sent[i]:
                bool1 = True
                all_sent[i] = remove_values_from_list(all_sent[i],str1)
                if str2 == '':
                    str2 = str1
                else:
                    str2 += "," + str1
        if bool1:
            bool1 = False
            del all_sent[i][-1]
            del all_sent[i][-1]
            del all_sent[i][-1]
            new_sent = build_sent2(all_sent[i])
            newp = name_sent(new_sent)
            all_sent[i] += [new_sent,newp,""]
            rule = "RD " + str2
            dummy = new_sentence2(old_sent,old_p,new_sent,newp,tot_sent,rule)

    rule = "DE "
    g = len(all_sent)
    i = -1
    impl = ""
    while i < g - 1:
        i += 1
        for j in range(len(all_sent[i])):
            if all_sent[i][j] in not_oft_def:
                not_oft_def.remove(all_sent[i][j])
            if all_sent[i][j] in conn:
                str4 = all_sent[i][j]
                str5 = ""
                str6 = ""
                if all_sent[i][j] == 'follow':
                    str1 = nonseq
                    impl = nonseq
                    del all_sent[i][j+1]
                    del all_sent[i][j-1]
                    del all_sent[i][j-2]
                    j -= 2
                elif all_sent[i][j] == 'then' + ua:
                    str1 = conditional
                    str5 = "ant"
                    str6 = "con"
                else:
                    str1 = implies
                    impl = implies
                old_sent = all_sent[i][-3]
                old_p = all_sent[i][-2]
                del all_sent[i][-1]
                del all_sent[i][-1]
                del all_sent[i][-1]
                ant = all_sent[i][:j]
                cons = all_sent[i][j+1:]
                ant_s = build_sent2(ant)
                cons_s = build_sent2(cons)
                antp = name_sent(ant_s)
                consp = name_sent(cons_s)
                ant += [ant_s,antp,str5]
                cons += [cons_s,consp,str6]
                all_sent.append(ant)
                all_sent.append(cons)
                rule += str4
                del all_sent[i]
                i -= 1
                new_sent = "(" + ant_s + " " + str1 + " " + cons_s + ")"
                new_p = "(" + antp + ' ' + str1 + ' ' + consp + ")"
                dummy = new_sentence2(old_sent,old_p,new_sent,new_p,tot_sent,rule)
                break

    words[36] = not_oft_def
    g = len(all_sent)
    i = -1
    while i < g - 1:
        i += 1
        for j in range(len(all_sent[i])):
            if all_sent[i][j] == 'that':
                print 'that used'
                old_sent = all_sent[i][-2]
                old_p = all_sent[i][-1]
                del all_sent[i][-1]
                del all_sent[i][-1]
                del all_sent[i][-1]
                ant = all_sent[i][:j]
                cons = all_sent[i][j+1:]
                cons_s = build_sent2(cons)
                consp = name_sent(cons_s)
                del ant[0]
                ant.insert(0,consp)
                ant_s = build_sent2(ant)
                antp = name_sent(ant_s)
                if consp in idf_var:
                    idf_var.remove(consp)
                    dv_nam.append([consp, cons_s,1])
                ant += [ant_s,antp]
                cons += [cons_s,consp]
                all_sent.append(ant)
                all_sent.append(cons)
                del all_sent[i]
                i -= 1
                dummy = new_sentence2(old_sent,old_p,ant_s,antp,tot_sent,'DF that')
                break

    # g = len(all_sent)
    # i = -1
    # while i < g - 1:
    #     i += 1
    #     for j in range(len(all_sent[i])):
    #         if all_sent[i][j] == 'and':
    #             old_sent = all_sent[i][-2]
    #             old_p = all_sent[i][-1]
    #             del all_sent[i][-1]
    #             del all_sent[i][-1]
    #             ant = all_sent[i][:j]
    #             cons = all_sent[i][j+1:]
    #             cons_s = build_sent2(cons)
    #             consp = name_sent(cons_s)
    #             del ant[0]
    #             ant.insert(0,consp)
    #             ant_s = build_sent2(ant)
    #             antp = name_sent(ant_s)
    #             if consp in idf_var:
    #                 idf_var.remove(consp)
    #                 dv_nam.append([consp, cons_s,1])
    #             ant += [ant_s,antp]
    #             cons += [cons_s,consp]
    #             all_sent.append(ant)
    #             all_sent.append(cons)
    #             del all_sent[i]
    #             i -= 1
    #             dummy = new_sentence2(old_sent,old_p,ant_s,antp,tot_sent,'df that')
    #             break

    return



def rel_repl(all_sent,tot_sent,words,dv_nam,idf_var,id_num):

    relations = words[6]
    doubles = words[31]
    doubles.sort()
    for j in range(len(all_sent)):
        i = -1
        while i < len(all_sent[j])-3:
            i += 1
            if "," in all_sent[j][i]:
                has_comma = True
                str3 = all_sent[j][i]
                str3 = str3.replace(",","")
            else:
                str3 = all_sent[j][i]
                has_comma = False
            if str3 == 'spies':
                bb = 8
            bool2 = check_dimension(doubles,0,str3)
            bool3 = False
            if bool2:
                str4 = all_sent[j][i] + " " + all_sent[j][i+1]
                bool3 = check_dimension(doubles,1,str4)
                if bool3:
                    str3 += " " + all_sent[j][i+1]
                    if str3 not in def_used:
                        def_used.append(str3)
            else:
                if str3 not in def_used:
                    def_used.append(str3)
            str2 = findinlist(str3,relations,0,1)

            if str2 != None:
                g = findposinlist(str3,dv_nam,0)
                if g == -1:
                    dv_nam.append([str3,str2])
                if has_comma:
                    all_sent[j][i] = str2 + ","
                else:
                    all_sent[j][i] = str2
            if bool3:
                if str2 != None:
                    del all_sent[j][i+1]
                else:
                    i += 1
        old_sent = all_sent[j][-3]
        oldp = all_sent[j][-2]
        old_type = all_sent[j][-1]
        new_sent = build_sent2(all_sent[j],True)
        newp = name_sent(new_sent)
        all_sent[j][-3] = new_sent
        all_sent[j][-2] = newp
        all_sent[j][-1] = old_type
        if newp != oldp:
            dummy = new_sentence2(old_sent,oldp,new_sent,newp,tot_sent,"SUB",id_num)
        all_sent[j] = categorize_words(words,all_sent[j],idf_var,all_sent,0,True)

#here we change not a into no and other synonyms
    num = [8,49,50,51,52]
    cat = ['many'+un,'any'+un]
    for i in range(len(all_sent)):
        old_sent = all_sent[i][0]
        oldp = all_sent[i][42]
        bool2 = False
        for j in num:
            bool1 = False # yyy
            if all_sent[i][j] == "not" or all_sent[i][j] == neg:
                if j == 8:
                    if all_sent[i][9] != ne:
                        if all_sent[i][8] == 'not':
                            all_sent[i][8] = "~"
                    if all_sent[i][10] == "a":
                        all_sent[i][10] = 'every'
                        bool2 = True
                        rule = "DE ~ a"
                    elif all_sent[i][10] == "every":
                        all_sent[i][10] = 'many'+un
                        bool2 = True
                        bool1 = True
                        rule = "DE ~ every"
                    elif all_sent[i][10] in cat:
                        rule = "DE ~ " + all_sent[i][10]
                        all_sent[i][10] = 'every'
                        bool2 = True
                    elif all_sent[i][9] == ne:
                        all_sent[i][9] = "="
                        bool2 = True
                        bool1 = True
                        rule = "DE ~"+ne
                elif j == 49:
                    if all_sent[i][16] == "a":
                        all_sent[i][16] = 'every'
                        bool2 = True
                        rule = "DE ~ a"
                    elif all_sent[i][16] == "every":
                        all_sent[i][16] = 'many'+un
                        bool1 = True
                        bool2 = True
                        rule = "DE ~ every"
                    elif all_sent[i][16] in cat:
                        all_sent[i][16] = 'every'
                        bool2 = True
                        rule = "DE ~ " + all_sent[i][18]
                    elif all_sent[i][15] == ne:
                        all_sent[i][15] = "="
                        bool1 = True
                        bool2 = True
                        rule = "DE ~"+ne
                elif j == 50:
                    if all_sent[i][20] == "a":
                        all_sent[i][20] = 'every'
                        bool2 = True
                        rule = "DE ~ a"
                    elif all_sent[i][20] == "every":
                        all_sent[i][20] = 'many'+un
                        bool1 = True
                        bool2 = True
                        rule = "DE ~ every"
                    elif all_sent[i][20] in cat:
                        all_sent[i][20] = 'every'
                        bool2 = True
                        rule = "DE ~ " + all_sent[i][22]
                elif j == 51:
                    if all_sent[i][24] == "a":
                        all_sent[i][24] = 'every'
                        bool2 = True
                        rule = "DE ~ a"
                    elif all_sent[i][24] == "every":
                        all_sent[i][24] = 'many'+un
                        bool1 = True
                        bool2 = True
                        rule = "DE ~ every"
                    elif all_sent[i][24] in cat:
                        all_sent[i][24] = 'every'
                        bool2 = True
                        rule = "DE ~ " + all_sent[i][26]
                elif j == 52:
                    if all_sent[i][28] == "a":
                        all_sent[i][28] = 'every'
                        bool2 = True
                        rule = "DE ~ a"
                    elif all_sent[i][28] == "every":
                        all_sent[i][28] = 'many'+un
                        bool1 = True
                        bool2 = True
                        rule = "DE ~ every"
                    elif all_sent[i][28] in cat:
                        all_sent[i][28] = 'every'
                        bool2 = True
                        rule = "DE ~ " + all_sent[i][30]
                if bool1:
                    all_sent[i][j] = None
                    all_sent[i][46].remove(j)


        if bool2:
            new_sent = build_sent(all_sent[i])
            newp = name_sent(new_sent)
            dummy = new_sentence2(old_sent,oldp,new_sent,newp,tot_sent,rule,"")
            all_sent[i][0] = new_sent
            all_sent[i][42] = newp
            dummy = new_categories(all_sent[i],words,idf_var,all_sent)

    return


def new_categories(list5,words,idf_var,all_sent,kind=False):

    list2 = list5[46]
    list1 = []

    if not kind:
        for j in list2:
            if list5[j] != None and list5[j] != "":
                list1.append(list5[j])
    else:
        num = [47,3,69,4,55,5,66,67,35,48,59,6,8,9,7,48,12,10,70,13,14,36,60,63,49,15,16,17,18,\
           61,64,50,19,20,21,22,62,65,51,23,24,25,26,52,27,28,\
           29,30,31,32,33,34]
        for j in num:
            if list5[j] != None and list5[j] != "":
                list1.append(list5[j])

    list3 = categorize_words(words,list1,idf_var,all_sent,2)
    if not kind:
        list5[56] = list3[56]
    else:
        return list3


def new_sentence2(old_sent,oldp,new_sent,newp,tot_sent,rule,anc1="",conn = iff,anc2="",anc3=""):

    global sn
    str5 = old_sent + " " + conn + " " + new_sent
    str6 = oldp + " " + conn + " " + newp
    bool1 = check_dimension(tot_sent,1,str5)
    if not bool1:
        sn += 1
        if sn == 8:
            bb = 7
        tot_sent.append([sn,str5,str6,"",rule,anc1,anc2,anc3,""])

def build_app(list1):

    str1 = list1[0]
    for i in range(1,len(list1)):
        str1 += ", " + list1[i]
    return str1

def rel_div(all_sent,m,tot_sent,i,pos,words,idf_var):

    genre = 1
    old_sent = all_sent[m][0]
    oldp = all_sent[m][42]
    list1 = [None] * 80
    str2 = findinlist(all_sent[m][i],pos,0,2)
    if (all_sent[m][i] == 'AS'):
        rule = "RDB"
        a = 14
        if all_sent[m][i] == 'AS':
            anaphora.append(all_sent[m][5])
    elif str2 == 'o':
        rule = "RDC"
        list3 = [None] * 80
        a = 14
        list3[8] = all_sent[m][8]
        list3[3] = all_sent[m][10]
        list3[5] = all_sent[m][5]
        list3[9] = all_sent[m][i]
        list3[10] = all_sent[m][16]
        list3[14] = all_sent[m][18]
        list3 = new_categories(list3,words,idf_var,all_sent,True)
        all_sent.append(list3)
        genre = 2
        str4 = build_sent(list3)
        str4p = name_sent(str4)
        list3[0] = str4
        list3[42] = str4p
    else:
        rule = "RDA"
        a = 5
    if i == 15:
        d = 16
        c = 18
    elif i == 19:
        d = 20
        c = 22

    list1[8] = all_sent[m][8]
    list1[3] = all_sent[m][3]
    list1[5] = all_sent[m][a]
    list1[9] = all_sent[m][i]
    list1[10] = all_sent[m][d]
    list1[14] = all_sent[m][c]
    list1[46] = [200]
    list1[56] = [200]
    all_sent[m][56].remove(100)

    if genre == 1:
        list6 = all_sent[m][46]
        list6.remove(i)
        list6.remove(c)
        if all_sent[m][8] != None:
            list6.remove(8)
        all_sent[m][46] = list6
        all_sent[m][i] = None
        all_sent[m][c] = None
        all_sent[m][d] = None
        all_sent[m][8] = None
    if genre == 1:
        dummy = new_sent_prelim(old_sent,oldp,all_sent,list1,m,rule,tot_sent,1)
    elif genre == 2:
        dummy = new_sent_prelim(old_sent,oldp,all_sent,list1,m,rule,tot_sent,2,list3)




def poss_elim(all_sent,m,i,tot_sent):

    list1 = [None] * 80
    str1 = all_sent[m][i][0]
    list1[5] = str1
    list1[9] = "OWN"
    if i == 69:
        str2 = all_sent[m][5]
    elif i == 70:
        str2 = all_sent[m][14]
    list1[14] = str2
    old_sent = all_sent[m][0]
    oldp = all_sent[m][42]
    all_sent[m][i] = None
    str4 = build_sent(all_sent[m])
    str4p = name_sent(str4)
    str5 = build_sent(list1)
    str5p = name_sent(str5)
    str3 = "(" + str4 + " & " + str5 + ")"
    str3p = "(" + str4p + " & " + str5p + ")"
    list1[0] = str5
    list1[42] = str5p
    list1[46] = [200]
    list1[56] = [200]
    all_sent.append(list1)
    dummy = new_sentence2(old_sent,oldp,str3,str3p,tot_sent,"PNE")

def poss_noun(idf_var,all_sent,m,n,dv_nam,str7):

    global definite
    str1 = all_sent[m][n]
    str1 = str1[:1]
    if str7 == "a":
        str2 = "indefinite"
        new_var = idf_var[0]
        del idf_var[0]
    elif str7 == "the":
        str2 = "definite"
        str9 = findinlist(str1,dv_nam,0,1)
        str10 = findinlist(str9,definite,1,0)
        if str10 == None:
            new_var = idf_var[0]
            del idf_var[0]
            definite.append([new_var,str9])

    str3 = findinlist(str2,dv_nam,1,0)
    all_sent[m][n] = new_var + "'s"
    list1 = [None] * 80
    list1[5] = new_var
    list1[14] = str3
    list1[9] = "J"
    list2 = [None] * 80
    list2[5] = new_var
    list2[14] = str1
    list2[9] = "I"
    str4 = build_sent(list1)
    str4p = name_sent(str4)
    str5 = build_sent(list2)
    str5p = name_sent(str5)
    str6 = str4 + " & " + str5
    str6p = str4p + " & " + str5p
    list3 = [str6,str6p]
    list1[0] = str4
    list1[42] = str4p
    list2[0] = str5
    list2[42] = str5p
    list1[46] = [200]
    list1[56] = [200]
    list2[46] = [200]
    list2[56] = [200]
    all_sent.append(list1)
    all_sent.append(list2)
    return list3

def that(all_sent,m,i,tot_sent,dv_nam,words,idf_var):

    num = [11,1,2,47,3,69,4,55,5,66,67,35,48,59,6,8,9,7,48,12,10,70,13,14,36,60,63,49,15,16,17,18,\
           61,64,50,19,20,21,22,62,65,51,23,24,25,26,52,27,28,\
           29,30,31,32,33,34]

    if m == 10:
        bb = 8
    global embed,prop_var

    list1 = []
    bool1 = False
    list3 = copy.deepcopy(all_sent[m])

    for j in num:
        if j == i:
            bool1 = True
        if list3[j] != None and bool1 and j!=i:
            list1.append(all_sent[m][j])
            list3[j] = None

    list2 = categorize_words(words,list1,idf_var,all_sent,2)
    str1 = build_sent(list2)
    list2[0] = str1
    str1 = remove_outer_paren(str1)
    str3 = str1.replace(" ","")
    g = findposinlist(str3,dv_nam,1)
    if g == -1:
        for z in range(len(idf_var)):
            if idf_var[z] in prop_var:
                new_var = idf_var[z]
                del idf_var[z]
                prop_var.remove(new_var)
                break
        dv_nam.append([new_var,str3,1])
    else:
        new_var = dv_nam[g][0]

    list2[42] = new_var
    list3[i] = None
    if i == 7:
        if list3[5] == 'it'+up:
            list3[5] = new_var
        else:
            list3[14] = new_var
    elif i == 60:
        list3[5] = new_var

    elif i == 61:
        if list3[14] == 'it'+up:
            list3[14] = new_var
        else:
            list3[18] = new_var

    elif i == 62:
        if list3[18] == 'it'+up:
            list3[62] = new_var
        else:
            list3[22] = new_var

    str2 = build_sent(list3)
    list3 = new_categories(list3,words,idf_var,all_sent,True)
    list3[0] = str2
    str2p = name_sent(str2)
    list3[42] = str2p
    all_sent.append(list3)
    embed.append(list2)
    dummy = new_sentence2(all_sent[m][0],all_sent[m][42],str2,str2p,tot_sent,"DE that"+uc)
    return


def scope_uni(all_sent,m,i,kind = ""):

    comma = all_sent[m][39]
    univ = ['every','a','many'+up,'many'+uo,'no']
    if kind == 1:
        if i == 59:
            i = 12
        elif i == 60:
            i = 16
        elif i == 61:
            i = 20
        elif i == 62:
            i = 24
    if comma == None:
        comma = 70
    if all_sent[m][59] != None and all_sent[m][3] in univ:
        if i < comma and i > 3:
            return False
    elif all_sent[m][60] != None and all_sent[m][10] in univ:
        if i < comma and i > 10:
            return False
    elif all_sent[m][61] != None and all_sent[m][17] in univ:
        if i < comma and i > 17:
            return False
    elif all_sent[m][62] != None and all_sent[m][21] in univ:
        if i < comma and i > 21:
            return False
    if i == 13 and all_sent[m][10] in univ:
        return False
    elif all_sent[m][i-1] in univ:
        return False
    return True

def rel_pro(i,m,all_sent,list1,words, idf_var,new_var=""):

    subjrp = ['who','which','that'+us]
    objrp = ['who'+uo,'that'+uo,'which'+uo]
    comma = all_sent[m][39]

    if new_var != "":
        for i in range(59,63):
            if all_sent[m][i] != None:
                break

    if all_sent[m][i] in subjrp:
        srp = True
    else:
        srp = False
    if i == 59:
        list2 = [[8,49],[9,15],[10,16],[13,17],[14,18],[15,19],[18,22],[60,61],[63,64]]
        all_sent[m][59] = None
        if new_var == "":
            list1[5] = all_sent[m][5]
        else:
            list1[5] = new_var
        list1[8] = all_sent[m][8]
        list1[9] = all_sent[m][9]
        list1[14] = all_sent[m][14]

        for j in range(len(list2)):
            k = list2[j][0]
            n = list2[j][1]
            all_sent[m][k] = all_sent[m][n]
            all_sent[m][n] = None

    elif i == 60 and srp:
        list2 = [[8,49],[9,15],[10,16],[13,17],[14,18],[15,19],[18,22]]
        all_sent[m][60] = None
        if new_var == "":
            list1[5] = all_sent[m][14]
        else:
            list1[5] = new_var
        for j in range(len(list2)):
            k = list2[j][0]
            n = list2[j][1]
            list1[k] = all_sent[m][n]
            all_sent[m][n] = None
    elif i == 61:
        a = 22
        c = 26
    elif i == 62:
        a = 30
        c = 34

    list1 = new_categories(list1,words,idf_var,all_sent,True)
    all_sent[m] = new_categories(all_sent[m],words,idf_var,all_sent,True)
    return list1


def new_sent_prelim(old_sent,oldp,all_sent,list1,m,rule,tot_sent,kind=1,list3=[]):

    if list1[8] == neg:
        list1[8] = "~"
    if kind == 2:
        sent2 = build_sent(list3)
        sent2p = name_sent(sent2)
    else:
        sent2 = build_sent(all_sent[m])
        sent2p = name_sent(sent2)
        all_sent[m][0] = sent2
        all_sent[m][42] = sent2p
    sent1 = build_sent(list1)
    sent1p = name_sent(sent1)
    list1[0] = sent1
    list1[42] = sent1p
    list2 = copy.deepcopy(list1)
    all_sent.append(list2)
    if kind == 1 or kind == 2:
        new_sent = "(" + sent1 + " & " + sent2 + ")"
        newp = "(" + sent1p + " & " + sent2p + ")"
        if kind == 1:
            conn = iff
        else:
            conn = conditional
    else:
        new_sent = sent1
        newp = sent1p
        conn = conditional
    dummy = new_sentence2(old_sent,oldp,new_sent,newp,tot_sent,rule,"",conn)

def mult_defnd(list1,def_num):

    for i in range(len(list1)):
        num = list1[i][0]
        if def_num + '12' == num:
            return True
    return False

def indefiniendum(def_num,sent_num,multiple):

    if multiple:
        if sent_num[:-1] == def_num + '1':
            return True
        else:
            return False
    else:
        if sent_num == def_num + '1':
            return True
        else:
            return False

def in_dv(list1,dv_nam):

    if not list1[9] == "=":
        return False
    else:
        bool1 = check_dimension(dv_nam,1,list1[14])
        return bool1

def prop_type(paren_num,gparen_num,paren_conn,gparen_conn,sent_num,def_con):
    # conjunct within idisjunct within antecedent - cda
    # idisjunct within a conjunct within antecedent - dca
    # conjunct within idisjunct within consequent - cdq
    # idisjunct within a conjunct within consequent - dcq
    # conjunct within idisjunct within bic1 - cdb
    # idisjunct within a conjunct within bic1 - dcb
    # conjunct within idisjunct within bic2 - cdf
    # idisjunct within a conjunct within bic2 - dcf

    # conjunct within xdisjunct within antecedent - cxa
    # xdisjunct within a conjunct within antecedent - xca
    # conjunct within xdisjunct within consequent - cxq
    # xdisjunct within a conjunct within consequent - xcq
    # conjunct within xdisjunct within bic1 - cxb
    # xdisjunct within a conjunct within bic1 - xcb
    # conjunct within xdisjunct within bic2 - cxf
    # xdisjunct within a conjunct within bic2 - xcf

    # xdisjunct within antecedent - xa
    # xdisjunct within consequent - xq
    # xdisjunct within bic1 - xb
    # xdisjunct within bic2 - xf
    # conjunct within antecedent - ca
    # conjunct within consequent - cq
    # conjunct within bic1 - cb
    # conjunct within bic2 - cf
    # idisjunct within antecedent - da
    # idisjunct within consequent - dq
    # idisjunct within bic1 - db
    # idisjunct within bic2 - df
    # idisjunct - d
    # xdisjunct - x


    global sn
    str2 = None
    str1 = ""
    if paren_conn == '&' and gparen_conn == xorr:
    # formerly known as dc
        str1 = "d"
        str2 = str(sn) + paren_num
    elif paren_conn == xorr and gparen_conn == iff:
        str1 = 'd'
    if def_con == conditional:
        str1 = "cj"
    elif paren_conn == "&" and gparen_conn == conditional:
        if paren_num[-2] == "1":
            str1 = "an"
            str2 = str(sn) + paren_num
        else:
            str1 = "cn"
            str2 = str(sn) + paren_num
    elif paren_conn == conditional:
        if sent_num[-1] == "1":
            str1 = "an"
            str2 = str(sn) + paren_num
        else:
            str1 = "cn"
            str2 = str(sn) + paren_num
    elif paren_conn == iff:
        str1 = 'bic'
    elif paren_conn == "&" and gparen_conn == iff:
        str1 = 'bic'
    elif paren_conn == xorr and gparen_conn == conditional:
        print "you have not coded for this sentence type yet"
        sys.exit()

    return str1

def add_sent(subj,relat,obj):

    list1 = [None] * 80
    list1[5] = subj
    list1[9] = relat
    list1[14] = obj
    str1 = build_sent(list1)
    list1[0] = str1
    str1p = name_sent(str1)
    list1[42] = str1p
    list1[40] = False
    list1[46] = [200]
    list1[56] = [200]
    return list1

def add_sent2(all_sent,m,k,o,new_var2,words):

    global idf_var
    num2 = [11,1,2,47,3,69,4,55,5,66,67,35,48,59,6,8,9,7,48,12,10,70,13,14,36,60,63,49,15,16,17,18,\
           61,64,50,19,20,21,22,62,65,51,23,24,25,26,52,27,28,\
           29,30,31,32,33,34]
    num = [15,19,23,27,31]
    #list2 is the con sent, list1 is the ant sent
    comma = all_sent[m][39]
    list1 = []
    bool1 = False
    for j in num2:
        if j == k:
            bool1 = True
        if bool1:
            if comma != None:
                if j == comma + 1:
                    break
            if all_sent[m][j] != None and all_sent[m][j] != "":
                list1.append(all_sent[m][j])
                all_sent[m][j] = None
    list1 = categorize_words(words,list1,idf_var,all_sent,2,False)
    all_sent.append(list1)
    list3 = []
    list3 = division("",all_sent,words,3) # division used on 6,7,8
    list2 = []
    if o == 5:
        list2.append(new_var2)
    for i in num2:
        if all_sent[m][i] != None and all_sent[m][i] != "":
            list2.append(all_sent[m][i])
    if o != 5:
        list2 = categorize_words(words,list2,idf_var,all_sent,2,False,new_var2,o)
    else:
        list2 = categorize_words(words,list2,idf_var,all_sent,2,False)
    news = build_sent(list2)
    newp = name_sent(news)
    list2[0] = news
    list2[42] = newp
    all_sent[m] = list2
    all_sent.append(list2)
    for i in range(len(list3)):
        new_sent = build_sent(list3[i])
        newp = name_sent(new_sent)
        list3[i][0] = new_sent
        list3[i][42] = newp
        list3[i][53] = 'an'
        list3[i][40] = False
    return list3



def division(tot_sent, all_sent,words,kind,def_sent=[]):

    global anaphora,idf_var
    univ = ['every']
    list2 = []
    p = len(all_sent) -2
    g = 0
    pos = words[28]
    compound = words[34]

    if kind == 1:
        b = 2
        e = 4
    elif kind == 0:
        b = 0
        e = 3
    elif kind == 3:
        b = 1
        e = 2
    elif kind == 2:
        b = 4
        e = 7
    elif kind == 4:
        b = 7
        e = 8

    for k in range(b,e):
        if k == 0:
            num = [66]
        elif k == 1:
            num = [4,13,17,21,25,33]
        elif k == 2:
            num = [35,36]
        elif k == 3:
            num = [59,60,61,62]
        elif k == 5:
            num = [15,19]
        elif k == 6:
            num = [5,63,64]
        elif k == 4:
            num = [62,61,60,7,69,70] # that elim and poss noun elim combined
        elif k == 7:
            num = [69,70]

        if kind == 3:
            m = p
        else:
            m = -1
        while m < len(all_sent) -1:
            m += 1
            if all_sent[m][46] != "x":
                if m == 1 and k == 3:
                    bb = 8
                old_sent = all_sent[m][0]
                oldp = all_sent[m][42]
                for i in num:
                    list1 = [None] * 80
                    if k == 0 and all_sent[m][i] != None and kind == 0 and \
                            all_sent[m][9] not in compound:
                        all_sent[m][66] = None
                        list1 = [None] * 80
                        list1[5] = all_sent[m][67]
                        all_sent[m][67] = None
                        rule = "DE and" + uc
                        for i in range(6,20):
                            list1[i] = all_sent[m][i]
                        dummy = new_sent_prelim(old_sent,oldp,all_sent,list1,m,rule,tot_sent,1)
                    elif k == 1 and all_sent[m][i] != None:
                        if i == 13:
                            n = 10
                            r = 9
                        else:
                            r = i-2
                            n = i-1
                        if scope_uni(all_sent,m,i) and (kind == 0 or kind == 3):
                            rule = 'ADJ E'
                            print "division used"
                            list17 = copy.deepcopy(all_sent[m])
                            if all_sent[m][8] != None or all_sent[m][12] != None:
                                str7 = "~"
                                all_sent[m][8] = None
                                all_sent[m][12] = None
                            else:
                                str7 = None
                            list1[8] = str7
                            list1[3] = all_sent[m][n]
                            if all_sent[m][r] != "I":
                                list1[5] = all_sent[m][i+1]
                            else:
                                list1[5] = all_sent[m][5]
                            list1[9] = "J"
                            list1[14] = all_sent[m][i]
                            all_sent[m][i] = None
                            if kind == 0:
                                dummy = new_sent_prelim(old_sent,oldp,all_sent,list1,m,rule,tot_sent,1)
                            else:
                                g += 1
                                list2.append(list1)
                                all_sent.append(list1)
                            list17[46] = "x"
                            all_sent.append(list17)
                    elif k == 2 and (kind == 1 or kind == 3) and all_sent[m][i] != None:
                        rule = "CIA"
                        list17 = copy.deepcopy(all_sent[m])
                        if i == 35:
                            j = 5
                        elif i == 36:
                            j = 14
                        elif i == 37:
                            j = 18
                        elif i == 38:
                            j = 22
                        str1 = all_sent[m][j]
                        all_sent[m][j] = all_sent[m][i]
                        list1[14] = str1
                        list1[5] = all_sent[m][i]
                        list1[9] = "I"
                        all_sent[m][i] = None
                        if kind == 3:
                            list2.append(list1)
                            all_sent.append(list1)
                            g += 1
                        else:
                            dummy = new_sent_prelim(old_sent,oldp,all_sent,list1,m,rule,tot_sent,1)
                        list17[46] = "x"
                        all_sent.append(list17)
                    elif k == 3 and kind == 1 and all_sent[m][i] != None and scope_uni(all_sent,m,i,1)\
                            and all_sent[m][i] != 'that'+uc: # formerly uc
                        rule = "DE " + all_sent[m][i]
                        list17 = copy.deepcopy(all_sent[m])
                        dummy = rel_pro(i,m,all_sent,list1)
                        dummy = new_sent_prelim(old_sent,oldp,all_sent,list1,m,rule,tot_sent,1)
                        list17[46] = "x"
                        all_sent.append(list17)
                    elif k == 4 and all_sent[m][i] == 'that'+uc: # formerly uc
                        dummy = that(all_sent,m,i,tot_sent,dv_nam,words,idf_var)
                        break
                    elif k == 4 and (i == 69 or i == 70) and all_sent[m][i] != None:
                        dummy = poss_elim(all_sent,m,i,tot_sent)
                        break
                    elif k == 5 and kind == 2 and all_sent[m][i] != None:
                #right now the only relation we have found that divides by making the object
                # the new subject is AS
                        list17 = copy.deepcopy(all_sent[m])
                        genre = 1
                        if kind == 1:
                            bb = 8

                        str2 = findinlist(all_sent[m][i],pos,0,2)
                        if (all_sent[m][i] == 'AS'):
                            rule = "RDB"
                            a = 14
                            if all_sent[m][i] == 'AS':
                                anaphora.append(all_sent[m][5])
                        elif str2 == 'o':
                            rule = "RDC"
                            list3 = [None] * 80
                            a = 14
                            list3[8] = all_sent[m][8]
                            list3[3] = all_sent[m][10]
                            list3[5] = all_sent[m][5]
                            list3[9] = all_sent[m][i]
                            list3[10] = all_sent[m][16]
                            list3[14] = all_sent[m][18]
                            list2.append(list3)
                            all_sent.append(list3)
                            g += 1
                            genre = 2
                            str4 = build_sent(list3)
                            str4p = name_sent(str4)
                            list3[0] = str4
                            list3[42] = str4p
                        else:
                            rule = "RDA"
                            a = 5
                        if i == 15:
                            d = 16
                            c = 18
                        elif i == 19:
                            d = 20
                            c = 22

                        # elif i == 23:
                        #     a = 22
                        #     c = 26
                        # elif i == 31:
                        #     a = 30
                        #     c = 34
                        if all_sent[m][9] == "EX":
                            bb = 8
                        list1[8] = all_sent[m][8]
                        list1[3] = all_sent[m][3]
                        list1[5] = all_sent[m][a]
                        list1[9] = all_sent[m][i]
                        list1[10] = all_sent[m][d]
                        list1[14] = all_sent[m][c]
                        if genre == 1:
                            all_sent[m][i] = None
                            all_sent[m][c] = None
                            all_sent[m][d] = None
                            all_sent[m][8] = None
                        if genre == 1:
                            dummy = new_sent_prelim(old_sent,oldp,all_sent,list1,m,rule,tot_sent,1)
                        elif genre == 2:
                            dummy = new_sent_prelim(old_sent,oldp,all_sent,list1,m,rule,tot_sent,2,list3)
                            genre = 1
                        list17[46] = "x"
                        all_sent.append(list17)
                    elif k == 6 and kind == 2:
                        str1 = all_sent[m][i]
                        if str1 == 'there':
                            dummy = there(all_sent,m,tot_sent,def_sent)
                            break




    if kind == 3:
        list2.append(all_sent[p+1])
        for i in range(0,g+1):
            del all_sent[-1]
        return list2
    else:
        return


def repl_sign(str3,match_dv,match_type):

    s = findposinmd(str3,match_dv,1)
    s = match_type[s]
    if s == 0:
        return mini_c
    else:
        return idd

def abb_change(list5, already_checked,all_sent,def_sent,i,match_dv,match_type,rename,j,def_con,\
               new_match = [],second=False):

    global never_used,dv_nam
    cap = False
    used_var = []
    spec_prop = ['general','particular','definite','indefinite'] #special properties

    for t in range(len(all_sent)):
        no_match = False
        bool1 = False
        if all_sent[t][9] == "J":
            str1 = findinlist(all_sent[t][14],dv_nam,0,1)
            if str1 in spec_prop:
                bool1 = True
        if bool1:
            pass
        elif t not in already_checked and all_sent[t][46] != "x" and all_sent[t][46] != 'y':
            # if a variable has already been turned into all_sent[t][j] then it cannot
            #happen again since in a definition all variables stand for different things
            if check_dimension(match_dv,1,all_sent[t][j]):
                pass
            else:
                for u in list5:
                    str5 = all_sent[t][u]
                    asent = all_sent[t][0]
                    dsent = def_sent[i][0]
                    if check_dimension(match_dv,1,all_sent[t][u]) and u == i:
                        no_match = True
                    elif all_sent[t][u] == def_sent[i][u]:
                        pass
                    elif u == 8 and (all_sent[t][53] == 'cn' or def_sent[i][53] == 'cn' or def_con == conditional):
                        cap = True
                        pass
                    else:
                        if u == 9:
                            already_checked.append(t)
                        no_match = True
                        break

                if not no_match:
                    match_dv.append([def_sent[i][j],all_sent[t][j]])
                    #cap is for a denied consequent sentence
                    str2 = "(" + def_sent[i][j] + idd + all_sent[t][j] + ")"
                    if cap:
                        str3 = build_sent(def_sent[i])
                        str3 = str3 + l4
                        match_type.append(4)
                        rename.append(str3)
                    else:
                        str2 = str2 + l3
                        match_type.append(3)
                        rename.append(str2)
                        #eee
                    if second:
                        for s in range(len(match_dv)):
                            if match_dv[s][0] == def_sent[i][j]:
                                never_used.append(match_dv[s][1])
                                break
                        new_match.append([def_sent[i][j],all_sent[t][j]])
                    def_sent[i][j] = all_sent[t][j]
                    return False
    return True

def abb_change2(match_dv,match_type,def_sent,i,idf_var,temp_match,j,gen_var,cnnan,rename):

    match_dv.append([def_sent[i][j], idf_var[0]])
    match_type.append(2)
    str1 = "(" + def_sent[i][j] + idd + idf_var[0] + ")"
    str1 = str1 + l2
    temp_match.append([def_sent[i][j], idf_var[0]])
    def_sent[i][j] = idf_var[0]
    gen_var.append(idf_var[0])
    cnnan.append(idf_var[0])
    rename.append(str1)
    del idf_var[0]

def qadj(all_sent,m,j,new_var,kind=0):

    adj_var = all_sent[m][j-1]
    all_sent[m][j-1] = None
    list1 = [None] * 80
    list1[5] = new_var
    list1[9] = "J"
    list1[14] = adj_var
    new_sent = build_sent(list1)
    newp = name_sent(new_sent)
    list1[0] = new_sent
    list1[42] = newp
    list1[46] = [200]
    list1[56] = [200]
    all_sent.append(list1)
    if kind == 1:
        list1[53] = 'an'
        list1[40] = False
    return list1

def cut_def(def_info,definition):

    minn = []
    maxx = 0
    mini = 0
    bool1 = False
    bool2 = False
    bool3 = False
    for i in range(1,len(def_info[0])):
        if "=" in def_info[0][i] and len(def_info[1][i][0]) == 2 and def_info[1][i][1] == "" \
            or mini_e in def_info[0][i] and len(def_info[1][i][0]) == 2 and def_info[1][i][1] == "":
            minn.append(def_info[1][i][0])
            bool2 = True
    h = 10
    if not bool2:
        return definition

    if len(minn) == 1 and minn[0] != "11":
        maxx = minn[0]
    elif len(minn) == 1 and minn[0] == "11":
        mini = 0
    else:
        for i in range(0,len(minn)):

            g = minn[i]
            h += 1
            hh = str(h)
            if i == 0 and minn[i] != "11":
                maxx = minn[i]
                bool3 = True
                break
            if i == 1 and g != hh and minn[0] != "11":
                mini = 0
            if g != hh:
                mini  = str(minn[i-1])
                bool1 = True
            if bool1:
                maxx = minn[i]
                bool3 = True
                break
    if not bool3 and len(minn)>1:
        m = len(definition) + 2
        mini = minn[-1]
    elif maxx == 0 and len(minn) == 1:
        m = len(definition) + 2
    else:
        j = findposinlist(maxx,def_info[1],0)
        m = definition.find(def_info[0][j])
    if mini != 0:
        j = findposinlist(mini,def_info[1],0)
        k = definition.find(def_info[0][j])
        k += len(def_info[0][j])
    elif mini == 0 and minn[0] == "11":
        j = findposinlist("11",def_info[1],0)
        k = len(def_info[0][j])
    else:
        k = -2

    definition = definition[k+2:m-2]
    definition = definition.strip()
    definition = remove_outer_paren(definition)

    return definition


def def_rn(defined,al_def,definition, definiendum,e, tot_sent,  dv_nam, idf_var, \
           words,rep_rel,all_sent,m,prop_con,p_sent,kind = "",k=0,circ = ""):
    # def_rn = definition rename
    # this function renames the variables in a definition
    #end0
    #match_type 0 = instantiation
    #match_type 1 = idd, constants, 2 = unused var, 3 = already has relation
    # 4 = negated consequent


    global sn,plural_c,definite2,definite,anaphora,ind_var,gen_var,def_used
    b = time.time()
    #this is for those determinatives which have negations in their definitions where
    #the sentences has an R variable
    identical_det = ["only","anything_except","anyone_except","many"+un,'no']
    if definiendum == "property"+un:
        bb = 7
    if definiendum not in def_used and not definiendum.isupper():
        def_used.append(definiendum)

    if definiendum in identical_det:
        ident_det = True
    else:
        ident_det = False
    match_dv = []
    match_type = []
    new_var = []
    rule = ""
    taken_out = []
    x = findposinlist(definiendum,rep_rel,0)
    if x > -1:
        rr_var = rep_rel[x][1]
    else:
        rr_var = 0
    detached = [conditional,iff,xorr,idisj]
    #if bool1 is false then there is a series of conjuncts that need to be removed from
    # the definition
    temp_ad = []
    ad = findposinmd(definiendum,already_defined,0)
    if ad == -1:
        already_df = False
        def_info = find_sentences(definition)
        temp_ad.append(definiendum)
        temp_ad.append(def_info)
    else:
        already_df = True
        def_info = already_defined[ad][1]

    def_loc = def_info[7]
    def_num = def_info[4][def_loc][0]
    dfn_num = def_num + "2"
    poss_str = ""
    ld = len(def_num)
    cnnan = []
    prop_con = []
    list1 = id_def(def_info,words,idf_var,all_sent)
    dv = list1[0]
    for i in range(len(list1[2])):
        if [list1[2][i],list1[3][i],list1[4][i]] not in prop_con:
            prop_con.append([list1[2][i],list1[3][i],list1[4][i]])
    # g = len(prop_con) - len(list1)
    # for i in range(len(list1),g,-1):
    #     prop_con[i].append(1)

    odef = all_sent[m][0]
    # we now must match the definite variables in the definition to the definite variables
    # already assigned
    list1 = []
    syn_det = ["no_one_except","any"+un]
    for i in range(len(dv)):
        temp_str = dv[i][1]
        for j in range(len(dv_nam)):
            dvn_temp = dv_nam[j][1]
            if dvn_temp == temp_str:
                telist7 = [dv[i][0],dv_nam[j][0]]
                if telist7 not in match_dv:
                    match_dv.append(telist7)
                    match_type.append(1)
                    break
        else:
            if dv[i][0] not in idf_var:
                telist7 = [dv[i][0], idf_var[0]]
                match_dv.append(telist7)
                match_type.append(2)
                list1.append([idf_var[0], temp_str])
                new_var.append(idf_var[0])
                del idf_var[0]
            else:
                telist7 = [dv[i][0], temp_str]
                list1.append(telist7)
                match_dv.append([dv[i][0],dv[i][0]])
                idf_var.remove(dv[i][0])
                match_type.append(9)
    dv_nam += list1

    if kind == 'pronoun':
        match_type.append(9)
        if definiendum != 'i':
            str1 = findinlist(definiendum,dv_nam,1,0)
            if str1 == None:
                all_sent[m][k] = idf_var[0]
                match_dv.append(["c",idf_var[0]])
                dv_nam.append([idf_var[0],definiendum])
                new_var.append(idf_var[0])
                del idf_var[0]
            else:
                all_sent[m][k] = str1
                match_dv.append(["c'",str1])
        else:
            match_dv.append(['i','i'])
        # when constructing definitions of personal pronouns or of determinatives the object of the IG relation
        # must be b and the subject must be z
    elif kind == 'determinative' or kind == 'poss pro' or kind == 'proper name possessive':
        if k == 10:
            j = 14
        else:
            j = k + 2
        ovar = all_sent[m][j]
        match_type.append(9)
        if kind == "proper name possessive":
            match_dv.append(["b",all_sent[m][k]])
        elif definiendum == "its" + ua or definiendum == "its" + ub: # its is slightly weird because it almost never exists
        # in the subject position
            match_dv.append(["c",all_sent[m][14]])
            all_sent[m][k] = ""
            match_dv.append(["b",all_sent[m][5]])
            match_type.append(9)
        else:
            all_sent[m][k] = ""
            match_dv.append(["b",all_sent[m][j]])
        if definiendum == 'the' or definiendum == 'that'+ud:
            str1 = all_sent[m][j]
            str3 = findinlist(str1,dv_nam,0,1)
            str2 = findinlist(str3,definite,1,0)
            match_type.append(9)
            if str2 == None:
                match_dv.append(["z",idf_var[0]])
                definite.append([idf_var[0],str3])
                if kind != 'proper name possessive':
                    all_sent[m][j] = idf_var[0]
                else:
                    all_sent[m][k] = idf_var[0]
                new_var.append(idf_var[0])
                new_var2 = idf_var[0]
                del idf_var[0]
            else:
                all_sent[m][j] = str2
                match_dv.append(["z'",str2])
                new_var2 = str2
        elif definiendum not in syn_det:
            match_type.append(9)
            new_var2 = idf_var[0]
            all_sent[m][j] = idf_var[0]
            match_dv.append(["z",idf_var[0]])
            new_var.append(idf_var[0])
            del idf_var[0]
        list1 = []
        if j == 14 and all_sent[m][70] != None and kind != 'proper name possessive':
            list1 = poss_noun(idf_var,all_sent,m,70,dv_nam,definiendum)
        if j == 5 and all_sent[m][69] != None and kind != 'proper name possessive':
            list1 = poss_noun(idf_var,all_sent,m,69,dv_nam,definiendum)
        if list1 != []:
            poss_str = list1[0]
            poss_strp = list1[1]
        if all_sent[m][45] == 1:
            str5 = findinlist(ovar,dv_nam,0,1)
            if str5 in tagged_nouns:
                tagged_nouns2.append([all_sent[m][j],str5])

    sdefinition = def_info[8]
    def_sent = []
    rename = []
    not_many = False
    first_in_def = [def_num+"1",def_num + "11"]
    temp_te = []
    heir_num = []
    spec_var = ['y','x','w']
    rule_found = False
    univ = ['every','no']
    idfq = ['a','many'+up,'many'+us,'many'+ud,"a"+ua]
    sent_uniq1 = []
    bool1 = False
    def_con = ""
    max_num = 0

    if definiendum in univ or definiendum in idfq:
        if definiendum in idfq or definiendum in univ:
            adj_var = None
            if all_sent[m][j-1] != None:
                list1 = qadj(all_sent,m,j,new_var2,0)
                sent_uniq1.append(list1)
        if definiendum in univ:
            if k == 3 and all_sent[m][59] != None:
                bool1 = True
                all_sent[m][59] = None
            elif k == 10 and all_sent[m][60] != None:
                bool1 = True
                all_sent[m][60] = None
            elif k == 16 and all_sent[m][61] != None:
                bool1 = True
                all_sent[m][61] = None
            elif k == 20 and all_sent[m][62] != None:
                bool1 = True
                all_sent[m][62] = None
            if bool1:
                list1 = add_sent2(all_sent,m,k,j,new_var2,words)
                for i in range(len(list1)):
                    sent_uniq1.append(list1[i])
            if all_sent[m][15] != None:
                new_relat = all_sent[m][9]
                new_obj = all_sent[m][14]
                all_sent[m][9] = all_sent[m][15]
                all_sent[m][15] = None
                all_sent[m][10] = all_sent[m][16]
                all_sent[m][16] = None
                all_sent[m][14] = all_sent[m][18]
                all_sent[m][18] = None
                # existence redundancy is done here
                if new_relat != 'EX':
                    list1 = add_sent(new_var2,new_relat,new_obj)
                    sent_uniq1.append(list1)

    if kind == "determinative" or kind == "pronoun" or kind == 'AS' or kind == 'poss pro':
        rule = "DE " + definiendum
        rule_found = True
    elif kind == "proper name possessive":
        rule = "PNP"
        kind = "determinative"
        rule_found = True
    #as we loop through the sentences they must be in the definition which is the point of n


    z = -1
    for i in range(len(def_info[0])):
        if i == 21:
            bb = 8
        n = def_info[4][i][0][:ld]
        if def_info[4][i][1] == iff and not rule_found:
            rule = "DF " + definiendum
            rule_found = True
            def_con = iff
            if already_df and kind == "":
                break

        elif def_info[4][i][1] == conditional and not rule_found:
            def_con = conditional
            rule = "NC " + definiendum
            rule_found = True
            if already_df and kind == "":
                break
        bool3 = False
        if "=" in def_info[3][i] and n != def_num:
            bool3 = True
        if os(def_info[3][i]) == True and not bool3:
            if not already_df:
                temp_str = space_words(def_info[3][i])
                temp_str = temp_str.replace("(","")
                temp_str = temp_str.replace(")","")
                telist7 = categorize_words(words,temp_str,idf_var,all_sent,1,False,"","",taken_out)
                if kind != "":
                    telist8 = copy.deepcopy(telist7)
                    temp_te.append(telist8)
            else:
                z += 1
                telist7 = copy.deepcopy(already_defined[ad][2][z])


            bool1 = False
            bool2 = False
            bb = 8
            # if bb == 9:
            #     pass
            if kind == 'AS' and telist7[9] == 'R':
                telist7[9] = anaphora[0]
                if i == 6:
                    telist7[5] = anaphora[1]
                str1 = build_sent(telist7)
            elif kind != "" and kind != 'R' and telist7[9] == "R":
                telist7[42] = True
                if telist7[3] != None:
                    temp_det = telist7[3]
                    has_detrm = True
                else:
                    has_detrm = False
                if ident_det:
                    neg1 = telist7[8]
                    if telist7[5] == 'b':
                        bool1 = True
                    if telist7[5] == 'z':
                        bool2 = True
                str2 = ''

                for p in range(2,80):
        # if the variable in the original definition is z,y,x,w then that must
        # go into the new definition in its proper place
                    if p == 46:
                        bb = 8
                    if telist7[p] in spec_var:
                        str2 = idf_var[0]
                        spec_var.remove(telist7[p])
                        match_dv.append([telist7[p],str2])
                        match_type.append(9)
                        del idf_var[0]
                    if p == j and str2 != "" and str2 != None:
                        telist7[p] = str2
                    elif p != 46 and p != 56:
                        telist7[p] = all_sent[m][p]
                        list1.append(all_sent[m][p])



                #not many is the one negated determinative which is defined in this way and its
                #negation is removed in the definiens
                if definiendum == 'not' + ui + ' ' + 'many' + ud:
                    if all_sent[m][8] == 'not' + ui and def_info[4][i][0] not in first_in_def:
                        telist7[8] = ""
                        telist7[k] = 'exactly_one'
                        str2 = findinlist(ovar,plural_c,0,1)
                        telist7[j] = str2
                    if def_info[4][i][0] in first_in_def:
                        telist7[j] = ovar
                        if all_sent[m][47] == 'not' + ui:
                            telist7[47] = 'not' + ui
                        elif all_sent[m][8] == 'not' + ui:
                            telist7[8] = 'not' + ui
                            telist7[47] = None
                            not_many = True
        #just in case the list has a tagged noun
                telist7[45] = all_sent[m][45]
        # for the determinatives which have negations in their definition then we need
        # to do something special
                list1 = new_categories(telist7,words,idf_var,all_sent,True)
                telist7[46] = list1[46]
                telist7[56] = list1[56]

                if ident_det:
                    if j == 5 or j == 14:
                        telist7[8] = neg1
                    elif j == 18 and neg1 == "~":
                        telist7[49] = neg1
                    elif j == 22 and neg1 == "~":
                        telist7[50] = neg1
                    elif j == 26 and neg1 == "~":
                        telist7[51] = neg1
        # the determinatives which have an identity statement in them behave differently
        # these are 'only' and 'anything except'
                if bool1:
                    telist7[j] = ovar
                if has_detrm:
                    telist7[k] = temp_det
                if definiendum == 'everything_except' + up and i == 13:
                    telist7[8] = "~"
                    match_type.append(9)
                    if 'y' in idf_var:
                        telist7[j] = 'y'
                        match_dv.append(['y','y'])
                    else:
                        telist7[j] = idf_var[0]
                        match_dv.append(['y',idf_var[0]])
                        new_var.append(idf_var[0])
                        del idf_var[0]
                if (definiendum == 'all' and i == 4) or (definiendum == 'only' + up and i==9):
                    telist7[j] = 'd'
                    telist7[42] = None

                if definiendum == 'any' + un and i == 2:
                    telist7[10] = "every"
                if bool2:
                    str2 = findinlist("z",match_dv,0,1)
                    telist7[j] = str2
        # if the sentence is first then we must restor the definiendum to it
                if def_info[4][i][0] in first_in_def and not not_many:
                    telist7[k] = definiendum
        # what this does is it puts the original variable back into the definiendum
                    if kind != "pronoun":
                        telist7[j] = ovar
                str1 = build_sent(telist7)
                sdefinition = sdefinition.replace(def_info[3][i],str1)
            else:
                str1 = build_sent(telist7)
# if a def sent is part of the defiendum then it does not have to be added to the all
# all_sent list
            if def_info[4][i][0][:-1] in first_in_def or def_info[4][i][0] in first_in_def:
                telist7[40] = True
            else:
                telist7[40] = False
            telist7[0] = str1
            sent_num = def_info[4][i][0]
            paren_num = def_info[4][i][0][:-1]
            gparen_num = def_info[4][i][0][:-2]
            paren_conn = findinlist(paren_num,def_info[4],0,1)
            gparen_conn = findinlist(gparen_num,def_info[4],0,1)

            #the dfn_num (definiens number) will always have three digits
            # any sentence that is not a conjunct in the definiens should not be defined

            if sent_num[:3] == dfn_num:
                if gparen_num != def_num and gparen_conn in detached:
                    if gparen_conn == conditional and paren_num[-2] == "1":
                        telist7[46] = [200]
                    elif gparen_conn == iff:
                        telist7[46] = [200]
                elif paren_num != def_num and paren_conn in detached:
                    if sent_num[-1] == "1" and paren_conn == conditional:
                        telist7[46] = [200]
                    elif paren_conn == iff:
                        telist7[46] = [200]

            telist7[68] = sent_num
            if max_num == 0:
                max_num = len(sent_num)
            elif len(sent_num) > max_num:
                max_num = len(sent_num)

            # cnn_type = prop_type(paren_num,gparen_num,paren_conn,gparen_conn,sent_num,def_con)
            # #if the cnn_type is 'an' or bic1 or bic2 then we need not define it
            # if cnn_type == 'an' or cnn_type == 'bic' or cnn_type == 'cn':
            #      telist7[46] = 'x'

            if paren_conn == None:
                bb = 7

            telist7[54] = str(sn) + "." + str(paren_num)
            telist7[44] = def_info[6][i][1]
            heir_num.append(def_info[4][i][0])
            for s in range(0,3):
                telist7.append(None)
            def_sent.append(telist7)
    if not already_df:
        if kind == "":
            list9 = copy.deepcopy(def_sent)
            temp_ad.append(list9)
            tem_he_num = copy.deepcopy(heir_num)
            temp_ad.append(tem_he_num)
        else:
            temp_ad.append(temp_te)
        list10 = copy.deepcopy(temp_ad)
        already_defined.append(list10)

    if already_df and kind == "":
        def_sent = copy.deepcopy(already_defined[ad][2])
        heir_num = copy.deepcopy(already_defined[ad][3])
    #ffd
    # the purpose of this is that the subject of the definiendum must match the subject
    # of the osent to be defined.  if its a relation then the object must also match
    if (kind == "" or kind == "R" or kind == 'AS'):
        mvar = []
        bool1 = mult_defnd(def_info[4],def_num)
        for i in range(len(def_sent)):
            bool2 = indefiniendum(def_num,heir_num[i],bool1)
            if bool2:
                if heir_num[i] in first_in_def:
                    match_dv.append([def_sent[i][5],all_sent[m][5]])
                    match_type.append(0)
                    if kind == "R" or kind == 'AS':
                        match_dv.append([def_sent[i][14],all_sent[m][14]])
                        match_type.append(0)
                        if bool1:
                            break
                else:
                    relat = def_sent[i][9]
                    oobj = def_sent[i][14]
                    nobj = findinlist(oobj,match_dv,0,1)
                    for j in range(len(all_sent)):
                        if all_sent[j][9] == relat and all_sent[j][14] == nobj:
                            match_dv.append([def_sent[i][5],all_sent[j][5]])
                            match_type.append(0)
                            break


    #if the definiendum is many-o then its object variable needs to be matched
    if definiendum == 'many' + uo:
        match_dv.append(['c',all_sent[m][14]])
        match_type.append(9)
    num = [5,14]
    num2 = [5,14,18,22,26,30,34]
    num3 = [9,14,8]
    num4 = [9,5,8]
    # the point of the exception list is that we do not change certain sentences in the
    # definiens if we are analyzing a pronoun or determinative
    str2 = ""
    already_checked2 = []
    cap = False
    unmatched = []
    temp_match = []

    for i in range(len(def_sent)):
        e = def_sent[i][68]
        if len(e) < max_num:
            e = str(e)
            f = max_num - len(e)
            g = "0" * f
            e += g
            # e = int(e)
            def_sent[i][68] = e

    if definiendum == 'my':
        bb = 8
    #end1
    #we sort the def_sent so that they appear in the same order as the definiendum here
    def_sent = sorted(def_sent, key = operator.itemgetter(68))
    prop_pos = [] # positions of propositional constants, if any
    unmat_var = []

    for i in range(len(def_sent)):
        if i == 3:
            bb = 8
        if def_sent[i][42] == None:
            for j in num2:
                temp_str = def_sent[i][j]
                isvar = isvariable(temp_str)
                if isvar:
                    if j > 17:
                        bb = 8
                    if temp_str != None:
                        str3 = findinlist(temp_str,match_dv,0,1)
                        if temp_str == "i":
                            pass
                        elif str3 != None and temp_str != str3:
                            already_checked2.append([i,j])
                            def_sent[i][j] = str3
                            str4 = repl_sign(str3,match_dv,match_type)
                            str2 = '(' + temp_str + str4 + str3 + ')'
                            if str2 not in rename and str2 != "":
                                rename.append(str2)
                            str2 = ""
                        # elif temp_str in unmat_var:
                        #     unmatched.append([i,j])
                        elif check_dimension(prop_con,0,temp_str):
                            if def_sent[i][2] != mini_e:
                                prop_pos.append([i,j])
                        elif temp_str == str3:
                            already_checked2.append([i,j])
                        elif def_sent[i][j] == rr_var:
                            dummy = abb_change2(match_dv,match_type,def_sent,i,idf_var,temp_match,j,gen_var,\
                                    cnnan,rename)
                        else:
                            # here we check to see if it has a plural form
                            # if j == 14 and def_sent[i][9] == 'OFP':
                            #     g = findposinlist(def_sent[i][5],plural_c,1)
                            #     if g > -1:
                            #         match_dv.append([def_sent[i][j],plural_c[g][0]])
                            #         match_type.append(9)
                            #         def_sent[i][j] = plural_c[g][0]

                            already_checked = []
                            if j == 5:
                                list5 = num3
                            else:
                                list5 = num4
                            no_match = abb_change(list5, already_checked,all_sent,\
                                def_sent,i,match_dv,match_type,rename,j,def_con)
                            if not no_match and j == 14 and unmatched != []:
                                dummy = abb_change(num3, already_checked,all_sent,\
                                    def_sent,i,match_dv,match_type,rename,j,def_con)
                            elif no_match:
                                unmatched.append([i,j])
                                # unmat_var.append(def_sent[i][j])
    if unmatched != []:
        new_match = []
        unmatched2 = []
        already_checked = []
        for k in range(len(unmatched)):
            if k == 5:
                bb = 8
            i = unmatched[k][0]
            j = unmatched[k][1]
            if j == 5:
                # sometimes an unmatched variable will appear twice and the second time
                # it needs to take the same variable as it did the first time
                str3 = findinlist(def_sent[i][j],match_dv,0,1)
                if str3 != None:
                    def_sent[i][j] = str3
                else:
                    #yyy
                    no_match = abb_change(num3, already_checked,all_sent,\
                        def_sent,i,match_dv,match_type,rename,5,def_con,new_match,True)
                    if no_match:
                        temp_str = def_sent[i][j]
                        str3 = findinlist(temp_str,match_dv,0,1)
                        if str3 != None and temp_str != str3:
                            def_sent[i][j] = str3
                            print "rare rename rule used"
                            str2 = '(' + temp_str + idd + str3 + ')'
                            str2 = str2 + l2
                            if str2 not in rename and str2 != "":
                                rename.append(str2)
                            str2 = ""
                        elif temp_str == str3:
                            pass
                        else:
                            dummy = abb_change2(match_dv,match_type,def_sent,i,idf_var,temp_match,j,\
                                    gen_var,cnnan,rename)
                            unmatched2.append([i,j])
            else:
                temp_str = def_sent[i][j]
                str3 = findinlist(temp_str,match_dv,0,1)
                if str3 != None and temp_str != str3:
                    def_sent[i][j] = str3
                    # str4 = repl_sign(str3,match_dv,match_type)
                    str2 = '(' + temp_str + idd + str3 + ')'
                    str2 = str2 + l2
                    if str2 not in rename and str2 != "":
                        rename.append(str2)
                    str2 = ""
                else:
                    if def_sent[i][j] not in taken_out:
                        dummy = abb_change2(match_dv,match_type,def_sent,i,idf_var,temp_match,j,gen_var,cnnan,rename)
                    unmatched2.append([i,j])
                    gen_var.append(def_sent[i][j])

        if unmatched2 != [] and new_match != []:
            for k in range(len(unmatched2)):
                i = unmatched2[k][0]
                j = unmatched2[k][1]
                temp_str = def_sent[i][j]
                str3 = findinlist(temp_str,temp_match,1,0)
                if str3 != None:
                    str4 = findinlist(str3,new_match,0,1)
                    if str4 != None:
                        print "unmatched2 used"
                        str2 = '(' + str3 + idd + str4 + ')'
                        if str2 not in rename and str2 != "":
                            rename.append(str2)
                            str2 = ""
                        if def_sent[i][j] in gen_var:
                            gen_var.remove(def_sent[i][j])
                            cnnan.remove(def_sent[i][j])
                            never_used.append(def_sent[i][j])
                        def_sent[i][j] = str4

    if prop_con != [] and prop_pos != []: # here we replace propositional constants
        match_dv2 = []
        num = [5,14]
        done = []
        bool1 = False
        bool2 = False
        for i in range(len(prop_con)):
            for j in num:
                str1 = prop_con[i][2][j]
                g = findposinlist(str1,match_dv,0)
                if g > -1:
                    bool1 = True
                    prop_con[i][2][j] = match_dv[g][1]
            if bool1:
                str1 = build_sent(prop_con[i][2])
                prop_con[i][2][0] = str1
                str1 = str1.replace(" ","")
                str1 = remove_outer_paren(str1)
                prop_con[i][1] = str1
                g = findposinlist(str1,dv_nam,1)
                str3 = prop_con[i][0]
                if g > -1:
                    str2 = dv_nam[g][0]
                    prop_con[i][0] = str2
                    match_dv2.append([str3,prop_con[i][0]])
                    str4 = "(" + str3 + idd + prop_con[i][0] + ")"
                    rename.append(str4)
                g = findposinlist(prop_con[i][0],dv_nam,1)
                if g > -1:
                    bool2 = True
                    str3 =idf_var[0]
                    del idf_var[0]
                    match_dv2.append([prop_con[i][0],str3])
                    str4 = "(" + prop_con[i][0] + idd + str3 + ")"
                    rename.append(str4)
                else:
                    g = findposinlist(str3,dv_nam,0)
                    if g > -1:
                        str5 = dv_nam[g][1]
                        if str5 != str1:
                            str3 =idf_var[0]
                            del idf_var[0]
                            match_dv2.append([prop_con[i][0],str3])
                            str4 = "(" + prop_con[i][0] + idd + str3 + ")"
                            rename.append(str4)

                dv_nam.append([str3,str1,1])
                prop_con[i][0] = str3
                done.append(i)

        if match_dv2 != []:
            for i in range(len(prop_pos)):
                bool1 = False
                j = prop_pos[i][0]
                k = prop_pos[i][1]
                str1 = def_sent[j][k]
                str2 = findinlist(str1,match_dv2,0,1)
                def_sent[j][k] = str2

    #jjj
    no_var_ch = var_ch(match_dv)
    if no_var_ch:
        rule = rule[0] + "E" + rule[2:]
        sn += 1


    # we now replace the skel string with the new sentences, to get the true definition
    skel_string = def_info[5]
    # skel_wid = def_info[8]
    skel_string2 = def_info[5]
    first_sent_found = False
    bool1 = False
    #ddd
    for i in range(len(def_sent)):
        str2 = build_sent(def_sent[i])
        def_sent[i][0] = str2
        if definiendum == 'i': # this prevents 'i' from being defined multi times
            def_sent[i][43] = "x"
    #because the definiendum for universal quantifiers is somewhat hard to get we
    # we just use the original sentence to be defined
    # also right now we are removing the negative sign from the o sent, though
    # in the future things might be more complicated than this
        if def_sent[i][40] and kind != "AS" and not first_sent_found:
            str2 = odef
            first_sent_found = True
            if kind != 'determinative' and kind != 'pronoun' and "~" in str2:
                if " ~" in str2:
                    str2 = str2.replace(" ~","")
                else:
                    str2 = str2.replace("~","")
                d = findposinlist(odef,all_sent,0)
                list1 = copy.deepcopy(all_sent[d])
                list1[8] = ""
                list1[0] = str2
                list1[43] = "x"
                bool1 = True
                all_sent.append(list1)



        elif kind == "AS":
            str2 = def_sent[i][0]
        skel_string = skel_string.replace(def_sent[i][44], str2)
        str1 = name_sent(str2)
        def_sent[i][42] = str1
        skel_string2 = skel_string2.replace(def_sent[i][44], str1)
        if bool1:
            list1[42] = str1
            bool1 = False

    #this algorithm makes sure the exact same definition does not appear twice even after
    #replacements have been made
    str1 = skel_string.replace(" ","")
    if str1 in al_def:
        return
    else:
        al_def.append(str1)

    if sent_uniq1 != [] or poss_str != "":
        str4 = ""
        str4p = ""
        if sent_uniq1 != []:
            for i in range(len(sent_uniq1)):
                if str4 == "":
                    str4 = sent_uniq1[i][0]
                    str4p = sent_uniq1[i][42]
                else:
                    str4 += " & " + sent_uniq1[i][0]
                    str4p += " & " + sent_uniq1[i][42]
                def_sent.append(sent_uniq1[i])
        else:
            str4 = poss_str
            str4p = poss_strp
        str4 += " & "
        str4p += " & "
        g = skel_string.find(iff)
        h = skel_string.find(conditional)
        if h == -1:
            skel_string = skel_string[:g+3] + str4 + skel_string[g+3:]
        else:
            skel_string = skel_string[:g + 4] + "(" + str4 + skel_string[g + 4:h - 1] + ") " + skel_string[h:]
            # skel_string = skel_string[:g+3] + "(" + str4 + skel_string[g+3:h-1] + ") " + skel_string[h:]
            # when we change the definition of 'every' we have to use the second
            # string

        g = skel_string2.find(iff)
        h = skel_string2.find(conditional)
        if poss_str != "":
            skel_string2 = skel_string2[:g+3] + str4p + skel_string2[g+3:h] + skel_string2[h:]
        elif h == -1:
            skel_string2 = skel_string2[:g+4] + str4p + skel_string2[g+4:]
        else:
            skel_string2 = skel_string2[:g + 4] + "(" + str4p + skel_string2[g + 4:h - 1] + ")" + skel_string2[h - 1:]
           # skel_string2 = skel_string2[:g+3] + "(" + str4p + skel_string2[g+3:h-1] + ")" + skel_string2[h-1:]

    str3 = skel_string2
    if kind == "" or kind == 'R':
        sn += 1
        definition = remove_outer_paren(definition)
        if rename != []:
            d = findposinlist(definiendum,defined,0)
            if d == -1:
                tot_sent.append([sn, definition, "","", rule,"","","",""])
                defined.append([definiendum,sn])
                anc1 = sn
            else:
                anc1 = defined[d][1]
            str2 = build_sent_list(rename)
            if rule[:2] != "DE":
                rule = "SUB"
            else:
                rule += " " + definiendum
            if str2 != None:
                sn += 1
                tot_sent.append([sn, str2, "","", 'RN',"","","",""])
            bool1 = check_dimension(tot_sent,1,skel_string)
            if not bool1:
                sn += 1
                tot_sent.append([sn, skel_string, str3,"", rule,anc1,sn-1,"",""])
        else:
            d = findposinlist(definiendum,defined,0)
            if d == -1:
                tot_sent.append([sn, definition, skel_string2,"", rule,"","","",""])
                defined.append([definiendum,sn])
            else:
                defined.append([definiendum,sn])

    else:
        bool1 = check_dimension(tot_sent,1,skel_string)
        if not bool1:
            sn += 1
            tot_sent.append([sn, skel_string, str3,"", rule,"","","",""])


    list1 = []
    num = [5,14,15,18,26,30]
    def_var = findinlist("definite",dv_nam,1,0)
    indef = findinlist("indefinite",dv_nam,1,0)
    gen = findinlist("general",dv_nam,1,0)

    for i in range(len(def_sent)):
        if def_sent[i][9] == "J":
            if def_sent[i][14] == def_var:
                if def_sent[i][5] in gen_var:
                    gen_var.remove(def_sent[i][5])
                if def_sent[i][5] not in definite2:
                    definite2.append(def_sent[i][5])
            elif def_sent[i][14] == indef:
                if def_sent[i][5] in gen_var:
                    gen_var.remove(def_sent[i][5])
                if def_sent[i][5] not in ind_var:
                    ind_var.append(def_sent[i][5])
            elif def_sent[i][14] == gen:
                if def_sent[i][5] not in gen_var:
                    gen_var.append(def_sent[i][5])
                    cnnan.append(def_sent[i][5])

        # the indefinite articles have special negations
        for n in num:
            if def_sent[i][n] in new_var:
                new_var.remove(def_sent[i][n])
        if definiendum == "many" + un:
            if not def_sent[i][40] and def_sent[i][8] == "~":
                def_sent[i] = not_a(def_sent[i],k,tot_sent,all_sent)



        bool1 = check_dimension(all_sent,0,def_sent[i][0])
        bool2 = in_dv(def_sent[i],dv_nam)
        # it used to be that the sentence had to not have a plural which means
        # that 41 had to be false

        if bool1 == False and bool2 == False and i != 0:
            if definiendum != "i":
                def_sent[i][43] = circ
            if cnnan != []:
                bb = 8
            all_sent.append(def_sent[i])

    if len(list1) > 1:
        str1 = ant_var(list1)
        if len(list1) > 1:
            list1[0][58] = str1
        else:
            list1[58] = str1
        ant_cond.append(list1)
    elif len(list1) == 1:
        list1[0][58] = list1[0][5]
        ant_cond.append(list1)

    c = time.time()
    d = c - b
    #end2
    return

def var_ch(match_dv):

    for i in range(len(match_dv)):
        if match_dv[i][0] != match_dv[i][1]:
            return False
    return True

def ant_var(list1):

    list2 = []
    num = [5,14,18,22,26,30,34]
    num2 = [5,14]
    for i in range(len(list1)):
        for j in num2:
            if list1[i][j] != None:
                list2.append(list1[i][j])

    for i in range(len(list2)):
        g = list2.count(list2[i])
        if g > 1:
            return list2[i]
    print 'your method for finding the antecedent variable is not working'
    sys.exit()


def not_a(list1,k,tot_sent,all_sent):

    num = [10,16,20,24]


    for i in num:
        if i > k and (list1[i] == "a" or list1[i] == "a" + ua):
            list2 = copy.deepcopy(list1)
            if list1[i] == "a":
                rule = "DE not a"
            else:
                rule = "DE not a" + ua
            list2[i] = 'every'
            str1 = build_sent(list2)
            str1p = name_sent(str1)
            list2[0] = str1
            list2[42] = str1p
            dummy = new_sentence2(list1[0],list1[42],str1,str1p,tot_sent,rule)
            list1[46] = [200]
            all_sent.append(list1)
            return list2
    return list1

def categorize_words(words,str2,idf_var,all_sent,kind=1,first=False,snoun="",\
                snum="",taken_out=[]):

    global sn
    global anaphora
    global never_used
    has_plural = False
    bool1 = False

    if kind == 0:
        list1 = str2
        osent = str2[-3]
        prp = str2[-2]
        g = len(list1) - 3
        sent_type = str2[-1]
    elif kind == 1:
        osent = copy.copy(str2)
        str2 = str2.strip()
        list1 = str2.split(' ')
        g = len(list1)
        prp = None
        sent_type = ''
    elif kind == 2:
        list1 = str2
        g = len(list1)
        prp = None
        sent_type = ''
        osent = None

    list1_cat = [None] * 80
    relation_type = 0
    list2 = []
    list3 = []
    decision = [200]
    spec_det = ['every','many'+un,'no']
    spec_rel = ["I","J"]
    posp = words[28]
    doubles = words[31]
    triples = words[32]
    proper_names = words[35]
    noun_list = ['n','p','v']
    has_comma = ""

    i = -1
    while i < g -1:
        i += 1
        if "," in list1[i]:
            list1[i] = list1[i].replace(",","")
            has_comma = list1[i]
        word = list1[i]
        if i < g - 2:
            next_word = list1[i+1]
        else:
            next_word = ""
        if word == 'you':
            bb = 8
        bool3 = False
        bool5 = False
        bool4 = check_dimension(triples,0,word)
        bool5 = False

        if bool4:
            if i+2 < len(list1):
                str4 = word + " " + list1[i+1] + " " + list1[i+2]
                bool5 = check_dimension(triples,1,str4)
                if bool5:
                    word = str4
                    if has_comma != "":
                        has_comma = word
        if not bool5:
            bool4 = check_dimension(doubles,0,word)
            if bool4 and i+1 < len(list1):

                str4 = word + " " + list1[i+1]
                if "," in str4:
                    str4 = str4.replace(",","")
                    has_comma = str4
                bool3 = check_dimension(doubles,1,str4)
                if bool3:
                    word = str4
                    if has_comma != "":
                        has_comma = word

        if word == 'it':
            #this means that the subject of the previous sentences obtains the anaphor
            #to which it refers
            all_sent[len(all_sent)-2][57] = 3
        if word == 'there':
            decision.append(110)
        if isvariable(word):
            pos = 'n'
            if word in idf_var: #zzz
                idf_var.remove(word)
                never_used.append(word)
                taken_out.append(word)
            if kind == 2:
                str1 = findinlist(word,dv_nam,0,1)
                str3 = findinlist(str1,posp,0,1)
                if str3 == "a":
                    pos = 'a'
        elif word == "~":
            pos = 'm'
        elif word == "it"+up:
            pos = 'v'
        elif word == ne:
            pos = 'r'
        elif word == 'not' + ui:
            pos = 'm'
            word = neg
        elif word == 'not':
            pos = 'm'
            word = "not"
        elif isinstance(word,int):
            pos = 'n'
        elif word[-2:] == "'s":
            pos = 'ps'
        else:
            pos = findinlist(word,posp,0,1)
        if word == 'plural form':
            has_plural = True

        #determined nouns occupy the noun position
        if pos == 'w':
            pos = 'n'

        if word == 'you':
            bb = 7
        if word == ' ' or word == "":
            pass
        elif next_word == mini_e:
            list1_cat[1] = word
        elif word == mini_e:
            list1_cat[2] = word
        elif (pos == 'd' or pos == 'q') and relation_type == 0:
            list1_cat[3] = word
            list2.append(3)
            if pos == 'd' and word not in spec_det:
                decision.append(20)
            elif pos == 'd' and word in spec_det:
                decision.append(120)
            elif pos == 'q':
                decision.append(85)
        elif pos == 'ps' and relation_type == 0 and list1_cat[5] == None:
            list1_cat[69] = word
            list2.append(69)
            temp_word = word[:-2]
            if temp_word in proper_names:
                decision.append(30)
            else:
                decision.append(90)

        elif pos == 'a' and relation_type == 0:
            list1_cat[4] = word
            list2.append(4)
            decision.append(50)
        elif pos == 'm' and list1_cat[3] == None and list1_cat[5] == None and relation_type == 0:
            list1_cat[47] = word
            list2.append(47)
        elif word == neg and isvariable(next_word) and list1_cat[5] == None:
            list1_cat[55] = word
            list2.append(55)
        elif pos in noun_list and relation_type == 0 and list1_cat[5] == None:
            list1_cat[5] = word
            list2.append(5)
            if word == 'there':
                decision.append(110)
            elif pos == 'p':
                decision.append(10)
        elif pos == 'c' and relation_type == 0 and list1_cat[5] != None:
            list1_cat[66] = word
            list2.append(66)
            decision.append(40)
        elif (pos == 'n' or pos == 'p') and relation_type == 0 and list1_cat[66] != None:
            list1_cat[67] = word
            list2.append(67)
        elif pos == 'n' and relation_type == 0 and list1_cat[5] != None:
            list1_cat[35] = word
            list2.append(35)
        elif pos == 'u' and relation_type == 0 and list1_cat[5] != None:
            list1_cat[59] = word
            list2.append(59)
            decision.append(70)
        elif word == 'that'+uc and list1_cat[7] == None and list1_cat[14] == None: # uc
            list1_cat[7] = word
            list2.append(7)
            decision.append(80)
        # elif pos == 'b' and relation_type == 0:
        #     list1_cat[7] = word
        #     list2.append(7)
        elif pos == 'm' and relation_type == 0:
            list1_cat[8] = word
            list2.append(8)
        elif pos == 'r' and relation_type == 0:
            list1_cat[9] = word
            list2.append(9)
            relation_type = 1
            if list1_cat[5] == None and list1_cat[4] != None:
                list1_cat[5] = list1_cat[4]
                list1_cat[4] = None
                list2.remove(4)
                list2.append(5)
            if snoun != "" and snum == 14:
                list1_cat[14] = snoun
        elif (pos == 'd' or pos == 'q') and relation_type == 1:
            list1_cat[10] = word
            list2.append(10)
            if pos == 'd' and word not in spec_det:
                decision.append(20)
            elif pos == 'd' and word in spec_det:
                decision.append(120)
            elif pos == 'q':
                decision.append(85)
        # this line of code must be first because if the word is an adjective
        # and the relation is IA then it must go in slot 14
        elif pos == 'm' and relation_type == 1 and list1_cat[14] == None and \
            list1_cat[60] == None:
            list1_cat[12] = word
            list2.append(12)
        elif pos == 'a' and relation_type == 1 and list1_cat[9] == "J":
            list1_cat[14] = word
            list2.append(14)
        elif pos == 'ps' and relation_type == 1 and list1_cat[14] == None:
            list1_cat[70] = word
            list2.append(70)
            temp_word = word[:-2]
            if temp_word in proper_names:
                decision.append(30)
            else:
                decision.append(90)
        elif pos == 'a' and relation_type == 1:
            list1_cat[13] = word
            list2.append(13)
            decision.append(50)
        elif pos in noun_list and relation_type == 1 and list1_cat[14] == None:
            list1_cat[14] = word
            list2.append(14)
            if pos == 'p':
                decision.append(10)
        elif pos == 'n' and relation_type == 1 and list1_cat[14] != None and list1_cat[60] == None:
            list1_cat[36] = word
            list2.append(36)
        elif pos == 'e' and relation_type == 1:
            list1_cat[48] = word
            list2.append(48)
        elif pos == 'u' and relation_type == 1 and list1_cat[14] != None:
            list1_cat[60] = word
            list2.append(60)
            if word == 'that'+uc:
                decision.append(80)
            else:
                decision.append(70)
        elif pos in noun_list and relation_type == 1 and list1_cat[60] != None:
            list1_cat[63] = word
            list2.append(63)
            if word == 'there':
                decision.append(110)
            elif pos == 'p':
                decision.append(10)
        elif (pos == 'm' and relation_type == 1) or (pos == "m" and list1_cat[15] in spec_rel):
            list1_cat[49] = word
            list2.append(49)
        elif pos == 'r' and relation_type == 1:
            list1_cat[15] = word
            relation_type = 2 #yyu
            list2.append(15)
            decision.append(100)
            if snoun != "" and snum == 18:
                list1_cat[18] = snoun
        elif (pos == 'd' or pos == 'q') and relation_type == 2:
            list1_cat[16] = word
            list2.append(16)
            if pos == 'd' and word not in spec_det:
                decision.append(20)
            elif pos == 'd' and word in spec_det:
                decision.append(120)
            elif pos == 'q':
                decision.append(85)
        elif pos == 'a' and relation_type == 2 and list1_cat[15] == "J":
            list1_cat[18] = word
            relation_type = 2
            list2.append(18)
        elif pos == 'a' and relation_type == 2:
            list1_cat[17] = word
            list2.append(17)
            decision.append(50)
        elif pos in noun_list and relation_type == 2 and list1_cat[18] == None:
            list1_cat[18] = word
            list2.append(18)
            if pos == 'p':
                decision.append(10)
        elif pos == 'u' and relation_type == 2 and list1_cat[18] != None:
            list1_cat[61] = word
            list2.append(61)
            if word != 'that'+uc:
                decision.append(70)
            else:
                decision.append(80)
        elif pos in noun_list and relation_type == 2 and list1_cat[61] != None:
            list1_cat[64] = word
            list2.append(64)
            if word == 'there':
                decision.append(110)
            elif pos == 'p':
                decision.append(10)
        elif (pos == 'm' and relation_type == 2) or (pos == "m" and list1_cat[18] in spec_rel):
            list1_cat[50] = word
            list2.append(50)
        elif pos == 'r' and relation_type == 2:
            relation_type = 3
            list1_cat[19] = word
            list2.append(19)
            decision.append(100)
            if snoun != "" and snum == 22:
                list1_cat[22] = snoun
        elif (pos == 'd' or pos == 'q') and relation_type == 3:
            list1_cat[20] = word
            list2.append(20)
            if pos == 'd' and word not in spec_det:
                decision.append(20)
            elif pos == 'd' and word in spec_det:
                decision.append(120)
            elif pos == 'q':
                decision.append(85)
        elif pos == 'a' and relation_type == 3 and list1_cat[19] == "J":
            list1_cat[22] = word
            relation_type = 3
            list2.append(22)
        elif pos == 'a' and relation_type == 3:
            list1_cat[21] = word
            list2.append(21)
            decision.append(50)
        elif pos in noun_list and relation_type == 3 and list1_cat[22] == None:
            list1_cat[22] = word
            list2.append(22)
            if pos == 'p':
                decision.append(10)
        elif pos == 'u' and relation_type == 3 and list1_cat[22] != None:
            list1_cat[62] = word
            list2.append(62)
            if word != 'that'+uc:
                decision.append(70)
        elif pos in noun_list and relation_type == 3 and list1_cat[62] != None:
            list1_cat[65] = word
            list2.append(65)
            if pos == 'p':
                decision.append(10)
        elif (pos == 'm' and relation_type == 3) or (pos == "m" and list1_cat[24] in spec_rel):
            list1_cat[51] = word
            list2.append(51)
        elif pos == 'r' and relation_type == 3:
            relation_type = 4
            list1_cat[23] = word
            list2.append(23)
            if snoun != "" and snum == 26:
                list1_cat[26] = snoun
        elif (pos == 'd' or pos == 'q') and relation_type == 4:
            list1_cat[24] = word
            list2.append(24)
            if pos == 'd' and word not in spec_det:
                decision.append(20)
            elif pos == 'd' and word in spec_det:
                decision.append(120)
            elif pos == 'q':
                decision.append(85)
        elif pos == 'a' and relation_type == 4 and list1_cat[23] == "J":
            list1_cat[26] = word
            relation_type = 4
            list2.append(26)
        elif pos == 'a' and relation_type == 4:
            list1_cat[25] = word
            list2.append(25)
            decision.append(50)
        elif pos in noun_list and relation_type == 4:
            list1_cat[26] = word
            list2.append(26)
            if pos == 'p':
                decision.append(10)
        elif (pos == 'm' and relation_type == 4) or (pos == "m" and list1_cat[27] in spec_rel):
            list1_cat[52] = word
            list2.append(52)
        elif pos == 'r' and relation_type == 4:
            relation_type = 5
            list1_cat[27] = word
            list2.append(27)
            if snoun != "" and snum == 30:
                list1_cat[30] = snoun
        elif (pos == 'd' or pos == 'q') and relation_type == 5:
            list1_cat[28] = word
            list2.append(28)
            if pos == 'd' and word not in spec_det:
                decision.append(20)
            elif pos == 'd' and word in spec_det:
                decision.append(120)
            elif pos == 'q':
                decision.append(85)
        elif pos == 'a' and relation_type == 5 and list1_cat[27] == "J":
            list1_cat[29] = word
            relation_type = 5
            list2.append(29)
        elif pos == 'a' and relation_type == 5:
            list1_cat[29] = word
            list2.append(29)
        elif pos in noun_list and relation_type == 5:
            list1_cat[30] = word
            list2.append(30)
            if pos == 'p':
                decision.append(10)
        elif pos == 'r' and relation_type == 5:
            relation_type = 6
            list1_cat[31] = word
            list2.append(31)
            if snoun != "" and snum == 34:
                list1_cat[34] = snoun
        elif (pos == 'd' or pos == 'q') and relation_type == 6:
            list1_cat[32] = word
            list2.append(32)
            if pos == 'd' and word not in spec_det:
                decision.append(20)
            elif pos == 'd' and word in spec_det:
                decision.append(120)
            elif pos == 'q':
                decision.append(85)
        elif pos == 'a' and relation_type == 6:
            list1_cat[33] = word
            list2.append(33)
            decision.append(50)
        elif pos in noun_list and relation_type == 6:
            list1_cat[34] = word
            list2.append(34)
            if pos == 'p':
                decision.append(10)
        elif pos == 'b':
            list1_cat[7] = word
        elif pos == 'm':
            if relation_type == None:
                list1_cat[8] = word
                list2.append(8)
            elif relation_type == 'r':
                list1_cat[13] = word
                list2.append(13)
        else:
            try:
                if list1[i][1] == "=":
                    pos = findinlist(list1[i][2],posp,0,1)
                    if pos == "r":
                        return 'n'
            except IndexError:
                bb = 8
            print "you misspelled " + word
            sys.exit()
        if word in anaphoric_relations and first:
                anaphora = []
                anaphora.append(list1_cat[9])
        if has_comma != "":
            for j in range(0,69):
                if list1_cat[j] == has_comma:
                    list1_cat[39] = j
                    has_comma = ""
                    break
        if bool3:
            del list1[i+1]
            g -= 1

    list2.sort()

    bool1 = isdefineable(list1_cat)
    list1_cat[46] = list2
    list1_cat[42] = prp
    list1_cat[0] = osent
    list1_cat[41] = has_plural
    list1_cat[54] = bool1
    list1_cat[53] = sent_type
    list1_cat[56] = decision
    return list1_cat

def dec_pro(decision,list3,pronouns):

    num10 = [5,14,18,22,26,30,34] # pronouns
    num20 = [3,10,16,20,24,28,32] # determiners
    num30 = [69,70] # proper name possessive
    num40 = [66] # and
    num50 = [4,13,17,21,25,33] # adjective
    num60 = [35,36] # cia
    num70 = [59,60,61,62] # relative pronouns
    num80 = [62,61,60,7] # that-c
    num90 = [69,70] # possessives
    num100 = [15,19] # # ,RDB
    num110 = [5,63,64] # there
    num120 = [3,10,16,20,24,28,32] # every, many-n
    list2 = list3[46]
    list4 = ['a','the']

    for i in list2:
        if i in num10 and list3[i] in pronouns:
            if 10 not in decision:
                decision.append(10)
        elif i in num20 and list3[i] in list4:
            if 20 not in decision:
                decision.append(20)
        elif i in num30:
            if i == 69:
                if list3[3] == None:
                    if 30 not in decision:
                        decision.append(30)
                else:
                    if 90 not in decision:
                        decision.append(90)
            elif i == 70:
                if list3[10] == None:
                    if 30 not in decision:
                        decision.append(30)
                else:
                    if 90 not in decision:
                        decision.append(90)
        elif i in num40:
            if 40 not in decision:
                decision.append(40)
        elif i in num50:
            if i == 13 and list3[10] == 'every':
                pass
            elif list3[i-1] == 'every':
                pass
            else:
                if 50 not in decision:
                    decision.append(50)
        elif i in num60:
            if 50 not in decision:
                decision.append(50)
        elif i in num70:
            bool1 = False
            if i == 59 and list3[10] != 'every':
                bool1 = True

    #     if i == 10 and list[59] != None:
    #     return False
    # elif i == 16 and list[60] != None:
    #     return False
    # elif i == 20 and list[61] != None:
    #     return False
    # elif i == 24 and list[62] != None:
    #     return False
    # else:
    #     return True



def build_sent_name(prop_name):
    str1 = ''
    str2 = ''
    list1 = []

    for i in range(len(prop_name)):
        if i == 24:
            bb = 8
        str3 = remove_outer_paren(prop_name[i][2])
        str3 = str3.replace("~","")
        str1 = '(' + prop_name[i][0] + mini_e + str3 + ')'
        if len(str2) == 0 and len(str1) > 57:
            list1.append(str1)
        elif (len(str2) + len(str1)) > 57:
            list1.append(str2)
            str2 = str1
            if i + 1 == len(prop_name):
                list1.append(str2)
        elif (len(str2) + len(str1)) <= 57:
            if len(str2) == 0:
                str2 = str1
            else:
                str2 = str2 + ' & ' + str1
            if i + 1 == len(prop_name):
                list1.append(str2)
    return list1



def syn(tot_sent, all_sent, words,def_atoms):

    global sn,def_used
    doubles = words[31]
    bool1 = False
    atoms = ['moment','relationship','point','number','thought','imagination',\
            'property','possible world','possible relationship','word','reality']
    synon = words[14]
    syn_pairs = words[13]
    m = -1
    while m < len(all_sent) -1:
        m += 1
        old_sent = all_sent[m][-3]
        oldp = all_sent[m][-2]
        sent_type = all_sent[m][-1]
        anc1 = ""
        anc2 = ""
        anc3 = ""
        anc4 = ""
        i = -1
        while i < len(all_sent[m])-4:
            i += 1
            str1 = all_sent[m][i]
            bool2 = check_dimension(doubles,0,str1)
            bool3 = False
            if bool2:
                str4 = all_sent[m][i] + " " + all_sent[m][i+1]
                bool3 = check_dimension(doubles,1,str4)
                if bool3:
                    str1 += " " + all_sent[m][i+1]
            if i == 9:
                bb = 7
            if str1 in synon:
                if str1 not in def_used:
                    def_used.append(str1)
                for j in range(len(syn_pairs)):
                    if str1 == syn_pairs[j][0]:
                        bool1 = True
                        rule = 'DE ' + str1
                        str5 = syn_pairs[j][2]
                        if " " in syn_pairs[j][1]:
                            str6 = syn_pairs[j][1]
                            g = str6.find(" ")
                            str3 = str6[:g]
                            str4 = str6[g+1:]
                            list2 = copy.deepcopy(all_sent[m])
                            list2[i] = str4
                            list2.insert(i,str3)
                            all_sent[m] = list2
                        else:
                            all_sent[m][i] = syn_pairs[j][1]
                        u = findinlist(str5,tot_sent,1,0,True)
                        if u == -1:
                            bool1 = True
                            str5v = name_sent(syn_pairs[j][2])
                            s = findinlist(str5,tot_sent,1,0)
                            sn += 1
                            if s == None:
                                s = sn
                            if anc1 == "":
                                anc1 = s
                            elif anc2 == "" and s != anc1:
                                w = copy.copy(s)
                                anc2 = w
                            elif anc3 == "" and s != anc1 and s != anc2:
                                u = copy.copy(s)
                                anc3 = u
                            tot_sent.append([sn, str5, "","", rule,"","","",""])
                        else:
                            s = tot_sent[u][0]
                            str5v = name_sent(syn_pairs[j][2])
                            if anc1 == "":
                                t = copy.copy(s)
                                anc1 = t
                            elif anc2 == "" and s != anc1:
                                w = copy.copy(s)
                                anc2 = w
                            elif anc3 == "" and s != anc1 and s != anc2:
                                u = copy.copy(s)
                                anc3 = u
                        if bool3:
                            del all_sent[m][i+1]
                        break
            if all_sent[m][i] in atoms:
                def_atoms.append(all_sent[m][i])

        if bool1:
            new_sent = build_sent2(all_sent[m],True)
            newp = name_sent(new_sent)
            all_sent[m][-3] = new_sent
            all_sent[m][-2] = newp
            all_sent[m][-1] = sent_type
            dummy = new_sentence2(old_sent,oldp,new_sent,newp,tot_sent,"SUB",anc1,iff,anc2,anc3)
            bool1 = False
    return


def quick_print(list1,list2,list3,kind=0,a=0,b=0,c=0):

    j = 1
    if kind == 0:
        for i in range(len(list2)):
            j += 1
            if list1 != []:
                w4.cell(row=j,column = 2).value = list1[i]
            w4.cell(row=j,column = 3).value = list2[i]
            if list3 != []:
                w4.cell(row=j,column = 4).value = list3[i]
    elif kind == 1:
        for i in range(len(list2)):
            j += 1
            if a != 0:
                w4.cell(row=j,column = 2).value = list2[i][a]
            w4.cell(row=j,column = 3).value = list2[i][b]
            if c != 0:
                w4.cell(row=j,column = 4).value = list2[i][c]


    wb4.save('../temp_proof.xlsx')
    sys.exit()


def print_sent_full(test_sent,p,tot_prop_name,words,yy = ""):

    global result_data
    global excel,strt,stp,def_used,words_used

    # p = 30
    bb = 8
    b = time.time()
    p += 2
    definitions2 = words[33]
    for i in range(len(dv_nam)):
        if dv_nam[i][0] not in def_used:
            def_used.append(dv_nam[i][1])

    if excel and words_used:
        for i in range(len(def_used)):
            j = findinlist(def_used[i],definitions2,0,1)
            if j != None:
                ws.cell(row=j,column=1).value = 1
                bool2 = True
                while bool2:
                    j += 1
                    word2 = ws.cell(row=j,column=3).value
                    if word2 == def_used[i]:
                        ws.cell(row=j,column=1).value = 1
                    else:
                        break

    c = time.time()
    # print c-b


    if stp == 0:
        stp = len(test_sent)
    elif yy != "":
        stp = yy

    o = -1
    for i in range(strt,stp):
        # if i == 2:
        #     break
        for j in range(len(test_sent[i])):
            try:
                if len(test_sent[i][j]) == 7:
                    test_sent[i][j].append("")
                elif len(test_sent[i][j]) == 6:
                    test_sent[i][j].append("")
                    test_sent[i][j].append("")
                elif len(test_sent[i][j]) == 5:
                    test_sent[i][j].append("")
                    test_sent[i][j].append("")
                    test_sent[i][j].append("")
            except TypeError:
                bb = 8

            if test_sent[i][j][7] != "" and test_sent[i][j][7] != None:
                str1 = test_sent[i][j][4] + ' ' + str(test_sent[i][j][5]) + ',' +\
                       str(test_sent[i][j][6]) + ',' + str(test_sent[i][j][7])
            elif test_sent[i][j][6] != "" and test_sent[i][j][6] != None:
                str1 = test_sent[i][j][4] + ' ' + str(test_sent[i][j][5]) + ',' + str(test_sent[i][j][6])
            elif test_sent[i][j][5] != None and test_sent[i][j][5] != "":
                str1 = test_sent[i][j][4] + ' ' + str(test_sent[i][j][5])
            elif test_sent[i][j][4] != None and test_sent[i][j][4] != "":
                str1 = test_sent[i][j][4]
            else:
                str1 = ""
            if j == 0:
                str1 = i
            if excel or one_sent:
                w4.cell(row=p,column=2).value = test_sent[i][j][0]
                w4.cell(row=p,column=3).value = test_sent[i][j][1]
                w4.cell(row=p,column=4).value = str1
            else:
                result_data['text_'+str(p-1)+'_1']=test_sent[i][j][0]
                result_data['text_'+str(p-1)+'_2']=test_sent[i][j][1]
                result_data['text_'+str(p-1)+'_3']= str1

            p += 1

        p += 1
        o += 1
        list1 = build_sent_name(tot_prop_name[o])
        for j in range(len(list1)):
            if excel or one_sent:
                w4.cell(row=p,column=3).value = list1[j]
            else:
                result_data['text_'+str(p)+'_2']=list1[j]
            p += 1
        p += 1

        bool1 = False
        if tot_prop_sent != []:
            for j in range(len(tot_prop_sent[o])):
                if j == 8:
                    bb = 7
                if not bool1 and tot_prop_sent[o][j][4] != "":
                    if excel or one_sent:
                        w4.cell(row=p,column=3).value = "____________________"
                    else:
                        result_data['text_'+str(p)+'_2']="____________________"

                    bool1 = True
                    p += 1
                if excel or one_sent:
                    w4.cell(row=p,column=2).value = tot_prop_sent[o][j][0]
                    w4.cell(row=p,column=3).value = tot_prop_sent[o][j][2] + tot_prop_sent[o][j][1]
                else:
                    result_data['text_'+str(p)+'_1']=tot_prop_sent[o][j][0]
                    result_data['text_'+str(p)+'_2']=tot_prop_sent[o][j][2] + tot_prop_sent[o][j][1]

                str2 = ""
                if len(tot_prop_sent[o][j]) == 5:
                    str2 = tot_prop_sent[o][j][3] + " " + str(tot_prop_sent[o][j][4])
                elif len(tot_prop_sent[o][j]) == 6:
                    str2 = tot_prop_sent[o][j][3] + " " + str(tot_prop_sent[o][j][4]) + \
                    "," + str(tot_prop_sent[o][j][5])
                else:

                    if tot_prop_sent[o][j][4] != "":
                        str2 = tot_prop_sent[o][j][3] + " " + str(tot_prop_sent[o][j][4])
                    if tot_prop_sent[o][j][5] != "" and tot_prop_sent[o][j][5] != None:
                        str2 += "," + str(tot_prop_sent[o][j][5])
                    if tot_prop_sent[o][j][6] != "" and tot_prop_sent[o][j][6] != None:
                        str2 += "," + str(tot_prop_sent[o][j][6])
                    if len(tot_prop_sent[o][j]) > 7:
                        if tot_prop_sent[o][j][7] != "" and tot_prop_sent[o][j][7] != None:
                            str2 += "," + str(tot_prop_sent[o][j][7])

                if excel or one_sent:
                    w4.cell(row=p,column=4).value = str2
                else:
                    result_data['text_'+str(p)+'_3']= str2
                if (excel or one_sent) and j+1 == len(tot_prop_sent[o]):
                    w4.cell(row=p,column=5).value = 1

                p += 1
            p += 3
    e = time.time()
    g = e - b
    return



def build_dict(ex_dict):

    global excel
    detm = []
    relat = []
    srelat = []
    trelat = []
    atomic_relations = []
    det = []
    adj = []
    adv = []
    noun = []
    cor = []
    lcon = []
    compound = []
    subo = []
    synon = []
    redundant = []
    proper_names = []
    aux = []
    atomic_relata = []
    negg = []
    dnoun = []
    not_oft_def = [] # words that are only defined if they appear in the input sentence
    uniq_obj = [] # words which have (b=julius caesar) as definiendum
    det_pairs = []
    syn_pairs = []
    particles = []
    relations = []
    relations2 = []
    definitions = []
    definitions2 = []
    really_atomic = []
    pronouns = []
    poss_pronouns = []
    doubles = []
    triples = []
    plurals = []
    neg_det = []
    pos = []
    category = ['r','s','t']
    almost_done = False

    i = -1
    if one_sent:
        mm = len(ex_dict)
    else:
        mm = 2000

    while i < mm-1:
    # for row in ws:
        i += 1
        if i == 90:
            bb = 8

        if excel:
            if i == 0:
                i = 1
            s = ws.cell(row=i,column=1).value
            str1 = ws.cell(row=i,column=3).value
            word = ws.cell(row=i,column=4).value
            if word == "true*":
                word = "true"
            if word == "false*":
                word = "false"

        elif one_sent:
            s=0
            str1 = ex_dict[i][0]
            word = ex_dict[i][1]
            if word != None:
                word = tran_str(word,2)
                word = word[0]
        else:
            s = row.extra
            str1 = row.type
            word = row.word

        if word == None and almost_done:
            break
        if word == None:
            almost_done = True
        else:
            almost_done = False
        if str1 != None:
            if not isinstance(str1,(int,long)):
                str1 = str1.strip()
            if word == 'non_whole':
                bb = 7
            elif word == 2:
                bb = 7

            if isinstance(word,(int,long)):
                word = str(word)

            if "(" in word:
                cc = word.index("(")
                word = word[:cc-1]

            word = word.strip()
            definitions2.append([word,i])
            if excel:
                str3 = ws.cell(row=i,column=5).value
                defin = ws.cell(row=i,column=6).value
            elif one_sent:
                str3 = ex_dict[i][2]
                defin = ex_dict[i][3]
                defin = tran_str(defin, 3)
                defin = defin[0]
            else:
                str3 = row.rel
                defin = row.definition


            if defin == 'redundant':
                redundant.append(word)
            if defin != None and defin.find("E.g.") == -1 and defin.find("EXP") == -1 \
                    and defin != 'redundant' and word != "." and defin.find("e.g.") == -1\
                    and str1 != "":
                if word != None:
                    word = word.strip()
                if str3 != None:
                    str3 = str3.strip()
                if str1 == None:
                    print "you did not state the part of speech for " + word
                    sys.exit()
                sec_let = copy.copy(str1)
                fir_let = str1[0:1]

                if "(" in word:
                    y = word.find("(")
                    word = word[:y-1]
                if " " in word:
                    m = word.count(" ")
                    if m == 1:
                        word1 = copy.copy(word)
                        y = word1.find(" ")
                        word1 = word1[:y]
                        doubles.append([word1,word])
                    if m == 2:
                        word1 = copy.copy(word)
                        y = word1.find(" ")
                        word1 = word1[:y]
                        triples.append([word1,word])

                sec_let = sec_let[1:2]
                thir_let = str1[2:3]
                if len(str1) > 4:
                    fif_let = str1[4:5]
                else:
                    fif_let = None

                if fir_let == 'r' and sec_let != 's':
                    pos.append([str3,fir_let,fif_let])
                else:
                    pos.append([word,fir_let,fif_let])

                if thir_let == "d":
                    compound.append(str3)
                elif thir_let == "n":
                    proper_names.append(word)


                if len(str1) > 3:
                    if str1[3] == 's':
                        srelat.append(word)
                    elif str1[3] == 't':
                        trelat.append(word)
                if (sec_let == 'a' or sec_let == 'b') and fir_let == "r":
                    if str3 == None:
                        bb = 8
                    if str3 not in atomic_relations:
                        atomic_relations.append(str3)
                if sec_let == 'b':
                    really_atomic.append(str3)
                elif sec_let == 'u':
                    uniq_obj.append(word)
                elif sec_let == 'k':
                    not_oft_def.append(word)
                if fir_let == 'a':
                    adj.append(word)
                elif fir_let == 'b':
                    aux.append(word)
                elif fir_let == 'c':
                    cor.append(word)
                elif fir_let == 'd':
                    detm.append(word)
                    det.append([word,sec_let,defin])
                elif fir_let == 'r':
                    relat.append([word,str3])
                elif fir_let == 'e':
                    adv.append(word)
                elif fir_let == 'l' and sec_let == 'b':
                    lcon.append(word)
                elif fir_let == 'm':
                    negg.append(word)
                elif fir_let == 'n':
                    noun.append(word)
                elif fir_let == 'p':
                    pronouns.append(word)
                elif fir_let == 'q':
                    poss_pronouns.append(word)
                elif fir_let == 'u':
                    subo.append(word)
                elif fir_let == 'w':
                    dnoun.append(word)
                if sec_let == 'a':
                    atomic_relata.append(word)
        # in the database the definition of plural must be written as 'plural of'
                elif sec_let == "m":
                    str6 = defin[10:]
                    plurals.append([word,str6])
                elif sec_let == 'q':
                    particles.append(word)
                if sec_let == 'p' or sec_let == 'd':
                    if sec_let == 'p':
                        sec_let = 7
                    elif sec_let == 'd':
                        sec_let = 5
                    list1a = [word, sec_let]
                elif sec_let == 'c':
                    anaphoric_relations.append(str3)
                elif sec_let == 's':
                    str6 = defin[defin.find("=")+1:-1]
                    str6 = str6.strip()
                    str7 = defin[1:defin.find("=")]
                    str7 = str7.strip()
                    list3a = [str7, str6, defin]
                    syn_pairs.append(list3a)
                    synon.append(str7)

                if sec_let != 'a' and sec_let != 'm' and defin != "artificial" and defin != 'redundant'\
                    and defin != "postponed" and sec_let != 'b':
                    if fir_let in category:
                        definitions.append([str3,defin,fir_let,sec_let,thir_let,fif_let,i])
                    else:
                        definitions.append([word,defin,fir_let,sec_let,thir_let,fif_let,i])



    syn_pairs.sort()
    relat.sort()
    atomic_relata.sort()
    relations.sort()
    relations2.sort()
    words = [adj, cor, detm, adv, lcon, noun, relat, srelat, trelat, subo,\
            aux, negg, dnoun,syn_pairs,synon,det, definitions, det_pairs, relations, \
             relations2, particles, redundant,atomic_relations, atomic_relata, \
             pronouns,poss_pronouns,plurals,neg_det,pos,really_atomic,\
             anaphoric_relations,doubles,triples,definitions2,compound,proper_names,\
             not_oft_def,uniq_obj]

    return words


def findinlist(str1, list1, i, j, bool1 = False):
    # this function takes a string, matches it to an element in the first dimension
    # of the list, then returns the matching second element

    for d in range(len(list1)):
            if str1 == list1[d][i]:
                str2 = list1[d][j]
                if bool1:
                    return d
                else:
                    return str2
    if bool1:
        return -1
    else:
        return None


def findposmd(str1,str2,list1,p,q,r):

    for i in range(len(list1)):
        if list1[i][p] == str1 and list1[i][q] == str2:
            return list1[i][r]

    return -1

def findposinmd(str1,list1,p):
    # this determines the position of an element in a multidimensional list
    for i in range(len(list1)):
        if list1[i][p] == str1:
            return i
    return -1

def isinmdlist(str1,list1,p):
    # this determines whether or not an element is in a multidimensional list
    for i in range(len(list1)):
        if list1[i][p] == str1:
            return True

    return False


def findposinlist(str1, list1,i):
    # this function takes a string, matches it to an element in the first dimension
    # of the list, then returns the position in the list

    if str1 == 0:
        return
    str2 = copy.copy(str1)
    if str2 != None:
        str2 = str2.replace(" ","")
    for d in range(len(list1)):
        str3 = copy.copy(list1[d][i])
        if str3 != None:
            str3 = str3.replace(" ","")
        if str2 == str3:
            return d
    else:
        return -1

def two_elements_in_list(list1,stri,strj,i,j):

    for k in range(len(list1)):
        if list1[k][i] == stri and list1[k][j] == strj:
            return True

    return False

def findin1dlist(str1,list1):

    for i in range(len(list1)):
        if str1 == list1[i]:
            return i

def isatomic(list1,words):

    atomic_relations = words[29]
    num = [5,14]
    if not list1[9] in atomic_relations:
        return False
    for i in num:
        if not isvariable(list1[i]):
            return False
    num = [3,4,6,7,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32, \
           33,34,35,47,48,49,50,51,52,53,69,70]
    for i in num:
        if list1[i] != "" and list1[i] != None:
            return False
    return True

def ismultidim(list1):

    if type(list1[0]) is list:
        return True
    else:
        return False


def whole_exception(list1,str1):

    exceptions = ['IMAGINATION','FACT','DESIRABLE RELATIONSHIP','POSSIBLE RELATIONSHIP',\
            'POSSIBLE WORLD','REALITY','RELATIONSHIP','SENSORIUM','SENSATIONAL RELATIONSHIP']

    bool1 = False
    bool2 = False
    bool3 = False
    bool4 = False
    for i in range(len(list1)):
        if list1[i][0] == str1:
            if list1[i][1] == 'WHOLE':
                bool1 = True
            if list1[i][1] in exceptions:
                bool2 = True
            if list1[i][1] == 'DESIRABLE RELATIONSHIP':
                bool3 = True
            if list1[i][1] == 'THOUGHT':
                bool4 = True

    if (bool1 and bool2) or (bool3 and bool4):
        return True
    else:
        return False


def axioms(greek2,list1,bo2,disjuncts,tot_sent,candd,candd2,conditionals,all_sent,prop_sent,\
           member_prop,not_id):

    already_done = []
    global dv_nam,sn,cnjts
    added = False
    used_ax = []
    list2 = extract_list(list1,0)
    for i in range(len(list2)):
        str1 = list2[i]
        if str1 not in already_done:
            already_done.append(str1)
            g = list2.count(str1)
            if g > 1:
                conjuncts = []
                list3 = []
                bool1 = whole_exception(list1,str1)
                if not bool1:
                    for m in range(i,len(bo2)):
                        if list1[m][0] == str1:
                            prop = bo2[m][42]
                            prop = prop.replace("~","")
                            if prop not in disjuncts:
                                if bo2[m][5] == str1:
                                    conjuncts.append([bo2[m],5])
                                elif bo2[m][14] == str1:
                                    conjuncts.append([bo2[m],14])
                            else:
                                if bo2[m][5] == str1:
                                    list3.append([bo2[m],5])
                                elif bo2[m][14] == str1:
                                    list3.append([bo2[m],14])

                    if len(conjuncts) == 1 and len(list3) >= 1:
                        for k in range(len(conjuncts)):
                            for j in range(len(list3)):
                                added = True
                                pos1 = conjuncts[k][1]
                                pos2 = list3[j][1]
                                rel1 = conjuncts[k][0][9]
                                rel2 = list3[j][0][9]
                                sub1 = conjuncts[k][0][5]
                                obj1 = conjuncts[k][0][14]
                                sub2 = list3[j][0][5]
                                obj2 = list3[j][0][14]
                                osec_sent = list3[j][0][0]
                                done = axioms2(greek2,pos1,pos2,rel1,rel2,sub1,obj1,sub2,obj2,osec_sent,tot_sent,used_ax,\
                                        candd,candd2,conditionals,all_sent,member_prop,not_id,prop_sent)

                    elif len(conjuncts) == 2:
                        added = True
                        pos1 = conjuncts[0][1]
                        pos2 = conjuncts[1][1]
                        rel1 = conjuncts[0][0][9]
                        rel2 = conjuncts[1][0][9]
                        sub1 = conjuncts[0][0][5]
                        obj1 = conjuncts[0][0][14]
                        sub2 = conjuncts[1][0][5]
                        obj2 = conjuncts[1][0][14]
                        osec_sent = conjuncts[1][0][0]
                        done = axioms2(greek2,pos1,pos2,rel1,rel2,sub1,obj1,sub2,obj2,osec_sent,tot_sent,used_ax,\
                                candd,candd2,conditionals,all_sent,member_prop,not_id,prop_sent)

                    elif len(conjuncts) > 2:
                        y = 0
                        for n in range(y,g-1):
                            y += 1
                            h = y
                            while h < g:
                                j = h
                                h += 1
                                k = n
                                added = True
                                pos1 = conjuncts[k][1]
                                pos2 = conjuncts[j][1]
                                rel1 = conjuncts[k][0][9]
                                rel2 = conjuncts[j][0][9]
                                sub1 = conjuncts[k][0][5]
                                obj1 = conjuncts[k][0][14]
                                sub2 = conjuncts[j][0][5]
                                obj2 = conjuncts[j][0][14]
                                osec_sent = conjuncts[j][0][0]
                                done = axioms2(greek2,pos1,pos2,rel1,rel2,sub1,obj1,sub2,obj2,osec_sent,tot_sent,used_ax,\
                                        candd,candd2,conditionals,all_sent,member_prop,not_id,prop_sent)

    if added:
        candd = get_rel_conj(candd,conditionals)
        conditionals5 = copy.deepcopy(conditionals)
        list1 = statement_logic(greek2,prop_sent,all_sent,conditionals5,\
                                     candd,candd2,disjuncts,0,all_sent)
        return list1
    else:
        return [True,conditionals]

def axioms2(greek2,pos1,pos2,rel1,rel2,sub1,obj1,sub2,obj2,osec_sent,tot_sent,used_ax,\
            candd,candd2,conditionals,all_sent,member_prop,not_id,prop_sent):

    global dv_nam,idf_var,sn,cnjts,band_aid_axiom

    rn_list = []
    thing_con = findinlist('thing',dv_nam,1,0)
    if thing_con == None:
        thing_con = idf_var[0]
        for i in range(len(tot_sent)):
            if tot_sent[i][4] == "ID":
                tot_sent[i][2] += " & (" + thing_con + "= thing)"
                dv_nam.append([thing_con,'thing'])
                break
        del idf_var[0]
    else:
        rn1 = "(" + "e" + mini_c + thing_con + ")"
        rn_list.append(rn1)
    if sub1 != 'b':
        rn1 = "(b" + mini_c + sub1 + ")"
        rn_list.append(rn1)
    if obj1 != 'c':
        rn1 = "(c" + mini_c + obj1 + ")"
        rn_list.append(rn1)
    thing_int = idf_var[0]
    del idf_var[0]
    new_var = idf_var[0]
    del idf_var[0]
    if thing_int != 'd':
        rn1 = "(d" + mini_c + thing_int + ")"
        rn_list.append(rn1)
    if pos1 == 5 and pos2 == 5:
        thing_var = obj2
        oax = "(((b" + rel1 + "c) & (dIe)) " + conditional + \
        " (b~" + rel2 + "d)) & (e=thing)"
        sent3 = "(" + sub1 + "~" + rel2 + thing_int + ")"
        subj4 = sub1
        obj4 = thing_int
        oax_name = "AX." + rel1 + "." + rel2 + "." + "ss"
    elif pos1 == 5 and pos2 == 14:
        thing_var = sub2
        oax = "(((b" + rel1 + "c) & (dIe)) " + conditional + \
        " (d~" + rel2 + "b)) & (e=thing)"
        sent3 = "(" + thing_int + "~" + rel2 + sub1 + ")"
        subj4 = thing_int
        obj4 = sub1
        oax_name = "AX." + rel1 + "." + rel2 + "." + "so"
    elif pos1 == 14 and pos2 == 5:
        thing_var = obj2
        oax = "(((b" + rel1 + "c) & (dIe)) " + conditional + \
        " (c~" + rel2 + "d)) & (e=thing)"
        sent3 = "(" + obj1 + "~" + rel2 + thing_int + ")"
        subj4 = obj1
        obj4 = thing_int
        oax_name = "AX." + rel1 + "." + rel2 + "." + "os"
    elif pos1 == 14 and pos2 == 14:
        thing_var = sub2
        oax = "(((b" + rel1 + "c) & (dIe)) " + conditional + \
        " (d~" + rel2 + "c)) & (e=thing)"
        sent3 = "(" + thing_int + "~" + rel2 + obj1 + ")"
        subj4 = thing_int
        obj4 = obj1
        oax_name = "AX." + rel1 + "." + rel2 + "." + "oo"

    sent1 = "(" + sub1 + rel1 + obj1 + ")"
    sent3a = sent3.replace("~","")
    sent5 = "(" + sub2 + rel2 + obj2 + ")"
    sent2 = "(" + thing_int + "I" + thing_con + ")"
    nax = "(" + sent1 + " & " + sent2 + ") " + conditional \
        + " " + sent3
    rename = build_sent_list(rn_list)
    # ax_enti = "(" + thing_var + "I" + thing_con + ")"
    subst1 = "(" + thing_var + mini_c + thing_int + ")"
    #sent4 = "(" + thing_var + "I" + thing_con + ")"
    subst4 = sent5 + " " + conditional + " " + sent3a

    sent1p = name_sent(sent1)
    sent2p = name_sent(sent2)
    #all_sent = add_thing_sent_to_all_sent(all_sent,sent2,sent2p,thing_int,thing_con)
    sent3p = name_sent(sent3)
    sent3ap = name_sent(sent3a)
    #sent4p = name_sent(sent4)
    sent5p = name_sent(sent5)
    naxp = "(" + sent1p + " & " + sent2p + ") " + conditional \
        + " " + sent3p
    subst4p = sent5p + " " + conditional + " " + sent3ap
    d = findposinlist(oax,used_ax,0)
    if d > -1:
        e = used_ax[d][1]
    else:
        e = sn+1
        sn += 1
        used_ax.append([oax, sn])
        tot_sent.append([sn,oax,"","",oax_name,"","","",""])
    sn += 1
    tot_sent.append([sn,rename,"","","RN","","","",""])
    sn += 1
    tot_sent.append([sn,nax,naxp,"","SUB",e,sn-1,"",""])
    prop_sent.append([sn,naxp,"","","","","","","",""])
    list2 = mainconn(naxp)
    enc_naxp = enclose(naxp)
    def_info = find_sentences(enc_naxp)
    list1 = prepare_iff_elim(greek2,def_info,naxp,all_sent,list2[0],list2[1],sn,tot_sent)
    conditionals.append(list1)
    #sn += 1
    #tot_sent.append([sn,sent4,sent4p,"","AY ENT","","","",""])
    #candd.append([sn,sent4p,""])
    #prop_sent.append([sn,sent4p,"","","","","","","",""])
    sn += 1
    band_aid_axiom = sent2p
    tot_sent.append([sn,sent2,sent2p,"","AY ENT","","","",""])
    prop_sent.append([sn,sent2p,"","","","","","","",""])
    candd.append([sn,sent2p,""])
    sn += 1
    tot_sent.append([sn,subst1,"","","OS",sn-1,sn-2,"",""])
    sn += 1
    tot_sent.append([sn,subst4,subst4p,"","SUB",sn-1,"","",""])
    prop_sent.append([sn,subst4p,"","","","","","","",""])
    list2 = mainconn(subst4p)
    enc_subst4p = enclose(subst4p)
    def_info = find_sentences(enc_subst4p)
    list1 = prepare_iff_elim(greek2,def_info,subst4p,all_sent,list2[0],list2[1],sn,tot_sent)
    conditionals.append(list1)
    cnjts.append(sent2p)

    #if the required sentences are not conjuncts then we must add them to the all sent list
    if sent5p not in cnjts or sent1p not in cnjts:
        list1 = [None] * 80
        list1[5] = subj4
        list1[8] = "~"
        list1[9] = rel2
        list1[14] = obj4
        list1[0] = sent3
        list1[42] = sent3p
        all_sent.append(list1)
        list2 = copy.deepcopy(list1)
        list2[8] = ""
        list2[0] = sent3a
        list2[42] = sent3ap
        all_sent.append(list2)
        list3 = [None] * 80
        list3[5] = thing_int
        list3[8] = ""
        list3[9] = "I"
        list3[14] = thing_con
        list3[0] = sent2
        list3[42] = sent2p
        list3[46] = [200]
        list3[56] = [200]
        all_sent.append(list3)
        list5 = [thing_int,"THING",[],[],[],[],[],"",[],[]]
        member_prop.append(list5)
        not_id.append([thing_int,thing_var])
        return False
    else:
        return True


def add_thing_sent_to_all_sent(all_sent,sent2,sent2p,thing_int,thing_con):

    list1 = [None] * 80
    list1[0] = sent2
    list1[42] = sent2p
    list1[5] = thing_int
    list1[9] = "I"
    list1[14] = thing_con
    all_sent.append(list1)

    return all_sent


def get_sent(all_sent,str1):

    for i in range(len(all_sent)):
        str2 = all_sent[i][42].replace("~","")
        if str1 == str2:
            return i
    print "the get sent function is wrong"
    sys.exit()


def find_group(str1,all_sent,subj,basic_objects):

    global gen_var
    pair1 = ["integer",'NUMBER']
    pair2 = ["",""]
    synonyms = [pair1,pair2]
    exceptions = ['this'+un,'that'+un]
    if subj == 't':
        bb = 8

    str3 = None
    str4 = None
    list1 = []
    for i in range(len(basic_objects)):
        if basic_objects[i][0] == subj:
            str4 = basic_objects[i][1]
            if str4 not in list1:
                list1.append(str4)

    for i in range(len(all_sent)):
        if all_sent[i][46] != "x":
            if all_sent[i][9] == "I" and all_sent[i][8] != "~" and all_sent[i][5] == subj:
                str2 = all_sent[i][14]
                str3 = findinlist(str2,dv_nam,0,1)
                if str3 in exceptions:
                    str3 = None
                if str3 != None:
                    d = findposinlist(str3,synonyms,0)
                    if d > -1:
                        str3 = synonyms[d][1]
                    str3 = str3.upper()
                    if str3 not in list1:
                        list1.append(str3)
                elif all_sent[i][14] not in gen_var:
                    str3 = all_sent[i][14].upper()
                    str3 = str3 + " THINGS"
                    list1.append(str3)

    if str3 == None and str4 == None and list1 == []:
        return None
    else:
        list2 = [subj,list1]
        return list2

def simple_id(tot_sent,all_sent,identities):

    num = [5,14,18,22]
    dummy = remove_duplicates2d(identities,0,1)
    for i in range(len(identities)):
        str1 = "(" + identities[i][0][0] + " = " + identities[i][0][1] + ")"
        for j in range(len(tot_sent)-1,0,-1):
            if str1 in tot_sent[j][1]:
                identities[i][1] = tot_sent[j][0]
                break

    for i in range(len(identities)):
        str1 = identities[i][0][0]
        str2 = identities[i][0][1]
        for j in range(len(all_sent)):
            if all_sent[j][46] != "x":
                for k in num:
                    if all_sent[j][k] == None and (k == 18 or k == 22):
                        break
                    if all_sent[j][k] == str1 or all_sent[j][k] == str2:
                        list1 = copy.deepcopy(all_sent[j])
                        old_sent = all_sent[j][0]
                        oldp = all_sent[j][42]
                        if all_sent[j][k] == str1:
                            list1[k] = str2
                        else:
                            list1[k] = str1
                        new_sent = build_sent(list1)
                        newp = name_sent(new_sent)
                        list1[0] = new_sent
                        list1[42] = newp
                        dummy = new_sentence2(old_sent,oldp,new_sent,newp,tot_sent,"SUB",identities[i][1])
                        all_sent.append(list1)

def reflex(all_sent,j,tot_sent,prop_sent):

    global sn,pn
    list1 = copy.deepcopy(all_sent[j])
    list1[8] = "~"
    str1 = "~" + all_sent[j][42]
    list1[42] = str1
    str2 = build_sent(list1)
    g = copy.copy(sn)
    sn += 1
    tot_sent.append([sn,str2,str1,"","IRR","","",""])
    for p in range(len(prop_sent)):
        if prop_sent[p][0] == g:
            break
    prop_sent.insert(p+1,[sn,all_sent[j][42],"~","","","","","",""])
    str3 = all_sent[j][42] + " & " + str1
    pn += 1
    for p in range(len(prop_sent)-1,-1,-1):
        if prop_sent[p][1] == all_sent[j][42] and prop_sent[p][2] == "":
            k = prop_sent[p][0]
            break
    prop_sent.append([pn,str3,"","&I",sn,k,None,None,None,None,None])
    pn += 1
    prop_sent.append([pn, bottom, "", bottom + "I", pn-1, None, None, None, None, None, None, \
    None, None, None, None])

    return False


def cat_err(all_sent,words,basic_objects,bo2,\
        member_prop,not_id,property_sent,tot_sent):
    #wwr
    global qn
    atomic = words[29]
    members = []
    non_id = []
    used_var = []
    str2 = ""
    consq = []
    for i in range(len(idf_var2)):
        if idf_var2[i] not in idf_var:
            used_var.append(idf_var2[i])
        else:
            if i > 26:
                break

    consistent = True
    nw = []
    basic_cat = ["moment","relationship","point","number","thought","imagination","group",\
    "property","possible world","word","natural whole","mind",'matter','sensorium',\
             'sensation']
    ax_ent = ""
    bool1 = False
    num = [5,14,18,22]
    listfa = []
    reflex_found = False
    spec_prop = ["indefinite","definite","general"]
    j = -1
    while j < (len(all_sent)) -1:
        j += 1
        if j == 13:
            bb = 8
        if all_sent[j][43] == "x":
            all_sent[j][46] = [200]
            all_sent[j][56] = [200]
        relat = all_sent[j][9]
        if relat == "J":
            str6 = findinlist(all_sent[j][14],dv_nam,0,1)
            if str6 in spec_prop:
                all_sent[j][46] = [200]
                all_sent[j][56] = [200]
        if isatomic(all_sent[j],words) and all_sent[j][5] == all_sent[j][14] and \
            all_sent[j][9] != "=" and all_sent[j][8] != "~":
            consistent = reflex(all_sent,j,tot_sent,prop_sent)
            if not consistent:
                break

        if all_sent[j][46] != "x":
            if all_sent[j][9] == ne:
                non_id.append([all_sent[j][0],all_sent[j][5],all_sent[j][14]])
            else:
                for p in num:
                    if all_sent[j][p] != None and isvariable(all_sent[j][p]):
                        if j == 13 and p == 14:
                            bb = 8
                        rel = ""
                        if relat == "A" or (relat == 'T' and p == 14):
                            kind = 'MOMENT'
                        elif relat == "IR" and p == 5:
                            kind = 'FACT'
                        elif relat == 'AB' or relat == "L" or relat == 'AB' or (relat == 'S' and p == 14) \
                                or (relat == 'WS' and p == 14):
                            kind = 'POINT'
                        elif relat == "G" or (relat == 'N' and p == 14):
                            kind = 'NUMBER'
                        elif relat == "M" and p == 5 or (relat == 'TK' and p == 14):
                            kind = 'MENTAL RELATIONSHIP'
                            rel = "ir"
                        elif relat == "M" and p == 14:
                            kind = 'IMAGINATION'
                        elif relat == "I" and p == 14:
                            kind = "NOUN CONCEPT"
                        elif relat == "H" and p == 14:
                            kind = "NOUN PROPERTY"
                        elif relat == "J" and p == 14:
                            kind = "ADJECTIVIAL PROPERTY"
                        elif relat == "HE" and p == 5:
                            kind = "PARTICLE"
                        elif (relat == 'TK' and p == 14) or (relat == "M" and p == 5):
                            kind = 'THOUGHT'
                        elif relat == "HE" and p == 14:
                            kind = "ENERGY"
                        elif relat == "W" and p == 5:
                            kind = "WHOLE"
                        elif relat == 'P' and p == 14:
                            kind = 'POSSIBLE WORLD'
                        elif relat == "D" and p == 14:
                            kind = 'POSSIBLE RELATIONSHIP'
                        elif relat == 'AL' or (relat == 'WV' and p == 14):
                            kind = 'LETTER'
                        elif (relat == 'TK' or relat == "D") and p == 5:
                            kind = 'MIND'
                        elif relat == "S" and p == 5:
                            kind = 'MATTER'
                        elif relat == "O" and p == 14:
                            kind = 'SENSORIUM'
                        else:
                            kind = ""
                        if len(members) > 30:
                            bb = 7
                        if all_sent[j][8] == "~":
                            kind = ""
                        dummy = cat_atoms(p,j,all_sent,members,basic_objects,kind,bo2,words,consq,rel,basic_cat)
    basic_objects2 = []
    if consistent:
        mem_var = []
        basic_objects2 = copy.deepcopy(basic_objects)
        basic_objects = sorted(basic_objects, key = operator.itemgetter(1,0))
        has2groups = []
        #if something is both matter and a natural whole then it is a natural whole
        #remove blanks in the second dimension
        i = -1
        while i < len(basic_objects) -1:
            i += 1
            if basic_objects[i][0] in nw and basic_objects[i][1] == 'MATTER':
                del basic_objects[i]
                i -= 1
        for i in range(len(members)):
            if i == 13:
                bb = 8
            if members[i][0] == 'v':
                pp = 7
            if members[i][4] == 'general':
                members[i][2] = members[i][2] + "*"
            if members[i][1] == "":
                group = find_group(members[i][2],all_sent,members[i][0],basic_objects)
                if group == None:
                    members[i][1] = 'THING'
                else:
                    if len(group[1]) > 1:
                        if group not in has2groups:
                            has2groups.append(group)
                    group = group[1][0]
                    members[i][1] = group
                    # basic_objects.append([members[i][0],group])

        for i in range(len(members)):
            if members[i][0] == 'u':
                pp = 7
            p = findposinlist(members[i][0],has2groups,0)
            if p > -1:
                members[i][1] = has2groups[p][1][0]

        members = sorted(members, key = operator.itemgetter(1,0))
        list4 = []
        list5 = []
        list6 = []
        list9 = []
        irrel = []
        senti = []
        senti2 = []
        gv_corr = []
        spec_prop = []
        str2 = ""
        str4 = ""
        dis_con = False
        u = 0
        if members != []:
            for i in range(len(members)):
                str1 = members[i][0]
                str3 = members[i][1]
                isirel = members[i][5]
                if str1 == 'p':
                    bb = 7
                if i == 12:
                    bb = 8

                if str1 != str2 and str2 != "":
                    senti3 = senti + senti2
                    list5.append([str2,members[i-1][1],list4,irrel,spec_prop,senti3])
                    qn += 1
                    member_prop.append([str2,members[i-1][1],list6,list4,list9,irrel,u,qn,senti,senti2])
                    u = 0 # number of positions a moment or a number occupies
                    list4 = []
                    list6 = []
                    list9 = []
                    irrel = []
                    senti = []
                    senti2 = []
                    gv_corr = []
                    spec_prop = []
                    if "@" in members[i][3]:
                        gv_corr.append([members[i][3],members[i][7]])
                    if members[i][4] == 1:
                        u += 1
                    if members[i][1] != "":
                        if isirel == "":
                            senti.append(members[i][6])
                            list4.append(members[i][2])
                            list6.append(members[i][3])
                        elif isirel == 'ir' or isirel == 'cn':
                            senti2.append(members[i][6])
                            irrel.append(members[i][2])
                            list9.append(members[i][3])
                        elif isirel == 'sp':
                            spec_prop.append(members[i][2])
                else:
                    if "@" in members[i][3]:
                        gv_corr.append([members[i][3],members[i][7]])
                    if members[i][4] == 1:
                        u += 1
                    if members[i][1] != "":
                        if isirel == "":
                            senti.append(members[i][6])
                            list4.append(members[i][2])
                            list6.append(members[i][3])
                        elif isirel == 'ir' or isirel == 'cn':
                            senti2.append(members[i][6])
                            irrel.append(members[i][2])
                            list9.append(members[i][3])
                        elif isirel == 'sp':
                            spec_prop.append(members[i][2])
                str2 = str1

            if members[i][1] != "":
                qn += 1
                senti3 = senti + senti2
                list5.append([str2,members[i-1][1],list4,irrel,spec_prop,senti3])
                member_prop.append([str2,members[i-1][1],list6,list4,list9,irrel,u,qn,senti,senti2])

            if has2groups != []:
                for i in range(len(has2groups)):
                    str1 = has2groups[i][0]
                    list3 = []
                    for m in range(len(list5)):
                        if list5[m][0] == str1:
                            break
                    for j in range(1,len(has2groups[i][1])):
                        str2 = has2groups[i][1][j].upper()
                        list5.append([str1,str2,list5[m][2],list5[m][3],list5[m][4],list5[m][5]])
                        member_prop.append([str1,str2,member_prop[m][2],member_prop[m][3],\
                            member_prop[m][4],member_prop[m][5],member_prop[m][6],"",member_prop[m][8],member_prop[m][9]])
            list5 = sorted(list5, key = operator.itemgetter(1,0))
            member_prop = sorted(member_prop, key = operator.itemgetter(1,0))
            # dummy = missing_variables(tot_sent,used_var,list5,never_used,all_sent,irrel,property_sent)
            str3 = list5[0][1]
            property_sent.append(["",str3,"","","","",""])
            non_id2 = copy.deepcopy(non_id)
            b = 0
            for i in range(len(list5)):
                str1 = list5[i][0] + " "
                str4 = list5[i][1]
                if i == 11:
                    bb = 7
                if str1 == 'n ':
                    bb = 8
                for k in range(2,5):
                    str2 = ""
                    str5 = ""
                    if len(list5[i][2]) == 0 and k == 2:
                        if list5[i][0] in gen_var:
                            str2 = "[general]"
                        elif list5[i][0] in definite2:
                            str2 = "[definite]"
                        elif list5[i][0] in ind_var:
                            str2 = "[indefinite]"
                    elif k == 4 and list5[i][4] != []:
                        for s in range(len(list5[i][k])):
                            if list5[i][k][s] != "":
                                if str5 == "":
                                    str5 =  " [" + list5[i][k][s]
                                else:
                                    str5 += " & " + list5[i][k][s]
                        str2 += str5 + "]"
                    else:
                        if list5[i][k] != []:
                            for s in range(len(list5[i][k])):
                                if list5[i][k][s] != "":
                                    if str2 == "":
                                        str2 = list5[i][k][s]
                                    else:
                                        str2 += " & " + list5[i][k][s]
                            if k == 3:
                                str2 = " {" + str2 + "}"
                    if k == 2 and str2 == "" and str1 in gen_var:
                        str1 += "[general]"
                    if str2 != "":
                        str1 += str2

                if str4 != str3:
                    property_sent.append(["",str4,"","","","",""])
                str3 = str4
                b += 1
                str7 = str(b) + "a"
                if non_id2 != []:
                    not_id = isnotid(list5[i][0],non_id2,property_sent)
                property_sent.append([member_prop[i][7],str1,"","","","",""])

            str1 = ""
        not_id = []
    bb = 8
    list1 = [basic_objects2,member_prop,property_sent,not_id,tot_sent,consistent]

    return list1


def cat_atoms(j,i,list,members,basic_objects,str1,bo2,words,consq,rel,basic_cat):
    # categorize atoms
    global dv_nam,gen_var,cnjts,ind_var
    atomic_relations = words[22]
    subj = list[i][5]
    relat = list[i][9]
    obj = list[i][14]
    sent = list[i][0]
    bool2 = False
    if list[i][42] == 'n':
        x = 1
    else:
        bool2 = True
    if not bool2:
        orelata = list[i][x] #opposite relata
    else:
        orelata = 1
    #here we determine if the property is irrelevant for determining identity
    bool1 = False
    spec_prop = ["definite","indefinite",'general','particular']
    if list[i][8] == None:
        list[i][8] = ""
    num = [5,14,18,22]
    if subj == "p" and relat == "I" and obj == 'z' and j == 5:
        bb = 8

    bool3 = False
    if relat == "J" and j == 5:
        str6 = findinlist(list[i][14],dv_nam,0,1)
        if str6 in spec_prop:
            bool3 = True
    bool4 = False
    if relat == "I" and j == 5:
        str6 = findinlist(list[i][14],dv_nam,0,1)
        if str6 in basic_cat:
            bool4 = True

    is_con = True
    if list[i][42] not in cnjts and list[i][53] != "an":
        is_con = False

    str5 = ""
    str9 = ""
    if str1 != "" and orelata in gen_var:
        str5 = "ir"
    elif bool3:
        str5 = 'sp'
    elif bool4:
        str5 = "ir"
    elif rel == 'ir':
        str5 = "ir"
    elif relat == "EX":
        str5 = "ir"
    elif j == 14 and relat == 'N':
        str5 = 'ir'
    elif not is_con:
        str5 = 'ir'
        str9 = "cn"
        consq.append(sent)
    elif (relat == "I" or relat == "J") and obj in gen_var:
        str5 = 'ir'
    # else:
    #     for k in num:
    #         if list[i][k] in gen_var or list[i][k] == None:
    #             str5 = 'ir'
    #         else:
    #             str5 = ""
    #             break

    if list[i][14] == None:
        str3 = ""
    else:
        str3 = list[i][14]
    if str9 == "cn":
        tilde = ""
        sent = sent.replace("~","")
        sent = sent.replace("  "," ")
    else:
        tilde = list[i][8]

    #if an object occupies 2 positions of the A relation then it cannot be replaced with
    # an object that occupies 1 position
    u = ""
    if relat == "A" or relat == "G":
        u = 1

    if j == 5:
        if list[i][14] == None:
            str7 = ""
        elif list[i][14] in gen_var:
            str7 = "@"
        else:
            str7 = list[i][14]

        members.append([list[i][j],str1,sent,tilde + list[i][9] \
            + str7,u,str5,list[i],list[i][14]])

    else:
        if list[i][5] in gen_var:
            str7 = "@"
        else:
            str7 = list[i][5]

        members.append([list[i][j],str1,sent,str7 + tilde \
        + list[i][9],u,str5,list[i],list[i][5]])



    if str1 != "":
        if [list[i][j],str1] not in basic_objects:
            basic_objects.append([list[i][j],str1])
            bo2.append(list[i])
    return



def identity(all_sent,tot_sent,basic_objects,words,candd,candd2,conditionals,\
    prop_sent,prop_name,id_num,identities,idf_var,truth_value,greek2):

    global sn,psent,impl,definite2,ind_var,gen_var,idf_var2,never_used
    global instan_time,instan_used,simple_id,cnjts,pn,affneg

    irrel_group = []
    embed_var = []
    dummy = remove_duplicates(all_sent,0)
    if identities != []:
        dummy = simple_id(tot_sent,all_sent,identities)
    dv_list = id_sent(dv_nam,all_sent,irrel_group,embed_var)
    tot_sent.insert(id_num-1,[id_num,dv_list[0],dv_list[1],"",'ID'])
    disjuncts = []
    negat = []
    sent = []
    property_sent = []
    # if proof_type == "l":
    #     pn = sn

    for i in range(len(tot_sent)):
        if tot_sent[i][2] != "":
            sent.append([tot_sent[i][0],tot_sent[i][2]])
            negat.append(tot_sent[i][3])


    list1 = plan(greek2,sent,all_sent,prop_sent,candd,candd2,conditionals, \
                      prop_name,disjuncts,tot_sent,2,negat)
    consistent = list1[0]
    conditionals = list1[1]


    tv = True # tv = truth value

    if proof_type == "l" and consistent:
        instan_used += 1
        k = sn
        g = sn
        tv = "True"
        tot_sent = rearrange(prop_sent, tot_sent, consistent, impl, g, all_sent, \
                             greek2, conditionals)
        # consistent = statement_logic(greek2, prop_sent, all_sent, conditionals, \
        #                              candd, candd2, disjuncts, 0, all_sent)
        # tot_prop_sent.append(prop_sent)
        # return [tot_sent, tv]



    if consistent and impl != nonseq:
        tv = False
    elif impl == nonseq and consistent:
        tv = False
    if not tv:

        if proof_type != "l":
            for i in range(len(conditionals)):
                str3 = conditionals[i][4]
                str3 = enclose(str3)
                def_info = find_sentences(str3)
                for y in range(len(def_info[0])):
                    if os(def_info[0][y]):
                        def_con = def_info[4][y][1]
                        sent_num = def_info[4][y][0]
                        paren_num = def_info[4][y][0][:-1]
                        gparen_num = def_info[4][y][0][:-2]
                        paren_conn = findinlist(paren_num,def_info[4],0,1)
                        gparen_conn = findinlist(gparen_num,def_info[4],0,1)
                        str9 = prop_type(paren_num,gparen_num,paren_conn,gparen_conn,sent_num,def_con)
                        str3 = def_info[0][y]
                        d = findposinlist(str3,all_sent,42)
                        all_sent[d][53] = str9

        bo2=[]
        member_prop = []
        not_id = []

        list1 = cat_err(all_sent,words,basic_objects,bo2,\
                member_prop,not_id,property_sent,tot_sent)
        basic_objects2 = list1[0]
        member_prop = list1[1]
        property_sent = list1[2]
        not_id = list1[3]
        tot_sent = list1[4]
        consistent = list1[5]

    if consistent:
        consistent = axioms(greek2,basic_objects2,bo2,disjuncts,tot_sent,candd,candd2,conditionals,all_sent,\
                       prop_sent,member_prop,not_id)

        # end3

        if proof_type == "l":
            tot_prop_sent.append(prop_sent)
            return [tot_sent, tv]


        if consistent:
            itime = time.time()
            instan_used += 1



            bb = 8
            # dummy = cjcnd(all_sent,conditionals,tot_sent) # this gathers all detached
            # and attatched sentences
            neg_embed = []
            if embed != []:

                list1 = []
                for i in range(len(embed)):
                    for j in range(len(all_sent)):
                        if (all_sent[j][5] == embed[i][42] or all_sent[j][14] == embed[i][42]) \
                            and all_sent[j][8] == "~":
                                neg_embed.append(embed[i][42])
                                list1.append(embed[i])
                all_sent += list1
                list1 = []

            rel_sent = [] # relevant sentence
            rel_prop = [] # relevant propositions (sentence letters)
            list5 = []
            linked = []
            remove_later = []
            pot_id = [] # potential identity
            conditionals2 = copy.deepcopy(conditionals)
            for k in range(len(conditionals2)):
                if conditionals2[k][6] == "":
                    list7 = conditionals2[k][0]
                    conditionals2[k][0] = []
                    conditionals2[k][0].append(list7)
                if conditionals2[k][7] == "":
                    list7 = conditionals2[k][1]
                    conditionals2[k][1] = []
                    conditionals2[k][1].append(list7)

            conjunc = ""
            gen_var2 = [] #general variables
            part_var = [] #particular variables
            # for i in range(len(all_sent)):
            #     dummy = find_gen(all_sent,gen_var2,i,part_var) #find general variables

            for i in range(len(all_sent)):

                if i == 42:
                    bb = 8
                if all_sent[i][8] == "~" or all_sent[i][42] in neg_embed:
                    if all_sent[i][42] in cnjts:
                    # if all_sent[i][42] in cnjts and all_sent[i][46] != "x":
                        bool1 = False
                        for j in range(len(all_sent)):
                            if j == 10 and i == 18:
                                bb = 8

                            if all_sent[j][42] not in cnjts and all_sent[j][46] != "x":
                                str1 = all_sent[i][42]
                                str2 = all_sent[j][42]
                                str1 = str1.replace("~","")
                                str2 = str2.replace("~","")
                                if str1 == str2:
                                    rel_sent.append([all_sent[j][42],all_sent[j]])
                                    remove_later.append(all_sent[j][42])
                                else:
                                    a = len(pot_id)
                                    dummy = instantiable(all_sent,j,i,pot_id,member_prop,True,linked,gen_var2)
                                    if len(pot_id) > a:
                                        bool1 = True
                                        rel_sent.append([all_sent[j][42],all_sent[j]])
                    else:
                        rel_sent.append([all_sent[i][42],all_sent[i]])

            orel_sent = copy.deepcopy(rel_sent) #original relevant sentence

            if rel_sent != []:
                bool1 = False
                i = -1
                while i < (len(rel_sent))-1:
                    i += 1
                    str1 = rel_sent[i][0]
                    k = -1
                    while k < (len(conditionals2))-1:
                        k += 1
                        bool1 = False
                        for q in range(0,2):
                            if bool1:
                                break
                            if q == 0:
                                r = 0
                                s = 1
                            else:
                                r = 1
                                s = 0
                            for m in range(len(conditionals2[k][r])):
                                bool3 = False
                                if conditionals2[k][r] != [""]:
                                    str3 = conditionals2[k][r][m][1] + conditionals2[k][r][m][0]
                                    if str1 == str3:
                                        bool3 = True
                                    elif not os(str3):
                                        d = findposinlist(str3,all_sent,42)
                                        if all_sent[d][53] == "an":
                                            if not check_dimension(rel_sent,0,str3):
                                                rel_sent.append([str3,all_sent[d]])

                                if bool3:
                                    str4 = findinlist(rel_sent[i],all_sent,42,46)
                                    if str4 == "x":
                                        del rel_sent[i]
                                        i -= 1
                                    if r == 0:
                                        r = 1
                                    else:
                                        r = 0
                                    for n in range(len(conditionals2[k][r])):
                                        str12 = conditionals2[k][r][n][1] + conditionals2[k][r][n][0]
                                        if os(str12):
                                            if not check_dimension(rel_sent,0,str12) and str12 not in cnjts:
                                                d = findposinlist(str12,all_sent,42)
                                                rel_sent.append([str12,all_sent[d]])

                                    del conditionals2[k]
                                    bool1 = True
                                    break

            bool1 = False
            kv_found = False
            list1 = []
            if remove_later != []:
                for i in range(len(remove_later)):
                    d = findposinlist(remove_later[i],rel_sent,0)
                    del rel_sent[d]

            #ignores time
            j = -1
            while j < (len(rel_sent)) -1:
                j += 1
                d = findposinlist(rel_sent[j][0],all_sent,42)
                if all_sent[d][46] != "x":
                    for i in range(len(all_sent)):
                        if i == 5 and j == 2:
                            bb = 8
                        dummy = instantiable(all_sent,d,i,pot_id,member_prop,False,linked,gen_var2,embed_var)

            candd2 = copy.deepcopy(candd)
            candd = []
            for i in range(len(conditionals)):
                candd.append([conditionals[i][2],conditionals[i][4],""])
            added = False
            if pot_id != []:
                already_done = []
                pot_id = remove_duplicates2d(pot_id,0,1)
                # pot_id = fix_id(pot_id,rel_sent,all_sent,linked)
                pot_id = areident(pot_id,member_prop,all_sent,dv_nam,tot_sent,candd2,not_id,\
                            candd,prop_sent)

                if pot_id != []:
                    added = new_cond(greek2,pot_id,candd,conditionals,tot_sent,member_prop,\
                        candd2,all_sent,orel_sent)

            if added:
                #we assume that 14 can be none and 18 full, but if 18 is none then the rest must also
                #be none
                list2 = []
                for i in range(len(conditionals)):
                    list2.append(conditionals[i][4])
                    for j in range(len(conditionals[i][38])):
                        d = findposinlist(conditionals[i][38][j],candd2,1)
                        if d > -1:
                            #candd2 used here maybe
                            # print "candd2 used"
                            if candd2[d] not in candd:
                                candd.append(candd2[d])
                st = time.time()
                hh = st - itime
                instan_time += hh
                list1 = statement_logic(greek2,prop_sent,all_sent,conditionals,candd,candd2,disjuncts,0)
                consistent = list1[0]
                conditionals = list1[1]
                # en = time.time()
                # print en-st

        if consistent and impl != nonseq and truth_value == "co":
            print "False: " + tot_sent[0][1]
            tv = "False"
        elif impl == nonseq and not consistent and truth_value == 'ta':
            print "False: " + tot_sent[0][1]
            tv = "False"



            #end4

    if impl != "":
        for i in range(len(prop_sent)):
            if prop_sent[i][1] == top or prop_sent[i][1] == bottom:
                anc1 = prop_sent[i][0]
                break
        if consistent:
            list3 = []
            for i in range(len(prop_sent)):
                if len(prop_sent[i][1]) < 3 and prop_sent[i][1] != top and prop_sent[i][1] != bottom:
                    list3.append([prop_sent[i][1],prop_sent[i][2]])
                    if i == 0:
                        str1 = prop_sent[i][2] + prop_sent[i][1]
                    else:
                        str1 += " " + prop_sent[i][2] + prop_sent[i][1]
            pn += 1
            prop_sent.append([pn,str1,"","","","","","",""])
            list3.sort()
            for i in range(len(list3)):
                if i == 0:
                    str1 = list3[i][1] + list3[i][0]
                else:
                    str1 += " " + list3[i][1] + list3[i][0]
            pn += 1
            prop_sent.append([pn,str1,"","","","","","",""])
            pn += 1
            prop_sent.append([pn,top,"","","","","","",""])

        if not consistent and impl == implies:
            str1 = bottom + " & " + bottom
            str2 = top
        if consistent and impl == implies:
            str1 = bottom + " & " + top
            str2 = bottom
        if not consistent and impl == nonseq:
            str1 = top + " & " + bottom
            str2 = bottom
        if consistent and impl == nonseq:
            str1 = top + " & " + top
            str2 = top
        pn += 1
        prop_sent.append([pn,str1,"","&I",anc1,pn-1,"","","",""])
        pn += 1
        prop_sent.append([pn,str2,"",str2 + "I",pn-1,"","","",""])

    k = sn
    insert_here = sn
    if property_sent != []:
        h = pn - 300
        for i in range(len(tot_sent)-1,0,-1):
            if tot_sent[i][0] != "":
                m = tot_sent[i][0]
                break

        j = 301 - m - 1
        for i in range(len(property_sent)):
            if property_sent[i][0] != "":
                property_sent[i][0] = property_sent[i][0] - j
                k = property_sent[i][0]

        for i in range(len(tot_sent)-1,5,-1):
            if i == 20:
                bb = 8
            try:
                if tot_sent[i][5] != "" and tot_sent[i][5]>300:
                    tot_sent[i][5] = tot_sent[i][5] - j
                if tot_sent[i][6] != "" and tot_sent[i][6]>300:
                    tot_sent[i][6] = tot_sent[i][6] - j
            except IndexError:
                bb = 8

        tot_sent.append(["","","","","","","","",""])
        tot_sent += property_sent
    g = 401 - k -1


######################

    if proof_type == 'l':
        tot_sent = rearrange2(prop_sent, tot_sent, consistent, impl, g, all_sent, greek2,conditionals)
        tot_prop_sent.append(prop_sent)
        return [tot_sent,tv]
    else:
        list3 = rearrange(prop_sent,tot_sent,consistent,impl,g,all_sent,greek2)
        tot_sent = list3[0]
        prop_sent = list3[1]
        tot_prop_sent.append(prop_sent)
        list1 = [tot_sent, tv]
        return list1
    # end5


def rearrange2(prop_sent,tot_sent,consistent,impl,g,all_sent,greek2,conditionals):

    list1 = put_nc_id_ax_df_into_list(tot_sent)
    tot_sent = list1[0]
    new_numbers = list1[1]
    conditionals = renumber_conditionals(conditionals,new_numbers)
    for i in range(len(tot_sent)-1,0,-1):
        if tot_sent[i][4] != "":
            break

    list1 = build_standard_sent_list([], [], \
        tot_sent, conditionals, all_sent, consistent, greek2,i)
    return tot_sent


def subtract_400(prop_sent,g):
    # this function renumbers numbers from 400 down to a more reasonable number
    for i in range(len(prop_sent)):
        if prop_sent[i][0] > 400 and prop_sent[i][0] != "":
            prop_sent[i][0] = prop_sent[i][0] - g
        if prop_sent[i][4] > 400 and prop_sent[i][4] != "":
            prop_sent[i][4] = prop_sent[i][4] - g
        if prop_sent[i][5] > 400 and prop_sent[i][5] != "":
            prop_sent[i][5] = prop_sent[i][5] - g
        if prop_sent[i][6] > 400 and prop_sent[i][6] != "":
            prop_sent[i][6] = prop_sent[i][6] - g
        if prop_sent[i][7] > 400 and prop_sent[i][7] != "":
            prop_sent[i][7] = prop_sent[i][7] - g
    return prop_sent

def put_nc_id_ax_df_into_list(tot_sent):
    #this function takes out sentences proved by NC, AX, RN etc and
    #prepares to put them into new locations
    list1 = []
    list2 = []
    list5 = []
    rn_used = False
    bool1 = False

    for i in range(0,len(tot_sent)):
        if i == 9:
            bb = 7
        str1 = tot_sent[i][4][:2]
        str2 = tot_sent[i][4][:2]
        if tot_sent[i][4] == "" and not bool1:
            list6 = copy.deepcopy(tot_sent[i])
            list5.append(list6)
        elif tot_sent[i][4] == "ID":
            list6 = copy.deepcopy(tot_sent[i])
            list5.append(list6)
            bool1 = True
        elif 'DF' == str1 or 'NC' == str1 or 'AX' == str1 \
             or 'RN' == str2:
            list4 = copy.deepcopy(tot_sent[i])
            list1.append(list4)
            rn_used = True
        elif bool1:
            if str1 == 'DE':
                tot_sent[i][4] = "DF " + tot_sent[i][4][3:]
            elif str1 == 'AY':
                tot_sent[i][4] = "AX ENT"
            list3 = copy.deepcopy(tot_sent[i])
            list2.append(list3)

    if rn_used:
        list7 = rearrange_tot_sent(list5, list1, list2)
        return list7
    else:
        return [tot_sent,[]]

def rearrange_tot_sent(list5,list1,list2):
    # this function puts the tot_sent into a better order
    tot_sent = []
    for i in range(len(list5)):
        tot_sent.append(list5[i])
    for i in range(len(list1)):
        tot_sent.append(list1[i])
    tot_sent.append(["","","","","","","","",""])
    for j in range(len(list2)):
        tot_sent.append(list2[j])

    list1 = []
    j = 0
    for i in range(len(tot_sent)):
        if (i > 3 and tot_sent[i][0] != "") or i <= 3:
            j += 1
            list1.append([tot_sent[i][0],j])
            tot_sent[i][0] = j

    for i in range(len(prop_sent)):
        if i == 53:
            bb = 8
        d = findinlist(prop_sent[i][0],list1,0,1)
        if d != None:
            prop_sent[i][0] = d
        for j in range(4,8):
            if prop_sent[i][j] == None or prop_sent[i][j] == "":
                break
            d = findinlist(prop_sent[i][j],list1,0,1)
            if d != None:
                prop_sent[i][j] = d

    for i in range(len(tot_sent)):
        for j in range(0,5):
            if len(tot_sent[i]) > 5 + j:
                if tot_sent[i][j+5] != "":
                    g = findinlist(tot_sent[i][j+5],list1,0,1)
                    tot_sent[i][j+5] = g
            else:
                break

    return [tot_sent,list1]

def build_standard_conditionals(conditionals):

    standard_cd = []
    for i in range(len(conditionals)):
        standard_cd.append([conditionals[i][2],conditionals[i][37],"","","","",""])

    return standard_cd

def build_standard_sent_list(nonstandard,standard_cj,\
                tot_sent,conditionals,all_sent,consistent,greek2,c=0):

    # this function divides all sentences into standard conjuncts, standard
    # conditionals and non standard sentences
    # it also converts the prop_sent into
    # nat sent and puts them into the tot sent list
    global band_aid_axiom

    if c == 0:
        if band_aid_axiom == 0:
            band_aid_axiom = 1500
        c = tot_sent[-1][0]
    tot_sent.append(["","","","","","","","","",""])
    tot_sent.append(["","_______________________","","","","","","","",""])

    if not consistent:
        d = len(prop_sent)-1
    else:
        d = len(prop_sent)

    for i in range(d):
        if i == 11:
            bb = 8
        if prop_sent[i][0] > c or prop_sent[i][1] == band_aid_axiom:
            if prop_sent[i][1] == bottom:
                tot_sent.append([prop_sent[i][0],str1,prop_sent[i][1],prop_sent[i][2],\
                        prop_sent[i][3],prop_sent[i][4],prop_sent[i][5],prop_sent[i][6],prop_sent[i][7]])
            elif os(prop_sent[i][1]):
                # try:
                str1 = prop_sent[i][2] + findinlist(prop_sent[i][1],prop_name,0,2)
                # except TypeError:
                #     bb = 8
                bool1 = False
                for d in range(len(all_sent)):
                    str3 = all_sent[d][42].replace("~","")
                    if prop_sent[i][1] == str3:
                        bool1 = True
                        break
                if consistent:
                    if bool1:
                        standard_cj.append([prop_sent[i][0],str1,prop_sent[i][1],prop_sent[i][2],\
                        prop_sent[i][3],prop_sent[i][4],prop_sent[i][5],prop_sent[i][6],prop_sent[i][7]])
                    else:
                        nonstandard.append([prop_sent[i][0],str1,prop_sent[i][1],prop_sent[i][2],\
                        prop_sent[i][3],prop_sent[i][4],prop_sent[i][5],prop_sent[i][6],prop_sent[i][7]])

                tot_sent.append([prop_sent[i][0],str1,prop_sent[i][1],prop_sent[i][2],\
                        prop_sent[i][3],prop_sent[i][4],prop_sent[i][5],prop_sent[i][6],prop_sent[i][7]])

            else:
                t = findposinmd(prop_sent[i][1],conditionals,4)
                if prop_sent[i][0] == 32:
                    bb = 8
                if t > -1:
                    if conditionals[t][37] == "" or conditionals[t][37] == None:
                        list2 = get_prop(prop_sent[i][1],True,greek2)
                        conditionals[t][37] = list2[0]
                        list3 = list2[1]
                        str1 = list2[0]
                    else:
                        list3 = conditionals[t][38]
                        str1 = conditionals[t][37]
                else:
                    if i == 55:
                        bb = 8
                    list2 = get_prop(prop_sent[i][1],True)
                    list3 = list2[1]
                    str1 = list2[0]
                bool1 = False
                list4 = mainconn(prop_sent[i][1])
                if list4[0] != "&":
                    for d in range(len(list3)):
                        str4 = list3[d].replace("~","")
                        bool1 = False
                        for e in range(len(all_sent)):
                            str3 = all_sent[e][42].replace("~","")
                            if str4 == str3:
                                bool1 = True
                                break

                tot_sent.append([prop_sent[i][0],str1,prop_sent[i][1],prop_sent[i][2],\
                    prop_sent[i][3],prop_sent[i][4],prop_sent[i][5],\
                                     prop_sent[i][6],prop_sent[i][7]])
                if consistent:
                    if not bool1:
                        nonstandard.append([prop_sent[i][0],str1,"","",\
                        prop_sent[i][3],prop_sent[i][4],prop_sent[i][5],\
                                         prop_sent[i][6],prop_sent[i][7]])

    if not consistent:
        tot_sent.append(prop_sent[-1])


def prepare_disjuncts(conditionals,greek2):

    for i in range(len(conditionals)):
        if conditionals[i][0] == "":
            str1 = enclose(conditionals[i][4])
            def_info = find_sentences(str1)
            conditionals[i][36] = def_info
            list1 = get_prop(conditionals[i][4],True,greek2)
            conditionals[i][37] = list1[0]
            conditionals[i][38] = list1[1]
    return conditionals

def get_detached(standard_cj,all_sent):
    # This puts all natural detached sentences into a list

    detached = []
    for i in range(len(standard_cj)):

        d = findposinmd(standard_cj[i][3] + standard_cj[i][2],all_sent,42)
        if d > -1:
            detached.append(all_sent[d])
    return detached

def get_detached_variables(detached):
    # This categorizes all abbreviations which appear in a detached sentence

    num = [5,14,18,22]
    temp_list = []
    indefinite_concept = findinlist("indefinite",dv_nam,1,0)
    definite_concept = findinlist("definite", dv_nam, 1, 0)
    general_concept = findinlist("general", dv_nam, 1, 0)
    defn = []
    indef = []
    general = []

    for i in range(len(detached)):
        for j in num:
            if isvariable(detached[i][j]):
                str1 = detached[i][j]
                if str1 not in defn and str1 not in indef and str1 not in general:
                    if isinmdlist(detached[i][j],dv_nam,0):
                        defn.append(detached[i][j])
                    elif detached[i][9] == 'J' and detached[i][14] == indefinite_concept:
                        indef.append(detached[i][j])
                    elif detached[i][9] == 'J' and detached[i][14] == definite_concept:
                        defn.append(detached[i][j])
                    elif detached[i][9] == 'J' and detached[i][14] == general_concept:
                        general.append(detached[i][j])
                    else:
                        temp_list.append(detached[i][j])

    indef = categorize_remaining_variables(indef,defn,temp_list)

    return [general,indef,defn]

def categorize_remaining_variables(indef,defn,temp_list):
    #this places the remaining variables in the indefinite list
    for i in range(len(temp_list)):
        if temp_list[i] not in defn:
            if temp_list[i] not in indef:
                indef.append(temp_list[i])
    return indef

def attached_variables(conditionals,detached_var):
    #This determines whether non-definite variables are in the antecedent or consequent

    ant_pot = [] # potentially general or indefinite antecedent variables
    con_pot = []  # potentially general or indefinite consequent variables
    general = []
    indef = detached_var[1]
    defn = detached_var[2]
    spec_var = detached_var[0]
    num = [5,14,18,22]
    num2 = [34,35]

    for i in range(len(conditionals)):
        for m in num2:
            for j in range(len(conditionals[i][m])):
                for n in num:
                    str1 = conditionals[i][m][j][n]
                    if str1 != "" and str1 != None and str1 != "i":
                        if isinmdlist(str1,dv_nam,0):
                            if str1 not in defn:
                                defn.append(str1)
                        elif str1 not in defn and str1 not in indef:
                            if m == 34:
                                if str1 not in ant_pot:
                                    ant_pot.append(str1)
                            else:
                                if str1 not in con_pot:
                                    con_pot.append(str1)


        list1 = variable_type(ant_pot,con_pot)
        general = quick_append(list1[0],general)
        indef = quick_append(list1[1],indef)
    # this is a bandaid, remove this later
    if spec_var in defn:
        defn.remove(spec_var)
    if indef in defn:
        indef.remove(spec_var)
    return [general,indef,defn]

def quick_append(list1,list2):

    for i in range(len(list1)):
        if list1[i] not in list2:
            list2.append(list1[i])
    return list2

def variable_type(ant_pot,con_pot):
    # this determines whether a variable in an attached sentence
    # is general or definite
    general = []
    i = -1
    while i < len(ant_pot) -1:
        i += 1
        j = -1
        while j < len(con_pot) - 1:
            j += 1
            if ant_pot[i] == con_pot[j]:
                general.append(ant_pot[i])
                del ant_pot[i]
                i -= 1
                del con_pot[j]
                j -= 1
                break

    indef = ant_pot + con_pot

    return [general,indef]

def get_id_sent(tot_sent):
    # this function gets the list of identities
    for i in range(len(tot_sent)):
        if tot_sent[i][4] == "ID":
            return [tot_sent[i][0],tot_sent[i][1],"","","",""]

def print_variables(list1,tot_sent):
    # this prints out the variables within the tot_sent list, just above
    # where it prints the attached sentences
    general = list1[0]
    indef = list1[1]
    defn = list1[2]
    identities = get_id_sent(tot_sent)

    str1 = ""
    str2 = ""
    str3 = ""
    j = 0
    if general != []:
        str1 = 'General Variables: '
        for i in range(len(general)):
            str1 += general[i] + " "
    if indef != []:
        str2 = 'Indefinite Variables: '
        for i in range(len(indef)):
            str2 += indef[i] + " "
    if defn != []:
        str3 = 'Definite Variables: '
        for i in range(len(defn)):
            str3 += defn[i] + " "

    for i in range(len(tot_sent)-1,0,-1):
        if len(tot_sent[i][1]) > 15:
            if tot_sent[i][1].startswith('STANDARD ATTA'):
                tot_sent.insert(i,identities)
                tot_sent.insert(i+1,["",str1,"","","","","",""])
                if str2 != "":
                    tot_sent.insert(i+2, ["", str2, "", "", "", "", "", ""])
                    j = 3
                else:
                    j = 2
                if str3 != "":
                    tot_sent.insert(i+j, ["", str3, "", "", "", "", "", ""])
                return tot_sent

def renumber_conditionals(conditionals,new_numbers):
    # this gives conditionals their proper number according to the new
    #numbering system as arrived at in the rearrange_tot_sent function

    if new_numbers == []:
        return conditionals
    for i in range(len(conditionals)):
        for j in range(len(new_numbers)):
            if conditionals[i][2] < 400:
                if conditionals[i][2] == new_numbers[j][0]:
                    conditionals[i][2] = new_numbers[j][1]

    return conditionals


def rearrange(prop_sent,tot_sent,consistent,impl,g,all_sent,greek2,\
              conditionals=[]):

    if proof_type != "l":
        prop_sent = subtract_400(prop_sent,g)
        prop_sent.sort()

    list1 = put_nc_id_ax_df_into_list(tot_sent)
    tot_sent = list1[0]
    new_numbers = list1[1]

    conditionals = renumber_conditionals(conditionals,new_numbers)

    if proof_type == 'l':
        nonstandard = []
        standard_cj = []
        standard_cd = []
        dummy = build_standard_sent_list(nonstandard,standard_cj,\
                tot_sent,conditionals,all_sent,consistent,greek2)
        if consistent:

            if conditionals != []:
                standard_cd = build_standard_conditionals(conditionals)

            dummy = add_stan_sent(nonstandard,standard_cd,standard_cj,tot_sent)

            conditionals = prepare_disjuncts(conditionals,greek2)

            detached = get_detached(standard_cj,all_sent)

            detached_var = get_detached_variables(detached)

            conditionals = link_nat_sent_to_all_sent(conditionals,all_sent)

            list1 = attached_variables(conditionals,detached_var)

            tot_sent = print_variables(list1,tot_sent)
            # tot_sent = relevance(list1,conditionals,standard_cj,tot_sent)


        return tot_sent
    else:
        if not consistent or impl == implies:
            list1 = []
            for i in range(len(prop_sent)-1,0,-1):
                if prop_sent[i][4] == "":
                    break
                if (i != len(prop_sent)-1 and prop_sent[i][0] in list1) or i == len(prop_sent)-1:
                    for j in range(4,8):
                        if prop_sent[i][j] == None or prop_sent[i][j] == "":
                            break
                        list1.append(prop_sent[i][j])
            list1.append(prop_sent[-1][0])
            list1.sort()
            str1 = str(list1[0])
            start = tot_sent[-1][0]
            if start == "":
                for i in range(len(tot_sent)-1,0,-1):
                    if tot_sent[i][0] != "":
                        start = tot_sent[i][0]
                        break

            bool1 = False
            list3 = []
            list2 = []
            for i in range(len(prop_sent)):
                if prop_sent[i][0] <= start:
                    list2.append(prop_sent[i])
                    list3.append([prop_sent[i][0],prop_sent[i][0]])
                elif prop_sent[i][0] in list1:
                    if not bool1:
                        bool1 = True
                        j = list3[-1][0]
                    j += 1
                    list3.append([prop_sent[i][0],j])
                    prop_sent[i][0] = j
                    list2.append(prop_sent[i])
                    anc1 = prop_sent[i][4]
                    nanc1 = findinlist(anc1,list3,0,1)
                    list2[-1][4] = nanc1
                    if prop_sent[i][5] != "" and prop_sent[i][5] != None:
                        anc1 = prop_sent[i][5]
                        nanc1 = findinlist(anc1,list3,0,1)
                        list2[-1][5] = nanc1
                        if prop_sent[i][6] != "" and prop_sent[i][6] != None:
                            anc1 = prop_sent[i][6]
                            nanc1 = findinlist(anc1,list3,0,1)
                            list2[-1][6] = nanc1
                            if prop_sent[i][7] != "" and prop_sent[i][7] != None:
                                anc1 = prop_sent[i][7]
                                nanc1 = findinlist(anc1,list3,0,1)
                                list2[-1][7] = nanc1
            prop_sent = list2

    return [tot_sent,prop_sent]




def relevance(list1,conditionals,standard_cj,tot_sent):



    bb = 8




def add_stan_sent(nonstandard,standard_cd,standard_cj,tot_sent):
    # this adds new sentences to the tot_sent list
    tot_sent.append(["","","","","","","","","",""])
    tot_sent.append(["","_______________________","","","","","","","",""])
    tot_sent.append(["","NONSTANDARD SENTENCES:","","","","","","","",""])
    for i in range(len(nonstandard)):
        tot_sent.append(nonstandard[i])
    tot_sent.append(["","","","","","","","","",""])
    tot_sent.append(["","STANDARD ATTACHED SENTENCES:","","","","","","","",""])
    for i in range(len(standard_cd)):
        tot_sent.append(standard_cd[i])
    tot_sent.append(["","","","","","","","","",""])
    tot_sent.append(["","STANDARD DETACHED SENTENCES:","","","","","","","",""])
    for i in range(len(standard_cj)):
        tot_sent.append(standard_cj[i])

def cjcnd(all_sent,conditionals,tot_sent): # conjuncts and conditionals = cjcnd

    global cnjts
    tot_sent.append(["","","","","","","",""])
    list1 = []
    list2 = []
    rel_relat = []
    for i in range(len(conditionals)):
        if conditionals[i][37] == "":
            str1 = convert2(conditionals[i][4],all_sent)
            conditionals[i][37] = str1
        tot_sent.append(["",conditionals[i][37],"","","","","",""])
    str1 = ""
    for i in range(len(all_sent)):
        if all_sent[i][42] in cnjts:
            g = len(all_sent[i][0])
            h = len(str1)
            if h + g > 79:
                tot_sent.append(["",str1,"","","","","",""])
                str1 = ""
            elif str1 == "":
                str1 = all_sent[i][0]
            else:
                str1 += " " + all_sent[i][0]

    tot_sent.append(["",str1,"","","","","",""])
    tot_sent.append(["","","","","","","",""])
    return

def make_cond(list1):

    more_prop = [unichr(945 + x) for x in range(24)]
    global prop_name
    list2 = []
    prop = list1[4]
    j = -1

    if list1[0] == "":
        list3 = get_prop(list1[4])
        for i in range(len(list3)):
            list2.append([list3[i],more_prop[i]])
            prop = prop.replace(list3[i],more_prop[i])
    else:
        if list1[6] != "":
            for i in range(len(list1[0])):
                j += 1
                tilde = list1[0][i][1]
                list2.append([tilde+list1[0][i][0],more_prop[j]])
                prop = prop.replace(tilde+list1[0][i][0],more_prop[j])
        else:
            j += 1
            tilde = list1[0][1]
            list2.append([tilde+list1[0][0],more_prop[j]])
            prop = prop.replace(tilde+list1[0][0],more_prop[j])

        if list1[7] != "":
            for i in range(len(list1[1])):
                j += 1
                tilde = list1[1][i][1]
                list2.append([tilde+list1[1][i][0],more_prop[j]])
                prop = prop.replace(tilde+list1[1][i][0],more_prop[j])
        else:
            j += 1
            tilde = list1[1][1]
            list2.append([tilde+list1[1][0],more_prop[j]])
            prop = prop.replace(tilde+list1[1][0],more_prop[j])
    sent = prop
    for i in range(len(list2)):
        if "~" in list2[i][0]:
            str2 = list2[i][0].replace("~","")
            tilde = "~"
        else:
            str2 = list2[i][0]
            tilde = ""
        str1 = findinlist(str2,prop_name,0,2)
        sent = sent.replace(list2[i][1],tilde+str1)

    return sent

def fix_id(pot_id,rel_sent,all_sent,linked):

    num = [5,14,18,22]
    useless = []
    tot_var = []

    for i in range(len(pot_id)):
        if pot_id[i][0] not in tot_var:
            tot_var.append(pot_id[i][0])
        if pot_id[i][1] not in tot_var:
            tot_var.append(pot_id[i][1])

    for i in range(len(rel_sent)):
        for j in num:
            if rel_sent[i][j] in tot_var:
                tot_var.remove(rel_sent[i][j])

    done = []
    for i in range(len(pot_id)):
        if i not in done:
            if pot_id[i][1] in tot_var:
                str1 = pot_id[i][0]
                str2 = pot_id[i][1]
                pot_id[i][0] = str2
                pot_id[i][1] = str1
                done.append(i)

def find_gen(all_sent,gen_var2,k,part_var):

    global dv_nam,cnjts
    num = [5,14,18,22]
    if all_sent[k][42] in cnjts:
        for j in num:
            if j > 17 and all_sent[k][j] == None:
                break
            part_var.append(all_sent[k][j])
            if all_sent[k][j] in gen_var2:
                gen_var2.remove(all_sent[k][j])
    else:
        for j in num:
            if j > 17 and all_sent[k][j] == None:
                break
            if not check_dimension(dv_nam,0,all_sent[k][j]) and all_sent[k][j] not in part_var:
                if all_sent[k][j] not in gen_var2:
                    gen_var2.append(all_sent[k][j])




def get_rel_conj(candd,conditionals):

    list2 = []
    for i in range(len(conditionals)):
        for j in range(len(conditionals[i][38])):
            d = findposinlist(conditionals[i][38][j],candd,1)
            if d > -1:
                list2.append(candd[d])
    return list2

def instantiable(all_sent,d,e,pot_id,member_prop,diff_nval,linked,gen_var2,embed_var=[]):

    #diff_nval = different negation value, sentences must have a different negation value
    #d is the rel sent, and e is the non rel sent
    global cnjts,gen_var
    relat1 = all_sent[d][9]
    srelat1 = all_sent[d][15]
    relat = all_sent[e][9]
    srelat = all_sent[e][15]
    temp_linked = []
    temp_linked2 = []
    one_before_zero = 0
    if d == 13 and e == 8:
        bb = 8

    if (diff_nval and all_sent[d][8] != all_sent[e][8]) or not diff_nval:
        if relat == relat1 and srelat == srelat1 and all_sent[d][0] != all_sent[e][0]:
            subj1 = all_sent[d][5]
            obj1 = all_sent[d][14]
            sobj1 = all_sent[d][18]
            subj = all_sent[e][5]
            obj = all_sent[e][14]
            sobj = all_sent[e][18]
            if subj1 == 'v' and relat == "I" and subj == 'u' and relat1 == "I":
                bb = 8
            if subj1 == subj and relat == relat1 and srelat == srelat1 and obj == obj1 \
                and sobj == sobj1:
                return

            elif (subj == subj1 or (subj1 in gen_var or subj in gen_var)) \
                and (obj == obj1 or (obj1 in gen_var or obj in gen_var)) \
                and (sobj == sobj1 or (sobj1 in gen_var or sobj in gen_var)):
                if subj1 == subj:
                    subj = ""
                    subj1 = ""
                if obj1 == obj:
                    obj = ""
                    obj1 = ""
                if sobj1 == sobj:
                    sobj = ""
                    sobj1 = ""
                list4 = [subj,subj1,obj,obj1,sobj,sobj1]
                for p in range(0,5,2):
                    if list4[p] != "":
                        temp_linked.append(list4[p])
                        temp_linked2.append(list4[p+1])
                        bool1 = False
                        for q in range(len(pot_id)):
                            if pot_id[q][0] == list4[p] and pot_id[q][1] == list4[p+1]:
                                bool1 = True
                                break
                        if not bool1:
                            f = findposinlist(list4[p],member_prop,0)
                            g = findposinlist(list4[p+1],member_prop,0)
                            len1 = len(member_prop[f][8])
                            len2 = len(member_prop[g][8])
                            if len1 > len2:
                                pot_id.append([list4[p],list4[p+1],""])
                                one_before_zero = False
                            elif len2 < len1:
                                pot_id.append([list4[p+1],list4[p],""])
                                one_before_zero = True
                            else:
                                if list4[p+1] in gen_var and list4[p] not in gen_var:
                                    pot_id.append([list4[p],list4[p+1],""])
                                elif list4[p+1] not in gen_var and list4[p] in gen_var:
                                    pot_id.append([list4[p+1],list4[p],""])
                                else:
                                    pot_id.append([list4[p],list4[p+1],"="])
                if len(temp_linked) > 1:
                    linked.append(temp_linked)
                    linked.append(temp_linked2)


                # if temp != []:
                #
                #     if one_before_zero == 0:
                #         if pot_id != []:
                #             for t in range(len(temp)):
                #                 bool1 = two_elements_in_list(pot_id,temp[t][0],temp[t][1],0,1)
                #                 if not bool1:
                #                     bool2 = two_elements_in_list(pot_id,temp[t][1],temp[t][0],0,1)
                #                     if bool2:
                #                         one_before_zero = True
                #                         break
                #                 else:
                #                     one_before_zero = False
                #         else:
                #             one_before_zero = False
                #
                #
                #
                #     if one_before_zero:
                #         q = 1
                #         s = 0
                #     else:
                #         q = 0
                #         s = 1
                #
                #     for r in range(len(temp)):
                #         pot_id.append([temp[r][q],temp[r][s],"="])
                return
            else:
                return

def most_common(list1):
    data = Counter(list1)
    return data.most_common(1)[0][0]

def new_cond(greek2,pot_id,candd,conditionals,tot_sent,member_prop,candd2,\
             all_sent,orel_sent):

    global sn,prop_name,prop_sent,dv_nam
    def_var = findinlist("definite",dv_nam,1,0)
    indef = findinlist("indefinite",dv_nam,1,0)
    gen = findinlist("general",dv_nam,1,0)
    pot_anc = [] #ancestor of potential identities
    pot_id = sorted(pot_id, key = operator.itemgetter(1))
    list1 = []
    list2 = []
    anc1 = ""
    anc2 = ""
    conditionals2 = copy.deepcopy(conditionals)
    sec_dim = [] #second dimension
    appears_twice = []
    pot_id2 = copy.deepcopy(pot_id)

    for i in range(len(pot_id)):
        sec_dim.append(pot_id[i][1])

    if len(pot_id) > 1:
        i = -1
        while i < len(pot_id)-1:
            i += 1
            bool1 = check_dimension(list1,1,pot_id[i][1])
            if bool1:
                bool2 = False
                for m in range(len(orel_sent)):
                    if i == -1:
                        break
                    d = findposinlist(orel_sent[m][0],all_sent,42)
                    sent = all_sent[d][0]
                    for n in range(len(all_sent)):
                        sent2 = all_sent[n][0]
                        if all_sent[n][46] != "x" and n != d:
                            if all_sent[n][9] == all_sent[d][9] and all_sent[d][8] == all_sent[n][8]:

                                if all_sent[n][14] == all_sent[d][14]:
                                    f = findposinlist(all_sent[n][5],pot_id,0)
                                    if f > -1:
                                        del pot_id[f]
                                        del pot_id2[f]
                                        del sec_dim[f]
                                        i -= 1
                                        bool2 = True
                                        break

                                elif all_sent[n][5] == all_sent[d][5]:
                                    f = findposinlist(all_sent[n][14],pot_id,0)
                                    if f > -1:
                                        del pot_id[f]
                                        del pot_id2[f]
                                        del sec_dim[f]
                                        bool2 = True
                                        i -= 1
                                        break
                if not bool2:
                    appears_twice.append(pot_id[i][1])
            else:
                list1.append(pot_id[i])

    if len(appears_twice) > 0 and len(pot_id)>1:
        str1 = most_common(sec_dim) # number of times the most abundant member of a list appears in that list
        maxm = sec_dim.count(str1)
        pot_id3 = []
        list2 = []
        i = -1
        while i < len(pot_id)-1:
            i += 1
            if i+1 == len(pot_id)-1:
                if pot_id[i][1] == pot_id[i+1][1]:
                    list2.append(pot_id[i][0])
                    list2.append(pot_id[i+1][0])
                    pot_id3.append([list2,pot_id[i][1]])
                    break
                elif pot_id[i][1] != pot_id[i+1][1]:
                    if list2 != []:
                        list2.append(pot_id[i][0])
                        pot_id3.append([list2,pot_id[i][1]])
                        pot_id3.append([[pot_id[i+1][0]],pot_id[i+1][1]])
                        break
                    else:
                        pot_id3.append([[pot_id[i][0]],pot_id[i][1]])
                        pot_id3.append([[pot_id[i+1][0]],pot_id[i+1][1]])
                        break
            elif pot_id[i][1] == pot_id[i+1][1]:
                list2.append(pot_id[i][0])
            elif pot_id[i][1] != pot_id[i+1][1] and list2 != []:
                list2.append(pot_id[i][0])
                pot_id3.append([list2,pot_id[i][1]])
                list2 = []
            elif pot_id[i][1] != pot_id[i+1][1] and list2 == []:
                pot_id3.append([[pot_id[i][0]],pot_id[i][1]])
        pot_id = pot_id3
    else:
        maxm = 1
        for i in range(len(pot_id)):
            str1 = pot_id[i][0]
            pot_id[i][0] = [str1]

    for i in range(len(pot_id2)):
        b = findposinlist(pot_id2[i][0],member_prop,0)
        c = findposinlist(pot_id2[i][1],member_prop,0)
        str1 = member_prop[b][0]
        str2 = member_prop[c][0]
        e = len(member_prop[b][2])
        f = len(member_prop[c][2])
        anc1 = member_prop[b][7]
        anc2 = member_prop[c][7]
        if anc1 == "":
            for k in range(len(member_prop)):
                if member_prop[k][0] == str1 and member_prop[k][7] != "":
                    anc1 = member_prop[k][7]
                    break
        if anc2 == "":
            for k in range(len(member_prop)):
                if member_prop[k][0] == str2 and member_prop[k][7] != "":
                    anc2 = member_prop[k][7]
                    break

        if pot_id2[i][2] == "":
            os1 = "(" + pot_id2[i][1] + mini_c + pot_id2[i][0] + ")"
            sn += 1
            tot_sent.append([sn,os1,"","","OS",anc1,anc2,"",""])
            pot_id2[i].append(sn)
        else:
            os1 = "(" + pot_id2[i][1] + "=" + pot_id2[i][0] + ")"
            sn += 1
            tot_sent.append([sn,os1,"","","LL",anc1,anc2,"",""])
            pot_id2[i].append(sn)

    if pot_id != []:
        num = [5,14,18,22]

        for i in range(len(conditionals2)):
            if i == 2:
                bb = 8
            ocond2 = conditionals2[i][4]
            res = convert(conditionals2[i])
            ocond_prop = res[0]
            ncond_prop = []
            nprop = []
            for s in range(0,maxm):
                ncond_prop.append(res[0])
                nprop.append(res[0])

            conversion = res[1]
            isrelevant = False
            anc2 = []
            most = 1
            for j in range(len(conditionals2[i][38])):

                oprop = conditionals2[i][38][j] #old proposition (sentence letter)
                osent = findinlist(oprop,all_sent,42,0)
                if osent == None:
                    bb = 8
                g = findposinlist(oprop,all_sent,42)
                if g == -1:
                    print "one of your sentences is missing from the all_sent list"
                new_list = []
                for s in range(0,maxm):
                    list9 = copy.deepcopy(all_sent[g])
                    new_list.append(list9)

                for h in range(len(pot_id)):
                    str2 = pot_id[h][1]

                    if str2 in osent:
                        if all_sent[g][9] == "J" and (all_sent[g][14] == gen or \
                            all_sent[g][14] == def_var or all_sent[g][14] == indef):
                            pass
                        else:
                            for q in num:
                                if all_sent[g][q] == None and q > 17:
                                    break
                                if all_sent[g][q] == str2:
                                    isrelevant = True
                                    for s in range(0,maxm):
                                        if len(pot_id[h][0]) == maxm:
                                            str1 = pot_id[h][0][s]
                                            f = findposmd(str1,str2,pot_id2,0,1,3)
                                            if [s,f] not in anc2:
                                                anc2.append([s,f])
                                        elif len(pot_id[h][0]) != maxm and len(pot_id[h][0]) > 1:
                                            # print "you have not coded for a matrix of instantiations yet"
                                            str1 = pot_id[h][0][0]
                                            f = findposmd(str1,str2,pot_id2,0,1,3)
                                            if [s,f] not in anc2:
                                                anc2.append([s,f])
                                        else:
                                            str1 = pot_id[h][0][0]
                                            f = findposmd(str1,str2,pot_id2,0,1,3)
                                            if [s,f] not in anc2:
                                                anc2.append([s,f])
                                        new_list[s][q] = str1
                                        if s + 1 > most:
                                            most += 1

                oprop = oprop.replace("~","")
                greek_prop = findinlist(oprop,conversion,0,1)
                ocond_prop = ocond_prop.replace(greek_prop,osent)

                for s in range(0,most):
                    if most > 1:
                        bb = 8
                    nsent = build_sent(new_list[s])
                    newp = name_sent(nsent)
                    ncond_prop[s] = ncond_prop[s].replace(greek_prop,nsent)
                    nprop[s] = nprop[s].replace(greek_prop,newp)

            if isrelevant:
                temp8 = []
                for s in range(0,most):
                    anc3 = ""
                    anc4 = ""
                    if unichr(945) in nprop[s]:
                        bb = 8

                    if nprop[s] not in temp8 and unichr(945) not in nprop[s]:
                        temp8.append(nprop[s])
                        for t in range(len(anc2)):
                            if anc2[t][0] == s and anc4 == "" and anc3 != "" and anc2[t][1] != anc3:
                                anc4 = anc2[t][1]
                                break
                            if anc2[t][0] == s and anc3 == "":
                                anc3 = anc2[t][1]
                        sn += 1
                        str1 = "(" + ocond_prop + ") " + conditional + " (" + ncond_prop[s] + ")"
                        str1p = "(" + ocond2 + ") " + conditional + " (" + nprop[s] + ")"
                        tot_sent.append([sn,str1,str1p,"","SUB",anc3,anc4,"",""])
                        list4 = [""] * 15
                        list4[0] = sn
                        list4[1] = str1p
                        list4[2] = ""
                        prop_sent.append(list4)
                        list2 = mainconn(str1p)
                        enc_str1p = enclose(str1p)
                        def_info = find_sentences(enc_str1p)
                        list1 = prepare_iff_elim(greek2,def_info,str1p,all_sent,list2[0],list2[1],sn)
                        list1[37] = str1
                        bool1 = check_dimension(conditionals,4,list1[4])
                        if not bool1:
                            conditionals.append(list1)

    else:
        conditionals += conditionals2

    return True

def convert(list1):

    more_prop = [unichr(945 + x) for x in range(24)]
    list2 = list1[38]
    oprop = list1[4]
    oprop = oprop.replace("~","")
    list3 = []
    k = -1
    list4 = [l1,l2,l3,l4]
    for j in range(len(oprop)):
        str2 = oprop[j:j+1]
        str3 = oprop[j+1:j+2]
        if str2.islower():
            k += 1
            if str3 in list4:
                str2 += str3
                oprop = oprop[:j] + more_prop[k] + oprop[j+2:]
            else:
                oprop = oprop[:j] + more_prop[k] + oprop[j+1:]
            list3.append([str2,more_prop[k]])
    return [oprop,list3]

def convert2(str1,all_sent):

    list4 = [l1,l2,l3,l4]
    j = 0
    while j < len(str1)-1:
        j += 1
        str2 = str1[j-1:j]
        str3 = str1[j:j+1]
        str4 = str1[j+1:j+2]
        if str3.islower():
            if str4 in list4:
                str3 += str4
            if str2 == "~":
                str3 = "~" + str3
            str5 = findinlist(str3,all_sent,42,0)
            g = len(str5)
            str1 = str1[:j] + str5 + str1[j+2:]
            j += g
    return str1

def oinstant(list1,list2,pot_id,oid):

    global gen_var
    # time ignored
    num = [5,14,18]
    for i in num:
        if list2[i] in gen_var and list2[i] != pot_id[1]:
            if [list1[i],list2[i]] not in oid:
                oid.append([list1[i],list2[i]])

def missing_variables(tot_sent,used_var,list5,never_used,all_sent,irrel,property_sent):

    global definite2
    global ind_var
    global gen_var

    var = [definite2,ind_var,gen_var]
    tot_var = definite2 + ind_var + gen_var
    tot_var2 = []
    var_name = ["definite abbreviations:","indefinite abbreviations:","general abbreviations:"]
    for i in range(0,3):
        str1 = ""
        if var[i] != []:
            for j in range(len(var[i])):
                tot_var2.append(var[i][j])
                str1 += " " + var[i][j]
            str1 = var_name[i] + str1
            property_sent.append(["",str1,"","","","","",""])
    str1 = ""
    for i in range(len(used_var)):
        if used_var[i] not in tot_var2 and used_var[i] not in never_used:
            str1 += " " + used_var[i]
    if str1 != "":
        tot_sent.append(["","variable type missing: " + str1,"","","","","","",""])

    str1 = ""
    list2 = []
    for i in range(len(list5)):
        list2.append(list5[i][0])
    for i in range(len(tot_var)):
        if i == 10:
            bb = 8
        if tot_var[i] not in list2 and tot_var[i] not in irrel and \
            tot_var[i] not in never_used:
            str1 += " " + tot_var[i]
    if str1 != "":
        tot_sent.append(["","missing variables:" + str1,"","","","","","",""])

def isnotid(str1,non_id2,property_sent):

    for y in range(len(non_id2)):
        if str1 in non_id2[y][0]:
            property_sent.append(["",non_id2[y][0],"","","","",""])
            del non_id2[y]
            return True
    return False

def asymmetry(all_sent,str1,str2):

    for i in range(len(all_sent)):
        if all_sent[i][46] != "x":
            if all_sent[i][5] == str1 or all_sent[i][5] == str2:
                if all_sent[i][14] == str1 or all_sent[i][14] == str2:
                    return False
    return True



def areident(pot_id,member_prop,all_sent,dv_nam,tot_sent,candd2,not_id,candd,prop_sent):

    pot_id2 = []
    global gen_var
    ax_ent = []
    thing_con = findinlist("thing",dv_nam,1,0) #thing concept, the variable which stands for
    # the concept thing

    w = -1
    while w < len(pot_id)-1:
        w += 1
        if w == 2:
            bb = 8
        b = findposinlist(pot_id[w][0],member_prop,0)
        c = findposinlist(pot_id[w][1],member_prop,0)
        if pot_id[w][1] == "p" and pot_id[w][0] == "u":
            bb = 8
        llist = copy.deepcopy(member_prop[b][8])
        rel_sent2 = copy.deepcopy(member_prop[c][8])
        if rel_sent2 != []:
            bool1 = same_group(member_prop,w,pot_id)
            bool3 = asymmetry(all_sent,pot_id[w][0],pot_id[w][1])
            # if not bool3:
                # print 'asymmetry used'
            if member_prop[b][6] != member_prop[c][6]:
                no_pos = False
            else:
                no_pos = True # number of positions = no_pos
            if bool1 and bool3 and no_pos:
                bool4 = isnotid2(pot_id[w],not_id)
                if not bool4:
                    s = -1
                    while s < len(rel_sent2) -1:
                        s += 1
                        l = -1
                        bool2 = False
                        if thing_con != None:
                            if rel_sent2[s][9] == "I" and rel_sent2[s][14] == thing_con:
                                ax_ent.append(member_prop[b][0])
                                if s + 1 == len(rel_sent2):
                                    break
                                else:
                                    s += 1
                        while l < len(llist) -1:
                            l += 1
                            if l == 2:
                                dd = 8
                            temp_str1a = rel_sent2[s][0]
                            temp_str2a = llist[l][0]
                            bool1 = equality2(rel_sent2,llist,s,l,pot_id,w,pot_id2)
                            if bool1 == 'y' or bool1 == 'm':
                                del rel_sent2[s]
                                s -= 1
                                del llist[l]
                                bool2 = True
                                break
                        if not bool2:
                            dummy = del_pi(pot_id,pot_id2,w)
                            if pot_id[w] in ax_ent:
                                ax_ent.remove(pot_id[w])
                            del pot_id[w]
                            w -= 1
                            break
                else:
                    del pot_id[w]
                    w -= 1
                    break
            else:
                dummy = del_pi(pot_id,pot_id2,w)
                if pot_id[w] in ax_ent:
                    ax_ent.remove(pot_id[w])
                del pot_id[w]
                w -= 1
        else:
            bool1 = same_group(member_prop,w,pot_id)
            bool3 = asymmetry(all_sent,pot_id[w][0],pot_id[w][1])
            # if not bool3:
            #     print 'asymmetry used'
            bool4 = isnotid2(pot_id[w],not_id)
            if member_prop[b][6] != member_prop[c][6] and member_prop[c][6] != 0:
                no_pos = False
            else:
                no_pos = True # number of positions = no_pos
            if not bool1 or not bool3 or bool4 or not no_pos:
                dummy = del_pi(pot_id,pot_id2,w)
                if pot_id[w] in ax_ent:
                    ax_ent.remove(pot_id[w])
                del pot_id[w]
                w -= 1
    if ax_ent != []:
        dummy = axiom_entity(ax_ent,thing_con,tot_sent,candd2,candd,prop_sent)

    return pot_id

def isnotid2(lst,not_id):

    for i in range(len(not_id)):
        if lst[0] in not_id[i] and lst[1] in not_id[i]:
            return True
    return False

def del_pi(pot_id,pot_id2,w): # delete potential identities

    str1 = pot_id[w][0] + pot_id[w][1]
    d = findposinlist(str1,pot_id2,2)
    if d > -1:
        del pot_id[w]
        w -= 1

def same_group(member_prop,w,pot_id):

    bool1 = False
    for i in range(len(member_prop)):
        if bool1:
            break
        if member_prop[i][0] == pot_id[w][0] and member_prop[i][1] == "THING":
            return True
        elif member_prop[i][0] == pot_id[w][1] and member_prop[i][1] == "THING":
            return True
        elif member_prop[i][0] == pot_id[w][0]:
            for j in range(i+1,len(member_prop)):
                if member_prop[j][1] == member_prop[i][1]:
                    if member_prop[j][0] == pot_id[w][1]:
                        return True
                else:
                    break
        elif member_prop[i][0] == pot_id[w][1]:
            for j in range(i+1,len(member_prop)):
                if member_prop[j][1] == member_prop[i][1]:
                    if member_prop[j][0] == pot_id[w][0]:
                        return True
                else:
                    break

    return False

# simple matrix
    # y = 0
    # for n in range(y,g-1):
    #     y += 1
    #     h = y
    #     while h < g:
    #         h += 1
    #         list4.append([n,h-1])

def axiom_entity(ax_ent,thing_con,tot_sent,candd2,candd,prop_sent):

    global sn,cnjts
    for i in range(len(ax_ent)):
        list1 = [None] * 80
        list1[5] = ax_ent[i]
        list1[9] = "I"
        list1[14] = thing_con
        new_sent = build_sent(list1)
        newp = name_sent(new_sent)
        sn += 1
        candd2.append([sn,newp,""])
        candd.append([sn,newp,""])
        cnjts.append(newp)
        prop_sent.append([sn,newp,"","","","","","","",""])
        tot_sent.append([sn,new_sent,newp,"","AY ENT","","","",""])

def isrel(str1,all_sent):
    #if the sentence has not already appeared since we are dealing with nonatoms, then
    #we do not need to infer it
    str1 = str1.replace("~","")
    for i in range(len(all_sent)):
        str2 = all_sent[i][42]
        str2 = str2.replace("~","")
        if str2 == str1:
            return True
    return False



def equality2(rel_sent2,llist,s,l,pot_id,w,pot_id2):

    num = [5,14,15,18,19,22]
    list2 = []
    lvar = pot_id[w][0] #long variable
    svar = pot_id[w][1] # short variable
    kind = pot_id[w][2]
    ssent = rel_sent2[s][0] #short sentence
    lsent = llist[l][0] # long sentence
    global gen_var
    status = 'y' #y = yes

    lpos = findin1dlist(lvar,llist[l]) # long position
    spos = findin1dlist(svar,rel_sent2[s]) # short position


    if svar == rel_sent2[s][5]:
        b = 14
        c = 5
    else:
        b = 5
        c = 14

    if rel_sent2[s][9] != llist[l][9]:
        return 'n' #n = no
    if lpos != spos:
        return 'n'
    elif rel_sent2[s][8] != llist[l][8]:
        return 'n'
    elif rel_sent2[s][8] + rel_sent2[s][9] == llist[l][8] + llist[l][9] and llist[l][9] != "=" and (rel_sent2[s][b] == llist[l][c] or rel_sent2[s][c] == llist[l][b]):
        #this is for sentences of the form cAFd & dAFe
        return 'n'
    elif rel_sent2[s][0] == llist[l][0]:
        return 'n'
    else:
        for i in num:
            if rel_sent2[s][i] == None and llist[l][i] == None:
                break
            elif rel_sent2[s][i] == svar and llist[l][i] == lvar:
                pass
            elif equality3(pot_id,w,rel_sent2,llist,i,s,l):
                pass
            elif rel_sent2[s][i] == llist[l][i] or (rel_sent2[s][i] == svar and llist[l][i] == lvar):
                pass
            elif rel_sent2[s][i] in gen_var:
                status = 'm' # m = maybe
                pot_id2.append([lvar,svar,llist[l][i]+rel_sent2[s][i]])
            elif rel_sent2[s][i] != llist[l][i]:
                return "n"
        return status

def equality3(pot_id,w,rel_sent2,llist,i,s,l):

    if len(pot_id) > 1 and w > 0:
        for k in range(len(pot_id)):
            if w != k:
                if rel_sent2[s][i] == pot_id[k][1] and llist[l][i] == pot_id[k][0]:
                    return True
        return False
    else:
        return False

def already_identical(identities,str1,str2):

    for i in range(len(identities)):
        if str1 in identities[i][0] and str2 in identities[i][0]:
            return True
    return False

def arentident(jobj, iobj,non_id):

    for i in range(len(non_id)):
        if (jobj in non_id[i][0] and iobj in non_id[i][0]):
            return True
    return False

def new_sentence(tot_sent,  old_list, list1, list2, list3, quant, rule,conn = iff,anc1 = "",anc2 = ""):

    global prop_name,psent,sn
    if old_list[0] == None:
        old_sent = build_sent(old_list)
        old_prop = findinlist(old_sent2, prop_name, 1,0)
    else:
        old_sent = old_list[0]
        old_prop = old_list[42]

    if list1[0] == None:
        str1 = build_sent(list1)
    else:
        str1 = list1[0]
    str1v = name_sent(str1)
    list1[0] = str1
    list1[42] = str1v
    if quant == 2:
        str2 = build_sent(list2)
        str2v = name_sent(str2)
    if list3 != "":
        str3 = build_sent(list3)
        str3v = name_sent(str3)
        list3[0] = str3
        print 'you have not coded for three new sentences yet'
        sys.exit()
    if quant == 1:
        str1 = old_sent + ' ' + conn + ' ' + str1
        str1v = old_prop + ' ' + conn + ' ' + str1v
    elif quant == 2:
        str1 = '(' + old_sent + ' & ' + str2 + ') ' + conditional + ' ' + str1
        str1v = '(' + old_prop + ' & ' + str2v + ') ' + conditional + ' ' + str1v
    elif quant == 3:
        str1 = '(' + old_sent + ' & ' + str2 + " & " + str3 + ') ' + conditional + ' ' + str1
        str1v = '(' + old_prop + ' & ' + str2v + "& " + str3v + ') ' + conditional + ' ' + str1v

    g = findinlist(str1,tot_sent,2,0,True)
    if g == -1 and quant != 3:
        sn += 1
        tot_sent.append([sn, str1, str1v, "", rule, anc1, anc2,"",""])




def check_dimension(list1, i, str1,bool1 = False,k=0):

    if not bool1:
        for j in range(len(list1)):
            if list1[j][i] == str1:
                return True
        return False
    else:
        for j in range(len(list1)):
            if j != k:
                if list1[j][i] == str1:
                    return True
        return False

def check_dimension2d(list1, i,j, str1):

    for k in range(len(list1[i])):
        if list1[k][i][j] == str1:
            return True
    return False

#################################################

## The following functions are for statement logic


def name_conditional(list1):

    # when using this function the list1 must be outputted from find_sentences
    # and you must use the 0th element since those sentences do not have negation signs
    global prop_var
    global prop_name
    skel_string = list1[5]
    list2 = []

    for i in range(1, len(list1[6])):
        if list1[6][i] != None and list1[6][i] != "":
            str3 = list1[0][i]
            str3 = remove_outer_paren(str3)
            str4 = copy.copy(str3)
            str4 = str4.replace(" ","")
            str1 = findinlist(str4,prop_name,1,0)
            if str1 != None:
                str2 = list1[1][i] + str1
                list2.append(str1)
                skel_string = skel_string.replace(list1[6][i][1], str2)
            else:
                str2 = prop_var[0]
                list2.append(str2)
                del prop_var[0]
                prop_name.append([str2, str4,str3])
                str2 = list1[1][i] + str2
                skel_string = skel_string.replace(list1[6][i][1], str2)
    return [skel_string, list2]

def tilde_removal(str1):


    str4 = ""
    if str1.find("~") > -1:
        str4 = "~"
        str1 = str1.replace("~","")
    return [str1,str4]

def tilde_removal2(str1):

    j = 0
    if str1[:2] == "~(":
        for i in range(len(str1)):
            str2 = str1[i:i+1]
            if str2 == "(":
                j += 1
            elif str2 == ")":
                j -= 1
            if j == 0 and i > 0:
                if i == len(str1) -1:
                    str1 = str1[1:]
                    str4 = "~"
                    return [str1, str4]
                else:
                    return [str1,""]
    elif str1[0] == "~" and str1[1].islower() and os(str1):
        str1 = str1[1:]
        str4 = "~"
    else:
        str4 = ""
    return [str1,str4]

def simple_sent_name(str1):

    str1 = remove_outer_paren(str1)
    str2 = findinlist(str1,prop_name,1,0)
    if str2 == None:
        ostring = str1.replace(" ","")
        str2 = prop_var[0]
        del prop_var[0]
    prop_name.append([str2, ostring,str1])
    return str2

def is_conjunction(str1):

    if str1.count(idisj) == 0 and str1.count(iff) == 0 and \
        str1.count(conditional) == 0 and str1.count('&') > 0 and str1.count(xorr) == 0:
        return True
    else:
        return False


def get_sentence_abbreviations(list1):
    # this extracts the sentence abbreviations from a complex attached sentence
    list2 = []
    for i in range(len(list1)):
        if os(list1[i]):
            list2.append(list1[i])
    return list2

def get_conjuncts(str1, bool1 = False):
    # remove outparent if true
    global subscripts
    arr1 = []
    if bool1:
        str1 = remove_outer_paren(str1)

    j = 0
    k = 1
    for i in range (len(str1)):
        str2 = str1[i:i+1]
        str5 = str1[i+1:i+2]
        if i > 0:
            str4 = str1[i-1:i]
        else:
            str4 = ""
        if str2 == "(":
            j += 1
        elif str2 == ")":
            j -= 1

        if j == 1 and str2 == "(" and str4 != "~":
            k = i
        elif j == 1 and str4 == "~" and str2 == "(":
            k = i - 1

        if (j==0 and str2 == ")") or (j == 0 and str2.islower()):
            if str2 == ")":
                str3 = str1[k:i+1]
            else:
                if str1[i-1:i] == "~" and str5 not in subscripts:
                    str3 = "~" + str2
                elif str1[i-1:i] != "~" and str5 not in subscripts:
                    str3 = str2
                elif str1[i-1:i] != "~" and str5 in subscripts:
                    str3 = str2 + str5
                    str2 = str2 + str5
                elif str1[i-1:i] == "~" and str5 in subscripts:
                    str3 = "~" + str2 + str5
                    str2 = str2 + str5

            k = 1
            str3 = str3.strip()
            arr1.append(str3)



    return arr1




def get_prop(str1,recon=False,greek2=[]):

    global subscripts
    arr1 = []
    gr_lst = []
    if str1 == "n " + iff + " d"+l1:
        bb = 8



    for i in range (len(str1)):
        str2 = str1[i:i+1]
        str5 = str1[i+1:i+2]
        if i > 0:
            str4 = str1[i-1:i]
        else:
            str4 = ""
        if str2.islower():
            if str1[i-1:i] == "~" and str5 not in subscripts:
                str3 = "~" + str2
            elif str1[i-1:i] != "~" and str5 not in subscripts:
                str3 = str2
            elif str1[i-1:i] != "~" and str5 in subscripts:
                str3 = str2 + str5
            elif str1[i-1:i] == "~" and str5 in subscripts:
                str3 = "~" + str2 + str5

            if recon:
                if not isinmdlist(str3,gr_lst,0):
                    if str3[0] == "~":
                        str6 = str3[1:]
                    else:
                        str6 = str3
                    if greek2 == []:
                        greek2 = copy.deepcopy(greek)
                    gr_lst.append([str6,greek2[0]])
                    del greek2[0]


            str3 = str3.strip()
            arr1.append(str3)

    if recon:
        if str1[0] == "~":
            i = 0
        else:
            i = -1
        while i < len(str1)-1:
            i += 1
            str3 = str1[i:i+1]
            if str3.islower():
                str4 = str1[i+1:i+2]
                if str4 in subscripts:
                    str3 = str3+str4
                str5 = findinlist(str3,gr_lst,0,1)
                if str4 in subscripts:
                   str1 = str1[:i] + str5 + str1[i+2:]
                else:
                    str1 = str1[:i] + str5 + str1[i+1:]

        for i in range(len(gr_lst)):
            str7 = gr_lst[i][1]
            str8 = gr_lst[i][0]
            str3 = findinlist(str8,prop_name,0,2)
            str1 = str1.replace(str7,str3)

        return [str1,arr1]


    return arr1


def link_nat_sent_to_all_sent(conditionals,all_sent):
    # this takes the sentences in 37 and puts them into list 34,35,33 etc
    ant = ['a','b','x','d']
    con = ['f','q','y','g']
    third_disjunct = 'd3'
    fourth_disjunct = 'd4'
    fifth_disjunct = 'd5'
    sixth_disjunct = 'd6'

    for m in range(len(conditionals)):
        list7 = conditionals[m]
        antecedent = []
        consequent = []
        third_d = []
        fourth_d = []
        fifth_d = []
        sixth_d = []
        def_info = list7[36]

        for i in range(len(list7[38])):
            bool1 = False
            for j in range(len(all_sent)):
                str1 = list7[38][i]
                truth_value = ""
                if str1[0] == "~":
                    str1 = str1[1:]
                    truth_value = "~"
                str2 = all_sent[j][42]
                if str2[0] == "~":
                    str2 = str2[1:]
                if str1 == str2:
                    list2 = copy.deepcopy(all_sent[j])
                    o = findin1dlist(list7[38][i],def_info[3])
                    if def_info[4][o][0] == None:
                        bb = 8

                    k = def_info[4][o][0]
                    list2[8] = truth_value
                    list2[43] = k[:-1]
                    list2[44] = k
                    list2[45] = len(k)
                    bool1 = True
                    list2 = ancestor_numbers(list2,k,def_info)
                    if list2[53][-1] in ant:
                        antecedent.append(list2)
                    elif list2[53][-1] in con:
                        consequent.append(list2)
                    elif list2[53] == third_disjunct:
                        third_d.append(list2)
                    elif list2[53] == fourth_disjunct:
                        fourth_d.append(list2)
                    elif list2[53] == fifth_disjunct:
                        fifth_d.append(list2)
                    elif list2[53] == sixth_disjunct:
                        sixth_d.append(list2)
                    else:
                        print 'you did not categorize the attached sentences correctly'
                        sys.exit()
            if not bool1:
                str1 = findinlist(str1,prop_name,0,2)
                print "sentence " + list7[38][i] + " - " + str1 + " was not found in the all sent list"
                sys.exit()
        list7[34] = antecedent
        list7[35] = consequent
        list7[33] = third_disjunct
        list7[32] = fourth_disjunct
        list7[31] = fifth_disjunct
        list7[30] = sixth_disjunct
        conditionals[m] = list7

    return conditionals

def ancestor_numbers(list2,k,def_info):
    # this determines the number and connective of the ancestors of a
    # sent in the conditional
    list2[53] = None
    self_num = k[-1]
    if len(k) == 4:
        ggparen_num = k[0]
        gparen_num = k[:2]
        paren_num = k[:3]
        ggparen_conn = findinlist(ggparen_num,def_info[4],0,1)
        gparen_conn = findinlist(gparen_num,def_info[4],0,1)
        paren_conn = findinlist(paren_num,def_info[4],0,1)
        ggparen_conn = convert_con_to_letter(ggparen_conn,gparen_num[-1])
        gparen_conn = convert_con_to_letter(gparen_conn,paren_num[-1])
        paren_conn = convert_con_to_letter(paren_conn,self_num)
        list2[45] = 4
        list2[46] = paren_conn
        list2[47] = gparen_conn
        list2[48] = ggparen_conn
        list2[53] = paren_conn + gparen_conn + ggparen_conn

    elif len(k) == 3:
        gparen_num = k[0]
        paren_num = k[:2]
        gparen_conn = findinlist(gparen_num,def_info[4],0,1)
        paren_conn = findinlist(paren_num,def_info[4],0,1)
        gparen_conn = convert_con_to_letter(gparen_conn,paren_num[-1])
        paren_conn = convert_con_to_letter(paren_conn,self_num)
        list2[45] = 3
        list2[46] = paren_conn
        list2[47] = gparen_conn
        list2[53] = paren_conn + gparen_conn

    elif len(k) == 2:
        paren_num = k[0]
        paren_conn = findinlist(paren_num,def_info[4],0,1)
        paren_conn = convert_con_to_letter(paren_conn,self_num)
        list2[45] = 2
        list2[46] = paren_conn
        list2[53] = paren_conn

    elif len(k) == 5:
        print "you have not coded for attached sentences with 5 generations yet"
        sys.exit()

    if list2[53] == None:
        print "the number ancestor function is messed up"
        sys.exit()
    return list2


def convert_con_to_letter(str1,str2):
    # this converts a connective to a letter
    if str1 == iff and str2 == '1':
        return 'b'
    elif str1 == iff and str2 == '2':
        return 'f'
    elif str1 == conditional and str2 == '1':
        return 'a'
    elif str1 == conditional and str2 == '2':
        return 'q'
    elif str1 == xorr and str2 == '1':
        return 'x'
    elif str1 == xorr and str2 == '2':
        return 'y'
    elif str1 == idisj and str2 == '1':
        return 'd'
    elif str1 == idisj and str2 == '2':
        return 'g'
    elif str1 == idisj and str2 == '3':
        return 'd3'
    elif str1 == idisj and str2 == '4':
        return 'd4'
    elif str1 == idisj and str2 == '5':
        return 'd5'
    elif str1 == idisj and str2 == '6':
        return 'd6'


    elif str1 == "&":
        return 'c'
    else:
        print 'the convert con to letter function is messed up'
        # sys.exit()

def prepare_iff_elim(greek2,def_info,str2,all_sent,mainc,s,num = "",tot_sent = []):

    global sn

    list7 = [""] * 39
    list7[36] = def_info
    if num == "":
        list7[2] = sn + 1
    else:
        list7[2] =  num

    str2 = remove_outer_paren(str2)
    if str2 == "k " + iff + " z":
        bb = 8
    list7[4] = str2
    list7[5] = ""
    if mainc == iff:
        list7[3] = "e"
    else:
        list7[3] = "c"

    str8 = str2[: s - 1]
    str8 = str8.strip()
    str9 = str2[s+1:]
    str9 = str9.strip()
    bool1 = True
    bool2 = True
    list8 = mainconn(str8)
    list2 = tilde_removal2(str8)
    if list8[0] != "&" or (list2[1] == "~" and list8[0] != ""):
        list2[0] = remove_outer_paren(list2[0])
        list7[0] = [list2[0],list2[1]]
        bool1 = False
    list8 = mainconn(str9)
    list2 = tilde_removal2(str9)
    if list8[0] != "&" or (list2[1] == "~" and list8[0] != ""):
        list2[0] = remove_outer_paren(list2[0])
        list7[1] = [list2[0],list2[1]]
        bool2 = False
    list4 = [bool1, bool2]
    for j in range(0, 2):
        if list4[j]:
            if j == 0:
                str7 = str8
            else:
                str7 = str9
            list2 = mainconn(str7)
            if list2[0] == '&':
                list3 = get_conjuncts(str7, True)
                list6 = []
                for k in range(len(list3)):
                    list5 = tilde_removal2(list3[k])
                    list5[0] = remove_outer_paren(list5[0])
                    list6.append([list5[0],list5[1]])
                if j == 0:
                    list7[0] = list6
                    list7[6] = str8
                    if iff in str8 or conditional in str8:
                        list7[27] = True
                    else:
                        list7[27] = False
                else:
                    list7[1] = list6
                    list7[7] = str9
                    if iff in str9 or conditional in str9:
                        list7[28] = True # we cannot negate the antecedent of this
                    # sentence because conditionals or biconds usually have general
                    # variables in them
                    else:
                        list7[28] = False

    list9 = get_prop(str2,True,greek2)
    list7[38] = list9[1]
    list7[37] = list9[0]
    if list9[0] == None or list9[0] == "":
        bb = 8

    return list7

def islist(list1):

    if list1[1] == '~' or list1[1] == "":
        return False
    else:
        return True

def new_prop(all_sent,prop_sent, str1, ng, asp, anc1, anc2, anc3 = None, anc4 = None, \
             is_premise = False, num = "",ostring = ""):

    if ng == None:
        ng = ""
    global sn,pn
    global cnjts

    if str1 == "k" and ng == "~":
        bb = 8

    if os(str1):
        cnjts.append(ng+str1)

    if ng == "":
        str1 = remove_outer_paren(str1)
    str2 = findinlist(str1,prop_sent,1,2)
    if str2 == ng:
        return True
    elif str2 == None:
        if is_premise:
            # sn = num
            prop_sent.append([num, str1, ng, "", "", "", None, None, ostring, None, None, \
            None, None, None, None])
        else:
            pn += 1
            prop_sent.append([pn, str1, ng, asp, anc1, anc2, None, None, None, None, None, \
            None, None, None, None])
        return True
    elif str2 != ng:
        pn += 1
        prop_sent.append([pn, str1, ng, asp, anc1, anc2, None, None, None, None, None, \
        None, None, None, None])
        anc2 = findinlist(str1,prop_sent,1,0)
        pn += 1
        if not os(str1):
            str1 = "(" + str1 + ")"
        str1 = str1 + " & " + "~" + str1
        prop_sent.append([pn, str1, "", "&I", pn-1, anc2, None, None, None, None, None, \
        None, None, None, None])
        str1 = bottom
        pn += 1
        prop_sent.append([pn, str1, "", bottom + "I", pn-1, None, None, None, None, None, None, \
        None, None, None, None])
        return False

def many_cond(greek2,all_sent,candd,candd2, conditionals, kind, asp, anc2, f, g, r):

    original_conditional = copy.deepcopy(conditionals[g])
    list1 = conditionals[g][f]
    del list1[0]
    # this list allows us to keep track of the ancestors even if we don't detach a
    # a part of the conditionals on the first time
    if conditionals[g][8] == "":
        conditionals[g][8] = [candd[r][0]]
    else:
        conditionals[g][8].append(candd[r][0])

    if f == 1:
        h = 7
    else:
        h = 6
    list2 = []
    list2.append([candd[r][1],candd[r][2]])
    if list1 == []:
        cjct = conditionals[g][h]
        consistent = new_prop_sent(greek2,all_sent,"", kind, asp, "",anc2, \
                    conditionals,g,candd,candd2, conditionals[g][8], cjct)
        if not consistent:
            return [False,conditionals]
        else:
            return [True,conditionals]
    j = -1
    while j < len(list1)-1:
        j += 1
        str2 = list1[j][0]
        neg2 = list1[j][1]
        for i in range(len(candd)):
            if i != r:
                str1 = candd[i][1]
                ng = candd[i][2]
                anc1 = candd[i][0]
                if str1 == str2 and ng == neg2:
                    del list1[j]
                    j -= 1
                    list2.append([str1, ng])
                    conditionals[g][8].append(anc1)
                    if list1 == []:
                        cjct = conditionals[g][h]
                        consistent = new_prop_sent(greek2,all_sent,"", kind, asp, "",anc2, \
                                    conditionals,g,candd,candd2, conditionals[g][8], cjct)
                        if not consistent:
                            return [False,conditionals]
                        else:
                            return [True,conditionals]
                    else:
                        conditionals[g][8] = None
                        break
                elif str1 == str2 and ng != neg2:
            # the point of having blank returns is because if it returns true
            # then we need to subtract the conditional counter, here g, by 1
                    conditionals[g][8] = ""
                    return [True,conditionals]
    conditionals[g] = original_conditional
    conditionals[g][f] = list1
    conditionals[g][8] = ""
    return [True,conditionals]

def modus_ponens(greek2,all_sent,conditionals, candd,candd2, prop_sent,kind):

    r = -1
    while r < len(candd) -1:
        if conditionals == []:
            return [True,conditionals]
        r += 1
        if r == 27:
             bb = 7
        str1 = candd[r][1]
        if str1 == 'u':
            bb = 8
        detach_sent_truth_val = candd[r][2]
        anc1 = candd[r][0]
        temp_detach_sent = copy.copy(str1)
        temp_detach_sent = temp_detach_sent.replace(" ","")
        temp_detach_sent = remove_outer_paren(temp_detach_sent)
        g = -1
        while g < len(conditionals) -1:
            g += 1
            if g == 2 and r==44:
                bb = 7
            if conditionals[g][0] != "":

                str12 = conditionals[g][3]
                if str12 != 'd':
                    anc2 = conditionals[g][2]
                    if conditionals[g][6] == "":
                        antec_conjunct = ""
                        temp_ant = conditionals[g][0][0]
                        temp_nega = conditionals[g][0][1]
                    else:
                        antec_conjunct = conditionals[g][6]
                        temp_ant = conditionals[g][0][0][0]
                        temp_nega = conditionals[g][0][0][1]
                    if conditionals[g][7] == "":
                        conseq_conjunct = ""
                        temp_con = conditionals[g][1][0]
                        temp_negc = conditionals[g][1][1]
                    else:
                        conseq_conjunct = conditionals[g][7]
                        temp_con = conditionals[g][1][0][0]
                        temp_negc = conditionals[g][1][0][1]
                    temp_ant = temp_ant.replace(" ","")
                    temp_con = temp_con.replace(" ","")
                    temp_ant = remove_outer_paren(temp_ant)
                    temp_con = remove_outer_paren(temp_con)

                    for f in range(0,2):
                        if f == 0 and temp_detach_sent == temp_ant:
                            if detach_sent_truth_val == temp_nega:
                                if str12 == 'c':
                                    str13 = "MP"
                                else:
                                    str13 = "EE"
                                if antec_conjunct != "" :
                                    list1 = many_cond(greek2,all_sent,candd,candd2, conditionals, "con", str13, \
                                                      anc2, f, g, r)
                                    consistent = list1[0]
                                    conditionals = list1[1]
                                    if not consistent:
                                        return [False,conditionals]
                                    elif consistent:
                                        del conditionals[g]
                                        g -= 1
                                        break
                                else:
                     # con indicates that the consequent of the conditional is to be detached
                     #
                                    consistent = new_prop_sent(greek2,all_sent,"", "con", \
                                        str13, anc1, anc2,conditionals,g,candd,candd2)
                                    if consistent == False:
                                        return [False,conditionals]
                                    del conditionals[g]
                                    g -= 1
                                    break
                            elif detach_sent_truth_val != temp_nega and str12 == 'e':
                                if not conditionals[g][28] and antec_conjunct == "":
                                #if conseq_conjunct != "":
                                #if kind != 2 and conseq_conjunct != "":
                                    consistent = new_prop_sent(greek2,all_sent,"~", "con", \
                                                "EN", anc1, anc2, conditionals,g,candd,candd2)
                                    if not consistent:
                                        return [False,conditionals]
                                    del conditionals[g]
                                    g -= 1
                                    break

                        elif f == 1 and temp_detach_sent == temp_con:
                            if detach_sent_truth_val == temp_negc and str12 == 'e':
                                if conseq_conjunct == "":
                                    consistent = new_prop_sent(greek2,all_sent,"", "ant", "EE", \
                                        anc1, anc2, conditionals,g,candd,candd2)
                                    if not consistent:
                                        return [False,conditionals]
                                    del conditionals[g]
                                    g -= 1
                                    break
                                else:
                                    list1 = many_cond(greek2,all_sent,candd,candd2, conditionals, "ant", "EE", \
                                                      anc2, f, g, r)
                                    consistent = list1[0]
                                    conditionals = list1[1]
                                    if not consistent:
                                        return [False,conditionals]
                                    elif consistent:
                                        del conditionals[g]
                                        g -= 1
                                        break
                            elif detach_sent_truth_val != temp_negc:
                                if not conditionals[g][27]:
                                #if kind != 2 and antec_conjunct != "":
                                    if str12 == 'c':
                                        str13 = "MT"
                                    else:
                                        str13 = "EN"
                                    consistent = new_prop_sent(greek2,all_sent,"~", "ant", \
                                                str13, anc1, anc2, conditionals,g,candd,candd2)
                                    if not consistent:
                                        return [False,conditionals]
                                    del conditionals[g]
                                    g -= 1
                                    break

                                
                        elif f == 0 and temp_detach_sent != temp_ant and \
                                antec_conjunct != "" and str12 == 'e':
                            if conditionals != []:
                                if not conditionals[g][28]:
                                #if kind != 2 and conseq_conjunct != "":
                                    s = -1
                                    while s < len(conditionals[g][0]) -1:
                                        s += 1
                                        if temp_detach_sent == conditionals[g][0][s][0] and \
                                            detach_sent_truth_val != conditionals[g][0][s][1]:

                                            consistent = new_prop_sent(greek2,all_sent,"~", "con", \
                                            "EN", anc1, anc2, conditionals,g,candd,candd2)
                                            if not consistent:
                                                return [False,conditionals]
                                            del conditionals[g]
                                            g -= 1
                                            break


                        elif f == 1 and temp_detach_sent != temp_con and conseq_conjunct != "":
                            #if kind != 2 and antec_conjunct != "":
                            if conditionals != []:
                                if not conditionals[g][27]:
                                    s = -1
                                    while s < len(conditionals[g][1]) -1:
                                        s += 1
                                        if temp_detach_sent == conditionals[g][1][s][0] and \
                                            detach_sent_truth_val != conditionals[g][1][s][1]:

                                            if str12 == 'e':
                                                str13 = "EN"
                                            else:
                                                str13 = "MT"
                                            consistent = new_prop_sent(greek2,all_sent,"~", "ant", \
                                            str13, anc1, anc2, conditionals,g,candd,candd2)
                                            if not consistent:
                                                return [consistent,conditionals]
                                            del conditionals[g]
                                            g -= 1
                                            break


    return [True,conditionals]

def disjunction_heirarchy(conditionals,str5,d,new_disj = False):

    global prop_name
    global sn,pn

    if d > len(conditionals)-1:
        return conditionals
    if iff in str5 or conditional in str5:
        return conditionals

    if conditionals[d][36] == "":
        str5 = enclose(str5)
        def_info = find_sentences(str5)
    else:
        def_info = conditionals[d][36]

    mainc = def_info[4][0][1]
    list2 = [""] * 39
    n = 7
    if mainc == xorr:
        list2[3] = 'x'
    else:
         list2[3] = 'd'
    if conditionals == [] or new_disj:
        list2[2] = pn
    else:
        list2[2] = conditionals[d][2]
    list2[5] = ""
    list2[4] = def_info[0][0]# fix this
    sentences = []

    for i in range(len(def_info[0])):
        if os(def_info[0][i]):
            siblings = []
            list3 = [None] * 9
            n += 1
            # str1 = findinlist(def_info[0][i],prop_name,1,0)
            str2 = def_info[4][i][0][:-1]
            g = findinlist(str2,def_info[4],0,1,True)
            parent = def_info[0][g]
            if def_info[4][g][1] == "&":
                list3[2] = 'c'
            elif def_info[4][g][1] == xorr:
                list3[2] = 'x'
            else:
                list3[2] = 'd'
            if len(str2) > 1:
                str3 = def_info[4][i][0][:-2]
                g = findinlist(str3,def_info[4],0,1,True)
                gparent = def_info[0][g]
            else:
                gparent = parent
            list3[1] = def_info[4][i][0]
            list3[5] = parent
            list3[6] = gparent
            list3[0] = [def_info[0][i], def_info[1][i]]
            #fix this
            b = parent.count(xorr)
            c = parent.count(idisj)
            if c > 1 or b > 1:
                list3[7] = 2
            else:
                list3[7] = 1
            sent_num = def_info[4][i][0]
            m = len(sent_num)
            for j in range(len(def_info[4])):
                if len(def_info[4][j][0]) == m and def_info[4][j][0][:-1] == str2 \
                    and j != i:
                    siblings.append([def_info[0][j],def_info[1][j]]) # fix this
            list3[4] = siblings
            list2[n] = list3
            sentences.append(list3[0][0])
            if list3[0][0] not in rel_conj:
                rel_conj.append(list3[0][0])
    list2[36] = def_info

    if conditionals == [] or new_disj:
        list2[38] = sentences
        conditionals.append(list2)
        return conditionals
    else:
        list2[38] = sentences
        list2[2] = conditionals[d][2]
        list2[37] = conditionals[d][37]
        conditionals[d] = list2
        return conditionals


def proper_spacing(str1):

    str1 = str1.replace(" ","")
    str1 = str1.replace(iff, " " + iff + " ")
    str1 = str1.replace(conditional," " + conditional + " ")
    str1 = str1.replace(idisj," " + idisj + " ")
    str1 = str1.replace(xorr," " + xorr + " ")
    str1 = str1.replace("&"," & ")
    return str1

def iff_elim(all_sent,prop_sent,conditionals,kind):

    new_sent = False
    for d in range(len(conditionals)):
        if conditionals[d][0] != "":
            list1 = ["",""]
            ng = conditionals[d][5]
            if conditionals[d][3] == "d" or conditionals[d][3] == 'n':
                list1 = [conditionals[d][4], ""]
            else:
                if conditionals[d][6] == "":
                    list1[0] = conditionals[d][0][0]
                else:
                    list1[0] = conditionals[d][6]
                if conditionals[d][7] == "":
                    list1[1] = conditionals[d][1][0]
                else:
                    list1[1] = conditionals[d][7]
            for s in range(0,2):
                if list1[s].find(iff) > -1:
                    new_sent = True
                    str1 = list1[s]
                    anc1 = conditionals[d][2]
                    old_str = copy.copy(str1)
                    str1 = str1.replace(" ","")
                    str1 = str1.replace("&"," & ")
                    str1 = str1.replace(iff , " " + iff + " ")
                    str1 = remove_outer_paren(str1)
                    list5 = mainconn(str1)
                    mc = list5[0]
                    bool4 = False
                    if str1[:2] == "~(":
                        bool4 = True
                        str1 = str1[2:len(str1) - 1]
                    r = str1.count(iff)
                    i = -1
                    for o in range(0,r):
                        k = 0
                        while i < len(str1) - 1:
                            i += 1
                            str2 = str1[i:i+1]
                            if str2 == iff:
                                p = copy.copy(i)
                                t = copy.copy(i)
                                bool5 = False
                                while k != -1:
                                    i -= 1
                                    str3 = str1[i:i+1]
                                    if str3 == "(":
                                        k -= 1
                                    elif str3 == ")":
                                        k += 1
                                        bool5 = True
                                    if k == -1:
                                        m = i + 1
                                    elif k == 0 and bool5:
                                        m = i
                                        break
                                bool3 = False
                                k = 0
                                while p < len(str1):
                                    p += 1
                                    str3 = str1[p:p+1]
                                    if str3 == "(":
                                        bool3 = True
                                        k -= 1
                                    elif str3 == ")":
                                        k += 1
                                    if bool3 and k == 0:
                                        p += 1
                                        break
                                    elif k == 1:
                                        break
                                ant = str1[m:t]
                                ant = ant.strip()
                                con = str1[t+1:p]
                                con = con.strip()
                                new1 = "(" + ant + " " + conditional + " " + con + ")"
                                new2 = "(" + con + " " + conditional + " " + \
                                       ant + ")"
                                if mc != "&":
                                    if r > 1 and o + 1 != r:
                                        new3 = "(" + new1 + ' & ' + new2 + ")*"
                                    else:
                                        new3 = "(" + new1 + ' & ' + new2 + ")"
                                else:
                                    if r > 1 and o + 1 != r:
                                        new3 = new1 + ' & ' + new2 + '*'
                                    else:
                                        new3 = new1 + ' & ' + new2
                                if m != 0 or p != len(str1):
                                    replacee = str1[m-1:p+1]
                                    new3 = str1.replace(replacee, new3)
                                str1 = new3
                                if r > 1 and o + 1 != r:
                                    i = str1.find("*")
                                    str1 = str1.replace("*","")
                                break
                    new3 = str1
                    new3 = proper_spacing(new3)
                    if bool4:
                        new3 = "~(" + new3 + ")"
                    else:
                        new3 = "(" + new3 + ")"
                    conditionals[d][4] = conditionals[d][4].replace(old_str,new3)
                    if conditionals[d][3] == 'c' or conditionals[d][3] == 'e':
                        if s == 0:
                            conditionals[d][0] = None
                            conditionals[d][6] = new3
                        else:
                            conditionals[d][1] = None
                            conditionals[d][7] = new3

            if conditionals[d][3] == "e":
                conditionals[d][3] = "c"
                anc1 = conditionals[d][2]
                list1 = [""] * 39
                list1[5] = ""
                if conditionals[d][6] == "":
                    str1 = conditionals[d][0][0]
                    if not os(str1):
                        str1 = "(" + str1 + ")"
                    ng1 = conditionals[d][0][1]
                else:
                    str1 = conditionals[d][6]
                    ng1 = ""
                if conditionals[d][7] == "":
                    str4 = conditionals[d][1][0]
                    if not os(str4):
                        str4 = "(" + str4 + ")"
                    ng4 = conditionals[d][1][1]
                else:
                    str4 = conditionals[d][7]
                    ng4 = ""

                list1[0] = [str4,ng4]
                list1[1] = [str1, ng1]
                str5 =  ng1 + str1 + " " + conditional + " " + ng4 + str4
                str6 = ng4 + str4 + " " + conditional + " " + ng1 + str1
                g = copy.copy(pn+1)
                if conditionals[d][5] == "" or conditionals[d][5] == None:
                    str3 = "(" + str5 + ") & (" + str6 + ")"
                    str7 = iff + "E"
                    no_contr = new_prop(all_sent,prop_sent, str3, ng, str7, anc1, None, None, None)

                    if not no_contr:
                        return [False,conditionals]
                    conditionals[d][2] = pn+1
                    conditionals[d][0] = [str1, ng1]
                    conditionals[d][1] = [str4, ng4]
                    no_contr = new_prop(all_sent,prop_sent,str5,"","&E",g,"")
                    if not no_contr:
                        return [False,conditionals]
                    list1[2] = pn + 1
                    no_contr = new_prop(all_sent,prop_sent,str6,"","&E",g,"")
                    if not no_contr:
                        return [False,conditionals]
                    conditionals[d][4] = str5
                    list1[4] = str6
                    conditionals.append(list1)
                else:
                    str3 = "(" + str5 + ") & (" + str6 + ")"
                    no_contr = new_prop(all_sent,prop_sent,str3,"~",iff + "E",g,"")
                    if not no_contr:
                        return [False,conditionals]
                    conditionals[d][3] = 'd'
                    conditionals[d][4] = str3
            elif new_sent:
                no_contr = new_prop(all_sent,prop_sent,conditionals[d][4],"",iff + "E",anc1,"")
                if not no_contr:
                    return [False,conditionals]
    return [True,conditionals]

def material_implication(all_sent,prop_sent, conditionals,kind):

    for d in range(len(conditionals)):
        if d == 3:
            bb = 7
        if conditionals[d][0] != "":
            str1 = conditionals[d][4]
            ng = conditionals[d][5]
            if str1.find(conditional) > -1:
                anc1 = conditionals[d][2]
                i = -1
                q = -1
                s = 0
                r = str1.count(conditional)
                while s < r:
                    i += 1
                    q += 1
                    str2 = str1[i:i+1]
                    if str2 == conditional:
                        s += 1
                        j = i
                        k = 0
                        m = 0
                        bool1 = False
                        while j != 0:
                            j -= 1
                            m += 1
                            if m > 200:
                                print "in the material implication function \
                                you are caught in an infinite loop"
                                sys.exit()


                            str3= str1[j:j+1]
                            if str3.islower() and k == 0:
                                bool1 = True
                            elif str3 == ")":
                                bool1 = True
                                k += 1
                            elif j == 0 and str3 != "(":
                                k = 0
                                bool1 = True
                            elif str3 == "(":
                                bool1 = True
                                k -= 1

                            if bool1 and k == 0:
                                str4 = str1[0:j]
                                str5 = str1[i+2:]
                                str7 = str1[j:i]
                                str1 = str4 + "~" + str7 + idisj + " " + str5
                                i += 1
                                break

                str1 = bad_paren(str1)
                no_contr = new_prop(all_sent,prop_sent, str1, ng, conditional + "E", anc1,"")
                if not no_contr:
                    return [False,conditionals]
                if str1.find("~~") > -1:
                    str1 = str1.replace("~~","")
                    g = copy.copy(pn)
                    no_contr = new_prop(all_sent,prop_sent,str1, ng, "~~E", g,"")
                    if not no_contr:
                        return [False,conditionals]
                conditionals[d][2] = pn
                conditionals[d][4] = str1
                conditionals[d][3] = "d"
                conditionals[d][5] = ng

    return [True,conditionals]

def bad_paren(str1):

    if str1.find("(") == -1:
        return str1
    # we first must get rid of strings of the following form ((p) & s)
    for i in range(len(str1)):
        str2 = str1[i:i+1]
        str3 = str1[i-1:i]
        if i > 1:
            str4 = str1[i-2:i-1]
        else:
            str4 = ""
        str5 = str1[i+1:i+2]
        if str2.islower() and str3 == "(" and str5 == ")":
            str1 = str1[:i-1] + str1[i:i+1] + str1[i+2:]
        elif str2.islower() and str4 == "(" and str3 == "~" and str5 == ")":
            str1 = str1[:i-2] + str1[i-1:i+1] + str1[i+2:]

    str1 = enclose(str1)
    list1 = find_sentences(str1)
    mstr = list1[3][0]
    for i in range(1, len(list1[3])):
        if list1[4][i][1] != "":
            mc = list1[4][i][1]
            ostr = list1[3][i]
            str2 = list1[4][i][0][:-1]
            prcnt = findinlist(str2,list1[4],0,1,False)
            if mc == prcnt:
                nstr = remove_outer_paren(ostr)
                nstr = remove_outer_paren(nstr)
                mstr = mstr.replace(ostr, nstr)
    return mstr

def demorgan(all_sent,prop_sent,conditionals,candd,candd2,kind,one_sent = False, str8 = "",anc1a = "",rule = "",conjt = []):

    d = -1
    rop = False
    if one_sent:
        d = len(conditionals) - 2

    while d < len(conditionals) -1:
        d += 1
        if one_sent:
            str1 = str8
        else:
            str1 = conditionals[d][5] + conditionals[d][4]
        if one_sent:
            rop = True
        else:
            if conditionals[d][5] == "~":
                rop = True
        if str1.find("~(") > -1:
            if one_sent:
                anc1 = anc1a
            else:
                anc1 = conditionals[d][2]
            r = str1.count("~(")
            s = 0
            i = -1
            while s < r:
                i += 1
                if i > 200:
                    print "you are caught in an infinite loop in the \
                    demorgan function"
                    sys.exit()
                str2 = str1[i:i+2]
                if str2 == "~(":
                    s += 1
                    bool2 = True
                    if i > 0:
                        str4 = str1[0:i]
                    else:
                        str4 = ""
                    str5 = str1[i+1:len(str1)+1]
                    str1 = str4 + str5
                    j = i
                    m = 0
                    k = 0
                    bool3 = False
                    while j < len(str1):
                        m += 1
                        if m > 200:
                            print "you are caught in an infinite loop in the \
                            demorgan function"
                            sys.exit()
                        bool1 = False
                        str3 = str1[j:j+1]
                        if j-1 > 0:
                            str6 = str1[j-1:j+1]
                        else:
                            str6 = ""

                        if str6 == "~(" and bool3 == False and bool2 == False:
                            k = 0
                            k += 1
                            s += 1
                            # bool3 means that python is searching only for those letters and connectives
                            # which are on the same level of parentheses
                            bool3 = True
                            str4 = str1[0:j]
                            str5 = str1[j:]
                            str1 = str4 + "~" + str5
                            j += 2
                            str3 = str1[j:j+1]


                        bool2 = False

                        if str3.islower() and bool3 == False:
                            str4= str1[0:j]
                            str5 = str1[j+1:(len(str1)+1)]
                            str1 = str4 + "~" + str3 + str5
                            j += 2
                            bool1 = True
                        elif bool3 == False:
                            if str3 == "(":
                                k += 1
                                j += 1
                                bool1 = True
                            elif str3 == ")":
                                k -= 1
                                j += 1
                                bool1 = True
                            elif str3 == "&":
                                str4 = str1[0:j]
                                str5 = str1[(j + 1):(len(str1) + 1)]
                                str1 = str4 + idisj+ str5
                                j += 1
                            elif str3 == idisj or str3 == xorr:
                                str4 = str1[0:j]
                                str5 = str1[(j+1):(len(str1)+1)]
                                str1 = str4 + "&" + str5
                                j += 1
                            else:
                                j += 1

                        elif str3 == ")":
                            j += 1
                            k -= 1
                        elif str3 == "(":
                            k += 1
                            j += 1
                        else:
                            j += 1

                        if k == 0 and bool3:
                            bool3 = False
                        if k == 0 and bool1 == True:
                            i = j
                            break

        # rop means remove outer paren, this is necessary if the original sentence was negated
            if rop:
                str1 = remove_outer_paren(str1)
            list1 = [None] * 15
            if str1.find("~~") > -1:
                str2 = copy.copy(str1)
                str2 = str2.replace("~~","")
                str2 = bad_paren(str2)
            else:
                str1 = bad_paren(str1)
            no_contr = new_prop(all_sent,prop_sent,str1,"","~(E",anc1,"")
            if not no_contr:
                return [False,conditionals]
            if str1.find("~~") > -1:
                str1 = str2
                anc1 = copy.copy(pn)
                no_contr = new_prop(all_sent,prop_sent,str2,"","~~E",anc1,"")
                if not no_contr:
                    return [False,conditionals]
            list2 = mainconn(str1)

            if list2[0] == "&":
                if not one_sent:
                    del conditionals[d]
                list3 = get_conjuncts(str1,True)
                anc1 = copy.copy(pn)
                for i in range(len(list3)):
                    list4 = tilde_removal2(list3[i])
                    no_contr = new_prop(all_sent,prop_sent,list4[0],list4[1],"&E",anc1,"")
                    if not no_contr:
                        return [False,conditionals]
                    list2 = mainconn(list3[i])
                    if list2[0] == idisj or list2[0] == xorr:
                        # add in more nones if it turns out that I need them
                        if one_sent:
                            conditionals = disjunction_heirarchy(conditionals,str1,0)
                        else:
                            list5 = [""] * 39
                            list5[2] = pn
                            list5[4] = list4[0]
                            list5[5] = list4[1]
                            conditionals.append(list5)
                    else:
                        candd.append([pn,list4[0],list4[1]])
                        if conjt != []:
                            conjt.append([pn,list4[0],list4[1]])
            else:
                if one_sent:
                    conditionals = disjunction_heirarchy(conditionals,str1,0,True)
                    return [True,conditionals]
                else:
                    conditionals[d][2] = pn
                    conditionals[d][4] = str1
    return [True,conditionals]

def unenclose(str1):
    # this removes ( ) from around a sentence abbreviation
    i = -1
    global subscripts
    if "(" not in str1:
        return str1

    while i < len(str1)-1:
        i += 1
        str2 = str1[i:i+1]
        str3 = str1[i-1:i]
        str4 = str1[i+1:i+2]
        if str2.islower() and str3 != "~" and str4 not in subscripts:
            str1 = str1[:i-1] + str2 + str1[i+2:]
        elif str2.islower() and str3 == "~" and str4 not in subscripts:
            str1 = str1[:i-2] + str3 + str2 + str1[i+2:]
        if str2.islower() and str3 != "~" and str4 in subscripts:
            str1 = str1[:i-1] + str2 + str4 + str1[i+3:]
        elif str2.islower() and str3 == "~" and str4 in subscripts:
            str1 = str1[:i-2] + str3 + str2 + str4 + str1[i+3:]

    return str1

def new_disjunct(all_sent,str1, ng, n, prop_sent, conditionals, candd,candd2,conjt, anc1, anc2, \
            anc3 = None, anc4=None, kind = 0, rule = ""):

    global sn,pn
    list2 = mainconn(str1)
    if kind == 1:
        del conditionals[n]
        consistent = new_prop(all_sent,prop_sent, str1, ng, "&I", \
            anc1, anc2, anc3, anc4)
        return [consistent,conditionals]
    elif kind == 2:
        consistent = new_prop(all_sent,prop_sent, str1, ng, "&I", \
            anc1, anc2, anc3, anc4)
        return [consistent,conditionals]
    else:
        if os(str1):
            del conditionals[n]
            str1 = remove_outer_paren(str1)
            list1 = tilde_removal2(str1)
            str1 = list1[0]
            consistent = new_prop(all_sent,prop_sent, str1, list1[1], rule + "E", \
            anc1, anc2)
            candd.append([pn,list1[0],list1[1]])
            conjt.append([pn,list1[0],list1[1]])
            return [consistent,conditionals]
        elif list2[0] == "&":
            del conditionals[n]
            str1 = remove_outer_paren(str1)
            dummy = new_prop(all_sent,prop_sent, str1, ng, rule + "E", \
            anc1, anc2)
            g = copy.copy(pn)
            list3 = get_conjuncts(str1)
            for i in range(len(list3)):
                list4 = tilde_removal2(list3[i])
                consistent = new_prop(all_sent,prop_sent, list4[0], list4[1], "&E", g,"")
                if dummy == False:
                    return [consistent,conditionals]
                if list3[i].find(idisj) > -1:
                    conditionals = disjunction_heirarchy(conditionals, list4[0],n, True)
                else:
                    candd.append([pn,list4[0],list4[1]])
                    conjt.append([pn,list4[0],list4[1]])
            return [True,conditionals]
        else:
            consistent = new_prop(all_sent,prop_sent, str1, ng, idisj + "E", \
            anc1, anc2)
            if consistent == False:
                return [consistent,conditionals]
            if ng == "~":
                str1 = ng + str1
            else:
                str1 = remove_outer_paren(str1)
            conditionals[n][2] = pn
            conditionals = disjunction_heirarchy(conditionals, str1,n, False)
            return [True,conditionals]

def xorr_elim(all_sent,conditionals,n,i,parent,grandparent,whole_d,candd,candd2,conjt,\
              prop_sent,anc1,anc2,kind=0):

    str9 = ""
    de_mor = False
    if kind == 0:
        for r in range(len(conditionals[n][i][4])):
            if r != i:
                if not os(conditionals[n][i][4][r][0]):
                    de_mor = True
                if str9 == "":
                    str9 += "~" + conditionals[n][i][4][r][1] + conditionals[n][i][4][r][0]
                else:
                    str9 += " & ~" + conditionals[n][i][4][r][1] + conditionals[n][i][4][r][0]
    else:
        grandp2 = copy.copy(grandparent)
        grandp2 = grandp2.replace(parent,"")
        for r in range(8,38):
            if conditionals[n][r] == "":
                break
            if conditionals[n][r][0][0] in grandp2:
                if str9 == "":
                    str9 += "~" + conditionals[n][r][0][1] + conditionals[n][r][0][0]
                else:
                    str9 += " & ~" + conditionals[n][r][0][1] + conditionals[n][r][0][0]
    g = copy.copy(pn)
    if parent != grandparent:
        str9 = remove_outer_paren(str9)
        if grandparent == whole_d:
            mc = mainconn(str9)
            if mc[0] == '&':
                list1 = xorr_elim2(str9,prop_sent,conditionals,candd,candd2,anc1,anc2)
                consistent = list1[0]
                conditionals = list1[1]
                if consistent == False:
                    return [consistent,conditionals]
            else:
                list4 = tilde_removal(str9)
                consistent = new_prop(all_sent,prop_sent, list4[0],list4[1], xorr + "E", \
                anc1, anc2)
                if consistent == False:
                    return [consistent,conditionals]
        else:
            str9 = "(" + str9 + ")"
            if kind == 0:
                str9 = grandparent.replace(parent,str9)
                str9 = whole_d.replace(grandparent, str9)
                str9 = bad_paren(str9)
                consistent = new_prop(all_sent,prop_sent,str9,"",xorr + "E",anc1,anc2)
                if str9.find("~~") > -1:
                    str9 = str9.replace("~~","")
                    consistent = new_prop(all_sent,prop_sent,str9,"","~~E",pn,"")

            else:
                str9 = whole_d.replace(grandparent,str9)
                str9 = bad_paren(str9)
                consistent = new_prop(all_sent,prop_sent,str9,"",xorr + "E",anc1,anc2)
                g = copy.copy(pn)
                if str9.find("~~") > -1:
                    str9 = str9.replace("~~","")
                    consistent = new_prop(all_sent,prop_sent,str9,"","~~E",g,"")
                    if consistent == False:
                        return consistent
                conditionals = disjunction_heirarchy(conditionals, str9,n, True)
                del conditionals[n]
            if de_mor:
                list1 = demorgan(prop_sent,conditionals,candd,candd2,conjt,"",True,str9,pn,xorr +"E")
                consistent = list1[0]
                conditionals = list1[1]
                if consistent == False:
                    return consistent
            else:
                if str9.find(idisj) > -1 or str9.find(xorr) > -1:
                    conditionals = disjunction_heirarchy(conditionals,str9,n,True)
                consistent = True
    else:
        #this does not account for the case where the parent == grandparent but
        # grandparent does not == whole d
        list1 = xorr_elim2(str9,prop_sent,conditionals,candd,candd2,conjt,anc1,anc2)
        consistent = list1[0]
        conditionals = list1[1]
    return [consistent,conditionals]

def xorr_elim2(all_sent,str9,prop_sent,conditionals,candd,candd2,conjt,anc1,anc2):

    str9 = bad_paren(str9)
    consistent = new_prop(all_sent,prop_sent, str9, "", xorr + "E", \
    anc1, anc2)
    if consistent == False:
        return [False,conditionals]
    if str9.find("~~") > -1:
        str9 = str9.replace("~~","")
        consistent = new_prop(all_sent,prop_sent,str9,"","~~E",pn,"")
        if consistent == False:
            return [consistent,conditionals]
    list3 = get_conjuncts(str9)
    g = copy.copy(pn)
    for b in range(len(list3)):
        list4 = tilde_removal2(list3[b])
        list4[0] = remove_outer_paren(list4[0])
        consistent = new_prop(all_sent,prop_sent, list4[0], list4[1], "&E", g,"")
        if consistent == False:
            return consistent
        if not os(list3[b]):
            if list4[1] == "~":
                list1 = demorgan(prop_sent,conditionals,\
                candd,candd2,"",True,list3[b],pn,"&E",conjt)
                consistent = list1[0]
                conditionals = list1[1]
                if consistent == False:
                    return [False,conditionals]
            else:
                conditionals = disjunction_heirarchy(conditionals, list4[0],n, True)
        else:
            candd.append([pn,list4[0],list4[1]])
            conjt.append([pn,list4[0],list4[1]])
    return [True,conditionals]

def disjunction_elimination(all_sent,prop_sent, conditionals, candd,candd2, kind = ""):

    bool1 = False
    bool2 = False
    global sn,pn
    global rel_conj

    for i in range(len(conditionals)):
        if conditionals[i][8] == "":
            conditionals = disjunction_heirarchy(conditionals, conditionals[i][4],i)
    i = -1
    conjt = copy.deepcopy(candd)
    if kind == 2:
        list1 = []
        rel_conj = finddisj(conditionals,list1,1)

    while i < len(conjt) -1:
        i += 1
        if conjt[i][1] not in rel_conj:
            del conjt[i]
            i -= 1
    d = -1
    while d < len(conjt) -1:
        d += 1
        str2 = conjt[d][2]
        conj = conjt[d][1]
        if conj == 'q':
            bb = 7
        if d == 42:
            bb = 7
        anc1 = conjt[d][0]
        n = -1
        while n < len(conditionals) -1:
            if bool1:
                bool1 = False
                d = -1
                break
            n += 1
            if n == 7:
                bb = 7
            i = 7
            while conditionals != []:
                if bool2:
                    bool2 = False
                    break
                i += 1
                if conj not in conditionals[n][38] and iff not in conditionals[n][4]\
                        and conditional not in conditionals[n][4]:
                    break
                else:
                    if conditionals[n][i] == "":
                        break
                    whole_d = conditionals[n][4]
                    anc2 = conditionals[n][2]
                    str3 = conditionals[n][i][0][0]
                    # 'pos or neg'
                    str4 = conditionals[n][i][0][1]
                    # 'disjunct or conjunct
                    str5 = conditionals[n][i][2]
                    # 'disjunct number
                    str6 = conditionals[n][i][1]

                    if conj == str3:
                        grandparent = conditionals[n][i][6]
                        parent = conditionals[n][i][5]
                        parent2 = copy.copy(parent)
                        parent3 = copy.copy(parent)
                        str7 = " " + idisj + " "
                        str7a = " " + xorr + " "
                        if str2 == str4 and str5 == "d":
                            # 'if the disjuncts are not embedded within a conjunct then the disjunction
                            # is simply deleted

                            del conditionals[n]
                            if parent != grandparent:
                                conj = str2 + conj
                                str8 = whole_d.replace(parent, conj)
                                conditionals = disjunction_heirarchy(conditionals, str8,n)
                            bool1 = True
                            n = -1
                            break

                        elif str2 == str4 and str5 == "x":

                            list1 = xorr_elim(all_sent,conditionals,n,i,parent,grandparent,whole_d,candd,candd2,\
                                        conjt,prop_sent,anc1,anc2)
                            consistent = list1[0]
                            conditionals = list1[1]
                            if not consistent:
                                return [False,conditionals]
                            del conditionals[n]
                            bool2 = True
                            bool1 = True
                            d = -1
                        elif str2 == str4 and str5 == "c":
                            list2 = []
                            list2.append([conj,str2])
                            anc3 = ""
                            anc4 = ""
                            list1 = conditionals[n][i][4]
                            f = -1
                            while f < len(list1) -1:
                                mc = mainconn(grandparent)
                                f += 1
                                for e in range(len(candd)):
                                    anc5 = candd[e][0]
            # since it's too hard to program, if the sibling is a disjunct then we just
            # ignore this
                                    if list1[f][0].find(idisj) > -1 or list1[f][0].find(xorr) > -1:
                                        break
                                    else:
                                        if candd[e][1] == list1[f][0]:
                                            if candd[e][2] == list1[f][1]:
                                                list2.append([list1[f][0],list1[f][1]])
                                                if len(list2) == 2:
                                                    anc3 = anc5
                                                elif len(list2) == 3:
                                                    anc4 = anc5
                                                del list1[f]
                                                if list1 == []:
                                                    str3 = build_sent_list2(list2)
                                                    if mc[0] == xorr:
                                                        new_prop(all_sent,prop_sent,str3,"","&I",anc1,anc3,anc4)
                                                        list1 = xorr_elim(conditionals,n,i,parent,\
                                                        grandparent,whole_d,candd,candd2,conjt,prop_sent,pn,anc2,1)
                                                        consistent = list1[0]
                                                        conditionals = list1[1]
                                                        if not consistent:
                                                            return [False,conditionals]
                                                    else:
                                            # if the conjunct is not embedded within another conjunct
                                            # then the disjunct is simply deleted
                                                        if whole_d == grandparent:
                                                            list1 = new_disjunct(all_sent,str3,"",n, prop_sent,\
                                                            conditionals,candd,candd2,conjt, anc1, anc3, anc4, anc5, 1)
                                                            conditionals = list1[1]
                                                        else:
                                                            str8 = whole_d.replace(grandparent, parent2)
                                                            if str8.find("(") > -1 and str8.find(idisj) > -1:
                                                                str8 = bad_paren(str8)
                                                            list1 = new_disjunct(all_sent,str3,"",n, prop_sent,\
                                                            conditionals,candd,candd2,conjt, anc1, "", anc3, anc4, 2)
                                                            conditionals = list1[1]
                                                            list1 = new_disjunct(all_sent,str8,"",n, prop_sent,\
                                                            conditionals,candd,candd2,conjt, pn-1, anc2)
                                                            consistent = list1[0]
                                                            conditionals = list1[1]
                                                            if not consistent:
                                                                return [False,conditionals]
                                                    bool1 = True
                                                    bool2 = True
                                                    n = 0
                                                    d = -1
                                                    break
                                                else:
                                                    f -= 1
                                                    break

                                            elif candd[e][2] != list1[f][1]:
                                                mc = mainconn(grandparent)
                                                if mc[0] == idisj:
                                                    rule = idisj
                                                    str7 = " " + idisj + " "
                                                else:
                                                    str7 = " " + xorr + " "
                                                    rule = xorr
                                                r = grandparent.find(parent)
                                                if r > 1:
                                                    parent = str7 + parent
                                                else:
                                                    parent = parent + str7
                                                anc1 = candd[e][0]
                                                str9 = grandparent.replace(parent, "")
                                                str8 = whole_d.replace(grandparent, str9)
                                                if str8.find("(") > -1 and (str8.find(idisj) > -1 or str8.find(xorr) > -1):
                                                    str8 = bad_paren(str8)
                                                list1 = new_disjunct(all_sent,str8,"",n, prop_sent,\
                                                        conditionals,candd,candd2,conjt, anc1, anc2,None,None,0,rule)
                                                consistent = list1[0]
                                                conditionals = list1[1]
                                                if not consistent:
                                                    return [False,conditionals]
                                                else:
                                                    list1 = []
                                                    bool1 = True
                                                    bool2 = True
                                                    n = 0
                                                    d = -1
                                                    break

                        elif str2 != str4 and str5 == "c":
                            mc = mainconn(conditionals[n][i][6])
                            if mc[0] == idisj:
                                str6 = str7 + parent
                                rule = idisj
                            else:
                                rule = xorr
                                str6 = str7a + parent
                            if grandparent.find(str6) > -1:
                                parent = str6
                            else:
                                parent = parent + str7
                            str9 = grandparent.replace(parent, "")
                            str8 = whole_d.replace(grandparent, str9)
                            if str8.find("(") > -1 and str8.find(idisj) > -1:
                                str8 = bad_paren(str8)
                            list1 = new_disjunct(all_sent,str8,"",n,prop_sent, conditionals, candd,candd2,conjt,anc1, anc2, None, None,0,rule)
                            consistent = list1[0]
                            conditionals = list1[1]
                            if not consistent:
                                return [False,conditionals]
                            bool1 = True
                            n = -1
                            break

                        elif str2 != str4 and (str5 == "d" or str5 == 'x'):
                            # if the disjunct is a triple disjunct then enter below
                            if str5 == 'd':
                                rule = idisj
                            else:
                                rule = xorr
                            if conditionals[n][i][7] > 1:
                                str6 = str4 + str3 + " " + rule + " "
                                if parent.find(str6) > -1:
                                    str5 = str6
                                else:
                                    str5 = " " + rule + " " + str4 + str3
                                str9 = parent.replace(str5, "")
                                str8 = whole_d.replace(parent, str9)
                                if str8.find("(") > -1 and (str8.find(idisj) > -1 or str8.find(xorr) > -1):
                                    str8 = bad_paren(str8)
                                list1 = new_disjunct(all_sent,str8,"",n,prop_sent,conditionals,\
                                    candd,candd2,conjt, anc1,anc2,None,None,0,rule)
                                consistent = list1[0]
                                conditionals = list1[1]
                                if not consistent:
                                    return [False,conditionals]
                                bool1 = True
                                n = -1
                                break

                            else:
                                str3 = conditionals[n][i][4][0][0] # ddd
                                str4 = conditionals[n][i][4][0][1]
                                str5 = str4 + str3
                                str8 = whole_d.replace(parent, str5)
                                if str8.find("(") > -1 and (str8.find(idisj) > -1 or str8.find(xorr) > -1):
                                    str8 = bad_paren(str8)
                                list1 = new_disjunct(all_sent,str8,"",n,prop_sent,conditionals,\
                                    candd,candd2,conjt, anc1,anc2,None,None,0,rule)
                                consistent = list1[0]
                                conditionals = list1[1]
                                if not consistent:
                                    return [False,conditionals]
                                bool1 = True
                                n = -1
                                break
    return [True,conditionals]

def extract_list(list1,d):

    list2 = []
    for i in range(len(list1)):
        list2.append(list1[i][d])
    return list2

def statement_logic(greek2,prop_sent,all_sent, conditionals, candd,candd2, disjuncts,kind="", conc="", impl=""):

    global time1,st_log_tim
    b = time.time()
    list1 = modus_ponens(greek2,all_sent,conditionals, candd,candd2, prop_sent,kind)
    consistent = list1[0]
    conditionals = list1[1]
    if consistent == False:
        return [False,conditionals]
    if kind != 2:
        list1 = iff_elim(all_sent,prop_sent,conditionals,kind)
        consistent = list1[0]
        conditionals = list1[1]
        if consistent == False:
            return [False,conditionals]
        list1 = material_implication(all_sent,prop_sent, conditionals,kind)
        consistent = list1[0]
        conditionals = list1[1]
        if consistent == False:
            return [False,conditionals]
    list1 = demorgan(all_sent,prop_sent, conditionals, candd,candd2,kind)
    consistent = list1[0]
    conditionals = list1[1]
    if consistent == False:
        return [False,conditionals]
    list1 = disjunction_elimination(all_sent,prop_sent,conditionals,candd,candd2,kind)
    consistent = list1[0]
    conditionals = list1[1]
    if consistent == False:
        return False
    if kind == 1:
        dummy = finddisj(conditionals,disjuncts)
    c = time.time()
    d = c - b
    st_log_tim += d
    return [True,conditionals]

def finddisj(conditionals,disjuncts, cate=""):

    if cate == 1:
        disjuncts = []

    for i in range(len(conditionals)):
        for j in range(8,36):
            if type(conditionals[i][j]) is list:
                if conditionals[i][j][0][0] not in disjuncts:
                    disjuncts.append(conditionals[i][j][0][0])
            else:
                break
    if cate == 1:
        return disjuncts

def add_outer_paren(str1):

    str1 = remove_outer_paren(str1)
    return "(" + str1 + ")"

def new_prop_sent(greek2,all_sent,ng, kind, asp, anc1, anc2, conditionals,g,candd,candd2,list3 =[], cjct = ""):

    global prop_sent
    global sn,pn
    global impl

    if pn == 61:
        bb = 8

    if kind == 'con':
        h = 1
        e = 7
    else:
        h = 0
        e = 6
    bool1 = False
    if list3 != []:
        pn += 1
        ancc = [4,5,6,7]
        list4 = [None] * 15
        for i in range(len(list3)):
            if i == 4:
                break
            list4[ancc[i]] = list3[i]
        list4[0] = pn
        list4[1] = cjct
        list4[2] = ""
        list4[3] = "&I"
        anc1 = pn
        prop_sent.append(list4)

    if conditionals[g][e] == "":
        str1 = conditionals[g][h][0]
        list2 = mainconn(str1)

        if implies in conditionals[g][h][0] or nonseq in conditionals[g][h][0]:
            pn += 1
            prop_sent.append([pn,str1, "",asp,anc1,anc2,"","",""])
            g = str1.find(implies)
            asp = "DF " + implies
            if g == -1:
                g = str1.find(nonseq)
                asp = "DF " + nonseq
            str2 = str1[:g]
            str3 = str1[g+1:]
            str2 = str2.strip()
            str3 = str3.strip()
            if impl == implies:
                str4 = str2 + " & ~" + str3 + " & " + bottom
                str5 = bottom
            else:
                str4 = str2 + " & ~" + str3 + " & " + top
                str5 = top
            pn += 1
            prop_sent.append([pn,str4, "",asp,pn-1,"","","",""])
            pn += 1
            prop_sent.append([pn,str2, "","&E",pn-1,"","","",""])
            candd.append([pn,str2,""])
            pn += 1
            prop_sent.append([pn,str3, "~","&E",pn-2,"","","",""])
            candd.append([pn,str3,"~"])
            pn += 1
            prop_sent.append([pn,str5, "","&E",pn-3,"","","",""])
            return

        # here we take care of double negatives
        if ng == "~" and conditionals[g][h][1] == "~":
            pn += 1
            prop_sent.append([pn, "~" + str1, "~", asp, anc1, anc2, None, None, None, None, None,None, None, None, None])
            g = copy.copy(pn)
            dummy = new_prop(all_sent,prop_sent,str1,"","~~E",g, None)
            if dummy == False:
                return False
            ng = ""
            bool1 = True
        elif (ng == "" and conditionals[g][h][1] == "~") or \
                (ng == "~" and conditionals[g][h][1] == ""):
            ng = "~"
        if list2[0] != "" and ng != "~":
            str1 = remove_outer_paren(str1)
        elif list2[0] != "" and ng == "~":
            str1 = add_outer_paren(str1)
        if bool1 == False:
            dummy = new_prop(all_sent,prop_sent,str1,ng,asp,anc1, anc2)
            if dummy == False:
                return False

        candd.append([pn, str1, ng])
        if (list2[0] == iff or list2[0] == conditional) and ng != "~":
            enc_str1 = enclose(str1)
            def_info = find_sentences(enc_str1)
            list3 = prepare_iff_elim(greek2,def_info,str1,all_sent,list2[0],list2[1],pn)
            conditionals.append(list3)
        elif list2[0] == iff or list2[0] == conditional or list2[0] == idisj or list2[0] == xorr:
            list5 = [""] * 39
            list5[2] = pn
            list5[4] = str1
            list5[5] = ng
            list5[3] = 'd'
            conditionals.append(list5)
    else:
        str1 = conditionals[g][e]
        if ng == "~":
            list5 = [""] * 39
            list5[2] = pn + 1
            list5[4] = str1
            list5[5] = "~"
            list5[3] = 'd'
            conditionals.append(list5)
            dummy = new_prop(all_sent,prop_sent, str1, ng, asp, anc1, anc2)
            if dummy == False:
                return False
        else:
            list1 = conditionals[g][h]
            str1 = remove_outer_paren(str1)
            dummy = new_prop(all_sent,prop_sent, str1, ng, asp, anc1, anc2)
            if dummy == False:
                return False
            anc1 = copy.copy(pn)
            for i in range(len(list1)):
                list2 = mainconn(list1[i][0])
                dummy = new_prop(all_sent,prop_sent, list1[i][0], list1[i][1], "&E", anc1, "")
                if dummy == False:
                    return False
                candd.append([pn, list1[i][0], list1[i][1]])
                if (list2[0] == conditional or list2[0] == iff) and list1[i][1] != "~":
                    enc_str = enclose(list1[i][0])
                    def_info = find_sentences(enc_str)
                    list4 = prepare_iff_elim(greek2,def_info,list1[i][0],all_sent, list2[0],list2[1],pn)
                    conditionals.append(list4)
                elif list2[0] != "":
                    list5 = [""] * 39
                    if list2[0] == conditional:
                        list5[3] = 'c'
                    elif list2[0] == iff:
                        list5[3] = 'e'
                    else:
                        list5[3] = 'd'
                    list5[2] = pn
                    list5[4] = list1[i][0]
                    list5[5] = list1[i][1]
                    conditionals.append(list5)
    return True

def oc(str1):
    # this function determines if there is only one connective which is not &
    # it is used to weed out conditionals from the candd list
    list1 = [conditional, idisj, iff,xorr]
    j = 0
    for i in range(len(str1)):
        str2 = str1[i:i+1]
        if str2 in list1:
            j += 1
    if j == 1:
        return True
    else:
        return False

def plan(greek2,sent,all_sent, prop_sent, candd,candd2, conditionals, prop_name, disjuncts,tot_sent, kind,negat):

    global conc
    global sn
    global rel_conj
    conj_elim = []
    temp_conditionals = []
    conc = ""
    impl = ""
    qq = 0

    for i in range(len(sent)):
        if i == 8:
            bb = 7
        g = sent[i].count('(')
        h = sent[i].count(')')
        if g != h:
            print 'wrong number of parentheses in sentence:' + sent[i]
            sys.exit()

        sent[i][1] = enclose(sent[i][1])
        if sent[i][1].find("!") > -1:
            qq += 1
        else:
            if sent[i][1].count("(") != sent[i][1].count(")"):
                print "line " + str(sent[i][0]) + " does not have the right number \
                                             of parentheses"

            sent[i][1] = remove_outer_paren(sent[i][1])
            ostring = copy.copy(sent[i][1])
            nstring = proper_spacing(ostring)

            if os(sent[i][1]):
                if kind == "":
                    list3 = tilde_removal(nstring)
                    list4 = tilde_removal(ostring)
                    str2 = list3[0]
                    ng = list3[1]
                else:
                    ng = negat[i]
                    str2 = sent[i][1]
                candd.append([sent[i][0], str2, ng])
            else:
                list1 = find_sentences(ostring)
                sent[i][1] = list1[0][0]
                str2 = list1[0][0]
                if kind == "":
                    list4 = tilde_removal2(str2)
                    ng = list4[1]
                    str2 = list4[0]
                else:
                    ng = negat[i]
                list2 = mainconn(str2)
                if list2[0] == idisj or list2[0] == xorr:
                    if oc(str2):
                        candd.append([nstring, str2,ng])
                    list5 = [""] * 39
                    list5[2] = sent[i][0]
                    list5[3] = 'd'
                    list5[4] = str2
                    list5[5] = ng
                    conditionals.append(list5)
                elif list1[4][0][1] != "&":
                    if list1[4][0][1] != idisj and ng == "" and list1[4][0][1] != xorr:
                        list7 = prepare_iff_elim(greek2,list1,str2,all_sent,list2[0],list2[1],sent[i][0],tot_sent)
                    else:
                        list7 = [""] * 39
                        list7[2] = sent[i][0]
                        list7[3] = 'd'
                        list7[4] = str2
                        list7[5] = ng
                    conditionals.append(list7)
                    if oc(str2):
                        candd.append([sent[i][0], str2,ng])
                else:
                    list3 = get_conjuncts(str2)
                    for j in range(len(list3)):
                        list5 = tilde_removal2(list3[j])
                        if os(list3[j]):
                            conj_elim.append([sent[i][0],list5[0],list5[1]])
                        else:
                            temp_conditionals.append([sent[i][0], list5[0],list5[1]])

            no_contr = new_prop(all_sent,prop_sent,str2,ng,"",None,None,None,None,True,sent[i][0],ostring)
            if not no_contr:
                return False

    if conj_elim != []:
        for i in range(len(conj_elim)):
            no_contr = new_prop(all_sent,prop_sent,conj_elim[i][1],conj_elim[i][2],"&E",\
                        conj_elim[i][0],None)
            if not no_contr:
                return False
            candd.append([pn, conj_elim[i][1], conj_elim[i][2]])

    if temp_conditionals != []:
        for i in range(len(temp_conditionals)):
            str2 = temp_conditionals[i][1]
            str2 = remove_outer_paren(str2)
            str3 = enclose(str2)
            list1 = find_sentences(str3)
                #ffd
            ng = temp_conditionals[i][2]
            list2 = mainconn(str2)
            no_contr = new_prop(all_sent, prop_sent, str2, ng, "&E", temp_conditionals[i][0], None)
            if list2[0] != idisj and ng == "" and list2[0] != "&" and list2[0] != xorr:
                list7 = prepare_iff_elim(greek2,list1,str2,all_sent,list2[0],list2[1],pn+1,tot_sent)
            else:
                list7 = [""] * 39
                list7[2] = pn + 1
                list7[4] = str2
                list7[3] = 'd'
            if ng == "~":
                list7[5] = "~"
            conditionals.append(list7)
            if oc(str2):
                candd.append([pn+1, str2,ng])

            if not no_contr:
                return False

    list1 = statement_logic(greek2,prop_sent,all_sent, conditionals, candd,candd2,disjuncts,kind,conc,impl)
    return list1

def repeat_relations(str1):
    #this is for those definitions in which the same relation is related to two different
    #general variables
    a = ["group","x"]
    b = ["member",'z']
    e = ['every',"y"]
    f = ['personhood','y']

    final_list = [a,b,e,f]
    return final_list


def populate_sentences(p):
    global result_data
    global excel
    bool1 = False
    bool2 = False
    bool3 = True
    first_sent = False
    sent = []
    test_sent = []
    g = 0

    if not excel:

        for row in w4:
            p += 1
            if row[1] == "" and bool2 == True and not bool3:
                break
            elif row[1] == 'stop':
                break
            elif row[1] == "" and not bool3:
                test_sent.append(sent)
                sent = []
                g = 0
                bool1 = False
                bool2 = True
                first_sent = False
            elif row[1] == "":
                pass
            elif row[1][0] == "*":
                bool3 = True
            elif row[1] != "" and bool1 == False:
                bool3 = False
                str2 = row[1]
                g += 1
                if len(sent) == 0:
                    if str2.find(bottom) > -1:
                        tv = 'co'
                        str2 = str2[2:]
                    else:
                        tv = 'ta'
                else:
                    tv = ""
                str2.strip()
                sent.append([g, str2,'',tv])
                if not first_sent:
                    result_data['text_'+str(p-2)+'_1']=len(test_sent)
                first_sent = True
                bool2 = False
    else:
        for row in w4.rows:
            p += 1
            if row[2].value == None and bool2 == True and not bool3:
                break
            elif row[2].value == 'stop':
                break
            elif row[2].value == None and not bool3:
                test_sent.append(sent)
                sent = []
                g = 0
                bool1 = False
                bool2 = True
                first_sent = False
            elif row[2].value == None:
                pass
            elif row[2].value[0] == "*":
                bool3 = True
            elif row[2].value != None and bool1 == False:
                bool3 = False
                str2 = row[2].value
                g += 1
                if len(sent) == 0:
                    if str2.find(bottom) > -1:
                        tv = 'co'
                        str2 = str2[2:]
                    else:
                        tv = 'ta'
                else:
                    tv = ""
                str2.strip()
                sent.append([g, str2,row[0].value,tv])
                if not first_sent:
                     w4.cell(row=p-1,column=2).value = len(test_sent)
                first_sent = True
                bool2 = False

    return [test_sent,p]

def get_result(post_data,archive_id=None,request=None):
    global ws,w4, result_data,p
    if not excel and not one_sent:
        if archive_id:
            ws = Define3.objects.filter(archives_id=archive_id)
        else:
            archive = Archives.objects.latest('archives_date')
            ws = Define3.objects.filter(archives_id=archive.id)


    if not excel and not mysql and not one_sent:
        result_data = dict(post_data.iterlists())
        w4=[]
        index=0
        while  True:
            row = (post_data["text_"+str(index)+"_1"],post_data["text_"+str(index)+"_2"],post_data["text_"+str(index)+"_3"])
            w4.append(row)
            if row[1] == "stop":
                break
            index+=1
        w4=tuple(w4)

    if mysql:
        if archive_id:
            tw4 = Input.objects.filter(archives_id=archive_id)
        else:
            archive = Archives.objects.latest('archives_date')
            tw4 = Input.objects.filter(archives_id=archive.id)
        w4 = []
        for x in tw4:

            row = (x.col1,x.col2,x.col3)
            w4.append(row)
        w4 = tuple(w4)

    global prop_name,plural_c,anaphora,definite, prop_var, ind_var
    global ant_cond,conditionals,candd,rel_conj,conc,prop_sent,sn,impl
    global tagged_nouns,tagged_nouns2,dv_nam,basic_objects,idf_var,greek
    global gen_var,definite2,cnjts,test_one,stp,strt,candd2,pn,embed,affneg

    if one_sent: #ggg
        # str99 = 'co^ Russell has courage  % Russell is|a not courageous'
        # str99 = str99.lower()
        # list2 = tran_str(str99,1)
        # if len(list2[0]) == 1:
        #     test_sent = [[[1,list2[0],1,list2[1]]]]
        # else:
        #     test_sent = [[]]
        #     for i in range(len(list2[0])):
        #         if i == 0:
        #             test_sent[0].append([i + 1,list2[0][i],1,list2[1]])
        #         else:
        #             test_sent[0].append([i+1,list2[0][i],None,None])
        list1 = pop_sent('hey')
        # list1 = populate_sentences(p)
        for i in range(len(list1)):
            for j in range(len(list1[i])):
                list2 = tran_str(list1[i][j][1],2)
                list1[i][j][1] = list2[0]

        # test_sent = list1[0]
        test_sent = list1
        p = 1
        ex_dict = large_dict('hey')
    elif temp17:
        list1 = populate_sentences(p)
        test_sent = list1[0]
        p = list1[1]
        ex_dict = large_dict('hey')
    else:
        list1 = populate_sentences(p)
        test_sent = list1[0]
        p = list1[1]
        ex_dict = ""



    words = build_dict(ex_dict)
    rep_rel = repeat_relations('hey')
    st = time.time()
    bb = st - tot_tim

    if stp == 0:
        stp = len(test_sent)
    if not excel and not one_sent:
        views.progressbar_send(request,0,100,0,1)
    for k in range(strt,stp):
        if not excel and not one_sent:
            views.progressbar_send(request,strt,stp,k,1)
        if k == 37:
            bb = 7
        st1 = time.time()
        prop_name = []
        tot_sent = []
        all_sent = []
        plural_c = []
        embed = []
        pn = 400
        anaphora = ""
        impl = ""
        definite = []
        definite2 = []
        gen_var = []
        ant_cond = []
        conditionals = []
        affneg = []
        candd = []
        cnjts = []
        ind_var = []
        rel_conj = []
        conc = []
        identities = []
        prop_sent = []
        tagged_nouns = []
        tagged_nouns2 = []
        dv_nam = []
        basic_objects = []
        def_atoms = []
        prop_var = copy.deepcopy(prop_var4)
        idf_var = copy.deepcopy(idf_var2)
        greek2 = copy.deepcopy(greek)
        id_num = test_sent[k][-1][0] + 1
        sn = id_num
        dummy = divide_sent(words, test_sent[k], idf_var,tot_sent,all_sent)
        num_sent = len(all_sent)
        dummy = syn(tot_sent, all_sent, words,def_atoms)
        dummy = rel_repl(all_sent,tot_sent,words,dv_nam,idf_var,id_num)
        dummy = word_sub(idf_var,dv_nam, tot_sent, all_sent,words,id_num)
        dummy = define(tot_sent, all_sent,idf_var, dv_nam, words,rep_rel,identities,\
                       def_atoms,num_sent)
        list2 = identity(all_sent,tot_sent,basic_objects,words,candd,candd2,\
                conditionals,prop_sent,prop_name,id_num,identities,idf_var,\
                test_sent[k][0][3],greek2)
        test_sent[k] = list2[0]
        tot_prop_name.append(prop_name)
        yy = ""
        if list2[1] == "False":
            yy = k+1
            # break
        en1 = time.time()
        z = en1 - st1
        print str(k) + " - " + str("{0:.2f}".format(z))
    en = time.time()
    if stp == 0:
        stp = k
    g = (en-st)/(stp-strt)
    m = def_tim/(stp-strt)
    dd = st_log_tim/(stp-strt)
    global instan_used,instan_time
    if instan_used != 0:
        ee = instan_time/instan_used
    else:
        ee = 0
    print "average " + str("{0:.3f}".format(g))
    print "time used in definitions " + str("{0:.3f}".format(m))
    print "time used in statement logic " + str("{0:.3f}".format(dd))
    print "time used in instantiation " + str("{0:.3f}".format(ee))
    dummy = print_sent_full(test_sent,p,tot_prop_name,words,yy)
    if django2:
        views.progressbar_send(request,0,100,100,2)
    if excel:
        pass #Saved at last
    elif mysql:
        views.save_result(result_data)
    else:
        return result_data

if excel or one_sent or temp17:
    dummy = get_result('hey')
    st = time.time()
    if excel:
        wb4.save('../inference engine new.xlsx')
    if print_to_doc:
        wb4.save('/Users/kylefoley/PycharmProjects/inference_engine2/inference2/temp_proof.xlsx')
        # wb4.save('../temp_proof.xlsx')
    if words_used:
        wb5.save('../dictionary last perfect.xlsx')
    en = time.time()
    print en-st
elif mysql:
    dummy = get_result('hey')

tot_tim2 = time.time()
g = tot_tim2 - tot_tim
print "total " + str("{0:.1f}".format(g))

