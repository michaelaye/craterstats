
import os
import gm
import craterstats

def demo(d=None):
    cmd=gm.read_textfile('config/demo_commands.txt',ignore_blank=True,ignore_hash=True)
    out='demo/'
    os.makedirs(out,exist_ok=True)
    f = '-o '+out+'{:02d}-demo '

    if d is None:
        d=range(0,len(cmd))

    for i in d:
        c=cmd[i]
        print(f'\nDemo {i}\ncraterstats.py '+c)
        a=craterstats.parse_args((f.format(i) + c).split())
        craterstats.main(a)

    print('\n\nDemo output written to: '+out)

if __name__ == '__main__':
    indices=None
    #indices=[17,18]
    demo(indices)

