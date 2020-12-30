import json
import sys
import argparse


def decompress(s):
    table = {i: chr(i) for i in range(0, 256)}
    last = s[0]
    result = [last]
    for k in range(1, len(s)):
        code = ord(s[k])
        entry = table[code] if code in table else last + last[0]
        result.append(entry)
        table[k + 255] = last + entry[0]
        last = entry
    return "".join(result)


def cmd_help():
    parser.print_help(sys.stderr)
    sys.exit("need command")


def cmd_decompress():
    pe = json.loads(sys.stdin.read())
    pe["data"] = decompress(pe["data"])
    print(json.dumps(pe))


parser = argparse.ArgumentParser(
    description="Tool for dealing with savefiles from http://petscii.krissz.hu/"
)
sub_parsers = parser.add_subparsers()
parser.set_defaults(command=cmd_help)
parser_de = sub_parsers.add_parser(
    "decompress-data", aliases=["dd"], help="decompress data field in-place"
)
parser_de.set_defaults(command=cmd_decompress)

if __name__ == "__main__":
    args = parser.parse_args()
    args.command()
