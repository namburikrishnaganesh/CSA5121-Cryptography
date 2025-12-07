def substitute(symbol):
    mapping = {
        '†': 'E',
        '‡': 'T',
        '(': 'H',
        ')': 'E',
        '*': 'S',
        ';': 'O',
        '8': 'N',
        '4': 'A',
        '5': 'R',
        '6': 'D',
        '2': 'L',
        '3': 'M',
        '0': 'C',
        '1': 'U',
        '9': 'I',
        '—': 'Y',
        ':': 'G',
        ']': 'B',
        '?': 'F',
        '.': 'P',
        '¶': 'K',
    }
    return mapping.get(symbol, symbol)
ciphertext = (
    "53‡‡†305))6*;4826)4‡.)4‡);806*;48†8¶60))85;;]8*;:"
    "‡*8†83(88)5*†;46(;88*96*?;8)*‡(;485);5*†2:*‡(;4956*2"
    "(5*—4)8¶8*;4069285);)6†8)4‡‡;1(‡9;48081;8:8‡1;48†85;"
    "4)485†528806*81(‡9;48;(88;4(‡?34;48)4‡;161;:188;‡?;"
)
plaintext = ''.join(substitute(ch) for ch in ciphertext)
print("Decrypted Output (partially mapped):")
print(plaintext)
