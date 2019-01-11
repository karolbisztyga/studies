'''
    @file       __main__.py
    @author     Karol Bisztyga (karolbisztyga@gmail.com)
    @date       2018/11/19
    @version    1.0

    @brief
        run this file to use the compiler
'''
import sys

try:
    from compiler.src.App import App
except ImportError:
    print('if you are using command line try python3 with option -m')
    exit(0)

result = App().run(sys.argv)
if not result[0] or not result[1]:
    exit(1)
exit(0)
