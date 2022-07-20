#!/usr/bin/env python

import os.path
import shutil
import argparse

import logging


logging.basicConfig(level=logging.INFO)


CONFIG = {
    'vim/vimrc': '.vimrc',
    'bashrc': '.bashrc',
    'screenrc': '.screenrc',
    'inputrc': '.inputrc',
    'vim/dir': '.vim',
}

def main(dry_run):
    script_dir = os.path.dirname(__file__)
    home_dir = os.path.expanduser('~')
    for src, dst in CONFIG.items():
        src_path = os.path.join(script_dir, src)
        dst_path = os.path.join(home_dir, dst)
        logging.info('copy %s => %s', src_path, dst_path)
        if not dry_run:
            if os.path.isdir(src_path):
                if os.path.exists(dst_path):
                    logging.info('delete dir %s', dst_path)
                    shutil.rmtree(dst_path)
                shutil.copytree(src_path, dst_path)
            else:
                shutil.copy(src_path, dst_path)


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--dry-run', action='store_true')
    args = argparser.parse_args()
    main(dry_run=args.dry_run)
