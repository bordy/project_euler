"""
Project Euler Problem #8
=========================

Find the greatest product of five consecutive digits in the 1000-digit
number.

            73167176531330624919225119674426574742355349194934
            96983520312774506326239578318016984801869478851843
            85861560789112949495459501737958331952853208805511
            12540698747158523863050715693290963295227443043557
            66896648950445244523161731856403098711121722383113
            62229893423380308135336276614282806444486645238749
            30358907296290491560440772390713810515859307960866
            70172427121883998797908792274921901699720888093776
            65727333001053367881220235421809751254540594752243
            52584907711670556013604839586446706324415722155397
            53697817977846174064955149290862569321978468622482
            83972241375657056057490261407972968652414535100474
            82166370484403199890008895243450658541227588666881
            16427171479924442928230863465674813919123162824586
            17866458359124566529476545682848912883142607690042
            24219022671055626321111109370544217506941658960408
            07198403850962455444362981230987879927244284909188
            84580156166097919133875499200524063689912560717606
            05886116467109405077541002256983155200055935729725
            71636269561882670428252483600823257530420752963450
"""

num= '731671765313306249192251196744265747423553491949349\
    698352031277450632623957831801698480186947885184385\
    861560789112949495459501737958331952853208805511125\
    406987471585238630507156932909632952274430435576689\
    664895044524452316173185640309871112172238311362229\
    893423380308135336276614282806444486645238749303589\
    072962904915604407723907138105158593079608667017242\
    712188399879790879227492190169972088809377665727333\
    001053367881220235421809751254540594752243525849077\
    116705560136048395864467063244157221553975369781797\
    784617406495514929086256932197846862248283972241375\
    657056057490261407972968652414535100474821663704844\
    031998900088952434506585412275886668811642717147992\
    444292823086346567481391912316282458617866458359124\
    566529476545682848912883142607690042242190226710556\
    263211111093705442175069416589604080719840385096245\
    544436298123098787992724428490918884580156166097919\
    133875499200524063689912560717606058861164671094050\
    775410022569831552000559357297257163626956188267042\
    8252483600823257530420752963450'

biggest = 0
i = 0
while i < (len(num) - 4):
    one = int(num[i])
    two = int(num[i+1])
    thr = int(num[i+2])
    fou = int(num[i+3])
    fiv = int(num[i+4])
    product = one * two * thr * fou * fiv
    if biggest < product:
        biggest = product
    i += (i+1)

print(biggest)