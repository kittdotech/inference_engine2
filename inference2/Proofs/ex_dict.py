#
#
# dict2= [['rbt','above','AB','((bIGc) x^ (dABb)) & ((bIGc) x^ (bABe)) & (c=point)'],\
# ['rbt','after|n ','AF','((bIGc) x^ (dAFb)) & ((bIGc) x^ (bAFe)) & (c=number)'],\
# ['rbt','after ','A','((bIGc) x^ (dAb)) & ((bIGc) x^ (bAe)) & (c=moment)'],\
# ['rbi','are|a','IA','((bIAc) x^ (cIGd)) & ((bIAc) t^ (bIGe)) & ((bIAc) t^ (cIGf)) & (d=property) & (e=thing) & (f=adjective)'],\
# ['rbi','are|g ','IG','((bIGc) x^ (cIGd)) & ((eIGf) x^ (eIGg)) & (d=concept|n) & (g=instance)'],\
# ['rbis','at','S','((bIGc) x^ (dSb)) & ((dIGf) x^ (dSb)) & (c=point) & (f=particle) '],\
# ['rbi','at|i ','AI','((dAIb) t^ (dIGc)) & ((bIGf) x^ (dAIb)) & (c=relationship) & (f=imagination) '],\
# ['rbi','at|n ','N','((bIGc) x^ (dNb)) & ((eIGf) x^ ((eNh) & (hAFg))) & ((jIGk) x^ (mNg)) & ((nIGo) x^ (nNp)) & (f=whole) & (c=number) & (g=1) & (k=individual) & (p=0) & (o=contradiction) '],\
# ['rbi','at|p ','P','((dPb) t^ (dIGc)) & ((bIGf) x^ (dPb)) & (c=relationship) & (f=possible world) '],\
# ['rbit','at|t ','T','((dTb) t^ (dIGc)) & ((bIGf) x^ (dTb)) & (c=relationship) & (f=moment) '],\
# ['rbi','desire','DS','((dDSb) t^ ((bIGc) & (bIAe))) & ((bIGf) x^ (dDSb)) & (c=relationship) & (f=mind) & (e=open|r)'],\
# ['r','have','H','((bHc) x^ (cIGd)) & ((bHc) t^ (bIGe)) & ((bHc) t^ (cIGf)) & (d=property|n) & (e=thing) & (f=noun)'],\
# ['rbi','has|w ','HW','((bIGc) x^ (bHWd)) & ((dIGe) x^ (bHWd)) & (d=whole) & (e=part)'],\
# ['rbts','in front of','FR','((bIGc) x^ (dFRb)) & ((bIGc) x^ (bFRe)) & (c=point)'],\
# ['rbts','left of','LF','((bIGc) x^ (dLFb)) & ((bIGc) x^ (bLFe)) & (c=point)'],\
# ['rbi','think about','TK','((bTKd) t^ (dIGc)) & ((bIGf) x^ (bTKd)) & (c=relationship) & (f=mind) '],\
# ['n','concept|n',None,'(c=concept|n) & ((bIGc) x^ (zIGb)) & ((bIGc) t^ (bIGe)) & (e=non_whole)'],\
# ['n','instance',None,'(c=instance) & ((bIGc) x^ (bIGd))'],\
# ['n','integer',None,'(c=integer) & ((bIGc) x^ (bAFd)) & ((bIGc) x^ (eAFb)) & ((bIGc) x^ (fNb)) & ((bIGc) t^ (bIGg)) & (g=non_whole)'],\
# ['n','mind',None,'(c=mind) & ((bIGc) t^ (bTKz))'],\
# ['n','moment',None,'(c=moment) & ((bIGc) x^ (dTb)) & ((bIGc) x^ (bAh)) & ((bIGc) x^ (eAb)) & ((bIGc) t^ (bIGf)) & (f=non_whole)'],\
# ['n','part',None,'(c=part) & ((bIGc) x^ (dHWb))'],\
# ['n','part|p',None,'(c=part|p) & (((bIGc) & (bOFd)) x^ (dHWb))'],\
# ['n','particle',None,'(c=particle) & ((bIGc) x^ (bSd)) & ((bIGd) x^ (hTg)) & ((bIGc) t^ (bIGf)) & (f=non_whole) & (g=now) & (hb^bSd)'],\
# ['n','point',None,'(c=point) & ((bIGc) x^ (dSb)) & ((bIGc) x^ (eABb)) & ((bIGc) x^ (bABm)) & ((bIGc) x^ (fFRb)) & ((bIGc) x^ (bFRj)) & ((bIGc) x^ (gLFb)) & ((bIGc) x^ (bLFk)) & ((bIGc) t^ (bIGh)) & (h=non_whole)'],\
# ['n','property',None,'(c=property) & ((bIGc) x^ (dIAb)) & ((bIGc) t^ (bIGe)) & (e=non_whole)'],\
# ['n','property|n',None,'(c=property|n) & ((bIGc) x^ (dHb)) & ((bIGc) t^ (bIGe)) & (e=non_whole)'],\
# ['na','thing',None,'See atomic categories'],\
# ['n','thought',None,'(c=thought) & ((bIGc) x^ (dTKb)) & ((bIGc) t^ (bIGe)) & ((bIGc) x^ (bAIf)) & (e=relationship)'],\
# ['n','whole',None,'(c=whole) & ((bIGc) x^ (bHWd))'],\
# ['na','plural form',None,'indefinable'],\
# ['rai','relational variable','R','indefinable'],\
# ['ns','set',None,'(set = whole)'],\
# ['ns','class',None,'(class = concept|n)'],\
# ['ns','concept|a',None,'(concept|a = property)'],\
# ['r','exist','EX','(exist=EX) & ((bEX) x^ (bIAc)) & (c=extant)'],\
# ['ns','group',None,'(group = whole)'],\
# ['a','material',None,'(c=material) & (d=particle) & ((bIAc) x^ (bIGd))'],\
# ['ns','number|i',None,'(number|i=integer)'],\
# ['as','physical ',None,'(physical=material)'],\
# ['ns','universal',None,'(universal = concept|n)'],\
# ['rbt','is','=','(is = =)'],\
# ['lb','then',None,'(then = i^)'],\
# ['u','that|c',None,'(it IA p that q) x^ (qIAp)'],\
# ['na','there',None,'(there EX b) x^ (bEX)'],\
# ['na','this|n',None,'(this|n Rc) x^ (bRc)'],\
# ['u','which',None,'(bRc which Qd) x^ ((bRc) & (cQd))'],\
# ['u','who',None,'((bRc who Qd) x^ ((bRc) & (cQd) & (bIGe))) & (e=person)'],\
# ['b','a|r',None,'redundant'],\
# ['b','an|r',None,'redundant'],\
# ['b','did',None,'redundant'],\
# ['b','do',None,'redundant'],\
# ['b','does',None,'redundant'],\
# ['b','if',None,'redundant'],\
# ['b','is|r',None,'redundant'],\
# ['b','is|r',None,'redundant'],\
# ['b','itself|r',None,'redundant'],\
# ['b','of|r',None,'redundant'],\
# ['b','on|r',None,'redundant'],\
# ['b','same',None,'redundant'],\
# ['dr','the|r',None,'redundant'],\
# ['b','was|r',None,'redundant'],\
# ['b','will|r',None,'redundant'],\
# ['b','b^',None,'The symbol to the left of b^ is an abbreviation of the symbols on the right which are relationships'],\
# ['r','=',None,'(b=c) means wherever we see b we may replace it with c and vice_versa'],\
# ['ra','zzz',None,'(bzzzc) means we may not replace b with c and vice_versa'],\
# ['b','nt+',None,'(nt+p t^ (pIGc)) & (c=relationship) & (qIAd) & (qb^p&nt+p) & (d=consistent)'],\
# ['m','not',None,'~'],\
# ['a','~',None,'(~p t^ (pIGc)) & (c=relationship) & (qIAd) & (qb^p&~p) & (d=contradictory)'],\
# ['c','and|c',None,'(b and|c c R d) x^ (b.cRd)'],\
# ['m','not|i',None,'(not|i = nt+)'],\
# ['nu','2',None,'((b=2) x^ ((cAFb) & (bAFe))) & (c=3) & (e=1)'],\
# ['ddi','a',None,'((a bRc) x^ ((zRc) & (zIGb) & (zIAe))) & (e=indefinite)'],\
# ['ddi','a|a',None,'((a|a bRc) x^ ((zRc) & (zIGb) & (zIAe))) & (e=general)'],\
# ['ddi','any',None,'((any bRc) x^ (((zIGb) t^ (zRc)) & (zIAe) & (yIGb) & (yIAd))) & (d=particular) & (e=general)'],\
# ['dt','any|n',None,'(b~R any|n c) x^ (bR no c)'],\
# ['ds','every',None,'(every=any)'],\
# ['dd','many|n',None,'(((many|n bRc) & (bOFPd) & (bIGe)) x^ ((zIGd) & (zRc) & (zIAg) & (yIGd) & (y~Rc) & (yIAg) & (yIAf) & (zIAf) & (yIAh) & (zIAh) & (y zzz z))) & (e=plural form) & (f=indefinite) & (g=many) & (h=particular)'],\
# ['dd','many|o',None,'(((many|o bIGc) & (bOFPd) & (bIGe) & (cOFPf) & (cIGe)) x^ ((zIGf) & (zIGd) & (zIAd) & (yIGd) & (y~IGf) & (yIAd) & (zIAh) & (yIAh))) & (e=plural form) & (g=many) & (h=indefinite)'],\
# ['dd','no',None,'(((no bRc) & (bIGy) & (bOFPd)) x^ ((xIAe) & (xIGd) & (zIAf) & ((zIGd) t^ (z~Rc)))) & (y=plural form) & (e=indefinite) & (f=general)'],\
# ['d','no|s',None,'((no|s bRc) x^ (((zIGb) t^ (z~Rc)) & (yIGb) & (zIAe) & (yIAd))) & (d=indefinite) & (e=general)'],\
# ['ddi','the',None,'((the bRc) x^ ((zRc) & (zIGb) & (zIAe))) & (e=definite)'],\
# ['ws','anyone',None,'(anyone = any person)'],\
# ['ws','anything',None,'(anything = any thing)'],\
# ['ws','anything|a',None,'(anything|a = a|a thing)'],\
# ['ws','everyone',None,'(everyone = any person)'],\
# ['ws','nothing',None,'(nothing = no|s thing)'],\
# ['ds','some',None,'(some=a)'],\
# ['ds','some|o',None,'(some|o = many|o)'],\
# ['ds','some|p',None,'(some|p = many|n)'],\
# ['ws','something',None,'(something = a thing)'],\
# ['ws','something',None,'(something = a thing)'],\
# ['ws','something|a',None,'(something|a = a|a thing)'],\
# ['ds','that|d',None,'(that|d=the)'],\
# ['ds','this',None,'(this=the)'],\
# ['p','he',None,'(d=person) & (e=male) & ((he Rb) t^ ((cRb) & (cIAe) & (cIGd))) & (g=definite) & (h=particular)'],\
# ['q','his',None,'((his bRc) t^ ((zRc) & (zIGb) & (dOWNz))) & (d=he)'],\
# ['p','i',None,'(d=person) & ((i Rb) t^ ((iIGd) & (iIAg))) & (g=definite)'],\
# ['p','it|p',None,'propositional it'],\
# ['q','its|a',None,'(bR its|a c) t^ ((zIGc) & (bHMz) & (bRz))'],\
# ['q','its|b',None,'((b R its|b c) t^ ((zIGd) & (bHMz) & (bRz))) & ((b R its|b c) t^ ((cOFPd) & (cIGe))) & (e=plural form)'],\
# ['q','my',None,'((my bRc) t^ ((zRc) & (zIGb) & (iOWNz)))'],\
# ['p','you',None,'(d=person) & ((you Rb) t^ ((cRb) & (cIGd) & (cIAg))) & (g=definite)'],\
# ['q','your',None,'(e=person) & ((your bRc) t^ ((zRc) & (zIGb) & (dOWNz))) & (d=you)'],\
# ['ra','about','ABT','postponed'],\
# ['rc','as','AS','(as=AS) & (((bASc) & (dRb)) x^ (cRb))'],\
# ['r','believe','B','(believe=B) & ((bBc) x^ (bTKd)) & ((bBc) t^ (bTKc)) & (e=true) & (db^cIAe)'],\
# ['na','body|c',None,'(c=body|c) & ((bIGc) x^ ((bHWd) t^ (dIGe))) & (e=particle)'],\
# ['ra','breaks','BRK','postponed'],\
# ['na','causal role',None,'postponed'],\
# ['ra','cause','CA','((pCAq) x^ ((bRc INMd Te) t^ ((fQg INMj Th) & (dCTGj) & (hSUTe)))) & (pb^bRc INMd) & (qb^fQg INMj)'],\
# ['n','courage',None,'(b=courage) & ((cHb) x^ (cIAd)) & (d=courageous)'],\
# ['na','courageous',None,'postponed'],\
# ['aa','definite',None,'(definite = individual)'],\
# ['rs','distinct from',None,'(distinct from = zzz)'],\
# ['r','exists','EX','(exists=EX) & ((bEX) x^ (bIAc)) & (c=extant)'],\
# ['n','familial part',None,'(c=familial part) & (((bIGc) & (bOFd)) x^ (bIGd))'],\
# ['na','family',None,'postponed'],\
# ['rs','from|b',None,'(from|b = born)'],\
# ['r','has|c|r (causal role)','HCA','((bHCAc) x^ (bCAc)) & ((bHCAc) t^ (bHc))'],\
# ['r','has|g|c','HGC','(cHGCb) x^ ((cHWe) t^ (eIGb))'],\
# ['r','has|m','HM','(have|m=HM) & ((bHMc) x^ (cIGb))'],\
# ['r','has|t','HAT','(have|t = HAT) & ((bHATc) x^ (cTCHb))'],\
# ['r','have|t','HAT','(have|t = HAT) & ((bHATc) x^ (cTCHb))'],\
# ['ra','have|w','HW','(c=body) &  (((bHWz) & (zIGc)) x^ (zSy))'],\
# ['ratso','in','IN','((bINc) x^ ((bIGd) & (cHWb))) & (d=point)'],\
# ['r','in|b','INB','((bINBc) x^ ((cHWb) & (bIGd))) & (d=moment)'],\
# ['r','in|e','INE','(bINEc) x^ ((bSd) & (cHWd))'],\
# ['r','in|m','INM','(bINMc) x^ ((bHWd) x^ ((dSe) & (cHWe)))'],\
# ['nk','individual',None,'(b=individual) & ((cIGb) x^ (((dIGe) t^ (d~IGc)) & (cIAf) & ((d zzz c) x^ (d~IAf)))) & (e=thing)'],\
# ['rs','inside',None,'(inside = INE)'],\
# ['ra','is|e','EX','((bEX) x^ (bIAc)) & (c=extant)'],\
# ['aa','large',None,'postponed'],\
# ['ra','lives','LV','postponed'],\
# ['na','logic',None,'postponed'],\
# ['a','many',None,'(z=many) & (y=2) & ((bIAz) x^ ((bNy) ed^ ((bNc) & (cAFy))))'],\
# ['a','mental',None,'(c=mental) & ((bIAc) x^ (bTKd))'],\
# ['a','mental|b',None,'(c=mental) & ((bIAc) x^ (dTKb))'],\
# ['na','murder',None,'postponed'],\
# ['n','non_whole',None,'(c=non_whole) & ((bIGc) x^ ((dIGe) t^ (b~HWd))) & (e=thing)'],\
# ['ra','of|p','OFP','(((bOFPc) & (bIGd) & (cIGe)) x^ ((fHWb.c) & (fIGg))) & (g=root) & (d=plural form) & (e=singular form)'],\
# ['ra','of','OF','postponed'],\
# ['r','of|i','OFI','(bOFIc) x^ (cHGCb)'],\
# ['r','on','ON','(on=ON) & ((bONc) x^ ((bABc) & (bNXTc)))'],\
# ['ns','one|p',None,'(one|p = person)'],\
# ['ra','own','OWN','postponed'],\
# ['ns','part|f',None,'(part|f=familial part)'],\
# ['a','partially material|a (property)',None,'(b=partially material|a) & ((cIAb) x^ ((dHWf) & (fIGg) & (dIAc) & (dHWh) & (hIGk))) & ((cIGb) t^ (cIGe)) & (e=property) & (g=body|c) & (k=mind)'],\
# ['na','party',None,'postponed'],\
# ['n','person',None,'(c=person) & (d=personhood) & ((bIGc) x^ (bHd))'],\
# ['n','personhood',None,'(c=personhood) & ((bHc) t^ ((bIGd) & (zTKw) & (zDSx) & (bHWz) & (bHWy) & (yIGe))) & (d=person) & (e=body|c)'],\
# ['n','region|a',None,'(c=region|a) & ((bIGc) x^ (dINEb))'],\
# ['nu','time',None,'(b=time) x^ ((eTd) x^ (bHWd))'],\
# ['ra','took','TAK','postponed'],\
# ['a','true',None,'(c=true) & ((bIAc) x^ (bIe)) & ((bIAc) t^ (bIGf)) & (e=reality) & (f=non_meta_statement)'],\
# ['aa','white',None,'postponed'],\
# ['ns','members',None,'(members = parts)'],\
# ['ns','numbers|i',None,'(numbers|i = integers)'],\
# ['ra','ate','ATE','postponed'],\
# ['ra','ate from','ATF','postponed'],\
# ['na','ball',None,'postponed'],\
# ['ra','born','BRN','postponed'],\
# ['na','boy',None,'postponed'],\
# ['ra','broke','BRK','postponed'],\
# ['na','cake',None,'postponed'],\
# ['na','casablanca',None,'postponed'],\
# ['na','cat',None,'postponed'],\
# ['aa','caught',None,'postponed'],\
# ['aa','cold',None,'postponed'],\
# ['nc','dog',None,'(c=dog) & (d=doglike) & ((bIGc) x^ (bIAd))'],\
# ['ac','doglike',None,'(c=dog) & (d=doglike) & ((bIAd) x^ ((bIGc) & (bHWe) & (bHWg) & (eIGh) & (gIGk))) & (k=mind) & (h=body|c)'],\
# ['na','door',None,'postponed'],\
# ['ra','drank','DRK','postponed'],\
# ['ra','drink','DRK','postponed'],\
# ['ra','drinks','DRK','postponed'],\
# ['na','earth',None,'postponed'],\
# ['ra','eat from','ATF','postponed'],\
# ['na','girl',None,'postponed'],\
# ['aa','green',None,'postponed'],\
# ['na','hamlet',None,'postponed'],\
# ['na','house',None,'postponed'],\
# ['n','kennedy',None,'(b=kennedy) & ((cIGb) t^ (bIGd)) & (d=family)'],\
# ['a','kennedy|a',None,'(b=kennedy|a) & (c=kennedy) & (((eIAb) & (fIGe)) x^ (fIGc))'],\
# ['ra','kiss','KS','postponed'],\
# ['ra','kissed','KS','postponed'],\
# ['na','male',None,'(b=male) & (c=female) & ((dIAb) t^ (d~IAc))'],\
# ['ra','love','LOV','postponed'],\
# ['n','man',None,'(b=man) & ((cIGb) x^ ((cIGd) & (cIAe))) & (d=person) & (e=male)'],\
# ['na','mars',None,'natural'],\
# ['na','movie',None,'postponed'],\
# ['na','munich',None,'postponed'],\
# ['na','nazi',None,'postponed'],\
# ['ra','reads','RD','postponed'],\
# ['a','red',None,'(c=red) & ((bIAc) t^ (bINMd))'],\
# ['n','redness',None,'(c=redness) & ((bHc) x^ (bIAd)) & (d=red)'],\
# ['aa','rewarded',None,'postponed'],\
# ['ra','saw','SEE','postponed'],\
# ['ra','see','SEE','postponed'],\
# ['na','set theory',None,'postponed'],\
# ['ra','shed','SHD','postponed'],\
# ['aa','smart',None,'postponed'],\
# ['r','smell','SME','((bSME) t^ (bIAc)) & (c=material)'],\
# ['r','smells','SME','((bSME) t^ (bIAc)) & (c=material)'],\
# ['na','speed limit',None,'postponed'],\
# ['ra','spied on','SPD','postponed'],\
# ['ra','spies on','SPD','postponed'],\
# ['ra','studied','STD','postponed'],\
# ['ra','teach','TCH','postponed'],\
# ['na','teacher',None,'postponed'],\
# ['na','tear',None,'postponed'],\
# ['na','van',None,'postponed'],\
# ['na','water',None,'postponed'],\
# ['n','woman',None,'(b=woman) & ((cIGb) t^ ((cIGd) & (cIAe))) & (d=person) & (e=female)'],\
# ['nm','beers',None,'plural of beer'],\
# ['ns','groups',None,'(groups = wholes)'],\
# ['nm','instances',None,'plural of instance'],\
# ['nm','integers',None,'plural of integer'],\
# ['nm','minds',None,'plural of mind'],\
# ['nm','moments',None,'plural of moment'],\
# ['nm','parts',None,'plural of part'],\
# ['nm','points',None,'plural of point'],\
# ['nm','tears',None,'plural of tear'],\
# ['nm','thoughts',None,'plural of thought'],\
# ['nm','wholes',None,'plural of whole'],\
# ['nu','ada',None,'((b=ada) t^ ((bIGc) & (bIGd))) & (c=woman) & (d=individual)'],\
# ['nu','aristotle',None,'((b=aristotle) t^ ((bIGc) & (bIGd))) & (c=man) & (d=individual)'],\
# ['nu','jessica',None,'((b=jessica) t^ ((bIGc) & (bIGd))) & (c=woman) & (d=individual)'],\
# ['nu','jfk',None,'((b=jfk) t^ ((bIGc) & (bIGd))) & (c=man) & (d=individual)'],\
# ['nu','jim',None,'((b=jim) t^ ((bIGc) & (bIGd))) & (c=man) & (d=individual)'],\
# ['nu','julius caesar',None,'((b=julius caesar) t^ ((bIGc) & (bIGd))) & (c=man) & (d=individual)'],\
# ['nu','leibniz',None,'((b=leibniz) t^ ((bIGc) & (bIGd))) & (c=man) & (d=individual)'],\
# ['nu','marilyn',None,'((b=marilyn) t^ ((bIGc) & (bIGd))) & (c=woman) & (d=individual)'],\
# ['nu','plato',None,'((b=plato) t^ ((bIGc) & (bIGd))) & (c=man) & (d=individual)'],\
# ['nu','russell',None,'((b=russell) t^ ((bIGc) & (bIGd))) & (c=man) & (d=individual)'],\
# ['nu','socrates',None,'((b=socrates) t^ ((bIGc) & (bIGd))) & (c=man) & (d=individual)'],\
# ['nu','xenothon',None,'((b=xenothon) t^ ((bIGc) & (bIGd))) & (c=man) & (d=individual)'],\
# ['ra','be|a','IA','(be|a=IA)'],\
# ['rbi','desires','DS','(desires=DS)'],\
# ['ra','has','H','(has=H)'],\
# ['rbi','is|a ','IA','(is|a=IA)'],\
# ['rbi','is|g ','IG','(is|g=IG)'],\
# ['rai','think','TK','(think=TK)'],\
# ['rai','thinks','TK','(thinks=TK)'],\
# ['ra','was','=','(was = =)'],\
# ['ra','was|a','IA','(was|a=IA)'],\
# ['ra','was|g','IG','(was|g=IG)'],\
# ['ns','whole|c (fallacious)',None,'(whole|c = concept|n)'],\
# [None,None,None,None]]