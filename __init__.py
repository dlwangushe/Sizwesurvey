from otree.api import *



class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Gender = models.StringField(
        choices=['Male', 'Female', 'Prefer not to answer'],
        label='1.What is your gender status?',
        widget=widgets.RadioSelect,
    )
    Age = models.IntegerField(
        choices=[[1, '0-15 years old'], [2, '15-35years old'], [3, '35-45'], [4, '45years and above']],
        label='2.What is your age ?',
        widget=widgets.RadioSelect,
    )
    Ethnicity = models.StringField(
        choices=['Black African', 'White', 'Indian/Asian', 'Colored'],
        label='3. Please specify your ethnicity',
        widget=widgets.RadioSelect,
    )
    Education = models.StringField(
        choices=['Primary', 'High school', 'Bachelor degree', 'Masters degree', 'PhD degree', 'Trade school'],
        label='4. What is the highest degree or level of education you have achieved?',
        widget=widgets.RadioSelect,
    )
    Marital_status = models.StringField(
        choices=['Yes', 'No', 'Prefer not to say'],
        label='5. Are you married?',
        widget=widgets.RadioSelect,
    )
    Economic_status = models.IntegerField(
        choices=[[1, 'R0-R5000'], [2, 'R5000-R15000'], [3, 'R15000-R25000'], [4, 'R25000-R35000'],
                 [5, 'R35000 and above']],
        label='6. What is your household annual income?',
        widgest=widgets.RadioSelect,
    )
    Employment_status = models.StringField(
        choices=['Employed full-time', 'Employed part-time', 'Seeking opportunities', 'Retired'],
        label='7. What is your current employemnt status?',
        widget=widgets.RadioSelect,
    )
    Savings_Group = models.IntegerField(
        choices=[[1, 'Leader'], [2, 'Very active'], [3, 'Somewhat active'],
                 [4, 'Does not participate in decision making']],
        label='8.How actively does this person participate in the group’s decision making? ?',
        widget=widgets.RadioSelect,
    )
    Household_participation = models.StringField(
        choices= ['More', 'Same number', 'Fewer'],
        label='9.In the past five years, does a member of your household participate in more or fewer groups or organisation?',
        widget=widgets.RadioSelect,
    )

    Household_belonging = models.StringField(label='10.Of all the groups to which members of your household belong, which two or more are important to your household?')
    Household_group_participation = models.IntegerField(
        label='11.In the past 12 months how many times did a member of this household participate in this group of activities,for example doing group or attending meetings?')
    Group_Member = models.StringField(
        choices=['Born into the group', 'Required to join', 'Invited', 'Voluntary choice'],
        label='12.How does one become a member of this group?',
        widget=widgets.RadioSelect,
    )
    Household_contribution = models.IntegerField(
        label='13.How much money or goods did your household contribute to this group in the past 12 months?')
    Household_work_days = models.IntegerField(
        label='14.How many days of work did your household give to this group in the past 12 months?')


    Group_benefit = models.StringField(
        choices=['Improves my household livelihood or access to service', 'Important in times of emergency/in future', 'Benefits the community', 'Enjoyment/Recreation', 'Spiritual', 'soicial status', 'self-esteem', 'Other (specify)'],
        label='15.What is the main benefit from joining this group?',
        widget=widgets.RadioSelect,
    )
    Household_access1 = models.StringField(
        choices=['Yes', 'No'],
        label='16a.Does the group help your household get access to any of the following services?',
        widget=widgets.RadioSelect,
    )
    Household_access2 = models.StringField(
        choices=['Education', 'Health services', 'Savings or credit', 'Water supply or sanitation', 'Agricultural input or technology', 'Other (specify)'],
        label='16b.Generally, does your household get assistance from the group to access the following categories?',
        widget=widgets.RadioSelect,
    )
    Group_members1 = models.StringField(
        choices=['Yes', 'No'],
        label='17a.Thinking about the members of this group, are most of them of the same',
        widget=widgets.RadioSelect,
    )
    Group_members2 = models.StringField(
        choices=['Neighborhood/Village', 'Family or Kin group', 'Religion', 'Gender', 'Age', 'Ethnic or linguistic group/race/caste/tribe'],
        label='17b.Thinking about the members of this group, are most of them of the coming from the same village or religion to mention the few?',
        widget=widgets.RadioSelect,
    )
    Same_members = models.StringField(
        choices=['Yes', 'No'],
        label='18a.Do members mostly have the same?',
        widget=widgets.RadioSelect,
    )
    Same_members2 = models.StringField(
        choices=['Occupation', 'Educational background or level'],
        label='18b.Are these members mostly have the same job or they have the same level of education?',
        widget=widgets.RadioSelect,
    )
    Rich_poor_members = models.StringField(
        choices=['Old age grant', 'Mixed rich/poor'],
        label='19.Are some members richer or poorer than others, or do they all have mostly the same income level?',
        widget=widgets.RadioSelect,
    )
    Group_Decision = models.StringField(
        choices=['Decision is imposed from outside', 'The leader decides and inform the other group members', 'The leader asks group members what they think and then decides', 'The group members hold a discussion and decide together', 'Other (specify)'],
        label='20.Where there is a decision to made in the group, how does this usually come about?',
        widget=widgets.RadioSelect,
    )
    Leadership_elections = models.StringField(
        choices=['By someone from outside', 'Each leader chooses his/her successor', 'By a committee within the group', 'By elections', 'Other (specify)'],
        label='21.How are leaders in this group are elected?',
        widget=widgets.RadioSelect,
    )
    Effective_leadership = models.StringField(
        choices=['Very effective', 'Somewhat effective', 'Not effective'],
        label='22.Overall, how effective is the group leadership?',
        widget=widgets.RadioSelect,
    )
    Group_funding = models.StringField(
        choices=['From members', 'Other sources within the society', 'Sources from outside the society'],
        label='23.What is the most important source of funding of this group?',
        widget=widgets.RadioSelect,
    )
    Group_advice = models.StringField(
        choices=['From the members', 'From other sources within the society', 'From sources outside the society'],
        label='24.What is the most important advice which this group receives?',
        widget=widgets.RadioSelect,
    )
    Original_funder = models.StringField(
        choices=['Central government', 'Local government', 'Local leader', 'Community members'],
        label='25.Who originally funded the group?',
        widget=widgets.RadioSelect,
    )
    Close_friends = models.IntegerField(
        label='26.About how many close friends do you have these days?')
    Small_money = models.StringField(
         choices=['No one', 'One or two people', 'Three or four people', 'Five or more'],
         label='27.If you suddenly need a small amount of money, how many people beyond your intermediate household could you turn to who would be willing to provide this money?',
         widget=widgets.RadioSelect,
    )
    How_many_people = models.IntegerField(
         label='28.If not zero of those people, how many do you think are currently are able to provide this money?')
    Economic_status = models.StringField(
         choices=['Similar', 'Higher', 'Lower'],
         label='29.If not zero are most of these people of similar/higher/lower economic status?',
         widget=widgets.RadioSelect,
    )
    Other_reason = models.StringField(
        label='30.What are other benefit from joining this group which are not in the options above?')
    Neighborhood_trust = models.StringField(
         choices=['Definitely', 'Probably', 'Probably not', 'Definitely not'],
         label='31.If you suddenly had to go away for a day or two, could you count on your neighbors to take care of your children?',
         widget=widgets.RadioSelect,
    )
    Emergency = models.StringField(
        choices=['No one', 'One or two people', 'Three or four people', 'Five or more'],
        label='32.If you faced a long term emergency such as the death of a breadwinner or rural harvest failure or job loss, how many people beyond your intermediate household could you         turn to who would be willing to assist you?',
        widget=widgets.RadioSelect,
    )
    People_assist = models.IntegerField(
        label='33.If not zero of those people, how many do you think are currently able to assist you?')
    Personal_problem = models.IntegerField(
        label='34.In the past 12 months, how many people with a personal problem have you turned to for assistance?')
    People_trusted = models.StringField(
        choices=['Most people can be trusted', 'You can not be too careful'],
        label='35.Generally speaking, would would you say most people can be trusted or that you cannot be too careful in your dealings with other people?',
        widget=widgets.RadioSelect,
    )
    Agree_disagree1 = models.IntegerField(
        choices=[[1,'1. Strongly disagree'], [2,'2. Disagree somewhat'],  [3,'3. Neither disagree nor agree'], [4,'4. Agree somewhat'], [5,'5.Strongly agree']],
        label='36a.Most people who lived in this village/neighborhood can be trusted',
        widget=widgets.RadioSelect,
    )
    Agree_disagree2 = models.IntegerField(
        choices=[[1,'1. Strongly disagree'], [2,'2. Disagree somewhat'],  [3,'3. Neither disagree nor agree'], [4,'4. Agree somewhat'], [5,'5.Strongly agree']],
        label='36b.In this village/neighborhood, one has to be alert or someone is likely take advantage of you',
        widget=widgets.RadioSelect,
    )
    Agree_disagree3 = models.IntegerField(
        choices=[[1,'1. Strongly disagree'], [2,'2. Disagree somewhat'],  [3,'3. Neither disagree nor agree'], [4,'4. Agree somewhat'], [5,'5.Strongly agree']],
        label='36c.Most people in this village/neighborhood are willing to help you if you need it',
        widget=widgets.RadioSelect,
    )
    Agree_disagree4 = models.IntegerField(
        choices=[[1,'1. Strongly disagree'], [2,'2. Disagree somewhat'],  [3,'3. Neither disagree nor agree'], [4,'4. Agree somewhat'], [5,'5.Strongly agree']],
        label='36d.In this village/neighborhood, people generally do not trust each other in matters of lending or borrowing money',
        widget=widgets.RadioSelect,
    )
    Trust_people_category1 = models.IntegerField(
        choices=[[1,'1.To a very small extent'], [2,'2.To a small extent'], [3,'3.Neither small nor great extent'], [4,'4.To a great extent'], [5,'5.To a very great extent']],
        label='37a.People from your ethnic or linguistic group/race/tribe etc',
        widget=widgets.RadioSelect,
    )
    Trust_people_category2 = models.IntegerField(
        choices=[[1,'1.To a very small extent'], [2,'2.To a small extent'], [3,'3.Neither small nor great extent'], [4,'4.To a great extent'], [5,'5.To a very great extent']],
        label='37b.People from other ethnic or linguistic group/race/tribe etc',
        widget=widgets.RadioSelect,
    )
    Trust_people_category3 = models.IntegerField(
        choices=[[1,'1.To a very small extent'], [2,'2.To a small extent'], [3,'3.Neither small nor great extent'], [4,'4.To a great extent'], [5,'5.To a very great extent']],
        label='37c.Shopkeepers',
        widget=widgets.RadioSelect,
    )
    Trust_people_category4 = models.IntegerField(
        choices=[[1,'1.To a very small extent'], [2,'2.To a small extent'], [3,'3.Neither small nor great extent'], [4,'4.To a great extent'], [5,'5.To a very great extent']],
        label='37d.Local government officials',
        widget=widgets.RadioSelect,
    )
    Trust_people_category5 = models.IntegerField(
        choices=[[1,'1.To a very small extent'], [2,'2.To a small extent'], [3,'3.Neither small nor great extent'], [4,'4.To a great extent'], [5,'5.To a very great extent']],
        label='37e.Central government officials',
        widget=widgets.RadioSelect,
    )
    Trust_people_category6 = models.IntegerField(
        choices=[[1,'1.To a very small extent'], [2,'2.To a small extent'], [3,'3.Neither small nor great extent'], [4,'4.To a great extent'], [5,'5.To a very great extent']],
        label='37f.Police',
        widget=widgets.RadioSelect,
    )
    Trust_people_category7 = models.IntegerField(
        choices=[[1,'1.To a very small extent'], [2,'2.To a small extent'], [3,'3.Neither small nor great extent'], [4,'4.To a great extent'], [5,'5.To a very great extent']],
        label='37g.Teachers',
        widget=widgets.RadioSelect,
    )
    Trust_people_category8 = models.IntegerField(
        choices=[[1,'1.To a very small extent'], [2,'2.To a small extent'], [3,'3.Neither small nor great extent'], [4,'4.To a great extent'], [5,'5.To a very great extent']],
        label='37h.Nurses and doctors',
        widget=widgets.RadioSelect,
    )
    Trust_people_category9 = models.IntegerField(
        choices=[[1,'1.To a very small extent'], [2,'2.To a small extent'], [3,'3.Neither small nor great extent'], [4,'4.To a great extent'], [5,'5.To a very great extent']],
        label='37i.Strangers',
        widget=widgets.RadioSelect,
    )
    Level_trust_village = models.StringField(
        choices=['Gotten better', 'Gotten worse', 'Stayed about the same'],
        label='38.Do you think that over the last five years, the level of trust in this village/neighborhood has?',
        widget=widgets.RadioSelect,
    )
    People_village_help_other = models.IntegerField(
        choices=[[5,'5. Always helping'], [4,'4.Helping most of the time'], [3,'3. Helping sometimes'], [2,'2. Rarely helping'], [1,'1. Never helping']],
        label='39.How well do people in your village/neighborhood help each other out these days?, use a five point scale, where 1 means always helping and 5 means never helping',
        widget=widgets.RadioSelect,
    )
    Community_project = models.StringField(
        choices=['Time', 'Money'],
        label='40.If a community project does not directly benefit you, but has benefit for many others in the village/neighborhood, would you contribute time or money to the project',
        widget=widgets.RadioSelect,
    )
    Post_office = models.StringField(
        choices=['Less than 15 minutes', 'Between 15 and 30 minutes', 'Between 31 and 60 minutes', 'More than one hour'],
        label='41.How long does it take you to reach the nearest working post office',
        widget=widgets.RadioSelect,
    )
    Household_read_newspaper = models.IntegerField(
        label='42.How many times in the last month have you or anyone in your household read a newspaper or had one read to you?')
    Listen_radio = models.StringField(
        choices=['Every day', 'Few times a week', 'Once a week', 'Less than once a week', 'Never'],
        label='43.How often do you listen to the radio?',
        widget=widgets.RadioSelect,
    )
    Watch_television = models.StringField(
        choices=['Every day', 'Few times a week', 'Once a week', 'Less than a week', 'Never'],
        label='44.How often do you watch television?',
        widget=widgets.RadioSelect,
    )
    Nearest_working_telephone = models.StringField(
        choices=['Telephone in the house', 'Less than 15 minutes', 'Between 15 and 30 minutes', 'Between 31 and 60 minutes', 'More than 1 hour'],
        label='45.How long does it take you to get to the nearest working telephone?',
        widget=widgets.RadioSelect,
    )
    Made_received_phone_call = models.IntegerField(
        label='46.In the past month, how many times have you made or received a phone call?')
    Sources_of_information = models.StringField(
        choices=['Relatives, friends and neighbors', 'Community bulletin board', 'Local market', 'Community or local newspaper', 'National newspaper', 'Radio', 'Television', 'Groups or associations', 'Business or work associates', 'Political associates', 'Community leaders', 'An agent of the government', 'NGOs', 'Internet'],
        label='47.What are the three most important sources of information about what the government is doing (such as agricultural extension, workfare, family planning etc)?',
        widget=widgets.RadioSelect,
    )
    Sources_of_market_information = models.StringField(
        choices=['Relatives, friends and neighbors', 'Community bulletin board', 'Local market', 'Community or local newspaper', 'National newspaper', 'Radio', 'Television', 'Groups or associations', 'Business or work associates', 'Political associates', 'Community leaders', 'An agent of the government', 'NGOs', 'Internet'],
        label='48.What are the three most important sources of market information (such as jobs, prices of goods or crop)?',
        widget=widgets.RadioSelect,
    )
    Access_information = models.StringField(
        choices=['Improved', 'deteriorated', 'Stayed about the same'],
        label='49.In general, compared to five years ago, has access of information?',
        widget=widgets.RadioSelect,
    )
    House_accessible_road = models.StringField(
        choices=['All year long', 'Only during certain seasons', 'Never easily accessible'],
        label='50.What part of the year is your house easily accessible by road?',
        widget=widgets.RadioSelect,
    )
    Neighboring_village_town = models.IntegerField(
        label='51.How many times have you travelled to a neighboring village or town in the past 12 months?')

