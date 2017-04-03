import unittest
from brabbel.expression import Expression

class TestExpression(unittest.TestCase):

    def setUp(self):
        pass

    def test_number(self):
        expression = Expression("1")
        result = expression.evaluate()
        self.assertEqual(result, 1.0)

    def test_negativenumber(self):
        expression = Expression("-1")
        result = expression.evaluate()
        self.assertEqual(result, -1.0)

    def test_string(self):
        expression = Expression("'1'")
        result = expression.evaluate()
        self.assertEqual(result, "1")

    def test_stringwithspace(self):
        expression = Expression("'foo and bar'")
        result = expression.evaluate()
        self.assertEqual(result, "foo and bar")

    def test_stringwithsinglequote(self):
        expression = Expression("'foo \\'and bar'")
        result = expression.evaluate()
        self.assertEqual(result, "foo \\'and bar")

    def test_stringwithbracket(self):
        expression = Expression("'foo (and bar'")
        result = expression.evaluate()
        self.assertEqual(result, "foo (and bar")

    def test_variable(self):
        expression = Expression("$string")
        result = expression.evaluate({"string": "string"})
        self.assertEqual(result, "string")

    def test_missingvariable(self):
        expression = Expression("$missingstring")
        result = expression.evaluate({"string": "string"})
        self.assertEqual(result, None)

    def test_true(self):
        expression = Expression("True")
        result = expression.evaluate()
        self.assertEqual(result, True)

    def test_false(self):
        expression = Expression("False")
        result = expression.evaluate()
        self.assertEqual(result, False)

    def test_listing(self):
        expression = Expression("[1,2,3]")
        result = expression.evaluate()
        self.assertEqual(result, [1, 2, 3])

    def test_nottrue(self):
        expression = Expression("not True")
        result = expression.evaluate()
        self.assertEqual(result, False)

    def test_notfalse(self):
        expression = Expression("not False")
        result = expression.evaluate()
        self.assertEqual(result, True)

    def test_plus(self):
        expression = Expression("1 + 1")
        result = expression.evaluate()
        self.assertEqual(result, 2.0)

    def test_plusplus(self):
        expression = Expression("1 + 1 + 1")
        result = expression.evaluate()
        self.assertEqual(result, 3.0)

    def test_sub(self):
        expression = Expression("7 - 4")
        result = expression.evaluate()
        self.assertEqual(result, 3.0)

    def test_mul(self):
        expression = Expression("7 * 7")
        result = expression.evaluate()
        self.assertEqual(result, 49.0)

    def test_div(self):
        expression = Expression("49 / 7")
        result = expression.evaluate()
        self.assertEqual(result, 7.0)

    def test_addmul(self):
        expression = Expression("4 + 3 * 7")
        result = expression.evaluate()
        self.assertEqual(result, 25.0)

    def test_addmulpar(self):
        expression = Expression("(4 + 3) * 7")
        result = expression.evaluate()
        self.assertEqual(result, 49.0)

    def test_plusnediv(self):
        expression = Expression("2 + 2 == 8 / 2")
        result = expression.evaluate()
        self.assertEqual(result, True)

    def test_eqnegnumber(self):
        expression = Expression("$a == -1")
        result = expression.evaluate({"a": 1})
        self.assertEqual(result, False)

    def test_eqandgt(self):
        expression = Expression("2 == 2 and 8 > 2")
        result = expression.evaluate()
        self.assertEqual(result, True)

    def test_eqorgt(self):
        expression = Expression("2 != 2 or 8 > 2")
        result = expression.evaluate()
        self.assertEqual(result, True)

    def test_notand(self):
        expression = Expression("not False and True")
        result = expression.evaluate()
        self.assertEqual(result, True)

    def test_in(self):
        expression = Expression("'foo' in ['foo','bar']")
        result = expression.evaluate()
        self.assertEqual(result, True)

    def test_notin(self):
        expression = Expression("not ('foo' in ['foo','bar'])")
        result = expression.evaluate()
        self.assertEqual(result, False)

    def test_datetoday(self):
        from datetime import date
        expression = Expression("date('today')")
        result = expression.evaluate()
        self.assertEqual(result, date.today())

    def test_datexlttoday(self):
        from datetime import date
        expression = Expression("date('20000101') < date('today')")
        result = expression.evaluate()
        self.assertEqual(result, True)

    def test_datexgttoday(self):
        from datetime import date
        expression = Expression("date('20000101') > date('today')")
        result = expression.evaluate()
        self.assertEqual(result, False)

    def test_bool1(self):
        expression = Expression("bool(1)")
        result = expression.evaluate()
        self.assertEqual(result, True)

    def test_bool0(self):
        expression = Expression("bool(0)")
        result = expression.evaluate()
        self.assertEqual(result, True)

    def test_boolstring(self):
        expression = Expression("bool('foo')")
        result = expression.evaluate()
        self.assertEqual(result, True)

    def test_boolstringempty(self):
        expression = Expression("bool('')")
        result = expression.evaluate()
        self.assertEqual(result, False)

    def test_boollist(self):
        expression = Expression("bool([1,2,3])")
        result = expression.evaluate()
        self.assertEqual(result, True)

    def test_boollistempty(self):
        expression = Expression("bool([])")
        result = expression.evaluate()
        self.assertEqual(result, False)

    def test_boolempty(self):
        expression = Expression("bool()")
        result = expression.evaluate()
        self.assertEqual(result, False)

    def test_boolorTrue(self):
        expression = Expression("bool(0) or True")
        result = expression.evaluate()
        self.assertEqual(result, True)

    def test_boolandFalse(self):
        expression = Expression("bool(0) and False")
        result = expression.evaluate()
        self.assertEqual(result, False)

    def test_notboolemptystring(self):
        expression = Expression("not bool('')")
        result = expression.evaluate()
        self.assertEqual(result, True)

    def test_notemptystring(self):
        expression = Expression("not ''")
        result = expression.evaluate()
        self.assertEqual(result, True)

    def test_notNone(self):
        expression = Expression("not None")
        result = expression.evaluate()
        self.assertEqual(result, True)

    def test_notTrue(self):
        expression = Expression("not True")
        result = expression.evaluate()
        self.assertEqual(result, False)

    def test_notFalse(self):
        expression = Expression("not False")
        result = expression.evaluate()
        self.assertEqual(result, True)

    def test_notboolor(self):
        expression = Expression("(not bool(0)) or False")
        result = expression.evaluate()
        self.assertEqual(result, False)

    def test_boolvar(self):
        expression = Expression("bool($float)")
        result = expression.evaluate({"float": 1})
        self.assertEqual(result, True)

    def test_boolempty(self):
        expression = Expression("bool($string)")
        result = expression.evaluate({"string": ""})
        self.assertEqual(result, False)

    def test_addstr(self):
        expression = Expression("$a + 'abc'")
        result = expression.evaluate({"a": u"xyz"})
        self.assertEqual(result, 'xyzabc')

    def test_len4ticks(self):
        expression = Expression("len($a)")
        result = expression.evaluate({"a": "''''"})
        self.assertEqual(result, 4)

    def test_smaller(self):
        import datetime
        expression = Expression("$a > timedelta($b)")
        result = expression.evaluate({"a": datetime.timedelta(seconds=100),
                                      "b": "00:00:120"})
        self.assertEqual(result, False)

    def test_equal(self):
        expression = Expression("timedelta($a) == timedelta($b)")
        result = expression.evaluate({"a": "01:30:00", "b": "00:90:00"})
        self.assertEqual(result, True)

    def test_sum_smaller(self):
        expression = Expression("(timedelta($a) +  timedelta($b)) < timedelta($c)")
        result = expression.evaluate({"a": "04:00:00",
                                      "b": "05:00:00",
                                      "c": "08:00:00"})
        self.assertEqual(result, False)

    #def test_lenexpr(self):
    #    expression = Expression("len(($a + 'abc'))")
    #    result = expression.evaluate({"a": "xyz"})
    #    self.assertEqual(result, 6)


