class User:
    def __init__(self, name='Unknown', num_of_tacos=5, score=0):
        self.name = name
        self.num_of_tacos = num_of_tacos
        self.score = score
        self.__super_private = 'Cue007'
        self._semi_private = 'Cue Nguyen'

    def give_a_taco(self, user):
        if self.num_of_tacos > 0:
            self.num_of_tacos -= 1
            user.num_of_tacos += 1
        else:
            print('Tacos = {}'.format(self.num_of_tacos))

    def __str__(self):
        return '{} has a score of {} with {} taco(s) remaining'.format(self.name, self.score, self.num_of_tacos)

if __name__ == '__main__':
    one_user = User('Cue')
    print(one_user._semi_private)
    # print(one_user.__super_private) --> error
    print(one_user.__dict__)
    print(one_user._User__super_private)