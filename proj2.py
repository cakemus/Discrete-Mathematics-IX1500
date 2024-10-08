import sympy

n = 126456119090476383371855906671054993650778797793018127
e = 7937

cipher = [71813256693940924296894077934214561172810879712474411, 
9448822287828090646994864850737396938193829207476291, 
88668970435389288697377439396925326741948237682465270, 
86506877126882849406016686638047102838609248170576618, 
16709897999784737136957685475437549241701090506782283, 
112082150953644879808862406205324790087623126644040573, 
101300870021945928543132671557050279918096489651239300, 
32937734818698596498554567892462717857351635451752837, 
103250795649561696933993996191026658588156558009063626, 
9944688399741552477615864010579036184245783411883057, 
119023583366882743798043931890543936842945498718476068, 
80592157601474287498990443067778705256100803395677817, 
102380508653117028882619903124827386257126674349361274, 
29811966446563529123471275226007901312118773446042793, 
92762330649448230399110375463713210616117461806861915, 
52785580108219931044518308758110100269607232524031605, 
96630768452430661169900035905564353166088443035700946, 
104675165348205433706999623683285417639543643952502324, 
40951632727878687548912007343839372258522783062745255, 
3439648578841960331931477586254936252926807061184128, 
92627296356479225180584868594165589614134261562166537, 
17702026915107984931197975326852130481340232863388490, 
35046202376732485019333999169687110582305137751148612, 
77294680692381954105730803435472597801358963832333113, 
58483888921987241464318109604079587034521404720554634, 
36276638436400152414964124035009391520390748123243684, 
51639523466890776909441678913110130114797820309131676, 
88728872239148972759884018820709080618086999507011767, 
45676147252256101340528647372987947783315245082701701, 
23720650117296688653687823869949231140410366974406435, 
116873909796842028543216809278057888647421675552833624, 
48366928605018172969920839968881382332820063246862564, 
35425491594411738404916586785616696655411948001887947, 
40450505118769549506412191479348341185611602935328569, 
107418270783831708663699380219027152916779513788697702, 
101200673359310801145084267798164209444861857835311695, 
65616489296627251359500608540483019164860755372512518, 
11847413450576524199351895472796724862275584777010578, 
2731217915540071371661447436484606877270200777923464, 
10599418784042349226543806726994624123223235946860821]

#factor n using factorint() to find p, q and find phi(n) using the Euler's Totient Function (p - 1) * (q - 1)
factors = sympy.factorint(n)
print("sympy.factorint(n): ", factors)
primes = list(factors.keys())
print("list(factors.keys()): ", primes)
if len(primes) != 2:
    raise ValueError("n is not a product of two primes.")
p, q = primes
phi_n = (p - 1) * (q - 1)

#find the private key d using modular inverse of e mod phi(n)
d = sympy.mod_inverse(e, phi_n)

#decrypt each ciphertext block using calculated d
def decrypt_block(c, d, n):
    return pow(c, d, n)

#decrypt all blocks in cipher going backwards one block at a time using the decrypt_block() function above
decrypted_message = [decrypt_block(c, d, n) for c in cipher[::-1]] #[::-1] goes backwards in the cipher


plaintext_bytes = b''

block_size = (n.bit_length() + 7) // 8 #+7 to round up the number of bytes if needed
for m in decrypted_message:
    m_bytes = m.to_bytes(block_size, 'big')
    plaintext_bytes += m_bytes #accumulate the byte strings from each decrypted block

print(f"decrypted_message: {decrypted_message}")
print(f"plaintext_bytes: {plaintext_bytes}")
#decode the accumulated bytes to text
try:
    plaintext = plaintext_bytes.decode('utf-8')
except UnicodeDecodeError:
    plaintext = plaintext_bytes.decode('latin-1')

print("Decrypted message:")
plaintext = plaintext[::-1] #to reverse order of text
print(plaintext)