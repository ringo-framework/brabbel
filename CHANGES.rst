0.3.1
=====
- Make comparison of operators more typesafe. Evaluation of terms is only
  valid of operators of the same type. Otherwise the term will evaluate to
  False.
- Implement short circuiting for "and" and "or" operators.

0.3.0
=====
Make Brabbel Python3 compatible. Added python-future package as dependency

- Allow dots "." in variable names.

0.2.7
=====
- Fixed handling of integer and string values in lists.

0.2.6
=====
- Added folders for documentation (currently empty)
- Allow "-" in Strings
- Added more tests.

0.2.5
=====
- Log warning if a variable can not be resolved in the values dict.
- Allow signed numbers. Currently only negativ sign is allowed.
- String to not have a "'" anymore.
- Added more tests.

0.2.4
=====
- Compatiblity: Allow "-" in variable names.
- Fixed strip of "'" in "len" function.

0.2.3
=====
- Allow empty strings
- Fix bool function
- Allow lists as param for functions

0.2.2
=====
- Added len function

0.2.1
=====
- Be more tolerant on whitespaces in delimeted lists,
- Fix call of functions

0.2
===
- Add operator mapping for operators like ge, gt, le, lt, eq, ne
- Be more tolerant on getting non existing values from the values dictionary.
- Removed Rule class.

0.1
===
- Initial Release
