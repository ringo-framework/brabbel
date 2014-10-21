from pyparsing import (
    ParserElement,
    Literal, Word,
    Combine, Group, oneOf, ZeroOrMore, Optional,
    nums, alphanums, alphas,
    delimitedList,
    operatorPrecedence, opAssoc)


"""
number    :: '0'..'9'+
string    :: '0'..'9''a'..'z''_'+
variable  :: '$' string

"""
ParserElement.enablePackrat()

########################################################################
#                               Helpers                                #
########################################################################


def _make_list(element=""):
    """Returns a list element

    :element: Parsed element as a string representation of a list
    :returns: List element

    """
    listing = []
    element = element[0].replace("[", "").replace("]", "")
    for e in element.split(","):
        try:
            e = float(e)
        except:
            pass
        listing.append(e)
    return [listing]


########################################################################
#                                ATOMS                                 #
########################################################################
lpar = Literal("(")
rpar = Literal(")")
number = Word(nums + '.').setParseAction(lambda t: float(t[0]))
string = Combine("'" + Word(alphanums + "_") + "'")
variable = Combine("$" + Word(alphanums + "_"))
identifier = Word(alphas + "_")
true = Literal("True").setParseAction(lambda t: True)
false = Literal("False").setParseAction(lambda t: False)
listing = Combine("[" + ZeroOrMore((number | string )+ZeroOrMore("," + (number | string ))) + "]").setParseAction(_make_list)
function = identifier.setResultsName("name") + lpar.suppress() + Group(Optional(delimitedList(number | string | variable))) + rpar.suppress()
atom = listing | number | string | variable | true | false | function

########################################################################
#                              Operators                               #
########################################################################
o_not = Literal("not")
o_plus = Literal("+")
o_minus = Literal("-")
o_mul = Literal("*")
o_div = Literal("/")
o_gt = Literal(">")
o_ge = Literal(">=")
o_lt = Literal("<")
o_le = Literal("<=")
o_ne = Literal("!=")
o_eq = Literal("==")
o_and = Literal("and")
o_or = Literal("or")
o_in = Literal("in")

bnf = operatorPrecedence(atom,
                         [(o_not, 1, opAssoc.RIGHT),
                          (o_mul, 2, opAssoc.LEFT),
                          (o_div, 2, opAssoc.LEFT),
                          (o_plus, 2, opAssoc.LEFT),
                          (o_minus, 2, opAssoc.LEFT),
                          (o_gt, 2, opAssoc.LEFT),
                          (o_ge, 2, opAssoc.LEFT),
                          (o_lt, 2, opAssoc.LEFT),
                          (o_le, 2, opAssoc.LEFT),
                          (o_ne, 2, opAssoc.LEFT),
                          (o_eq, 2, opAssoc.LEFT),
                          (o_and, 2, opAssoc.LEFT),
                          (o_or, 2, opAssoc.LEFT),
                          (o_in, 2, opAssoc.LEFT),
                         ])


class Parser(object):

    """Parser class for python expression."""

    def __init__(self):
        """@todo: to be defined1. """
        pass

    def parse(self, expr):
        """Returns the BNF-Tree of the given expression

        :expr: String of the expression
        :returns: Returns the parsed BNF form the the expression

        """
        return bnf.parseString(expr)
