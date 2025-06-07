import re

class Person():
    def __init__(self, name, groups):
        self.name = name
        self.groups = groups
        self.groups.append(name)
    def __str__(self):
        return f"{self.name}: {self.groups}"

class TextSection():
    def __init__(self, text, tags):
        self.text = text
        self.tags = tags
    def __str__(self):
        return f"{self.tags}: {self.text}"

class Generator():
    def __init__(self):
        pass

    def _cleanDoubleEmptyLines(self, lines):
        result = []
        prevEmpty = False

        for s in lines:
            if s == "":
                if not prevEmpty:
                    result.append(s)
                    prevEmpty = True
            else:
                result.append(s)
                prevEmpty = False

        return result

    def _linesToText(self, lines):
        text = ""
        for line in lines:
            text += line
            text += "\n"
        return text        

    def _areTokensValid(self, tokens):
        if len(tokens) == 0:
            return False
        for token in tokens:
            if token.strip() == "":
                return False
        return True

    def _isValidTagLine(self, tagLine):
        return re.fullmatch(r'(\[[^\[\]]+\])+', tagLine)

    def generate(self, str):
        lines = str.splitlines()
        if len(lines) == 0:
            return []
        persons = []
        textSections = []

        # first line
        if not self._isValidTagLine(lines[0].strip()):
            raise Exception(f"0")

        tags = re.findall(r"\[(.*?)\]", lines[0].strip())
        tags = [t.strip() for t in tags]

        if len(tags) != len(set(tags)):
            raise Exception(f"0")
        
        for tag in tags:
            tokens = tag.split(":")
            tokens = [t.strip() for t in tokens]
            if not self._areTokensValid(tokens):
                raise Exception(f"0")
            persons.append(Person(tokens[0], tokens[1:]))

        # following lines
        i = 0
        #print(len(lines))
        while i < len(lines) -1:
            #print(f"HERE {i}")
            i += 1
            line = lines[i].strip()
            #print(f"{i}: {line}")
            if line == "":
                continue
            if line.startswith("---"):
                textSections.append(TextSection("", ["Alle"]))
                continue
            # jetzt muss es sich um eine tag-line halten
            if not self._isValidTagLine(line):
                #print(f"{i}: {line}")
                raise Exception(f"{i}")
            tags = re.findall(r"\[(.*?)\]", line.strip())
            tags = [t.strip() for t in tags]
            i += 1
            #print(f"-{i}: { lines[i]}")
            if i == len(lines):
                raise Exception(f"{i}")
            textSections.append(TextSection(lines[i], tags))

        texts = []

        for person in persons:
            output = []
            for textSection in textSections:
                if "Alle" in textSection.tags or any(x in person.groups for x in textSection.tags):
                    output.append(textSection.text)
            output = self._cleanDoubleEmptyLines(output)
            texts.append((person.name, self._linesToText(output)))
        
        return texts