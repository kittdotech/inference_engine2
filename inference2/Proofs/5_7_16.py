from openpyxl import load_workbook
from collections import Counter
import timeit
import copy
import time
import operator
import sys
# from django_tools.middlewares import ThreadLocal
# from inference2 import views
tot_tim = time.time()
excel = False
mysql = True
debug = False
words_used = False
strt = 0
stp = 0



######################################
# last perfect


if not excel and not mysql:
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
if debug:
    import easygui

anaphoric_relations = []
prop_name = []
prop_var = []
plural_c = []
embed = []
affneg = []
affirmed = []
denied = []
anaphora = ""
impl = ""
time1 = 0
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
conc = []
prop_sent = []
tagged_nouns = []
tagged_nouns2 = []
dv_nam = []
basic_objects = []
result_data = {}
cond_r = unichr(8835)
top = unichr(8868)
bottom = unichr(8869)
neg = unichr(172)
idd = unichr(8781)
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
sn = 1
pn = 400
id_num=0

ne = u"\u2260"
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
idf_var3 = [unichr(122 - t) + l1 for t in range(25)]
idf_var4 = [unichr(122 - t) + l2 for t in range(25)]
idf_var2 = idf_var2 + idf_var3 + idf_var4
p = 1
subscripts = [l1,l2,l3,l4]

if excel:
    wb4 = load_workbook('../inference engine.xlsx')
    wb5 = load_workbook('../dictionary last perfect.xlsx')
    w4 = wb4.worksheets[0]
    ws = wb5.worksheets[0]
else:
    ws = Define3.objects.all() #Kyle
    w4 = Input.objects.all()

#
# >> 8835
# ta^ 8868
# co^ 8869
# ; 172
# <> 8801
# c^ 8658
# # 8703
# i^ 8866
# > 8594
# nf^ 8876
# ed^ 8891
# + 8744
# && 8896
# @ 8855
# if^ 8660


def remove_outer_paren(str1):

    if str1 == "":
        return ""
    elif str1.count(")") == 0:
        return str1

    j = 0
    # on very rare occasions we will encounter strings of the following form ((p))
    if str1[0] != "(" and str1[-1] != ")":
        return str1
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

    return str1


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
        easygui.msgbox('error in isvariable function')
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


def find_sentences(instring, cut_skel = False):

    if instring == None:
        return

    g = instring.count('(')
    h = instring.count(')')
    if g != h:
        easygui.msgbox('wrong number of parentheses in sentence:' + instring)
        return "stop"
    marker = False
    il = -1
    total = -1
    c = -1
    neg_value = []
    str1 = ""
    sent1 = []
    single_sent = []
    doubles = []
    sent_type2 = []
    wneg = []
    output = [None] * 9
    # the skel name list names each single sentence after a greek letter, even if
    # the same sentence appears twice it obtains a different name on the second
    # appearance
    skel_nam = []
    sent_num = []
    if instring.find("~(") > -1:
        instring = instring.replace("~(", "(!")
    if instring.find(implies) > -1:
        str2 = implies
    elif instring.find(nonseq) > -1:
        str2 = nonseq
    str3 = mainconn(instring)
    instring = instring.strip()
    str4 = str3[0]
    f = str3[1]
    id_num = []
    id_num.append(["1",str4,f])
    sent_num.append([1, '1', instring, str4,f])
    prtnum = 1
    str21 = ""
    skel_string = instring
    p = 947
    connectives = ["&", idisj, iff, conditional, nonseq, implies,xorr]
    arr1 = []
    mini_c2 = mini_c + neg
    instring2 = copy.copy(instring)
    prt = copy.copy(instring)
    list1 = mainconn(instring)
    grandparent_type = list1[0]
    more_num = [unichr(945 + x) for x in range(24)]
    # prop_var = [unichr(97 + t) for t in range(26)]

    if os(instring) == False:
        temp_string = mainconn(instring)

        if instring.find(implies) > -1:
            str1 = implies
        elif instring.find(nonseq) > -1:
            str1 = nonseq
        else:
            if temp_string == iff:
                str1 = "bicond"
            elif temp_string == conditional:
                str1 = "cond"
            elif temp_string == "&":
                str1 = "cj"

        sent1.append(instring)
        neg_value.append("")
        sent_type2.append(str1)
        wneg.append(instring)
        skel_nam.append(None)

    j = 0
    n = 0
    for i in range(0, len(instring)):
        str1 = instring[i:(i + 1)]
        for o in connectives:
            if str1 == o:
                j += 1

    while n < j + 1:

        il += 1
        if il > 15:
            break

        e = 0
        l = len(instring)
        x = -1
        while x < l - 1:
            x += 1
            temp_string = instring[x: x + 1]
            if instring[x: x + 1] == "(":

                if marker == False:
                    z = x
                    marker = True

                total += 1
            elif instring[x: x + 1] == ")":
                total -= 1
                if total == -1:
                    marker = False
                    e += 1
                    c += 1

                    temp_sent = instring[z: x + 1]
                    if temp_sent == '(bIGc)':
                        pp = 7
                    otemp_sent = copy.copy(temp_sent)

                    if (len(instring) - len(temp_sent)) > 2:
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
                                # prtnum = int(prtnum)
                                # prtnum += 1
                                # prtnum = str(prtnum)
                                # f = 0
                                # numb = prtnum + str(f)



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
                        instring = instring[1:len(instring) - 1]
                        l = len(instring)
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
                            instring = str21
                            arr1.append(instring)
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

    sdefinition = cut_def([sent1,id_num],instring2)
    str1 = copy.copy(sdefinition)
    for i in range(len(wneg)):
        if os(wneg[i]):
            str1 = str1.replace(skel_nam[i][0],skel_nam[i][1])

    skel_string = str1
    # skel_string = remove_outer_paren(skel_string)
    if skel_string.find("(!") > -1:
        skel_string = skel_string.replace("(!","~(")

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
    global sn
    m = -1
    while m < len(all_sent) -1:
        m += 1
        if all_sent[m][47] == "no word sub":
            return
        bool1 = False
        list4 = copy.deepcopy(all_sent[m][46])
        old_sent = all_sent[m][0]
        oldp = all_sent[m][42]
        # old_list = copy.deepcopy(all_sent[m])
        for i in range(len(all_sent[m][46])):
            k = all_sent[m][46][i]
            if k == 49:
                bb = 8
            str2 = all_sent[m][k]
            if str2 != None:
                if str2 not in def_used and not str2.isupper():
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
                list4.remove(k)
            elif k in num and all_sent[m][45] != k:
                bool1 = True
                if str2 != None and str2 not in pronouns and str2 != 'there':
                    dummy = add_to_dv(dv_nam,all_sent,m,k,idf_var,str2)
                    list4.remove(k)

        if bool1:
            new_sent = build_sent(all_sent[m])
            newp = name_sent(new_sent)
            all_sent[m][0] = new_sent
            all_sent[m][42] = newp
            dummy = new_sentence2(old_sent,oldp,new_sent,newp,tot_sent,"SUB",id_num)
            all_sent[m][46] = list4
            bool1 = False
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
    all_sent[m][46] = "x"
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

