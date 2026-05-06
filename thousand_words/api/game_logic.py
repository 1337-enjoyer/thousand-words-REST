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
