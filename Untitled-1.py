
def calculate_frequencies(file_contents):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    frequencies = {}
    file_contents = file_contents.split()
    str1 = "" #낱자 하나하나를 넣어 단어를 넣을 문자열 생성

    
    for word in file_contents:
        str1 = ''.join(ch for ch in word if ch.isalnum()) #word의 만약 숫자나 알파벳이면 낱자들을 합하기
        if str1.lower() not in uninteresting_words: 

            if str1.lower() not in frequencies:
                frequencies[str1.lower()] = 1
            else:
                frequencies[str1.lower()] += 1
    return frequencies

print(calculate_frequencies(file_contents))