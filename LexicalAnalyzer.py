import re


class LexicalAnalyzer:
    # Token row
    lin_num = 1

    def tokenize(self, code):
        rules = [
            ('FURY', r'fury'),                      # main
            ('HULK', r'hulk'),                      # variavel
            ('VISAO', r'visao'),                    # print
            ('GROOT', r'groot'),                    # if
            ('ROCKET', r'rocket'),                  # endif
            ('VENOM', r'venom'),                    # +
            ('CARNIFICINA', r'carnificina'),        # -
            ('MADROX', r'madrox'),                  # *
            ('GOLIAS', r'golias'),                  # >
            ('MISTICA', r'mistica'),                # ==
            ('THANOS', r'thanos'),                  # /
            ('DRESTRANHO', r'drestranho'),          # while
            ('DORMAMO', r'dormamo'),                # endwhile
            ('FORMIGA', r'formiga'),                # <
            ('AMERICA', r'america'),                # &&
            ('STARK', r'stark'),                    # ||
            ('SHIELD', r'shield'),                  # end main
            ('AVENGERS', r'avengers'),              # open main
            ('LINCE', r'lince'),                    # read file
            ('CHAMADA_DE_FUNCAO', r'\-\>'),         # atribuição
            ('ATTR', r'\='),                        # =
            ('ATRIBUIR', r'\.'),                     # ANOTHER CHARACTER
            ('ID', r'[a-zA-Z]\w*'),                 # IDENTIFIERS
            ('FLOAT_CONST', r'\d(\d)*\.\d(\d)*'),   # FLOAT
            ('INTEGER_CONST', r'\d(\d)*'),          # INT
            ('NEWLINE', r'\n'),                     # NEW LINE
            ('SKIP', r'[ \t]+'),                    # SPACE and TABS
            ('COMENTARIOS', r'\#')                  # comentarios
        ]

        tokens_join = '|'.join('(?P<%s>%s)' % x for x in rules)
        lin_start = 0

        # Lists of output for the program
        token = []
        lexeme = []
        row = []
        column = []

        # It analyzes the code to find the lexemes and their respective Tokens
        for m in re.finditer(tokens_join, code):
            token_type = m.lastgroup
            token_lexeme = m.group(token_type)
            if token_type == 'COMENTARIOS':
                lin_start = m.end()
                self.lin_num += 1
            if token_type == 'NEWLINE':
                lin_start = m.end()
                self.lin_num += 1
            elif token_type == 'SKIP':
                continue
            elif token_type == 'MISMATCH':
                raise RuntimeError('%r unexpected on line %d' % (token_lexeme, self.lin_num))
            else:
                    col = m.start() - lin_start
                    column.append(col)
                    token.append(token_type)
                    lexeme.append(token_lexeme)
                    row.append(self.lin_num)
                    # To print information about a Token
                    print('Token = {0}, Lexeme = \'{1}\', Row = {2}, Column = {3}'.format(token_type, token_lexeme, self.lin_num, col))

        return token, lexeme, row, column
