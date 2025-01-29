import argparse
import secrets
import string
import random

def generate_password(length=12, use_digits=True, use_specials=True, use_upper=True, use_lower=True):
    """Gera uma senha segura de acordo com as configuraçoes especificadas."""
    character_pool = ""

    if use_upper:
        character_pool += string.ascii_uppercase
    if use_lower:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_specials:
        character_pool += string.punctuation
    
    if not character_pool:
        raise ValueError("Pelo menos um conjunto de caracteres deve ser selecionado.")

    password = ''.join(secrets.choice(character_pool) for _ in range(length))
    return password

def generate_passphrase(words_count=4):
    """Gera uma passphrase (frase secreta) usando palavras aleatórias."""
    with open("wordlist.txt", "r", encoding="utf-8") as file:
        words = [word.strip() for word in file.readlines()]
    
    if len(words) < words_count:
        raise ValueError("A wordlist não contém palavras suficientes para a geração.")
    
    passphrase = ' '.join(random.sample(words, words_count))
    return passphrase

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gerador de Senhas Seguras 🔑")
    parser.add_argument("-l", "--length", type=int, default=12, help="Comprimento da senha (padrão: 12 caracteres)")
    parser.add_argument("-d", "--digits", action="store_true", help="Incluir números")
    parser.add_argument("-s", "--specials", action="store_true", help="Incluir caracteres especiais")
    parser.add_argument("-u", "--upper", action="store_true", help="Incluir letras maiúsculas")
    parser.add_argument("-p", "--passphrase", action="store_true", help="Gerar uma passphrase (frase secreta)")
    parser.add_argument("-w", "--words", type=int, default=4, help="Número de palavras na passphrase (padrão: 4)")

    args = parser.parse_args()

    if args.passphrase:
        print(f"🔐 Sua Passphrase: {generate_passphrase(args.words)}")
    else:
        print(f"🔑 Sua Senha: {generate_password(args.length, args.digits, args.specials, args.upper, True)}")