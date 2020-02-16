#!/usr/bin/env python3
# author_email="mohamadhayeri9@gmail.com"
# author_git_profile = "https://github.com/mohamadhayeri9"

"""
Explain problem:
We want to do inner join betwen two string. These strings have multiple words.
"""


def inner_join(str1: str, str2: str) -> list:
    result = list(set(str1.split()) & set(str2.split()))
    return result


def main() -> None:
    str1 = """
    Emma
    Olivia
    Ava
    Isabella
    Sophia
    Charlotte
    Mia
    Amelia
    Harper
    Evelyn
    Abigail
    Emily
    Elizabeth
    Mila
    Ella
    Avery
    Sofia
    Camila
    Aria
    Scarlett
    Victoria
    Madison
    Luna
    Grace
    Chloe
    Penelope
    Layla
    Riley
    Nora
    Lily
    Eleanor
    Hannah
    Lillian
    Addison
    Aubrey
    Ellie
    Stella
    Natalie
    Zoe
    Leah
    Hazel
    Violet
    Aurora
    Savannah
    Audrey
    Brooklyn
    Bella
    Claire
    Skylar
    """
    
    str2 = "asd dfg"
    result = inner_join(str1, str2)
    print(result)


if __name__ == "__main__":
    main()
