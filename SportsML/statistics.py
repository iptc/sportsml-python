#!/usr/bin/env python

import xml.etree.ElementTree as etree
import json

from .core import NEWSMLG2_NS, BaseObject, GenericArray
from .base_metadata import CommonAttributes, CoverageAttributes


class Statistic(BaseObject):
    # TODO
    pass


class Statistics(GenericArray):
    """
    Array of Statistic objects.
    """
    element_class = Statistic


class BaseStats(CommonAttributes):
    """
    The very basic stats type for persons and teams.
    Extended by base2stats and used directly by officalstats.
    """
    dict = {}
    ratings = None
    sports_properties = None
    stats = None

    def __init__(self, **kwargs):
        super(BaseStats, self).__init__(**kwargs)
        self.dict = {}
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            self.ratings = Ratings(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'rating')
            )
            self.sports_properties = Ratings(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'sports-property')
            )
            self.stats = GenericStats(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'stats')
            )

    def as_dict(self):
        super(BaseStats, self).as_dict()
        # self.dict.update({'dummyBaseStats': 'dummyValue'})
        if self.ratings:
            self.dict.update({ 'ratings': self.ratings.as_dict() })
        if self.sports_properties:
            self.dict.update({ 'sportsProperties': self.sports_properties.as_dict() })
        if self.stats:
            self.dict.update({ 'stats-BASESTATS': self.stats.as_dict() })
        return self.dict
        
    def __bool__(self):
        # FIXME return super(BaseStats, self).__bool__() or (self.ratings or self.sports_properties or self.stats) is not None
        return (self.ratings or self.sports_properties or self.stats) is not None


class GenericStatAttributes(BaseObject):
    """
    List of attributes used in generic stats
    """
    # The sport to which the stats belong.
    sport = None
    # The general classification of the stat within the sport eg ofensive, defensive, rebounding (basketball), special teams (american football).
    class_attr = None
    # The formal identifier of the kind of stat.
    stat_type = None
    # The formal type of the stat value eg. integer, string, etc.
    value_type = None
    # The value of the stat.
    value = None

    def __init__(self, **kwargs):
        super(GenericStatAttributes, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            self.sport = xmlelement.get('sport')
            self.class_attr = xmlelement.get('class')
            self.stat_type = xmlelement.get('stat-type')
            self.value_type = xmlelement.get('value-type')
            self.value = xmlelement.get('value')

    def as_dict(self):
        super(GenericStatAttributes, self).as_dict()
        if self.sport:
            self.dict.update({ 'sport': self.sport })
        if self.class_attr:
            self.dict.update({ 'class': self.class_attr })
        if self.stat_type:
            self.dict.update({ 'statType': self.stat_type })
        if self.value_type:
            self.dict.update({ 'valueType': self.value_type })
        if self.value:
            self.dict.update({ 'value': self.value })
        return self.dict


class GenericStat(GenericStatAttributes, CoverageAttributes):
    """
    A generic stat element that can be used together with or instead of
    more specific stat element and attributes. With nested stats the lower levels should
    be regarded as having the same value as their parents if that attribute is not
    specifically set.
    TODO implement this logic ^^ for nested stats
    """
    dict = {}
    # The name of the stat.
    # SportsML names are same as attribute names of stats in the sport-specific plugins.
    names = None
    stats = None

    def __init__(self, **kwargs):
        self.dict = {}
        super(GenericStat, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            from .entities import Names
            self.names = Names(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'name')
            )
            self.stats = GenericStats(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'stat')
            )

    def as_dict(self):
        super(GenericStat, self).as_dict()
        if self.names:
            self.dict.update({ 'names': self.names.as_dict() })
        if self.stats:
            self.dict.update({ 'stats-GENERICSTAT': self.stats.as_dict() })
        return self.dict

class GenericStats(GenericArray):
    """
    Array of GenericStat objects.
    """
    element_class = GenericStat


class OfficialStats(BaseStats):
    # inherits everything from BaseStats
    pass


class TeamStats(BaseObject):
    def __init__(self, xmlelement=None, **kwargs):
        if type(xmlelement) == etree.Element:
            # TODO
            pass

    def as_dict(self):
        # TODO
        return None


