class Worker:
    def __init__(
            self,
            name: str,
            surname: str,
            position: str,
            wage: float = 0,
            bonus: float = 0
    ):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"Зарплата": wage, "Премия": bonus}


class Position(Worker):
    def get_full_name(self, reverse=False):
        return ' '.join(sorted([self.name, self.surname], reverse=reverse))

    def get_total_income(self):
        return sum(self._income.values())

if __name__ == '__main__':
    position_data = [
        {
            'name': 'Ivan',
            'surname': 'Petrov',
            'position': 'Scrum master',
            'wage':  40000,
            'bonus': 0
        },
        {
            'name': 'Oleg',
            'surname': 'Ivanov',
            'position': 'developer',
            'wage':  90000,
            'bonus': 60000
        },
        {
            'name': 'Ekaterina',
            'surname': 'Ivanova',
            'position': 'service delivery manager',
            'wage':  60000,
            'bonus': 30000
        },
    ]

    for item in position_data:
        position = Position(**item)

        print('#######################################')
        print('From data: ', item)
        print('Position name: ', position.name)
        print('Position surname: ', position.surname)
        print('Position full name: ', position.get_full_name())
        print('Position full name reverse: ', position.get_full_name(reverse=True))
        print('Position position: ', position.position)
        print('Position total income: ', position.get_total_income())
        print('#######################################\n\n')
