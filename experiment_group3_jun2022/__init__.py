from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'Experiment1_group3_Jun2022'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    cubicle_number = models.IntegerField()

    outcome = models.FloatField()

    score1 = models.StringField(
        choices=[[0, 'negative'], [1, 'positive']],
        label='You think your total score is',
        widget=widgets.RadioSelect,
    )

    # score2_positive = models.StringField(
    #     choices=[[4, '0 to 2'], [5, '2 to 4'], [6, '4 to 6']],
    #     label='You think your total score is between',
    # )
    #
    # score2_negative = models.StringField(
    #     choices=[[1, '-6 to -4'], [2, '-4 to -2'], [3, '-2 to 0']],
    #     label='You think your total score is between',
    # )

    score2 = models.StringField(
        choices=[[1, '-6 to -4'], [2, '-4 to -2'], [3, '-2 to 0'], [4, '0 to 2'], [5, '2 to 4'], [6, '4 to 6']],
        label='And your total score is between',
        widget=widgets.RadioSelect,
    )

    # @ staticmethod
    # def get_form_fields(player):
    #    if player.score1 == 'negative':
    #        return ['bid_1', 'bid_2', 'bid_3']
    #    else:
    #        return ['bid_1', 'bid_2']

    info1 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label="",
        widget=widgets.RadioSelect,
    )

    score3 = models.StringField(
        choices=[[0, 'negative'], [1, 'positive']],
        label='Now, you think your total score is',
        widget=widgets.RadioSelect,
    )

    score4 = models.StringField(
        choices=[[1, '-6 to -4'], [2, '-4 to -2'], [3, '-2 to 0'], [4, '0 to 2'], [5, '2 to 4'], [6, '4 to 6']],
        label='And your total score is between',
        widget=widgets.RadioSelect,
    )

    score1_task1 = models.StringField(
        choices=[[0, 'negative'], [1, 'positive']],
        label='You think your total score is',
        widget=widgets.RadioSelect,
    )

    score2_task1 = models.StringField(
        choices=[[1, '-6 to -4'], [2, '-4 to -2'], [3, '-2 to 0'], [4, '0 to 2'], [5, '2 to 4'], [6, '4 to 6']],
        label='And your total score is between',
        widget=widgets.RadioSelect,
    )

    info_task1 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label="",
        widget=widgets.RadioSelect,
    )

    score3_task1 = models.StringField(
        choices=[[0, 'negative'], [1, 'positive']],
        label='Now, you think your total score is',
        widget=widgets.RadioSelect,
    )

    score4_task1 = models.StringField(
        choices=[[1, '-6 to -4'], [2, '-4 to -2'], [3, '-2 to 0'], [4, '0 to 2'], [5, '2 to 4'], [6, '4 to 6']],
        label='And your total score is between',
        widget=widgets.RadioSelect,
    )

    score1_task2 = models.StringField(
        choices=[[0, 'negative'], [1, 'positive']],
        label='You think your total score is',
        widget=widgets.RadioSelect,
    )

    score2_task2 = models.StringField(
        choices=[[1, '-6 to -4'], [2, '-4 to -2'], [3, '-2 to 0'], [4, '0 to 2'], [5, '2 to 4'], [6, '4 to 6']],
        label='And your total score is between',
        widget=widgets.RadioSelect,
    )

    info_task2 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label="",
        widget=widgets.RadioSelect,
    )

    score3_task2 = models.StringField(
        choices=[[0, 'negative'], [1, 'positive']],
        label='Now, you think your total score is',
        widget=widgets.RadioSelect,
    )

    score4_task2 = models.StringField(
        choices=[[1, '-6 to -4'], [2, '-4 to -2'], [3, '-2 to 0'], [4, '0 to 2'], [5, '2 to 4'], [6, '4 to 6']],
        label='And your total score is between',
        widget=widgets.RadioSelect,
    )

    q1 = models.IntegerField(
        choices=[[1,'not at all'], [2, 'somewhat'], [3, 'moderately so'], [4, 'very much so']],
        widget=widgets.RadioSelect,
        label='1. I feel calm.',)

    q2 = models.IntegerField(
        choices=[[1,'not at all'], [2, 'somewhat'], [3, 'moderately so'], [4, 'very much so']],
        widget=widgets.RadioSelect,
        label='2. I feel secure.',)

    q3 = models.IntegerField(
        choices=[[1,'not at all'], [2, 'somewhat'], [3, 'moderately so'], [4, 'very much so']],
        widget=widgets.RadioSelect,
        label='3. I am tense.',)

    q4 = models.IntegerField(
        choices=[[1,'not at all'], [2, 'somewhat'], [3, 'moderately so'], [4, 'very much so']],
        widget=widgets.RadioSelect,
        label='4. I feel strained.',)

    q5 = models.IntegerField(
        choices=[[1,'not at all'], [2, 'somewhat'], [3, 'moderately so'], [4, 'very much so']],
        widget=widgets.RadioSelect,
        label='5. I feel at ease.',)

    q6 = models.IntegerField(
        choices=[[1,'not at all'], [2, 'somewhat'], [3, 'moderately so'], [4, 'very much so']],
        widget=widgets.RadioSelect,
        label='6. I feel upset.',)

    q7 = models.IntegerField(
        choices=[[1,'not at all'], [2, 'somewhat'], [3, 'moderately so'], [4, 'very much so']],
        widget=widgets.RadioSelect,
        label='7. I am presently worrying over possible misfortunes.',)

    q8 = models.IntegerField(
        choices=[[1,'not at all'], [2, 'somewhat'], [3, 'moderately so'], [4, 'very much so']],
        widget=widgets.RadioSelect,
        label='8. I feel satisfied.',)

    q9 = models.IntegerField(
        choices=[[1,'not at all'], [2, 'somewhat'], [3, 'moderately so'], [4, 'very much so']],
        widget=widgets.RadioSelect,
        label='9. I feel frightened.',)

    q10 = models.IntegerField(
        choices=[[1,'not at all'], [2, 'somewhat'], [3, 'moderately so'], [4, 'very much so']],
        widget=widgets.RadioSelect,
        label='10. I feel comfortable.',)

    q11 = models.IntegerField(
        choices=[[1,'not at all'], [2, 'somewhat'], [3, 'moderately so'], [4, 'very much so']],
        widget=widgets.RadioSelect,
        label='11. I feel self-confident.',)

    q12 = models.IntegerField(
        choices=[[1,'not at all'], [2, 'somewhat'], [3, 'moderately so'], [4, 'very much so']],
        widget=widgets.RadioSelect,
        label='12. I feel nervous.',)

    q13 = models.IntegerField(
        choices=[[1,'not at all'], [2, 'somewhat'], [3, 'moderately so'], [4, 'very much so']],
        widget=widgets.RadioSelect,
        label='13. I am jittery.',)

    q14 = models.IntegerField(
        choices=[[1,'not at all'], [2, 'somewhat'], [3, 'moderately so'], [4, 'very much so']],
        widget=widgets.RadioSelect,
        label='14. I feel indecisive.',)

    q15 = models.IntegerField(
        choices=[[1,'not at all'], [2, 'somewhat'], [3, 'moderately so'], [4, 'very much so']],
        widget=widgets.RadioSelect,
        label='15. I an relaxed.',)

    q16 = models.IntegerField(
        choices=[[1,'not at all'], [2, 'somewhat'], [3, 'moderately so'], [4, 'very much so']],
        widget=widgets.RadioSelect,
        label='16. I feel content.',)

    q17 = models.IntegerField(
        choices=[[1,'not at all'], [2, 'somewhat'], [3, 'moderately so'], [4, 'very much so']],
        widget=widgets.RadioSelect,
        label='17. I am worried.',)

    q18 = models.IntegerField(
        choices=[[1,'not at all'], [2, 'somewhat'], [3, 'moderately so'], [4, 'very much so']],
        widget=widgets.RadioSelect,
        label='18. I feel confused.',)

    q19 = models.IntegerField(
        choices=[[1,'not at all'], [2, 'somewhat'], [3, 'moderately so'], [4, 'very much so']],
        widget=widgets.RadioSelect,
        label='19. I feel steady.',)

    q20 = models.IntegerField(
        choices=[[1,'not at all'], [2, 'somewhat'], [3, 'moderately so'], [4, 'very much so']],
        widget=widgets.RadioSelect,
        label='20. I feel pleasant.',)


    age = models.IntegerField(label='What is your age?', min=13, max=125)
    gender = models.StringField(
        choices=[['Male', 'Male'], ['Female', 'Female'], [0, 'Prefer not to answer']],
        label='What is your gender?',
        widget=widgets.RadioSelect,
    )
    ethnicity = models.StringField(
        choices=[[1, 'European'], [2, 'Non-European'], [3, 'Asian'], [4, 'Prefer not to answer']],
        label='What is your ethnicity?',
        widget=widgets.RadioSelect,
    )
    education1 = models.StringField(
        choices=[[1, 'Bachelor'], [2, 'Master'], [3, 'Research Master'], [4, 'PhD']],
        label="what is your current education status?",
        widget=widgets.RadioSelect,
    )
    education2 = models.StringField(
        choices=[[1, '1st Year'], [2, '2st Year'], [3, '3rd Year'], [4, 'None of the above']],
        label="",
        widget=widgets.RadioSelect,
    )
    education3 = models.StringField(
        choices=[['TiSEM', 'TiSEM'], ['TLS', 'TLS'], ['TSB', 'TSB'], ['TSHD', 'TSHD'], [5, 'School of Catholic Theology']],
        label="",
        widget=widgets.RadioSelect,
    )
    work1 = models.StringField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='Do you have a part-time job?',
        widget=widgets.RadioSelect,
    )
    work2 = models.IntegerField(label='If yes, how many hours per week?', min=1, max=56)
    earning = models.StringField(
        choices=[['Grants', 'Grants'], ['Scholarship', 'Scholarship'], ['Loans', 'Loans'], ['Family support', 'Family support'], ['Self support', 'Self support']],
        label='How do you finance your studies?',
        widget=widgets.RadioSelect,
    )