def define(tot_sent, all_sent, idf_var, dv_nam,words,rep_rel,identities,def_atoms):

    all_sent = remove_duplicates(all_sent,0)
    num = [3,5,10,14,16,18,20,22,24,26,28,30,32,34,63,64,65]
    pronouns2 = copy.deepcopy(words[24])
    if "it" in pronouns2:
        pronouns2.remove("it")
        pronouns2.remove("it"+up)
    pronouns = pronouns2
    prop_con = [] # delete this after I'm sure I don't need it
    p_sent = []
    determinative = words[2]
    definitions = words[16]
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
    atoms2 = [['moment','T',14],['relationship','I',5],['point','S',14],['number','N',14],\
              ['thought','TK',14],['imagination','AI',14],\
            ['property',"IA",14],['possible world','U',14],\
              ['possible relationship',"U",5],['word','AW',"b"],['reality',"I",14]]

    def_relat = ['IA','IG','=','H']
    used_atoms = []
    ua_relat = [] #used atomic relations
    #unique objects which form a group, in the definiednum the relation is = but in the
    #definiens the IG relation appears
    unq_gr = ['time'] #unique group
    global sn,anaphora,gen_var
    bool1 = False
    once = False
    def_sent = []
    al_def = [] #already defined
    numbers_def = []
    defined = []
    last = ["many"+ua,"few"+ua]
    universal = ['all','no','any','no'+us,"a","many"+un,"a"+ua]
    universal2 = ['no','no'+us]
    indefinite = ['a',"many"+un,"a"+ua]
    universal3 = ['all','any','no','no'+us]

    for i in range(len(dv_nam)):
        if i == 3:
            bb = 7
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
            #list1[46] = "x"
            all_sent.append(list1)
            # say you have the word 7 in your claim, then the code will define all numbers
            # down to 0 if you do not have the following code
            try:
                str3 = int(dv_nam[i][1])
                numbers_def.append(dv_nam[i][1])
            except ValueError:
                pass

    m = -1
    g = (len(all_sent))
    while m < g - 1:
        m += 1
        if all_sent[m][45] > 2:
            all_sent.append(all_sent[m])
            del all_sent[m]
            m -= 1
            g -= 1
    for d in range(0,9):
        if d == 1:
            once = True
            num = [0]
        elif d == 2:
            num = [3,10,16,20,24]
        elif d == 4:
            once = True
            num = [0]
        elif d == 5:
            num = [3,10,16,20,24]
        elif d == 6:
            num = [5,14]
        elif d == 7:
            once = True
            num = [0]
        elif d == 8:
            num = [9,14,48]
        m = -1
        while m < len(all_sent) -1:
            m += 1
            if len(all_sent) > 80:
                break
            if all_sent[m][46] != "x" and all_sent[m][46] != "y":
                bool2 = False
                if m == 5 and d == 8:
                    bb = 7
                if m > 100:
                    easygui.msgbox('in the define function you are caught in an infinite loop')
                for i in num:
                    if i == 14 and m == 2:
                        bb = 7
                    if i == 64 and m == 2:
                        bb = 7
                    str1 = all_sent[m][i]
                    relat = all_sent[m][9]
                    old_sent = all_sent[m][0]
                    oldp = all_sent[m][42]
                    if d == 0:
                        if (i == 5 and all_sent[m][3] == None and all_sent[m][40] == 69) \
                            or (i == 14 and all_sent[m][10] == None and all_sent[m][40] == 70):
                            pn_poss_noun = True
                        else:
                            pn_poss_noun = False

                #this is for those sentences whose noun was once part of a relative pronoun
                        if i == all_sent[m][45]:
                            print 'noun once part of relative pronoun'
                            str3 = findinlist(all_sent[m][i],tagged_nouns2,1,0)
                            if str3 == None:
                                all_sent.append(all_sent[m])
                                print "this might contain an error"
                                break
                            all_sent[m][i] = str3
                            new_sent = build_sent(all_sent[m])
                            newp = name_sent(new_sent)
                            dummy = new_sentence2(old_sent,oldp,new_sent,newp,tot_sent,"rel pro")
                            all_sent[m][0] = new_sent
                            all_sent[m][42] = newp
                            all_sent[m][45] = None

                        elif (str1 in pronouns or str1 in determinative or pn_poss_noun) \
                                and str1 not in universal:
                            bool1 = True
                            if str1 in pronouns:
                                str2 = "pronoun"
                            elif pn_poss_noun:

                                str2 = "proper name possessive"
                                str1 = 'the'
                            else:
                                str2 = "determinative"
                            if all_sent[m][43] != i:
                                definition = findinlist(str1,definitions,0,1)
                                if all_sent[m][0] not in def_sent:
                                    list3 = copy.deepcopy(all_sent[m])
                                    dummy = def_rn(defined,al_def,definition, str1,0, tot_sent, \
                                        dv_nam, idf_var,words, all_sent,m,rep_rel,[],[],\
                                            str2,i)

                                    if str1 == 'i': # this prevents 'i' from being defined
                                        list3[43] = i # many times
                                    else:
                                        list3[46] = "x"
                                    all_sent[m] = list3

                                    if str1 == "i":
                                        m -= 1
                                    else:
                                        def_sent.append(all_sent[m][0])
                                    break
                    elif d == 1 and once:
                        once = False
                        dummy = division(tot_sent,all_sent,words,0,def_sent)
                        dummy = division(tot_sent,all_sent,words,4,def_sent)
                        m = len(all_sent)
                        break
                    elif d == 2 and all_sent[m][i] in universal2 and scope_rel_pro(all_sent[m],i):
                        definition = findinlist(str1,definitions,0,1)
                        list3 = copy.deepcopy(all_sent[m])
                        dummy = def_rn(defined,al_def,definition, str1,0, tot_sent, \
                            dv_nam, idf_var,words, all_sent,m,rep_rel,[],[],\
                                       "determinative",i)
                        list3[46] = "x"
                        all_sent[m] = list3
                        def_sent.append(all_sent[m][0])
                        break

                    elif d == 3 and (all_sent[m][i] in indefinite or (all_sent[m][i] in universal2 and scope_rel_pro(all_sent[m],i))):
                        definition = findinlist(str1,definitions,0,1)
                        list3 = copy.deepcopy(all_sent[m])
                        dummy = def_rn(defined,al_def,definition, str1,0, tot_sent, \
                            dv_nam, idf_var,words, all_sent,m,rep_rel,[],[],\
                                "determinative",i)
                        list3[46] = "x"
                        all_sent[m] = list3
                        def_sent.append(all_sent[m][0])
                        if all_sent[m][57] != None:
                            if all_sent[m][57] == i:
                                if all_sent[m][3] == "":
                                    anaphora = all_sent[m][5]
                                    all_sent[m][57] = None
                        break
                    elif d == 4 and once:
                        once = False
                        dummy = division(tot_sent,all_sent,words,1,def_sent)
                        m = len(all_sent)
                        break
                    elif d == 5 and (all_sent[m][i] in universal3 or all_sent[m][i] in poss_pro):
                        definition = findinlist(str1,definitions,0,1)
                        list3 = copy.deepcopy(all_sent[m])
                        if all_sent[m][i] in poss_pro:
                            str2 = "poss pro"
                        else:
                            str2 = "determinative"

                        dummy = def_rn(defined,al_def,definition, str1,0, tot_sent, \
                            dv_nam, idf_var,words, all_sent,m,rep_rel,[],[],\
                                str2,i)
                        list3[46] = "x"
                        all_sent[m] = list3
                        def_sent.append(all_sent[m][0])
                        break
                    elif d == 6 and all_sent[m][i] == 'it':
                        list3 = copy.deepcopy(all_sent[m])
                        list2 = copy.deepcopy(all_sent[m])
                        list2[i] = anaphora
                        list2[0] = None
                        dummy = new_sentence(tot_sent,all_sent[m],list2,"","",1,"DE it")
                        list3[46] = "x"
                        all_sent[m] = list3
                        all_sent.append(list2)
                        break
                    elif d == 7 and once:
                        once = False
                        dummy = division(tot_sent,all_sent,words,2,def_sent)
                        m = len(all_sent)
                        break
                    elif d == 8:
                        adverb = False
                        id = False
                        kind = ""
                        if str1 == 's':
                            bb = 8
                        if m == 5:
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
                                all_sent[m][46] = "x"
                            elif i == 9 and relat != 'IA' and relat != 'IG' and relat != '=' \
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
                                    definition = "(c'=" + definiendum + ") & (d'=natural_whole) & ((bIGc') " + conditional \
                                    + " (bIGd'))"
                                pos = definitions[g][2]
                                circ = definitions[g][3]
                                circ2 = all_sent[m][43]
                                basic_molecule = definitions[g][4]
                    #this prevents us from getting caught in an infinite loop.
                                if basic_molecule == 'b' and all_sent[m][9] == 'IG':
                                    break
                                if relat == 'IG' and definiendum in unq_gr:
                                    break
                                if circ2 == 'c':
                                    circ += circ2
                                if (relat == 'IA' and pos == 'a') or (relat == 'IG' and pos == 'n') or (relat == 'H' and pos == 'n') \
                                    or pos == 'r' or pos == 'e' or pos == 's' or (relat== '=' and pos == 'n') or adverb or id:
                                    if definition != None and all_sent[m][0] not in def_sent:
                                        def_sent.append(all_sent[m][0])
                                        dummy = def_rn(defined,al_def,definition, definiendum,0,tot_sent,dv_nam, idf_var,\
                                            words,all_sent,m,rep_rel,[],[],kind,i,circ)
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
    return

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
        list1[9] = "IG"
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
                if all_sent[j][9] == 'IG' and all_sent[j][14] == str1 and all_sent[j][46] != "x"\
                        and all_sent[j][46] != "y":
                    str2 = all_sent[j][5]
                    con = findinlist(str2,dv_nam,0,1)
                    pos = findinlist(con,posp,0,1)
                    if pos == None:
                        bb = 7
                    if con != None:
                        if pos == 'a':
                            str4 = 'IA'
                        elif pos == 'n':
                            str4 = 'IG'
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
    global prop_var,affneg,prop_name,affirmed,denied

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
        # if ng == "":
        #     affirmed.append(h)
        # else:
        #     denied.append(h)
        # if h in affirmed and h in denied:
        #     affneg.append(str1)

        return ng + h
    else:
        prop_name.append([prop_var[0], no_space, str1])
        str2 = prop_var[0]
        # if ng == "":
        #     affirmed.append(str2)
        # else:
        #     denied.append(str2)
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
    # num = [3, 10, 16, 20, 24, 28, 32]
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

    must_be_blank = [2,3,4,6,7,10,11,13,15,16,17,18,20,21,23,24,25,27,28,29,31,32,33,\
        35,36,49,50,51,52,55]
    must_be_variable = [5,14,22,30]

    for i in must_be_blank:
        if list1[i] != None and list1[i] != '':
            return False
    for i in must_be_variable:
        if list1[i] != None:
            if not isvariable(list1[i]):
                return False
    return True

def build_sent(list1,g=0):

    #if you revise this list then then you must also revise it in
    #the add_sent2, as well as the function 'that'
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

def id_sent(list4,all_sent,irrel_group = [],h=0,embed_var=[]):
    # this function turns the dv_nam into a string of conjuncts

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
    pos = words[28]
    doubles = words[31]
    doubles.sort()
    bool1 = False
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
                bool1 = True
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
                    if all_sent[i][10] == "a":
                        all_sent[i][10] = 'no' + us
                        bool1 = True
                        bool2 = True
                        rule = "DE ~ a"
                    elif all_sent[i][10] in cat:
                        rule = "DE ~ " + all_sent[i][10]
                        all_sent[i][10] = 'no'
                        bool1 = True
                        bool2 = True
                    elif all_sent[i][9] == ne:
                        all_sent[i][9] = "="
                        bool1 = True
                        bool2 = True
                        rule = "DE ~"+ne
                elif j == 49:
                    if all_sent[i][16] == "a":
                        all_sent[i][16] = 'no' + us
                        bool1 = True
                        bool2 = True
                        rule = "DE ~ a"
                    elif all_sent[i][16] in cat:
                        all_sent[i][16] = 'no'
                        bool1 = True
                        bool2 = True
                        rule = "DE ~ " + all_sent[i][18]
                    elif all_sent[i][15] == ne:
                        all_sent[i][15] = "="
                        bool1 = True
                        bool2 = True
                        rule = "DE ~"+ne
                elif j == 50:
                    if all_sent[i][20] == "a":
                        all_sent[i][20] = 'no' + us
                        bool1 = True
                        bool2 = True
                        rule = "DE ~ a"
                    elif all_sent[i][20] in cat:
                        all_sent[i][20] = 'no'
                        bool1 = True
                        bool2 = True
                        rule = "DE ~ " + all_sent[i][22]
                elif j == 51:
                    if all_sent[i][24] == "a":
                        all_sent[i][24] = 'no' + us
                        bool1 = True
                        bool2 = True
                        rule = "DE ~ a"
                    elif all_sent[i][24] in cat:
                        all_sent[i][24] = 'no'
                        bool1 = True
                        bool2 = True
                        rule = "DE ~ " + all_sent[i][26]
                elif j == 52:
                    if all_sent[i][28] == "a":
                        all_sent[i][28] = 'no' + us
                        bool1 = True
                        bool2 = True
                        rule = "DE ~ a"
                    elif all_sent[i][28] in cat:
                        all_sent[i][28] = 'no'
                        bool1 = True
                        bool2 = True
                        rule = "DE ~ " + all_sent[i][30]
                if bool1:
                    all_sent[i][j] = None
                    bool1 = False
        if bool2:
            new_sent = build_sent(all_sent[i])
            newp = name_sent(new_sent)
            dummy = new_sentence2(old_sent,oldp,new_sent,newp,tot_sent,rule,"")
            bool2 = False
            all_sent[i][0] = new_sent
            all_sent[i][42] = newp

    return


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

def division(tot_sent, all_sent,words,kind,def_sent=[]):

    global anaphora,idf_var

    univ = ['all','any','no','no'+us]
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
                            list17 = copy.deepcopy(all_sent[m])
                            if all_sent[m][8] != None or all_sent[m][12] != None:
                                str7 = "~"
                                all_sent[m][8] = None
                                all_sent[m][12] = None
                            else:
                                str7 = None
                            list1[8] = str7
                            list1[3] = all_sent[m][n]
                            if all_sent[m][r] != "IG":
                                list1[5] = all_sent[m][i+1]
                            else:
                                list1[5] = all_sent[m][5]
                            list1[9] = "IA"
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
                        list1[9] = "IG"
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
    list1[9] = "IA"
    list2 = [None] * 80
    list2[5] = new_var
    list2[14] = str1
    list2[9] = "IG"
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
    all_sent[m][46] = "x"

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
    list3[0] = str2
    all_sent.append(list3)
    str2p = name_sent(str2)
    embed.append(list2)
    dummy = new_sentence2(all_sent[m][0],all_sent[m][42],str2,str2p,tot_sent,"DE that"+uc)
    return


def scope_uni(all_sent,m,i,kind = ""):

    comma = all_sent[m][39]
    univ = ['all','any','no','no'+us,'a','many'+up,'many'+uo]
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

def rel_pro(i,m,all_sent,list1,new_var=""):

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

def prop_type2(dfn_num,sent_num,paren_conn,paren_num):

    #the dfn_num (definiens number) will always have three digits
    # any sentence that is not a conjunct in the definiens should not be defined

    if sent_num[3] == dfn_num:
        if paren_num != dfn_num:
            if paren_conn != "&":
                return 'x'

def prop_type(paren_num,gparen_num,paren_conn,gparen_conn,sent_num,def_con):

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
        easygui.msgbox("you have not coded for this sentence type yet")

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
    list3 = division("",all_sent,words,3)
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

def abb_change(list5, already_checked,all_sent,def_sent,i,match_dv,rename,j,def_con,\
               new_match = [],second=False):

    global never_used,dv_nam
    cap = False
    used_var = []
    spec_prop = ['general','particular','definite','indefinite'] #special properties

    for t in range(len(all_sent)):
        no_match = False
        bool1 = False
        if all_sent[t][9] == "IA":
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
                    str2 = "(" + def_sent[i][j] + mini_c + all_sent[t][j] + ")"
                    rename.append(str2)
                    if cap:

                        str3 = build_sent(def_sent[i])
                        # str3 = str3 + l3
                        rename.append(str3) #eee
                    if second:
                        for s in range(len(match_dv)):
                            if match_dv[s][0] == def_sent[i][j]:
                                never_used.append(match_dv[s][1])
                                break
                        new_match.append([def_sent[i][j],all_sent[t][j]])
                    def_sent[i][j] = all_sent[t][j]
                    return False
    return True