# FUNCTIONS
# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['Gender', 'Age', 'Ethnicity', 'Education', 'Marital_status' , 'Employment_status']


class Networks(Page):
    form_model = 'player'
    form_fields = ['Savings_Group', 'Household_participation', 'Household_belonging', 'Household_group_participation',
                   'Group_Member', 'Household_contribution', 'Household_work_days', 'Group_benefit', 'Household_access1',
                   'Household_access2','Group_members1', 'Group_members2', 'Same_members', 'Same_members2', 'Rich_poor_members',
                   'Group_Decision', 'Leadership_elections', 'Effective_leadership', 'Group_funding','Group_advice', 'Original_funder',
                   'Close_friends', 'Small_money', 'How_many_people', 'Economic_status', 'Other_reason', 'Neighborhood_trust',
                   'Emergency', 'People_assist', 'Personal_problem', 'People_trusted', 'Agree_disagree1', 'Agree_disagree2',
                   'Agree_disagree3', 'Agree_disagree4', 'Trust_people_category1', 'Trust_people_category2',
                   'Trust_people_category3', 'Trust_people_category4', 'Trust_people_category5', 'Trust_people_category6',
                   'Trust_people_category7', 'Trust_people_category8', 'Trust_people_category9', 'Level_trust_village',
                   'People_village_help_other', 'Community_project', 'Post_office', 'Household_read_newspaper',
                   'Listen_radio', 'Watch_television', 'Nearest_working_telephone', 'Made_received_phone_call',
                   'Sources_of_information', 'Sources_of_market_information', 'Access_information',
                   'House_accessible_road', 'Neighboring_village_town']


page_sequence = [Demographics, Networks]
