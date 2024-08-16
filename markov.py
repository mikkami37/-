import random


def generate_text():
    
    characters = ['し', 'か', 'の', 'こ', 'た', 'ん']
    
    transition_matrix = {
        'し': [0.0, 0.5, 0.0, 0.0, 0.5, 0.0],
        'か': [0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
        'の': [0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
        'こ': [0.25, 0.0, 0.5, 0.25, 0.0, 0.0],
        'た': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0],
        'ん': [0.5, 0.0, 0.0, 0.0, 0.5, 0.0]
    }

    target_string = "しかのこのこのここしたんたん"
    generated_text = ""
    current_char = 'し'  

    count=0
    while target_string not in generated_text:

     generated_text += current_char
            
     next_char_prob = transition_matrix[current_char]
     next_char = random.choices(characters, weights=next_char_prob)[0]
     current_char = next_char
     count+=1
    
    return generated_text, count

result = generate_text()
print(result[0])
print("生成文字数："+str(result[1]))