def abb_change2(match_dv,def_sent,i,idf_var,temp_match,j,gen_var,cnnan,rename):

    match_dv.append([def_sent[i][j], idf_var[0]])
    str1 = "(" + def_sent[i][j] + mini_c + idf_var[0] + ")"
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
    list1[9] = "IA"
    list1[14] = adj_var
    new_sent = build_sent(list1)
    newp = name_sent(new_sent)
    list1[0] = new_sent
    list1[42] = newp
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
           words,all_sent,m,rep_rel,prop_con,p_sent,kind = "",k=0,circ = ""):
    # def_rn = definition rename
    # this function renames the variables in a definition
    #end0
    global sn,plural_c,definite2,definite,anaphora,ind_var,gen_var,def_used
    b = time.time()
    #this is for those determinatives which have negations in their definitions where
    #the sentences has an R variable
    identical_det = ["only","anything_except","anyone_except","no","many"+um,"many"+un,\
        "no" + us]
    if definiendum == "you":
        bb = 7
    new_idf = []
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
    detached = [conditional,iff,xorr,idisj]
    str1 = copy.copy(definition)
    #if bool1 is false then there is a series of conjuncts that need to be removed from
    # the definition
    if kind == "" or kind == 'R':
        def_info = find_sentences(definition,True)
    else:
        def_info = find_sentences(definition)
    x = findposinlist(definiendum,rep_rel,0)
    if x > -1:
        rr_var = rep_rel[x][1]
    else:
        rr_var = 0
    def_loc = def_info[7]
    def_num = def_info[4][def_loc][0]
    dfn_num = def_num + "2"
    poss_str = ""
    ld = len(def_num)
    list1 = []
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

    adj_sent = []
    has_plural = list1[1]
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

        if definiendum != 'i':
            str1 = findinlist(definiendum,dv_nam,1,0)
            if str1 == None:
                all_sent[m][k] = idf_var[0]
                match_dv.append(["c",idf_var[0]])
                dv_nam.append([idf_var[0],definiendum])
                new_var.append(idf_var[0])
                match_type.append(9)
                del idf_var[0]
            else:
                all_sent[m][k] = str1
                match_dv.append(["c'",str1])
                match_type.append(9)
        else:
            match_dv.append(['i','i'])
            match_type.append(9)
        # when constructing definitions of personal pronouns or of determinatives the object of the IG relation
        # must be b and the subject must be z
    elif kind == 'determinative' or kind == 'poss pro' or kind == 'proper name possessive':
        if k == 10:
            j = 14
        else:
            j = k + 2
        ovar = all_sent[m][j]
        if kind == "proper name possessive":
            match_dv.append(["b",all_sent[m][k]])
        elif definiendum == "its" + ua or definiendum == "its" + ub: # its is slightly weird because it almost never exists
        # in the subject position
            match_dv.append(["c",all_sent[m][14]])
            all_sent[m][k] = ""
            match_dv.append(["b",all_sent[m][5]])
        else:
            all_sent[m][k] = ""
            match_dv.append(["b",all_sent[m][j]])
        if definiendum == 'the' or definiendum == 'that'+ud:
            str1 = all_sent[m][j]
            str3 = findinlist(str1,dv_nam,0,1)
            str2 = findinlist(str3,definite,1,0)
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
    skel_string = def_info[5]
    exception = []
    not_many = False
    first_in_def = [def_num+"1",def_num + "11"]
    temp_plural = []
    heir_num = []
    spec_var = ['y','x','w']
    rule_found = False
    univ = ['any','all','no','no' + us]
    idfq = ['a','many'+up,'many'+us,'many'+ud,'many'+uo,"a"+ua]
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
    for i in range(len(def_info[0])):
        if i == 21:
            bb = 8
        n = def_info[4][i][0][:ld]
        if def_info[4][i][1] == iff and not rule_found:
            rule = "DF " + definiendum
            rule_found = True
            def_con = iff
        elif def_info[4][i][1] == conditional and not rule_found:
            def_con = conditional
            rule = "NC " + definiendum
            rule_found = True
        bool3 = False
        if "=" in def_info[3][i] and n != def_num:
            bool3 = True
        # if mini_e in def_info[3][i]:
        #     bool3 = True
        if os(def_info[3][i]) == True and not bool3:
        # if os(def_info[3][i]) == True and n == def_num:
            temp_str = space_words(def_info[3][i])
            temp_str = temp_str.replace("(","")
            temp_str = temp_str.replace(")","")
            telist7 = categorize_words(words,temp_str,idf_var,all_sent,1,False,"","",taken_out)
            bool1 = False
            bool2 = False
            bb = 8
            # if bb == 9:
            #     pass
            if telist7[9] == "n":
                 pass
            else:
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
                        if p == 14:
                            bb = 8
                        if telist7[p] in spec_var:
                            str2 = idf_var[0]
                            spec_var.remove(telist7[p])
                            match_dv.append([telist7[p],str2])
                            del idf_var[0]
                        if p == j and str2 != "" and str2 != None:
                            telist7[p] = str2
                        else:
                            telist7[p] = all_sent[m][p]
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
                        telist7[8] = ""
                        telist7[10] = "no"
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
                            telist7[46] = 'y'
                        elif gparen_conn == iff:
                            telist7[46] = 'y'
                    elif paren_num != def_num and paren_conn in detached:
                        if sent_num[-1] == "1" and paren_conn == conditional:
                            telist7[46] = 'y'
                        elif paren_conn == iff:
                            telist7[46] = 'y'

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
                    if kind == "R" or kind == 'AS':
                        match_dv.append([def_sent[i][14],all_sent[m][14]])
                        if bool1:
                            break
                else:
                    relat = def_sent[i][9]
                    oobj = def_sent[i][14]
                    nobj = findinlist(oobj,match_dv,0,1)
                    for j in range(len(all_sent)):
                        if all_sent[j][9] == relat and all_sent[j][14] == nobj:
                            match_dv.append([def_sent[i][5],all_sent[j][5]])
                            break


    #if the definiendum is many-o then its object variable needs to be matched
    if definiendum == 'many' + uo:
        match_dv.append(['c',all_sent[m][14]])

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
                            str2 = '(' + temp_str + mini_c + str3 + ')'
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


                            dummy = abb_change2(match_dv,def_sent,i,idf_var,temp_match,j,gen_var,cnnan,rename)
                        else:
                            # here we check to see if it has a plural form
                            if j == 14 and def_sent[i][9] == 'OFP':
                                g = findposinlist(def_sent[i][5],plural_c,1)
                                if g > -1:
                                    match_dv.append([def_sent[i][j],plural_c[g][0]])
                                    def_sent[i][j] = plural_c[g][0]
                            else:
                                already_checked = []
                                if j == 5:
                                    list5 = num3
                                else:
                                    list5 = num4
                                no_match = abb_change(list5, already_checked,all_sent,\
                                    def_sent,i,match_dv,rename,j,def_con)
                                if not no_match and j == 14 and unmatched != []:
                                    dummy = abb_change(num3, already_checked,all_sent,\
                                        def_sent,i,match_dv,rename,j,def_con)
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
                        def_sent,i,match_dv,rename,5,def_con,new_match,True)
                    if no_match:
                        temp_str = def_sent[i][j]
                        str3 = findinlist(temp_str,match_dv,0,1)
                        if str3 != None and temp_str != str3:
                            def_sent[i][j] = str3
                            str2 = '(' + temp_str + mini_c + str3 + ')'
                            if str2 not in rename and str2 != "":
                                rename.append(str2)
                            str2 = ""
                        elif temp_str == str3:
                            pass
                        else:
                            dummy = abb_change2(match_dv,def_sent,i,idf_var,temp_match,j,gen_var,cnnan,rename)
                            unmatched2.append([i,j])
            else:
                temp_str = def_sent[i][j]
                str3 = findinlist(temp_str,match_dv,0,1)
                if str3 != None and temp_str != str3:
                    def_sent[i][j] = str3
                    str2 = '(' + temp_str + mini_c + str3 + ')'
                    if str2 not in rename and str2 != "":
                        rename.append(str2)
                    str2 = ""
                else:
                    if def_sent[i][j] not in taken_out:
                        dummy = abb_change2(match_dv,def_sent,i,idf_var,temp_match,j,gen_var,cnnan,rename)
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
                        str2 = '(' + str3 + mini_c + str4 + ')'
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
                    str4 = "(" + str3 + "=" + prop_con[i][0] + ")"
                    rename.append(str4)
                g = findposinlist(prop_con[i][0],dv_nam,1)
                if g > -1:
                    bool2 = True
                    str3 =idf_var[0]
                    del idf_var[0]
                    match_dv2.append([prop_con[i][0],str3])
                    str4 = "(" + prop_con[i][0] + "=" + str3 + ")"
                    rename.append(str4)
                else:
                    g = findposinlist(str3,dv_nam,0)
                    if g > -1:
                        str5 = dv_nam[g][1]
                        if str5 != str1:
                            str3 =idf_var[0]
                            del idf_var[0]
                            match_dv2.append([prop_con[i][0],str3])
                            str4 = "(" + prop_con[i][0] + "=" + str3 + ")"
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
            def_sent[i][43] = k
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
                list1[46] = "x"
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
            skel_string = skel_string[:g+4] + "(" + str4 + skel_string[g+4:h-1] + ") " + skel_string[h:]

        g = skel_string2.find(iff)
        h = skel_string2.find(conditional)
        if poss_str != "":
            skel_string2 = skel_string2[:g+3] + str4p + skel_string2[g+3:h] + skel_string2[h:]
        elif h == -1:
            skel_string2 = skel_string2[:g+4] + str4p + skel_string2[g+4:]
        else:
            skel_string2 = skel_string2[:g+4] + "(" + str4p + skel_string2[g+4:h-1] + ")" + skel_string2[h-1:]

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

    if definiendum == 'any':
        bb = 8
    list1 = []
    num = [5,14,15,18,26,30]
    def_var = findinlist("definite",dv_nam,1,0)
    indef = findinlist("indefinite",dv_nam,1,0)
    gen = findinlist("general",dv_nam,1,0)

    for i in range(len(def_sent)):
        if def_sent[i][9] == 'IA':
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
        if definiendum == "no"+us or definiendum == "no" or definiendum == "many" + un:
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
            # def_sent[i][46] = None
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

    easygui.msgbox('your method for finding the antecedent variable is not working')

def not_a(list1,k,tot_sent,all_sent):

    num = [10,16,20,24]

    for i in num:
        if i > k and (list1[i] == "a" or list1[i] == "a" + ua):
            list2 = copy.deepcopy(list1)
            if list1[i] == "a":
                rule = "DE not a"
            else:
                rule = "DE not a" + ua
            list2[i] = 'no'+us
            list2[8] = None
            str1 = build_sent(list2)
            str1p = name_sent(str1)
            list2[0] = str1
            list2[42] = str1p
            dummy = new_sentence2(list1[0],list1[42],str1,str1p,tot_sent,rule)
            list1[46] = "x"
            all_sent.append(list1)
            return list2
    return list1