# FUNCTIONS


# PAGES
class CubicleNum(Page):
    form_model = 'player'
    form_fields = ['cubicle_number']


class GeneralInstruction(Page):
    pass


class TutorialP1(Page):
    pass


class TutorialP2(Page):
    form_model = 'player'
    form_fields = ['score1', 'score2']
    # @staticmethod
    # def live_method(player, score1):
    #     if score1 == 'negative':
    #         return 'score2_negative'
    #     else:
    #         return 'score2_positive'

class TutorialP3(Page):
    form_model = 'player'
    form_fields = ['info1']

class TutorialP4(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player):
        if player.info1 == 1:
            return ['score3', 'score4']
        else:
            return

class Task1P1(Page):
    pass

class Task1P2(Page):
    form_model = 'player'
    form_fields = ['score1_task1', 'score2_task1']

class Task1P3(Page):
    form_model = 'player'
    form_fields = ['info_task1']

class Task1P4(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player):
        if player.info_task1 == 1:
            return ['score3_task1', 'score4_task1']
        else:
            return


class Task2P1(Page):
    pass

class Task2P2(Page):
    form_model = 'player'
    form_fields = ['score1_task2', 'score2_task2']

class Task2P3(Page):
    form_model = 'player'
    form_fields = ['info_task2']

