#!/usr/bin/env python3

VALID_2ND_POSITION_TOKENS = ('NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS',
                             'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV', 'DATE', 'HEAD', 'TRLR', 'NOTE')
VALID_3RD_POSITION_TOKENS = ('INDI', 'FAM')


def detect_tokens(line):
    tokens = {}
    tokens["string"] = line

    line = line.split(" ", 2)

    tokens["level"] = line[0]

    if line[1] in VALID_2ND_POSITION_TOKENS:
        tokens["tag"] = line[1]
        tokens['args'] = line[2]
        tokens['valid'] = 'Y'
    elif line[2] in VALID_3RD_POSITION_TOKENS:
        tokens['args'] = line[1]
        tokens["tag"] = line[2]
        tokens['valid'] = 'Y'
    else:
        tokens["tag"] = line[1]
        tokens['args'] = line[2]
        tokens['valid'] = 'N'
    return tokens


def parse(dir):
    parsed_file = []
    with open(dir, "r") as reader:
        content = reader.read().splitlines()

    for line in content:
        parsed_file.append(detect_tokens(line))
    return parsed_file


def main():

    parsed_file = parse("project02/test_input.ged")

    for tokens in parsed_file:
        print(f"--> {tokens['string']}\n"
              f"<-- {tokens['level']}|{tokens['tag']}|{tokens['valid']}|{tokens['args']}")


if __name__ == "__main__":
    main()