def plurals(tot_sent, all_sent, words, dv_nam, idf_var):

    global plural_c
    global sn
    c = time.time()
    all_sent = remove_duplicates(all_sent,0)
    pnouns = words[26]
    bool1 = False
    for m in range(len(dv_nam)):
        pluralf = dv_nam[m][1]
        g = findposinlist(pluralf,pnouns,0)
        if g > -1:
            if not bool1:
                new_abb = idf_var[0]
                del idf_var[0]
                dv_nam.append([new_abb,"plural form"])
                bool1 = True
            str1 = dv_nam[m][0]
            singular = findinlist(pluralf,pnouns,0,1)
            singa = findinlist(singular,dv_nam,1,0)
            if singa == None:
                singa = idf_var[0]
                del idf_var[0]
                dv_nam.append([singa,singular])
            defndm = "(" + str1 + "=" + pluralf + ")"
            sent1 = "(" + str1 + "OFP" + singa + ")"
            list1 = [None] * 80
            list1[0] = sent1
            list1[5] = str1
            list1[9] = "OFP"
            list1[14] = singa
            plural_c.append([singa,str1])
            sent2 = "(" + str1 + "IG" + new_abb + ")"
            list3 = [None] * 80
            list3[5] = str1
            list3[9] = "IG"
            list3[14] = new_abb
            list3[0] = sent2
            defp = name_sent(defndm)
            sent1p = name_sent(sent1)
            list1[42] = sent1p
            all_sent.append(list1)
            sent2p = name_sent(sent2)
            list3[42] = sent2p
            all_sent.append(list3)
            tot = defndm + " " + iff + " (" + sent1 + " & " + sent2 + ")"
            totp = defp + " " + iff + " (" + sent1p + " & " + sent2p + ")"
            sn += 1
            tot_sent.append([sn,tot,totp,"","DE " + pluralf,"","","",""])
    b = time.time()
    d = b - c
    return

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
    spec_rel = ["IG","IA"]
    posp = words[28]
    doubles = words[31]
    triples = words[32]
    proper_names = words[35]
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
            str4 = word + " " + list1[i+1] + " " + list1[i+2]

            # if "," in str4:
            #     str4 = str4.replace(",","")
            #     has_comma = str4
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
        # if word == 'TO':
        #     bb = 8
        #     break
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
        elif pos == 'ps' and relation_type == 0 and list1_cat[5] == None:
            list1_cat[69] = word
            list2.append(69)
            list1_cat[40] = 69
        elif pos == 'a' and relation_type == 0:
            list1_cat[4] = word
            list2.append(4)
        elif pos == 'm' and list1_cat[3] == None and list1_cat[5] == None and relation_type == 0:
            list1_cat[47] = word
            list2.append(47)
        elif word == neg and isvariable(next_word) and list1_cat[5] == None:
            list1_cat[55] = word
            list2.append(55)
        elif (pos == 'n' or pos == 'p') and relation_type == 0 and list1_cat[5] == None:
            list1_cat[5] = word
            list2.append(5)
        elif (pos == 'n' or pos == 'p') and relation_type == 0 and list1_cat[5] == None:
            list1_cat[5] = word
            list2.append(5)
        elif pos == 'c' and relation_type == 0 and list1_cat[5] != None:
            list1_cat[66] = word
            list2.append(66)
        elif (pos == 'n' or pos == 'p') and relation_type == 0 and list1_cat[66] != None:
            list1_cat[67] = word
            list2.append(67)
        elif pos == 'n' and relation_type == 0 and list1_cat[5] != None:
            list1_cat[35] = word
            list2.append(35)
        elif pos == 'u' and relation_type == 0 and list1_cat[5] != None:
            list1_cat[59] = word
            list2.append(59)
        elif word == 'that'+uc and list1_cat[7] == None and list1_cat[14] == None: # uc
             list1_cat[7] = word
             list2.append(7)
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
        # this line of code must be first because if the word is an adjective
        # and the relation is IA then it must go in slot 14
        elif pos == 'm' and relation_type == 1 and list1_cat[14] == None and \
            list1_cat[60] == None:
            list1_cat[12] = word
            list2.append(12)
        elif pos == 'a' and relation_type == 1 and list1_cat[9] == 'IA':
            list1_cat[14] = word
            list2.append(14)
        elif pos == 'ps' and relation_type == 1 and list1_cat[14] == None:
            list1_cat[70] = word
            list2.append(70)
            list1_cat[40] = 70
        elif pos == 'a' and relation_type == 1:
            list1_cat[13] = word
            list2.append(13)
        elif (pos == 'n' or pos == 'p') and relation_type == 1 and list1_cat[14] == None:
            list1_cat[14] = word
            list2.append(14)
        elif pos == 'n' and relation_type == 1 and list1_cat[14] != None and list1_cat[60] == None:
            list1_cat[36] = word
            list2.append(36)
        elif pos == 'e' and relation_type == 1:
            list1_cat[48] = word
            list2.append(48)
        elif pos == 'u' and relation_type == 1 and list1_cat[14] != None:
            list1_cat[60] = word
            list2.append(60)
        elif (pos == 'n' or pos == 'p') and relation_type == 1 and list1_cat[60] != None:
            list1_cat[63] = word
            list2.append(63)
        elif (pos == 'm' and relation_type == 1) or (pos == "m" and list1_cat[15] in spec_rel):
            list1_cat[49] = word
            list2.append(49)
        elif pos == 'r' and relation_type == 1:
            list1_cat[15] = word
            relation_type = 2
            list2.append(15)
            if snoun != "" and snum == 18:
                list1_cat[18] = snoun
        elif (pos == 'd' or pos == 'q') and relation_type == 2:
            list1_cat[16] = word
            list2.append(16)
        elif pos == 'a' and relation_type == 2 and list1_cat[15] == 'IA':
            list1_cat[18] = word
            relation_type = 2
            list2.append(18)
        elif pos == 'a' and relation_type == 2:
            list1_cat[17] = word
            list2.append(17)
        elif (pos == 'n' or pos == 'p') and relation_type == 2 and list1_cat[18] == None:
            list1_cat[18] = word
            list2.append(18)
        elif pos == 'u' and relation_type == 2 and list1_cat[18] != None:
            list1_cat[61] = word
            list2.append(61)
        elif (pos == 'n' or pos == 'p') and relation_type == 2 and list1_cat[61] != None:
            list1_cat[64] = word
            list2.append(64)
        elif (pos == 'm' and relation_type == 2) or (pos == "m" and list1_cat[18] in spec_rel):
            list1_cat[50] = word
            list2.append(50)
        elif pos == 'r' and relation_type == 2:
            relation_type = 3
            list1_cat[19] = word
            list2.append(19)
            if snoun != "" and snum == 22:
                list1_cat[22] = snoun
        elif (pos == 'd' or pos == 'q') and relation_type == 3:
            list1_cat[20] = word
            list2.append(20)
        elif pos == 'a' and relation_type == 3 and list1_cat[19] == 'IA':
            list1_cat[22] = word
            relation_type = 3
            list2.append(22)
        elif pos == 'a' and relation_type == 3:
            list1_cat[21] = word
            list2.append(21)
        elif (pos == 'n' or pos == 'p') and relation_type == 3 and list1_cat[22] == None:
            list1_cat[22] = word
            list2.append(22)
        elif pos == 'u' and relation_type == 3 and list1_cat[22] != None:
            list1_cat[62] = word
            list2.append(62)
        elif (pos == 'n' or pos == 'p') and relation_type == 3 and list1_cat[62] != None:
            list1_cat[65] = word
            list2.append(65)
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
        elif pos == 'a' and relation_type == 4 and list1_cat[23] == 'IA':
            list1_cat[26] = word
            relation_type = 4
            list2.append(26)
        elif pos == 'a' and relation_type == 4:
            list1_cat[25] = word
            list2.append(25)
        elif (pos == 'n' or pos == 'p') and relation_type == 4:
            list1_cat[26] = word
            list2.append(26)
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
        elif pos == 'a' and relation_type == 5 and list1_cat[27] == 'IA':
            list1_cat[29] = word
            relation_type = 5
            list2.append(29)
        elif pos == 'a' and relation_type == 5:
            list1_cat[29] = word
            list2.append(29)
        elif (pos == 'n' or pos == 'p') and relation_type == 5:
            list1_cat[30] = word
            list2.append(30)
        elif pos == 'r' and relation_type == 5:
            relation_type = 6
            list1_cat[31] = word
            list2.append(31)
            if snoun != "" and snum == 34:
                list1_cat[34] = snoun
        elif (pos == 'd' or pos == 'q') and relation_type == 6:
            list1_cat[32] = word
            list2.append(32)
        elif pos == 'a' and relation_type == 6:
            list1_cat[33] = word
            list2.append(33)
        elif (pos == 'n' or pos == 'p') and relation_type == 6:
            list1_cat[34] = word
            list2.append(34)
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
            # easygui.msgbox('you did not categorize the word ' + word)
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
    list1_cat[46] = list2
    list1_cat[42] = prp
    list1_cat[0] = osent
    list1_cat[41] = has_plural
    list1_cat[53] = sent_type
    return list1_cat

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

def print_sent_full(test_sent,p,tot_prop_name,words,yy = ""):

    global result_data
    global excel,strt,stp,def_used,words_used

    # p = 30
    bb = 8
    b = time.time()
    p += 2
    definitions2 = words[33]

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
                        bool2 = False
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
            if len(test_sent[i][j]) == 7:
                test_sent[i][j].append("")
            elif len(test_sent[i][j]) == 6:
                test_sent[i][j].append("")
                test_sent[i][j].append("")
            elif len(test_sent[i][j]) == 5:
                test_sent[i][j].append("")
                test_sent[i][j].append("")
                test_sent[i][j].append("")
            # elif len(test_sent[i][j]) == 4:
            #     bb = 7
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
            if excel:
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
            if excel:
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
                    if excel:
                        w4.cell(row=p,column=3).value = "____________________"
                    else:
                        result_data['text_'+str(p)+'_2']="____________________"

                    bool1 = True
                    p += 1
                if excel:
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

                if excel:
                    w4.cell(row=p,column=4).value = str2
                else:
                    result_data['text_'+str(p)+'_3']= str2
                if excel and j+1 == len(tot_prop_sent[o]):
                    w4.cell(row=p,column=5).value = 1

                p += 1
        p += 3
    e = time.time()
    g = e - b
    return



def build_dict(str1):

    global excel
    list1 = []
    list4 = []
    word_type = []
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
    i = 0
    for row in ws:
        i += 1
        if i == 90:
            bb = 8

        if excel:
            s = row[0].value
            str1 = row[2].value
            word = row[3].value
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
        # if "%" in word:
        #     word = str(word)
        if str1 != None:
            if not isinstance(str1,(int,long)):
                str1 = str1.strip()
            if word == 'in' + ub:
                bb = 7
            elif word == 2:
                bb = 7
            str5 = copy.copy(str1)

            if isinstance(word,(int,long)):
                word = str(word)

            word = word.strip()
            definitions2.append([word,i])
            if excel:
                str3 = row[4].value
                defin = row[5].value
            else:
                str3 = row.rel
                defin = row.definition


            if defin == 'redundant':
                redundant.append(word)
            if defin != None and defin.find("E.g.") == -1 and defin.find("EXP") == -1 \
                    and defin != 'redundant' and word != ".":
                if word != None:
                    word = word.strip()
                if str3 != None:
                    str3 = str3.strip()
                if str1 == None:
                    easygui.msgbox("you did not state the part of speech for " + word)
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
                thir_let = copy.copy(str1)
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
                elif sec_let == "j":
                    proper_names.append(word)
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
    # relations.sort()
    # relations2.sort()
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

def findposinlist(str1, list1,i):
    # this function takes a string, matches it to an element in the first dimension
    # of the list, then returns the matching second element

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


