# This method exploits the fact that we know the server has no security and
# there is no encrpytion done to make the password secure.
# This method is known as a timing attack
def check_password(user, guess) -> bool:
    import server
    actual = server.password_database[user]
    if len(guess) != len(actual):
        return False

    for i in range(len(guess)):
        if guess[i] != actual[i]:
            return False
    return True


def random_str(size) -> str:
    import random
    import server
    return ''.join(random.choices(server.allowed_characters, k=size))


def crack_length(user, max_password_length=32, verbose=False) -> int:
    import numpy as np
    import timeit

    trials = 1000
    attempts = np.empty(max_password_length)

    for i in range(max_password_length):
        i_time = timeit.repeat(stmt='check_password(user, guess)',
                               setup=f'user={user!r};guess=random_str({i!r})',
                               globals=globals(),
                               number=trials,
                               repeat=10)
        # repeat the function check_password(user, x)
        # with user parameter given user=user and guess is a random string of length i
        # gloals() gives access to global variables
        # do this process trials=1000 amount of times
        # repeat above repeat=10 amount of times 

        attempts[i] = min(i_time)
        # take the minimum time for lowest variablility

    if verbose:
        np.set_printoptions(precision=4)
        most_likely_length = np.argsort(attempts)[::-1][:5]
        percents = attempts[most_likely_length] / attempts[most_likely_length[0]]

        print(f'\npassword length = {most_likely_length}')
        print(f'likelihood = {percents}\n')
        # top 5 most likely password lengths as a percentage of the first most likely length
            # as a percentage of the first

    most_likely = int(np.argmax(attempts))
    return most_likely
