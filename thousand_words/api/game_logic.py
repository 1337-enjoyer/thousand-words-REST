import random


def get_game_question(words_queryset):
    all_words = list(words_queryset)
    target_word = random.choice(all_words)

    other_words = [w for w in all_words if w.id != target_word.id]
    random_others = random.sample(other_words, 2)

    translations = [
        random_others[0].translation,
        random_others[1].translation,
        target_word.translation
    ]
    random.shuffle(translations)

    return {
        "word": target_word.word,
        "translations": translations,
        "solution": target_word.translation
    }

def get_multiple_questions(queryset, count):
    all_words = list(queryset)
    
    if count > len(all_words):
        count = len(all_words)
    
    questions = []
    
    selected_words = random.sample(all_words, count)
    
    for word in selected_words:
        other_words = [w for w in all_words if w.id != word.id]
        
        wrong_translations = []
        for w in random.sample(other_words, min(2, len(other_words))):
            wrong_translations.append(w.translation.strip())
        
        translations = wrong_translations + [word.translation.strip()]
        random.shuffle(translations)
        
        questions.append({
            "word": word.word,
            "translations": translations,
            "solution": word.translation.strip()
        })
    
    return {
        "count": len(questions),
        "questions": questions
    }