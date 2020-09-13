#!/usr/bin/env python3

VALID_2ND_POSITION_TOKENS = ('NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS',
                             'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV', 'DATE', 'HEAD', 'TRLR', 'NOTE')
VALID_3RD_POSITION_TOKENS = ('INDI', 'FAM')


def detect_tokens(line):
    tokens = {}
    tokens["string"] = line

    split_line = line.split(" ", 2)

    tokens["level"] = split_line[0]

    if split_line[1] in VALID_2ND_POSITION_TOKENS:
        tokens["tag"] = split_line[1]
        tokens['args'] = split_line[2] if len(split_line) == 3 else ""
        tokens['valid'] = 'Y'
    elif split_line[2] in VALID_3RD_POSITION_TOKENS:
        tokens['args'] = split_line[1]
        tokens["tag"] = split_line[2]
        tokens['valid'] = 'Y'
    else:
        tokens["tag"] = split_line[1]
        tokens['args'] = split_line[2]
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
