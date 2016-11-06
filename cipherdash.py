# ciperdash.py
# Created by Freegle Yuan on 2016-11-06

# The direct dash in terminal for User to encode and decodes

import ciphermanipulate

cipher_processor = ciphermanipulate.CipherProcessor()
action_type = 1
while 0 < action_type < 5:
    print "\nOptions\n(0) exit\n(1) encode message\n(2) decode message"
    action_type = int(raw_input("Choose: "))


    if action_type > 0:
        key = raw_input("Enter key: ")

    if action_type == 1 or action_type == 2:
        cipher_processor.key = key
        message = raw_input("Enter message: ")
        if action_type == 1:
            print cipher_processor.encode(message)
        else:
            print cipher_processor.decode(message)

    else:
        pass
