def large_dict(str1):
    dict2= [['rbt','above','AB','((bIGc) x^ (dABb)) & ((bIGc) x^ (bABe)) & (c=point)'],\
['rbt','after|l','AL','((bIGc) x^ (dALb)) & ((bIGc) x^ (bALe)) & (c=letter)'],\
['rbt','after|n ','AF','((bIGc) x^ (dAFb)) & ((bIGc) x^ (bAFe)) & (c=number)'],\
['rbt','after ','A','((bIGc) x^ (dAb)) & ((bIGc) x^ (bAe)) & (c=moment)'],\
['rbi','and','&','((p&q) t^ (p.qIGb)) & (q~Ic) & (rPd) & (b=relationship) & (qb^p&~p) & (c=reality|t) & (rb^p&~q)'],\
['rbi','are|a','IA','((bIAc) x^ (cIGd)) & ((bIAc) t^ (bIGe)) & ((bIAc) t^ (cIGf)) & (d=property) & (e=thing) & (f=adjective)'],\
['rbi','are|g ','IG','((bIGc) x^ (cIGd)) & ((eIGf) x^ (eIGg)) & (d=concept|n) & (g=instance)'],\
['rbis','at','S','((bIGc) x^ (dSb)) & ((dIGf) x^ (dSb)) & (c=point) & (f=particle) '],\
['rbi','at|i ','AI','((dAIb) t^ (dIGc)) & ((bIGf) x^ (dAIb)) & (c=relationship) & (f=imagination) '],\
['rbi','at|n ','N','((bIGc) x^ (dNb)) & ((eIGf) x^ ((eNh) & (hAFg))) & ((jIGk) x^ (mNg)) & ((nIGo) x^ (nNp)) & (f=whole) & (c=number) & (g=1) & (k=individual) & (p=0) & (o=contradiction) '],\
['rbi','at|p ','P','((dPb) t^ (dIGc)) & ((bIGf) x^ (dPb)) & (c=relationship) & (f=possible world) '],\
['rbi','at|s ','SS','((bIGc) x^ (dSSb)) & ((dIGc) x^ (dSSb)) & (f=sensation) & (c=point|s) '],\
['rbit','at|t ','T','((dTb) t^ (dIGc)) & ((bIGf) x^ (dTb)) & (c=relationship) & (f=moment) '],\
['rbi','at|y','Z','((bIGc) x^ (dZb)) & (c=point|a)'],\
['rbi','desire','DS','((dDSb) t^ ((bIGc) & (bIAe))) & ((bIGf) x^ (dDSb)) & (c=relationship) & (f=mind) & (e=open|r)'],\
['r','have','H','((bHc) x^ (cIGd)) & ((bHc) t^ (bIGe)) & ((bHc) t^ (cIGf)) & (d=property|n) & (e=thing) & (f=noun)'],\
['rbi','has|w ','HW','((bIGc) x^ (bHWd)) & ((dIGe) x^ (bHWd)) & (d=whole) & (e=part)'],\
['rbi','in|o','I','((c=reality|t) x^ (pIc)) & ((dIGe) t^ (d~IGc)) & ((c=reality|t) t^ ((cIGf) & (cIGg))) & ((qIc) t^ (cHWq)) &  (e=thing) & (f=non_relationship) & (g=relationship)'],\
['rbts','in front of','FR','((bIGc) x^ (dFRb)) & ((bIGc) x^ (bFRe)) & (c=point)'],\
['rbi','is|v','IV','((bIVc) x^ (bIGd)) & ((bIVc) x^ (cIGf)) & ((bIVc) t^ (bIGe)) & (d=property|v) & (f=adverb) & (e=non_whole)'],\
['rbi','is|y','IY','((bIYc) x^ (cIGd)) & ((bIYc) x^ (cIGf)) & ((bIYc) t^ (bIGe)) & (d=property|d) & (f=determinative) & (e=non_whole)'],\
['rbts','left of','LF','((bIGc) x^ (dLFb)) & ((bIGc) x^ (bLFe)) & (c=point)'],\
['rbi','think about','TK','((bTKd) t^ (dIGc)) & ((bIGf) x^ (bTKd)) & (c=relationship) & (f=mind) '],\
['n','concept|n',None,'(c=concept|n) & ((bIGc) x^ (zIGb)) & ((bIGc) t^ (bIGe)) & (e=non_whole)'],\
['a','consistent',None,'(c=consistent) & ((pIAc) k^ (pPq)) & ((pIAc) t^ (pIGd)) & (d=relationship)'],\
['a','contradictory',None,'(c=contradictory) & ((pIAc) e^ ((nIGd) & (p~Pn))) & (d=possible world) & ((pIAc) t^ (pIGd)) & (d=relationship)'],\
['aa','extant',None,'((bIAc) t^ (cIGd)) & (d=property)'],\
['n','fact',None,'(c=fact) & ((bIGc) x^ (bId)) & ((bIGc) t^ (bIGe)) & (((hAg) & (bIGc)) t^ (b~Id Th)) & (d=reality) & (e=relationship) & (g=now)'],\
['na','here',None,'(b=here) t^ (cSb)'],\
['n','imagination',None,'(c=imagination) & ((bIGc) x^ (dAIb)) & ((bIGc) t^ (bIGf)) & (f=non_relationship)'],\
['n','instance',None,'(c=instance) & ((bIGc) x^ (bIGd))'],\
['n','integer',None,'(c=integer) & ((bIGc) x^ (bAFd)) & ((bIGc) x^ (eAFb)) & ((bIGc) x^ (fNb)) & ((bIGc) t^ (bIGg)) & (g=non_whole)'],\
['n','letter',None,'(c=letter) & ((bIGc) x^ ((dPe) & (jPg))) & ((bIGc) t^ (bIGm)) & (hIGc) & (db^bALh) & (jb^(kIGc) t^ (k~ALb)) & (m=non_whole)'],\
['n','mind',None,'(c=mind) & ((bIGc) t^ (bTKz))'],\
['n','mind|a',None,'(c=mind) & ((bIGc) x^ (bTKh)) & ((bIGc) x^ (bDSt)) & ((bIGc) t^ (bIGj)) & (((bTKr) & (rCRRq) & (sHWb) & (qPh) & (To)) t^ ((qPe) & (nt+qPf) & (Tg) & (gAo))) & (j=non_whole) & (rb^sRt INSm) & (qb^sQu INSm)'],\
['n','moment',None,'(c=moment) & ((bIGc) x^ (dTb)) & ((bIGc) x^ (bAh)) & ((bIGc) x^ (eAb)) & ((bIGc) t^ (bIGf)) & (f=non_whole)'],\
['na','now',None,'(b=now) t^ (cSb)'],\
['n','part',None,'(c=part) & ((bIGc) x^ (dHWb))'],\
['n','part|p',None,'(c=part|p) & (((bIGc) & (bOFd)) x^ (dHWb))'],\
['n','particle',None,'(c=particle) & ((bIGc) x^ (bSd)) & ((bIGd) x^ (hTg)) & ((bIGc) t^ (bIGf)) & (f=non_whole) & (g=now) & (hb^bSd)'],\
['n','particle|m',None,'(c=particle|m) & ((bIGc) x^ (bSSd)) & ((bIGd) x^ (hTg)) & ((bIGc) t^ (bIGf)) & (f=non_whole) & (g=now) & (hb^bSSd)'],\
['n','point',None,'(c=point) & ((bIGc) x^ (dSb)) & ((bIGc) x^ (eABb)) & ((bIGc) x^ (bABm)) & ((bIGc) x^ (fFRb)) & ((bIGc) x^ (bFRj)) & ((bIGc) x^ (gLFb)) & ((bIGc) x^ (bLFk)) & ((bIGc) t^ (bIGh)) & (h=non_whole)'],\
['n','point|s',None,'(c=point|s) & ((bIGc) x^ (dSSb)) & ((bIGc) t^ (bIGe)) & (e=non_whole)'],\
['n','point|b',None,'(c=point|b) & ((bIGc) x^ (dZb)) & ((bIGc) x^ (eABb)) & ((bIGc) x^ (bABm)) & ((bIGc) x^ (gLFb)) & ((bIGc) x^ (bLFk)) & ((bIGc) t^ (bIGh)) & (h=non_whole)'],\
['n','possible relationship',None,'(c=possible relationship) & ((pIGc) x^ (pPb))'],\
['n','possible world',None,'(c=possible world) & ((bIGc) x^ (pPb))'],\
['n','property',None,'(c=property) & ((bIGc) x^ (dIAb)) & ((bIGc) t^ (bIGe)) & (e=non_whole)'],\
['n','property|d',None,'(c=property|d) & ((bIGc) x^ (dIYb)) & ((bIGc) t^ (bIGe)) & (e=non_whole)'],\
['n','property|n',None,'(c=property|n) & ((bIGc) x^ (dHb)) & ((bIGc) t^ (bIGe)) & (e=non_whole)'],\
['n','property|v',None,'(c=property|v) & ((bIGc) x^ (dIVb)) & ((bIGc) t^ (bIGe)) & (e=non_whole)'],\
['n','reality|t',None,'((c=reality|t) x^ (pIc)) & ((dIGe) t^ (d~IGc)) & ((c=reality|t) t^ ((cIGf) & (cIGg))) & ((qIc) t^ (cHWq)) &  (e=thing) & (f=non_relationship) & (g=relationship)'],\
['n','sensation',None,'(c=sensation) & ((bIGc) x^ (bSSd)) & ((bIGc) t^ (bIGe)) & (e=non_whole)'],\
['n','sensorium',None,'(c=sensorium) & ((bIGc) x^ ((bHWd) x^ (eSSd)))'],\
['na','thing',None,'See atomic categories'],\
['n','thought',None,'(c=thought) & ((bIGc) x^ (dTKb)) & ((bIGc) t^ (bIGe)) & ((bIGc) x^ (bAIf)) & (e=relationship)'],\
['n','whole',None,'(c=whole) & ((bIGc) x^ (bHWd))'],\
['na','abbreviation',None,'(c=abbreviation) & ((bIGc) x^ ((bIGd) ed^ (bIGe))) & (d=constant) & (e=variable)'],\
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
['na','relation',None,'(c=relation) & ((bIGc) t^ (bIGd)) & (d=non_whole)'],\
['rai','relational variable','R','indefinable'],\
['na','relatum',None,'(c=relatum) & ((bIGc) x^ (bRd)) & ((eIGc) x^ (fRe))'],\
['a','root (word)',None,'(wildly disjunctive), (c=root) & ((bIAc) t^ (bIGd)) & (d=word)'],\
['na','singular form',None,'(wildly disjunctive)'],\
['na','subject',None,'hard coded - the first relatum is the subject'],\
['na','subject|i',None,'indefinable (must occur in if the relation is an intransitive verb)'],\
['na','variable',None,'indefinable'],\
['na','verb form',None,'(wildly disjunctive)'],\
['a','actual|p',None,'(c=actual|p) & (d=reality) & ((pIAc) x^ (pId))'],\
['a','actual|w',None,'(c=actual|w) & ((bIAc) x^ (b=reality))'],\
['ns','set',None,'(set = whole)'],\
['rs','aware of',None,'(aware of=TK)'],\
['rs','belong|g ',None,'(belong|g=IG)'],\
['r','belong to','BLN','(bBLNc) x^ (cHWb)'],\
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
['aa','consistent',None,'(b=consistent) & ((cIAb) x^ (cPd))'],\
['r','exist','EX','(exist=EX) & ((bEX) x^ (bIAc)) & (c=extant)'],\
['ns','feature ',None,'(feature=property)'],\
['ns','group',None,'(group = whole)'],\
['ns','group|c',None,'(group|c = concept|n)'],\
['rs','instantiate',None,'(instantiate=IG)'],\
['r','instantiated by','INSP','(instantiated by=INSP) & ((bINSPc) x^ (cIGb))'],\
['ns','item',None,'(item=thing)'],\
['a','material',None,'(c=material) & (d=particle) & ((bIAc) x^ (bIGd))'],\
['a','material|m',None,'(z=material|m) & (((bIAz) & (cIGb)) x^ (cSd))'],\
['ns','material|n ',None,'(material|n=matter)'],\
['ns','matter',None,'(matter=particle)'],\
['ns','member',None,'(member = part)'],\
['ns','member|i',None,'(member|i = instance)'],\
['ns','mental whole',None,'(mental whole = thought)'],\
['n','mind|b',None,'(c=mind|b) & ((bIGc) x^ ((bHWd.h.j) & (dIGe) & (hIGf) & (jIGg))) & (e=mind) & (f=imagination) & (g=sensorium)'],\
['as','natural|p',None,'(natural|p = material)'],\
['ns','number|i',None,'(number|i=integer)'],\
['ns','object',None,'(object=thing)'],\
['n','part|f|a',None,'(c=part|f|a) & ((bIGc) x^ (bIGd)) & (d=fact)'],\
['n','part|i',None,'(c=part|i) & ((bIGc) x^ (bIGd)) & (d=thought)'],\
['n','part|w',None,'(c=part|w) & ((bIGc) x^ (bIGd)) & (d=possible relationship)'],\
['as','physical|c',None,'(physical|c = material|c)'],\
['as','physical|m',None,'(physical|m = material|m)'],\
['as','physical ',None,'(physical=material)'],\
['ns','trait',None,'(trait = property)'],\
['aa','possible',None,'(b=possible) & ((pIAb) x^ (pPc))'],\
['n','present',None,'(present = now)'],\
['ns','qualia ',None,'(qualia=sensation)'],\
['r','right of','RT','(right of=RT) & ((bRTc) x^ (cLFb))'],\
['ns','sense datum ',None,'(sense datum=particle|m)'],\
['ns','collection',None,'(collection = whole)'],\
['ns','time|m ',None,'(time|m=moment)'],\
['ns','character trait',None,'(character trait = property)'],\
['ns','universal',None,'(universal = concept|n)'],\
['','thing',None,'(c=thing) & ((bIGc) x^ ((bIGd) ed^ (bIGe))) & ((bIGd) t^ (bIGh)) & (d=relation) & (e=non_relation) & (h=non_whole)'],\
['','non_relation',None,'(c=non_relation) & ((bIGc) x^ ((bIGd) ed^ (bIGe) ed^ (bIGf) ed^ (bIGg))) & (((bIGe) ed^ (bIGf)) t^ (bIGh)) & (d=class concept) & (e=property|n) & (f=property) & (g=instance) & (h=non_whole)'],\
['','class concept',None,'(c=class concept) & ((bIGc) x^ ((bIGd) ed^ (bIGe))) & ((bIGd) t^ (bIGf)) & ((bIGc) t^ (bIGg)) & (d=relationship) & (e=non_relationship) & (f=whole) & (g=non_whole)'],\
['','non_relationship',None,'(c=non_relationship) & ((bIGc) x^ ((bIGd) ed^ (bIGe))) & (d=whole) & (e=non_whole)'],\
['','non_whole',None,'(c=non_whole) & ((bIGc) x^ ((bIGe) ed^ (bIGf) ed^ (bIGg) ed^ (bIGh) ed^ (bIGj) ed^ (bIGk))) & (e=letter) & (f=mind) & (g=moment) & (h=basic number) & (j=particle) & (k=point)'],\
['','whole',None,' (c=whole) & ((bIGc) x^ ((bIGd) ed^ (bIGe) ed^ (bIGf) ed^ (bIGg) ed^ (bIGh))) & (d=imagination) & (e=possible world) & (f=reality) & (g=sensorium) & (h=other)'],\
['','relationship',None,'(c=relationship) & ((bIGc) x^ ((bIGd) ed^ (bIGe))) & (d=external relationship) & (e=thought)'],\
['','thought',None,'(c=thought) & ((bIGc) x^ ((bIAd) ed^ (bIAe))) & (d=imaginary relationship) & (e=sensational relationship)'],\
['l','t^',None,'(p t^ q) & (eIAc) & (nt+e~IAc) & (eb^dIAc) & (db^(rIAc) & (s~IAc) & (tIAc) & (uIAc))'],\
['l','v+',None,'(p v+ q) & (eIAc) & (nt+e~IAc) & (eb^dIAc) & (db^(rIAc) & (s~IAc) & (tIAc) & (u~IAc))'],\
['l','x^',None,'(p x^ q) & (eIAc) & (nt+e~IAc) & (eb^dIAc) & (db^(rIAc) & (s~IAc) & (t~IAc) & (uIAc))'],\
['l','i^',None,'postponed'],\
['l','nf^',None,'postponed'],\
['l','ed^',None,'(p ed^ q) & (eIAc) & (nt+e~IAc) & (eb^dIAc) & (db^(r~IAc) & (sIAc) & (tIAc) & (u~IAc))'],\
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
['u','that|c',None,'(it IA p that q) x^ (qIAp)'],\
['u','that|o',None,'hard coded'],\
['us','that|s',None,'(that|s = which)'],\
['na','that|n',None,'(that|n = this|n)'],\
['na','there',None,'(there EX b) x^ (bEX)'],\
['na','this|n',None,'(this|n Rc) x^ (bRc)'],\
['u','where|i',None,'hardcoded - (bRc where|i dQf) x^ ((bRc) & (dQf INE c))'],\
['u','which',None,'(bRc which Qd) x^ ((bRc) & (cQd))'],\
['u','which|o',None,'hard coded'],\
['u','who',None,'((bRc who Qd) x^ ((bRc) & (cQd) & (bIGe))) & (e=person)'],\
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
['b','nt+',None,'(nt+p t^ (pIGc)) & (c=relationship) & (qIAd) & (qb^p&nt+p) & (d=consistent)'],\
['m','not',None,'~'],\
['ma','~',None,'(~p t^ (pIGc)) & (c=relationship) & (qIAd) & (qb^p&~p) & (d=contradictory)'],\
['b','g^',None,'If we have (bg^c) on line 3 and SUB 2,3 in the justification section then only in line 2 may we replace b with c but not vice versa.'],\
['c','and|c',None,'(b and|c c R d) x^ (b.cRd)'],\
['m','not|i',None,'(not|i = nt+)'],\
['rat','not equal to',None,'(not equal to = zzz)'],\
['','0',None,''],\
['','0',None,'Numbers'],\
['','0',None,''],\
['nu','0',None,'((b=0) x^ ((cAFb) & (bAFe))) & (c=1) & (e=1)'],\
['nu','1',None,'((b=1) x^ ((cAFb) & (bAFe))) & (c=2) & (e=0)'],\
['nu','2',None,'((b=2) x^ ((cAFb) & (bAFe))) & (c=3) & (e=1)'],\
['nu','3',None,'((b=3) x^ ((cAFb) & (bAFe))) & (c=4) & (e=2)'],\
['dd','at least one',None,'(at least one bRc) x^ ((zRc) & (zIGb))'],\
['dd','at least three',None,'(((at least three bRc) & (bOFd) & (bIGe)) x^ ((zRc) & (zIGd) & (yRc) & (yIGd) & (xIGd) & (xRc))) & (e=plural form)'],\
['dd','at least two',None,'(((at least two bRc) & (bOFd) & (bIGe)) x^ ((zRc) & (zIGd) & (yRc) & (yIGd))) & (e=plural form)'],\
['dd','exactly one',None,'(exactly one b R c) x^ ((zIGb) & (((yIGb) & (yRc)) t^ (y=z)))'],\
['dd','exactly three',None,'(((exactly three bRc) & (bOFd) & (bIGe)) x^ ((yIGd) & (xIGd) & (yRc) & (xRc) & (wRc) & (wIGd) & (((zIGd) & (zRc)) t^ ((z=y) ed^ (z=x) ed^ (z=w))))) & (e=plural form)'],\
['dd','exactly two',None,'(((exactly two bRc) & (bOFd) & (bIGe)) x^ ((yIGd) & (xIGd) & (yRc) & (xRc) & (((zIGd) & (zRc)) t^ ((z=y) ed^ (z=x))))) & (e=plural form)'],\
['a','second|m',None,'(z=second|m) & (y=first|m) & ((bIAz) & (bIGc)) x^ ((dIAy) & (dIGc) & (bSCMd))'],\
['a','second|o',None,'(z=second|o) & (y=first|o) & ((bIAz) & (bIGc)) x^ ((dIAy) & (dIGc) & (bSUOd))'],\
['a','second|p',None,'(z=second|p) & (y=first|p) & ((bIAz) & (b=c Te)) x^ ((dIAy) & (d=c Tf) & (bSCPd ASCc))'],\
['a','second|s',None,'(z=second|s) & (y=first|s) & ((bIAz) & (bIGc)) x^ ((dIAy) & (dIGc) & (bSCDd))'],\
['a','second|u',None,'(z=second|u) & (y=first|u) & ((bIAz) & (bIGc)) x^ ((dIAy) & (dIGc) & (bSCUd))'],\
['dd','zero',None,'(bR zero c) x^ ((b~Rc) & (cN0))'],\
['dd','zero',None,'(zero = no)'],\
['ddi','a',None,'((a bRc) x^ ((zRc) & (zIGb) & (zIAe))) & (e=indefinite)'],\
['ddi','a|a',None,'((a|a bRc) x^ ((zRc) & (zIGb) & (zIAe))) & (e=general)'],\
['di','all',None,'(all = every)'],\
['ds','another',None,'(another bRc) x^ ((zRc) & (zIGb))'],\
['ds','any',None,'(any = every)'],\
['dt','any|n',None,'(b~R any|n c) x^ (bR no c)'],\
['d','anyone except',None,'((anyone except bRc) x^ ((anything except bRc) & (bIGd))) & (d=person)'],\
['d','anything except',None,'(anything except bRc) x^ (((z=~b) t^ (zRc)) & (b~Rc))'],\
['d','every',None,'((every bRc) x^ (((zIGb) t^ (zRc)) & (zIAe) & (yIGb) & (yIAd))) & (d=particular) & (e=general)'],\
['','every (different)',None,'((every b R different|b c) x^ ((dIGb) t^ ((dRe) & (dRf) & (d~Rg))) & (((mIGb) & (jIGb) & (kIGc)) t^ ((m~Rk) v+ (j~Rk)))) & (h=indefinite) & (e.f.gIAh) & (e.f.gIGc)'],\
['d','everything except|p',None,'((everything except|p bRc) x^ (((z~IGb) t^ (zRc)) & ((yIGb) t^ (y~Rc)))'],\
['dd','few',None,'postponed'],\
['dd','many|d',None,'((many|d bRc) x^ ((zRc) & (zIGb) & (zIAe))) & (e=many)'],\
['dd','many|n',None,'((many|n bRc) x^ ((zIGb) & (zRc) & (zIAg) & (yIGb) & (y~Rc) & (yIAg) & (y zzz z))) & (g=many)'],\
['dd','many|s',None,'(many|s bRc) x^ ((zIGb) & (zRc) & (zIAd) & (yIGb) & (y~Rc) & (yIAd))'],\
['dd','no',None,'((no bRc) x^ (((zIGb) t^ (z~Rc)) & (zIAe) & (yIGb) & (yIAd))) & (d=particular) & (e=general)'],\
['d','no one except',None,'((no one except bRc) x^ ((only bRc) & (bIGd))) & (d=person)'],\
['dd','only',None,'(only bRc) x^ (((z=~b) t^ (z~Rc)) & (bRc))'],\
['ddi','the',None,'((the bRc) x^ ((zRc) & (zIGb) & (zIAe))) & (e=definite)'],\
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
['d','nothing|d',None,'((nothing|d bRc) x^ ((no b dRc) & (dIGz))) & (z=thing)'],\
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
['p','he',None,'(d=person) & (e=male) & ((he Rb) t^ ((cRb) & (cIAe) & (cIGd))) & (g=definite) & (h=particular)'],\
['ps','her',None,'(her=she)'],\
['q','her|p',None,'(d=person) & (e=female) & ((her|p bRc) t^ ((bRc) & (dIAe) & (dPSb)))'],\
['ps','him',None,'(him=he)'],\
['q','his',None,'((his bRc) t^ ((zRc) & (zIGb) & (dOWNz))) & (d=he)'],\
['p','i',None,'(d=person) & ((i Rb) t^ ((iIGd) & (iIAg))) & (g=definite)'],\
['pa','it',None,'hard coded'],\
['v','it|p',None,'propositional it'],\
['p','it|w',None,'hard coded'],\
['q','its|a',None,'(bR its|a c) t^ ((zIGc) & (bHMz) & (bRz))'],\
['ps','me',None,'(me=i)'],\
['q','my',None,'((my bRc) t^ ((zRc) & (zIGb) & (iOWNz)))'],\
['q','my|a',None,'((my bRc) t^ ((zRc) & (zIGb) & (iHWz)))'],\
['q','our',None,'(d=person) & ((our bRc) t^ ((bRc) & (eIGd) & (zIGe) & (ePSb)))'],\
['p','she',None,'(d=person) & (e=female) & ((she Rb) t^ ((cRb) & (cIGd) & (cIAe) & (cIAg) & (cIAh))) & (g=definite) & (h=particular)'],\
['ps','them',None,'(them=they)'],\
['p','they',None,'(d=person) & ((they Rb) t^ ((cRb) & (cIGd) & (zIGc) & (cIAg) & (cIAh))) & (g=definite) & (h=particular)'],\
['p','we',None,'(d=person) & ((we Rb) t^ ((cRb) & (cIGd) & (zIGc) & (cIAg) & (cIAh))) & (g=definite) & (h=particular)'],\
['p','you',None,'(d=person) & ((you Rb) t^ ((cRb) & (cIGd) & (cIAg))) & (g=definite)'],\
['p','you|p',None,'(d=person) & ((you|p Rb) t^ ((cRb) & (cIGd) & (zIGc))) & (g=definite) & (h=particular)'],\
['q','your',None,'(e=person) & ((your bRc) t^ ((zRc) & (zIGb) & (dOWNz))) & (d=you)'],\
['q','your|p',None,'(d=person) & ((your|p bRc) t^ ((bRc) & (eIGd) & (zIGe) & (ePSb)))'],\
['n','ability',None,'(c=ability) & ((dH can b) x^ (d can R)) & (((bIGc) & (R OFV b)) t^ (d can R))'],\
['ra','about','ABT','postponed'],\
['r','above|a','ABO','(above|a=ABO) & ((bABOc) x^ ((bSz) & (zABc)))'],\
['r','above|m','ABV','(above|m=ABV) & ((bABVc) x^ ((bSz) & (cSy) & (zABy)))'],\
['a','abstract',None,'(c=abstract) & ((bIAc) x^ ((bAd) ed^ (bABe) ed^ (bAFf) ed^ (gHb) ed^ (bHWj) ed^ (mIGb) ed^ (nIAb) ed^ (bIGo))) & (o=relation)'],\
['a','abstract|a',None,'(c=abstract|a) & (((bIAc) & (bITd) & (bRe)) x^ (((fIGd) t^ (fRe))))'],\
['a','abstract|c',None,'(c=abstract|c) & (e=abstract) & (((bIAc) & (dIGb)) x^ (dIAe))'],\
['a','abstract|d',None,'(c=abstract|d) & ((bIAc) x^ ((bAd) ed^ (bABe) ed^ (bAFf) ed^ (gHb) ed^ (bIAp) ed^ (mIGb) ed^ (nIAb) ed^ (bIGo))) & (o=relation) & (p=abstract|g)'],\
['a','abstract|g',None,'(c=abstract|g) & ((bIAc) x^ ((bHWe) t^ (eIAf))) & (f=abstract|d)'],\
['n','abstract essence',None,'(abstract essence = essence|a)'],\
['e','abstractly',None,'((bEX abstractly) x^ ((bIAd) & (bIAc))) & (c=abstract) & (d=extant)'],\
['a','absurd',None,'(b=absurd) & ((pIAb) x^ ((pIAc) & (nt+pIAc))) & (c=contradictory)'],\
['as','absurd|r',None,'(absurd|r = ridiculous)'],\
['ns','action',None,'(action = effect)'],\
['a','actual',None,'(c=actual) & (((bIAc) & (bIGd)) x^ (bIGd))'],\
['ns','actual|s',None,'(actual|s = physical|s)'],\
['rs','actualize','ACU','(actualize = materialize)'],\
['e','actually',None,'(b=reality) & ((p actually) x^ (pIb))'],\
['r','after|p','AFT','((bAFTc) x^ ((bHWd) & (dIAe) & (dAc))) & (e=first)'],\
['r','allow','ALO','(allow=ALO) & (eb^bPRVc) & ((bALOc) x^ ((dTRYc) t^ (b~TRYe)))'],\
['e','always|p',None,'(c=always|p) & ((pIVc) x^ ((bIGd) t^ (pPb))) & (d=possible world)'],\
['e','always',None,'(c=always) & ((pIVc) x^ ((bIGd) t^ (pTb))) & (d=moment)'],\
['rs','appear',None,'(appear=SM)'],\
['ns','arbitrary group',None,'(arbitrary group = group|a)'],\
['ns','area ',None,'(area=region)'],\
['a','artificial',None,'(c=artificial) & ((bIAc) x^ ((bIAd) & (eIGf) & (eCAg INTh))) & (d=natural) & (f=person) & (gb^bIAd) & (h=past)'],\
['rc','as','AS','(as=AS) & (((bASc) & (dRb)) x^ (cRb))'],\
['o','ask (how)',None,'((bASKc) x^ ((gIGf) t^ (bTKk))) & (c b^ how CAe) & (f=cause) & (h b^ gCAe) & (k b^ hUj)  '],\
['o','ask (what)',None,'((hASKg) x^ ((cIGd) t^ (hTKk))) & (d=thing) & (e b^ bRc) & (g b^ bR what?) & (k b^ eUf)'],\
['rs','at|i',None,'(at|i=INP)'],\
['rs','at|n',None,'(at|n=NXT)'],\
['a','atomic|p',None,'(b=indefinable|p) & (c=property) & (e=relationship) & (gb^fHd) & (((dIGc) & (dIAb)) x^ ((hIGe) t^ (hnf^g)))'],\
['a','atomic|r',None,'(b=indefinable|r) & (f=relationship) & (h=relation) & (cb^dRe) & (((R IAb) & (R IGf)) x^ ((gIGf) t^ (gnf^c)))'],\
['o','atomic equivalent',None,'(b=indefinable equivalent) & (((cIGb) & (cOFd)) x^ ((c x^ d) & (d~IAf) & ((eIGc) t^ (eIAf)))) & (f=indefinable)'],\
['n','atomic relationship',None,'(c=indefinable relationship) & (d=subject) & (e=relation) & (f=object) & (g=truth value) & (h=locative molecular relationship) & (k=variable) & ((bIGc) x^ ((zIGd) & (yIGe) & (wIGg) & (bHz) & (bHy) & (vIGf) & (bHV) & (bHv) & (vIGk) & (zIGk) & (uIGh) & (bIGd) & (uHb)))'],\
['rs','attempt',None,'(attempt=TRY)'],\
['rs','attended',None,'(attended = participated)'],\
['as','authentic',None,'(authentic=actual)'],\
['na','authority',None,'postponed'],\
['n','axiom',None,'(c=axiom) & ((bIGc) x^ ((eIGd) t^ (enf^b)) & (((bHWf) & (fIGg)) t^ (f~HWh))) & (g=antecedent sentence) & (h=IG)'],\
['r','before','BF','(before=BF) & ((bBFc) x^ (cAb))'],\
['r','behind','BH','(behind=BH) & ((bBHc) x^ (cFRb))'],\
['r','behind|w','BEH','(behind|d=BEH) & ((bBEHc) x^ ((bHWd) & (dSe) & (cFRe)))'],\
['n','belief',None,'(c=belief) & ((bIGc) x^ (zBb))'],\
['r','believe','B','(believe=B) & ((bBc) x^ (bTKd)) & ((bBc) t^ (bTKc)) & (e=true) & (db^cIAe)'],\
['rs','believe|t ',None,'(believe|t=BT)'],\
['rs','believes',None,'(believes = B)'],\
['r','believes|t','BT','(believe tentatively=BT) & ((bBTp) x^ ((bBr) & (bBp))) & (qb^b~Bp) & (rb^qPz)'],\
['r','belong|o','BLG','(belong|o=BLG) & ((bBLGc) x^ (cOWNb))'],\
['r','belongs to|i','BIM','(bBIMc) x^ (cHIMb)'],\
['r','below','BEL','(below|a=BEL) & ((bBELc) x^ ((bSz) & (cABz)))'],\
['r','below','BW','(below=BW) & ((bBWc) x^ (cABb))'],\
['r','below|m','BLW','(below|m=BLW) & ((bBLWc) x^ ((bSz) & (bSy) & (yABz)))'],\
['r','between|p','BTP','(between|p=BTP) & ((bBTPc_d) x^ ((bNz) & (cNy) & (dNx) & (((xAFz) & (zAFy)) ed^ ((yAFz) & (zAFx)))))'],\
['r','between|p','BTW','(between=BTW) & ((bBTWc_d) x^ (((bAFc) & (dAFb)) ed^ ((dAFb) & (cAFb))))'],\
['r','between|a','BTA','(bBTAc_d) x^ ((eIGf) t^ ~((cRe) & (eRd))) & ((R=LF) ed^ (R=AB) ed^ (R=FR)) & (f=thing)'],\
['rs','between|t ',None,'(between|t=CBT)'],\
['na','body|c',None,'(c=body|c) & ((bIGc) x^ ((bHWd) t^ (dIGe))) & (e=particle)'],\
['n','boundary',None,'(c=boundary) & (((bIGc) & (dHb)) x^ (dINb))'],\
['rs','break',None,'(break=VIO)'],\
['ra','breaks','BRK','postponed'],\
['n','broad reality',None,'((b=broad reality) x^ (((cId) ed^ (cPe)) x^ (bHWc))) & (d=reality)'],\
['ra','calculate','CLC','postponed'],\
['ra','calculates','CLC','postponed'],\
['ea','can|a',None,'(d=ability) & (((pb^bR) & (p can|a) & (R VCPc)) x^ (cIGd))'],\
['e','cannot|w',None,'(state=STT) & (c=absolutely false) & (((p cannot|w) & (bSTTp)) x^ ((bDSz) & (zb^pIAc)))'],\
['as','case',None,'(case = true)'],\
['r','continguous','CTG','(bCTGc) x^ (((bHWd) x^ ((dINb) & (c~HWd))) & ((cHWe) x^ ((eINc) & (b~HWe))) & (bHWf) & (cHWg) & ((hIGj) t^ (h~BTAf_g))) & (j=thing)'],\
['ns','causal part',None,'(causal part = part|c)'],\
['na','causal role',None,'postponed'],\
['n','causal whole',None,'(c=causal whole) & (((bIGc) & (bOFd)) x^ ((bCAUc) & (dIGb)))'],\
['ra','cause','CA','((pCAq) x^ ((bRc INMd Te) t^ ((fQg INMj Th) & (dCTGj) & (hSUTe)))) & (pb^bRc INMd) & (qb^fQg INMj)'],\
['r','cause|i','CAU','(cause|i=CAU) & ((bCAUc) x^ ((bSz Ty CA c SzTx)))'],\
['ra','cause|m','CAUS','postponed'],\
['r','cause|p','CAS','(cause|p=CAS) & (e=reality) & ((bCASc GVd) x^ ((((dIe Ty) & (bSzTy)) t^ (cPx)) & (xNw) & (((dIe Ty) & (b~SzTy)) t^ (cPv)) & (vNu) & (wAFu)))'],\
['r','cause|w','CSE','((bCSEc) x^ ((bHWd) x^ ((d~IAe Tf) t^ (c~IAe Tg)))) & (((d~IAe Tf) t^ (c~IAe Tg)) t^ (gSUTf)) & (e=extant)'],\
['a','certain',None,'(b=certain) & (((cIAb) & (cTOd Tg)) x^ ((eb^(cIf)) & (dTKe Tg) & (hb^(d~TKe Tk)) & (nb^((jIGm) t^ (h~Pj))) & (kAg) & (dTKn))) & (f=reality) & (g=now) & (m=possible world)'],\
['rxd','chronologically between','CBT','(chronologically between=CBT) & ((bCBTc and|c d) x^ (((bAc) & (dAb)) ed^ ((bAd) & (cAb))))'],\
['n','common name',None,'(c=common name) & ((bIGc) x^ ((bIGd) & (bRFe) & (eIGf))) & (d=word) & (f=concept|n)'],\
['ns','concept|p',None,'(concept|p=plan)'],\
['n','concept',None,'(c=concept) & ((dIGb) ed^ (eHb) ed^ (fIAb)) t^ (bIGc)'],\
['na','concept phrase',None,'(c=concept_phrase) & ((bIGc) x^ ((dIGb) & (eRFb) & ((eHWf) t^ (fIGj)) & (eNg) & (gAFh))) & (h=1) & (g=word)'],\
['ns','conclusion',None,'(conclusion=inference)'],\
['as','concrete',None,'(concrete=particular)'],\
['ns','condition|s',None,'(condition|s=situation)'],\
['o','connected|i',None,'(b=connected|i) & ((cIAb) x^ ((gIGe) & (gOFc) & (hIGd) & (cHVh) & (mHVc) & ((kIGg) ed^ (k=g)) & (kIAf))) & (d=main relation) & (e=indefinable equivalent) & (f=connected|s)'],\
['a','connected|s',None,'(b=connected|s) & ((c and|c d IA b Te) x^ (((c t^ d) ed^ (c ed^ d) ed^ (c x^ d) ed^ (c v+ d)) & (c~If Te) & (d~If Te))) & (f=reality)'],\
['ns','consequence',None,'(consequence=inference)'],\
['a','consistently extant',None,'(c=consistently extant) & ((bIAc) x^ (pPc)) & (pb^bIAd) & (d=extant)'],\
['r','contain','CT','(contain=CT) & ((bCTc) x^ (cINb))'],\
['a','contingently contradictory',None,'(b=contingently contradictory) & ((p.qIAb) x^ ((pIAd) & (qIAd) & (p.q~IAd))) & (d=consistent)'],\
['a','contradictorily extant',None,'(c=contradictorily extant) & ((bIAc) x^ ((eIGf) t^ (p~Pe))) & (pb^bIAd) & (d=extant) & (f=possible world)'],\
['a','contradictorily extant|a',None,'(c=contradictorily extant|a) & ((bIAc contradictorily) x^ ((pHWb) & ((eIGf) t^ (p~Pe)))) & (d=extant) & (f=possible world)'],\
['','contradictory',None,'(c=contradictory) & ((pIAc) x^ ((bIGd) t^ (p~Pb))) & (pb^q.nt+q)'],\
['rs','contrary of',None,'(contrary of=NEG)'],\
['as','contrasting ',None,'(contrasting=different)'],\
['r','correspond|s','CRS','(corresponds|s to=CRS) & ((bCRSc) x^ ((zb^yIx) & (((bHw) & (w=~z)) t^ (cHw))))'],\
['r','count',None,'((bCNTc) x^ (bTKd)) & (db^(cHWe) & (cNf))'],\
['r','count|n',None,'(bCOTc) x^ (cNb)'],\
['n','courage',None,'(b=courage) & ((cHb) x^ (cIAd)) & (d=courageous)'],\
['na','courageous',None,'postponed'],\
['na','dead',None,'postponed'],\
['ns','deduction',None,'(deduction=inference)'],\
['aa','definite',None,'(definite = individual)'],\
['as','definite|v',None,'(definite|v = certain)'],\
['n','definite description',None,'(c=definite description) & ((bIGc) x^ ((dHb) & ((ezzzd) t^ (e~Hb)))) & (d=property)'],\
['axd','different',None,'(c=different) & ((b and|c d IA c) x^ (b=~c))'],\
['r','different from','DF','(different from=DF) & ((bDFc) x^ (bzzzc))'],\
['a','difficult',None,'(c=difficult) & (((bIAc) & (bTOd)) x^ ((dTRYb Tf) t^ ((hHWe) x^ ((bPe Tg) & (gAf) & (hIAk))))) & (k=few)         '],\
['rs','distinct from',None,'(distinct from = zzz)'],\
['a','divine',None,'(b=divine) & (c=God) & ((dIAb) x^ (d=c))'],\
['a','divine|s',None,'(c=divine|s) & (d=God) & ((bIAc) x^ (bSMLd))'],\
['ns','duration ',None,'(duration=period)'],\
['r','during','DUR','(during=DUR) & ((pDURb) x^ ((bHWc.d.e) & (pTe) & (eAc) & (dAe)))'],\
['r','during|o','DRG','(during|o=DRG) & ((bDRGc) x^ ((bHWe) t^ ((cHWe) & (eIGf)))) & (f=moment)'],\
['r','during|t','DR','(during|t=DR) & ((bDRc) x^ ((cHWb.d.e) & (eAb) & (bAd)))'],\
['r','earlier|p than','ELA','(bELAc) x^ (((bHWd) & (cHWe)) t^ (eAd))'],\
['r','earlier than','EL','(earlier than=EL) & ((bELc) x^ (cAb))'],\
['a','easy',None,'(c=easy) & (((bIAc) & (bTOd)) x^ ((dTRYb Tf) t^ ((hHWe) x^ ((bPe Tg) & (gAf) & (hIAk))))) & (k=many)         '],\
['r','empirical (of a relation)',None,'(b=empirical) & (R IAb) x^ ((R = SEE) ed^ (R = HR) ed^ (R = TOC) ed^ (R = TST) ed^ (R = SML))'],\
['ns','empty space',None,'(empty space=void)'],\
['n','energy',None,'(c=energy) & ((bIGc) t^ ((dHb) & (dIGf))) & (f=particle)'],\
['a','entire past',None,'((b=entire past) x^ ((bHWc) t^ (dAc))) & (d=now)'],\
['ns','entity',None,'(entity=thing)'],\
['ns','entity|n',None,'(entity|n=object|n)'],\
['n','epistemic possible world',None,'(b=epistemic possible world) & (fb^d~Be) & (((cIGb) & (cTOd)) x^ (fPc))'],\
['a','epistemically contingent',None,'postponed'],\
['a','epistemically impossible',None,'(b=epistemically impossible) & (e=possible world) & (rb^(dIGe) u+ (d~Pe)) & (qb^cBp) & ((pIA b TO c) x^ ((cBr) & (bBp)))'],\
['a','epistemically necessary',None,'(b=epistemically necessary) & ((pIA b TO c) x^ (cKNp))'],\
['a','epistemically probable',None,'(b=epistemically probable) & (((pIAb) & (pTOc Td)) x^ ((zb^cBp Ty) & (xb^c~Bp Ty) & (yAd) & (zNw) & (yNv) & (ub^wAFv) & (cBu Td)))'],\
['n','essence|a',None,'(c=essence|a) & ((bIGc) x^ ((zIGy) x^ (zHb)))'],\
['n','essence|i',None,'(c=individual essence) & ((bIGc) & (uHSb Te)) x^ (((bHWj Tg) & (jIGn) & (dHj)) t^ ((qIAr) & (s~IAr))) & ((fHWm) x^ ((tHm Tg) & (mIGn))) & ((qHWp) x^ (oPp)) & ((sHWq) x^ (nt+oPq)) & (uHWt.d) & (eSUTg))) & (n=intrinsic accidental property) & (r=many) & (ob^fHWj Te)'],\
['na','essence|n',None,'postponed'],\
['n','essence|p',None,'(c=individual essence|p) & (((bIGc) & (dHSb) & (fHWd)) x^ ((fHSj) & (jIGg) & ((bHWh) x^ (jHWh)))) & (g=individual essence)'],\
['n','event',None,'(b=event) & ((pIGb) x^ (pOC))'],\
['n','everything|n',None,'((b=everything|n) x^ ((cIGd) t^ (bHWc))) & (d=thing)'],\
['r','exist|b','EXB','((bEXB) x^ (bIAc)) & (c=contradictorily extant)'],\
['r','exist|c','EXC','((bEXC) x^ (bIAc)) & (c=consistently extant)'],\
['rs','exist as',None,'(exist as = IG)'],\
['r','exists','EX','(exists=EX) & ((bEX) x^ (bIAc)) & (c=extant)'],\
['rs','exists|a',None,'(exists|a=EA)'],\
['rs','exists|i',None,'(exists|i=EI)'],\
['rs','exists|m',None,'(exists|m=EM)'],\
['rs','exists|n',None,'(exists|n=EXN)'],\
['rs','exists|p',None,'(exists|p=EP)'],\
['rs','exists|s',None,'(exists|s=ES)'],\
['r','exists divinely','ED','(exists divinely=ED) & (c=God) & ((bED) x^ (bIGc))'],\
['r','exists historically','EH','(exist historically=EH) & (c=current present) & ((bEH) x^ ((bSzTy) & (cAy)))'],\
['r','exists in the imagination','EI','(exists in the imagination=EI) & ((bEI) x^ (bAIz))'],\
['r','exists intersubjectively','EIN','(exists intersubjectively=EIN) & ((bEIN) x^ ((bAIy z) & (xN2) & ((y=x) ed^ (yAFx))))'],\
['r','exists mentally','EM','(exists mentally=EM) & ((bEM) x^ (bTKz))'],\
['r','exists naturally','EXN','(exists naturally=EXN) & ((bEXN) x^ (bSz))'],\
['rs','exists physically ',None,'(exists physically=EXN )'],\
['r','exists probabilistically','EP','(exists probabilistically=EP) & ((bEP) x^ (bPz))'],\
['r','exists sensationally','ES','(exists sensationally=ES) & ((bES) x^ (bSSz))'],\
['n','explicit|e relationship|e',None,'(c=explicit|e relationship|e) & ((bIGc) x^ ((bHWd) & (bHWe) & (bHWh) & (dIGf) & (eIGg) & (hIGf))) & (f=relatum) & (g=relation)'],\
['n','external relationship',None,'(c=external relationship) & ((pIGc) x^ ((pPd) v+ (pIe))) & (e=reality)'],\
['a','fake',None,'(c=fake) & (((bIAc) & (bIGd)) x^ (b~IGd))'],\
['a','false',None,'(c=false) & ((bIAc) x^ (b~IAd)) & (d=true)'],\
['n','familial part',None,'(c=familial part) & (((bIGc) & (bOFd)) x^ (bIGd))'],\
['n','familial part|a',None,'(c=familial part|a) & ((bIGc) x^ (dHMb))'],\
['ns','familial whole',None,'(familial whole=group)'],\
['na','family',None,'postponed'],\
['n','family|i',None,'(b=family|i) & (((cIGb) & (dIGc) & (eIGc)) x^ (((dIGf) & (dOFe)) ed^ ((eIGf) & (eOFd)) ed^ ((dIGh) & (dOFe)) ed^ ((eIGh) & (eOFd)) ed^ ((dIGg) & (dOFe)) ed^ ((eIGg) & (eOFd)) ed^ ((dIGk) & (dOFe)) ed^ ((eIGk) & (eOFd)) ed^ ((dIGl) & (dOFe)) ed^ ((eIGl) & (eOFd)))) & (f=sibling) & (g=mother) & (h=father) & (k=aunt) & (l=uncle)'],\
['aa','fanatical',None,'postponed'],\
['ra','feel',None,'postponed'],\
['ra','feels',None,'postponed'],\
['a','few|a',None,'(c=few|a) & (((bIAc) & (eIAf)) x^ ((bNd) & (eNg) & (gAFd))) & (f=many|a)'],\
['d','few ',None,'(few=~mn)'],\
['a','fictional',None,'(c=fictional) & ((bIGc TOh) x^ ((bAId) & (hTKe))) & (eb^(fIg) t^ (b~CRRf)) & (g=reality)'],\
['ra','follows from (contingently)','FLC','(follows from=FLC) & ((bFLCc) x^ ((dIAm Pe) & (fIAm Pg) & (h~IAm Pm) & (jIAm Pk))) & (db^b.c) & (fb^b.nt+c) & (hb^nt+b.c) & (jb^nt+b.nt+c) & (m=probable)'],\
['ra','follows from (necessarily)','FL','(follows from=FL) & ((bFLc) x^ ((dIAta^ Pe) & (fIAta^ Pg) & (hIAco^ Pm) & (jIAta^ Pk))) & (db^b.c) & (fb^b.nt+c) & (hb^nt+b.c) & (jb^nt+b.nt+c)'],\
['as','forbidden',None,'(forbidden=morally impossible)'],\
['as','forbidden|l',None,'(forbidden|l=legally impossible)'],\
['rs','from|b',None,'(from|b = born)'],\
['rs','from|c','FRMC','(FRMC = FLC)'],\
['r','front|a','FRA','(in|r front|a of|r=FRA) & ((bFRAc) x^ (((bHWm) & (mSj)) t^ (jFRc))) & (cIGf) & (jIGf) & (f=point) & (h=particle) & (k=natural whole) & (bIGk) & (mIGh)'],\
['r','front|m','FRN','(in|r front|m of|r=FRN) & ((bFRNc) x^ ((bSz) & (cSy) & (zFRy)))'],\
['r','front|o','FRO','(in|r front|p of|r=FRO) & ((bFROc) x^ (((cHWd) & (dSe)) t^ (bFRe))) & (f=natural whole) & (g=point) & (h=particle) & (bIGg) & (cIGf) & (dIGh)'],\
['r','front|w','FNT','(in|r front|w of|r=FNT) & ((bFNTc) x^ ((bHWd) & (dSe) & (cHWf) & (fSg)) t^ (eFRg))'],\
['aa','general',None,'hard coded'],\
['ns','general term',None,'(general term = concept|n)'],\
['as','genuine',None,'(genuine=actual)'],\
['r','given','GV','(given=GV) & ((pGVq) x^ (qu+p))'],\
['ra','go','GO','postponed'],\
['ra','go to','GO','postponed'],\
['n','goal',None,'(c=goal) & (((bIGc) & (bFORd)) x^ (dDSb))'],\
['n','God',None,'(b=God) x^ (((b~EX) & (z=~b)) t^ (z~EXN))'],\
['ra','goes','GO','(GO=MOV)'],\
['aa','good',None,'postponed'],\
['r','greater than','GR','(greater than=GR) & ((bGRc) x^ (bAFc))'],\
['n','group|a',None,'(c=group|a) & ((bIGc) x^ ((bHWs) x^ (sHu))) & (xb^(wHWb) x^ (wHv)) & (ub^tBx)'],\
['na','HA ... friend icm',None,'b and c have a friend in common: postponed'],\
['ns','haecceity',None,'(haecceity=unique essence)'],\
['rs','happen ',None,'(happen=OC)'],\
['ra','has|c','HC','postponed'],\
['r','has|p|k (causal power)','HCB','(has|p|k= HCB) & ((bHCBc) x^ ((bRd INMe Tf) t^ ((gRh INMe Tg) & (gSUTf)))'],\
['r','has|c|p','HCP','(bHCPc) x^ ((bHWc) x^ (bCSEd))'],\
['r','has|c|r (causal role)','HCA','((bHCAc) x^ (bCAc)) & ((bHCAc) t^ (bHc))'],\
['ra','has|e (corpse)','HA','has|c=HA, c=matter, d=dead ((bHAz) & (zIGc)) x^ ((zSy) & (bOWNz) & (zIAd))'],\
['r','has|g|c','HGC','(cHGCb) x^ ((cHWe) t^ (eIGb))'],\
['r','has|i','HI','((bHIc) x^ (((bHWc) ed^ (bHc)) & (cIAd))) & (d=intrinsic)'],\
['r','has|i|m','HIM','((bHIMc) x^ (cAIb))'],\
['r','has|m','HM','(have|m=HM) & ((bHMc) x^ (cIGb))'],\
['r','has|n','HN','(has|n=HN) & ((bHNc) x^ ((bINd) & (bINe) & (eINUd)))'],\
['r','has|s','HSS','(bHSSc) x^ ((cSSd) & (bHWc))'],\
['r','has|s|p','HSP','(bHSPc) x^ (cINb)'],\
['r','has|t','HAT','(have|t = HAT) & ((bHATc) x^ (cTCHb))'],\
['r','has|p|j','HCD','(has|p|j = HCD) & ((bHCDc) x^ (((bTKWr) & (rCRRq) & (qPh) & (To)) t^ ((qTg) & (gAo))) & (qb^bRu INSm)'],\
['r','has|p|e','HCE','(bHCEc) x^ ((bHCBc) ed^ (bHCDc))'],\
['','have|b','HB','((bHBc) x^ ((bHWc) & (cIGd))) & (d=body|c)'],\
['r','have|g|c','HGC','(cHGCb) x^ ((cHWe) t^ (eIGb))'],\
['rxd','have|i|c (... in common|r)','HCM','(b and|c c HCM d) x^ ((bIAd) & (cIAd))'],\
['rs','have|o ',None,'(have|o=own)'],\
['r','have|p|n','HPN','((bHPNc) x^ (cRFb)) & ((bHPNc) t^ ((bIGd) & (cIGe))) & (d=individual) & (e=proper name)'],\
['r','have|r (object is a relation)','HR','((bHRc TOd) x^ (bRd)) & (c=R)'],\
['r','have|t','HAT','(have|t = HAT) & ((bHATc) x^ (cTCHb))'],\
['ra','have|w','HW','(c=body) &  (((bHWz) & (zIGc)) x^ (zSy))'],\
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
['a','historical',None,'(c=historical) & (d=current present) & ((bIAc) x^ ((bTz) & (dAz) & (b~Td)))'],\
['n','hypothetical material object',None,'(c=hypothetical material object) & ((bIGc) x^ ((bSz) ed^ (b~Sd)))'],\
['rs','identical',None,'is identical to=='],\
['ns','identification',None,'(identification=definite description)'],\
['r','identify',None,'(identify=IDT) & ((bIDTc) x^ ((cHd) & (cIAe) & (bTNKf) & (dIGg))) & (f b^ cHd) & (d=individual essence) & (e=particular)'],\
['a','imaginary',None,'(c=imaginary) & ((bIGc TOh) x^ ((bAId) & (hTKe))) & (eb^(fIg) & (bCRRf)) & (g=reality)'],\
['n','imagination',None,'(c=imagination) & ((bIGc) x^ (zAIb))'],\
['n','implicit|i relationship|i',None,'(c=implicit|i relationship|i) & ((bIGc) x^ ((bHWd) & (bHWe))) & (dIGf) & (eIGg) & (f=subject|i) & (g=intransitive verb)'],\
['rs','implies ',None,'(implies=i^)'],\
['aa','important',None,'postponed'],\
['a','improbable',None,'(c=improbable) & ((bIAc) x^ (b~IAd)) & (d=probable)'],\
['ratso','in','IN','((bINc) x^ ((bIGd) & (cHWb))) & (d=point)'],\
['rs','in|a ',None,'(in|a=DUR)'],\
['r','in|b','INB','((bINBc) x^ ((cHWb) & (bIGd))) & (d=moment)'],\
['r','in|f','INF','(bINFc) x^ ((bIGd) & (cIGd) & ((cHWe) x^ (bHWe))) & (d=period)'],\
['r','in|c','INC','(in) & ((bINCc) t^ ((zSc) & (dIGc) & (eIGc) & (fIGc) & (gIGc) & (hIGc) & (iIGc) & (jIGc) & (kIGc) & (hLFi) & (hABj) & (dFRh) & (eFRi) & (iABk) & (eABg) & (dLFe) & (dABf) & (fFRj) & (hLFb) & (hABb) & (bLFi) & (iABb) & (bLFk) & (bABk) & (jLFb) & (bABj)))'],\
['ratso','in|d','IND','((bINDc) t^ (((bHWd) & (dIGe)) x^ (cHWd))) & (e=point)'],\
['r','in|e','INE','(bINEc) x^ ((bSd) & (cHWd))'],\
['r','in|g','ING','(c=relationship) & (in|g=ING) & ((bINGp) x^ (((bAWz) ed^ (zAWb)) & (pHWb) & (pIGc)))'],\
['r','in|m','INM','(bINMc) x^ ((bHWd) x^ ((dSe) & (cHWe)))'],\
['r','in|s','INS','(bINSc) x^ ((bHWd) & (dINMc))'],\
['r','in|r','INR','(in|r=INR) & ((bINRc) x^ ((bSd) & (dINc)))'],\
['rs','in|p','INP','(in|s = is|g)'],\
['rs','in|t ',None,'(in|t=during)'],\
['','in-q','INQ','((bINQc) & (cIAd)) x^ (bIAd)'],\
['r','in|v','INV','((bINVc) x^ ((bCAc) & (dHWb.e) & (eHWf) & (fIGg))) & (cb^fMOV) & (g=body|c)'],\
['aa','indefinite',None,'(b=indefinite) & ((cIAb) x^ ((cIAj) & ((kzzzc) t^ (k~IAj)) & ((eIGd) t^ ((fPg) & (nt+fPh))))) & (f b^ e=c) & (cIGd)'],\
['aa','indefinite|a',None,'postponed'],\
['a','indeterminate',None,'(b=indeterminate) & (((pIAb) & ((p=q) ed^ (p=r))) x^ ((qNz) & (rNy) & (xNw) & (pNv) & (wAFy) & (zAFw) & ((vAFw) ed^ (wAFv))))'],\
['a','indexical',None,'postponed'],\
['nk','individual',None,'(b=individual) & ((cIGb) x^ (((dIGe) t^ (d~IGc)) & (cIAf) & ((d zzz c) x^ (d~IAf)))) & (e=thing)'],\
['as','individual|p',None,'(individual|p=particular)'],\
['ns','individual essence',None,'(individual essence=essence|i)'],\
['n','individual essence',None,'(individual essence = essence|i)'],\
['n','individual|p',None,'(c=individual|p) & ((bIGc) x^ ((bHWd.e) & (dSf) & (eTKg) & (bNh))) & (h=2)'],\
['r','infer','INF','(infer=INF) & ((bINFc d) x^ ((zb^nt+c && d) & (yb^zIAco^) & (bBy)))'],\
['n','inference|c',None,'(c=inference) & ((bIGc) x^ (dFLCb)) & (follows from=FLC)'],\
['n','inference|n',None,'(c=inference) & ((bIGc) x^ (dFLb)) & (follows from=FL)'],\
['a','infinite',None,'(c=infinite) & (((bIAc) & (bPCPc)) x^ ((zIGc) t^ (((yAFz) & (zAFx)) ed^ ((yAz) & (zAx)) ed^ ((yLFz) & (zLFx)) ed^ ((yABz) & (zABx)) ed^ ((yFRz) & (zFRx)))))'],\
['a','infinite',None,'(c=infinite) & ((bIAc) x^ ((zIGb) t^ ((yAFz) & (zAFx)) ed^ ((yAz) & (zAx)) ed^ ((yLFz) & (zLFx)) ed^ ((yABz) & (zABx)) ed^ ((yFRz) & (zFRx))))'],\
['rs','inside',None,'(inside = INE)'],\
['ns','interval ',None,'(interval=period)'],\
['r','intrinsic',None,'(c=intrinsic) & ((dHWb) ed^ (dHb)) t^ (bIAc)'],\
['ra','is|e','EX','((bEX) x^ (bIAc)) & (c=extant)'],\
['ns','item|n',None,'(item|n=object|n)'],\
['rs','judge',None,'(judge = believe)'],\
['ns','kind',None,'(kind=type)'],\
['ns','kind',None,'(kind|n = natural kind)'],\
['ns','kind',None,'(kind = type)'],\
['aa','large',None,'postponed'],\
['r','later than','LAT','(later than=LAT) & ((bLATc) x^ (bAc))'],\
['r','left of|a','LEF','(left of|a=LEF) & ((bLEFc) x^ ((bSz) & (zLFc)))'],\
['r','left of|m','LFT','(left of|m=LFT) & ((bLFTc) x^ ((bSz) & (cSy) & (zLFy)))'],\
['a','legally contingent',None,'(b=legally contingent) & (d=authorities) & (punish=PNS) & ((pIAb SsTt) x^ (((mn dDSv SsTt) ed^ (all dDSv SsTt)) & (vb^u~Po) & (uCRRp) & (xb^tPNSz) & ((z~CAp SsTt) t^ ((mn d~DSx SsTt) ed^ (all d~DSx SsTt))) & ((zCAp SsTt) t^ ((mn d~DSx SsTt) ed^ (all d~DSx SsTt)))))'],\
['a','legally impossible',None,'(b=legally impossible) & (d=authorities) & (punish=PNS) & ((pIAb SsTt) x^ (((mn dDSv SsTt) ed^ (all dDSv SsTt)) & (vb^u~Po) & (uCRRp) & (xb^tPNSz) & ((zCAp SsTt) t^ ((mn dDSx SsTt) ed^ (all dDSx SsTt))) & ((z~CAp SsTt) t^ ((mn d~DSx SsTt) ed^ (all d~DSx SsTt)))))'],\
['a','legally necessary',None,'(b=legally necessary) & (d=authorities) & (punish=PNS) & ((pIAb SsTt) x^ (((mn dDSv SsTt) ed^ (all dDSv SsTt)) & (vb^u~Po) & (uCRRp) & (xb^tPNSz) & ((z~CAp SsTt) t^ ((mn d~DSx SsTt) ed^ (all d~DSx SsTt))) & ((zCAp SsTt) t^ ((mn dDSx SsTt) ed^ (all dDSx SsTt)))))'],\
['r','lesser than','LSS','(lesser than=LSS) & ((bLSSc) x^ (cAFb))'],\
['r','lie','LI','(lies about=LI) & ((bLIp|c) x^ ((bSTTp|c) & (b~Bp) & (zb^cBp) & (bDSz)))'],\
['ra','live','LV','postponed'],\
['ra','lives','LV','postponed'],\
['na','logic',None,'postponed'],\
['a','logically contingent',None,'(b=logically contingent) & ((pIAb) x^ ((pIAta^) & (nt+pIAta^)))'],\
['a','logically impossible',None,'(b=logically impossible) & ((pIAb) x^ ((nt+pPc) & ((dIGe) t^ (p~Pd)))) & (e=possible world)'],\
['a','logically necessary',None,'(b=logically necessary) & ((pIAb) x^ ((pIAta^) & (nt+p~IAta^)))'],\
['a','logically possible',None,'(b=logically possible) & (c=logically necessary) & (d=logically contingent) & ((pIAb) x^ ((pIAc) ed^ (pIAd)))'],\
['as','logically true',None,'(logically true=logically necessary)'],\
['n','lower class',None,'(d=lower) & (c=class) & (f=natural essence) & (((bIGc) & (bIAd) & (eIGb)) x^ (((zIGe) x^ (zHy)) & (yIGf) & (((xIGe) & (o~IGx)) t^ (xSw))))'],\
['rs','make','MK','(make = cause)'],\
['r','make sense','MK','(make=MK) & (c=sense|a) & (d=grammatical) & ((bMKc) x^ ((bIAd) & (bIAta^)))'],\
['a','many',None,'(z=many) & (y=2) & ((bIAz) x^ ((bNy) ed^ ((bNc) & (cAFy))))'],\
['a','many|a',None,'(c=many|a) & (((bIAc) & (eIAf)) x^ ((bNd) & (eNg) & (dAFg))) & (f=few|a)'],\
['n','material part',None,'(c=material part) & (e=sentient being) & (((bIGc) & (bOFd)) x^ ((bSz) & (dHWb) & (dIGe)))'],\
['n','material whole',None,'(c=material whole) & (e=material part) & (((bIGc) & (bOFd)) x^ ((dIGe) & (bHWd)))'],\
['r','materialize','MTL','(materialize=MTL) & (bMTL Tc) x^ ((b~EXN Td) & (bEXN Tc) & (cAd))'],\
['r','means|r',None,'((bMNc BYd TOe Tg) x^ ((bCAd Tg) & (bDSf))) & (fb^(eEXPd Tg) t^ ((eBc Th) & (hSUTg)))'],\
['as','meaningful',None,'(meaningful=significant)'],\
['a','mental',None,'(c=mental) & ((bIAc) x^ (bTKd))'],\
['aa','mental|a',None,'(c=mental) & ((bIAc) x^ ((eTKb) ed^ (bTKd)))'],\
['a','mental|b',None,'(c=mental) & ((bIAc) x^ (dTKb))'],\
['ns','moment|e',None,'(moment|e=event)'],\
['n','moment|f (first)',None,'(z=moment) & (((bIGz) & (bIAf)) x^ ((cTb) & (dAb))) & (f=first)'],\
['n','moment|l (last)',None,'(z=moment) & (((bIGz) & (bIAf)) x^ ((cTb) & (bAd))) & (f=last)'],\
['a','morally contingent',None,'(b=morally contingent) & (c=painful) & (f=acceptable) & ((pIAb e) x^ ((zCRRp) & ((yIAc) ed^ (y~IAc)) & (vb^yAFx) & (vIAd) & (zCAUy) & (ub^vIAf) & (tb^xAFnt+y) & (sb^tIAf) & ((nt+y~IAc) ed^ (nt+yIAc)) & (eBu) & (eBs)))'],\
['a','morally impossible',None,'(b=morally impossible) & (c=painful) & (d=unacceptable) & (f=acceptable) & ((pIAb e) x^ ((zCRRp) & (yIAc) & (vb^yAFx) & (vIAd e) & (zCAUy) & (ub^(vIAd e)) & (tb^xAFnt+y) & (sb^tIAf e) & ((nt+y~IAc) ed^ (nt+yIAc)) & (eBu) & (eBs)))'],\
['a','morally necessary',None,'(b=morally necessary) & (c=painful) & (d=unacceptable) & (f=acceptable) & ((pIAb e) x^ ((zCRRp) & ((yIAc) ed^ (y~IAc)) & (vb^yAFx) & (vIAd) & (zCAUy) & (ub^vIAf) & (tb^xAFnt+y) & (sb^tIAd) & (nt+yIAc) & (eBu) & (eBs)))'],\
['d','more',None,'(more...than) & ((bR mor c thn d Uf) x^ ((cNz Uf) & (dNy Uf) & (zAFy) & (bRc Uf) & (bRd Uf)))'],\
['aa','mortal',None,'postponed'],\
['r','move','MV','(bMV FRM c Td TOe Tf) x^ ((bINMc Td) & (bINMe Tf))'],\
['','move|m','MOV','(bMOVc FRM d Te TOf Tg) x^ ((bHWh.c) & (((hBk Te) & (cINMd)) t^ (cINMf Tg)))'],\
['','move|a','MVA','(bMVAc FRM d Te TOf Tg RLj) x^ ((bHWh.c) & (jINMk Te) & (jINMk Tg) & (((hBk Te) & (cINMd)) t^ (cINMf Tg)))'],\
['na','murder',None,'postponed'],\
['e','must|w',None,'(states=STT) & (c=absolutely true) & (((p must|w) & (bSTTp)) x^ ((bDSz) & (zb^pIAc)))'],\
['n','narrow reality',None,'(d=reality) & ((b=narrow reality) x^ ((zId) t^ (zIGb)))'],\
['a','natural|s (statement)',None,'(b=natural|s) & ((cIAb) x^ ((cHWd) & (dIAe) & (dIGf) & (jIGh) & (jIAg.k))) & (e=natural) & (f=subject) & (g=active) & (h=relation) & (k=non_spatio_temporal)'],\
['ns','natural essence',None,'(natural essence = essence|n)'],\
['na','natural kind ',None,'(c=natural kind) & ((bIGc) x^ ((dIGb) & (dIAe))) & (e=material)'],\
['n','natural number',None,'(c=natural number) & ((bIGc) x^ ((zNb) & ((b=0) ed^ (bAF0))))'],\
['aa','necessary',None,'(necessary = logically necessary)'],\
['r','necessary physical condition','NC','(necessary physical condition=NC) & (g=possible worlds) & (h=reality) & (((bScTd) & (eScTf) & (pNCq GVr)) x^ ((pb^eSc) & (qb^bSc) & (fSUTz) & (zSUTd)  & (((rIh) & (pTd)) t^ ((qPy Tz) & (nt+qPx Tz))) & (((rIh) & (p~Td)) t^ (q~Po Tz)) & (pP mn g)))'],\
['r','negation of','NEG','(is the negation of=NEG) & (b=contradictory) & ((pNEGq) x^ ((rb^p && q) & (rIAb)))'],\
['e','never',None,'(never=nv) & ((p nv) x^ (p~To))'],\
['ra','next to','NXT','next to: postponed'],\
['ns','non actual relationship',None,'(non actual relationship=possible relationship)'],\
['n','non_relationship',None,'(c=non_relationship) & ((bIGc) x^ (((dIGe) t^ (b~HWd)) & ((fIGg) t^ (b~HWf)))) & (g=relation) & (e=relatum)'],\
['n','non_whole',None,'(c=non_whole) & ((bIGc) x^ ((dIGe) t^ (b~HWd))) & (e=thing)'],\
['r','noun counterpart of','NCP','(is the noun counterpart of=NCP) & (is the adjective counterpart of=ACP) & ((bNCPc) x^ (cACP))'],\
['ns','number|n',None,'(number|n=natural number)'],\
['n','object|r',None,'(c=object|r) & (d=relation) & (e=noun) & ((bIGc) x^ ((zIGd) & (bIGe) & (bAWz)))'],\
['n','object|n',None,'(c=object|n) & (d=relation) & (e=thing) & ((bIGc) x^ ((bIGe) & (b~IGd)))'],\
['a','objective',None,'(b=objective) & (c=reality) & ((pIAb) x^ ((pPz) ed^ (pIc)))'],\
['as','obligatory',None,'(obligatory=morally necessary)'],\
['as','obligatory|l',None,'(obligatory|l=legally necessary)'],\
['r','occur','OC','(occur=OC) & ((pOC) x^ ((p~Id Tb) & (pId Tc) & (cAb))) & (d=reality)'],\
['ra','of|n','OFN','(((bOFNc) & (bIGd) & (cIGe)) x^ ((fHWb.c) & (fIGg))) & (g=root) & (d=noun) & (e=adjective)'],\
['ra','of|v','OFV','(((bOFVc) & (bIGd) & (cIGe)) x^ ((fHWb.c) & (fIGg))) & (g=root) & (d=verb form) & (e=noun form)'],\
['ra','of','OF','postponed'],\
['r','of|a','OFA','(of|a=OFA) & (((bOFAc) & (dACPc)) x^ (bIAd))'],\
['rs','of|c','OFC','(OFC = FLC)'],\
['r','of|c|p','OFCP','(bOFCPc) x^ (cHCPb)'],\
['r','of|f|a','OFFA','((bOFFAc) x^ (bIc)) & (bIGd) & (d=part|f)'],\
['r','of|f|m','OFFM','((bOFFMc) x^ (bIGc)) & ((bOFFMc) t^ ((bIGd) & (cIGe))) & (d=familial part|a) & (e=concept)'],\
['g','of|g','OFG','(of|g=OFG) & ((cOFGb) x^ ((bHc) ed^ (bOWNc) ed^ (bHWc)))'],\
['r','of|i','OFI','(bOFIc) x^ (cHGCb)'],\
['r','of|i|m','OFIM','((bOFIMc) x^ (cHIMb))'],\
['r','of|m','OFM','(of|m=OFM) & (d=person) & ((bOFMc) x^ ((bSz) & (cHWb) & (cIGd)))'],\
['r','of|p|w','OFPW','((bOFPWc) x^ (bPc)) & (bIGd) & (d=part|w)'],\
['r','of|r','OFQ','(of|r=OFR) & (verbal counterpart=VCP) & (((R VCP b) & (The b OFR d)) x^ (d R))'],\
['r','of|s','OFS','(of|s=OFS) & ((bOFSc) x^ (cHGb))'],\
['r','of|s|p','OFSP','(bOFSPc) x^ (cHSPb)'],\
['aa','omnipotent',None,'postponed'],\
['r','on','ON','(on=ON) & ((bONc) x^ ((bABc) & (bNXTc)))'],\
['ns','one|p',None,'(one|p = person)'],\
['a','open|r',None,'(b=open|r) & ((pIAb) x^ ((pPc) & (nt+pPd) & (p~Ie) & (nt+p~Ie))) & (e=reality|t)'],\
['r','opposite to','OPP','(opposite to=OPP) & ((bOPPc) x^ ((dFRAb) & (dFRAc))) & (dIGf) & (bIGg) & (cIGg) & (f=point) & (g=natural whole)'],\
['r','outside of','OT','(outside of=OT) & ((bOTc) x^ ((b~INc) & (bSz)))'],\
['ra','own','OWN','postponed'],\
['r','own|i','OWI','(own|i=OWI) & ((bOWIc) t^ (cAIz))'],\
['ra','owns','OWN','postponed'],\
['n','pain',None,'(c=pain) & (((bIGc) & (bTOd)) x^ ((zb^bSSy) & (dHWb) & (d~DSz)))'],\
['ns','part|d',None,'(part|d=property part)'],\
['n','part|c',None,'(c=part|c) & ((bIGc) x^ ((dHWb) x^ (dCSEe)))'],\
['ns','part|f',None,'(part|f=familial part)'],\
['n','part|s',None,'(c=part|s) & ((bIGc) x^ (bINd))'],\
['ns','part|s',None,'(part|s=physical spatial part)'],\
['a','partially material|a (property)',None,'(b=partially material|a) & ((cIAb) x^ ((dHWf) & (fIGg) & (dIAc) & (dHWh) & (hIGk))) & ((cIGb) t^ (cIGe)) & (e=property) & (g=body|c) & (k=mind)'],\
['','partially material|b (concept)',None,'(b=partially material|a) & ((cIAb) x^ ((dHWf) & (fIGg) & (dIGc) & (dHWh) & (hIGk))) & (g=body|c) & (k=mind)'],\
['ns','partially spiritual',None,'(partially spiritual = partially material|b)'],\
['r','participate','PRTC','(bPRTCc) x^ ((dCAUSc) x^ (dHWb))'],\
['na','party',None,'postponed'],\
['a','past',None,'(c=past) & (d=now) & ((bIAc) x^ (dAb))'],\
['ns','past|e',None,'(past|e=entire past)'],\
['n','period|d (discontiguous)',None,'(c=period|d) & ((bIGc) x^ ((bHWd) t^ (dIGe))) & (e=moment)'],\
['n','period (contiguous)',None,'(c=period) & ((bIGc) x^ (((kAf) & (hAk)) x^ (bHWk)))'],\
['as','permitted',None,'(permitted = morally contingent)'],\
['as','permitted|l',None,'(permitted|l=legally contingent)'],\
['n','person',None,'(c=person) & (d=personhood) & ((bIGc) x^ (bHd))'],\
['n','personhood',None,'(c=personhood) & ((bHc) t^ ((bIGd) & (zTKw) & (zDSx) & (bHWz) & (bHWy) & (yIGe))) & (d=person) & (e=body|c)'],\
['n','phenomenon',None,'(c=phenomenon) & (d=event) & ((bIGc) x^ ((bIGd) & (zIGb)))'],\
['ns','phenomenon|e',None,'(phenomenon|e=event)'],\
['n','phenomenon',None,'(phenomenon = thing)'],\
['ra','phrase',None,'postponed'],\
['a','physical|s',None,'(c=physical|s) & ((bIAc) x^ (((dHe) & (eIGg) & (dSf)) t^ (bHWf))) & (g=energy)'],\
['r','physical contingent condition','CC','(contingent physical condition=CC) & (given=GV) & (e=reality) & (f=possible worlds) & (((bScTd) & (eScTf) & (pCCq GVr)) x^ ((pb^eSc) & (qb^bSc) & (fSUTz) & (zSUTd) & (((rIe) & (pTd)) t^ ((qPy Tz) & (nt+qP x Tz))) & (((rIe) & (p~Td)) t^ ((qPw Tz) & (nt+qPv Tz))) & (pP mn f) & (wNr) & (vNq) & (yNs) & (xNt) & (rAFq) & (tAFs)))'],\
['n','physical law',None,'(c=physical law) & (d=situation) & ((bIGc) x^ ((bPo) & (bIGd)))'],\
['n','physical relationship',None,'(z=physical relationship) & (y=subject) & (x=relationship) & ((bIGz) x^ ((bHVc) & (bIGx) & (cIGy) & (eHc) & (eSf)))'],\
['n','physical spatial part',None,'(c=physical spatial part) & (((bIGc) & (bOFd)) x^ ((bSz) & (dSy) & (zINy)))'],\
['n','physical spatial whole',None,'(c=physical spatial whole) & (((bIGc) & (bOFd)) x^ ((bSz) & (dSy) & (yINz)))'],\
['n','physical temporal part',None,'(c=physical temporal part) & (((bIGc) & (bOFd)) x^ ((bTz) & (dTy) & (zDURy)))'],\
['n','physical temporal whole',None,'(c=physical temporal whole) & (((bIGc) & (bOFd)) x^ ((bTz) & (dTy) & (yDURz)))'],\
['a','physically contingent',None,'(b=physically contingent) & (c=relata) & (d=reality) & (((pSeTf) u+ (qIAb Tg)) x^ (((pSeTf) t^ ((qPx Tg) & (q~Pw Tg))) & (ySUTg) &  (gSUTf)))'],\
['a','physically impossible',None,'(b=physically impossible) & (c=relata) & (d=reality) & (((pSeTf) u+ (qIAb Tg)) x^ (((pSeTf) t^ ((q~Po Tg) & (nt+qPo Tg))) & (zCRRq) & (z~Id Ty) & (ySUTg) & (gSUTf)))'],\
['a','physically necessary',None,'(b=physically necessary) & (c=relata) & (d=reality) & (succeed|t=SUT) & (correspond=CRR) & (((pSeTf) u+ (qIAb Tg)) x^ (((pSeTf) t^ ((qPo Tg) & (nt+q~Po Tg) & (zId Ty))) & (zCRRq) & (ySUTg) & (gSUTf)))'],\
['a','physically possible',None,'(b=physically possible) & (c=physically necessary) & (d=physically contingent) & ((pIAb) x^ ((pIAc) ed^ (pIAd)))'],\
['ns','place',None,'(place=region)'],\
['n','plan',None,'(c=plan) & ((bIGc) x^ ((bDSz) & (bBy))) & (zb^bCAUc) & (yb^zPx)'],\
['n','pleasure',None,'(c=pleasure) & (((bIGc) & (bTOd)) x^ ((zb^bSSy) & (dHWb) & (bDSd)))'],\
['r','plural counterpart','PCP','(plural counterpart=PCP) & (d=plural) & (e=singular) & (f=root word) & (((bIGd) & (bOFc)) x^ ((cIGe) & (bIGz) & (cIGz) & (zIGf) & (mny bEXV)) x^ (bPCPc))'],\
['n','plural counterpart of',None,'(e=plural counterpart) & ((bPCPc) x^ ((bIGe) & (bOFc)))'],\
['n','point|s',None,'(c=point|s) & (((bIGc)) t^ ((dLFb) & (bLFe) & (((zLFd) & (eLFz)) t^ (z=b))))'],\
['a','positively infinite|g',None,'(c=positively infinite|g) & (((bIAc) & (bPCPd)) x^ (((zIGd) & (zNy)) t^ ((xIGd) & (xNw) & (wAFy))))'],\
['a','potentially|o vague (of a physical object)',None,'(b=potentially|o) & ((cIAb) x^ (cIAd)) & (d=natural|o)'],\
['a','potentially|p vague (of a property)',None,'(b=potentially|p) & (((cIAb) & (dIAc)) x^ (dIAe)) & (e=natural|o)'],\
['a','potentially|r vague (of a relation)',None,'(b=potentially|r) & (((R IAb) & (cRd)) x^ ((cIAe) & (dIAe))) & (e=natural|o)'],\
['a','potentially|v vague (of a statement)',None,'(b=potentially|v) & ((cIAb) x^ (cIAd)) & (d=natural|s)'],\
['as','precise',None,'(precise = certain)'],\
['a','predicable',None,'(c=predicable) & ((bIAc) & (bOFd)) x^ (fIAg)) & (b=Re) & (fb^dRe) & (g=consistent)'],\
['n','predicate',None,'(c=predicate) & ((bIGc) x^ ((cHWd.e) & (dIGf) & (eIGg))) & (f=relation) & (g=object)'],\
['r','predicates',None,'((bPRCc) x^ (cRd)) & (b=Rd)'],\
['n','premise',None,'(c=premise) & (((bIGc) & (bFORd)) x^ (((eIGf) t^ (enf^b)) & (gHWb) & (gi^d)))'],\
['a','present|a',None,'(c=present|a) & (d=present) & ((cACPd))'],\
['r','prevent','PRV','(prevent=PRV) & ((bPRVc) x^ ((xCRRc) & ((bSzTy) t^ (x~Po Tw)) & (wSUTy)))'],\
['n','probability',None,'(c=probability) & (g=ratio) & (h=possible worlds) & (f=reality) & (given=GV) & (((bIGc) & (bOFd GVe)) x^ ((eIf) t^ ((dPb h) & (bIGg))))'],\
['a','probable',None,'(c=probable) & ((bIAc) x^ (jAFk)) & ((eHWd) x^ (bPd)) & ((gHWh) x^ (b~Ph)) & (gNj) & (eNk)'],\
['n','proper name',None,'(c=proper name) & ((bIGc) x^ ((bIGd) & (bRFe) & (eIGf))) & (d=word) & (f=individual)'],\
['n','property|o',None,'(c=property|o) & ((bIGc) x^ (zOWNb))'],\
['n','property bearer',None,'(c=property bearer) & ((bIGc) x^ (bHz))'],\
['n','property part',None,'(c=property part) & (((bIGc) & (bOFd)) x^ ((dHb) ed^ (dIAb)))'],\
['ra','punish',None,'postponed'],\
['a','purely material|c (concept|n)',None,'(b=purely material|c) & ((cIAb) x^ ((dHWf) & (dIGc) & (fIGg) & ((hIGk) t^ (d~HWh)))) & ((cIAb) t^ (cIGe)) & (e=concept|n) & (g=body|c) & (k=mind)'],\
['n','putative mistake',None,'(d=putative mistake) & (e=reality) & (make=MK) & ((yb^cCAz) & (wb^yIe) & (((bMKc) & (cTOb) & (cIGd)) x^ ((bCAc Tw) & (zOC Tv) & (vSUTw) & ((yIe) ed^ ((yAIx) & (bHWx))) & (bBw) & (b~DSz))))'],\
['e','putatively',None,'(putatively b TOc) x^ (cBb)'],\
['n','quantity',None,'(c=quantity) & (((bIGc) & (bOFd) & (dPCPe)) x^ ((zIGe) & (zNb) & (zIAf) & (((yIGe) & (yNw)) t^ (w~AFb))))'],\
['r','raise the probability of','RAS','(raise the probability of=RAS) & ((bRASc) x^ (bCASc))'],\
['ra','ratio',None,'postponed'],\
['a','real|c',None,'(c=real|c) & ((bIAc) x^ (bHCEd))'],\
['as','real',None,'(real=actual)'],\
['ns','real|s',None,'(real|s = physical|s)'],\
['n','real group',None,'(c=real group) & (d=abstractspace) & (vb^(xIGb) e^ (xHw)) & ((bIGc) x^ ((zIGb) & (yIGb) & (vId)))'],\
['ra','real time',None,'postponed'],\
['es','really',None,'(really=actually)'],\
['r','refer','RF','((bRFc) x^ ((mTn) t^ ((jTq) & (qAn))) & (db^bIAf) & (hb^cIAf) & (jb^kTKh) & (mb^kEXPd) & (f=extant)'],\
['n','region|a',None,'(c=region|a) & ((bIGc) x^ (dINEb))'],\
['n','region|n',None,'(c=region|n) & ((bIGc) x^ (dINMb))'],\
['n','relation|n',None,'(bIGc) x^ ((dHWb.c) & (bIGe) & (cIGf) & (dIGh) & (dIAj))) & (e=noun) & (f=relation) & (h=word) & (j=root)'],\
['na','relationship',None,'(c=relationship) & ((bIGc) x^ ((bIGd) ed^ (bIGe))) & ((bIGc) x^ (bTf)) & (d=explicit|e relationship|e) & (e=implicit|i relationship|i)'],\
['rxd','resemble','RES','(b and|c cRES) x^ (bRSc)'],\
['r','resembles','RS','((bRSc) x^ (((dHWe) x^ ((bIAe) & (cIAe))) & (dIAf))) & (f=many|a)'],\
['a','respect|p',None,'postponed'],\
['r','right|a of','RIG','(right|a of=RIG) & ((bRIGc) x^ ((bSz) & (cLFz)))'],\
['r','right|b','RTE','(right|b of=RTE) & ((bRTEc) x^ ((cSz) & (zLFb)))'],\
['r','right|m of','RGT','(right|m of=RGT) & ((bRGTc) x^ ((bSz) & (cSy) & (yLFz)))'],\
['r','satisfy',None,'(((bSTSc) & (cIGd) & (c=Re)) x^ (bRe)) & (d=predicate)'],\
['r','seem','SM','(seem=SM) & (z=reality) & ((bSM TOc) x^ ((zIGc) & (zBp) & (p~Iz)))'],\
['rs','sense ',None,'(sense=EXP)'],\
['ns','sentence|r',None,'(sentence|r=relationship)'],\
['n','sentient being',None,'(sentient being = living being)'],\
['d','seventy five percent',None,'((75% b R c) x^ (k=3*j)) & ((eHWg) x^ (gRc)) & ((hHWm) x^ (m~Rc)) & (gIGb) & (mIGb) & (hNj) & (eNk))'],\
['r','share','SHR','(share=SHR) & ((b and|c cSHRd) x^ (((bHd) & (cHd)) ed^ ((bOWNd) & (cOWNd)) ed^ ((bHWd) & (cHWd))))'],\
['a','significant',None,'(b=significant) & (c=grammatical) & ((pIAb) x^ ((pIAta^) & (pIAc)))'],\
['r','similar to','SML','(similar to=SML) & (d=essence) & ((bSMLc) x^ ((bHz) & (zIGd) & (cH mn y) & (yIGz)))'],\
['n','simple individual',None,'(c=simple individual) & ((bIGc) x^ ((bSz) & ((ySx) t^ (x~INz))))'],\
['r','simultaneous with','SIM','(simultaneous with=SIM) & ((bSIMc) x^ ((bTz) & (cTz)))'],\
['n','situation',None,'(b=situation) & (c=relationship) & (d=relata) & (have=HV) & ((pIGb) x^ ((pIGc) & (zIGd) & (pHVz) & (zSy)))'],\
['ns','sort',None,'(sort=type)'],\
['nub','space',None,'(b=space) x^ ((cSd) x^ (bHWd))'],\
['ns','space|r ',None,'(space|r=region)'],\
['ns','species ',None,'(species=kind)'],\
['ns','state',None,'(state=property)'],\
['r','state','STT','(state|s=STT) & ((bSTTc) x^ ((bCAUz) & (zRFc)))'],\
['n','state of affairs',None,'(c=state of affairs) & ((bIGc) x^ ((bHWd) x^ ((dIAe) & (dIGf)))) & (f=fact)'],\
['ns','statement',None,'(statement=relationship)'],\
['rs','states',None,'(states = STT)'],\
['r','stronger than','STR','(stronger than=STR) & (f=reality) & (zb^(eIf) u+ (dCAb)) & (yb^(eIf) u+ (dCAc)) & (((bSTRc GVe) & (dDSb) & (dDSc)) x^ ((zPx) & (yPw) & (wNv) & (xNu) & (uAFv)))'],\
['ns','subgroup',None,'(subgroup=type)'],\
['n','subject',None,'(c=subject) & (d=relation) & (e=noun) & ((bIGc) x^ ((zIGd) & (bIGe) & (zAWb)))'],\
['a','succeeding',None,'(c=succeeding) & ((bIAc * d) x^ (bAd))'],\
['a','succeeding|n',None,'(c=succeeding|n) & ((bIAc * d) x^ (bAFd))'],\
['r','succeeds','SC','(succeeds=SC) & ((bSCc) x^ ((dNe) t^ ~((dAFc) & (bAFe))))'],\
['r','succeeds|m','SCM','(succeed|m=SCM) & (bSCMc) x^ ((cIGd) & (bIGd) & (cMTL Te) & (bMTL Tf) & (fAe))'],\
['r','succeeds|o','SUO','(succeed|o=SUO) & ((bSUOc) x^ ((cOC Td) & (bOC Te) & (bIGf) & (cIGf) & (eAd) & ((gIGf Th) t^ ~((eAh) & (hAd)))))'],\
['r','succeeds|p','SCP','(succeed|p=SCP) & ((bSCPc ASCd) x^ ((c=d Te) & (b=d Tf) & (fAe) & ((g=d Th) t^ (h~CBTf e))))'],\
['r','succeeds|s','SCD','(succeed|s=SCD) & ((bSCDc ASCd) x^ ((bIGd) & (cIGd) & (bSe) & (cSf) & (eDf) & ((gIGd) t^ ~((fDg) & (gDe)))))'],\
['r','succeeds|t','SUT','(succeed|t=SUT) & ((bSUTc ASCd) x^ ((eTb) & (fTc) & (bAc) & ((gTh) t^ ~((bAh) & (hAc)))))'],\
['r','succeeds|u','SCU','(succeed|u=SCU) & ((bSCUc) x^ ((dUTc Te) & (fUTb Tf) & ((f=d) ed^ (f~=d)) & (bIGg) & (cIGg) & (((hUTm Tj) & (mIGg)) t^ ~((fAj) & (jAe)))))'],\
['as','supernatural',None,'(supernatural=divine)'],\
['n','symbol',None,'(c=symbol) & ((bIGc) x^ (bRFz))'],\
['a','teleologically contingent',None,'(b=teleologically contingent) & (((cDSd) & (pIAb c)) x^ (((c~CAUp Tx) t^ ((dPu Tw) & (d~Pv))) & ((cCAUp Tx) t^ ((dPz Tw) & (d~Py Tw)))))'],\
['a','teleologically impossible',None,'(b=teleologically impossible) & (((cDSd) & (pIAb c)) x^ (((cCAUp Tx) t^ (d~Po Tw)) & ((c~CAUp Tx) t^ ((dPz Tw) & (d~Py Tw)))))'],\
['a','teleologically necessary',None,'(b=teleologicallynecessary) & (((cDSd) & (pIAb c)) x^ (((c~CAUp Tx) t^ (d~Po Tw)) & ((cCAUp Tx) t^ ((dPz Tw) & (d~Py Tw)))))'],\
['a','teleologically possible',None,'(b=teleologically possible) & (c=teleologically necessary) & (d=teleologically contingent) & ((pIAb) x^ ((pIAc) ed^ (pIAd)))'],\
['r','tend toward','TD','postponed'],\
['rs','think|t','TKT','(TKT = B)'],\
['r','think|w','TKW','((bTKWc) x^ ((bHWd) & (dTKc)))'],\
['nu','time',None,'(b=time) x^ ((eTd) x^ (bHWd))'],\
['ra','took','TAK','postponed'],\
['ns','trait ',None,'(trait=property)'],\
['a','true',None,'(c=true) & ((bIAc) x^ (bIe)) & ((bIAc) t^ (bIGf)) & (e=reality) & (f=non_meta_statement)'],\
['n','truth value',None,'(c=truth value) & (e=truth) & (f=falsehood) & ((bIGc) x^ ((bc^e) & (bc^f)))'],\
['r','try','TRY','(try=TRY) & (d=reality) & ((bTRYc) x^ ((uCRRc) & (bCAUy) & ((yId) t^ ((uPw) & (nt+uPv))) & (xb^yCAUc) & (bBx) & (bDSc)))'],\
['n','type',None,'(c=type) & (((bIGc) & (bOFd)) x^ ((zIGb) t^ (zIGd)))'],\
['a','unacceptable',None,'(b=unacceptable) & ((pIAb TO c) x^ ((zCRRp) & (yb^z~Po) & (cDSy)))'],\
['as','uncertain',None,'(vague = uncertain)'],\
['a','unique',None,'(c=unique) & ((bIAc) x^ ((dIGe) t^ (d~IGb))) & (e=thing)'],\
['ra','universe',None,'postponed'],\
['a','upper class',None,'(d=upper) & (c=class) & (f=abstract essence) & (((bIGc) & (bIAd) & (eIGb)) x^ (((zIGe) x^ (zHy)) & (yIGf) & (((xIGe) & (o~IGx)) t^ (xSw))))'],\
['ra','utters','UT','postponed'],\
['a','vague',None,'(b=vague) & (((cIAb) & (cTOd Tg)) x^ ((dTKe Tg) & (kAg) & (dTKm))) & (f=reality) & (g=now) & (eb^cIf) & (hb^d~TKe Tk) & (mb^hPj)'],\
['a','vague|o (of a physical object)',None,'(b=vague|o) & (((cIAb) & (cTOd)) x^ ((d~KNe) & (fIAg))) & (e b^ fIGc) & (g=natural)'],\
['a','vague|s (of a statement)',None,'(b=vague) & (((cIAb) & (cTOd)) x^ ((cIAe) & (d~KNc))) & (e=natural|s)'],\
['na','vague pairs',None,'postponed'],\
['r','variable space relation','D','(bDc) x^ ((bLFc) ed^ (bRTc) ed^ (bABc) ed^ (bBLc) ed^ (bFRc) ed^ (bBHc))'],\
['r','violate','VIO','(violate=VIO) & (b=action) & ((pVIOq) x^ ((zDSy) & (yb^q~Po) & (pCRRq) & (pIb) & (pIGb)))'],\
['n','void',None,'((b=void) x^ ((cIGz) t^ (c~Sb))) & (z=thing)'],\
['ra','went','GO','(GO = MOV)'],\
['rs','were|e',None,'(were|e = EX)'],\
['r','were/would',None,'(((p were) t^ (q would)) x^ ((p~Ib) & (q~Ib) & ((pPc) t^ (qPc)))) & (b=reality)'],\
['rs','while',None,'(while=DUR)'],\
['ns','while|n ',None,'(while|n=period)'],\
['aa','white',None,'postponed'],\
['n','whole|l (living)',None,'(c=whole|l) & ((bIGc) x^ ((bHWd) t^ ((dIGe) ed^ (dIGf)))) & (e=mind) & (f=whole|m)'],\
['ns','whole|m (material)',None,'(whole|m = body|c)'],\
['n','whole|n (numerical)',None,'(c=whole|n) & ((bIGc) x^ ((bHWd) t^ (dIGe))) & (e=number)'],\
['n','whole|s (spatial)',None,'(c=whole|s) & ((bIGc) x^ ((bHWd) t^ (dIGe))) & (e=point)'],\
['ns','whole|t (temporal)',None,'(whole|t = period|d)'],\
['ns','whole|v (verbal)',None,'(whole|v = word)'],\
['rs','within',None,'(within = in|e)'],\
['n','word',None,'(c=word) & ((bIGc) t^ (((bHWd) t^ (dIGe)) & (bIGf))) & (f=symbol) & (e=letter)'],\
['ns','numbers|i',None,'(numbers|i = integer)'],\
['na','7pm',None,'postponed'],\
['na','apple',None,'postponed'],\
['a','aristotelian|c',None,'(c=aristotelian|c) & (d=aristotle) & ((bIAc) x^ (bSMLd)) '],\
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
['n','chlorophyll',None,'(c=chlorophyll) & ((bIGc) t^ (b~IGd)) & (d=plastic)'],\
['aa','cold',None,'postponed'],\
['na','courtyard',None,'postponed'],\
['ra','danced','DNC','postponed'],\
['nc','dog',None,'(c=dog) & (d=doglike) & ((bIGc) x^ (bIAd))'],\
['ac','doglike',None,'(c=dog) & (d=doglike) & ((bIAd) x^ ((bIGc) & (bHWe) & (bHWg) & (eIGh) & (gIGk))) & (k=mind) & (h=body|c)'],\
['n','doglike|s',None,'(c=doglike|s) & (d=doglike) & ((bIAc) x^ ((eIAd) & (eSMLb)))'],\
['na','dogness',None,'(c=dogness) & ((bHc) x^ (bIAd)) & (d=doglike)'],\
['na','door',None,'postponed'],\
['ra','drank','DRK','postponed'],\
['ra','drink','DRK','postponed'],\
['ra','drinks','DRK','postponed'],\
['na','earth',None,'postponed'],\
['ra','eat from','ATF','postponed'],\
['ra','echolocate','ECH','postponed'],\
['ra','echolocates','ECH','postponed'],\
['na','eiffel tower',None,'(c=eiffel tower) & (d=artificial) & ((bIAc) t^ (bIAd))'],\
['na','eye',None,'(c=eye) & (d=natural) & ((bIAc) t^ (bIAd))'],\
['n','female',None,'(b=male) & (c=female) & ((dIAc) t^ (d~IAb))'],\
['a','feminine',None,'(b=feminine) & (c=female) & ((dIAb) x^ (dIGc))'],\
['a','feminine|s',None,'(b=feminine|s) & (c=female) & (((dIAb) & (eIGc)) x^ (dSMLe))'],\
['n','flower',None,'(c=flower) & ((bIGc) t^ ((bHWd) & (dIGe))) & (e=chlorophyll)'],\
['na','french',None,'postponed'],\
['na','girl',None,'postponed'],\
['aa','green',None,'postponed'],\
['na','hamlet',None,'postponed'],\
['na','head',None,'(e=natural) & (d=head) & ((bHd) t^ (bIAe))'],\
['na','heaven',None,'postponed'],\
['a','hirsute',None,'(c=hirsute) & (d=hairs) & ((bIAc SeTf) x^ (bHW mn dSeTf))'],\
['na','home',None,'postponed'],\
['na','house',None,'postponed'],\
['n','hydrogen',None,'natural'],\
['n','kennedy',None,'(b=kennedy) & ((cIGb) t^ (bIGd)) & (d=family)'],\
['a','kennedy|a',None,'(b=kennedy|a) & (c=kennedy) & (((eIAb) & (fIGe)) x^ (fIGc))'],\
['ra','kiss','KS','postponed'],\
['ra','kissed','KS','postponed'],\
['na','male',None,'(b=male) & (c=female) & ((dIAb) t^ (d~IAc))'],\
['ra','love','LOV','postponed'],\
['na','mammal',None,'postponed'],\
['n','man',None,'(b=man) & ((cIGb) x^ ((cIGd) & (cIAe))) & (d=person) & (e=male)'],\
['na','mars',None,'natural'],\
['na','moon',None,'postponed'],\
['na','movie',None,'postponed'],\
['na','munich',None,'postponed'],\
['na','nazi',None,'postponed'],\
['na','north america',None,'postponed'],\
['na','paris',None,'(c=paris) & (d=artificial) & ((bIGc) t^ (bIAd))'],\
['n','pocketwatch',None,'postponed'],\
['na','pyramid',None,'postponed'],\
['na','rain',None,'postponed'],\
['ra','raining','RAI','postponed'],\
['ra','rains','RAI','postponed'],\
['ra','reads','RD','postponed'],\
['a','red',None,'(c=red) & ((bIAc) t^ (bINMd))'],\
['n','redness',None,'(c=redness) & ((bHc) x^ (bIAd)) & (d=red)'],\
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
['r','smell','SME','((bSME) t^ (bIAc)) & (c=material)'],\
['r','smells','SME','((bSME) t^ (bIAc)) & (c=material)'],\
['ra','speak','SPK','postponed'],\
['na','speed limit',None,'postponed'],\
['ra','spied on','SPD','postponed'],\
['ra','spies on','SPD','postponed'],\
['ra','spoke','SPK','postponed'],\
['na','sprite',None,'(c=sprite) & (d=artificial) & ((bIAc) t^ (bIAd))'],\
['ra','standing','STD','postponed'],\
['ra','studied','STD','postponed'],\
['n','table',None,'artificial'],\
['na','table',None,'(c=table) & (d=artificial) & ((bIAc) t^ (bIAd))'],\
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
['n','woman',None,'(b=woman) & ((cIGb) t^ ((cIGd) & (cIAe))) & (d=person) & (e=female)'],\
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
['nun','ada',None,'((b=ada) t^ ((bIGc) & (bIGd))) & (c=woman) & (d=individual)'],\
['nun','aristotle',None,'((b=aristotle) t^ ((bIGc) & (bIGd))) & (c=man) & (d=individual)'],\
['nun','diane',None,'((b=diane) t^ ((bIGc) & (bIGd))) & (c=woman) & (d=individual)'],\
['nun','jack',None,'((b=jack) t^ ((bIGc) & (bIGd))) & (c=man) & (d=individual)'],\
['nun','jessica',None,'((b=jessica) t^ ((bIGc) & (bIGd))) & (c=woman) & (d=individual)'],\
['nun','jfk',None,'((b=jfk) t^ ((bIGc) & (bIGd))) & (c=man) & (d=individual)'],\
['nun','jim',None,'((b=jim) t^ ((bIGc) & (bIGd))) & (c=man) & (d=individual)'],\
['nun','julius caesar',None,'((b=julius caesar) t^ ((bIGc) & (bIGd))) & (c=man) & (d=individual)'],\
['nun','kiera knightley',None,'((b=kiera knightley) t^ ((bIGc) & (bIGd))) & (c=woman) & (d=individual)'],\
['nun','leibniz',None,'((b=leibniz) t^ ((bIGc) & (bIGd))) & (c=man) & (d=individual)'],\
['nun','marilyn',None,'((b=marilyn) t^ ((bIGc) & (bIGd))) & (c=woman) & (d=individual)'],\
['nun','plato',None,'((b=plato) t^ ((bIGc) & (bIGd))) & (c=man) & (d=individual)'],\
['nun','russell',None,'((b=russell) t^ ((bIGc) & (bIGd))) & (c=man) & (d=individual)'],\
['nun','socrates',None,'((b=socrates) t^ ((bIGc) & (bIGd))) & (c=man) & (d=individual)'],\
['nun','xenothon',None,'((b=xenothon) t^ ((bIGc) & (bIGd))) & (c=man) & (d=individual)'],\
['ra','am|e','EX','(am=EX)'],\
['ra','are|e','EX','(are|g=EX)'],\
['ra','be|a','IA','(be|a=IA)'],\
['r','belongs to','BLN','(bBLNc) x^ (cHWb)'],\
['rbi','desires','DS','(desires=DS)'],\
['ra','has','H','(has=H)'],\
['rbi','have|w','HW','(have|w=HW)'],\
['rbi','is|a ','IA','(is|a=IA)'],\
['rbi','is|g ','IG','(is|g=IG)'],\
['r','participated','PRTC','(bPRTCc) x^ ((dCAUSc) x^ (dHWb))'],\
['r','participates','PRTC','(bPRTCc) x^ ((dCAUSc) x^ (dHWb))'],\
['rai','think','TK','(think=TK)'],\
['rai','thinks','TK','(thinks=TK)'],\
['ra','was','=','(was = =)'],\
['ra','was|a','IA','(was|a=IA)'],\
['ra','was|g','IG','(was|g=IG)'],\
['ra','was|e','EX','(was|e = EX)'],\
['ns','whole|c (fallacious)',None,'(whole|c = concept|n)'],\
['','',None,''],\
['','',None,''],\
['','',None,''],\
['r','absorb|g','ADS','(bADSc) x^ ((b.eIGd) & (fINHh) & (bHWh) & (cCRCf) & (fIGg))) & (d=body|c) & (g=body|m)'],\
['r','correspond','CRA','(bCRAc) x^ (((bEMh Td) & (eADc Tf) & (bSg Td)) t^ ((cSSj Tf) & (fSUTd))))'],\
['r','correspond|b','CRB','(bCRBc) x^ (((dEMe Tf) & (gADe Th) & (dSb Tf)) t^ ((jSSc Tf) & (hSUTf))))'],\
['r','correspond|c','CRC','(bCRCc) x^ (((bHWd) x^ (dINMe)) & ((cHWf) x^ (fINHg)) & ((bHWh) t^ ((hCRAj) & (cHWj))) & ((cHWk) t^ ((mCRAk) & (bHWm))))) '],\
['r','experience','EXP','(bEXPc Tg) x^ ((bADSd Th) t^ ((bTKc Tg) & (cIf) & (gSUTh))) & (cb^dRe)'],\
['r','in|h','INH','(bINHc) x^ ((bHWd) x^ ((dSSe) & (cHWe)))'],\
['r','misinterpret','MSI','(bMSIc Tg) x^ ((bADSd Th) t^ ((bTKc Tg) & (c~If) & (gSUTh))) & (cb^dRe)'],\
['r','think|d','TKD','(bTKDc) x^ (cId)'],\
['n','body|m',None,'(c=body|m) & ((bIGc) x^ ((bHWd) t^ (dIGe))) & (e=particle|m)'],\
['n','boson',None,'(c=boson) & ((bIGc) x^ (dEMb)) & ((bIGc) x^ (eADb)) & ((bIGc) t^ (bIGg)) & (g=particle)'],\
['n','fermion',None,'(c=fermion) & ((bIGc) x^ (bEMd)) & ((bIGc) x^ (bADe)) & ((bIGc) t^ (bIGg)) & (g=particle)'],\
['rs','perceive',None,'(perceive = absorb|g)'],\
['r','hallucinate','HLC','(bHLCc Td) x^ ((bEMSe Tf) t^ ((bTKk Tg) & (gSUTf) & (cIAj) & (c~Ih))) & (j=natural|s) & (kb^cIh)'],\
['r','emit|s','EMS','(bEMSc) x^ ((cHWd) x^ ((eEMd) & (bHWe)))'],\
['rb','absorb','AD','(c=boson) & ((bIGc) x^ (eADb)) & ((eIGd) x^ (eADf)) & (d=fermion)'],\
['rb','emit','EM','(c=fermion) & ((bIGc) x^ (bEMd)) & (e=boson) & ((dIGe) x^ (bEMd))'],\
['n','subset',None,'(c=subset) & (((bIGc) & (bOFd)) x^ ((bHWe) t^ (dHWe)) & ((dHWf) t^ ((gPh) & (nt+gPj))) & (gb^bHWf)'],\
['n','superset',None,'(c=superset) & (((bIGc) & (bOFd)) x^ ((dHWe) t^ (bHWe)) & ((bHWf) t^ ((gPh) & (nt+gPj))) & (gb^dHWf)'],\
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