class Task2P4(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player):
        if player.info_task2 == 1:
            return ['score3_task2', 'score4_task2']
        else:
            return

    @staticmethod
    def before_next_page(player, timeout_happened):
        if player.id_in_group > 10:
            if player.info_task2 == 1:
                if player.score3_task2 == '0' and player.score4_task2 == '1':
                    player.payoff = 8.9
                    player.outcome = 3.9
                else:
                    player.payoff = 6.9
                    player.outcome = 1.9
            else:
                if player.score1_task2 == '0' and player.score2_task2 == '1':
                    player.payoff = 8.9
                    player.outcome = 3.9
                else:
                    player.payoff = 6.9
                    player.outcome = 1.9
        else:
            if player.info_task1 == 1:
                if player.score3_task1 == '0' and player.score4_task1 == '1':
                    player.payoff = 13
                    player.outcome = 8
                else:
                    player.payoff = 11
                    player.outcome = 6
            else:
                if player.score1_task1 == '0' and player.score2_task1 == '1':
                    player.payoff = 13
                    player.outcome = 8
                else:
                    player.payoff = 11
                    player.outcome = 6



    # @staticmethod
    # def vars_for_template(player):
    #     a = player.payoff - 5
    #     return dict(
    #         a=a,
    #     )

class Questionnaire1(Page):
    form_model = 'player'
    form_fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20']


class Result(Page):
    pass


class Questionnaire2(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'ethnicity', 'work1', 'work2', 'education1', 'education2', 'education3']




page_sequence = [
    CubicleNum, GeneralInstruction,
    Task1P1, Task1P2, Task1P3, Task1P4,
    Task2P1, Task2P2, Task2P3, Task2P4,
    Questionnaire1,
    Result,
    Questionnaire2]
