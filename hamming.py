def hamming_distance(word1, word2):
    # Make the words equal in length by right-padding with spaces
    len1, len2 = len(word1), len(word2)
    if len1 < len2:
        word1 += ' ' * (len2 - len1)
    elif len2 < len1:
        word2 += ' ' * (len1 - len2)

    # Calculate Hamming distance
    distance = sum(bit1 != bit2 for bit1, bit2 in zip(word1, word2))

    return distance

def hamming_distance_list(target_word, word_list):
    distances = {}

    for word in word_list:
        distance = hamming_distance(target_word, word)
        distances[word] = distance

    return distances

if __name__ == "__main__":
    target_word = input("Enter the target word: ")
    word_list = ["apple", "orange", "banana", "grape", "berry"]

    distances = hamming_distance_list(target_word, word_list)

    print(f"Hamming distances from '{target_word}':")
    for word, distance in distances.items():
        print(f"{word}: {distance}")

