import re
class StrUtil(object):
    @staticmethod
    def upper(s: str) -> str:
        return s.upper()

    @classmethod
    def isblank(cls, string):
        if string in [None,'None','null','NULL','']:
            return True
        else:
            return False
        
    @staticmethod
    def build_string(*items, separator:str = "",):
        items = [item for item in items if not StrUtil.isblank(item)]
        return separator.join(items)
    
    @staticmethod
    def split_file_name(file_name:str):
        pattern = r"(.*?)([_-])([DMYHS_-]+)(\..*)"
        match = re.match(pattern, file_name)
        return match.group(1)+match.group(2), match.group(3), match.group(4)
    
    @staticmethod
    def reformated_date_pattern(date_pattern:str):
        count = {}
        spliters = {}
        for i, char in enumerate(date_pattern):
            if char in ["-", '_']:
                spliters[i] = char
                continue
            if count.get(char) is None:
                count[char] = 0
            count[char] += 1
        pattern = ""
        for index, key in enumerate(count.keys()):
            pattern = pattern + "\\d{" + f"{count.get(key)}" + "}" + (spliters.get(index) if spliters.get(index) else "")
        return pattern