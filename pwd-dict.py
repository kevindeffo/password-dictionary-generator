import random

def collect_user_info():
    print("=== Entrez les informations personnelles ===")
    infos = []
    infos.append(input("Prénom : ").strip())
    infos.append(input("Nom : ").strip())
    infos.append(input("Date de naissance (JJMMAAAA) : ").strip())
    infos.append(input("Ville de naissance : ").strip())
    infos.append(input("Mot-clé supplémentaire : ").strip())
    return [info for info in infos if info]

def generate_password_dictionary(user_data, exact_length, count):
    symbols = ['!', '@', '#', '$', '%', '&', '*']
    numbers = '0123456789'
    base_elements = user_data + [s for s in symbols] + list(numbers)

    dictionary = set()
    max_attempts = count * 10
    attempts = 0

    while len(dictionary) < count and attempts < max_attempts:
        attempts += 1

        parts = random.choices(base_elements, k=5)
        pwd = ''.join(parts)

        # Décider aléatoirement si on applique des majuscules ou pas
        apply_uppercase = random.choice([True, False])  # 50% des cas
        if apply_uppercase:
            pwd = ''.join(
                c.upper() if random.random() < 0.4 and c.isalpha() else c
                for c in pwd
            )

        # Adapter pour que ça fasse exactement la bonne taille
        if len(pwd) < exact_length:
            extra = ''.join(random.choices(''.join(base_elements), k=exact_length - len(pwd)))
            if apply_uppercase:
                extra = ''.join(
                    c.upper() if random.random() < 0.4 and c.isalpha() else c
                    for c in extra
                )
            pwd += extra
        elif len(pwd) > exact_length:
            pwd = pwd[:exact_length]

        dictionary.add(pwd)

    return list(dictionary)


def main():
    user_data = collect_user_info()

    try:
        exact_length = int(input("Longueur EXACTE des mots de passe : "))
        count = int(input("Nombre de mots de passe à générer : "))
    except ValueError:
        print("⚠️  Veuillez entrer des valeurs valides.")
        return

    passwords = generate_password_dictionary(user_data, exact_length, count)

    with open("dictionnaire.txt", "w", encoding="utf-8") as f:
        for pwd in passwords:
            f.write(pwd + "\n")

    print(f"\n✅ {len(passwords)} mots de passe de {exact_length} caractères générés dans 'dictionnaire.txt'.")

if __name__ == "__main__":
    main()
