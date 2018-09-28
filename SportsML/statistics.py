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
    ratings = None
    sports_properties = None
    stats = None

    def __init__(self, **kwargs):
        super(BaseStats, self).__init__(**kwargs)
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
        if self.ratings:
            self.dict.update({ 'ratings': self.ratings.as_dict() })
        if self.sports_properties:
            self.dict.update({ 'sportsProperties': self.sports_properties.as_dict() })
        if self.stats:
            self.dict.update({ 'stats': self.stats.as_dict() })
        return self.dict
        
    def __bool__(self):
        # FIXME return super(BaseStats, self).__bool__() or (self.ratings or self.sports_properties or self.stats) is not None
        return (self.ratings or self.sports_properties or self.stats) is not None


class GenericStatAttributes(BaseObject):
    """
    List of attributes used in generic stats
    """
    attributes = {
        # The sport to which the stats belong.
        'sport': 'sport',
        # The general classification of the stat within the sport eg ofensive, defensive, rebounding (basketball), special teams (american football).
        'class': 'class',
        # The formal identifier of the kind of stat.
        'stat-type': 'statType',
        # The formal type of the stat value eg. integer, string, etc.
        'value-type': 'valueType',
        # The value of the stat.
        'value': 'value'
    }


class GenericStat(GenericStatAttributes, CoverageAttributes):
    """
    A generic stat element that can be used together with or instead of
    more specific stat element and attributes. With nested stats the lower levels should
    be regarded as having the same value as their parents if that attribute is not
    specifically set.
    TODO implement this logic ^^ for nested stats
    """
    # dict = {}
    # The name of the stat.
    # SportsML names are same as attribute names of stats in the sport-specific plugins.
    names = None
    stats = None

    def __init__(self, **kwargs):
        # self.dict = {}
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
            self.dict.update({ 'stats': self.stats.as_dict() })
        return self.dict


class GenericStats(GenericArray):
    """
    Array of GenericStat objects.
    """
    element_class = GenericStat


class OfficialStats(BaseStats):
    # inherits everything from BaseStats
    pass


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
    attributes = {
        # Points accumulated by this associate.
        # For example, points earned by a NASCAR owner.
        'points': 'points'
    }

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

    def as_dict(self):
        super(Base2Stats, self).as_dict()
        if self.outcome_totals:
            self.dict.update({ 'outcomeTotals': self.outcome_totals.as_dict() })
        if self.outcome_results:
            self.dict.update({ 'outcomeResults': self.outcome_results.as_dict() })
        return self.dict


class PenaltyStats(CommonAttributes):
    """
    Statistics that detail the number of each type of penalty.
    Can be recorded for either a team or a player.
    """
    attributes = {
        # Could be a numeric value like 2, 5 or 10 for ice hockey, or yellow-card or red-card for soccer etc.
        'type': 'type',
        # The number of that type of penalities for this team or player.
        'count': 'count',
        # Amount penalized. Eg. total minutes (ice-hockey, lacrosse, etc.) or yards (american-football).
        'value': 'value'
    }
    

class PenaltyStatsSet(GenericArray):
    """
    Array of PenaltyStatsobjects.
    """
    element_class= PenaltyStats


class Ranks(BaseObject):
    # TODO
    pass


