import string

bad_words = ['madarchod', 'bhosdike', 'gandu', 'behenchod', 'saala', 'chutiyapa']

def count_words(text):
    return len(text.split())

def count_chars(text):
    return len(text)

def count_vowels(text):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)

def count_consonants(text):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char.isalpha() and char not in vowels)

def find_palindromes(text):
    words = text.split()
    return [word for word in words if word.lower() == word[::-1].lower() and len(word) > 1]

def filter_bad_words(text):
    words = text.split()
    clean_words = []
    found = []
    for word in words:
        if word.lower() in bad_words:
            clean_words.append("😶")
            found.append(word)
        else:
            clean_words.append(word)
    return " ".join(clean_words), found

def most_frequent_word(text):
    word_freq = {}
    for word in text.split():
        word = word.lower()
        word_freq[word] = word_freq.get(word, 0) + 1
    max_word = max(word_freq, key=word_freq.get)
    return max_word, word_freq[max_word]

# 💬 Main Program
if __name__ == "__main__":
    user_input = input("💬 Enter your text: ")

    print("\n🔍 Analyzing...\n")

    print("📦 Total Words:", count_words(user_input))
    print("🧮 Total Characters:", count_chars(user_input))
    print("🟢 Vowels:", count_vowels(user_input))
    print("🟤 Consonants:", count_consonants(user_input))

    cleaned, bad_found = filter_bad_words(user_input)
    print("🚫 Bad Words Found:", len(bad_found), "→", bad_found)
    print("🧼 Cleaned Text:", cleaned)

    palindromes = find_palindromes(user_input)
    print("🔁 Palindromes Found:", palindromes)

    word, freq = most_frequent_word(user_input)
    print("🏆 Most Frequent Word:", f"'{word}' ({freq} times)")
