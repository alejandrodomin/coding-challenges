def possible(note, magazine):
    for letter in note:
        if letter not in magazine:
            return False
            
    return True
    
if __name__=="__main__":
    print(possible("a", "aksgb"))