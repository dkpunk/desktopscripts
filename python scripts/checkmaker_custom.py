## checkmaker_custom
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-n','--name',help = "name of the check required")
parser.add_argument('-c','--category',help = "name of the category required")
parser.add_argument('-han','--handlers',help = "list of the handlers required")
parser.add_argument('--interval',help = "check interval")
parser.add_argument('--instance',help = "instance of the check")
parser.add_argument('--command',help = "command which will be executed")
parser.add_argument('--subscribers',help = "list of subscribers required")
parser.add_argument('--check_type',help = "name of the check_type required")

args=parser.parse_args()

print(args)