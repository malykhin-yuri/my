#!/usr/bin/env python

import os.path
import shutil
import argparse


CONFIG = {
    'vim/vimrc': '.vimrc',
    'bashrc': '.bashrc',
    'screenrc': '.screenrc',
    'inputrc': '.inputrc',
    'vim/dir': 'dodi',
}

def main(dry_run):
    script_dir = os.path.dirname(__file__)
    home_dir = os.path.expanduser('~')
    for src, dst in CONFIG.items():
        src_path = os.path.join(script_dir, src)
        dst_path = os.path.join(home_dir, dst)
        print('copy {} => {}'.format(src_path, dst_path))
        if not dry_run:
            if os.path.isdir(src_path):
                shutil.copytree(src_path, dst_path)
            else:
                shutil.copy(src_path, dst_path)


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--dry-run', action='store_true')
    args = argparser.parse_args()
    main(dry_run=args.dry_run)
