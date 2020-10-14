import sys


class Message:
    def __init__(self, hl7_line):
        splits = r"|^~\&"
        self.message_segments = hl7_line.split(splits[0])
        self.name = self.message_segments[0]
        self.content = "|".join(self.message_segments[1:])

    def to_list(self):
        # return [self.name, self.content]
        return self.message_segments

    def __repr__(self):
        return self.name


class HL7:
    def __init__(self, hl7_file):
        with open(hl7_file, 'r') as f:
            contents = [line.strip() for line in f.readlines()]
        self.messages = [Message(line).to_list() for line in contents]

    def normalize(self):
        longest = max([len(message) for message in self.messages])
        for message in self.messages:
            items_to_append = longest - len(message)
            to_append = [""]*items_to_append
            message += to_append
        return self.messages


if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit(print("Enter an HL7 file"))
    elif sys.argv[1].split(".")[-1].upper() != "HL7":
        sys.exit(print("Not a valid HL7 file"))
    else:
        hl7 = HL7(sys.argv[1])
