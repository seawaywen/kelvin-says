#!/usr/bin/env python3

import random

good_list = [
    "In our village, folks say God crumbles up the old moon into stars.  -Alexander Solzhenitsyn, One Day in the Life of Ivan Denisovich",
    "She wasn't doing a thing that I could see, except standing there leaning on the balcony railing, holding the universe together.  -J. D. Salinger, 'A Girl I Knew'",
    "I took a deep breath and listened to the old brag of my heart; I am, I am, I am.  -Sylvia Plath, The Bell Jar",
    "Beauty is an enormous, unmerited gift given randomly, stupidly.  -Khaled Hosseini, And the Mountains Echoed",
    "Sometimes I can feel my bones straining under the weight of all the lives I'm not living.  -Jonathan Safran Foer, Extremely Loud and Incredibly Close",
    "What are men to rocks and mountains?   -Jane Austen, Pride and Prejudice",
    "'Dear God,' she prayed, 'let me be something every minute of every hour of my life.'  -Betty Smith, A Tree Grows in Brooklyn",
    "The curves of your lips rewrite history.   -Oscar Wilde, The Picture of Dorian Gray",
    "A dream, all a dream, that ends in nothing, and leaves the sleeper where he lay down, but I wish you to know that you inspired it.  -Charles Dickens, A Tale of Two Cities",
    "As Estha stirred the thick jam he thought Two Thoughts and the Two Thoughts he thought were these: a) Anything can happen to anyone. and b) It is best to be prepared.  -Arundhati Roy, The God of Small Things",
    "If equal affection cannot be, let the more loving one be me.  -W. H. Auden, 'The More Loving One'",
    "And now that you don't have to be perfect, you can be good.  -John Steinbeck, East of Eden",
    "There are more things in Heaven and Earth, Horatio, than are dreamt of in your philosophy.  -William Shakespeare, Hamlet",
    "America, I've given you all and now I'm nothing.   -Allen Ginsburg, 'America'",
    "It might be that to surrender to happiness was to accept defeat, but it was a defeat better than many victories.  -W. Somerset Maugham, Of Human Bondage",
]

def get_sentence():
    return(good_list[random.randint(0, len(good_list) - 1)])


if __name__ == '__main__':
    good = get_sentence()
    print('-' * len(good))
    print(good)
    print('-' * len(good))
