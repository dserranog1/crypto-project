# Type of algorithm globals
CLASSICS = "classics"
SELECTION = "selection"
OTRO = "otro"

# Common events / elements
CLEAR_TEXT_INPUT_BOX = "-CLEAR-TEXT-INPUT-BOX"
ENCRYPTED_TEXT_INPUT_BOX = "-ENCRYPTED-TEXT-INPUT-BOX"
KEY_INPUT = "-KEY-INPUT-BOX"
ENCRYPT = "-ENCRYPT"
DECRYPT = "-DECRYPT"
GENERATE = "-GENERATE"
ANALYZE = "-ANALYZE"
KEY_GEN = "-KEY-GEN"
DELETE = "-DELETE"


# Shift algorithm globals
SHIFT = "SHIFT"
SHIFT_ENCRYPT = SHIFT + ENCRYPT
SHIFT_DECRYPT = SHIFT + DECRYPT
SHIFT_GENERATE = SHIFT + GENERATE
SHIFT_KEY_GEN = SHIFT + KEY_GEN
SHIFT_ANALYZE = SHIFT + ANALYZE
SHIFT_CLEAR_TEXT_INPUT_BOX = SHIFT + CLEAR_TEXT_INPUT_BOX
SHIFT_DELETE_CLEAR_TEXT_INPUT_BOX = SHIFT + DELETE + CLEAR_TEXT_INPUT_BOX
SHIFT_ENCRYPTED_TEXT_INPUT_BOX = SHIFT + ENCRYPTED_TEXT_INPUT_BOX
SHIFT_DELETE_ENCRYPTED_TEXT_INPUT_BOX = SHIFT + DELETE + ENCRYPTED_TEXT_INPUT_BOX
SHIFT_KEY_INPUT = SHIFT + KEY_INPUT

# Permutation algorithm globals

PERMUTATION = "PERMUTATION"
PERMUTATION_ENCRYPT = PERMUTATION + ENCRYPT
PERMUTATION_DECRYPT = PERMUTATION + DECRYPT
PERMUTATION_GENERATE = PERMUTATION + GENERATE
PERMUTATION_KEY_GEN = PERMUTATION + KEY_GEN
PERMUTATION_ANALYZE = PERMUTATION + ANALYZE
PERMUTATION_CLEAR_TEXT_INPUT_BOX = PERMUTATION + CLEAR_TEXT_INPUT_BOX
PERMUTATION_DELETE_CLEAR_TEXT_INPUT_BOX = PERMUTATION + DELETE + CLEAR_TEXT_INPUT_BOX
PERMUTATION_ENCRYPTED_TEXT_INPUT_BOX = PERMUTATION + ENCRYPTED_TEXT_INPUT_BOX
PERMUTATION_DELETE_ENCRYPTED_TEXT_INPUT_BOX = (
    PERMUTATION + DELETE + ENCRYPTED_TEXT_INPUT_BOX
)
PERMUTATION_KEY_INPUT = PERMUTATION + KEY_INPUT


# Vigenere algorithm globals

VIGENERE = "VIGENERE"
VIGENERE_ENCRYPT = VIGENERE + ENCRYPT
VIGENERE_DECRYPT = VIGENERE + DECRYPT
VIGENERE_GENERATE = VIGENERE + GENERATE
VIGENERE_KEY_GEN = VIGENERE + KEY_GEN
VIGENERE_ANALYZE = VIGENERE + ANALYZE
VIGENERE_CLEAR_TEXT_INPUT_BOX = VIGENERE + CLEAR_TEXT_INPUT_BOX
VIGENERE_DELETE_CLEAR_TEXT_INPUT_BOX = VIGENERE + DELETE + CLEAR_TEXT_INPUT_BOX
VIGENERE_ENCRYPTED_TEXT_INPUT_BOX = VIGENERE + ENCRYPTED_TEXT_INPUT_BOX
VIGENERE_DELETE_ENCRYPTED_TEXT_INPUT_BOX = (
    VIGENERE + DELETE + ENCRYPTED_TEXT_INPUT_BOX
)
VIGENERE_KEY_INPUT = VIGENERE + KEY_INPUT


# Sustitution algorithm globals

SUBSTITUTION = "SUBSTITUTION"
SUBSTITUTION_ENCRYPT = SUBSTITUTION + ENCRYPT
SUBSTITUTION_DECRYPT = SUBSTITUTION + DECRYPT
SUBSTITUTION_GENERATE = SUBSTITUTION + GENERATE
SUBSTITUTION_KEY_GEN = SUBSTITUTION + KEY_GEN
SUBSTITUTION_ANALYZE = SUBSTITUTION + ANALYZE
SUBSTITUTION_CLEAR_TEXT_INPUT_BOX = SUBSTITUTION + CLEAR_TEXT_INPUT_BOX
SUBSTITUTION_DELETE_CLEAR_TEXT_INPUT_BOX = SUBSTITUTION + DELETE + CLEAR_TEXT_INPUT_BOX
SUBSTITUTION_ENCRYPTED_TEXT_INPUT_BOX = SUBSTITUTION + ENCRYPTED_TEXT_INPUT_BOX
SUBSTITUTION_DELETE_ENCRYPTED_TEXT_INPUT_BOX = (
    SUBSTITUTION + DELETE + ENCRYPTED_TEXT_INPUT_BOX
)
SUBSTITUTION_KEY_INPUT = SUBSTITUTION + KEY_INPUT

# Affine algorithm globals

AFFINE = "AFFINE"
AFFINE_ENCRYPT = AFFINE + ENCRYPT
AFFINE_DECRYPT = AFFINE + DECRYPT
AFFINE_GENERATE = AFFINE + GENERATE
AFFINE_KEY_GEN = AFFINE + KEY_GEN
AFFINE_ANALYZE = AFFINE + ANALYZE
AFFINE_CLEAR_TEXT_INPUT_BOX = AFFINE + CLEAR_TEXT_INPUT_BOX
AFFINE_DELETE_CLEAR_TEXT_INPUT_BOX = AFFINE + DELETE + CLEAR_TEXT_INPUT_BOX
AFFINE_ENCRYPTED_TEXT_INPUT_BOX = AFFINE + ENCRYPTED_TEXT_INPUT_BOX
AFFINE_DELETE_ENCRYPTED_TEXT_INPUT_BOX = (
    AFFINE + DELETE + ENCRYPTED_TEXT_INPUT_BOX
)
SUBSTITUTION_KEY_INPUT = AFFINE + KEY_INPUT

# Hill algorithm globals

HILL = "HILL"
HILL_ENCRYPT = HILL + ENCRYPT
HILL_DECRYPT = HILL + DECRYPT
HILL_GENERATE = HILL + GENERATE
HILL_KEY_GEN = HILL + KEY_GEN
HILL_ANALYZE = HILL + ANALYZE
HILL_CLEAR_TEXT_INPUT_BOX = HILL + CLEAR_TEXT_INPUT_BOX
HILL_DELETE_CLEAR_TEXT_INPUT_BOX = HILL + DELETE + CLEAR_TEXT_INPUT_BOX
HILL_ENCRYPTED_TEXT_INPUT_BOX = HILL + ENCRYPTED_TEXT_INPUT_BOX
HILL_DELETE_ENCRYPTED_TEXT_INPUT_BOX = (
    HILL + DELETE + ENCRYPTED_TEXT_INPUT_BOX
)
HILL_KEY_INPUT = HILL + KEY_INPUT
