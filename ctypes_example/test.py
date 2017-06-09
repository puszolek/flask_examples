from ctypes import *

libtest = cdll.LoadLibrary('Main.dll')
print(libtest.main())
