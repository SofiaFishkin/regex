from pprint import pprint
import re
import csv


def read_file(phonebook_raw):
    with open("phonebook_raw.csv") as f:
      rows = csv.reader(f, delimiter=",")
      contacts_list = list(rows)
    pprint(contacts_list)


def phone_number(contacts_list):
    number_pattern_raw = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)' \
                            r'(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)' \
                            r'(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'
    number_pattern_new = r'+7(\4)\8-\11-\14\15\17\18\19\20'
    contacts_list_updated = list()
    for card in contacts_list:
        card_as_string = ','.join(card)
        formatted_card = re.sub(number_pattern_raw, number_pattern_new, card_as_string)
        card_as_list = formatted_card.split(',')
        contacts_list_updated.append(card_as_list)
    return contacts_list_updated


def format_full_name(contacts_list):
    name_pattern_raw = r'^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)' \
                       r'(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)'
    name_pattern_new = r'\1\3\10\4\6\9\7\8'
    contacts_list_updated = list()
    for card in contacts_list:
        card_as_string = ','.join(card)
        formatted_card = re.sub(name_pattern_raw, name_pattern_new, card_as_string)
        card_as_list = formatted_card.split(',')
        contacts_list_updated.append(card_as_list)
    return contacts_list_updated


def join_duplicates(contacts_list):
    for name in contacts_list:
        for duplicates in contacts_list:
            if name[0] == duplicates[0] and name[1] == duplicates[1] and name is not duplicates:
                if name[2] is '':
                    name[2] = duplicates[2]
                if name[3] is '':
                    name[3] = duplicates[3]
                if name[4] is '':
                    name[4] = duplicates[4]
                if name[5] is '':
                    name[5] = duplicates[5]
                if name[6] is '':
                    name[6] = duplicates[6]
    contacts_list_updated = list()
    for card in contacts_list:
        if card not in contacts_list_updated:
            contacts_list_updated.append(card)
    return contacts_list_updated


def write_file(contacts_list):
    with open("phonebook.csv", "w") as f:
      datawriter = csv.writer(f, delimiter=',')
      datawriter.writerows(contacts_list)


if __name__ == '__main__':
    contacts = read_file('phonebook_raw.csv')
    contacts = phone_number(contacts)
    contacts = format_full_name(contacts)
    contacts = join_duplicates(contacts)
    contacts[0][2] = 'patronymic'
    write_file(contacts)