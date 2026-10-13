from sly import Lexer
import sys

class CustomLexer(Lexer):
    ignore = ' \t'
    ignore_comment = r'\#.*'

    tokens = {ID, INTNUM, FLOATNUM, STR, MULTILINESTR,
              DOTADD, DOTSUB, DOTMUL, DOTDIV,
              ADDASSIGN, SUBASSIGN, MULASSIGN, DIVASSIGN,
              LE, GE, NE, EQ,
              IF, ELSE, FOR, WHILE,
              BREAK, CONTINUE, RETURN,
              EYE, ZEROS, ONES,
              PRINT}
    
    literals = {'+', '-', '*', '/',
                '=', 
                '<', '>', 
                '(', ')', '[', ']', '{', '}', 
                ':', "'", ',', ';'}

    DOTADD = r'\.\+'
    DOTSUB = r'\.-'
    DOTMUL = r'\.\*'
    DOTDIV = r'\./'
    ADDASSIGN = r'\+='
    SUBASSIGN = r'-='
    MULASSIGN = r'\*='
    DIVASSIGN = r'/='
    LE = r'<='
    GE = r'>='
    NE = r'!='
    EQ = r'=='

    ID = r'[a-zA-Z_]\w*'
    ID["if"] = IF
    ID["else"] = ELSE
    ID['for'] = FOR
    ID['while'] = WHILE
    ID['break'] = BREAK
    ID['continue'] = CONTINUE
    ID['return'] = RETURN
    ID['eye'] = EYE
    ID['zeros'] = ZEROS
    ID['ones'] = ONES
    ID['print'] = PRINT

    FLOATNUM = r'((0|[1-9][0-9]*)\.[0-9]*|\.[0-9]+)([eE][+-]?[0-9]+)?|(0|[1-9][0-9]*)[eE][+-]?[0-9]+'
    INTNUM = r'(0|[1-9][0-9]*)'

    @_(r'"""[\s\S]*?"""')
    def MULTILINESTR(self, t):
       self.lineno += t.value.count('\n')
       return t
    STR = r'"[^"\n]*"'

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)

    def error(self, t):
      print(f"Line {self.lineno}: illegal character {t.value[0]!r} at index {self.index}")
      self.index += 1


if __name__ == "__main__":
    n = len(sys.argv)
    if n <= 1:
        print(f"Usage: python main.py [filename1] [filename2]...")
        
    for i in range(1, n):
        filename = sys.argv[i]
        print(f"Filename: {filename}")
        with open(sys.argv[1]) as f:
            text = f.read()

        lexer = CustomLexer()
        for token in lexer.tokenize(text):
            print(f"({token.lineno}): {token.type}({token.value})")