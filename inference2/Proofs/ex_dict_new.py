def large_dict(str1):
    dict2= [['rbt','above','AB','((bIc) x^ (dABb)) & ((bIc) x^ (bABe)) & (c=point)'],\
['rbt','after|l','AL','((bIc) x^ (dALb)) & ((bIc) x^ (bALe)) & (c=letter)'],\
['rbt','after|n ','G','((bIc) x^ (dGb)) & ((bIc) x^ (bGe)) & (c=number)'],\
['rbt','after ','A','((bIc) x^ (dAb)) & ((bIc) x^ (bAe)) & (c=moment)'],\
['rbi','and','&','((p&q) t^ (p.qIb)) & (q~Ic) & (rPd) & (b=relationship) & (qb^p&~p) & (c=reality|t) & (rb^p&~q)'],\
['rbi','are|a','J','((bJc) x^ (cId)) & ((bJc) t^ (bIe)) & ((bJc) t^ (cIf)) & (d=property) & (e=thing) & (f=adjective)'],\
['rbi','are|g ','I','((bIc) x^ (cId)) & ((eIf) x^ (eIg)) & (d=concept|n) & (g=instance)'],\
['rbis','at','S','((bIc) x^ (dSb)) & ((dIf) x^ (dSb)) & (c=point) & (f=particle) '],\
['rbi','at|i ','M','((dMb) t^ (dIc)) & ((bIf) x^ (dMb)) & (c=relationship) & (f=imagination) '],\
['rbi','at|n ','N','((bIc) x^ (dNb)) & ((eIf) x^ ((eNh) & (hGg))) & ((jIk) x^ (mNg)) & ((nIo) x^ (nNp)) & (f=whole) & (c=number) & (g=1) & (k=individual) & (p=0) & (o=contradiction) '],\
['rbi','at|p ','P','((dPb) t^ (dIc)) & ((bIf) x^ (dPb)) & (c=relationship) & (f=possible world) '],\
['rbi','at|s ','O','((bIc) x^ (dOb)) & ((dIc) x^ (dOb)) & (f=sensation) & (c=point|s) '],\
['rbit','at|t ','T','((dTb) t^ (dIc)) & ((bIf) x^ (dTb)) & (c=relationship) & (f=moment) '],\
['rbi','at|y','Z','((bIc) x^ (dZb)) & (c=point|a)'],\
['rbi','desire','D','((dDb) t^ ((bIc) & (bJe))) & ((bIf) x^ (dDb)) & (c=relationship) & (f=mind) & (e=open|r)'],\
['r','have','H','((bHc) x^ (cId)) & ((bHc) t^ (bIe)) & ((bHc) t^ (cIf)) & (d=property|n) & (e=thing) & (f=noun)'],\
['rbi','has|w ','W','((bIc) x^ (bWd)) & ((dIe) x^ (bWd)) & (d=whole) & (e=part)'],\
['rbi','in|o','I','((c=reality|t) x^ (pIRc)) & ((dIe) t^ (d~Ic)) & ((c=reality|t) t^ (cIf)) & ((qIRc) x^ (cWq)) &  (e=thing) & (f=non_relationship) & (g=relationship)'],\
['rbts','in front of','F','((bIc) x^ (dFb)) & ((bIc) x^ (bFe)) & (c=point)'],\
['rbi','is|v','IV','((bIVc) x^ (bId)) & ((bIVc) x^ (cIf)) & ((bIVc) t^ (bIe)) & (d=property|v) & (f=adverb) & (e=non_whole)'],\
['rbi','is|y','IY','((bIYc) x^ (cId)) & ((bIYc) x^ (cIf)) & ((bIYc) t^ (bIe)) & (d=property|d) & (f=determinative) & (e=non_whole)'],\
['rbts','left of','L','((bIc) x^ (dLb)) & ((bIc) x^ (bLe)) & (c=point)'],\
['rbi','think about','TK','((bTKd) t^ (dIc)) & ((bIf) x^ (bTKd)) & (c=relationship) & (f=mind) '],\
['n','concept|n',None,'(c=concept|n) & ((bIc) x^ (zIb)) & ((bIc) t^ (bIe)) & (e=non_whole)'],\
['a','consistent',None,'(c=consistent) & ((pJc) k^ (pPq)) & ((pJc) t^ (pId)) & (d=relationship)'],\
['a','contradictory',None,'(c=contradictory) & ((pJc) e^ ((nId) & (p~Pn))) & (d=possible world) & ((pJc) t^ (pId)) & (d=relationship)'],\
['aa','extant',None,'((bJc) t^ (cId)) & (d=property)'],\
['n','fact',None,'(c=fact) & ((bIc) x^ (bIRd)) & ((bIc) t^ (bIe)) & (((hAg) & (bIc)) t^ (b~IRd Th)) & (d=reality) & (e=relationship) & (g=now)'],\
['na','here',None,'(b=here) t^ (cSb)'],\
['n','imagination',None,'(c=imagination) & ((bIc) x^ (dMb)) & ((bIc) t^ (bIf)) & (f=non_relationship)'],\
['n','instance',None,'(c=instance) & ((bIc) x^ (bId))'],\
['n','integer',None,'(c=integer) & ((bIc) x^ (bGd)) & ((bIc) x^ (eGb)) & ((bIc) x^ (fNb)) & ((bIc) t^ (bIg)) & (g=non_whole)'],\
['n','letter',None,'(c=letter) & ((bIc) x^ ((dPe) & (jPg))) & ((bIc) t^ (bIm)) & (hIc) & (db^bALh) & (jb^(kIc) t^ (k~ALb)) & (m=non_whole)'],\
['n','mind',None,'(c=mind) & ((bIc) t^ (bTKz))'],\
['n','mind|a',None,'(c=mind) & ((bIc) x^ (bTKh)) & ((bIc) x^ (bDt)) & ((bIc) t^ (bIj)) & (((bTKr) & (rCRRq) & (sWb) & (qPh) & (To)) t^ ((qPe) & (nt+qPf) & (Tg) & (gAo))) & (j=non_whole) & (rb^sRt INSm) & (qb^sQu INSm)'],\
['n','moment',None,'(c=moment) & ((bIc) x^ (dTb)) & ((bIc) x^ (bAh)) & ((bIc) x^ (eAb)) & ((bIc) t^ (bIf)) & (f=non_whole)'],\
['na','now',None,'(b=now) t^ (cSb)'],\
['n','part',None,'(c=part) & ((bIc) x^ (dWb))'],\
['n','part|p',None,'(c=part|p) & (((bIc) & (bOFd)) x^ (dWb))'],\
['n','particle',None,'(c=particle) & ((bIc) x^ (bSd)) & ((bId) x^ (hTg)) & ((bIc) t^ (bIf)) & (f=non_whole) & (g=now) & (hb^bSd)'],\
['n','particle|m',None,'(c=particle|m) & ((bIc) x^ (bOd)) & ((bId) x^ (hTg)) & ((bIc) t^ (bIf)) & (f=non_whole) & (g=now) & (hb^bOd)'],\
['n','point',None,'(c=point) & ((bIc) x^ (dSb)) & ((bIc) x^ (eABb)) & ((bIc) x^ (bABm)) & ((bIc) x^ (fFb)) & ((bIc) x^ (bFj)) & ((bIc) x^ (gLb)) & ((bIc) x^ (bLk)) & ((bIc) t^ (bIh)) & (h=non_whole)'],\
['n','point|s',None,'(c=point|s) & ((bIc) x^ (dOb)) & ((bIc) t^ (bIe)) & (e=non_whole)'],\
['n','point|b',None,'(c=point|b) & ((bIc) x^ (dZb)) & ((bIc) x^ (eABb)) & ((bIc) x^ (bABm)) & ((bIc) x^ (gLb)) & ((bIc) x^ (bLk)) & ((bIc) t^ (bIh)) & (h=non_whole)'],\
['n','possible relationship',None,'(c=possible relationship) & ((pIc) x^ (pPb))'],\
['n','possible world',None,'(c=possible world) & ((bIc) x^ (pPb))'],\
['n','property',None,'(c=property) & ((bIc) x^ (dJb)) & ((bIc) t^ (bIe)) & (e=non_whole)'],\
['n','property|d',None,'(c=property|d) & ((bIc) x^ (dIYb)) & ((bIc) t^ (bIe)) & (e=non_whole)'],\
['n','property|n',None,'(c=property|n) & ((bIc) x^ (dHb)) & ((bIc) t^ (bIe)) & (e=non_whole)'],\
['n','property|v',None,'(c=property|v) & ((bIc) x^ (dIVb)) & ((bIc) t^ (bIe)) & (e=non_whole)'],\
['n','reality|t',None,'((c=reality|t) x^ (pIRc)) & ((dIe) t^ (d~Ic)) & ((c=reality|t) t^ ((cIf) & (cIg))) & ((qIRc) t^ (cWq)) &  (e=thing) & (f=non_relationship) & (g=relationship)'],\
['n','sensation',None,'(c=sensation) & ((bIc) x^ (bOd)) & ((bIc) t^ (bIe)) & (e=non_whole)'],\
['n','sensorium',None,'(c=sensorium) & ((bIc) x^ ((bWd) x^ (eOd)))'],\
['na','thing',None,'See atomic categories'],\
['n','thought',None,'(c=thought) & ((bIc) x^ (dTKb)) & ((bIc) t^ (bIe)) & ((bIc) x^ (bMf)) & (e=relationship)'],\
['n','whole',None,'(c=whole) & ((bIc) x^ (bWd))'],\
['na','abbreviation',None,'(c=abbreviation) & ((bIc) x^ ((bId) ed^ (bIe))) & (d=constant) & (e=variable)'],\
['na','adjective',None,'(wildly disjunctive)'],\
['na','constant',None,'indefinable'],\
['na','intransitive verb',None,'(wildly disjunctive)'],\
['na','noun',None,'indefinable'],\
['na','noun form',None,'indefinable'],\
['na','plural form',None,'indefinable'],\
['','non_spatio_temporal',None,'(wildly disjunctive)'],\
['','spatio_temporal',None,'(wildly disjunctive)'],\
['','active',None,'(wildly disjunctive)'],\
['','passive',None,'(wildly disjunctive)'],\
['na','relation',None,'(c=relation) & ((bIc) t^ (bId)) & (d=non_whole)'],\
['rai','relational variable','R','indefinable'],\
['na','relatum',None,'(c=relatum) & ((bIc) x^ (bRd)) & ((eIc) x^ (fRe))'],\
['a','root (word)',None,'(wildly disjunctive), (c=root) & ((bJc) t^ (bId)) & (d=word)'],\
['na','singular form',None,'(wildly disjunctive)'],\
['na','subject',None,'hard coded - the first relatum is the subject'],\
['na','subject|i',None,'indefinable (must occur in if the relation is an intransitive verb)'],\
['na','variable',None,'indefinable'],\
['na','verb form',None,'(wildly disjunctive)'],\
['a','actual|p',None,'(c=actual|p) & (d=reality) & ((pJc) x^ (pIRd))'],\
['a','actual|w',None,'(c=actual|w) & ((bJc) x^ (b=reality))'],\
['ns','set',None,'(set = whole)'],\
['rs','aware of',None,'(aware of=TK)'],\
['rs','belong|g ',None,'(belong|g=I)'],\
['r','belong to','BLN','(bBLNc) x^ (cWb)'],\
['ns','body ',None,'(body=particle)'],\
['ns','category|c ',None,'(category|c=concept|n)'],\
['ns','attribute',None,'(attribute = property)'],\
['ns','characteristic ',None,'(characteristic=property)'],\
['ns','class',None,'(class = concept|n)'],\
['ns','class|w',None,'(class|w = whole)'],\
['ns','class concept',None,'(class concept=concept|n)'],\
['ns','agglomeration',None,'(agglomeration = whole)'],\
['ns','concept|a',None,'(concept|a = property)'],\
['ns','condition',None,'(condition=property)'],\
['rs','conscious of',None,'(conscious of=TK)'],\
['n','consciousness',None,'(consciousness=mind)'],\
['aa','consistent',None,'(b=consistent) & ((cJb) x^ (cPd))'],\
['r','exist','EX','(exist=EX) & ((bEX) x^ (bJc)) & (c=extant)'],\
['ns','feature ',None,'(feature=property)'],\
['ns','group',None,'(group = whole)'],\
['ns','group|c',None,'(group|c = concept|n)'],\
['rs','instantiate',None,'(instantiate=I)'],\
['r','instantiated by','INSP','(instantiated by=INSP) & ((bINSPc) x^ (cIb))'],\
['ns','item',None,'(item=thing)'],\
['a','material',None,'(c=material) & (d=particle) & ((bJc) x^ (bId))'],\
['a','material|m',None,'(z=material|m) & (((bJz) & (cIb)) x^ (cSd))'],\
['ns','material|n ',None,'(material|n=matter)'],\
['ns','matter',None,'(matter=particle)'],\
['ns','member',None,'(member = part)'],\
['ns','member|i',None,'(member|i = instance)'],\
['ns','mental whole',None,'(mental whole = thought)'],\
['n','mind|b',None,'(c=mind|b) & ((bIc) x^ ((bWd.h.j) & (dIe) & (hIf) & (jIg))) & (e=mind) & (f=imagination) & (g=sensorium)'],\
['as','natural|p',None,'(natural|p = material)'],\
['ns','number|i',None,'(number|i=integer)'],\
['ns','object',None,'(object=thing)'],\
['n','part|f|a',None,'(c=part|f|a) & ((bIc) x^ (bId)) & (d=fact)'],\
['n','part|i',None,'(c=part|i) & ((bIc) x^ (bId)) & (d=thought)'],\
['n','part|w',None,'(c=part|w) & ((bIc) x^ (bId)) & (d=possible relationship)'],\
['as','physical|c',None,'(physical|c = material|c)'],\
['as','physical|m',None,'(physical|m = material|m)'],\
['as','physical ',None,'(physical=material)'],\
['ns','trait',None,'(trait = property)'],\
['aa','possible',None,'(b=possible) & ((pJb) x^ (pPc))'],\
['n','present',None,'(present = now)'],\
['ns','qualia ',None,'(qualia=sensation)'],\
['r','right of','RT','(right of=RT) & ((bRTc) x^ (cLb))'],\
['ns','sense datum ',None,'(sense datum=particle|m)'],\
['ns','collection',None,'(collection = whole)'],\
['ns','time|m ',None,'(time|m=moment)'],\
['ns','character trait',None,'(character trait = property)'],\
['ns','universal',None,'(universal = concept|n)'],\
['','thing',None,'(c=thing) & ((bIc) x^ ((bId) ed^ (bIe))) & ((bId) t^ (bIh)) & (d=relation) & (e=non_relation) & (h=non_whole)'],\
['','non_relation',None,'(c=non_relation) & ((bIc) x^ ((bId) ed^ (bIe) ed^ (bIf) ed^ (bIg))) & (((bIe) ed^ (bIf)) t^ (bIh)) & (d=class concept) & (e=property|n) & (f=property) & (g=instance) & (h=non_whole)'],\
['','class concept',None,'(c=class concept) & ((bIc) x^ ((bId) ed^ (bIe))) & ((bId) t^ (bIf)) & ((bIc) t^ (bIg)) & (d=relationship) & (e=non_relationship) & (f=whole) & (g=non_whole)'],\
['','non_relationship',None,'(c=non_relationship) & ((bIc) x^ ((bId) ed^ (bIe))) & (d=whole) & (e=non_whole)'],\
['','non_whole',None,'(c=non_whole) & ((bIc) x^ ((bIe) ed^ (bIf) ed^ (bIg) ed^ (bIh) ed^ (bIj) ed^ (bIk))) & (e=letter) & (f=mind) & (g=moment) & (h=basic number) & (j=particle) & (k=point)'],\
['','whole',None,' (c=whole) & ((bIc) x^ ((bId) ed^ (bIe) ed^ (bIf) ed^ (bIg) ed^ (bIh))) & (d=imagination) & (e=possible world) & (f=reality) & (g=sensorium) & (h=other)'],\
['','relationship',None,'(c=relationship) & ((bIc) x^ ((bId) ed^ (bIe))) & (d=external relationship) & (e=thought)'],\
['','thought',None,'(c=thought) & ((bIc) x^ ((bJd) ed^ (bJe))) & (d=imaginary relationship) & (e=sensational relationship)'],\
['l','t^',None,'(p t^ q) & (eJc) & (nt+e~Jc) & (eb^dJc) & (db^(rJc) & (s~Jc) & (tJc) & (uJc))'],\
['l','v+',None,'(p v+ q) & (eJc) & (nt+e~Jc) & (eb^dJc) & (db^(rJc) & (s~Jc) & (tJc) & (u~Jc))'],\
['l','x^',None,'(p x^ q) & (eJc) & (nt+e~Jc) & (eb^dJc) & (db^(rJc) & (s~Jc) & (t~Jc) & (uJc))'],\
['l','i^',None,'postponed'],\
['l','nf^',None,'postponed'],\
['l','ed^',None,'(p ed^ q) & (eJc) & (nt+e~Jc) & (eb^dJc) & (db^(r~Jc) & (sJc) & (tJc) & (u~Jc))'],\
['lc','because',None,'(because b, c) x^ (b & (b i^ c))'],\
['rs','entails ',None,'(entails = i^)'],\
['lb','hence',None,'(hence = i^)'],\
['rbt','is','=','(is = =)'],\
['l','is|b',None,'(is|b = b^)'],\
['r','is|i ',None,'(is|i = x^)'],\
['rs','mean|e ',None,'(mean|e = x^)'],\
['rs','means|s ',None,'(means|s = =)'],\
['rs','means|t ',None,'(means|t = i^)'],\
['lb','not follow',None,'(not follow = nf^)'],\
['lc','since',None,'(since = because)'],\
['lb','so',None,'(so = i^)'],\
['r','synonymous|p with',None,'(synonymous|p with=x^)'],\
['r','synonymous with ',None,'(synonymous with==)'],\
['lb','then',None,'(then = i^)'],\
['lb','then|a',None,'(then|a = t^)'],\
['lb','therefore',None,'(therefore = i^)'],\
['lb','thus',None,'(thus = i^)'],\
['u','that|c',None,'(it J p that q) x^ (qJp)'],\
['u','that|o',None,'hard coded'],\
['us','that|s',None,'(that|s = which)'],\
['na','that|n',None,'(that|n = this|n)'],\
['na','there',None,'(there EX b) x^ (bEX)'],\
['na','this|n',None,'(this|n Rc) x^ (bRc)'],\
['u','where|i',None,'hardcoded - (bRc where|i dQf) x^ ((bRc) & (dQf INE c))'],\
['u','which',None,'(bRc which Qd) x^ ((bRc) & (cQd))'],\
['u','which|o',None,'hard coded'],\
['u','who',None,'((bRc who Qd) x^ ((bRc) & (cQd) & (bIe))) & (e=person)'],\
['u','who|o',None,'hard coded'],\
['u','whom',None,'hard coded'],\
['b','a|r',None,'redundant'],\
['b','an|r',None,'redundant'],\
['b','be|r',None,'redundant'],\
['b','did',None,'redundant'],\
['b','do',None,'redundant'],\
['b','does',None,'redundant'],\
['b','each other',None,'redundant'],\
['b','if',None,'redundant'],\
['b','in|r',None,'redundant'],\
['b','in common|r',None,'redundant'],\
['b','is|r',None,'redundant'],\
['b','it|r',None,'redundant'],\
['b','itself|r',None,'redundant'],\
['b','of|r',None,'redundant'],\
['b','on|r',None,'redundant'],\
['b','particular',None,'redundant'],\
['b','real|g',None,'redundant'],\
['b','same',None,'redundant'],\
['b','that|r',None,'redundant'],\
['dr','the|r',None,'redundant'],\
['b','then|r',None,'redundant'],\
['b','to|r',None,'redundant'],\
['b','was|r',None,'redundant'],\
['b','will|r',None,'redundant'],\
['b','(period)',None,'(b.cRd) x^ ((bRd) & (cRd))'],\
['b','c^',None,'(bc^c) means wherever we see b we may replace it with c but not vice_versa'],\
['b','e^',None,'If the symbols to the left or the right of e^ are written on a line, then we may write the symbols on the other side of e^ on a different line.'],\
['b','k^',None,'If the symbols to the left of k^ are written on a line, then we may write the symbol to the right of k^ on a different line'],\
['b','b^',None,'The symbol to the left of b^ is an abbreviation of the symbols on the right which are relationships'],\
['r','=',None,'(b=c) means wherever we see b we may replace it with c and vice_versa'],\
['ra','zzz',None,'(bzzzc) means we may not replace b with c and vice_versa'],\
['b','nt+',None,'(nt+p t^ (pIc)) & (c=relationship) & (qJd) & (qb^p&nt+p) & (d=consistent)'],\
['m','not',None,'~'],\
['ma','~',None,'(~p t^ (pIc)) & (c=relationship) & (qJd) & (qb^p&~p) & (d=contradictory)'],\
['b','g^',None,'If we have (bg^c) on line 3 and SUB 2,3 in the justification section then only in line 2 may we replace b with c but not vice versa.'],\
['c','and|c',None,'(b and|c c R d) x^ (b.cRd)'],\
['m','not|i',None,'(not|i = nt+)'],\
['rat','not equal to',None,'(not equal to = zzz)'],\
['','0',None,''],\
['','0',None,'Numbers'],\
['','0',None,''],\
['nu','0',None,'((b=0) x^ ((cGb) & (bGe))) & (c=1) & (e=1)'],\
['nu','1',None,'((b=1) x^ ((cGb) & (bGe))) & (c=2) & (e=0)'],\
['nu','2',None,'((b=2) x^ ((cGb) & (bGe))) & (c=3) & (e=1)'],\
['nu','3',None,'((b=3) x^ ((cGb) & (bGe))) & (c=4) & (e=2)'],\
['dd','at least one',None,'(at least one bRc) x^ ((zRc) & (zIb))'],\
['dd','at least three',None,'(((at least three bRc) & (bOFd) & (bIe)) x^ ((zRc) & (zId) & (yRc) & (yId) & (xId) & (ed^c))) & (e=plural form)'],\
['dd','at least two',None,'(((at least two bRc) & (bOFd) & (bIe)) x^ ((zRc) & (zId) & (yRc) & (yId))) & (e=plural form)'],\
['dd','exactly one',None,'(exactly one b R c) x^ ((zIb) & (((yIb) & (yRc)) t^ (y=z)))'],\
['dd','exactly three',None,'(((exactly three bRc) & (bOFd) & (bIe)) x^ ((yId) & (xId) & (yRc) & (ed^c) & (wRc) & (wId) & (((zId) & (zRc)) t^ ((z=y) ed^ (z=x) ed^ (z=w))))) & (e=plural form)'],\
['dd','exactly two',None,'(((exactly two bRc) & (bOFd) & (bIe)) x^ ((yId) & (xId) & (yRc) & (ed^c) & (((zId) & (zRc)) t^ ((z=y) ed^ (z=x))))) & (e=plural form)'],\
['a','second|m',None,'(z=second|m) & (y=first|m) & ((bJz) & (bIc)) x^ ((dJy) & (dIc) & (bSCMd))'],\
['a','second|o',None,'(z=second|o) & (y=first|o) & ((bJz) & (bIc)) x^ ((dJy) & (dIc) & (bSUOd))'],\
['a','second|p',None,'(z=second|p) & (y=first|p) & ((bJz) & (b=c Te)) x^ ((dJy) & (d=c Tf) & (bSCPd ASCc))'],\
['a','second|s',None,'(z=second|s) & (y=first|s) & ((bJz) & (bIc)) x^ ((dJy) & (dIc) & (bSCDd))'],\
['a','second|u',None,'(z=second|u) & (y=first|u) & ((bJz) & (bIc)) x^ ((dJy) & (dIc) & (bSCUd))'],\
['dd','zero',None,'(bR zero c) x^ ((b~Rc) & (cN0))'],\
['dd','zero',None,'(zero = no)'],\
['ddi','a',None,'((a bRc) x^ ((zRc) & (zIb) & (zJe))) & (e=indefinite)'],\
['ddi','a|a',None,'((a|a bRc) x^ ((zRc) & (zIb) & (zJe))) & (e=general)'],\
['di','all',None,'(all = every)'],\
['ds','another',None,'(another bRc) x^ ((zRc) & (zIb))'],\
['ds','any',None,'(any = every)'],\
['dt','any|n',None,'(b~R any|n c) x^ (bR no c)'],\
['d','anyone except',None,'((anyone except bRc) x^ ((anything except bRc) & (bId))) & (d=person)'],\
['d','anything except',None,'(anything except bRc) x^ (((z=~b) t^ (zRc)) & (b~Rc))'],\
['d','every',None,'((every bRc) x^ (((zIb) t^ (zRc)) & (zJe) & (yIb) & (yJd))) & (d=particular) & (e=general)'],\
['','every (different)',None,'((every b R different|b c) x^ ((dIb) t^ ((dRe) & (dRf) & (d~Rg))) & (((mIb) & (jIb) & (kIc)) t^ ((m~Rk) v+ (j~Rk)))) & (h=indefinite) & (e.f.gJh) & (e.f.gIc)'],\
['d','everything except|p',None,'((everything except|p bRc) x^ (((z~Ib) t^ (zRc)) & ((yIb) t^ (y~Rc)))'],\
['dd','few',None,'postponed'],\
['dd','many|d',None,'((many|d bRc) x^ ((zRc) & (zIb) & (zJe))) & (e=many)'],\
['dd','many|n',None,'((many|n bRc) x^ ((zIb) & (zRc) & (zJg) & (yIb) & (y~Rc) & (yJg) & (y zzz z))) & (g=many)'],\
['dd','many|s',None,'(many|s bRc) x^ ((zIb) & (zRc) & (zJd) & (yIb) & (y~Rc) & (yJd))'],\
['dd','no',None,'((no bRc) x^ (((zIb) t^ (z~Rc)) & (zJe) & (yIb) & (yJd))) & (d=particular) & (e=general)'],\
['d','no one except',None,'((no one except bRc) x^ ((only bRc) & (bId))) & (d=person)'],\
['dd','only',None,'(only bRc) x^ (((z=~b) t^ (z~Rc)) & (bRc))'],\
['ddi','the',None,'((the bRc) x^ ((zRc) & (zIb) & (zJe))) & (e=definite)'],\
['ds','all of the',None,'(all of the=all)'],\
['ds','all the',None,'(all the=all)'],\
['ds','an',None,'(an = a)'],\
['ds','an|a',None,'(an|a = a|a)'],\
['ws','anyone',None,'(anyone = every person)'],\
['ws','anything',None,'(anything = every thing)'],\
['ws','anything|a',None,'(anything|a = a|a thing)'],\
['ws','everyone',None,'(everyone = every person)'],\
['ds','everyone except',None,'(everyone except = every person except)'],\
['ws','everything',None,'(everything = any thing)'],\
['d','everything except',None,'(everything except = every thing except)'],\
['ds','none of the',None,'(none of the = no)'],\
['xs','not|i a',None,'(not|i a = no|s)'],\
['xs','not|i a',None,'(not|i a = no|s)'],\
['xs','not|i a|a',None,'(not|i a|a = no|s)'],\
['xs','not|i all',None,'(not|i all = many|n)'],\
['xs','not|i anything',None,'(not|i anything = no thing)'],\
['xs','not|i everyone',None,'(not|i everyone = many|s person)'],\
['xs','not|i everything',None,'(not|i everything = many|s thing)'],\
['dd','not|i many|d',None,'(not|i many|d bRc) x^ (exactly one bRc)'],\
['xs','not|i many|m',None,'(not|i many|m = few)'],\
['xs','not|i many|n',None,'(not|i many|n = every)'],\
['ws','nothing',None,'(nothing = no thing)'],\
['d','nothing|d',None,'((nothing|d bRc) x^ ((no b dRc) & (dIz))) & (z=thing)'],\
['ds','nothing except',None,'(nothing except = only)'],\
['ds','nothing except|p',None,'(nothing except|p = only|p)'],\
['ds','one',None,'(one=some)'],\
['ds','one of',None,'(one of=some)'],\
['ds','some',None,'(some=a)'],\
['ds','some|m',None,'(some|m = many|d)'],\
['ds','some|p',None,'(some|p = many|n)'],\
['ds','some of the',None,'(some of the = many|d)'],\
['ws','someone',None,'(someone = some person)'],\
['ws','someone|n',None,'(someone|n = some|m person)'],\
['ws','something',None,'(something = a thing)'],\
['ws','something',None,'(something = a thing)'],\
['ws','something|a',None,'(something|a = a|a thing)'],\
['ds','that|d',None,'(that|d=the)'],\
['ds','the|a',None,'(the|a=a)'],\
['ds','this',None,'(this=the)'],\
['p','he',None,'(d=person) & (e=male) & ((he Rb) t^ ((cRb) & (cJe) & (cId))) & (g=definite) & (h=particular)'],\
['ps','her',None,'(her=she)'],\
['q','her|p',None,'(d=person) & (e=female) & ((her|p bRc) t^ ((bRc) & (dJe) & (dPSb)))'],\
['ps','him',None,'(him=he)'],\
['q','his',None,'((his bRc) t^ ((zRc) & (zIb) & (dOWNz))) & (d=he)'],\
['p','i',None,'(d=person) & ((i Rb) t^ ((iId) & (iJg))) & (g=definite)'],\
['pa','it',None,'hard coded'],\
['v','it|p',None,'propositional it'],\
['p','it|w',None,'hard coded'],\
['q','its|a',None,'(bR its|a c) t^ ((zIc) & (bHMz) & (bRz))'],\
['ps','me',None,'(me=i)'],\
['q','my',None,'((my bRc) t^ ((zRc) & (zIb) & (iOWNz)))'],\
['q','my|a',None,'((my bRc) t^ ((zRc) & (zIb) & (iWz)))'],\
['q','our',None,'(d=person) & ((our bRc) t^ ((bRc) & (eId) & (zIe) & (ePSb)))'],\
['p','she',None,'(d=person) & (e=female) & ((she Rb) t^ ((cRb) & (cId) & (cJe) & (cJg) & (cJh))) & (g=definite) & (h=particular)'],\
['ps','them',None,'(them=they)'],\
['p','they',None,'(d=person) & ((they Rb) t^ ((cRb) & (cId) & (zIc) & (cJg) & (cJh))) & (g=definite) & (h=particular)'],\
['p','we',None,'(d=person) & ((we Rb) t^ ((cRb) & (cId) & (zIc) & (cJg) & (cJh))) & (g=definite) & (h=particular)'],\
['p','you',None,'(d=person) & ((you Rb) t^ ((cRb) & (cId) & (cJg))) & (g=definite)'],\
['p','you|p',None,'(d=person) & ((you|p Rb) t^ ((cRb) & (cId) & (zIc))) & (g=definite) & (h=particular)'],\
['q','your',None,'(e=person) & ((your bRc) t^ ((zRc) & (zIb) & (dOWNz))) & (d=you)'],\
['q','your|p',None,'(d=person) & ((your|p bRc) t^ ((bRc) & (eId) & (zIe) & (ePSb)))'],\
['n','ability',None,'(c=ability) & ((dH can b) x^ (d can R)) & (((bIc) & (R OFV b)) t^ (d can R))'],\
['ra','about','ABT','postponed'],\
['r','above|a','ABO','(above|a=ABO) & ((bABOc) x^ ((bSz) & (zABc)))'],\
['r','above|m','ABV','(above|m=ABV) & ((bABVc) x^ ((bSz) & (cSy) & (zABy)))'],\
['a','abstract',None,'(c=abstract) & ((bJc) x^ ((bAd) ed^ (bABe) ed^ (bGf) ed^ (gHb) ed^ (bWj) ed^ (mIb) ed^ (nJb) ed^ (bIo))) & (o=relation)'],\
['a','abstract|a',None,'(c=abstract|a) & (((bJc) & (bITd) & (bRe)) x^ (((fId) t^ (fRe))))'],\
['a','abstract|c',None,'(c=abstract|c) & (e=abstract) & (((bJc) & (dIb)) x^ (dJe))'],\
['a','abstract|d',None,'(c=abstract|d) & ((bJc) x^ ((bAd) ed^ (bABe) ed^ (bGf) ed^ (gHb) ed^ (bJp) ed^ (mIb) ed^ (nJb) ed^ (bIo))) & (o=relation) & (p=abstract|g)'],\
['a','abstract|g',None,'(c=abstract|g) & ((bJc) x^ ((bWe) t^ (eJf))) & (f=abstract|d)'],\
['n','abstract essence',None,'(abstract essence = essence|a)'],\
['e','abstractly',None,'((bEX abstractly) x^ ((bJd) & (bJc))) & (c=abstract) & (d=extant)'],\
['a','absurd',None,'(b=absurd) & ((pJb) x^ ((pJc) & (nt+pJc))) & (c=contradictory)'],\
['as','absurd|r',None,'(absurd|r = ridiculous)'],\
['ns','action',None,'(action = effect)'],\
['a','actual',None,'(c=actual) & (((bJc) & (bId)) x^ (bId))'],\
['ns','actual|s',None,'(actual|s = physical|s)'],\
['rs','actualize','ACU','(actualize = materialize)'],\
['e','actually',None,'(b=reality) & ((p actually) x^ (pIRb))'],\
['r','after|p','DDD','((bDDDc) x^ ((bWd) & (dJe) & (dAc))) & (e=first)'],\
['r','allow','ALO','(allow=ALO) & (eb^bPRVc) & ((bALOc) x^ ((dTRYc) t^ (b~TRYe)))'],\
['e','always|p',None,'(c=always|p) & ((pIVc) x^ ((bId) t^ (pPb))) & (d=possible world)'],\
['e','always',None,'(c=always) & ((pIVc) x^ ((bId) t^ (pTb))) & (d=moment)'],\
['rs','appear',None,'(appear=SM)'],\
['ns','arbitrary group',None,'(arbitrary group = group|a)'],\
['ns','area ',None,'(area=region)'],\
['a','artificial',None,'(c=artificial) & ((bJc) x^ ((bJd) & (eIf) & (eCAg INTh))) & (d=natural) & (f=person) & (gb^bJd) & (h=past)'],\
['rc','as','AS','(as=AS) & (((bASc) & (dRb)) x^ (cRb))'],\
['o','ask (how)',None,'((bASKc) x^ ((gIf) t^ (bTKk))) & (c b^ how CAe) & (f=cause) & (h b^ gCAe) & (k b^ hUj)  '],\
['o','ask (what)',None,'((hASKg) x^ ((cId) t^ (hTKk))) & (d=thing) & (e b^ bRc) & (g b^ bR what?) & (k b^ eUf)'],\
['rs','at|i',None,'(at|i=INP)'],\
['rs','at|n',None,'(at|n=NXT)'],\
['a','atomic|p',None,'(b=indefinable|p) & (c=property) & (e=relationship) & (gb^fHd) & (((dIc) & (dJb)) x^ ((hIe) t^ (hnf^g)))'],\
['a','atomic|r',None,'(b=indefinable|r) & (f=relationship) & (h=relation) & (cb^dRe) & (((R Jb) & (R If)) x^ ((gIf) t^ (gnf^c)))'],\
['o','atomic equivalent',None,'(b=indefinable equivalent) & (((cIb) & (cOFd)) x^ ((c x^ d) & (d~Jf) & ((eIc) t^ (eJf)))) & (f=indefinable)'],\
['n','atomic relationship',None,'(c=indefinable relationship) & (d=subject) & (e=relation) & (f=object) & (g=truth value) & (h=locative molecular relationship) & (k=variable) & ((bIc) x^ ((zId) & (yIe) & (wIg) & (bHz) & (bHy) & (vIf) & (bHV) & (bHv) & (vIk) & (zIk) & (uIh) & (bId) & (uHb)))'],\
['rs','attempt',None,'(attempt=TRY)'],\
['rs','attended',None,'(attended = participated)'],\
['as','authentic',None,'(authentic=actual)'],\
['na','authority',None,'postponed'],\
['n','axiom',None,'(c=axiom) & ((bIc) x^ ((eId) t^ (enf^b)) & (((bWf) & (fIg)) t^ (f~Wh))) & (g=antecedent sentence) & (h=I)'],\
['r','before','BF','(before=BF) & ((bBFc) x^ (cAb))'],\
['r','behind','BH','(behind=BH) & ((bBHc) x^ (cFb))'],\
['r','behind|w','BEH','(behind|d=BEH) & ((bBEHc) x^ ((bWd) & (dSe) & (cFe)))'],\
['n','belief',None,'(c=belief) & ((bIc) x^ (zBb))'],\
['r','believe','B','(believe=B) & ((bBc) x^ (bTKd)) & ((bBc) t^ (bTKc)) & (e=true) & (db^cJe)'],\
['rs','believe|t ',None,'(believe|t=BT)'],\
['rs','believes',None,'(believes = B)'],\
['r','believes|t','BT','(believe tentatively=BT) & ((bBTp) x^ ((bBr) & (bBp))) & (qb^b~Bp) & (rb^qPz)'],\
['r','belong|o','BLG','(belong|o=BLG) & ((bBLGc) x^ (cOWNb))'],\
['r','belongs to|i','BIM','(bBIMc) x^ (cHIMb)'],\
['r','below','BEL','(below|a=BEL) & ((bBELc) x^ ((bSz) & (cABz)))'],\
['r','below','BW','(below=BW) & ((bBWc) x^ (cABb))'],\
['r','below|m','BLW','(below|m=BLW) & ((bBLWc) x^ ((bSz) & (bSy) & (yABz)))'],\
['r','between|p','BTP','(between|p=BTP) & ((bBTPc_d) x^ ((bNz) & (cNy) & (dNx) & (((xGz) & (zGy)) ed^ ((yGz) & (zGx)))))'],\
['r','between|p','BTW','(between=BTW) & ((bBTWc_d) x^ (((bGc) & (dGb)) ed^ ((dGb) & (cGb))))'],\
['r','between|a','BTA','(bBTAc_d) x^ ((eIf) t^ ~((cRe) & (eRd))) & ((R=L) ed^ (R=AB) ed^ (R=F)) & (f=thing)'],\
['rs','between|t ',None,'(between|t=CBT)'],\
['na','body|c',None,'(c=body|c) & ((bIc) x^ ((bWd) t^ (dIe))) & (e=particle)'],\
['n','boundary',None,'(c=boundary) & (((bIc) & (dHb)) x^ (dINb))'],\
['rs','break',None,'(break=VIO)'],\
['ra','breaks','BRK','postponed'],\
['n','broad reality',None,'((b=broad reality) x^ (((cIRd) ed^ (cPe)) x^ (bWc))) & (d=reality)'],\
['ra','calculate','CLC','postponed'],\
['ra','calculates','CLC','postponed'],\
['ea','can|a',None,'(d=ability) & (((pb^bR) & (p can|a) & (R VCPc)) x^ (cId))'],\
['e','cannot|w',None,'(state=STT) & (c=absolutely false) & (((p cannot|w) & (bSTTp)) x^ ((bDz) & (zb^pJc)))'],\
['as','case',None,'(case = true)'],\
['r','continguous','CTG','(bCTGc) x^ (((bWd) x^ ((dINb) & (c~Wd))) & ((cWe) x^ ((eINc) & (b~We))) & (bWf) & (cWg) & ((hIj) t^ (h~BTAf_g))) & (j=thing)'],\
['ns','causal part',None,'(causal part = part|c)'],\
['na','causal role',None,'postponed'],\
['n','causal whole',None,'(c=causal whole) & (((bIc) & (bOFd)) x^ ((bCAUc) & (dIb)))'],\
['ra','cause','CA','((pCAq) x^ ((bRc INMd Te) t^ ((fQg INMj Th) & (dCTGj) & (hSUTe)))) & (pb^bRc INMd) & (qb^fQg INMj)'],\
['r','cause|i','CAU','(cause|i=CAU) & ((bCAUc) x^ ((bSz Ty CA c SzTx)))'],\
['ra','cause|m','CAUS','postponed'],\
['r','cause|p','CAS','(cause|p=CAS) & (e=reality) & ((bCASc GVd) x^ ((((dIRe Ty) & (bSzTy)) t^ (cPx)) & (xNw) & (((dIRe Ty) & (b~SzTy)) t^ (cPv)) & (vNu) & (wGu)))'],\
['r','cause|w','CSE','((bCSEc) x^ ((bWd) x^ ((d~Je Tf) t^ (c~Je Tg)))) & (((d~Je Tf) t^ (c~Je Tg)) t^ (gSUTf)) & (e=extant)'],\
['a','certain',None,'(b=certain) & (((cJb) & (cTOd Tg)) x^ ((eb^(cIRf)) & (dTKe Tg) & (hb^(d~TKe Tk)) & (nb^((jIm) t^ (h~Pj))) & (kAg) & (dTKn))) & (f=reality) & (g=now) & (m=possible world)'],\
['rxd','chronologically between','CBT','(chronologically between=CBT) & ((bCBTc and|c d) x^ (((bAc) & (dAb)) ed^ ((bAd) & (cAb))))'],\
['n','common name',None,'(c=common name) & ((bIc) x^ ((bId) & (bRFe) & (eIf))) & (d=word) & (f=concept|n)'],\
['ns','concept|p',None,'(concept|p=plan)'],\
['n','concept',None,'(c=concept) & ((dIb) ed^ (eHb) ed^ (fJb)) t^ (bIc)'],\
['na','concept phrase',None,'(c=concept_phrase) & ((bIc) x^ ((dIb) & (eRFb) & ((eWf) t^ (fIj)) & (eNg) & (gGh))) & (h=1) & (g=word)'],\
['ns','conclusion',None,'(conclusion=inference)'],\
['as','concrete',None,'(concrete=particular)'],\
['ns','condition|s',None,'(condition|s=situation)'],\
['o','connected|i',None,'(b=connected|i) & ((cJb) x^ ((gIe) & (gOFc) & (hId) & (cHVh) & (mHVc) & ((kIg) ed^ (k=g)) & (kJf))) & (d=main relation) & (e=indefinable equivalent) & (f=connected|s)'],\
['a','connected|s',None,'(b=connected|s) & ((c and|c d J b Te) x^ (((c t^ d) ed^ (c ed^ d) ed^ (c x^ d) ed^ (c v+ d)) & (c~IRf Te) & (d~IRf Te))) & (f=reality)'],\
['ns','consequence',None,'(consequence=inference)'],\
['a','consistently extant',None,'(c=consistently extant) & ((bJc) x^ (pPc)) & (pb^bJd) & (d=extant)'],\
['r','contain','CT','(contain=CT) & ((bCTc) x^ (cINb))'],\
['a','contingently contradictory',None,'(b=contingently contradictory) & ((p.qJb) x^ ((pJd) & (qJd) & (p.q~Jd))) & (d=consistent)'],\
['a','contradictorily extant',None,'(c=contradictorily extant) & ((bJc) x^ ((eIf) t^ (p~Pe))) & (pb^bJd) & (d=extant) & (f=possible world)'],\
['a','contradictorily extant|a',None,'(c=contradictorily extant|a) & ((bJc contradictorily) x^ ((pWb) & ((eIf) t^ (p~Pe)))) & (d=extant) & (f=possible world)'],\
['','contradictory',None,'(c=contradictory) & ((pJc) x^ ((bId) t^ (p~Pb))) & (pb^q.nt+q)'],\
['rs','contrary of',None,'(contrary of=NEG)'],\
['as','contrasting ',None,'(contrasting=different)'],\
['r','correspond|s','CRS','(corresponds|s to=CRS) & ((bCRSc) x^ ((zb^yIRx) & (((bHw) & (w=~z)) t^ (cHw))))'],\
['r','count',None,'((bCNTc) x^ (bTKd)) & (db^(cWe) & (cNf))'],\
['r','count|n',None,'(bCOTc) x^ (cNb)'],\
['n','courage',None,'(b=courage) & ((cHb) x^ (cJd)) & (d=courageous)'],\
['na','courageous',None,'postponed'],\
['na','dead',None,'postponed'],\
['ns','deduction',None,'(deduction=inference)'],\
['aa','definite',None,'(definite = individual)'],\
['as','definite|v',None,'(definite|v = certain)'],\
['n','definite description',None,'(c=definite description) & ((bIc) x^ ((dHb) & ((ezzzd) t^ (e~Hb)))) & (d=property)'],\
['axd','different',None,'(c=different) & ((b and|c d J c) x^ (b=~c))'],\
['r','different from','DF','(different from=DF) & ((bDFc) x^ (bzzzc))'],\
['a','difficult',None,'(c=difficult) & (((bJc) & (bTOd)) x^ ((dTRYb Tf) t^ ((hWe) x^ ((bPe Tg) & (gAf) & (hJk))))) & (k=few)         '],\
['rs','distinct from',None,'(distinct from = zzz)'],\
['a','divine',None,'(b=divine) & (c=God) & ((dJb) x^ (d=c))'],\
['a','divine|s',None,'(c=divine|s) & (d=God) & ((bJc) x^ (bSMLd))'],\
['ns','duration ',None,'(duration=period)'],\
['r','during','DUR','(during=DUR) & ((pDURb) x^ ((bWc.d.e) & (pTe) & (eAc) & (dAe)))'],\
['r','during|o','DRG','(during|o=DRG) & ((bDRGc) x^ ((bWe) t^ ((cWe) & (eIf)))) & (f=moment)'],\
['r','during|t','DR','(during|t=DR) & ((bDRc) x^ ((cWb.d.e) & (eAb) & (bAd)))'],\
['r','earlier|p than','ELA','(bELAc) x^ (((bWd) & (cWe)) t^ (eAd))'],\
['r','earlier than','EL','(earlier than=EL) & ((bELc) x^ (cAb))'],\
['a','easy',None,'(c=easy) & (((bJc) & (bTOd)) x^ ((dTRYb Tf) t^ ((hWe) x^ ((bPe Tg) & (gAf) & (hJk))))) & (k=many)         '],\
['r','empirical (of a relation)',None,'(b=empirical) & (R Jb) x^ ((R = SEE) ed^ (R = HR) ed^ (R = TOC) ed^ (R = TST) ed^ (R = SML))'],\
['ns','empty space',None,'(empty space=void)'],\
['n','energy',None,'(c=energy) & ((bIc) t^ ((dHb) & (dIf))) & (f=particle)'],\
['a','entire past',None,'((b=entire past) x^ ((bWc) t^ (dAc))) & (d=now)'],\
['ns','entity',None,'(entity=thing)'],\
['ns','entity|n',None,'(entity|n=object|n)'],\
['n','epistemic possible world',None,'(b=epistemic possible world) & (fb^d~Be) & (((cIb) & (cTOd)) x^ (fPc))'],\
['a','epistemically contingent',None,'postponed'],\
['a','epistemically impossible',None,'(b=epistemically impossible) & (e=possible world) & (rb^(dIe) u+ (d~Pe)) & (qb^cBp) & ((pJ b TO c) x^ ((cBr) & (bBp)))'],\
['a','epistemically necessary',None,'(b=epistemically necessary) & ((pJ b TO c) x^ (cKNp))'],\
['a','epistemically probable',None,'(b=epistemically probable) & (((pJb) & (pTOc Td)) x^ ((zb^cBp Ty) & (xb^c~Bp Ty) & (yAd) & (zNw) & (yNv) & (ub^wGv) & (cBu Td)))'],\
['n','essence|a',None,'(c=essence|a) & ((bIc) x^ ((zIy) x^ (zHb)))'],\
['n','essence|i',None,'(c=individual essence) & ((bIc) & (uHSb Te)) x^ (((bWj Tg) & (jIn) & (dHj)) t^ ((qJr) & (s~Jr))) & ((fWm) x^ ((tHm Tg) & (mIn))) & ((qWp) x^ (oPp)) & ((sWq) x^ (nt+oPq)) & (uWt.d) & (eSUTg))) & (n=intrinsic accidental property) & (r=many) & (ob^fWj Te)'],\
['na','essence|n',None,'postponed'],\
['n','essence|p',None,'(c=individual essence|p) & (((bIc) & (dHSb) & (fWd)) x^ ((fHSj) & (jIg) & ((bWh) x^ (jWh)))) & (g=individual essence)'],\
['n','event',None,'(b=event) & ((pIb) x^ (pOC))'],\
['n','everything|n',None,'((b=everything|n) x^ ((cId) t^ (bWc))) & (d=thing)'],\
['r','exist|b','EXB','((bEXB) x^ (bJc)) & (c=contradictorily extant)'],\
['r','exist|c','EXC','((bEXC) x^ (bJc)) & (c=consistently extant)'],\
['rs','exist as',None,'(exist as = I)'],\
['r','exists','EX','(exists=EX) & ((bEX) x^ (bJc)) & (c=extant)'],\
['rs','exists|a',None,'(exists|a=EA)'],\
['rs','exists|i',None,'(exists|i=EI)'],\
['rs','exists|m',None,'(exists|m=EM)'],\
['rs','exists|n',None,'(exists|n=EXN)'],\
['rs','exists|p',None,'(exists|p=EP)'],\
['rs','exists|s',None,'(exists|s=ES)'],\
['r','exists divinely','ED','(exists divinely=ED) & (c=God) & ((bED) x^ (bIc))'],\
['r','exists historically','EH','(exist historically=EH) & (c=current present) & ((bEH) x^ ((bSzTy) & (cAy)))'],\
['r','exists in the imagination','EI','(exists in the imagination=EI) & ((bEI) x^ (bMz))'],\
['r','exists intersubjectively','EIN','(exists intersubjectively=EIN) & ((bEIN) x^ ((bMy z) & (xN2) & ((y=x) ed^ (yGx))))'],\
['r','exists mentally','EM','(exists mentally=EM) & ((bEM) x^ (bTKz))'],\
['r','exists naturally','EXN','(exists naturally=EXN) & ((bEXN) x^ (bSz))'],\
['rs','exists physically ',None,'(exists physically=EXN )'],\
['r','exists probabilistically','EP','(exists probabilistically=EP) & ((bEP) x^ (bPz))'],\
['r','exists sensationally','ES','(exists sensationally=ES) & ((bES) x^ (bOz))'],\
['n','explicit|e relationship|e',None,'(c=explicit|e relationship|e) & ((bIc) x^ ((bWd) & (bWe) & (bWh) & (dIf) & (eIg) & (hIf))) & (f=relatum) & (g=relation)'],\
['n','external relationship',None,'(c=external relationship) & ((pIc) x^ ((pPd) v+ (pIRe))) & (e=reality)'],\
['a','fake',None,'(c=fake) & (((bJc) & (bId)) x^ (b~Id))'],\
['a','false',None,'(c=false) & ((bJc) x^ (b~Jd)) & (d=true)'],\
['n','familial part',None,'(c=familial part) & (((bIc) & (bOFd)) x^ (bId))'],\
['n','familial part|a',None,'(c=familial part|a) & ((bIc) x^ (dHMb))'],\
['ns','familial whole',None,'(familial whole=group)'],\
['na','family',None,'postponed'],\
['n','family|i',None,'(b=family|i) & (((cIb) & (dIc) & (eIc)) x^ (((dIf) & (dOFe)) ed^ ((eIf) & (eOFd)) ed^ ((dIh) & (dOFe)) ed^ ((eIh) & (eOFd)) ed^ ((dIg) & (dOFe)) ed^ ((eIg) & (eOFd)) ed^ ((dIk) & (dOFe)) ed^ ((eIk) & (eOFd)) ed^ ((dIl) & (dOFe)) ed^ ((eIl) & (eOFd)))) & (f=sibling) & (g=mother) & (h=father) & (k=aunt) & (l=uncle)'],\
['aa','fanatical',None,'postponed'],\
['ra','feel',None,'postponed'],\
['ra','feels',None,'postponed'],\
['a','few|a',None,'(c=few|a) & (((bJc) & (eJf)) x^ ((bNd) & (eNg) & (gGd))) & (f=many|a)'],\
['d','few ',None,'(few=~mn)'],\
['a','fictional',None,'(c=fictional) & ((bIc TOh) x^ ((bMd) & (hTKe))) & (eb^(fIRg) t^ (b~CRRf)) & (g=reality)'],\
['ra','follows from (contingently)','FLC','(follows from=FLC) & ((bFLCc) x^ ((dJm Pe) & (fJm Pg) & (h~Jm Pm) & (jJm Pk))) & (db^b.c) & (fb^b.nt+c) & (hb^nt+b.c) & (jb^nt+b.nt+c) & (m=probable)'],\
['ra','follows from (necessarily)','FL','(follows from=FL) & ((bFLc) x^ ((dJta^ Pe) & (fJta^ Pg) & (hJco^ Pm) & (jJta^ Pk))) & (db^b.c) & (fb^b.nt+c) & (hb^nt+b.c) & (jb^nt+b.nt+c)'],\
['as','forbidden',None,'(forbidden=morally impossible)'],\
['as','forbidden|l',None,'(forbidden|l=legally impossible)'],\
['rs','from|b',None,'(from|b = born)'],\
['rs','from|c','FRMC','(FRMC = FLC)'],\
['r','front|a','FRA','(in|r front|a of|r=FRA) & ((bFRAc) x^ (((bWm) & (mSj)) t^ (jFc))) & (cIf) & (jIf) & (f=point) & (h=particle) & (k=natural whole) & (bIk) & (mIh)'],\
['r','front|m','FRN','(in|r front|m of|r=FRN) & ((bFRNc) x^ ((bSz) & (cSy) & (zFy)))'],\
['r','front|o','FRO','(in|r front|p of|r=FRO) & ((bFROc) x^ (((cWd) & (dSe)) t^ (bFe))) & (f=natural whole) & (g=point) & (h=particle) & (bIg) & (cIf) & (dIh)'],\
['r','front|w','FNT','(in|r front|w of|r=FNT) & ((bFNTc) x^ ((bWd) & (dSe) & (cWf) & (fSg)) t^ (eFg))'],\
['aa','general',None,'hard coded'],\
['ns','general term',None,'(general term = concept|n)'],\
['as','genuine',None,'(genuine=actual)'],\
['r','given','GV','(given=GV) & ((pGVq) x^ (qu+p))'],\
['ra','go','GO','postponed'],\
['ra','go to','GO','postponed'],\
['n','goal',None,'(c=goal) & (((bIc) & (bFORd)) x^ (dDb))'],\
['n','God',None,'(b=God) x^ (((b~EX) & (z=~b)) t^ (z~EXN))'],\
['ra','goes','GO','(GO=MOV)'],\
['aa','good',None,'postponed'],\
['r','greater than','GR','(greater than=GR) & ((bGRc) x^ (bGc))'],\
['n','group|a',None,'(c=group|a) & ((bIc) x^ ((bWs) x^ (sHu))) & (xb^(wWb) x^ (wHv)) & (ub^tBx)'],\
['na','HA ... friend icm',None,'b and c have a friend in common: postponed'],\
['ns','haecceity',None,'(haecceity=unique essence)'],\
['rs','happen ',None,'(happen=OC)'],\
['ra','has|c','HC','postponed'],\
['r','has|p|k (causal power)','HCB','(has|p|k= HCB) & ((bHCBc) x^ ((bRd INMe Tf) t^ ((gRh INMe Tg) & (gSUTf)))'],\
['r','has|c|p','HCP','(bHCPc) x^ ((bWc) x^ (bCSEd))'],\
['r','has|c|r (causal role)','HCA','((bHCAc) x^ (bCAc)) & ((bHCAc) t^ (bHc))'],\
['ra','has|e (corpse)','HA','has|c=HA, c=matter, d=dead ((bHAz) & (zIc)) x^ ((zSy) & (bOWNz) & (zJd))'],\
['r','has|g|c','HGC','(cHGCb) x^ ((bWe) t^ (eIc))'],\
['r','has|i','HI','((bHIc) x^ (((bWc) ed^ (bHc)) & (cJd))) & (d=intrinsic)'],\
['r','has|i|m','HIM','((bHIMc) x^ (cMb))'],\
['r','has|m','HM','(have|m=HM) & ((bHMc) x^ (cIb))'],\
['r','has|n','HN','(has|n=HN) & ((bHNc) x^ ((bINd) & (bINe) & (eINUd)))'],\
['r','has|s','HSS','(bHSSc) x^ ((cOd) & (bWc))'],\
['r','has|s|p','HSP','(bHSPc) x^ (cINb)'],\
['r','has|t','HAT','(have|t = HAT) & ((bHATc) x^ (cTCHb))'],\
['r','has|p|j','HCD','(has|p|j = HCD) & ((bHCDc) x^ (((bTKWr) & (rCRRq) & (qPh) & (To)) t^ ((qTg) & (gAo))) & (qb^bRu INSm)'],\
['r','has|p|e','HCE','(bHCEc) x^ ((bHCBc) ed^ (bHCDc))'],\
['','have|b','HB','((bHBc) x^ ((bWc) & (cId))) & (d=body|c)'],\
['r','have|g|c','HGC','(cHGCb) x^ ((bWe) t^ (eIc))'],\
['rxd','have|i|c (... in common|r)','HCM','(b and|c c HCM d) x^ ((bJd) & (cJd))'],\
['rs','have|o ',None,'(have|o=own)'],\
['r','have|p|n','HPN','((bHPNc) x^ (cRFb)) & ((bHPNc) t^ ((bId) & (cIe))) & (d=individual) & (e=proper name)'],\
['r','have|r (object is a relation)','HR','((bHRc TOd) x^ (bRd)) & (c=R)'],\
['r','have|t','HAT','(have|t = HAT) & ((bHATc) x^ (cTCHb))'],\
['ra','have|w','W','(c=body) &  (((bWz) & (zIc)) x^ (zSy))'],\
['ra','have a baby',None,'postponed'],\
['ra','have a feeling that',None,'postponed'],\
['ra','have a friend',None,'postponed'],\
['ra','have a moment',None,'postponed'],\
['ra','have a name',None,'postponed'],\
['ra','have a permit',None,'postponed'],\
['ra','have a person',None,'postponed'],\
['ra','have a plan',None,'postponed'],\
['ra','have a question',None,'postponed'],\
['ra','have a requirement',None,'postponed'],\
['ra','have an experience',None,'postponed'],\
['ra','have an idea',None,'postponed'],\
['ra','have difficulty',None,'postponed'],\
['ra','have fun',None,'postponed'],\
['ra','have sex',None,'postponed'],\
['ra','have space left',None,'postponed'],\
['ra','have time',None,'postponed'],\
['ra','have trouble',None,'postponed'],\
['rs','hence ',None,'(hence=i^)'],\
['a','historical',None,'(c=historical) & (d=current present) & ((bJc) x^ ((bTz) & (dAz) & (b~Td)))'],\
['n','hypothetical material object',None,'(c=hypothetical material object) & ((bIc) x^ ((bSz) ed^ (b~Sd)))'],\
['rs','identical',None,'is identical to=='],\
['ns','identification',None,'(identification=definite description)'],\
['r','identify',None,'(identify=IDT) & ((bIDTc) x^ ((cHd) & (cJe) & (bTNKf) & (dIg))) & (f b^ cHd) & (d=individual essence) & (e=particular)'],\
['a','imaginary',None,'(c=imaginary) & ((bIc TOh) x^ ((bMd) & (hTKe))) & (eb^(fIRg) & (bCRRf)) & (g=reality)'],\
['n','imagination',None,'(c=imagination) & ((bIc) x^ (zMb))'],\
['n','implicit|i relationship|i',None,'(c=implicit|i relationship|i) & ((bIc) x^ ((bWd) & (bWe))) & (dIf) & (eIg) & (f=subject|i) & (g=intransitive verb)'],\
['rs','implies ',None,'(implies=i^)'],\
['aa','important',None,'postponed'],\
['a','improbable',None,'(c=improbable) & ((bJc) x^ (b~Jd)) & (d=probable)'],\
['ratso','in','IN','((bINc) x^ ((bId) & (cWb))) & (d=point)'],\
['rs','in|a ',None,'(in|a=DUR)'],\
['r','in|b','INB','((bINBc) x^ ((cWb) & (bId))) & (d=moment)'],\
['r','in|f','INF','(bINFc) x^ ((bId) & (cId) & ((cWe) x^ (bWe))) & (d=period)'],\
['r','in|c','INC','(in) & ((bINCc) t^ ((zSc) & (dIc) & (eIc) & (fIc) & (gIc) & (hIc) & (iIc) & (jIc) & (kIc) & (hLi) & (hABj) & (dFh) & (eFi) & (iABk) & (eABg) & (dLe) & (dABf) & (fFj) & (hLb) & (hABb) & (bLi) & (iABb) & (bLk) & (bABk) & (jLb) & (bABj)))'],\
['ratso','in|d','IND','((bINDc) t^ (((bWd) & (dIe)) x^ (cWd))) & (e=point)'],\
['r','in|e','INE','(bINEc) x^ ((bSd) & (cWd))'],\
['r','in|g','ING','(c=relationship) & (in|g=ING) & ((bINGp) x^ (((bAWz) ed^ (zAWb)) & (pWb) & (pIc)))'],\
['r','in|m','INM','(bINMc) x^ (((bWd) x^ ((dSe) & (cWe))) & (bWf) & (fSg) & (hWg))'],\
['r','in|s','INS','(bINSc) x^ ((bWd) & (dINMc))'],\
['r','in|r','INR','(in|r=INR) & ((bINRc) x^ ((bSd) & (dINc)))'],\
['rs','in|p','INP','(in|s = is|g)'],\
['rs','in|t ',None,'(in|t=during)'],\
['','in-q','INQ','((bINQc) & (cJd)) x^ (bJd)'],\
['r','in|v','INV','((bINVc) x^ ((bCAc) & (dWb.e) & (eWf) & (fIg))) & (cb^fMOV) & (g=body|c)'],\
['aa','indefinite',None,'(b=indefinite) & ((cJb) x^ ((cJj) & ((kzzzc) t^ (k~Jj)) & ((eId) t^ ((fPg) & (nt+fPh))))) & (f b^ e=c) & (cId)'],\
['aa','indefinite|a',None,'postponed'],\
['a','indeterminate',None,'(b=indeterminate) & (((pJb) & ((p=q) ed^ (p=r))) x^ ((qNz) & (rNy) & (xNw) & (pNv) & (wGy) & (zGw) & ((vGw) ed^ (wGv))))'],\
['a','indexical',None,'postponed'],\
['nk','individual',None,'(b=individual) & ((cIb) x^ ((dIe) t^ (d~Ic))) & (e=thing)'],\
['as','individual|p',None,'(individual|p=particular)'],\
['ns','individual essence',None,'(individual essence=essence|i)'],\
['n','individual essence',None,'(individual essence = essence|i)'],\
['n','individual|p',None,'(c=individual|p) & ((bIc) x^ ((bWd.e) & (dSf) & (eTKg) & (bNh))) & (h=2)'],\
['r','infer','INF','(infer=INF) & ((bINFc d) x^ ((zb^nt+c && d) & (yb^zJco^) & (bBy)))'],\
['n','inference|c',None,'(c=inference) & ((bIc) x^ (dFLCb)) & (follows from=FLC)'],\
['n','inference|n',None,'(c=inference) & ((bIc) x^ (dFLb)) & (follows from=FL)'],\
['a','infinite',None,'(c=infinite) & (((bJc) & (bPCPc)) x^ ((zIc) t^ (((yGz) & (zGx)) ed^ ((yAz) & (zAx)) ed^ ((yLz) & (zLx)) ed^ ((yABz) & (zABx)) ed^ ((yFz) & (zFx)))))'],\
['a','infinite',None,'(c=infinite) & ((bJc) x^ ((zIb) t^ ((yGz) & (zGx)) ed^ ((yAz) & (zAx)) ed^ ((yLz) & (zLx)) ed^ ((yABz) & (zABx)) ed^ ((yFz) & (zFx))))'],\
['rs','inside',None,'(inside = INE)'],\
['ns','interval ',None,'(interval=period)'],\
['r','intrinsic',None,'(c=intrinsic) & ((dWb) ed^ (dHb)) t^ (bJc)'],\
['ra','is|e','EX','((bEX) x^ (bJc)) & (c=extant)'],\
['ns','item|n',None,'(item|n=object|n)'],\
['rs','judge',None,'(judge = believe)'],\
['ns','kind',None,'(kind=type)'],\
['ns','kind',None,'(kind|n = natural kind)'],\
['ns','kind',None,'(kind = type)'],\
['aa','large',None,'postponed'],\
['r','later than','LAT','(later than=LAT) & ((bLATc) x^ (bAc))'],\
['r','left of|a','LEF','(left of|a=LEF) & ((bLEFc) x^ ((bSz) & (zLc)))'],\
['r','left of|m','LFT','(left of|m=LFT) & ((bLFTc) x^ ((bSz) & (cSy) & (zLy)))'],\
['a','legally contingent',None,'(b=legally contingent) & (d=authorities) & (punish=PNS) & ((pJb SsTt) x^ (((mn dDv SsTt) ed^ (all dDv SsTt)) & (vb^u~Po) & (uCRRp) & (xb^tPNSz) & ((z~CAp SsTt) t^ ((mn d~Dx SsTt) ed^ (all d~Dx SsTt))) & ((zCAp SsTt) t^ ((mn d~Dx SsTt) ed^ (all d~Dx SsTt)))))'],\
['a','legally impossible',None,'(b=legally impossible) & (d=authorities) & (punish=PNS) & ((pJb SsTt) x^ (((mn dDv SsTt) ed^ (all dDv SsTt)) & (vb^u~Po) & (uCRRp) & (xb^tPNSz) & ((zCAp SsTt) t^ ((mn dDx SsTt) ed^ (all dDx SsTt))) & ((z~CAp SsTt) t^ ((mn d~Dx SsTt) ed^ (all d~Dx SsTt)))))'],\
['a','legally necessary',None,'(b=legally necessary) & (d=authorities) & (punish=PNS) & ((pJb SsTt) x^ (((mn dDv SsTt) ed^ (all dDv SsTt)) & (vb^u~Po) & (uCRRp) & (xb^tPNSz) & ((z~CAp SsTt) t^ ((mn d~Dx SsTt) ed^ (all d~Dx SsTt))) & ((zCAp SsTt) t^ ((mn dDx SsTt) ed^ (all dDx SsTt)))))'],\
['r','lesser than','LSS','(lesser than=LSS) & ((bLSSc) x^ (cGb))'],\
['r','lie','LI','(lies about=LI) & ((bLIp|c) x^ ((bSTTp|c) & (b~Bp) & (zb^cBp) & (bDz)))'],\
['ra','live','LV','postponed'],\
['ra','lives','LV','postponed'],\
['na','logic',None,'postponed'],\
['a','logically contingent',None,'(b=logically contingent) & ((pJb) x^ ((pJta^) & (nt+pJta^)))'],\
['a','logically impossible',None,'(b=logically impossible) & ((pJb) x^ ((nt+pPc) & ((dIe) t^ (p~Pd)))) & (e=possible world)'],\
['a','logically necessary',None,'(b=logically necessary) & ((pJb) x^ ((pJta^) & (nt+p~Jta^)))'],\
['a','logically possible',None,'(b=logically possible) & (c=logically necessary) & (d=logically contingent) & ((pJb) x^ ((pJc) ed^ (pJd)))'],\
['as','logically true',None,'(logically true=logically necessary)'],\
['n','lower class',None,'(d=lower) & (c=class) & (f=natural essence) & (((bIc) & (bJd) & (eIb)) x^ (((zIe) x^ (zHy)) & (yIf) & (((xIe) & (o~Ix)) t^ (xSw))))'],\
['rs','make','MK','(make = cause)'],\
['r','make sense','MK','(make=MK) & (c=sense|a) & (d=grammatical) & ((bMKc) x^ ((bJd) & (bJta^)))'],\
['a','many',None,'(z=many) & (y=2) & ((bJz) x^ ((bNy) ed^ ((bNc) & (cGy))))'],\
['a','many|a',None,'(c=many|a) & (((bJc) & (eJf)) x^ ((bNd) & (eNg) & (dGg))) & (f=few|a)'],\
['n','material part',None,'(c=material part) & (e=sentient being) & (((bIc) & (bOFd)) x^ ((bSz) & (dWb) & (dIe)))'],\
['n','material whole',None,'(c=material whole) & (e=material part) & (((bIc) & (bOFd)) x^ ((dIe) & (bWd)))'],\
['r','materialize','MTL','(materialize=MTL) & (bMTL Tc) x^ ((b~EXN Td) & (bEXN Tc) & (cAd))'],\
['r','means|r',None,'((bMNc BYd TOe Tg) x^ ((bCAd Tg) & (bDf))) & (fb^(eEXPd Tg) t^ ((eBc Th) & (hSUTg)))'],\
['as','meaningful',None,'(meaningful=significant)'],\
['a','mental',None,'(c=mental) & ((bJc) x^ (bTKd))'],\
['aa','mental|a',None,'(c=mental) & ((bJc) x^ ((eTKb) ed^ (bTKd)))'],\
['a','mental|b',None,'(c=mental) & ((bJc) x^ (dTKb))'],\
['ns','moment|e',None,'(moment|e=event)'],\
['n','moment|f (first)',None,'(z=moment) & (((bIz) & (bJf)) x^ ((cTb) & (dAb))) & (f=first)'],\
['n','moment|l (last)',None,'(z=moment) & (((bIz) & (bJf)) x^ ((cTb) & (bAd))) & (f=last)'],\
['a','morally contingent',None,'(b=morally contingent) & (c=painful) & (f=acceptable) & ((pJb e) x^ ((zCRRp) & ((yJc) ed^ (y~Jc)) & (vb^yGx) & (vJd) & (zCAUy) & (ub^vJf) & (tb^xGnt+y) & (sb^tJf) & ((nt+y~Jc) ed^ (nt+yJc)) & (eBu) & (eBs)))'],\
['a','morally impossible',None,'(b=morally impossible) & (c=painful) & (d=unacceptable) & (f=acceptable) & ((pJb e) x^ ((zCRRp) & (yJc) & (vb^yGx) & (vJd e) & (zCAUy) & (ub^(vJd e)) & (tb^xGnt+y) & (sb^tJf e) & ((nt+y~Jc) ed^ (nt+yJc)) & (eBu) & (eBs)))'],\
['a','morally necessary',None,'(b=morally necessary) & (c=painful) & (d=unacceptable) & (f=acceptable) & ((pJb e) x^ ((zCRRp) & ((yJc) ed^ (y~Jc)) & (vb^yGx) & (vJd) & (zCAUy) & (ub^vJf) & (tb^xGnt+y) & (sb^tJd) & (nt+yJc) & (eBu) & (eBs)))'],\
['d','more',None,'(more...than) & ((bR mor c thn d Uf) x^ ((cNz Uf) & (dNy Uf) & (zGy) & (bRc Uf) & (bRd Uf)))'],\
['aa','mortal',None,'postponed'],\
['r','move','MV','(bMV FM c Td TOe Tf) x^ ((bINMc Td) & (bINMe Tf))'],\
['','move|m','MOV','(bMOVc FM d Te TOf Tg) x^ ((bWh.c) & (((hBk Te) & (cINMd)) t^ (cINMf Tg)))'],\
['','move|a','MVA','(bMVAc FM d Te TOf Tg RLj) x^ ((bWh.c) & (jINMk Te) & (jINMk Tg) & (((hBk Te) & (cINMd)) t^ (cINMf Tg)))'],\
['na','murder',None,'postponed'],\
['e','must|w',None,'(states=STT) & (c=absolutely true) & (((p must|w) & (bSTTp)) x^ ((bDz) & (zb^pJc)))'],\
['n','narrow reality',None,'(d=reality) & ((b=narrow reality) x^ ((zIRd) t^ (zIb)))'],\
['a','natural|s (statement)',None,'(b=natural|s) & ((cJb) x^ ((cWd) & (dJe) & (dIf) & (jIh) & (jJg.k))) & (e=natural) & (f=subject) & (g=active) & (h=relation) & (k=non_spatio_temporal)'],\
['ns','natural essence',None,'(natural essence = essence|n)'],\
['na','natural kind ',None,'(c=natural kind) & ((bIc) x^ ((dIb) & (dJe))) & (e=material)'],\
['n','natural number',None,'(c=natural number) & ((bIc) x^ ((zNb) & ((b=0) ed^ (bG0))))'],\
['aa','necessary',None,'(necessary = logically necessary)'],\
['r','necessary physical condition','NC','(necessary physical condition=NC) & (g=possible worlds) & (h=reality) & (((bScTd) & (eScTf) & (pNCq GVr)) x^ ((pb^eSc) & (qb^bSc) & (fSUTz) & (zSUTd)  & (((rIRh) & (pTd)) t^ ((qPy Tz) & (nt+qPx Tz))) & (((rIRh) & (p~Td)) t^ (q~Po Tz)) & (pP mn g)))'],\
['r','negation of','NEG','(is the negation of=NEG) & (b=contradictory) & ((pNEGq) x^ ((rb^p && q) & (rJb)))'],\
['e','never',None,'(never=nv) & ((p nv) x^ (p~To))'],\
['ra','next to','NXT','next to: postponed'],\
['ns','non actual relationship',None,'(non actual relationship=possible relationship)'],\
['n','non_relationship',None,'(c=non_relationship) & ((bIc) x^ (((dIe) t^ (b~Wd)) & ((fIg) t^ (b~Wf)))) & (g=relation) & (e=relatum)'],\
['n','non_whole',None,'(c=non_whole) & ((bIc) x^ ((dIe) t^ (b~Wd))) & (e=thing)'],\
['r','noun counterpart of','NCP','(is the noun counterpart of=NCP) & (is the adjective counterpart of=ACP) & ((bNCPc) x^ (cACP))'],\
['ns','number|n',None,'(number|n=natural number)'],\
['n','object|r',None,'(c=object|r) & (d=relation) & (e=noun) & ((bIc) x^ ((zId) & (bIe) & (bAWz)))'],\
['n','object|n',None,'(c=object|n) & (d=relation) & (e=thing) & ((bIc) x^ ((bIe) & (b~Id)))'],\
['a','objective',None,'(b=objective) & (c=reality) & ((pJb) x^ ((pPz) ed^ (pIRc)))'],\
['as','obligatory',None,'(obligatory=morally necessary)'],\
['as','obligatory|l',None,'(obligatory|l=legally necessary)'],\
['r','occur','OC','(occur=OC) & ((pOC) x^ ((p~IRd Tb) & (pIRd Tc) & (cAb))) & (d=reality)'],\
['ra','of|n','OFN','(((bOFNc) & (bId) & (cIe)) x^ ((fWb.c) & (fIg))) & (g=root) & (d=noun) & (e=adjective)'],\
['ra','of|v','OFV','(((bOFVc) & (bId) & (cIe)) x^ ((fWb.c) & (fIg))) & (g=root) & (d=verb form) & (e=noun form)'],\
['ra','of','OF','postponed'],\
['r','of|a','OFA','(of|a=OFA) & (((bOFAc) & (dACPc)) x^ (bJd))'],\
['rs','of|c','OFC','(OFC = FLC)'],\
['r','of|c|p','OFCP','(bOFCPc) x^ (cHCPb)'],\
['r','of|f|a','OFFA','((bOFFAc) x^ (bIRc)) & (bId) & (d=part|f)'],\
['r','of|f|m','OFFM','((bOFFMc) x^ (bIc)) & ((bOFFMc) t^ ((bId) & (cIe))) & (d=familial part|a) & (e=concept)'],\
['g','of|g','OFG','(of|g=OFG) & ((cOFGb) x^ ((bHc) ed^ (bOWNc) ed^ (bWc)))'],\
['r','of|i','OFI','(bOFIc) x^ (cHGCb)'],\
['r','of|i|m','OFIM','((bOFIMc) x^ (cHIMb))'],\
['r','of|m','OFM','(of|m=OFM) & (d=person) & ((bOFMc) x^ ((bSz) & (cWb) & (cId)))'],\
['r','of|p|w','OFPW','((bOFPWc) x^ (bPc)) & (bId) & (d=part|w)'],\
['r','of|r','OFQ','(of|r=OF) & (verbal counterpart=VCP) & (((R VCP b) & (The b OF d)) x^ (d R))'],\
['r','of|s','OFS','(of|s=OFS) & ((bOFSc) x^ (cHGb))'],\
['r','of|s|p','OFSP','(bOFSPc) x^ (cHSPb)'],\
['aa','omnipotent',None,'postponed'],\
['r','on','ON','(on=ON) & ((bONc) x^ ((bABc) & (bNXTc)))'],\
['ns','one|p',None,'(one|p = person)'],\
['a','open|r',None,'(b=open|r) & ((pJb) x^ ((pPc) & (nt+pPd) & (p~IRe) & (nt+p~IRe))) & (e=reality|t)'],\
['r','opposite to','OPP','(opposite to=OPP) & ((bOPPc) x^ ((dFRAb) & (dFRAc))) & (dIf) & (bIg) & (cIg) & (f=point) & (g=natural whole)'],\
['r','outside of','OT','(outside of=OT) & ((bOTc) x^ ((b~INc) & (bSz)))'],\
['ra','own','OWN','postponed'],\
['r','own|i','OWI','(own|i=OWI) & ((bOWIc) t^ (cMz))'],\
['ra','owns','OWN','postponed'],\
['n','pain',None,'(c=pain) & (((bIc) & (bTOd)) x^ ((zb^bOy) & (dWb) & (d~Dz)))'],\
['ns','part|d',None,'(part|d=property part)'],\
['n','part|c',None,'(c=part|c) & ((bIc) x^ ((dWb) x^ (dCSEe)))'],\
['ns','part|f',None,'(part|f=familial part)'],\
['n','part|s',None,'(c=part|s) & ((bIc) x^ (bINd))'],\
['ns','part|s',None,'(part|s=physical spatial part)'],\
['a','partially material|a (property)',None,'(b=partially material|a) & ((cJb) x^ ((dWf) & (fIg) & (dJc) & (dWh) & (hIk))) & ((cIb) t^ (cIe)) & (e=property) & (g=body|c) & (k=mind)'],\
['','partially material|b (concept)',None,'(b=partially material|a) & ((cJb) x^ ((dWf) & (fIg) & (dIc) & (dWh) & (hIk))) & (g=body|c) & (k=mind)'],\
['ns','partially spiritual',None,'(partially spiritual = partially material|b)'],\
['r','participate','PRTC','(bPRTCc) x^ ((dCAUSc) x^ (dWb))'],\
['na','party',None,'postponed'],\
['a','past',None,'(c=past) & (d=now) & ((bJc) x^ (dAb))'],\
['ns','past|e',None,'(past|e=entire past)'],\
['n','period|d (discontiguous)',None,'(c=period|d) & ((bIc) x^ ((bWd) t^ (dIe))) & (e=moment)'],\
['n','period (contiguous)',None,'(c=period) & ((bIc) x^ (((kAf) & (hAk)) x^ (bWk)))'],\
['as','permitted',None,'(permitted = morally contingent)'],\
['as','permitted|l',None,'(permitted|l=legally contingent)'],\
['n','person',None,'(c=person) & (d=personhood) & ((bIc) x^ (bHd))'],\
['n','personhood',None,'(c=personhood) & ((bHc) t^ ((bId) & (zTKw) & (zDx) & (bWz) & (bWy) & (yIe))) & (d=person) & (e=body|c)'],\
['n','phenomenon',None,'(c=phenomenon) & (d=event) & ((bIc) x^ ((bId) & (zIb)))'],\
['ns','phenomenon|e',None,'(phenomenon|e=event)'],\
['n','phenomenon',None,'(phenomenon = thing)'],\
['ra','phrase',None,'postponed'],\
['a','physical|s',None,'(c=physical|s) & ((bJc) x^ (((dHe) & (eIg) & (dSf)) t^ (bWf))) & (g=energy)'],\
['r','physical contingent condition','CC','(contingent physical condition=CC) & (given=GV) & (e=reality) & (f=possible worlds) & (((bScTd) & (eScTf) & (pCCq GVr)) x^ ((pb^eSc) & (qb^bSc) & (fSUTz) & (zSUTd) & (((rIRe) & (pTd)) t^ ((qPy Tz) & (nt+qP x Tz))) & (((rIRe) & (p~Td)) t^ ((qPw Tz) & (nt+qPv Tz))) & (pP mn f) & (wNr) & (vNq) & (yNs) & (xNt) & (rGq) & (tGs)))'],\
['n','physical law',None,'(c=physical law) & (d=situation) & ((bIc) x^ ((bPo) & (bId)))'],\
['n','physical relationship',None,'(z=physical relationship) & (y=subject) & (x=relationship) & ((bIz) x^ ((bHVc) & (bIx) & (cIy) & (eHc) & (eSf)))'],\
['n','physical spatial part',None,'(c=physical spatial part) & (((bIc) & (bOFd)) x^ ((bSz) & (dSy) & (zINy)))'],\
['n','physical spatial whole',None,'(c=physical spatial whole) & (((bIc) & (bOFd)) x^ ((bSz) & (dSy) & (yINz)))'],\
['n','physical temporal part',None,'(c=physical temporal part) & (((bIc) & (bOFd)) x^ ((bTz) & (dTy) & (zDURy)))'],\
['n','physical temporal whole',None,'(c=physical temporal whole) & (((bIc) & (bOFd)) x^ ((bTz) & (dTy) & (yDURz)))'],\
['a','physically contingent',None,'(b=physically contingent) & (c=relata) & (d=reality) & (((pSeTf) u+ (qJb Tg)) x^ (((pSeTf) t^ ((qPx Tg) & (q~Pw Tg))) & (ySUTg) &  (gSUTf)))'],\
['a','physically impossible',None,'(b=physically impossible) & (c=relata) & (d=reality) & (((pSeTf) u+ (qJb Tg)) x^ (((pSeTf) t^ ((q~Po Tg) & (nt+qPo Tg))) & (zCRRq) & (z~IRd Ty) & (ySUTg) & (gSUTf)))'],\
['a','physically necessary',None,'(b=physically necessary) & (c=relata) & (d=reality) & (succeed|t=SUT) & (correspond=CRR) & (((pSeTf) u+ (qJb Tg)) x^ (((pSeTf) t^ ((qPo Tg) & (nt+q~Po Tg) & (zIRd Ty))) & (zCRRq) & (ySUTg) & (gSUTf)))'],\
['a','physically possible',None,'(b=physically possible) & (c=physically necessary) & (d=physically contingent) & ((pJb) x^ ((pJc) ed^ (pJd)))'],\
['ns','place',None,'(place=region)'],\
['n','plan',None,'(c=plan) & ((bIc) x^ ((bDz) & (bBy))) & (zb^bCAUc) & (yb^zPx)'],\
['n','pleasure',None,'(c=pleasure) & (((bIc) & (bTOd)) x^ ((zb^bOy) & (dWb) & (bDd)))'],\
['r','plural counterpart','PCP','(plural counterpart=PCP) & (d=plural) & (e=singular) & (f=root word) & (((bId) & (bOFc)) x^ ((cIe) & (bIz) & (cIz) & (zIf) & (mny bEXV)) x^ (bPCPc))'],\
['n','plural counterpart of',None,'(e=plural counterpart) & ((bPCPc) x^ ((bIe) & (bOFc)))'],\
['n','point|s',None,'(c=point|s) & (((bIc)) t^ ((dLb) & (bLe) & (((zLd) & (eLz)) t^ (z=b))))'],\
['a','positively infinite|g',None,'(c=positively infinite|g) & (((bJc) & (bPCPd)) x^ (((zId) & (zNy)) t^ ((xId) & (xNw) & (wGy))))'],\
['a','potentially|o vague (of a physical object)',None,'(b=potentially|o) & ((cJb) x^ (cJd)) & (d=natural|o)'],\
['a','potentially|p vague (of a property)',None,'(b=potentially|p) & (((cJb) & (dJc)) x^ (dJe)) & (e=natural|o)'],\
['a','potentially|r vague (of a relation)',None,'(b=potentially|r) & (((R Jb) & (cRd)) x^ ((cJe) & (dJe))) & (e=natural|o)'],\
['a','potentially|v vague (of a statement)',None,'(b=potentially|v) & ((cJb) x^ (cJd)) & (d=natural|s)'],\
['as','precise',None,'(precise = certain)'],\
['a','predicable',None,'(c=predicable) & ((bJc) & (bOFd)) x^ (fJg)) & (b=Re) & (fb^dRe) & (g=consistent)'],\
['n','predicate',None,'(c=predicate) & ((bIc) x^ ((cWd.e) & (dIf) & (eIg))) & (f=relation) & (g=object)'],\
['r','predicates',None,'((bPRCc) x^ (cRd)) & (b=Rd)'],\
['n','premise',None,'(c=premise) & (((bIc) & (bFORd)) x^ (((eIf) t^ (enf^b)) & (gWb) & (gi^d)))'],\
['a','present|a',None,'(c=present|a) & (d=present) & ((cACPd))'],\
['r','prevent','PRV','(prevent=PRV) & ((bPRVc) x^ ((xCRRc) & ((bSzTy) t^ (x~Po Tw)) & (wSUTy)))'],\
['n','probability',None,'(c=probability) & (g=ratio) & (h=possible worlds) & (f=reality) & (given=GV) & (((bIc) & (bOFd GVe)) x^ ((eIRf) t^ ((dPb h) & (bIg))))'],\
['a','probable',None,'(c=probable) & ((bJc) x^ (jGk)) & ((eWd) x^ (bPd)) & ((gWh) x^ (b~Ph)) & (gNj) & (eNk)'],\
['n','proper name',None,'(c=proper name) & ((bIc) x^ ((bId) & (bRFe) & (eIf))) & (d=word) & (f=individual)'],\
['n','property|o',None,'(c=property|o) & ((bIc) x^ (zOWNb))'],\
['n','property bearer',None,'(c=property bearer) & ((bIc) x^ (bHz))'],\
['n','property part',None,'(c=property part) & (((bIc) & (bOFd)) x^ ((dHb) ed^ (dJb)))'],\
['ra','punish',None,'postponed'],\
['a','purely material|c (concept|n)',None,'(b=purely material|c) & ((cJb) x^ ((dWf) & (dIc) & (fIg) & ((hIk) t^ (d~Wh)))) & ((cJb) t^ (cIe)) & (e=concept|n) & (g=body|c) & (k=mind)'],\
['n','putative mistake',None,'(d=putative mistake) & (e=reality) & (make=MK) & ((yb^cCAz) & (wb^yIe) & (((bMKc) & (cTOb) & (cId)) x^ ((bCAc Tw) & (zOC Tv) & (vSUTw) & ((yIe) ed^ ((yMx) & (bWx))) & (bBw) & (b~Dz))))'],\
['e','putatively',None,'(putatively b TOc) x^ (cBb)'],\
['n','quantity',None,'(c=quantity) & (((bIc) & (bOFd) & (dPCPe)) x^ ((zIe) & (zNb) & (zJf) & (((yIe) & (yNw)) t^ (w~Gb))))'],\
['r','raise the probability of','RAS','(raise the probability of=RAS) & ((bRASc) x^ (bCASc))'],\
['ra','ratio',None,'postponed'],\
['a','real|c',None,'(c=real|c) & ((bJc) x^ (bHCEd))'],\
['as','real',None,'(real=actual)'],\
['ns','real|s',None,'(real|s = physical|s)'],\
['n','real group',None,'(c=real group) & (d=abstractspace) & (vb^(xIb) e^ (xHw)) & ((bIc) x^ ((zIb) & (yIb) & (vIRd)))'],\
['ra','real time',None,'postponed'],\
['es','really',None,'(really=actually)'],\
['r','refer','RF','((bRFc) x^ ((mTn) t^ ((jTq) & (qAn))) & (db^bJf) & (hb^cJf) & (jb^kTKh) & (mb^kEXPd) & (f=extant)'],\
['n','region|a',None,'(c=region|a) & ((bIc) x^ (dINEb))'],\
['n','region|n',None,'(c=region|n) & ((bIc) x^ (dINMb))'],\
['n','relation|n',None,'(bIc) x^ ((dWb.c) & (bIe) & (cIf) & (dIh) & (dJj))) & (e=noun) & (f=relation) & (h=word) & (j=root)'],\
['na','relationship',None,'(c=relationship) & ((bIc) x^ ((bId) ed^ (bIe))) & ((bIc) x^ (bTf)) & (d=explicit|e relationship|e) & (e=implicit|i relationship|i)'],\
['rxd','resemble','RES','(b and|c cRES) x^ (bRSc)'],\
['r','resembles','RS','((bRSc) x^ (((dWe) x^ ((bJe) & (cJe))) & (dJf))) & (f=many|a)'],\
['a','respect|p',None,'postponed'],\
['r','right|a of','RIG','(right|a of=RIG) & ((bRIGc) x^ ((bSz) & (cLz)))'],\
['r','right|b','RTE','(right|b of=RTE) & ((bRTEc) x^ ((cSz) & (zLb)))'],\
['r','right|m of','RGT','(right|m of=RGT) & ((bRGTc) x^ ((bSz) & (cSy) & (yLz)))'],\
['r','satisfy',None,'(((bSTSc) & (cId) & (c=Re)) x^ (bRe)) & (d=predicate)'],\
['r','seem','SM','(seem=SM) & (z=reality) & ((bSM TOc) x^ ((zIc) & (zBp) & (p~IRz)))'],\
['rs','sense ',None,'(sense=EXP)'],\
['ns','sentence|r',None,'(sentence|r=relationship)'],\
['n','sentient being',None,'(sentient being = living being)'],\
['d','seventy five percent',None,'((75% b R c) x^ (k=3*j)) & ((eWg) x^ (gRc)) & ((hWm) x^ (m~Rc)) & (gIb) & (mIb) & (hNj) & (eNk))'],\
['r','share','SHR','(share=SHR) & ((b and|c cSHRd) x^ (((bHd) & (cHd)) ed^ ((bOWNd) & (cOWNd)) ed^ ((bWd) & (cWd))))'],\
['a','significant',None,'(b=significant) & (c=grammatical) & ((pJb) x^ ((pJta^) & (pJc)))'],\
['r','similar to','SML','(similar to=SML) & (d=essence) & ((bSMLc) x^ ((bHz) & (zId) & (cH mn y) & (yIz)))'],\
['n','simple individual',None,'(c=simple individual) & ((bIc) x^ ((bSz) & ((ySx) t^ (x~INz))))'],\
['r','simultaneous with','SIM','(simultaneous with=SIM) & ((bSIMc) x^ ((bTz) & (cTz)))'],\
['n','situation',None,'(b=situation) & (c=relationship) & (d=relata) & (have=HV) & ((pIb) x^ ((pIc) & (zId) & (pHVz) & (zSy)))'],\
['ns','sort',None,'(sort=type)'],\
['nub','space',None,'(b=space) x^ ((cSd) x^ (bWd))'],\
['ns','space|r ',None,'(space|r=region)'],\
['ns','species ',None,'(species=kind)'],\
['ns','state',None,'(state=property)'],\
['r','state','STT','(state|s=STT) & ((bSTTc) x^ ((bCAUz) & (zRFc)))'],\
['n','state of affairs',None,'(c=state of affairs) & ((bIc) x^ ((bWd) x^ ((dJe) & (dIf)))) & (f=fact)'],\
['ns','statement',None,'(statement=relationship)'],\
['rs','states',None,'(states = STT)'],\
['r','stronger than','STR','(stronger than=STR) & (f=reality) & (zb^(eIRf) u+ (dCAb)) & (yb^(eIRf) u+ (dCAc)) & (((bSTRc GVe) & (dDb) & (dDc)) x^ ((zPx) & (yPw) & (wNv) & (xNu) & (uGv)))'],\
['ns','subgroup',None,'(subgroup=type)'],\
['n','subject',None,'(c=subject) & (d=relation) & (e=noun) & ((bIc) x^ ((zId) & (bIe) & (zAWb)))'],\
['a','succeeding',None,'(c=succeeding) & ((bJc * d) x^ (bAd))'],\
['a','succeeding|n',None,'(c=succeeding|n) & ((bJc * d) x^ (bGd))'],\
['r','succeeds','SC','(succeeds=SC) & ((bSCc) x^ ((dNe) t^ ~((dGc) & (bGe))))'],\
['r','succeeds|m','SCM','(succeed|m=SCM) & (bSCMc) x^ ((cId) & (bId) & (cMTL Te) & (bMTL Tf) & (fAe))'],\
['r','succeeds|o','SUO','(succeed|o=SUO) & ((bSUOc) x^ ((cOC Td) & (bOC Te) & (bIf) & (cIf) & (eAd) & ((gIf Th) t^ ~((eAh) & (hAd)))))'],\
['r','succeeds|p','SCP','(succeed|p=SCP) & ((bSCPc ASCd) x^ ((c=d Te) & (b=d Tf) & (fAe) & ((g=d Th) t^ (h~CBTf e))))'],\
['r','succeeds|s','SCD','(succeed|s=SCD) & ((bSCDc ASCd) x^ ((bId) & (cId) & (bSe) & (cSf) & (eDf) & ((gId) t^ ~((fDg) & (gDe)))))'],\
['r','succeeds|t','SUT','(succeed|t=SUT) & ((bSUTc ASCd) x^ ((eTb) & (fTc) & (bAc) & ((gTh) t^ ~((bAh) & (hAc)))))'],\
['r','succeeds|u','SCU','(succeed|u=SCU) & ((bSCUc) x^ ((dUTc Te) & (fUTb Tf) & ((f=d) ed^ (f~=d)) & (bIg) & (cIg) & (((hUTm Tj) & (mIg)) t^ ~((fAj) & (jAe)))))'],\
['as','supernatural',None,'(supernatural=divine)'],\
['n','symbol',None,'(c=symbol) & ((bIc) x^ (bRFz))'],\
['a','teleologically contingent',None,'(b=teleologically contingent) & (((cDd) & (pJb c)) x^ (((c~CAUp Tx) t^ ((dPu Tw) & (d~Pv))) & ((cCAUp Tx) t^ ((dPz Tw) & (d~Py Tw)))))'],\
['a','teleologically impossible',None,'(b=teleologically impossible) & (((cDd) & (pJb c)) x^ (((cCAUp Tx) t^ (d~Po Tw)) & ((c~CAUp Tx) t^ ((dPz Tw) & (d~Py Tw)))))'],\
['a','teleologically necessary',None,'(b=teleologicallynecessary) & (((cDd) & (pJb c)) x^ (((c~CAUp Tx) t^ (d~Po Tw)) & ((cCAUp Tx) t^ ((dPz Tw) & (d~Py Tw)))))'],\
['a','teleologically possible',None,'(b=teleologically possible) & (c=teleologically necessary) & (d=teleologically contingent) & ((pJb) x^ ((pJc) ed^ (pJd)))'],\
['r','tend toward','TD','postponed'],\
['rs','think|t','TKT','(TKT = B)'],\
['r','think|w','TKW','((bTKWc) x^ ((bWd) & (dTKc)))'],\
['nu','time',None,'(b=time) x^ ((eTd) x^ (bWd))'],\
['ra','took','TAK','postponed'],\
['ns','trait ',None,'(trait=property)'],\
['a','true',None,'(c=true) & ((bJc) x^ (bIRe)) & ((bJc) t^ (bIf)) & (e=reality) & (f=non_meta_statement)'],\
['n','truth value',None,'(c=truth value) & (e=truth) & (f=falsehood) & ((bIc) x^ ((bc^e) & (bc^f)))'],\
['r','try','TRY','(try=TRY) & (d=reality) & ((bTRYc) x^ ((uCRRc) & (bCAUy) & ((yIRd) t^ ((uPw) & (nt+uPv))) & (xb^yCAUc) & (bBx) & (bDc)))'],\
['n','type',None,'(c=type) & (((bIc) & (bOFd)) x^ ((zIb) t^ (zId)))'],\
['a','unacceptable',None,'(b=unacceptable) & ((pJb TO c) x^ ((zCRRp) & (yb^z~Po) & (cDy)))'],\
['as','uncertain',None,'(vague = uncertain)'],\
['a','unique',None,'(c=unique) & ((bJc) x^ ((dIe) t^ (d~Ib))) & (e=thing)'],\
['ra','universe',None,'postponed'],\
['a','upper class',None,'(d=upper) & (c=class) & (f=abstract essence) & (((bIc) & (bJd) & (eIb)) x^ (((zIe) x^ (zHy)) & (yIf) & (((xIe) & (o~Ix)) t^ (xSw))))'],\
['ra','utters','UT','postponed'],\
['a','vague',None,'(b=vague) & (((cJb) & (cTOd Tg)) x^ ((dTKe Tg) & (kAg) & (dTKm))) & (f=reality) & (g=now) & (eb^cIRf) & (hb^d~TKe Tk) & (mb^hPj)'],\
['a','vague|o (of a physical object)',None,'(b=vague|o) & (((cJb) & (cTOd)) x^ ((d~KNe) & (fJg))) & (e b^ fIc) & (g=natural)'],\
['a','vague|s (of a statement)',None,'(b=vague) & (((cJb) & (cTOd)) x^ ((cJe) & (d~KNc))) & (e=natural|s)'],\
['na','vague pairs',None,'postponed'],\
['r','variable space relation','D','(bDc) x^ ((bLc) ed^ (bRTc) ed^ (bABc) ed^ (bBLc) ed^ (bFc) ed^ (bBHc))'],\
['r','violate','VIO','(violate=VIO) & (b=action) & ((pVIOq) x^ ((zDy) & (yb^q~Po) & (pCRRq) & (pIRb) & (pIb)))'],\
['n','void',None,'((b=void) x^ ((cIz) t^ (c~Sb))) & (z=thing)'],\
['ra','went','GO','(GO = MOV)'],\
['rs','were|e',None,'(were|e = EX)'],\
['r','were/would',None,'(((p were) t^ (q would)) x^ ((p~IRb) & (q~IRb) & ((pPc) t^ (qPc)))) & (b=reality)'],\
['rs','while',None,'(while=DUR)'],\
['ns','while|n ',None,'(while|n=period)'],\
['aa','white',None,'postponed'],\
['n','whole|l (living)',None,'(c=whole|l) & ((bIc) x^ ((bWd) t^ ((dIe) ed^ (dIf)))) & (e=mind) & (f=whole|m)'],\
['ns','whole|m (material)',None,'(whole|m = body|c)'],\
['n','whole|n (numerical)',None,'(c=whole|n) & ((bIc) x^ ((bWd) t^ (dIe))) & (e=number)'],\
['n','whole|s (spatial)',None,'(c=whole|s) & ((bIc) x^ ((bWd) t^ (dIe))) & (e=point)'],\
['ns','whole|t (temporal)',None,'(whole|t = period|d)'],\
['ns','whole|v (verbal)',None,'(whole|v = word)'],\
['rs','within',None,'(within = in|e)'],\
['n','word',None,'(c=word) & ((bIc) t^ (((bWd) t^ (dIe)) & (bIf))) & (f=symbol) & (e=letter)'],\
['ns','numbers|i',None,'(numbers|i = integer)'],\
['na','7pm',None,'postponed'],\
['na','apple',None,'postponed'],\
['a','aristotelian|c',None,'(c=aristotelian|c) & (d=aristotle) & ((bJc) x^ (bSMLd)) '],\
['n','aristotelianness',None,'((b=aristotelianness) x^ (cHb)) & (c=Aristotle)'],\
['ra','ate','ATE','postponed'],\
['ra','ate from','ATF','postponed'],\
['na','ball',None,'postponed'],\
['ra','bark','BRK','postponed'],\
['ra','barks','BRK','postponed'],\
['na','beer',None,'postponed'],\
['ra','born','BRN','postponed'],\
['na','boy',None,'postponed'],\
['ra','broke','BRK','postponed'],\
['na','cake',None,'postponed'],\
['na','car',None,'postponed'],\
['na','casablanca',None,'postponed'],\
['na','cat',None,'postponed'],\
['aa','caught',None,'postponed'],\
['n','chlorophyll',None,'(c=chlorophyll) & ((bIc) t^ (b~Id)) & (d=plastic)'],\
['aa','cold',None,'postponed'],\
['na','courtyard',None,'postponed'],\
['ra','danced','DNC','postponed'],\
['nc','dog',None,'(c=dog) & (d=doglike) & ((bIc) x^ (bJd))'],\
['ac','doglike',None,'(c=dog) & (d=doglike) & ((bJd) x^ ((bIc) & (bWe) & (bWg) & (eIh) & (gIk))) & (k=mind) & (h=body|c)'],\
['n','doglike|s',None,'(c=doglike|s) & (d=doglike) & ((bJc) x^ ((eJd) & (eSMLb)))'],\
['na','dogness',None,'(c=dogness) & ((bHc) x^ (bJd)) & (d=doglike)'],\
['na','door',None,'postponed'],\
['ra','drank','DRK','postponed'],\
['ra','drink','DRK','postponed'],\
['ra','drinks','DRK','postponed'],\
['na','earth',None,'postponed'],\
['ra','eat from','ATF','postponed'],\
['ra','echolocate','ECH','postponed'],\
['ra','echolocates','ECH','postponed'],\
['na','eiffel tower',None,'(c=eiffel tower) & (d=artificial) & ((bJc) t^ (bJd))'],\
['na','eye',None,'(c=eye) & (d=natural) & ((bJc) t^ (bJd))'],\
['n','female',None,'(b=male) & (c=female) & ((dJc) t^ (d~Jb))'],\
['a','feminine',None,'(b=feminine) & (c=female) & ((dJb) x^ (dIc))'],\
['a','feminine|s',None,'(b=feminine|s) & (c=female) & (((dJb) & (eIc)) x^ (dSMLe))'],\
['n','flower',None,'(c=flower) & ((bIc) t^ ((bWd) & (dIe))) & (e=chlorophyll)'],\
['na','french',None,'postponed'],\
['na','girl',None,'postponed'],\
['aa','green',None,'postponed'],\
['na','hamlet',None,'postponed'],\
['na','head',None,'(e=natural) & (d=head) & ((bHd) t^ (bJe))'],\
['na','heaven',None,'postponed'],\
['a','hirsute',None,'(c=hirsute) & (d=hairs) & ((bJc SeTf) x^ (bW mn dSeTf))'],\
['na','home',None,'postponed'],\
['na','house',None,'postponed'],\
['n','hydrogen',None,'natural'],\
['n','kennedy',None,'(b=kennedy) & ((cIb) t^ (bId)) & (d=family)'],\
['a','kennedy|a',None,'(b=kennedy|a) & (c=kennedy) & (((eJb) & (fIe)) x^ (fIc))'],\
['ra','kiss','KS','postponed'],\
['ra','kissed','KS','postponed'],\
['na','male',None,'(b=male) & (c=female) & ((dJb) t^ (d~Jc))'],\
['ra','love','LOV','postponed'],\
['na','mammal',None,'postponed'],\
['n','man',None,'(b=man) & ((cIb) x^ ((cId) & (cJe))) & (d=person) & (e=male)'],\
['na','mars',None,'natural'],\
['na','moon',None,'postponed'],\
['na','movie',None,'postponed'],\
['na','munich',None,'postponed'],\
['na','nazi',None,'postponed'],\
['na','north america',None,'postponed'],\
['na','paris',None,'(c=paris) & (d=artificial) & ((bIc) t^ (bJd))'],\
['n','pocketwatch',None,'postponed'],\
['na','pyramid',None,'postponed'],\
['na','rain',None,'postponed'],\
['ra','raining','RAI','postponed'],\
['ra','rains','RAI','postponed'],\
['ra','reads','RD','postponed'],\
['a','red',None,'(c=red) & ((bJc) t^ (bINMd))'],\
['n','redness',None,'(c=redness) & ((bHc) x^ (bJd)) & (d=red)'],\
['na','reptile',None,'postponed'],\
['aa','rewarded',None,'postponed'],\
['a','ridiculous',None,'postponed'],\
['na','rocky mountains',None,'postponed'],\
['na','round square',None,'postponed'],\
['na','russian',None,'postponed'],\
['ra','saw','SEE','postponed'],\
['ra','see','SEE','postponed'],\
['na','set theory',None,'postponed'],\
['ra','shed','SHD','postponed'],\
['ra','sleep','SLP','postponed'],\
['ra','sleeps','SLP','postponed'],\
['aa','smart',None,'postponed'],\
['r','smell','SME','((bSME) t^ (bJc)) & (c=material)'],\
['r','smells','SME','((bSME) t^ (bJc)) & (c=material)'],\
['ra','speak','SPK','postponed'],\
['na','speed limit',None,'postponed'],\
['ra','spied on','SPD','postponed'],\
['ra','spies on','SPD','postponed'],\
['ra','spoke','SPK','postponed'],\
['na','sprite',None,'(c=sprite) & (d=artificial) & ((bJc) t^ (bJd))'],\
['ra','standing','STD','postponed'],\
['ra','studied','STD','postponed'],\
['n','table',None,'artificial'],\
['na','table',None,'(c=table) & (d=artificial) & ((bJc) t^ (bJd))'],\
['ra','talked','TLK','postponed'],\
['ra','teach','TCH','postponed'],\
['na','teacher',None,'postponed'],\
['ra','teaches','TCH','postponed'],\
['na','tear',None,'postponed'],\
['ra','top',None,'postponed'],\
['na','uk prime minister',None,'postponed'],\
['na','us president',None,'postponed'],\
['na','van',None,'postponed'],\
['na','water',None,'postponed'],\
['na','wine',None,'postponed'],\
['n','woman',None,'(b=woman) & ((cIb) t^ ((cId) & (cJe))) & (d=person) & (e=female)'],\
['ns','beers',None,'(beers=beer)'],\
['ns','cars',None,'(cars=car)'],\
['ns','cats',None,'(cats=cat)'],\
['ns','concepts',None,'(concepts=concept)'],\
['ns','dogs',None,'(dogs=dog)'],\
['ns','eiffel towers',None,'(eiffel towers=eiffel tower)'],\
['ns','eyes',None,'(eyes=eye)'],\
['ns','girls',None,'(girls=girl)'],\
['ns','groups',None,'(groups=whole)'],\
['ns','groups|c',None,'(groups|c=group|c)'],\
['ns','hydrogens',None,'(hydrogens=hydrogen)'],\
['ns','instances',None,'(instances=instance)'],\
['ns','integers',None,'(integers=integer)'],\
['ns','mammals',None,'(mammals=mammal)'],\
['ns','members',None,'(members=part)'],\
['ns','members|i',None,'(members|i=instance)'],\
['ns','men',None,'(men=man)'],\
['ns','minds',None,'(minds=mind)'],\
['ns','moments',None,'(moments=moment)'],\
['ns','moons',None,'(moons=moon)'],\
['ns','parts',None,'(parts=part)'],\
['ns','people',None,'(people=person)'],\
['ns','points',None,'(points=point)'],\
['ns','pyramids',None,'(pyramids=pyramid)'],\
['ns','reptiles',None,'(reptiles=reptile)'],\
['ns','russians',None,'(russians=russian)'],\
['ns','tears',None,'(tears=tear)'],\
['ns','thoughts',None,'(thoughts=thought)'],\
['ns','us presidents',None,'(us presidents=us president)'],\
['ns','wholes',None,'(wholes=whole)'],\
['nun','ada',None,'((b=ada) t^ ((bIc) & (bId))) & (c=woman) & (d=individual)'],\
['nun','aristotle',None,'((b=aristotle) t^ ((bIc) & (bId))) & (c=man) & (d=individual)'],\
['nun','diane',None,'((b=diane) t^ ((bIc) & (bId))) & (c=woman) & (d=individual)'],\
['nun','jack',None,'((b=jack) t^ ((bIc) & (bId))) & (c=man) & (d=individual)'],\
['nun','jessica',None,'((b=jessica) t^ ((bIc) & (bId))) & (c=woman) & (d=individual)'],\
['nun','jfk',None,'((b=jfk) t^ ((bIc) & (bId))) & (c=man) & (d=individual)'],\
['nun','jim',None,'((b=jim) t^ ((bIc) & (bId))) & (c=man) & (d=individual)'],\
['nun','julius caesar',None,'((b=julius caesar) t^ ((bIc) & (bId))) & (c=man) & (d=individual)'],\
['nun','kiera knightley',None,'((b=kiera knightley) t^ ((bIc) & (bId))) & (c=woman) & (d=individual)'],\
['nun','leibniz',None,'((b=leibniz) t^ ((bIc) & (bId))) & (c=man) & (d=individual)'],\
['nun','marilyn',None,'((b=marilyn) t^ ((bIc) & (bId))) & (c=woman) & (d=individual)'],\
['nun','plato',None,'((b=plato) t^ ((bIc) & (bId))) & (c=man) & (d=individual)'],\
['nun','russell',None,'((b=russell) t^ ((bIc) & (bId))) & (c=man) & (d=individual)'],\
['nun','socrates',None,'((b=socrates) t^ ((bIc) & (bId))) & (c=man) & (d=individual)'],\
['nun','xenothon',None,'((b=xenothon) t^ ((bIc) & (bId))) & (c=man) & (d=individual)'],\
['ra','am|e','EX','(am=EX)'],\
['ra','are|e','EX','(are|g=EX)'],\
['ra','be|a','J','(be|a=J)'],\
['r','belongs to','BLN','(bBLNc) x^ (cWb)'],\
['rbi','desires','D','(desires=D)'],\
['ra','has','H','(has=H)'],\
['rbi','have|w','W','(have|w=W)'],\
['rbi','is|a ','J','(is|a=J)'],\
['rbi','is|g ','I','(is|g=I)'],\
['r','participated','PRTC','(bPRTCc) x^ ((dCAUSc) x^ (dWb))'],\
['r','participates','PRTC','(bPRTCc) x^ ((dCAUSc) x^ (dWb))'],\
['rai','think','TK','(think=TK)'],\
['rai','thinks','TK','(thinks=TK)'],\
['ra','was','=','(was = =)'],\
['ra','was|a','J','(was|a=J)'],\
['ra','was|g','I','(was|g=I)'],\
['ra','was|e','EX','(was|e = EX)'],\
['ns','whole|c (fallacious)',None,'(whole|c = concept|n)'],\
['','',None,''],\
['','',None,''],\
['','',None,''],\
['r','absorb|g','ADS','(bADSc) x^ ((b.eId) & (fINHh) & (bWh) & (cCRCf) & (fIg))) & (d=body|c) & (g=body|m)'],\
['r','correspond','CRA','(bCRAc) x^ (((bEMh Td) & (eADc Tf) & (bSg Td)) t^ ((cOj Tf) & (fSUTd))))'],\
['r','correspond|b','CRB','(bCRBc) x^ (((dEMe Tf) & (gADe Th) & (dSb Tf)) t^ ((jOc Tf) & (hSUTf))))'],\
['r','correspond|c','CRC','(bCRCc) x^ (((bWd) x^ (dINMe)) & ((cWf) x^ (fINHg)) & ((bWh) t^ ((hCRAj) & (cWj))) & ((cWk) t^ ((mCRAk) & (bWm))))) '],\
['r','experience','EXP','(bEXPc Tg) x^ ((bADSd Th) t^ ((bTKc Tg) & (cIRf) & (gSUTh))) & (cb^dRe)'],\
['r','in|h','INH','(bINHc) x^ ((bWd) x^ ((dOe) & (cWe)))'],\
['r','misinterpret','MSI','(bMSIc Tg) x^ ((bADSd Th) t^ ((bTKc Tg) & (c~IRf) & (gSUTh))) & (cb^dRe)'],\
['r','think|d','TKD','(bTKDc) x^ (cIRd)'],\
['n','body|m',None,'(c=body|m) & ((bIc) x^ ((bWd) t^ (dIe))) & (e=particle|m)'],\
['n','boson',None,'(c=boson) & ((bIc) x^ (dEMb)) & ((bIc) x^ (eADb)) & ((bIc) t^ (bIg)) & (g=particle)'],\
['n','fermion',None,'(c=fermion) & ((bIc) x^ (bEMd)) & ((bIc) x^ (bADe)) & ((bIc) t^ (bIg)) & (g=particle)'],\
['rs','perceive',None,'(perceive = absorb|g)'],\
['r','hallucinate','HLC','(bHLCc Td) x^ ((bEMSe Tf) t^ ((bTKk Tg) & (gSUTf) & (cJj) & (c~IRh))) & (j=natural|s) & (kb^cIRh)'],\
['r','emit|s','EMS','(bEMSc) x^ ((cWd) x^ ((eEMd) & (bWe)))'],\
['rb','absorb','AD','(c=boson) & ((bIc) x^ (eADb)) & ((eId) x^ (eADf)) & (d=fermion)'],\
['rb','emit','EM','(c=fermion) & ((bIc) x^ (bEMd)) & (e=boson) & ((dIe) x^ (bEMd))'],\
['n','subset',None,'(c=subset) & (((bIc) & (bOFd)) x^ ((bWe) t^ (dWe)) & ((dWf) t^ ((gPh) & (nt+gPj))) & (gb^bWf)'],\
['n','superset',None,'(c=superset) & (((bIc) & (bOFd)) x^ ((dWe) t^ (bWe)) & ((bWf) t^ ((gPh) & (nt+gPj))) & (gb^dWf)'],\
['','',None,''],\
['','',None,''],\
['','',None,''],\
['','',None,''],\
['','',None,''],\
['','',None,''],\
['','',None,''],\
['','',None,''],\
['','',None,''],\
['','',None,''],\
['','',None,''],\
['','',None,''],\
['','',None,''],\
['','',None,''],\
['','',None,''],\
['','',None,''],\
['','',None,''],\
['','',None,''],\
['','',None,''],\
['','',None,''],\
['','',None,''],\
['','',None,''],\
['','',None,''],\
['','',None,''],\
['','',None,''],\
['','',None,''],\
['','',None,''],\
['','',None,''],\
['','',None,''],\
[None,None,None,None]]
    return dict2