class StatAttributes(BaseObject):
    attributes = {
        # Final or current score of the team or player.
        'score': 'score',
        # Final or current score of the opposing team or player.
        'score_opposing': 'scoreOpposing',
        # Average per-game score for the team or player.
        'score_average': 'scoreAverage',
        # Average per-game score for the opposing team or player.
        'score_opposing_average': 'scoreOpposingAverage',
        # Describes how the score and score-opposing is valued.
        # SportsML vocab uri: http://cv.iptc.org/newscodes/spscoreunits/
        'score_units': 'scoreUnits',
        # The points or time behind the leading score.
        'score_behind': 'scoreBehind',
        # Final or current number of attempts to score by a team or player. Example: in ice hockey, would represent total shots on goal.
        'score_attempts': 'scoreAttempts',
        # Final or current number of attempts to score by an opposing team or player.
        'score_attempts_opposing': 'scoreAttemptsOpposing',
        # A subset of score-attempts. Only counts those attempts that were on-goal.
        'score_attempts_on_goal': 'scoreAttemptsOnGoal',
        # Final or current number of attempts to score by an opposing team or player that were on-goal.
        'score_attempts_on_goal_opposing': 'scoreAttemptsOnGoalOpposing',
        # Percentage of attempted scores that reached their mark.
        'score_percentage': 'scorePercentage',
        # Percentage of attempted scores by opposing team or player that reached their mark.
        'score_percentage_opposing': 'scorePercentageOpposing',
        # Describes the effect that the result of the event or rank changing
        # has had on the team. Example: Whether or not a team has qualified for the
        # playoffs, or has been promoted or demoted to a different division.
        # SportsML vocab uri: http://cv.iptc.org/newscodes/spresulteffect/
        'result_effect': 'resultEffect',
        # Whether the competitor won, lost, or tied.
        # SportsML vocab uri: http://cv.iptc.org/newscodes/speventoutcome/
        'event_outcome': 'eventOutcome',
        # How many points were earned as a result of the outcome of this particular event.
        'event_standing_points': 'eventStandingPoints',
        # How many points were deducted as a result of the outcome of this particular event.
        # This occurs, for example, in the German Handball leagues.
        'event_standing_points_against': 'eventStandingPointsAgainst',
        # Qualifies "score" attribute.
        'score_type': 'scoreType',
        # Number of sports-events the player has yet to participate in.
        'events_remaining': 'eventsRemaining',
        # Amount of time the team or player has possession of ball (or similar object like puck).
        'time_of_possession': 'timeOfPossession',
        # Amount of time the team or player has possession of ball (or similar object like puck) expressed as a percentage of the full time of the match.
        'time_of_possession_percentage': 'timeOfPossessionPercentage',
        # Amount of time the opposing team or player has possession of ball (or similar object like puck) expressed as a percentage of the full time of the match.
        'time_of_possession_percentage_opposing': 'timeOfPossessionPercentageOpposing',
        # Amount of time the team or player has possession of ball (or similar object like puck) per game.
        'time_of_possession_average': 'timeOfPossessionAverage',
        # Amount of time the opposing team or player has possession of ball (or similar object like puck) per game.
        'time_of_possession_average_opposing': 'timeOfPossessionAverageOpposing',
        # Number of events in a series won by team or player.
        'series_score': 'seriesScore',
        # Number of events in a series won by opposing team or player.
        'series_score_opposing': 'seriesScoreOpposing',
        # The final score as adjusted by some authority. Usually as a result
        # of some dispute or transgression that must be settled post-event and rendered in
        # the score. Will differ from the regular score reflecting the number of actual
        # goals scored in play. Should be tested for before displaying actual
        # score.
        'adjusted_score_for': 'adjustedScoreFor',
        # The final score against as adjusted by some authority. Usually as
        # a result of some dispute or transgression that must be settled post-event and
        # rendered in the score. Will differ from the regular score reflecting the number
        # of actual goals scored in play. Should be tested for before displaying actual
        # score.
        'adjusted_score_against': 'adjustedScoreAgainst'
    }


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
    attributes = {
        # The number of sports-events in which this team or player has already participated.
        'events-played': 'eventsPlayed',
        # Value for the amount of time played by the team or player over the
        # course of a particular time-span, such as a season.
        'time-played-total': 'timePlayedTotal'
    }
    
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

    def as_dict(self):
        super(BaseGenericEntityStats, self).as_dict()
        if self.sub_scores:
            self.dict.update({'subScores': self.sub_scores.as_dict()})
        if self.event_records:
            self.dict.update({'eventRecords': self.event_records.as_dict() })
        return self.dict


class BaseTeamStats(BaseGenericEntityStats):
    """
    Statistics that apply to the team as a whole.
    Not all stats are used in every sport.
    """
    pass  # only inherits from BaseGenericEntityStats


class TeamStats(BaseTeamStats):
    """ TODO
        <xs:element name="team-stats-american-football" type="americanFootballTeamStatsComplexType"/>
        <xs:element name="team-stats-baseball" type="baseballTeamStatsComplexType"/>
        <xs:element name="team-stats-basketball" type="basketballTeamStatsComplexType"/>
        <xs:element name="team-stats-ice-hockey" type="iceHockeyTeamStatsComplexType"/>
        <xs:element name="team-stats-soccer" type="soccerTeamStatsComplexType"/>
        <xs:element name="team-stats-tennis" type="tennisTeamStatsComplexType"/>
        <xs:element name="team-stats-motor-racing" type="motorRacingTeamStatsComplexType"/>
        <xs:element name="team-stats-curling" type="curlingTeamStatsComplexType"/>
        <xs:element name="team-stats-rugby" type="rugbyTeamStatsComplexType"/>
    """
    pass

class TeamStatsSet(GenericArray):
    """
    Array of TeamStats objects.
    """
    element_class = TeamStats


class BasePlayerStats(BaseGenericEntityStats):
    """
    Statistics that capture how a player has performed.
    Generally changes over the course of a sports-event.
    """
    attributes = {
        # Value for the amount of time played by this player in a particular sports-event.
        'time-played-event': 'timePlayed',
        # Value for the average amount of time played per-event by the player over the course of a particular time-span, such as a season.
        'time-played-event-average': 'timePlayedEventAverage',
        # Number of sports-events the player has played in since the start of the event.
        'events-started': 'eventsStandard',
        # Exact universal time player entered event. For example, the time a downhill skiier began a run.
        'date-time-entered': 'dateTimeEntered',
        # Exact universal time player exited event. For example, the time a downhill skiier finished a run.
        'date-time-exited': 'dateTimeExited',
        # Time player entered event expressed as conventional game-clock time. For example, the game minute a soccer player was subbed on to the field.
        'event-time-entered': 'eventTimeEntered',
        # Time player exited event expressed as conventional game-clock time. For example, the game minute a soccer player was subbed off the field.
        'event-time-exited': 'eventTimeExited'
    }


class PlayerStats(BasePlayerStats):

    def __init__(self, **kwargs):
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
    def __init__(self, **kwargs):
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
