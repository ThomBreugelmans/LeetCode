import importlib
from regex_matcher import regex_matcher

rgx_matcher = regex_matcher()
print('aaa is matched by a*? {}'.format(rgx_matcher.isMatch(s='aaa', p='a*')))                # should be True
print('aa is matched by a*? {}'.format(rgx_matcher.isMatch(s='aa', p='a*')))                # should be True
print('aaa is matched by a? {}'.format(rgx_matcher.isMatch(s='aaa', p='a')))                  # should be False
print('aaa is matched by a*a? {}'.format(rgx_matcher.isMatch(s='aaa', p='a*a')))              # should be True   
print('aaba is matched by ab*a*c*a? {}'.format(rgx_matcher.isMatch(s='aaba', p='ab*a*c*a')))  # should be False
print('aaaaaaaaaaaaab is matched by a*a*a*a*a*a*a*a*a*a*a*a*b? {}'
        .format(rgx_matcher.isMatch(s='aaaaaaaaaaaaab', p='a*a*a*a*a*a*a*a*a*a*a*a*b')))      # should be True
""