class TestReallife(unittest.TestCase):
    def test_1(self):
        expression = Expression("( 'antragsteller' in       ['institutionen_einsicht', 'user', 'antragsteller']   ) == False")
        result = expression.evaluate()
        self.assertEqual(result, False)

    def test_2(self):
        expression = Expression("( 'abfrages' eq 'antrags' ) and ( '1' eq '2') or ( 'admin' in ['institutionen_einsicht','user','antragsteller'] ) or ( 'formularmanager' in ['institutionen_einsicht','user','antragsteller'] )")
        result = expression.evaluate()
        self.assertEqual(result, False)

    # Two complex rules from the prospi project.
    def test_3(self):
        import datetime
        expression = Expression("( ( ( $ap_ausb eq '1' ) and ( $pp_phase in ['1','2'] ) ) or ( ( $ap_ausb eq '3' ) and ( $pp_phase in ['3','4'] ) ) or ( ( $ap_ausb in ['2','4'] ) or ( not bool($ap_ausb) ) ) )")
        values = {'ap_austritt': u'1', 'pp_phase_s': u'', 'ap_q1': u'Rechtsanwalt und Notarfachangestellte', 'ap_geschlecht': u'0', 'ap_austritt_ja': u'ja', 'programm_info': '', 'bericht_state_id': 2, 'pp_austritt_ca': datetime.date(2014, 3, 14), 'ap_ausb': u'1', 'pp_phase': u'1', 'pp_ga': [u'2', u''], 'ap_austritt_date': datetime.date(2014, 3, 14), 'proj_kommentar': u'', 'proj_fkz': u'09.00101.13', 'ap_bj1': u'', 'ap_bj2': u'', 'ap_bj3': u'', 'pp_beginn': u'seit', 'updated': datetime.datetime(2014, 10, 23, 12, 33, 25), '_roles': '', 'ap_quer': u'1', 'ap_quali': u'1', 'pp_gesamtst': u'275', 'form_info': '', 'pp_kinder': [u'1', u''], 'created': datetime.datetime(2014, 9, 23, 14, 5, 30), 'ausbildungsformat': None, 'pp_eintritt_ps': datetime.date(2014, 1, 6), 'logo_einbindung': None, 'pp_eintritt_vb': None, 'ap_code': u'A.CB257', 'ap_q2': u'', 'ap_austritt_s': u'', 'ap_mhg': u'0', 'ap_q3': u''}
        result = expression.evaluate(values)
        self.assertEqual(result, True)

    def test_4(self):
        import datetime
        expression = Expression("( ( ( $ap_ausb eq '1' ) and ( $pp_phase in ['1','2'] ) ) or ( ( $ap_ausb eq '3' ) and ( $pp_phase in ['3','4'] ) ) or ( ( $ap_ausb in ['2','4'] ) or ( not bool($ap_ausb) ) ) )")
        values = {'ap_austritt': u'1', 'pp_phase_s': u'', 'ap_q1': u'Rechtsanwalt und Notarfachangestellte', 'ap_geschlecht': u'0', 'ap_austritt_ja': u'ja', 'programm_info': '', 'bericht_state_id': 2, 'pp_austritt_ca': datetime.date(2014, 3, 14), 'ap_ausb': u'1', 'pp_phase': u'', 'pp_ga': [u'2', u''], 'ap_austritt_date': datetime.date(2014, 3, 14), 'proj_kommentar': u'', 'proj_fkz': u'09.00101.13', 'ap_bj1': u'', 'ap_bj2': u'', 'ap_bj3': u'', 'pp_beginn': u'seit', 'updated': datetime.datetime(2014, 10, 23, 12, 41, 39), '_roles': '', 'ap_quer': u'1', 'ap_quali': u'1', 'pp_gesamtst': u'275', 'form_info': '', 'pp_kinder': [u'1', u''], 'created': datetime.datetime(2014, 9, 23, 14, 5, 30), 'projekt': None, 'ausbildungsformat': None, 'pp_eintritt_ps': datetime.date(2014, 1, 6), 'logo_einbindung': None, 'pp_eintritt_vb': None, 'ap_code': u'A.CB257', 'ap_q2': u'', 'ap_austritt_s': u'', 'ap_mhg': u'0', 'ap_q3': u''}
        result = expression.evaluate(values)
        self.assertEqual(result, False)

    def test_5(self):
        import datetime
        expression = Expression("len($xxx) le 9")
        values = {'xxx': u'abcdefghi'}
        result = expression.evaluate(values)
        self.assertEqual(result, True)

    def test_6(self):
        expression = Expression("( 'LOP-PM' in ['admins'] ) or ( 'False' == 'True' )")
        result = expression.evaluate({})
        self.assertEqual(result, False)

    def test_7(self):
        expression = Expression("bool($x) and ($x == 0)")
        result = expression.evaluate({'x': None})
        self.assertEqual(result, False)

    def test_8(self):
        expression = Expression("bool($x) and ($x == 1)")
        result = expression.evaluate({'x': 0})
        self.assertEqual(result, False)
