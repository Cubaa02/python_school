# structures.py

def charFrequency(sentence):
    # Step 3: Use a dictionary to count the frequency of each character
    frequency = {}
    for char in sentence:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    # Step 4: Convert the dictionary to a list of tuples and sort it by frequency in descending order
    sorted_frequency = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
    
    # Step 5: Return the sorted list of tuples
    return sorted_frequency

# Example usage
sentence = "Tři sta třicet tři stříbrných stříkaček přestříkalo přes tři sta třicet tři stříbrných střech."
print(charFrequency(sentence))