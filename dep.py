from sys import stderr


EXIT_SUCCESS = 0
EXIT_FAILURE = 1
HELP_OPTION_DESCRIPTION = "      --help     display this help and exit\n"
VERSION_OPTION_DESCRIPTION = "      --version  output version information and exit\n"
GETOPT_HELP_OPTION_DECL = "help"
GETOPT_VERSION_OPTION_DECL = "version"
MB_LEN_MAX = 1

def emit_try_help():
    stderr.write("Try \'wc --help\' for more information.\n")

def emit_stdin_note():
    print("\nWith no FILE, or when FILE is -, read standard input.\n")

def emit_ancillary_info(program):
    pass

