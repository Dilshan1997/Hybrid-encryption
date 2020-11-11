# Hybrid-encryption
## Main contents of the project

1. What is the hybrid system and cryptography schema
2. RSA implementation 
3. AES/DES implementation 
4. Hybrid implementation 
5. GUI
6. Demonstration
7. Presantation

## Presentation
1. Introduction
2. About RSA Algorithm
3. About AES Algorithm
4. About DES Algorithm
5. About hybrid system
6. Analytical informations
7. Conclusions

**GCM mode**

Galois/Counter Mode, defined in NIST SP 800-38D. It only works in combination with a 128 bits cipher like AES.

The new() function at the module level under Crypto.Cipher instantiates a new GCM cipher object for the relevant base algorithm.

Crypto.Cipher.<algorithm>.new(key, mode, *, nonce=None, mac_len=None)
Create a new GCM object, using <algorithm> as the base block cipher.

Parameters:	
key (bytes) – the cryptographic key
mode – the constant Crypto.Cipher.<algorithm>.MODE_GCM
nonce (bytes) – the value of the fixed nonce. It must be unique for the combination message/key. If not present, the library creates a random nonce (16 bytes long for AES).
mac_len (integer) – the desired length of the MAC tag, from 4 to 16 bytes (default: 16).
Returns:	
a GCM cipher object

The cipher object has a read-only attribute nonce.
