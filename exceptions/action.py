import sys


system_platform = 'linux'

try:
    assert (system_platform in sys.platform), 'this is mac'
    print('This is', system_platform)
except:
    print('This is not', system_platform)