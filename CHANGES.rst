0.5.1
=====
- Fixed unicode error.

0.5.0
=====
Inofficial release! Has only been internally tagged as 0.5.0. Not actually
released on upstream.

- Use Lock on Parser when parsing an expression to prevent hickups of the
  parser resulting an exceptions.

0.4.4
=====
- Added float function to cast value to float. Used to make comparisions
  between float and int possible.

0.4.3
=====
- Improved parsing single quoted strings. Now almost all chars are allowed
  except a single quote "'" will will raise an execption because parsing
  fails. Because the fix is a improvement at all and the remaining bug is is
  currently considered as a rare corner case. This will be released anyway.

0.4.2
=====
- Added workaround for failing parsing of expressions when pyparsing is under
  high load.

0.4.1
=====
- Changed license from MIT to GPL v2+ and added LICENSE.txt
- Added "bdist_rpm" section setup.cfg.
- Added "egg_info" section setup.cfg.

0.4.0
=====
- Make comparison of operators more type safe. Evaluation of terms is only
  valid of operators of the same type. Otherwise the term will evaluate to
  False.
- Implement short circuiting for "and" and "or" operators.
- Support "True","False","None" in bool function.
- Refactored code. Created own module for operators and functions.
- Added documentation.

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
