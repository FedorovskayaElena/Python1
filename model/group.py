from sys import maxsize
from model.technical import clear_extra_spaces


class Group:
    def __init__(self, name=None, header=None, footer=None, group_id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.group_id = group_id

    def __repr__(self):
        return "%s: %s, %s, %s" % (self.group_id, self.name, self.header, self.footer)

    def __eq__(self, other):
        return (self.group_id is None or other.group_id is None or str(self.group_id) == str(other.group_id)) and \
               clear_extra_spaces(self.name) == clear_extra_spaces(other.name)

    def id_or_max(self):
        if self.group_id:
            return int(self.group_id)
        else:
            return maxsize

    def clean_group(self, id_transfer_to_int=False):
        if self.name is not None:
            self.name = clear_extra_spaces(self.name)
        if self.header is not None:
            self.header = clear_extra_spaces(self.header)
        if self.footer is not None:
            self.footer = clear_extra_spaces(self.footer)
        if id_transfer_to_int:
            self.group_id = int(self.group_id)
        return self

    def copy_not_null_fields_from_group(self, new):
        if new.name is not None:
            self.name = new.name
        if new.header is not None:
            self.header = new.header
        if new.footer is not None:
            self.footer = new.footer
        if new.group_id is not None:
            self.group_id = new.group_id
        return self
