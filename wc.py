import getopt
import os
from re import split
from sys import exit, argv, stdin
import dep


PROGRAM_NAME = "wc"
BUFFER_SIZE = 16 * 1024

counts = {
    'total_lines' : 0,
    'total_words' : 0,
    'total_chars' : 0,
    'total_bytes' : 0,
    'max_line_length' : 0
}

print_opt = {
    'print_lines' : False,
    'print_words' : False,
    'print_chars' : False,
    'print_bytes' : False,
    'print_linelength' : False
}

number_width = 0
have_read_stdin = False

class Fstatus(object):
    def __init__(self, failed, st):
        self.failed = failed
        self.st = st

longopts = [
    "bytes",
    "chars",
    "lines",
    "words",
    "files0-from=",
    "max-line-length",
    dep.GETOPT_HELP_OPTION_DECL,
    dep.GETOPT_VERSION_OPTION_DECL
]


def iswspace(wc):
    pass

def usage(status):
    if status != dep.EXIT_SUCCESS:
        dep.emit_try_help()
    else:
        print("\nUsage: wc [OPTION]... [FILE]...\n  \
                or:  wc [OPTION]... --files0-from=F\n")
        print("\nPrint newline, word, and byte counts for each FILE, and a total line if\n\
                more than one FILE is specified.  A word is a non-zero-length sequence of\n\
                characters delimited by white space.\n")
        dep.emit_stdin_note()
        print("\n\nThe options below may be used to select which counts are printed, always in\n\
                the following order: newline, word, character, byte, maximum line length.\n  \
                -c, --bytes            print the byte counts\n  \
                -m, --chars            print the character counts\n  \
                -l, --lines            print the newline counts\n")
        print("\n      --files0-from=F    read input from the files specified by\n                           \
                NUL-terminated names in file F;\n                           \
                If F is - then read names from standard input\n  \
                -L, --max-line-length  print the maximum display width\n  \
                -w, --words            print the word counts\n")
        print(dep.HELP_OPTION_DESCRIPTION)
        print(dep.VERSION_OPTION_DESCRIPTION)
        dep.emit_ancillary_info(PROGRAM_NAME)
    
    exit(status)

def write_counts(lines, words, chars, bytes, linelength, file):
    format_sp_int = " %*s"
    format_int = 1

    if print_opt['print_lines']:
        pass
    if print_opt['print_words']:
        pass
    if print_opt['print_chars']:
        pass
    if print_opt['print_bytes']:
        pass
    if print_opt['print_linelength']:
        pass
    if file:
        pass

def wc(fd, file_x, fstatus, current_pos, li):
    ok = True
    counter = {
        'lines': 0,
        'words': 0,
        'chars': 0,
        'bytes': 0,
        'linelength': 0
    }
    count_opt = {
        'count_bytes': False,
        'count_chars': False,
        'count_complicated': False
    }
    file = file_x if file_x else "-"
    count_opt['count_bytes'] = print_opt['print_bytes'] or print_opt['print_chars']
    count_opt['count_chars'] = False
    count_opt['count_complicated'] = print_opt['print_words'] or print_opt['print_linelength']
    string = fd.read()
    counts['total_bytes'] = len(string)
    token_list = split(r"[\s,]+", string)
    if li:
        token_list = list(filter(lambda t: not (t in li), token_list))
    print(token_list)
    counts['total_words'] = len(token_list)
    counts['total_lines'] = len(string.split('\n'))

    return ok

def wc_file(file, fstatus):
    if not file or file == "-":
        have_read_stdin = True
    else:
        fd = open(file, 'r')

def get_input_fstatus(nfiles, file):
    pass

def compute_number_width(nfiles, fstatus):
    width = 1

    if 0 < nfiles and fstatus[0].failed <= 0:
        minimum_width = 1
        regular_total = 0

        for i in fstatus:
            if not i.failed:
                if (i.st.st_mode):
                    regular_total += i.st.st_size
                else:
                    minimum_width = 7
        
        while 10 <= regular_total:
            width += 1
        if width < minimum_width:
            width = minimum_width

    return width

def main():
    files_from = None

    try:
        opts, args = getopt.gnu_getopt(argv[1:], "clLmwe:", longopts)
    except getopt.GetoptError as err:
        print(err)
        usage(dep.EXIT_FAILURE)

    print(opts)
    
    for opt, arg in opts:
        if opt in ("-c", "--bytes"):
            print_opt['print_bytes'] = True
        elif opt in ("-m", "--chars"):
            print_opt['print_chars'] = True
        elif opt in ("-l", "--lines"):
            print_opt['print_lines'] = True
        elif opt in ("-w", "--words"):
            print_opt['print_words'] = True
        elif opt in ("-L", "--max-line-length"):
            print_opt['print_linelength'] = True
        elif opt == "--files0-from":
            files_from = arg
        elif opt == "--help":
            usage(dep.EXIT_SUCCESS)
        # else:
        #     usage(dep.EXIT_FAILURE)

    stop_token_list = []
    for opt, arg in opts:
        if opt == "-e":
            stoplist = open(arg)
            stop_token_list = stoplist.read().split()
            stoplist.close()

    if not (print_opt['print_lines'] or print_opt['print_words'] or print_opt['print_chars'] or print_opt['print_bytes'] or print_opt['print_linelength']):
        print_opt['print_lines'] = False
        print_opt['print_words'] = False
        print_opt['print_bytes'] = False

    if os.path.isdir(args[0]):
        pass
    elif os.path.exists(args[0]):
        fd = open(args[0])
        wc(fd, args[0], None, 0, stop_token_list)
        fd.close()

    write_counts(None, None, None, None, None, args[0])

    read_tokens = False

    if files_from:
        if files_from == "-":
            stream = stdin
        else:
            stream = open(files_from, "r")
    
#    fstatus = get_input_fstatus(nfiles, files)
#    number_width = compute_number_width(nfiles, fstatus)

    ok = True

    if ok and (not files_from):
        pass
    
    return dep.EXIT_SUCCESS if ok else dep.EXIT_FAILURE

if __name__ == "__main__":
    main()