class TeamStatsSet(GenericArray):
    """
    Array of TeamStats objects.
    """
    element_class = TeamStats


class SubScores(BaseObject):
    # TODO
    pass

class EventRecords(BaseObject):
    # TODO
    pass

class Ratings(BaseObject):
    # TODO
    pass

class SportsProperties(BaseObject):
    # TODO
    pass

class StatsSet(BaseObject):
    # TODO
    pass

class OutcomeTotals(BaseObject):
    # TODO
    pass

class OutcomeResults(BaseObject):
    # TODO
    pass

class Base2Stats(BaseStats):
    """
    Second level stats. Extends baseStats. Extended further in base3stats and used directly in associate
    """
    outcome_totals = None
    outcome_results = None
    # Points accumulated by this associate.
    # For example, points earned by a NASCAR owner.
    points = None

    def __init__(self, **kwargs):
        super(Base2Stats, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            self.outcome_totals = OutcomeTotals(
                xmlelement = xmlelement.findall(NEWSMLG2_NS+'outcome-total')
            )
            self.outcome_results = OutcomeResults(
                xmlelement = xmlelement.findall(NEWSMLG2_NS+'outcome-result')
            )
            self.points = xmlelement.get('points')

    def as_dict(self):
        super(Base2Stats, self).as_dict()
        if self.outcome_totals:
            self.dict.update({ 'outcomeTotals': self.outcome_totals.as_dict() })
        if self.outcome_results:
            self.dict.update({ 'outcomeResults': self.outcome_results.as_dict() })
        if self.points:
            self.dict.update({ 'points': self.points })
        return self.dict


class PenaltyStats(BaseObject):
    # TODO
    pass


class PenaltyStatsSet(GenericArray):
    """
    Array of PenaltyStatsobjects.
    """
    element_class= PenaltyStats


class Ranks(BaseObject):
    # TODO
    pass


class StatAttributes(BaseObject):
    # TODO
    # Final or current score of the team or player.
    score = None
    # Final or current score of the opposing team or player.
    score_opposing = None
    # Average per-game score for the team or player.
    score_average = None
    # Average per-game score for the opposing team or player.
    score_opposing_average = None
    # Describes how the score and score-opposing is valued.
    # SportsML vocab uri: http://cv.iptc.org/newscodes/spscoreunits/
    score_units = None
    # The points or time behind the leading score.
    score_behind = None
    # Final or current number of attempts to score by a team or player. Example: in ice hockey, would represent total shots on goal.
    score_attempts = None
    # Final or current number of attempts to score by an opposing team or player.
    score_attempts_opposing = None
    # A subset of score-attempts. Only counts those attempts that were on-goal.
    score_attempts_on_goal = None
    # Final or current number of attempts to score by an opposing team or player that were on-goal.
    score_attempts_on_goal_opposing = None
    # Percentage of attempted scores that reached their mark.
    score_percentage = None
    # Percentage of attempted scores by opposing team or player that reached their mark.
    score_percentage_opposing = None
    # Describes the effect that the result of the event or rank changing
    # has had on the team. Example: Whether or not a team has qualified for the
    # playoffs, or has been promoted or demoted to a different division.
    # SportsML vocab uri: http://cv.iptc.org/newscodes/spresulteffect/
    result_effect = None
    # Whether the competitor won, lost, or tied.
    # SportsML vocab uri: http://cv.iptc.org/newscodes/speventoutcome/
    event_outcome = None
    # How many points were earned as a result of the outcome of this particular event.
    event_standing_points = None
    # How many points were deducted as a result of the outcome of this particular event.
    # This occurs, for example, in the German Handball leagues.
    event_standing_points_against = None
    # Qualifies "score" attribute.
    score_type = None
    # Number of sports-events the player has yet to participate in.
    events_remaining = None
    # Amount of time the team or player has possession of ball (or similar object like puck).
    time_of_possession = None
    # Amount of time the team or player has possession of ball (or similar object like puck) expressed as a percentage of the full time of the match.
    time_of_possession_percentage = None
    # Amount of time the opposing team or player has possession of ball (or similar object like puck) expressed as a percentage of the full time of the match.
    time_of_possession_percentage_opposing = None
    # Amount of time the team or player has possession of ball (or similar object like puck) per game.
    time_of_possession_average = None
    # Amount of time the opposing team or player has possession of ball (or similar object like puck) per game.
    time_of_possession_average_opposing = None
    # Number of events in a series won by team or player.
    series_score = None
    # Number of events in a series won by opposing team or player.
    series_score_opposing = None
    # The final score as adjusted by some authority. Usually as a result
    # of some dispute or transgression that must be settled post-event and rendered in
    # the score. Will differ from the regular score reflecting the number of actual
    # goals scored in play. Should be tested for before displaying actual
    # score.
    adjusted_score_for = None
    # The final score against as adjusted by some authority. Usually as
    # a result of some dispute or transgression that must be settled post-event and
    # rendered in the score. Will differ from the regular score reflecting the number
    # of actual goals scored in play. Should be tested for before displaying actual
    # score.
    adjusted_score_against = None

    def __init__(self, **kwargs):
        super(StatAttributes, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            self.score = xmlelement.get('score')
            self.score_opposing = xmlelement.get('score-opposing')
            self.score_average = xmlelement.get('score-average')
            self.score_opposing_average = xmlelement.get('score-opposing-average')
            self.score_units = xmlelement.get('score-units')
            self.score_behind = xmlelement.get('score-behind')
            self.score_attempts = xmlelement.get('score-attempts')
            self.score_attempts_opposing = xmlelement.get('score-attempts-opposing')
            self.score_attempts_on_goal = xmlelement.get('score-attempts-on-goal')
            self.score_attempts_on_goal_opposing = xmlelement.get('score-attempts-on-goal-opposing')
            self.score_percentage = xmlelement.get('score-percentage')
            self.score_percentage_opposing = xmlelement.get('score-percentage-opposing')
            self.result_effect = xmlelement.get('result-effect')
            self.event_outcome = xmlelement.get('event-outcome')
            self.event_standing_points = xmlelement.get('event-standing-points')
            self.event_standing_points_against = xmlelement.get('event-standing-points-against')
            self.score_type = xmlelement.get('score-type')
            self.events_remaining = xmlelement.get('events-remaining')
            self.time_of_possession = xmlelement.get('time-of-possession')
            self.time_of_possession_percentage = xmlelement.get('time-of-possession-percentage')
            self.time_of_possession_percentage_opposing = xmlelement.get('time-of-possession-percentage-opposing')
            self.time_of_possession_average = xmlelement.get('time-of-possession-average')
            self.time_of_possession_average_opposing = xmlelement.get('time-of-possession-average-opposing')
            self.series_score = xmlelement.get('series-score')
            self.series_score_opposing = xmlelement.get('series-score-opposing')
            self.adjusted_score_for = xmlelement.get('adjusted-score-for')
            self.adjusted_score_against = xmlelement.get('adjusted-score-against')

    def as_dict(self):
        super(StatAttributes, self).as_dict()
        if self.penalty_stats_set:
            self.dict.update({ 'penaltyStats': self.penalty_stats_set.as_dict() })
        if self.score:
            self.dict.update({ 'score': self.score })
        if self.score_opposing:
            self.dict.update({ 'scoreOpposing': self.score_opposing })
        if self.score_average:
            self.dict.update({ 'scoreAverage': self.score_average })
        if self.score_opposing_average:
            self.dict.update({ 'scoreOpposingAverage': self.score_opposing_average })
        if self.score_units:
            self.dict.update({ 'scoreUnits': self.score_units })
        if self.score_behind:
            self.dict.update({ 'scoreBehind': self.score_behind })
        if self.score_attempts:
            self.dict.update({ 'scoreAttempts': self.score_attempts })
        if self.score_attempts_opposing:
            self.dict.update({ 'scoreAttemptsOpposing': self.score_attempts_opposing })
        if self.score_attempts_on_goal:
            self.dict.update({ 'scoreAttemptsOnGoal': self.score_attempts_on_goal })
        if self.score_attempts_on_goal_opposing:
            self.dict.update({ 'scoreAttemptsOnGoalOpposing': self.score_attempts_on_goal_opposing })
        if self.score_percentage:
            self.dict.update({ 'scorePercentage': self.score_percentage })
        if self.score_percentage_opposing:
            self.dict.update({ 'scorePercentageOpposing': self.score_percentage_opposing })
        if self.result_effect:
            self.dict.update({ 'resultEffect': self.result_effect })
        if self.event_outcome:
            self.dict.update({ 'eventOutcome': self.event_outcome })
        if self.event_standing_points:
            self.dict.update({ 'eventStandingPoints': self.event_standing_points })
        if self.event_standing_points_against:
            self.dict.update({ 'eventStandingPointsAgainst': self.event_standing_points_against })
        if self.score_type:
            self.dict.update({ 'scoreType': self.score_type })
        if self.events_remaining:
            self.dict.update({ 'eventsRemaining': self.events_remaining })
        if self.time_of_possession:
            self.dict.update({ 'timeOfPossession': self.time_of_possession })
        if self.time_of_possession_percentage:
            self.dict.update({ 'timeOfPossessionPercentage': self.time_of_possession_percentage })
        if self.time_of_possession_percentage_opposing:
            self.dict.update({ 'timeOfPossessionPercentageOpposing': self.time_of_possession_percentage_opposing })
        if self.time_of_possession_average:
            self.dict.update({ 'timeOfPossessionAverage': self.time_of_possession_average })
        if self.time_of_possession_average_opposing:
            self.dict.update({ 'timeOfPossessionAverageOpposing': self.time_of_possession_average_opposing })
        if self.series_score:
            self.dict.update({ 'seriesScore': self.series_score })
        if self.series_score_opposing:
            self.dict.update({ 'seriesScoreOpposing': self.series_score_opposing })
        if self.adjusted_score_for:
            self.dict.update({ 'adjustedScoreFor': self.adjusted_score_for })
        if self.adjusted_score_against:
            self.dict.update({ 'adjustedScoreAgainst': self.adjusted_score_against })
        return self.dict

class Base3Stats(Base2Stats, CoverageAttributes, StatAttributes):
    """
    Extends base2stats. Further extended in genericEntitystats. Used directly by groupStats
    """
    penalty_stats_set = None
    awards = None
    ranks = None

    def __init__(self, **kwargs):
        super(Base3Stats, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            self.penalty_stats_set = PenaltyStatsSet(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'penalty-stats')
            )
            from .sports_events import Awards
            self.awards = Awards(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'award')
            )
            self.ranks = Ranks(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'rank')
            )
            self.points = xmlelement.get('points')

    def as_dict(self):
        super(Base3Stats, self).as_dict()
        if self.penalty_stats_set:
            self.dict.update({ 'penaltyStats': self.penalty_stats_set.as_dict() })
        if self.awards:
            self.dict.update({ 'awards': self.awards.as_dict() })
        if self.ranks:
            self.dict.update({ 'ranks': self.ranks.as_dict() })
        return self.dict



