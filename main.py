import argparse
import configparser
import os
import subprocess

def archive():
    """Compresses a file/directory in a lossless/lossfull manner.
        
    """ 


class BackupRoot(argparse.Action):

    def __init__(self, option_strings, dest, nargs=None, const=None, default=None, type=None, choices=None, required=False, help=None, metavar=None):
        super().__init__(option_strings, dest, nargs, const, default, type, choices, required, help, metavar)

    def __call__(self, parser, namespace, values, option_string=None):
        path = values[0]
        if not values: return
        if not os.path.isdir(path): 
            print ('Backup root needs to be a directory')
            return
        
        dirs = os.listdir(path)
        dirs = [di for di in dirs if os.path.isdir(di)]
        print ('is this list of dirs ok?')
        print (dirs)
        inp = input ('? y/n ')
        if inp == 'y':
            print ('ok')
        else:
            print ('aborting')


class Archive(argparse.Action):
    
    def __call__(self, parser, namespace, values, option_string=None):
        val = values[0]
        
        if not os.path.isdir(val[0]) or not os.path.isfile(val):
            print ('{} is not a valid path.'.format(val))
            return
         
        subprocess.call(['tar', '-vcf', 'backup.tar', val])


class Upload(argparse.Action):
    
    def __call__(self, parser, namespace, values, option_string=None):
        print (values)

# for all archiving purposes
ARCHIVER_FILE = 'archive.sh'
parser = argparse.ArgumentParser(prog='Backup Maker', description='Backs up all your projects')
parser.add_argument('--root', nargs=1, action=BackupRoot, help='set root directory that contains all your projects to backup', )
parser.add_argument('-a','--archive', nargs=1, action=Archive, help='Creates an archive file of the given directory', )
parser.add_argument('-u','--upload', nargs=1, action=Upload, help='Uploads the backed up files to cloud directory given in config file.', )

parser.parse_args()
