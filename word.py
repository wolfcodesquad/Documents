from mailmerge import MailMerge
from datetime import date


def generate_doc(template, data, output):
    document = MailMerge((template))
    document.merge(**data)
    print(document.get_merge_fields())
    document.write(output)