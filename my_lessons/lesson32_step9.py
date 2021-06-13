def test_substring(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке
    if substring not in full_string:
        print(f"expected '{substring}' to be substring of '{full_string}'")