# vim: set fileencoding=utf-8 :

# #STKPWHRAO*EUFRPBLGTSDZ
KEYS = (
    '#',
    'S-', 'T-', 'K-', 'P-', 'W-', 'H-', 'R-',
    'A-', 'O-',
    '*',
    '-E', '-U',
    '-F', '-R', '-P', '-B', '-L', '-G', '-T', '-S', '-D', '-Z',
)

IMPLICIT_HYPHEN_KEYS = ('A-', 'O-', '5-', '0-', '-E', '-U', '*')

SUFFIX_KEYS = ('-Z', '-D', '-S', '-G')

NUMBER_KEY = '#'

NUMBERS = {
    'S-': '1-',
    'T-': '2-',
    'P-': '3-',
    'H-': '4-',
    'A-': '5-',
    'O-': '0-',
    '-F': '-6',
    '-P': '-7',
    '-L': '-8',
    '-T': '-9',
}

UNDO_STROKE_STENO = '*'

ORTHOGRAPHY_RULES = [
    ## Plurals. Based on https://espanol.lingolia.com/es/gramatica/sustantivos/plural
    # Plural for sustantive that ends with "í". Ex.: jabalí + s -> jabalíes
    (r'^(.*)í \^ s$', r'\1íes'),
    
    # Plural for sustantive that ends with "ú". Ex.: bambú + s -> bambúes
    (r'^(.*)ú \^ s$', r'\1úes'),

    # Plural for sustantive that ends with consonants "d", "j", "l", "n", "r". Ex.: reloj + s -> relojes
    # TODO: This one is sketchy. If the word is acute and ends with "n" it must have an accent mark:
    # pantalón + s -> pantalones (in this case the accent mark must be removed).
    (r'^(.*(?:d|j|l|n|r)) \^ s$', r'\1es'),
    
    # Plural for sustantive that ends with consonant "z". Ex.: cruz + s -> cruces
    (r'^(.*)z \^ s$', r'\1ces'),
    
    # Plural for acute sustantive that ends with "s". Ex.: mandamás + s -> mandamases
    (r'^(.*)ás \^ s$', r'\1ases'),
    # Ex.: entremés + s -> entremeses
    (r'^(.*)és \^ s$', r'\1eses'),
    # Ex.: chisgarabís + s -> chisgarabises. TODO: This one is sketchy. Consider "país" that has hiatus,
    # and the correct plural is "países".
    (r'^(.*)ís \^ s$', r'\1ises'),
    # Ex.: intradós + s -> intradoses
    (r'^(.*)ós \^ s$', r'\1oses'),
    # Ex.: autobús + s -> autobuses
    (r'^(.*)ús \^ s$', r'\1uses'),
    # TODO: The same rule goes for the plural in acute sustantive that ends with "x", but in this
    # case the last syllable must not have accent mark. At the moment I don't see any easy way to implement
    # with ORTHOGRAPHY_RULES. Also, probably there are very few words with this characteristics (I
    # found "gambux" for example).

    ## Participles. Based on https://espanol.lingolia.com/es/gramatica/verbos/participio
    # Irregular participles when radix has a vocal as last letter.
    # Ex. traer + ido|ida -> traído|traída, leer + ido|ida -> leído|leída, oír + ido|ida -> oído|oída
    (r'^(.*)(a|e|i|o|u)(?:a|e|i|o|u)r \^ ido$', r'\1\2ído'),
    (r'^(.*)(a|e|i|o|u)(?:a|e|i|o|u)r \^ ida$', r'\1\2ída'),
    (r'^(.*)(a|e|i|o|u)(?:á|é|í|ó|ú)r \^ ido$', r'\1\2ído'),
    (r'^(.*)(a|e|i|o|u)(?:á|é|í|ó|ú)r \^ ida$', r'\1\2ída'),
    # TODO: Especial cases are not covered at the moment. Ex. abierto, provisto, vuelto, etc.
    
    # Participle ending with "ar". Ex.: aclamar + ado|ada -> aclamado|aclamada
    (r'^(.*)ar \^ ado$', r'\1ado'),
    (r'^(.*)ar \^ ada$', r'\1ada'),

    # Participle ending with "er" or "ir". Ex.: temer + ido|ida -> temido|temida,
    # vivir + ido|ida -> vivido|vivida
    (r'^(.*)(?:e|i)r \^ ido$', r'\1ido'),
    (r'^(.*)(?:e|i)r \^ ida$', r'\1ida'),

    ## Gerunds. Based on https://espanol.lingolia.com/es/gramatica/verbos/gerundio
    # Irregular gerunds, if "ñir" and "e" -> "i" changing:
    # desteñir -> destiñendo
    (r'^(.*)(?:e)([bcdfghjklmnñpqrstvwxyz])?(s)?(ñir) \^ nd$', r'\1i\2\3ñendo'),

    # Irregular gerunds, if "ñir" or "llir" happens, must use "endo" instead of "iendo":
    (r'^(.*)(ñ|ll)ir \^ nd$', r'\1\2endo'),

    # Irregular gerunds, verbs ending with "ir" and "e" -> "i" changing:
    # reír -> riendo
    (r'^(.*)(?:e)(ir|ír) \^ nd$', r'\1iendo'),    
    # preferir -> prefiriendo
    # sentir -> sintiendo
    (r'^(.*)(?:e)([bcdfghjklmnñpqrstvwxyz])?(s)?([bcdfghjklmnpqrstvwxyz])?(l|r)?(ir|ír) \^ nd$', r'\1i\2\3\4\5iendo'),
    # seguir -> siguiendo
    (r'^(.*)(?:e)([bcdfghjklmnñpqrstvwxyz])?(s)?(guir) \^ nd$', r'\1iguiendo'),

    # Irregular gerunds, verbs ending with "er" or "ir" and "o" -> "u" changing:
    (r'^(.*)(?:o)([bcdfghjklmnñpqrstvwxyz])?(s)?([bcdfghjklmnñpqrstvwxyz])?(l|r)?(er|ér|ir|ír) \^ nd$', r'\1u\2\3\4\5iendo'),
    
    # Irregular gerunds, verbs wich radix ends with vowel must use "yendo" instead of "iendo":
    (r'^(.*)([aeiouáéíóú])(er|ér|ir|ír) \^ nd$', r'\1\2yendo'),
    (r'^(ir) \^ nd$', r'yendo'),

    # Regular gerunds, verbs ending with "ar" must use "ando". Ex. "terminar" -> "terminando":
    (r'^(.*)ar \^ nd$', r'\1ando'),

    # Regular gerunds, verbs ending with "er" or "ir" must use "iendo". Ex. "temer" -> "temiendo",
    # "vivir" -> "viviendo":
    (r'^(.*)(er|ir) \^ nd$', r'\1iendo'),

]

