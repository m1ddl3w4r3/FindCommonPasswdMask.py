passwords_file = "passwords.txt"

from collections import Counter

def create_password_mask(passwords_file):
    mask_dict = {
        "uppercase":"?u",
        "lowercase":"?l",
        "digit":"?d",
        "special":"?s"
    }

    def get_mask(char):
        if char.isupper():
            return mask_dict['uppercase']
        elif char.islower():
            return mask_dict['lowercase']
        elif char.isdigit():
            return mask_dict['digit']
        else:
            return mask_dict['special']
    with open(passwords_file, 'r') as file:
        lines = file.readlines()

    masks = []
    for line in lines:
        line = line.strip()
        mask = ''.join(get_mask(char) for char in line)
        masks.append(mask)
    return masks

password_masks = create_password_mask(passwords_file)

mask_counter = Counter(password_masks)

three_mask = mask_counter.most_common(10)


print("Top 10 Password Masks")
print("---------------------")
for i, (mask, count) in enumerate(three_mask, 1):
    print(f"{i}. {mask}: {count} occurrences")