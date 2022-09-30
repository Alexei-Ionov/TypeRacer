"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns True. If there are fewer than K such paragraphs, return
    the empty string.

    Arguments:
        paragraphs: a list of strings
        select: a function that returns True for paragraphs that can be selected
        k: an integer

    >>> ps = ['hi', 'how are you', 'fine']
    >>> s = lambda p: len(p) <= 4
    >>> choose(ps, s, 0)
    'hi'
    >>> choose(ps, s, 1)
    'fine'
    >>> choose(ps, s, 2)
    ''
    """
    # BEGIN PROBLEM 1
    if k >= len(paragraphs):
        return ''

    elif select(paragraphs[k]) == True:
        return paragraphs[k]

    elif select(paragraphs[k]) != True:
        paragraphs.remove(paragraphs[k])
        return choose(paragraphs, select, k)
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether
    a paragraph contains one of the words in TOPIC.

    Arguments:
        topic: a list of words related to a subject

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    def topic_checker(paragraphs):
        paragraphs1 = lower(paragraphs)
        paragraphs2 = remove_punctuation(paragraphs1)
        paragraphs3 = split(paragraphs2)
        for strings in topic:
            if strings in paragraphs3:
                return True

        return False

    return topic_checker
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    Arguments:
        typed: a string that may contain typos
        reference: a string without errors

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    >>> accuracy('', '')
    100.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
 
    # BEGIN PROBLEM 3

    if typed_words == reference_words:
        percent_correct = 100.0
        return percent_correct

    if not typed_words and not reference_words:
        percent_correct = 100.0
        return percent_correct

    if typed_words and not reference_words:
        percent_correct = 0.0
        return percent_correct

    if not typed_words and reference_words:

        percent_correct = 0.0
        return percent_correct

    elif typed_words != reference_words and len(typed_words) == len(reference_words):

        total = len(typed_words)
        index = 0
        num_right = 0
        typed_words = split(typed)
        reference_words = split(reference)
        while index < total:

            if typed_words[index] == reference_words[index]:
                num_right = num_right + 1

            if typed_words[index] != reference_words[index]:
                num_right = num_right + 0

            percent_correct = (num_right / total) * 100

            index = index + 1

        return percent_correct


    elif typed_words != reference_words and len(typed_words) > len(reference_words):

        total_total = len(typed_words)
        total_part_1 = len(reference_words)
        index = 0
        num_right = 0
        while index < total_part_1:

            if typed_words[index] == reference_words[index]:
                num_right = num_right + 1

            if typed_words[index] != reference_words[index]:
                num_right = num_right + 0

            percent_correct = (num_right / total_total) * 100

            index = index + 1

        return percent_correct


    elif typed_words != reference_words and len(typed_words) < len(reference_words):

        total_short = len(typed_words)
        total_long = len(reference_words)
        index = 0
        num_right = 0
        typed_words = split(typed)
        reference_words = split(reference)
        while index < total_short:

            if typed_words[index] == reference_words[index]:
                num_right = num_right + 1

            if typed_words[index] != reference_words[index]:
                num_right = num_right + 0

            percent_correct = (num_right / total_short) * 100

            index = index + 1

        return percent_correct
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string.

    Arguments:
        typed: an entered string
        elapsed: an amount of time in seconds

    >>> wpm('hello friend hello buddy hello', 15)
    24.0
    >>> wpm('0123456789',60)
    2.0
    """
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    total_length = len(typed)

    if total_length >= 1:
        words = total_length / 5
        time_in_minutes = elapsed / 60
        words_per_minute = words / time_in_minutes
        return words_per_minute

    if total_length == 0:
        return 0.0
    
    
    # END PROBLEM 4


###########
# Phase 2 #
###########

def autocorrect(typed_word, word_list, diff_function, limit):
    """Returns the element of WORD_LIST that has the smallest difference
    from TYPED_WORD. Instead returns TYPED_WORD if that difference is greater
    than LIMIT.

    Arguments:
        typed_word: a string representing a word that may contain typos
        word_list: a list of strings representing reference words
        diff_function: a function quantifying the difference between two words
        limit: a number

    >>> ten_diff = lambda w1, w2, limit: 10 # Always returns 10
    >>> autocorrect("hwllo", ["butter", "hello", "potato"], ten_diff, 20)
    'butter'
    >>> first_diff = lambda w1, w2, limit: (1 if w1[0] != w2[0] else 0) # Checks for matching first char
    >>> autocorrect("tosting", ["testing", "asking", "fasting"], first_diff, 10)
    'testing'
    """
    # BEGIN PROBLEM 5

    if typed_word in word_list:
        return typed_word


    elif typed_word not in word_list:

        index = 0
        B = []
        while index < len(word_list):
            word_in_word_list = word_list[index]
            value = diff_function(typed_word, word_in_word_list, limit)

            B.append(value)

            index = index + 1
        

        if min(B) > limit:
            return typed_word

        else:
            min_index = B.index(min(B))
            desired_word = word_list[min_index]
            return desired_word


            
    
    # END PROBLEM 5