class BaseGenericEntityStats(Base3Stats):
    """
    Statistics that apply to a team as a whole or a player.
    Not all stats are used in every sport.
    """
    sub_scores = None
    event_records = None
    # The number of sports-events in which this team or player has already participated.
    events_played = None
    # Value for the amount of time played by the team or player over the
    # course of a particular time-span, such as a season.
    time_played_total = None
    
    def __init__(self, **kwargs):
        super(BaseGenericEntityStats, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            self.sub_scores = SubScores(
                xmlelement = xmlelement.findall(NEWSMLG2_NS+'sub-score')
            )
            self.event_records = EventRecords(
                xmlelement = xmlelement.findall(NEWSMLG2_NS+'event-record')
            )
            self.events_played = xmlelement.get('events-played')
            self.time_played_total = xmlelement.get('time-played-total')

    def as_dict(self):
        super(BaseGenericEntityStats, self).as_dict()
        if self.sub_scores:
            self.dict.update({'subScores': self.sub_scores.as_dict()})
        if self.event_records:
            self.dict.update({'eventRecords': self.event_records.as_dict() })
        if self.events_played:
            self.dict.update({'eventsPlayed': self.events_played})
        if self.time_played_total:
            self.dict.update({'timePlayedTotal': self.time_played_total})
        return self.dict


class BasePlayerStats(BaseGenericEntityStats):
    """
    Statistics that capture how a player has performed.
    Generally changes over the course of a sports-event.
    """
    # Value for the amount of time played by this player in a particular sports-event.
    time_played_event = None
    # Value for the average amount of time played per-event by the player over the course of a particular time-span, such as a season.
    time_played_event_average = None
    # Number of sports-events the player has played in since the start of the event.
    events_started = None
    # Exact universal time player entered event. For example, the time a downhill skiier began a run.
    date_time_entered = None
    # Exact universal time player exited event. For example, the time a downhill skiier finished a run.
    date_time_exited = None
    # Time player entered event expressed as conventional game-clock time. For example, the game minute a soccer player was subbed on to the field.
    event_time_entered = None
    # Time player exited event expressed as conventional game-clock time. For example, the game minute a soccer player was subbed off the field.
    event_time_exited = None

    def __init__(self, **kwargs):
        super(BasePlayerStats, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            self.time_played_event = xmlelement.get('time-played-event')
            self.time_played_event_average = xmlelement.get('time-played-event-average')
            self.events_started = xmlelement.get('events-started')
            self.date_time_entered = xmlelement.get('date-time-entered')
            self.date_time_exited = xmlelement.get('date-time-exited')
            self.event_time_entered = xmlelement.get('event-time-entered')
            self.event_time_exited = xmlelement.get('event-time-exited')

    def as_dict(self):
        super(BasePlayerStats, self).as_dict()
        self.dict.update({'dummyBasePlayerStats': 'dummy value'})
        if self.time_played_event:
            self.dict.update({ 'timePlayedEvent': self.time_played_event })
        if self.time_played_event_average:
            self.dict.update({ 'timePlayedEventAverage': self.time_played_event_average })
        if self.events_started:
            self.dict.update({ 'eventsStarted': self.events_started })
        if self.date_time_entered:
            self.dict.update({ 'dateTimeEntered': self.date_time_entered })
        if self.date_time_exited:
            self.dict.update({ 'dateTimeExited': self.date_time_exited })
        if self.event_time_entered:
            self.dict.update({ 'eventTimeEntered': self.event_time_entered })
        if self.event_time_exited:
            self.dict.update({ 'eventTimeExited': self.event_time_exited })
        return self.dict


class PlayerStats(BasePlayerStats):
    dict = {}

    def __init__(self, **kwargs):
        self.dict = {}
        super(PlayerStats, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            pass

    """
    TODO: sport-specific player stats
                <xs:choice minOccurs="0">
                    <xs:element name="player-stats-american-football" type="americanFootballPlayerStatsComplexType"/>
                    <xs:element name="player-stats-baseball" type="baseballPlayerStatsComplexType"/>
                    <xs:element name="player-stats-basketball"  type="basketballPlayerStatsComplexType"/>
                    <xs:element name="player-stats-golf" type="golfPlayerStatsComplexType"/>
                    <xs:element name="player-stats-ice-hockey" type="iceHockeyPlayerStatsComplexType"/>
                    <xs:element name="player-stats-soccer" type="soccerPlayerStatsComplexType"/>
                    <xs:element name="player-stats-tennis" type="tennisPlayerStatsComplexType"/>
                    <xs:element name="player-stats-motor-racing" type="motorRacingPlayerStatsComplexType"/>
                    <xs:element name="player-stats-curling" type="curlingPlayerStatsComplexType"/>
                    <xs:element name="player-stats-rugby" type="rugbyPlayerStatsComplexType"/>
                    <!-- element ref="player-stats-alpineskiing" / -->
                </xs:choice>

    """
    def as_dict(self):
        super(PlayerStats, self).as_dict()
        return self.dict


class PlayerStatsSet(GenericArray):
    """
    Array of PlayerStats objects.
    """
    element_class = PlayerStats


class WageringStats(BaseObject):
    def __init__(self, xmlelement=None, **kwargs):
        if type(xmlelement) == etree.Element:
            # TODO
            pass

    def as_dict(self):
        # TODO
        return None


class WageringStatsSet(GenericArray):
    """
    Array of WageringStats objects.
    """
    element_class = WageringStats



