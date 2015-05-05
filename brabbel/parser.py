import logging
from builtins import object
from pyparsing import (
    ParserElement,
    Literal, Word,
    Combine, Group, Optional,
    nums, alphanums, alphas,
    delimitedList,
    operatorPrecedence, opAssoc)


"""
number    :: '0'..'9'+
string    :: '0'..'9''a'..'z''_'+
variable  :: '$' string

"""
log = logging.getLogger(__name__)
ParserElement.enablePackrat()

########################################################################
#                               Helpers                                #
########################################################################


def _str(origString, loc, tokens):
    return unicode(tokens[0])


def _number(origString, loc, tokens):
    try:
        return int(tokens[0])
    except:
        return float(tokens[0])


def _make_list(element=""):
    """Returns a list element

    :element: Parsed element as a string representation of a list
    :returns: List element

    """
    listing = []
    for e in element:
        listing.append(e)
    return [listing]


########################################################################
#                                ATOMS                                 #
########################################################################
lpar = Literal("(")
lbr = Literal("[")
rpar = Literal(")")
rbr = Literal("]")
lquote = Literal("'")
rquote = Literal("'")
number = Combine(Optional("-") + Word(nums + '.')).setParseAction(_number)
# TODO: Remove "-" from list of allowed chars. Is only here for
# compatibility. (None) <2014-10-28 14:04>
variable = Combine("$" + Word(alphanums + "_" + "-" + "."))
string = Combine(lquote.suppress() + Optional(Word(alphanums + "_" + " " + "-" + ":")) + rquote.suppress()).setParseAction(_str)
identifier = Word(alphas + "_")
none = Literal("None").setParseAction(lambda t: False)
true = Literal("True").setParseAction(lambda t: True)
false = Literal("False").setParseAction(lambda t: False)
listing = lbr.suppress() + delimitedList(Optional(string | number)).setParseAction(_make_list) + rbr.suppress()
function = identifier.setResultsName("name") + lpar.suppress() + Group(Optional(delimitedList(number | string | variable | listing | true | false | none))) + rpar.suppress()
atom = listing | number | string | variable | true | false | none | function

########################################################################
#                              Operators                               #
########################################################################

opmapping = {
    " ge ": " >= ",
    " gt ": " > ",
    " lt ": " < ",
    " le ": " <= ",
    " eq ": " == ",
    " ne ": " != "
}

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
        # Replace operators like gt, lt...
        for op in opmapping:
            expr = expr.replace(op, opmapping[op])
        try:
            return bnf.parseString(expr)
        except Exception:
            log.exception("Error on parsing %s" % expr)