def sphinx_swaps(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths and returns the result.

    Arguments:
        start: a starting word
        goal: a string representing a desired goal word
        limit: a number representing an upper bound on the number of chars that must change

    >>> big_limit = 10
    >>> sphinx_swaps("nice", "rice", big_limit)    # Substitute: n -> r
    1
    >>> sphinx_swaps("range", "rungs", big_limit)  # Substitute: a -> u, e -> s
    2
    >>> sphinx_swaps("pill", "pillage", big_limit) # Don't substitute anything, length difference of 3.
    3
    >>> sphinx_swaps("roses", "arose", big_limit)  # Substitute: r -> a, o -> r, s -> o, e -> s, s -> e
    5
    >>> sphinx_swaps("rose", "hello", big_limit)   # Substitute: r->h, o->e, s->l, e->l, length difference of 1.
    5
    """
    # BEGIN PROBLEM 6
    def helper_function(start, goal, limit, counter):
        counter = counter + 1
        
        index = 0

        if len(start) < 1 or len(goal) < 1:
            return 0

        if counter > limit:
            
            return limit + 1

        elif counter <= limit:
            
            if len(start) == len(goal):
                if start[index] == goal[index]:
                    return 0 + helper_function(start[index+1:], goal[index+1:], limit, counter-1)
                elif start[index] != goal[index]:
                    return 1 + helper_function(start[index+1:], goal[index+1:], limit, counter)



            elif len(start) != len(goal):
                diff = abs(len(start) - len(goal))
                min_length = min(len(start), len(goal))

                if start[index] == goal[index]:
                    return diff + 0 + helper_function(start[index + 1:min_length], goal[index+1:min_length], limit, counter-1)

                elif start[index] != goal[index]:
                    return diff + 1 + helper_function(start[index + 1 :min_length], goal[index+1:min_length], limit, counter)

    return helper_function(start, goal, limit, -1)


    # END PROBLEM 6
def minimum_mewtations(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL.
    This function takes in a string START, a string GOAL, and a number LIMIT.

    Arguments:
        start: a starting word
        goal: a goal word
        limit: a number representing an upper bound on the number of edits

    >>> big_limit = 10
    >>> minimum_mewtations("cats", "scat", big_limit)       # cats -> scats -> scat
    2
    >>> minimum_mewtations("purng", "purring", big_limit)   # purng -> purrng -> purring
    2
    >>> minimum_mewtations("ckiteus", "kittens", big_limit) # ckiteus -> kiteus -> kitteus -> kittens
    3
    """
    def helper_function2(start, goal, limit, counter):

        counter = counter + 1
        index = 0

        if counter > limit:
            return limit + 10

        elif len(start) < 1 or len(goal) < 1:
            if len(start) != len(goal):
                diff = abs(len(start) - len(goal))
                return diff # Fill in the condition
            if len(start) == len(goal):
                return 0


        elif len(start) ==len(goal):

            if start[index] == goal[index]:

                return helper_function2(start[index+1:], goal[index+1:], limit, counter - 1)

            elif start[index] != goal[index]:
                add = 1 + helper_function2(start, goal[1:], limit, counter)
                remove = 1 + helper_function2(start[1:], goal, limit, counter)
                sub = 1 + helper_function2(start[index+1:], goal[index+1:], limit, counter)
                return min(add,remove,sub)

        elif len(start) != len(goal):

    
            if start[index] == goal[index]:
                return helper_function2(start[index+1:], goal[index+1:], limit, counter-1)

            elif start[index] != goal[index]: #BWORD --> WORD
                add = 1 + helper_function2(start, goal[1:], limit, counter)
                remove =  1 + helper_function2(start[1:], goal, limit, counter)
                sub = 1 + helper_function2(start[index + 1:], goal[index + 1:], limit,counter)
                return min(add, remove, sub)


    return helper_function2(start, goal, limit, -1)


def final_diff(start, goal, limit):
    """A diff function that takes in a string START, a string GOAL, and a number LIMIT.
    If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function.'


FINAL_DIFF_LIMIT = 6  # REPLACE THIS WITH YOUR LIMIT


###########
# Phase 3 #
###########


def report_progress(sofar, prompt, user_id, upload):
    """Upload a report of your id and progress so far to the multiplayer server.
    Returns the progress so far.

    Arguments:
        sofar: a list of the words input so far
        prompt: a list of the words in the typing prompt
        user_id: a number representing the id of the current user
        upload: a function used to upload progress to the multiplayer server

    >>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
    >>> # The above function displays progress in the format ID: __, Progress: __
    >>> print_progress({'id': 1, 'progress': 0.6})
    ID: 1 Progress: 0.6
    >>> sofar = ['how', 'are', 'you']
    >>> prompt = ['how', 'are', 'you', 'doing', 'today']
    >>> report_progress(sofar, prompt, 2, print_progress)
    ID: 2 Progress: 0.6
    0.6
    >>> report_progress(['how', 'aree'], prompt, 3, print_progress)
    ID: 3 Progress: 0.2
    0.2
    """
    # BEGIN PROBLEM 8
    index = 0
    score = 0
    while index < len(sofar):

        if sofar[index] == prompt[index]:
            score = score + 1
        elif sofar[index] != prompt[index]:
            break
        index = index + 1

    progress = score / len(prompt)

    d = {'id': user_id, 'progress': progress}

    upload(d)

    return  progress
    # END PROBLEM 8

def helper_function3(words):
    index = 0
    times_list = []
    while index < len(words) -1:
        time_diff = words[index + 1] - words[index]

        times_list.append(time_diff)

        index = index + 1

    return times_list


def time_per_word(words, times_per_player):
    """Given timing data, return a match dictionary, which contains a
    list of words and the amount of time each player took to type each word.

    Arguments:
        words: a list of words, in the order they are typed.
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.

    >>> p = [[75, 81, 84, 90, 92], [19, 29, 35, 36, 38]]
    >>> match = time_per_word(['collar', 'plush', 'blush', 'repute'], p)
    >>> match["words"]
    ['collar', 'plush', 'blush', 'repute']
    >>> match["times"]
    [[6, 3, 6, 2], [10, 6, 1, 2]]
    """
    # BEGIN PROBLEM 9


    times = [helper_function3(k) for k in times_per_player]

    return match(words, times)
    # END PROBLEM 9


def fastest_words(match):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        match: a match dictionary as returned by time_per_word.

    >>> p0 = [5, 1, 3]
    >>> p1 = [4, 1, 6]
    >>> fastest_words(match(['Just', 'have', 'fun'], [p0, p1]))
    [['have', 'fun'], ['Just']]
    >>> p0  # input lists should not be mutated
    [5, 1, 3]
    >>> p1
    [4, 1, 6]
    """
    player_indices = range(len(match["times"]))  # contains an *index* for each player
    word_indices = range(len(match["words"]))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    main_list = []
    im_screwed_for_math_midterm = 0

    while im_screwed_for_math_midterm < len(player_indices):
        main_list.insert(im_screwed_for_math_midterm, [])

        im_screwed_for_math_midterm = im_screwed_for_math_midterm + 1




    for i in word_indices:

        word_at_index = word_at(match, i)


        # find the player with the shortest time put that word in that player's list in the main list

        time_at_index = [time(match, j, i) for j in player_indices]
       

        min_time = min(time_at_index)  #whos time is this?
     

        index_of_min_time = time_at_index.index(min(time_at_index))  #returns the player whos this is
      

        main_list[index_of_min_time].append(word_at_index)


    return main_list
    # END PROBLEM 10


def match(words, times):
    """A dictionary containing all words typed and their times.

    Arguments:
        words: A list of strings, each string representing a word typed.
        times: A list of lists for how long it took for each player to type
            each word.
            times[i][j] = time it took for player i to type words[j].

    Example input:
        words: ['Hello', 'world']
        times: [[5, 1], [4, 2]]
    """
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return {"words": words, "times": times}


def word_at(match, word_index):
    """A utility function that gets the word with index word_index"""
    assert 0 <= word_index < len(match["words"]), "word_index out of range of words"
    return match["words"][word_index]


def time(match, player_num, word_index):
    """A utility function for the time it took player_num to type the word at word_index"""
    assert word_index < len(match["words"]), "word_index out of range of words"
    assert player_num < len(match["times"]), "player_num out of range of players"
    return match["times"][player_num][word_index]


def match_string(match):
    """A helper function that takes in a match dictionary and returns a string representation of it"""
    return f"match({match['words']}, {match['times']})"


enable_multiplayer = True  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)
