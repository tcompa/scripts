'''
program: simple_class.py
created: 2016-03-14 -- 17 CEST
'''

import random


class Gaussian_distribution():
    '''
    Gaussian_distribution class.

    Methods:
       * __init__()          : Initialize one instance.
       * get_variance()      : Compute the variance.
       * get_random_sample() : Extract one random sample.
    '''

    def __init__(self, mu, sigma):
        '''
        Initialize a Gaussian_distribution instance.

        Args:
           mu    : Mean of the distribution.
           sigma : Standard deviation of the distribution.
        '''
        self.mean = mu
        self.std = sigma
        print('Initialized Gaussian distribution' +
              ' (mean=%f, std=%f)' % (self.mean, self.std))

    def get_variance(self):
        '''Compute and return the variance of the distribution.'''
        return self.std ** 2

    def get_random_sample(self):
        '''Extract a random sample from the distribution.'''
        return random.gauss(self.mean, self.std)


G1 = Gaussian_distribution(3.0, 0.75)
G2 = Gaussian_distribution(7.0, 0.25)
print('Variance of G1: %f' % G1.get_variance())
print('Variance of G2: %f' % G2.get_variance())

for i in range(10):
    sample = G1.get_random_sample()
    print('%i-th sample from G1: %f' % (i, sample))