def cat_atoms(j,i,list,members,basic_objects,str1,bo2,words,consq,rel,basic_cat):
    # categorize atoms
    global dv_nam,gen_var,cnjts,ind_var
    atomic_relations = words[22]
    subj = list[i][5]
    relat = list[i][9]
    obj = list[i][14]
    sent = list[i][0]
    bool2 = False
    if j == 5:
        x = 14
    elif j == 14:
        x = 5
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
    if subj == "p" and relat == 'IG' and obj == 'z' and j == 5:
        bb = 8

    bool3 = False
    if relat == "IA" and j == 5:
        str6 = findinlist(list[i][14],dv_nam,0,1)
        if str6 in spec_prop:
            bool3 = True
    bool4 = False
    if relat == "IG" and j == 5:
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
    elif (relat == 'IG' or relat == "IA") and obj in gen_var:
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
    if relat == "A" or relat == "AF":
        u = 1

    if j == 5:
        if list[i][14] == None:
            str7 = ""
        elif list[i][14] in gen_var:
            str7 = "@"
        else:
            str7 = list[i][14]
        try:
            members.append([list[i][j],str1,sent,tilde + list[i][9] \
                + str7,u,str5,list[i],list[i][14]])
        except TypeError:
            bb = 8
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


def axioms(list1,bo2,disjuncts,tot_sent,candd,candd2,conditionals,all_sent,prop_sent,\
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
                                done = axioms2(pos1,pos2,rel1,rel2,sub1,obj1,sub2,obj2,osec_sent,tot_sent,used_ax,\
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
                        done = axioms2(pos1,pos2,rel1,rel2,sub1,obj1,sub2,obj2,osec_sent,tot_sent,used_ax,\
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
                                done = axioms2(pos1,pos2,rel1,rel2,sub1,obj1,sub2,obj2,osec_sent,tot_sent,used_ax,\
                                        candd,candd2,conditionals,all_sent,member_prop,not_id,prop_sent)

    if added:
        candd = get_rel_conj(candd,conditionals)
        conditionals5 = copy.deepcopy(conditionals)
        consistent = statement_logic(prop_sent,conditionals5,candd,candd2,disjuncts,0)

        if consistent:
            bb = 8

        return consistent
    else:
        return True

def axioms2(pos1,pos2,rel1,rel2,sub1,obj1,sub2,obj2,osec_sent,tot_sent,used_ax,\
            candd,candd2,conditionals,all_sent,member_prop,not_id,prop_sent):

    global dv_nam,idf_var,sn,cnjts

    rn_list = []
    thing_con = findinlist('thing',dv_nam,1,0)
    if thing_con == None:
        thing_con = idf_var[0]
        for i in range(len(tot_sent)):
            if tot_sent[i][4] == "ID":
                tot_sent[i][2] += " & (" + thing_con + "= thing)"
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
        oax = "(((b" + rel1 + "c) & (dIGe)) " + conditional + \
        " (b~" + rel2 + "d)) & (e=thing)"
        sent3 = "(" + sub1 + "~" + rel2 + thing_int + ")"
        subj4 = sub1
        obj4 = thing_int
        oax_name = "AX." + rel1 + "." + rel2 + "." + "ss"
    elif pos1 == 5 and pos2 == 14:
        thing_var = sub2
        oax = "(((b" + rel1 + "c) & (dIGe)) " + conditional + \
        " (d~" + rel2 + "b)) & (e=thing)"
        sent3 = "(" + thing_int + "~" + rel2 + sub1 + ")"
        subj4 = thing_int
        obj4 = sub1
        oax_name = "AX." + rel1 + "." + rel2 + "." + "so"
    elif pos1 == 14 and pos2 == 5:
        thing_var = obj2
        oax = "(((b" + rel1 + "c) & (dIGe)) " + conditional + \
        " (c~" + rel2 + "d)) & (e=thing)"
        sent3 = "(" + obj1 + "~" + rel2 + thing_int + ")"
        subj4 = obj1
        obj4 = thing_int
        oax_name = "AX." + rel1 + "." + rel2 + "." + "os"
    elif pos1 == 14 and pos2 == 14:
        thing_var = sub2
        oax = "(((b" + rel1 + "c) & (dIGe)) " + conditional + \
        " (d~" + rel2 + "c)) & (e=thing)"
        sent3 = "(" + thing_int + "~" + rel2 + obj1 + ")"
        subj4 = thing_int
        obj4 = obj1
        oax_name = "AX." + rel1 + "." + rel2 + "." + "oo"

    sent1 = "(" + sub1 + rel1 + obj1 + ")"
    sent3a = sent3.replace("~","")
    sent5 = "(" + sub2 + rel2 + obj2 + ")"
    sent2 = "(" + thing_int + "IG" + thing_con + ")"
    nax = "(" + sent1 + " & " + sent2 + ") " + conditional \
        + " " + sent3
    rename = build_sent_list(rn_list)
    ax_enti = "(" + thing_var + "IG" + thing_con + ")"
    subst1 = "(" + thing_var + mini_c + thing_int + ")"
    sent4 = "(" + thing_var + "IG" + thing_con + ")"
    subst4 = sent5 + " " + conditional + " " + sent3a

    sent1p = name_sent(sent1)
    sent2p = name_sent(sent2)
    sent3p = name_sent(sent3)
    sent3ap = name_sent(sent3a)
    sent4p = name_sent(sent4)
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
    list1 = prepare_iff_elim(naxp,list2[0],list2[1],sn,tot_sent)
    list1[37] = nax
    conditionals.append(list1)
    sn += 1
    tot_sent.append([sn,sent4,sent4p,"","AY ENT","","","",""])
    candd.append([sn,sent4p,""])
    prop_sent.append([sn,sent4p,"","","","","","","",""])
    sn += 1
    tot_sent.append([sn,sent2,sent2p,"","AY ENT","","","",""])
    prop_sent.append([sn,sent2p,"","","","","","","",""])
    candd.append([sn,sent2p,""])
    sn += 1
    tot_sent.append([sn,subst1,"","","OS",sn-1,sn-2,"",""])
    sn += 1
    tot_sent.append([sn,subst4,subst4p,"","SUB",sn-1,"","",""])
    prop_sent.append([sn,subst4p,"","","","","","","",""])
    list2 = mainconn(subst4p)
    list1 = prepare_iff_elim(subst4p,list2[0],list2[1],sn,tot_sent)
    list1[37] = subst4
    conditionals.append(list1)
    cnjts.append(sent2p)
    cnjts.append(sent4p)

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
        list3[9] = "IG"
        list3[14] = thing_con
        list3[0] = sent2
        list3[42] = sent2p
        list3[46] = "x"
        all_sent.append(list3)
        list5 = [thing_int,"THING",[],[],[],[],[],"",[],[]]
        member_prop.append(list5)
        list4 = copy.deepcopy(list3)
        list4[5] = thing_var
        list4[0] = sent4
        list4[42] = sent4p
        not_id.append([thing_int,thing_var])
        all_sent.append(list4)
        return False
    else:
        return True






# (d'HWv) & (wIGd')
# ((bHWc) & (dIGe)) > (d~IGb) & (e=thing)
# (b>d) & (c>v) & (d>f) & (e>g)
# (d' HW v) & (fIGe) > (f~IGd'))
# (wIGe)
# (fIGe)
# (wIGe) , (wIGd') , (fIGe)
# (f>g)
# (w=g)
# (f~IGd') > (w~IGd')

def get_sent(all_sent,str1):

    for i in range(len(all_sent)):
        str2 = all_sent[i][42].replace("~","")
        if str1 == str2:
            return i

    easygui.msgbox("the get sent function is wrong")


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
            if all_sent[i][9] == "IG" and all_sent[i][8] != "~" and all_sent[i][5] == subj:
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

    global sn
    global pn
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

def identity(all_sent,tot_sent,basic_objects,words,candd,candd2,conditionals,\
    prop_sent,prop_name,id_num,identities,idf_var,truth_value):

    global sn,psent,impl,definite2,ind_var,gen_var,idf_var2,never_used,simple_id,cnjts,pn,affneg

    irrel_group = []
    embed_var = []
    dummy = remove_duplicates(all_sent,0)
    if identities != []:
        dummy = simple_id(tot_sent,all_sent,identities)
    dv_list = id_sent(dv_nam,all_sent,irrel_group,1,embed_var)
    tot_sent.insert(id_num-1,[id_num,dv_list[0],dv_list[1],"",'ID'])
    disjuncts = []
    negat = []
    sent = []
    qn = 300 # numbers the property sent list
    property_sent = []
    for i in range(len(tot_sent)):
        if tot_sent[i][2] != "":
            sent.append([tot_sent[i][0],tot_sent[i][2]])
            negat.append(tot_sent[i][3])

    consistent = plan(sent,prop_sent,candd,candd2,conditionals, prop_name,disjuncts,tot_sent,2,negat)

    tv = True # tv = truth value
    if consistent and impl != nonseq:
        tv = False
    elif impl == nonseq and consistent:
        tv = False
    if not tv:
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
                    list2 = unenclose(def_info[3][y])
                    str3 = list2[0]
                    d = findposinlist(str3,all_sent,42)
                    all_sent[d][53] = str9

        atomic = words[29]
        members = []
        non_id = []
        used_var = []
        consq = []
        for i in range(len(idf_var2)):
            if idf_var2[i] not in idf_var:
                used_var.append(idf_var2[i])
            else:
                if i > 26:
                    break

        nw = []
        bo2 = []
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
            if j == 33:
                bb = 8
            if all_sent[j][43] == "x":
                all_sent[j][46] = ""
            relat = all_sent[j][9]
            if relat == "IA":
                str6 = findinlist(all_sent[j][14],dv_nam,0,1)
                if str6 in spec_prop:
                    all_sent[j][46] = "x"

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
                            if j == 23 and p == 5:
                                bb = 8
                            rel = ""
                            if relat == "A" or (relat == 'T' and p == 14):
                                kind = 'MOMENT'
                            elif relat == 'I' and p == 5:
                                kind = 'FACT'
                            elif relat == 'AB' or relat == 'LF' or relat == 'AB' or (relat == 'S' and p == 14) \
                                    or (relat == 'WS' and p == 14):
                                kind = 'POINT'
                            elif relat == 'AF' or (relat == 'N' and p == 14):
                                kind = 'NUMBER'
                            elif relat == 'AI' and p == 5 or (relat == 'TK' and p == 14):
                                kind = 'MENTAL RELATIONSHIP'
                                rel = "ir"
                            elif relat == 'AI' and p == 14:
                                kind = 'IMAGINATION'
                            elif relat == "IG" and p == 14:
                                kind = "NOUN CONCEPT"
                            elif relat == "H" and p == 14:
                                kind = "NOUN PROPERTY"
                            elif relat == "IA" and p == 14:
                                kind = "ADJECTIVIAL PROPERTY"
                            elif relat == "HE" and p == 5:
                                kind = "PARTICLE"
                            elif (relat == 'TK' and p == 14) or (relat == 'AI' and p == 5):
                                kind = 'THOUGHT'
                            elif relat == "HE" and p == 14:
                                kind = "ENERGY"
                            elif relat == "HW" and p == 5:
                                kind = "WHOLE"
                            elif relat == 'P' and p == 14:
                                kind = 'POSSIBLE WORLD'
                            elif relat == 'DS' and p == 14:
                                kind = 'POSSIBLE RELATIONSHIP'
                            elif relat == 'AL' or (relat == 'WV' and p == 14):
                                kind = 'LETTER'
                            elif (relat == 'TK' or relat == 'DS') and p == 5:
                                kind = 'MIND'
                            elif relat == "S" and p == 5:
                                kind = 'MATTER'
                            elif relat == "SS" and p == 14:
                                kind = 'SENSORIUM'
                            else:
                                kind = ""
                            if len(members) > 30:
                                bb = 7
                            if all_sent[j][8] == "~":
                                kind = ""
                            dummy = cat_atoms(p,j,all_sent,members,basic_objects,kind,bo2,words,consq,rel,basic_cat)

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
            member_prop = []
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
            consistent = axioms(basic_objects2,bo2,disjuncts,tot_sent,candd,candd2,conditionals,all_sent,\
                           prop_sent,member_prop,not_id)
            # end3
            bb = 9
            # if bb == 10:
            if consistent:
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
                        # elif all_sent[i][46] != "x":
                            all_sent[i][45] = str2
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
                        added = new_cond(pot_id,candd,conditionals,tot_sent,member_prop,\
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
                    # st = time.time()
                    consistent = statement_logic(prop_sent,conditionals,candd,candd2,disjuncts,0)
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


    prop_sent.sort()

    i = -1
    list2 = []
    list1 = []
    list5 = []
    list4 = []
    bool1 = False
    rn_used = False
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

        # for i in range(1,len(list1)):
        #     if list1[i] > start:
        #         break
        #     str1 += " " + str(list1[i])
        # for i in range(len(tot_sent)):
        #     if tot_sent[i][0] in list1:
        #         tot_sent[i][0] = str(tot_sent[i][0]) + " *"

        # tot_sent.insert(insert_here+1,["","relevant sentences: " + str1,"","","","",""])
        # if affneg != []:
        #     str2 = ""
        #     for i in range(len(affneg)):
        #         str1 = affneg[i]
        #         str2 += " " + str1
        #     tot_sent.insert(insert_here+2,["","both affirmed and negated: " + str2,"","","","",""])

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
    tot_prop_sent.append(prop_sent)
    # end5
    list1 = [tot_sent,tv]
    return list1

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
    if d == 18 and e == 6:
        bb = 8

    if (diff_nval and all_sent[d][8] != all_sent[e][8]) or not diff_nval:
        if relat == relat1 and srelat == srelat1 and all_sent[d][0] != all_sent[e][0]:
            subj1 = all_sent[d][5]
            obj1 = all_sent[d][14]
            sobj1 = all_sent[d][18]
            subj = all_sent[e][5]
            obj = all_sent[e][14]
            sobj = all_sent[e][18]
            if subj1 == 'v' and relat == 'IG' and subj == 'u' and relat1 == 'IG':
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

def new_cond(pot_id,candd,conditionals,tot_sent,member_prop,candd2,\
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
            oconditional = res[0]
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
                nsent = copy.copy(osent)
                if g == -1:
                    print "one of your sentences is missing from the all_sent list"
                new_list = []
                for s in range(0,maxm):
                    list9 = copy.deepcopy(all_sent[g])
                    new_list.append(list9)

                for h in range(len(pot_id)):
                    str2 = pot_id[h][1]
                    if str2 in osent:
                        if all_sent[g][9] == "IA" and (all_sent[g][14] == gen or \
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
                        list1 = prepare_iff_elim(str1p,list2[0],list2[1],sn)
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
                            if rel_sent2[s][9] == "IG" and rel_sent2[s][14] == thing_con:
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
        list1[9] = "IG"
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
        easygui.msgbox('you have not coded for three new sentences yet')
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


def name_conditional(list1,nat_logic = True):

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
                elif str1[i-1:i] == "~" and str5 in subscripts:
                    str3 = "~" + str2 + str5
            k = 1
            str3 = str3.strip()
            arr1.append(str3)

    return arr1

def get_prop(str1):

    global subscripts
    arr1 = []
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

            str3 = str3.strip()
            arr1.append(str3)

    return arr1

def prepare_iff_elim(str2, mainc, s, num = "",tot_sent = []):

    global sn
    if str2 == "r " + conditional + " s":
        bb = 8

    list7 = [""] * 39
    if num == "":
        list7[2] = sn + 1
    else:
        list7[2] =  num
    list7[4] = str2
    list7[5] = ""
    list9 = []
    j = 0
    str2 = remove_outer_paren(str2)
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
                else:
                    list7[1] = list6
                    list7[7] = str9

    list7[38] = get_prop(str2)
    if tot_sent != []:
        list7[37] = findinlist(str2,tot_sent,2,1)
    return list7

def islist(list1):

    if list1[1] == '~' or list1[1] == "":
        return False
    else:
        return True

def new_prop(prop_sent, str1, ng, asp, anc1, anc2, anc3 = None, anc4 = None, \
             is_premise = False, num = "",ostring = ""):

    if ng == None:
        ng = ""
    global sn,pn
    global cnjts
    list1 = [None] * 15

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

def many_cond(candd,candd2, conditionals, kind, asp, anc2, f, g, r):

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
        dummy = new_prop_sent("", kind, asp, "",anc2, \
                    conditionals,g,candd,candd2, conditionals[g][8], cjct)
        if dummy == False:
            return False
        else:
            return True
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
                        dummy = new_prop_sent("", kind, asp, "",anc2, \
                                    conditionals,g,candd,candd2, conditionals[g][8], cjct)
                        if dummy == False:
                            return False
                        else:
                            return True
                    else:
                        conditionals[g][8] == None
                        break
                elif str1 == str2 and ng != neg2:
            # the point of having blank returns is because if it returns true
            # then we need to subtract the conditional counter, here g, by 1
                    conditionals[g][8] = ""
                    return ""
    conditionals[g][f] = list1
    conditionals[g][8] = ""
    return ""

def modus_ponens(conditionals, candd,candd2, prop_sent,kind):

    r = -1
    while r < len(candd) -1:
        if conditionals == []:
            return True
        r += 1
        if r == 27:
             bb = 7
        str1 = candd[r][1]
        if str1 == 'l':
            bb = 8
        str8 = candd[r][2]
        anc1 = candd[r][0]
        temp1 = copy.copy(str1)
        temp1 = temp1.replace(" ","")
        temp1 = remove_outer_paren(temp1)
        g = -1
        bool1 = False
        while g < len(conditionals) -1:
            g += 1
            if g == 2 and r==16:
                bb = 7
            if conditionals[g][0] != "":

                str12 = conditionals[g][3]
                if str12 != 'd':
                    anc2 = conditionals[g][2]
                    if conditionals[g][6] == "":
                        aconjunction = ""
                        temp_ant = conditionals[g][0][0]
                        temp_nega = conditionals[g][0][1]
                    else:
                        aconjunction = conditionals[g][6]
                        temp_ant = conditionals[g][0][0][0]
                        temp_nega = conditionals[g][0][0][1]
                    if conditionals[g][7] == "":
                        cconjunction = ""
                        temp_con = conditionals[g][1][0]
                        temp_negc = conditionals[g][1][1]
                    else:
                        cconjunction = conditionals[g][7]
                        temp_con = conditionals[g][1][0][0]
                        temp_negc = conditionals[g][1][0][1]
                    temp_ant = temp_ant.replace(" ","")
                    temp_con = temp_con.replace(" ","")
                    temp_ant = remove_outer_paren(temp_ant)
                    temp_con = remove_outer_paren(temp_con)

                    for f in range(0,2):
                        if f == 0 and temp1 == temp_ant:
                            if str8 == temp_nega:
                                if str12 == 'c':
                                    str13 = "MP"
                                else:
                                    str13 = "EE"
                                if aconjunction != "" :
                                    dummy = many_cond(candd,candd2, conditionals, "con", str13, \
                                                      anc2, f, g, r)
                                    if dummy == False:
                                        return False
                                    elif dummy:
                                        del conditionals[g]
                                        g -= 1
                                        break
                                else:
                     # con indicates that the consequent of the conditional is to be detached
                     #                if len(conditionals) <= 4:
                     #                    bb = 7
                                    dummy = new_prop_sent("", "con", \
                                        str13, anc1, anc2,conditionals,g,candd,candd2)
                                    if dummy == False:
                                        return False
                                    del conditionals[g]
                                    g -= 1
                                    break
                            elif str8 != temp_nega and str12 == 'e':
                                if kind != 2 and cconjunction != "":
                                    dummy = new_prop_sent("~", "con", \
                                                "EN", anc1, anc2, conditionals,g,candd,candd2)
                                    if dummy == False:
                                        return False
                                    del conditionals[g]
                                    g -= 1
                                    break
                        elif f == 1 and temp1 == temp_con:
                            if str8 == temp_negc and str12 == 'e':
                                if cconjunction == "":
                                    dummy = new_prop_sent("", "ant", "EE", \
                                        anc1, anc2, conditionals,g,candd,candd2)
                                    if dummy == False:
                                        return False
                                    del conditionals[g]
                                    g -= 1
                                    break
                                else:
                                    dummy = many_cond(candd,candd2, conditionals, "ant", "EE", \
                                                      anc2, f, g, r)
                                    if dummy == False:
                                        return False
                                    elif dummy:
                                        del conditionals[g]
                                        g -= 1
                                        break
                            elif str8 != temp_negc:
                                if kind != 2 and aconjunction != "":
                                    if str12 == 'c':
                                        str13 = "MT"
                                    else:
                                        str13 = "EN"
                                    dummy = new_prop_sent("~", "ant", \
                                                str13, anc1, anc2, conditionals,g,candd,candd2)
                                    if dummy == False:
                                        return False
                                    del conditionals[g]
                                    g -= 1
                                    break
                        elif f == 0 and temp1 != temp_ant and \
                                aconjunction != "" and str12 == 'e':
                            if kind != 2 and cconjunction != "":
                                s = -1
                                if conditionals != []:
                                    while s < len(conditionals[g][0]) -1:
                                        s += 1
                                        if temp1 == conditionals[g][0][s][0] and \
                                            str8 != conditionals[g][0][s][1]:
                                            dummy = new_prop_sent("~", "con", \
                                            "EN", anc1, anc2, conditionals,g,candd,candd2)
                                            if dummy == False:
                                                return False
                                            del conditionals[g]
                                            g -= 1
                                            break

                        elif f == 1 and temp1 != temp_con and cconjunction != "":
                            if kind != 2 and aconjunction != "":
                                s = -1
                                if conditionals != []:
                                    while s < len(conditionals[g][1]) -1:
                                        s += 1
                                        if temp1 == conditionals[g][1][s][0] and \
                                            str8 != conditionals[g][1][s][1]:
                                            if str12 == 'e':
                                                str13 = "EN"
                                            else:
                                                str13 = "MT"
                                            dummy = new_prop_sent("~", "ant", \
                                            str13, anc1, anc2, conditionals,g,candd,candd2)
                                            if dummy == False:
                                                return False
                                            del conditionals[g]
                                            g -= 1
                                            break



    return True

def disjunction_heirarchy(conditionals, str5,d,new_disj = False):

    global prop_name
    global sn,pn

    if d > len(conditionals)-1:
        return

    str5 = enclose(str5)
    list1 = find_sentences(str5, False)
    mainc = list1[4][0][1]

    for i in range(len(list1[0])):
        list2 = unenclose(list1[0][i])
        list1[0][i] = list2[0]

    list2 = [""] * 39
    n = 7
    if mainc == xorr:
        list2[3] = 'x'
    else:
         list2[3] = 'd'
    if conditionals == [] or new_disj:
        list2[2] = pn
    else:
        try:
            list2[2] = conditionals[d][2]
        except IndexError:
            bb = 8
    list2[5] = ""
    list2[4] = list1[0][0]# fix this
    sentences = []

    for i in range(len(list1[0])):
        if os(list1[0][i]):
            siblings = []
            list3 = [None] * 9
            n += 1
            # str1 = findinlist(list1[0][i],prop_name,1,0)
            str2 = list1[4][i][0][:-1]
            g = findinlist(str2,list1[4],0,1,True)
            parent = list1[0][g]
            if list1[4][g][1] == "&":
                list3[2] = 'c'
            elif list1[4][g][1] == xorr:
                list3[2] = 'x'
            else:
                list3[2] = 'd'
            if len(str2) > 1:
                str3 = list1[4][i][0][:-2]
                g = findinlist(str3,list1[4],0,1,True)
                gparent = list1[0][g]
            else:
                gparent = parent
            list3[1] = list1[4][i][0]
            list3[5] = parent
            list3[6] = gparent
            list3[0] = [list1[0][i], list1[1][i]]
            #fix this
            b = parent.count(xorr)
            c = parent.count(idisj)
            if c > 1 or b > 1:
                list3[7] = 2
            else:
                list3[7] = 1
            sent_num = list1[4][i][0]
            m = len(sent_num)
            for j in range(len(list1[4])):
                if len(list1[4][j][0]) == m and list1[4][j][0][:-1] == str2 \
                    and j != i:
                    siblings.append([list1[0][j],list1[1][j]]) # fix this
            list3[4] = siblings
            list2[n] = list3
            sentences.append(list3[0][0])
            if list3[0][0] not in rel_conj:
                rel_conj.append(list3[0][0])

    if conditionals == [] or new_disj:
        list2[38] = sentences
        conditionals.append(list2)
    else:
        list2[38] = sentences
        conditionals[d] = list2

def proper_spacing(str1):

    str1 = str1.replace(" ","")
    str1 = str1.replace(iff, " " + iff + " ")
    str1 = str1.replace(conditional," " + conditional + " ")
    str1 = str1.replace(idisj," " + idisj + " ")
    str1 = str1.replace(xorr," " + xorr + " ")
    str1 = str1.replace("&"," & ")
    return str1

def iff_elim(prop_sent, conditionals,kind):

    new_sent = False
    no_contr = True
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
                    no_contr = new_prop(prop_sent, str3, ng, str7, anc1, None, None, None)

                    if not no_contr:
                        return False
                    conditionals[d][2] = pn+1
                    conditionals[d][0] = [str1, ng1]
                    conditionals[d][1] = [str4, ng4]
                    no_contr = new_prop(prop_sent,str5,"","&E",g,"")
                    if not no_contr:
                        return False
                    list1[2] = pn + 1
                    no_contr = new_prop(prop_sent,str6,"","&E",g,"")
                    if not no_contr:
                        return False
                    conditionals[d][4] = str5
                    list1[4] = str6
                    conditionals.append(list1)
                else:
                    str3 = "(" + str5 + ") & (" + str6 + ")"
                    no_contr = new_prop(prop_sent,str3,"~",iff + "E",g,"")
                    if not no_contr:
                        return False
                    conditionals[d][3] = 'd'
                    conditionals[d][4] = str3
            elif new_sent:
                no_contr = new_prop(prop_sent,conditionals[d][4],"",iff + "E",anc1,"")
                if not no_contr:
                    return False
    return True

def material_implication(prop_sent, conditionals,kind):

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
                                easygui.msgbox("in the material implication function \
                                you are caught in an infinite loop")
                                return
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
                no_contr = new_prop(prop_sent, str1, ng, conditional + "E", anc1,"")
                if not no_contr:
                    return False
                if str1.find("~~") > -1:
                    str1 = str1.replace("~~","")
                    g = copy.copy(pn)
                    no_contr = new_prop(prop_sent,str1, ng, "~~E", g,"")
                    if not no_contr:
                        return False
                conditionals[d][2] = pn
                conditionals[d][4] = str1
                conditionals[d][3] = "d"
                conditionals[d][5] = ng

    return True

            # search for double negatives

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
    list1 = find_sentences(str1, False)
    for i in range(len(list1[3])):
        list2 = unenclose(list1[3][i])
        list1[3][i] = list2[0]
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

def demorgan(prop_sent, conditionals, candd,candd2,kind,one_sent = False, str8 = "",anc1a = "",rule = "",conjt = []):

    d = -1
    temp_bool = True
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
                    easygui.msgbox("you are caught in an infinite loop in the \
                    demorgan function")
                    return
                bool2 = False
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
                            easygui.msgbox("you are caught in an infinite loop in the \
                            demorgan function")
                            return
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
            no_contr = new_prop(prop_sent,str1,"","~(E",anc1,"")
            if not no_contr:
                return False
            if str1.find("~~") > -1:
                str1 = str2
                anc1 = copy.copy(pn)
                no_contr = new_prop(prop_sent,str2,"","~~E",anc1,"")
                if not no_contr:
                    return False
            list2 = mainconn(str1)

            if list2[0] == "&":
                if not one_sent:
                    del conditionals[d]
                list3 = get_conjuncts(str1,True)
                anc1 = copy.copy(pn)
                for i in range(len(list3)):
                    list4 = tilde_removal2(list3[i])
                    no_contr = new_prop(prop_sent,list4[0],list4[1],"&E",anc1,"")
                    if not no_contr:
                        return False
                    list2 = mainconn(list3[i])
                    if list2[0] == idisj or list2[0] == xorr:
                        # add in more nones if it turns out that I need them
                        if one_sent:
                            dummy = disjunction_heirarchy(conditionals,str1,0)
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
                    dummy = disjunction_heirarchy(conditionals,str1,0,True)
                    return
                else:
                    #dummy = disjunction_heirarchy(conditionals,str1,0,True)
                    conditionals[d][2] = pn
                    conditionals[d][4] = str1
    return True

def unenclose(str1):

    i = -1
    global subscripts
    list1 = []
    while i < len(str1)-1:
        i += 1
        str2 = str1[i:i+1]
        str3 = str1[i-1:i]
        str4 = str1[i+1:i+2]
        if str2.islower() and str3 != "~" and str4 not in subscripts:
            str1 = str1[:i-1] + str2 + str1[i+2:]
            list1.append(str2)
        elif str2.islower() and str3 == "~" and str4 not in subscripts:
            str1 = str1[:i-2] + str3 + str2 + str1[i+2:]
            list1.append(str2)
        if str2.islower() and str3 != "~" and str4 in subscripts:
            str1 = str1[:i-1] + str2 + str4 + str1[i+3:]
            list1.append(str2 + str4)
        elif str2.islower() and str3 == "~" and str4 in subscripts:
            str1 = str1[:i-2] + str3 + str2 + str4 + str1[i+3:]
            list1.append(str2 + str4)
    return [str1,list1]

def new_disjunct(str1, ng, n, prop_sent, conditionals, candd,candd2,conjt, anc1, anc2, \
            anc3 = None, anc4=None, kind = 0, rule = ""):

    global sn,pn
    list2 = mainconn(str1)
    if kind == 1:
        del conditionals[n]
        dummy = new_prop(prop_sent, str1, ng, "&I", \
            anc1, anc2, anc3, anc4)
        return dummy
    elif kind == 2:
        dummy = new_prop(prop_sent, str1, ng, "&I", \
            anc1, anc2, anc3, anc4)
        return dummy
    else:
        if os(str1):
            del conditionals[n]
            str1 = remove_outer_paren(str1)
            list1 = tilde_removal2(str1)
            str1 = list1[0]
            dummy = new_prop(prop_sent, str1, list1[1], rule + "E", \
            anc1, anc2)
            candd.append([pn,list1[0],list1[1]])
            conjt.append([pn,list1[0],list1[1]])
            return dummy
        elif list2[0] == "&":
            del conditionals[n]
            str1 = remove_outer_paren(str1)
            dummy = new_prop(prop_sent, str1, ng, rule + "E", \
            anc1, anc2)
            g = copy.copy(pn)
            list3 = get_conjuncts(str1)
            for i in range(len(list3)):
                list4 = tilde_removal2(list3[i])
                dummy = new_prop(prop_sent, list4[0], list4[1], "&E", g,"")
                if dummy == False:
                    return dummy
                if list3[i].find(idisj) > -1:
                    dummy = disjunction_heirarchy(conditionals, list4[0],n, True)
                else:
                    candd.append([pn,list4[0],list4[1]])
                    conjt.append([pn,list4[0],list4[1]])
            return True
        else:
            dummy = new_prop(prop_sent, str1, ng, idisj + "E", \
            anc1, anc2)
            if dummy == False:
                return dummy
            if ng == "~":
                str1 = ng + str1
            else:
                str1 = remove_outer_paren(str1)
            dummy = disjunction_heirarchy(conditionals, str1,n, False)
            conditionals[n][2] = pn
            return True

def xorr_elim(conditionals,n,i,parent,grandparent,whole_d,candd,candd2,conjt,\
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
                consistent = xorr_elim2(str9,prop_sent,conditionals,candd,candd2,anc1,anc2)
                if consistent == False:
                    return consistent
            else:
                list4 = tilde_removal(str9)
                consistent = new_prop(prop_sent, list4[0],list4[1], xorr + "E", \
                anc1, anc2)
                if consistent == False:
                    return consistent
        else:
            str9 = "(" + str9 + ")"
            if kind == 0:
                str9 = grandparent.replace(parent,str9)
                str9 = whole_d.replace(grandparent, str9)
                str9 = bad_paren(str9)
                dummy = new_prop(prop_sent,str9,"",xorr + "E",anc1,anc2)
                if str9.find("~~") > -1:
                    str9 = str9.replace("~~","")
                    dummy = new_prop(prop_sent,str9,"","~~E",pn,"")

            else:
                str9 = whole_d.replace(grandparent,str9)
                str9 = bad_paren(str9)
                dummy = new_prop(prop_sent,str9,"",xorr + "E",anc1,anc2)
                g = copy.copy(pn)
                if str9.find("~~") > -1:
                    str9 = str9.replace("~~","")
                    consistent = new_prop(prop_sent,str9,"","~~E",g,"")
                    if consistent == False:
                        return consistent
                dummy = disjunction_heirarchy(conditionals, str9,n, True)
                del conditionals[n]
            if de_mor:
                consistent = demorgan(prop_sent,conditionals,candd,candd2,conjt,"",True,str9,pn,xorr +"E")
                if consistent == False:
                    return consistent
            else:
                if str9.find(idisj) > -1 or str9.find(xorr) > -1:
                    dummy = disjunction_heirarchy(conditionals,str9,n,True)
                consistent = True
    else:
        #this does not account for the case where the parent == grandparent but
        # grandparent does not == whole d
        consistent = xorr_elim2(str9,prop_sent,conditionals,candd,candd2,conjt,anc1,anc2)

    return consistent

def xorr_elim2(str9,prop_sent,conditionals,candd,candd2,conjt,anc1,anc2):

    str9 = bad_paren(str9)
    consistent = new_prop(prop_sent, str9, "", xorr + "E", \
    anc1, anc2)
    if consistent == False:
        return False
    if str9.find("~~") > -1:
        str9 = str9.replace("~~","")
        dummy = new_prop(prop_sent,str9,"","~~E",pn,"")
        if dummy == False:
            return dummy
    list3 = get_conjuncts(str9)
    g = copy.copy(pn)
    for b in range(len(list3)):
        list4 = tilde_removal2(list3[b])
        list4[0] = remove_outer_paren(list4[0])
        dummy = new_prop(prop_sent, list4[0], list4[1], "&E", g,"")
        if dummy == False:
            return dummy
        if not os(list3[b]):
            if list4[1] == "~":
                consistent = demorgan(prop_sent,conditionals,\
                candd,candd2,"",True,list3[b],pn,"&E",conjt)
                if consistent == False:
                    return False
            else:
                dummy = disjunction_heirarchy(conditionals, list4[0],n, True)
        else:
            candd.append([pn,list4[0],list4[1]])
            conjt.append([pn,list4[0],list4[1]])
    return True

def disjunction_elimination(prop_sent, conditionals, candd,candd2, kind = ""):

    bool1 = False
    bool2 = False
    global sn,pn
    global rel_conj

    for i in range(len(conditionals)):
        if conditionals[i][8] == "":
            dummy = disjunction_heirarchy(conditionals, conditionals[i][4],i)
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
                if conj not in conditionals[n][38]:
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
                                dummy = disjunction_heirarchy(conditionals, str8,n)
                            bool1 = True
                            n = -1
                            break

                        elif str2 == str4 and str5 == "x":

                            consistent = xorr_elim(conditionals,n,i,parent,grandparent,whole_d,candd,candd2,\
                                        conjt,prop_sent,anc1,anc2)
                            if consistent == False:
                                return False
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
                                                        new_prop(prop_sent,str3,"","&I",anc1,anc3,anc4)
                                                        consistent = xorr_elim(conditionals,n,i,parent,\
                                                        grandparent,whole_d,candd,candd2,conjt,prop_sent,pn,anc2,1)
                                                        if consistent == False:
                                                            return False
                                                    else:
                                            # if the conjunct is not embedded within another conjunct
                                            # then the disjunct is simply deleted
                                                        if whole_d == grandparent:
                                                            dummy = new_disjunct(str3,"",n, prop_sent,\
                                                            conditionals,candd,candd2,conjt, anc1, anc3, anc4, anc5, 1)
                                                        else:
                                                            str8 = whole_d.replace(grandparent, parent2)
                                                            if str8.find("(") > -1 and str8.find(idisj) > -1:
                                                                str8 = bad_paren(str8)
                                                            dummy = new_disjunct(str3,"",n, prop_sent,\
                                                            conditionals,candd,candd2,conjt, anc1, "", anc3, anc4, 2)
                                                            dummy = new_disjunct(str8,"",n, prop_sent,\
                                                            conditionals,candd,candd2,conjt, pn-1, anc2)
                                                            if dummy == False:
                                                                return False
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
                                                dummy = new_disjunct(str8,"",n, prop_sent,\
                                                        conditionals,candd,candd2,conjt, anc1, anc2,None,None,0,rule)
                                                if dummy == False:
                                                    return False
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
                            dummy = new_disjunct(str8,"",n,prop_sent, conditionals, candd,candd2,conjt,anc1, anc2, None, None,0,rule)
                            if dummy == False:
                                return False
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
                                dummy = new_disjunct(str8,"",n,prop_sent,conditionals,\
                                    candd,candd2,conjt, anc1,anc2,None,None,0,rule)
                                if dummy == False:
                                    return False
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
                                dummy = new_disjunct(str8,"",n,prop_sent,conditionals,\
                                    candd,candd2,conjt, anc1,anc2,None,None,0,rule)
                                if dummy == False:
                                    return False
                                bool1 = True
                                n = -1
                                break
    return True

def extract_list(list1,d):

    list2 = []
    for i in range(len(list1)):
        list2.append(list1[i][d])
    return list2

def statement_logic(prop_sent, conditionals, candd,candd2, disjuncts,kind="", conc="", impl=""):

    global time1
    b = time.time()
    consistent = modus_ponens(conditionals, candd,candd2, prop_sent,kind)
    e = time.time()
    f = e - b
    time1 += f
    if consistent == False:
        return False
    if kind != 2:
        consistent = iff_elim(prop_sent,conditionals,kind)
        if consistent == False:
            return False
        consistent = material_implication(prop_sent, conditionals,kind)
        if consistent == False:
            return False
        consistent = demorgan(prop_sent, conditionals, candd,candd2,kind)
        if consistent == False:
            return False
        consistent = disjunction_elimination(prop_sent,conditionals,candd,candd2,kind)
        if consistent == False:
            return False
        if kind == 1:
            dummy = finddisj(conditionals,disjuncts)
    c = time.time()
    d = c - b
    return True

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

def new_prop_sent(ng, kind, asp, anc1, anc2, conditionals,g,candd,candd2,list3 =[], cjct = ""):

    global prop_sent
    global sn,pn
    global impl

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
            dummy = new_prop(prop_sent,str1,"","~~E",g, None)
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
            dummy = new_prop(prop_sent,str1,ng,asp,anc1, anc2)
            if dummy == False:
                return False

        candd.append([pn, str1, ng])
        if (list2[0] == iff or list2[0] == conditional) and ng != "~":
            list3 = prepare_iff_elim(str1, list2[0],list2[1],pn)
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
            dummy = new_prop(prop_sent, str1, ng, asp, anc1, anc2)
            if dummy == False:
                return False
        else:
            list1 = conditionals[g][h]
            str1 = remove_outer_paren(str1)
            dummy = new_prop(prop_sent, str1, ng, asp, anc1, anc2)
            if dummy == False:
                return False
            anc1 = copy.copy(pn)
            for i in range(len(list1)):
                list2 = mainconn(list1[i][0])
                dummy = new_prop(prop_sent, list1[i][0], list1[i][1], "&E", anc1, "")
                if dummy == False:
                    return False
                candd.append([pn, list1[i][0], list1[i][1]])
                if (list2[0] == conditional or list2[0] == iff) and list1[i][1] != "~":
                    list4 = prepare_iff_elim(list1[i][0], list2[0],list2[1],pn)
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

def plan(sent, prop_sent, candd,candd2, conditionals, prop_name, disjuncts,tot_sent, kind = '',negat=[]):

    global conc
    global sn
    global rel_conj
    conj_elim = []
    temp_conditionals = []
    list4 = []
    str3 = ""
    str1 = ""
    conc = ""
    impl = ""
    qq = 0
    nat_logic = False
    # if the first sentence is just one letter then we're using statement logic
    # if sent[0][1].find("(") > -1:
    #     for j in range(len(sent[0][1])):
    #         str2 = sent[0][1][j:j+1]
    #         str3 = sent[0][1][j+1:j+2]
    #         if (str2.islower() or str2.isupper()) and (str3.islower() or str3.isupper()):
    #             nat_logic = True
    #         if j > 8:
    #             break


    for i in range(len(sent)):
        if i == 18:
            bb = 7
        g = sent[i].count('(')
        h = sent[i].count(')')
        if g != h:
            easygui.msgbox('wrong number of parentheses in sentence:' + sent[i])
            return "stop"
        if nat_logic == False:
            sent[i][1] = enclose(sent[i][1])
        if sent[i][1].find("!") > -1:
            qq += 1
        else:
            if sent[i][1].count("(") != sent[i][1].count(")"):
                easygui.msgbox("line " + str(sent[i][0]) + " does not have the right number \
                                             of parentheses" )
            if nat_logic == False:
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
                if nat_logic:
                    list3[0] = simple_sent_name(list3[0],list4[0])
                candd.append([sent[i][0], str2, ng])
            else:
                list1 = find_sentences(ostring, True)
                if not nat_logic:
                    list6 = unenclose(list1[0][0])
                    sent[i][1] = list6[0]
                else:
                    list6 = name_conditional(list1,nat_logic)
                    list6[0] = proper_spacing(list6[0])
                str2 = list6[0]
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
                    str3 = ""
                    if list1[4][0][1] != idisj and ng == "" and list1[4][0][1] != xorr:
                        list7 = prepare_iff_elim(str2, list2[0], list2[1],sent[i][0],tot_sent)
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
                    list3 = get_conjuncts(list6[0])
                    for j in range(len(list3)):
                        list5 = tilde_removal2(list3[j])
                        if os(list3[j]):
                            conj_elim.append([sent[i][0],list5[0],list5[1]])
                        else:
                            temp_conditionals.append([sent[i][0], list5[0],list5[1]])

            no_contr = new_prop(prop_sent,str2,ng,"",None,None,None,None,True,sent[i][0],ostring)
            if not no_contr:
                return False

    if conj_elim != []:
        for i in range(len(conj_elim)):
            no_contr = new_prop(prop_sent,conj_elim[i][1],conj_elim[i][2],"&E",\
                        conj_elim[i][0],None)
            if not no_contr:
                return False
            candd.append([pn, conj_elim[i][1], conj_elim[i][2]])

    if temp_conditionals != []:
        for i in range(len(temp_conditionals)):
            if nat_logic:
                list1 = find_sentences(temp_conditionals[i][1], True)
                list6 = name_conditional(list1)
                str2 = list6[0]
            else:
                str2 = temp_conditionals[i][1]
            ng = temp_conditionals[i][2]
            list2 = mainconn(str2)

            if list2[0] != idisj and ng == "" and list2[0] != "&" and list2[0] != xorr:
                list7 = prepare_iff_elim(str2, list2[0], list2[1],pn+1,tot_sent)
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
            no_contr = new_prop(prop_sent, str2,ng,"&E",temp_conditionals[i][0], None)
            if not no_contr:
                return False

    consistent = statement_logic(prop_sent, conditionals, candd,candd2,disjuncts,kind,conc,impl)
    return consistent


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

def repeat_relations(str1):
    #this is for those definitions in which the same relation is related to two different
    #general variables
    a = ["group","x"]
    b = ["member",'z']
    c = ["no"+us,"y"]
    d = ['no',"y"]
    e = ['any',"y"]
    f = ['personhood','y']

    final_list = [a,b,c,d,e,f]
    return final_list

def get_result(post_data,archive_id=None,request=None):
    global ws,w4, result_data,p
    p = 1
    if not excel:
        if archive_id:
            ws = Define3.objects.filter(archives_id=archive_id)
        else:
            archive = Archives.objects.latest('archives_date')
            ws = Define3.objects.filter(archives_id=archive.id)


    if not excel and not mysql: #rajive fix mysql here
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
    global ant_cond,conditionals,candd,rel_conj,conc,prop_sent,sn,impl,denied
    global tagged_nouns,tagged_nouns2,dv_nam,basic_objects,idf_var,p,affirmed
    global gen_var,definite2,cnjts,test_one,stp,strt,candd2,pn,embed,affneg

    list1 = populate_sentences(p)
    test_sent = list1[0]
    p = list1[1]
    words = build_dict('hey') # rajiv
    st = time.time()
    rep_rel = repeat_relations('hey')

    if stp == 0:
        stp = len(test_sent)
#rajiv - use these numbers for the progress bar
    if not excel:
        views.progressbar_send(request,0,100,0,1)
    for k in range(strt,stp):
        if not excel:
            views.progressbar_send(request,strt,stp,k,1)
        if k == 37:
            bb = 7
        st1 = time.time()
        prop_name = []
        tot_sent = []
        all_sent = []
        never_used = []
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
        affirmed = []
        denied = []
        candd = []
        cnjts = []
        ind_var = []
        rel_conj = []
        conc = []
        psent = []
        identities = []
        prop_sent = []
        tagged_nouns = []
        tagged_nouns2 = []
        dv_nam = []
        basic_objects = []
        def_atoms = []
        prop_var = copy.deepcopy(prop_var4)
        idf_var = copy.deepcopy(idf_var2)
        id_num = test_sent[k][-1][0] + 1
        sn = id_num
        dummy = divide_sent(words, test_sent[k], idf_var,tot_sent,all_sent)
        dummy = syn(tot_sent, all_sent, words,def_atoms)
        dummy = rel_repl(all_sent,tot_sent,words,dv_nam,idf_var,id_num)
        dummy = word_sub(idf_var,dv_nam, tot_sent, all_sent,words,id_num)
        dummy = plurals(tot_sent,all_sent,words,dv_nam, idf_var)
        dummy = define(tot_sent, all_sent,idf_var, dv_nam, words,rep_rel,identities,def_atoms)
        list2 = identity(all_sent,tot_sent,basic_objects,words,candd,candd2,\
                 conditionals,prop_sent,prop_name,id_num,identities,idf_var,test_sent[k][0][3])
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
    g = (en-st)/(k+1)
    print "average " + str("{0:.2f}".format(g))
    # print "modus ponens" + str(time1/(k+1))
    dummy = print_sent_full(test_sent,p,tot_prop_name,words,yy)
    if not excel:
        views.progressbar_send(request,0,100,100,2)
    if excel:
        pass #Saved at last
    elif mysql:

        views.save_result(result_data)
    else:
        return result_data
if excel:
    dummy = get_result('hey')
    # st = time.time()
    #wb4.save('../inference engine.xlsx')
    # wb5.save('dictionary new 2.xlsx')
    # en = time.time()
    # print en-st
elif mysql:
    dummy = get_result('hey')

tot_tim2 = time.time()
g = tot_tim2 - tot_tim
print "total " + str("{0:.1f}".format(g))

