class Justify:

    @staticmethod
    def justify_instant():
        test = input('please input a number:')
        if test.isdigit():
                if int(test) % 9 == 0:
                        return ('YES')
                else:
                        return('No')
        else:
            return ('please input a number.')

print(Justify.justify_instant())