ORTHOGRAPHY_RULES_ALIASES = {}

ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
    'Gemini PR': {
        '#'         : ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#A', '#B', '#C'),
        'S-'        : ('S1-', 'S2-'),
        'T-'        : 'T-',
        'K-'        : 'K-',
        'P-'        : 'P-',
        'W-'        : 'W-',
        'H-'        : 'H-',
        'R-'        : 'R-',
        'A-'        : 'A-',
        'O-'        : 'O-',
        '*'         : ('*1', '*2', '*3', '*4'),
        '-E'        : '-E',
        '-U'        : '-U',
        '-F'        : '-F',
        '-R'        : '-R',
        '-P'        : '-P',
        '-B'        : '-B',
        '-L'        : '-L',
        '-G'        : '-G',
        '-T'        : '-T',
        '-S'        : '-S',
        '-D'        : '-D',
        '-Z'        : '-Z',
        'no-op'     : ('Fn', 'pwr', 'res1', 'res2'),
    },
    'Keyboard': {
        '#'         : ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='),
        'S-'        : ('a', 'q'),
        'T-'        : 'w',
        'K-'        : 's',
        'P-'        : 'e',
        'W-'        : 'd',
        'H-'        : 'r',
        'R-'        : 'f',
        'A-'        : 'c',
        'O-'        : 'v',
        '*'         : ('t', 'g', 'y', 'h'),
        '-E'        : 'n',
        '-U'        : 'm',
        '-F'        : 'u',
        '-R'        : 'j',
        '-P'        : 'i',
        '-B'        : 'k',
        '-L'        : 'o',
        '-G'        : 'l',
        '-T'        : 'p',
        '-S'        : ';',
        '-D'        : '[',
        '-Z'        : '\'',
        'arpeggiate': 'space',
        # Suppress adjacent keys to prevent miss-strokes.
        'no-op'     : ('z', 'x', 'b', ',', '.', '/', ']', '\\'),
    },
    'Passport': {
        '#'    : '#',
        'S-'   : ('S', 'C'),
        'T-'   : 'T',
        'K-'   : 'K',
        'P-'   : 'P',
        'W-'   : 'W',
        'H-'   : 'H',
        'R-'   : 'R',
        'A-'   : 'A',
        'O-'   : 'O',
        '*'    : ('~', '*'),
        '-E'   : 'E',
        '-U'   : 'U',
        '-F'   : 'F',
        '-R'   : 'Q',
        '-P'   : 'N',
        '-B'   : 'B',
        '-L'   : 'L',
        '-G'   : 'G',
        '-T'   : 'Y',
        '-S'   : 'X',
        '-D'   : 'D',
        '-Z'   : 'Z',
        'no-op': ('!', '^', '+'),
    },
    'Stentura': {
        '#'    : '#',
        'S-'   : 'S-',
        'T-'   : 'T-',
        'K-'   : 'K-',
        'P-'   : 'P-',
        'W-'   : 'W-',
        'H-'   : 'H-',
        'R-'   : 'R-',
        'A-'   : 'A-',
        'O-'   : 'O-',
        '*'    : '*',
        '-E'   : '-E',
        '-U'   : '-U',
        '-F'   : '-F',
        '-R'   : '-R',
        '-P'   : '-P',
        '-B'   : '-B',
        '-L'   : '-L',
        '-G'   : '-G',
        '-T'   : '-T',
        '-S'   : '-S',
        '-D'   : '-D',
        '-Z'   : '-Z',
        'no-op': '^',
    },
    'TX Bolt': {
        '#'    : '#',
        'S-'   : 'S-',
        'T-'   : 'T-',
        'K-'   : 'K-',
        'P-'   : 'P-',
        'W-'   : 'W-',
        'H-'   : 'H-',
        'R-'   : 'R-',
        'A-'   : 'A-',
        'O-'   : 'O-',
        '*'    : '*',
        '-E'   : '-E',
        '-U'   : '-U',
        '-F'   : '-F',
        '-R'   : '-R',
        '-P'   : '-P',
        '-B'   : '-B',
        '-L'   : '-L',
        '-G'   : '-G',
        '-T'   : '-T',
        '-S'   : '-S',
        '-D'   : '-D',
        '-Z'   : '-Z',
    },
    'Treal': {
        '#'    : ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#A', '#B'),
        'S-'   : ('S1-', 'S2-'),
        'T-'   : 'T-',
        'K-'   : 'K-',
        'P-'   : 'P-',
        'W-'   : 'W-',
        'H-'   : 'H-',
        'R-'   : 'R-',
        'A-'   : 'A-',
        'O-'   : 'O-',
        '*'    : ('*1', '*2'),
        '-E'   : '-E',
        '-U'   : '-U',
        '-F'   : '-F',
        '-R'   : '-R',
        '-P'   : '-P',
        '-B'   : '-B',
        '-L'   : '-L',
        '-G'   : '-G',
        '-T'   : '-T',
        '-S'   : '-S',
        '-D'   : '-D',
        '-Z'   : '-Z',
        'no-op': ('X1-', 'X2-', 'X3'),
    },
}

DICTIONARIES_ROOT = 'asset:plover_spanish_system_eo_variant:dictionaries'
DEFAULT_DICTIONARIES = ('spanish_eo_00_user.json', 'spanish_eo_10_articles.json', 'spanish_eo_20_main.json')
